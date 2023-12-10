from flask import Flask, render_template, request, send_from_directory
from pytube import YouTube
import os
from moviepy.editor import *
import shutil
import automaticDel

app = Flask(__name__)

VIDEO_DIR = 'static'
if not os.path.exists(VIDEO_DIR):
    os.makedirs(VIDEO_DIR)

def delete_static_contents():
    static_path = 'static'
    if os.path.exists(static_path):
        for filename in os.listdir(static_path):
            file_path = os.path.join(static_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Fail {file_path}: {e}')
    else:
        print('The folder does not exist.')





@app.route('/video', methods=['GET'])
def video():
    video_id = request.args.get('id')
    video_path = os.path.join(VIDEO_DIR, f'{video_id}.mp4')
    destination = os.path.join(VIDEO_DIR)
    if not os.path.exists(video_path):
        youtube_url = f'https://www.youtube.com/watch?v={video_id}'
        download_video(youtube_url, destination, video_id)

    video_filename = os.path.basename(video_path)
    return render_template('video.html', video_filename=video_filename)


@app.route('/audio', methods=['GET'])
def audio():
    video_id = request.args.get('id')
    audio_path = os.path.join(VIDEO_DIR, f'{video_id}.mp3')
    video_path = os.path.join(VIDEO_DIR, f'{video_id}.mp4')
    destination = os.path.join(VIDEO_DIR)
    if not os.path.exists(video_path):
        youtube_url = f'https://www.youtube.com/watch?v={video_id}'
        download_video(youtube_url, destination, video_id)
        if not os.path.exists(audio_path):
            convert_mp3(video_path=video_path, destination=destination, id=video_id)
    else:
        if not os.path.exists(audio_path):
            convert_mp3(video_path=video_path, destination=destination, id=video_id)
    
    audio_filename = os.path.basename(audio_path)
    return render_template('audio.html', audio_filename=audio_filename)

def download_video(url, output_path, id):
    yt = YouTube(url)
    video_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
    video_stream.download(output_path, filename=f'{id}.mp4')


def convert_mp3(video_path, destination, id):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(f"{destination}\\{id}.mp3", verbose=False, logger=None)

@app.route('/videos/<filename>')
def uploaded_file(filename):
    return send_from_directory(VIDEO_DIR, filename)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/license')
def license():
    return render_template("license.html")

if __name__ == '__main__':
    app.run(debug=True)
