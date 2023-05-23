# yt2audio

## Start

Clone this repository and navigate to the corresponding directory. Inside this folder you have to start a terminal window and type:

    python gui.py

or

    python3 gui.py

If any errors occur, you should install the requirements described below.


## Install Requirements

To install the dependencies, type:

    pip install -r requirements.txt

## Error Handlink

Update the repository:

    git pull

and run the repair script:

    bash repair_script.sh

Furthermore, you need a ffmpeg player:

    https://stackoverflow.com/questions/30770155/ffprobe-or-avprobe-not-found-please-install-one

Create an issue at GitHub.

### Error log: `ModuleNotFoundError: No module named 'tkinter'`

    sudo apt-get install python3-tk

### Error log: `youtube_dl.utils.DownloadError: ERROR: ffprobe/avprobe and ffmpeg/avconv not found. Please install one.`

Make sure you have the latest version for youtube-dl:

    sudo youtube-dl -U

After that you can solve this problem by installing the missing ffmpeg.

Ubuntu and debian:

    sudo apt-get install ffmpeg

macOS:

    brew install ffmpeg

Windows:

    choco install ffmpeg

