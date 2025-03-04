# Automated Transcription System

## Overview
This project is an automated transcription system that monitors a specified directory for audio and video files. It transcribes both newly added and existing media files using OpenAI's Whisper model and saves the transcription as a text file.

## Features
- Automatically transcribes both existing and newly added audio/video files in the monitored directory.
- Supports multiple file formats: MP3, WAV, MP4, MKV, MOV, FLV, AAC, and M4A.
- Uses Whisper's "base" model for transcription.
- Saves transcriptions as `.txt` files alongside the original media files.

## Prerequisites
Ensure you have the following installed:
- Python 3.7+
- pip

## Installation
1. Clone this repository or download the script.
2. Install the required dependencies:
   ```sh
   pip install openai-whisper watchdog
   ```
3. (Optional) Install FFmpeg if not already installed (required for some media formats):
   ```sh
   sudo apt update && sudo apt install ffmpeg  # For Ubuntu
   brew install ffmpeg  # For macOS
   choco install ffmpeg  # For Windows (using Chocolatey)
   ```

## Usage
1. Modify the `directory_to_monitor` variable in the script to the folder you want to monitor.
2. Run the script:
   ```sh
   python script.py
   ```
3. The script will:
   - Transcribe all existing media files in the directory.
   - Monitor the directory for new media files and transcribe them in real time.

## How It Works
1. The script processes all existing media files in the specified directory and transcribes them.
2. A file system observer continuously watches for newly added media files.
3. When a new file is detected, it is automatically transcribed, and the output is saved as a `.txt` file in the same directory.

## Example Output
If a file named `audio.mp3` is processed, a corresponding `audio.txt` file will be created with the transcription.

## Customization
- Change the Whisper model by modifying the line:
  ```python
  model = whisper.load_model("base")
  ```
  Available models: `tiny`, `base`, `small`, `medium`, `large`.
- Modify `SUPPORTED_FORMATS` to add or remove supported file types.


## Acknowledgments
- OpenAI Whisper for speech-to-text transcription.
- Watchdog for file system monitoring.

---
Enjoy automated transcriptions with ease!
