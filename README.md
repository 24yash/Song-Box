# Music Player Project

This project is a simple music player application developed using Flask, allowing users to upload and play audio files.

## Usage

### Uploading Songs

- Navigate to the home page.
- Click on the "Upload Songs" button.
- Choose an `.mp3` audio file to upload.

### Playing Songs

- Once uploaded, go to the "Play Songs" page.
- All uploaded songs will be listed with their names.
- Click on the play button to listen to any uploaded song.

**Note:** During submission, the `audios` folder (>10 MB) might be excluded. Add it back during presentations or viva.

## Project Structure

- `app.py`: Contains the Flask application setup and routes.
- `static/audios`: Folder to store uploaded audio files. (Note: Files larger than 10 MB might not be included for submission purposes.)
- `templates/`: Contains HTML templates for rendering the web pages.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Setup

1. **Clone Repository:**

```bash
   git clone https://github.com/24yash/Song-Box.git
```

2. **Install Dependencies:**

```bash
   pip install -r requirements.txt
```

3. **Run Application:**

```bash
   python app.py
```
