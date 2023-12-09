from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = 'static'
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# Index
@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None

    if request.method == 'POST':
        url = request.form['url']

        try:
            # Crear objeto YouTube
            yt = YouTube(url)
            video = yt.streams.get_highest_resolution()
            video_path = os.path.join(app.config['DOWNLOAD_FOLDER'])
            video.download(output_path=app.config['DOWNLOAD_FOLDER'])
            video_url = url_for('static', filename=yt.title + '.mp4')
        except Exception as e:
            error_message = f"Ocurrió un error: {e}"
            return render_template('index.html', error_message=error_message, video_url=video_url)

    return render_template('index.html', video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)
