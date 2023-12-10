# YouTube Downloader
This project is a YouTube video downloader created with Python, utilizing the `PyTube` library.  
**NOTE**: This project will be supported in case bugs arise or new features are required. I cannot guarantee that I will continue with this project in the future.
**NOTE**: You need FFMPEG to convert the files to .mp3

## Requirements
Ensure you have Python 3.12.0 installed on your system. To install the necessary libraries, run the following command:    

```bash
pip install -r requirements.txt
```  
### Usage
To download a video, run the following command:  
`python main.py <urltoyoutube> <format>`  
Replace `<urltoyoutube>` with the URL of the YouTube video you want to download and `<format>` with the desired format (mp4 or mp3).  

## Executable Tutorial
Follow these steps to create and use the executable:  

### Install Requirements:
Ensure you have Python 3.12.0 installed, and then run the following command to install the required libraries:  
`pip install -r requirements.txt`  

### Compile the Executable:
Open the Build file in the source code and edit it to include your file path. For example:  
```pyinstaller --noconfirm --onefile --console "C:/Users/usr/Documents/GitHub/YoutubeDownloader/main.py"```  
### Run the Executable:
Open a CMD terminal, navigate to the directory containing your executable, and execute the following command:  
`main.exe <urltoyoutube> <format>`  
Replace `<urltoyoutube>` with the YouTube video URL and `<format>` with the desired format (mp4 or mp3).  
