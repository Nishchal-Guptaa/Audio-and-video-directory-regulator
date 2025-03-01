import os
import time
import whisper
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

SUPPORTED_FORMATS = ('.mp3', '.wav', '.mp4', '.mkv', '.mov', '.flv', '.aac', '.m4a')

model = whisper.load_model("base") 

processed_files = set()

def transcribe_file(file_path):
    """Transcribe the audio/video file and save the transcription."""
    if file_path in processed_files:
        print(f"Skipping already processed file: {file_path}")
        return

    print(f"Transcribing file: {file_path}")
    result = model.transcribe(file_path)
    transcription = result['text']

    transcription_file = f"{os.path.splitext(file_path)[0]}.txt"
    with open(transcription_file, 'w') as f:
        f.write(transcription)

    processed_files.add(file_path)
    print(f"Transcription saved to: {transcription_file}")

class MediaFileHandler(FileSystemEventHandler):
    """Handles file system events."""
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(SUPPORTED_FORMATS):
            transcribe_file(event.src_path)

def process_existing_files(directory):
    """Process all existing media files in the specified directory and its subdirectories."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(SUPPORTED_FORMATS):
                file_path = os.path.join(root, filename)
                transcribe_file(file_path)

def monitor_directory(directory):
    """Monitor the specified directory for new media files."""
    event_handler = MediaFileHandler()
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()
    print(f"Monitoring directory: {directory}")

    try:
        while True:
            time.sleep(1)  
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    directory_to_monitor = r"C:\Users\nishc\Desktop\testDir"
    
    process_existing_files(directory_to_monitor)
    
    monitor_directory(directory_to_monitor)