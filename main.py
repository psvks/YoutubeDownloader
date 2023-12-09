import argparse
from pytube import YouTube
from colorama import *

def download_video(url, format):
    try:
        yt = YouTube(url)
        if format == "mp4":
            video_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        elif format == "only_audio":
            video_stream = yt.streams.filter(only_audio=True).first()
        else:
            print("Invalid format. Use: 'ytdownloader.exe https://youtube.com/watch?v=1hdAAZzgCuk mp4' or 'ytdownloader.exe https://youtube.com/watch?v=1hdAAZzgCuk only_audio'")
            return
        video_title = yt.title
        download_path = f"{video_title}.{video_stream.subtype}"
        total_size = video_stream.filesize
        print(f'YTDownloader will be downloading: {Fore.LIGHTCYAN_EX}{total_size}{Fore.RESET} bytes')
        video_stream.download()
        print("Download complete.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Descargar videos de YouTube.")
    parser.add_argument("url", help="URL del video de YouTube")
    parser.add_argument("format", choices=["mp4", "only_audio"], help="Formato de salida ('mp4' o 'mp3')")
    args = parser.parse_args()
    download_video(args.url, args.format)
