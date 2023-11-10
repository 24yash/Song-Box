#while submitting you can skip the audios folder (>10 mb) and during viva add it back!
import os
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/audios'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///music.sqlite3"
app.app_context().push()
db = SQLAlchemy(app)

class Song(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  filename = db.Column(db.String(255), nullable=False)

def create_tables():
  db.create_all()

@app.route('/')
def index():
  return redirect(url_for('upload'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
  if request.method == 'POST':
    file = request.files['file']
    if file:
      filename = file.filename
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

      song = Song(filename=filename)
      db.session.add(song)
      db.session.commit()
      return redirect(url_for('upload'))
    else:
      return "No file uploaded", 400
  return render_template('upload.html', songs=Song.query.all())

@app.route('/play')
def play():
  return render_template('play.html', songs=Song.query.all())

if __name__ == '__main__':
  create_tables()
  app.run(host='0.0.0.0', port=80)