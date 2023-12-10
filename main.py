import argparse
from pytube import YouTube
from colorama import *
from moviepy.editor import *
from hurry.filesize import verbose, size
from tqdm import tqdm


def makeVidFolder():
    folder_name = "videos"
    folder_path = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        pass
    if not os.path.exists(os.path.join(os.getcwd(), 'audio')):
        os.makedirs(os.path.join(os.getcwd(), 'audio'))
    else:
        pass

def downloadVideo(url, format, debug):
    makeVidFolder()
    folder_video = os.path.join(os.getcwd(), 'videos')
    folder_audio = os.path.join(os.getcwd(), 'audio')
    try:
        def progress_function(chunk, file_handle, bytes_remaining):
            current = ((total_size - bytes_remaining) / total_size)
            percent = int(current * 100)
            with tqdm(total=100, desc="Downloading", unit="%", position=0, leave=True) as pbar:
                pbar.update(percent - pbar.n)

        yt = YouTube(url, on_progress_callback=progress_function)
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
        print(f'{Fore.LIGHTYELLOW_EX}YTDownloader{Fore.RESET} will be downloading: {Fore.LIGHTCYAN_EX}{size(total_size, system=verbose)}{Fore.RESET}')
        print(f'{Fore.LIGHTCYAN_EX}Writing file.{Fore.RESET}')
        if format == "mp3":
            video_stream.download(output_path=folder_video)
            video = VideoFileClip(f"{folder_video}\\{yt.title}.mp4")
            print(f'{Fore.LIGHTCYAN_EX}Writing .mp3 file.{Fore.RESET}')
            video.audio.write_audiofile(f"{folder_audio}\\{yt.title}.mp3", verbose=False, logger=None)
            if debug:
                print(video_stream.get_file_path())
            print(f"{Fore.LIGHTGREEN_EX}Conversion and download complete.")
        else:
            video_stream.download(output_path=folder_video)
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
