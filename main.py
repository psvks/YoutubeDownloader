import argparse
from pytube import YouTube
from colorama import *
from moviepy.editor import *
import os
import time
import math


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


def downloadVideo(url, format, debug):
    try:
        yt = YouTube(url)
        if format == "mp4":
            video_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        elif format == "only_audio":
            video_stream = yt.streams.filter(only_audio=True).first()
        elif format == "mp3":
            video_stream = yt.streams.filter(file_extension='mp4').first()
        else:
            print("Invalid format. Use: 'ytdownloader.exe https://youtube.com/watch?v=1hdAAZzgCuk mp4' or 'ytdownloader.exe https://youtube.com/watch?v=1hdAAZzgCuk only_audio'")
            return
        video_title = yt.title
        download_path = f"{video_title}.{video_stream.subtype}"
        total_size = video_stream.filesize
        print(f'{Fore.LIGHTYELLOW_EX}YTDownloader{Fore.RESET} will be downloading: {Fore.LIGHTCYAN_EX}{convert_size(total_size)}{Fore.RESET}')
        print(f'{Fore.LIGHTCYAN_EX}Writing file.{Fore.RESET}')
        if format == "mp3":
            video_stream.download()
            video = VideoFileClip(f"{yt.title}.mp4")
            video.audio.write_audiofile(f"{yt.title}.mp3", verbose=False)
            if debug:
                print(video_stream.get_file_path())
            print(f"{Fore.LIGHTGREEN_EX}Conversion and download complete.")
        else:
            video_stream.download()
            print(f'{Fore.LIGHTGREEN_EX}Download complete.')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download youtube videos")
    parser.add_argument("url", help="URL of the youtube video")
    parser.add_argument("format", choices=["mp4", "only_audio", "mp3"], help="Format. ('mp4', 'only_audio', 'mp3')")
    parser.add_argument("--debug", action='store_true', help="Returns were the MP3 or MP4 is. (For servers or other things.)")
    args = parser.parse_args()
    downloadVideo(args.url, args.format, args.debug)
