try:
    import tkinter as tk
    from tkinter import filedialog
    from pytube import YouTube
    from pytube.cli import on_progress
    import os
    import signal
except ModuleNotFoundError:
    print("Please install tkinter, pytube, signal, and os modules.")
    exit()


class Downloader:
    """
    A class that downloads YouTube videos.
    """
    DEFAULT_SAVE_LOCATION = f"{os.getcwd()}/Downloads"

    def __init__(self):
        self._url = None
        self._yt = None
        self._video = None
        self._save_directory = None
        self._output_file = None

    def start(self) -> None:
        self.show_tips()
        self.get_url()
        self.extract_video()
        self.get_save_directory()
        self.start_download()
        self.confirm_success()

    def get_url(self) -> None:
        link = input("Enter the URL of the video you want to download: \n>> ")
        print(f"Correct URL? {link}")
        if input("Y/N: ").lower().strip() == "y":
            self._url = link
        else:
            self.get_url()

    def extract_video(self) -> None:
        try:
            yt = YouTube(self._url)
            print("Please wait...")
            self._yt = yt
            self._video = self._yt.streams.filter(file_extension='mp4').get_highest_resolution()
        except Exception:
            print("Video is unavailable or Link is invalid.")
            print("Try Again.")
            self.get_url()
            self.extract_video()

    def get_save_directory(self) -> None:
        if not os.path.isdir(self.DEFAULT_SAVE_LOCATION):
            os.mkdir(self.DEFAULT_SAVE_LOCATION)
        root = tk.Tk()
        root.withdraw()
        destination = filedialog.askdirectory()
        if destination == "":
            print("No directory selected.")
            print(f"Using default directory: {self.DEFAULT_SAVE_LOCATION}")
        elif os.path.isdir(destination):
            print(f"Confirm destination: {destination}")
            if input("Y/N: ").lower().strip() == "y":
                self._save_directory = destination
            else:
                self.get_save_directory()
        else:
            print(f"Directory {destination} does not exist.")
            self.get_save_directory()

    def start_download(self) -> None:
        print("Downloading...")
        out_file = self._video.download(output_path=self._save_directory)
        self._output_file = out_file

    def confirm_success(self) -> None:
        print(f"{self._video.title} has been successfully downloaded to {self._output_file}.\n")

    def show_tips(self) -> None:
        print("YouTube Downloader-Ian Chen.")
        print("Last updated 01/08/2024.")
        print("Press Ctrl+C to cancel download.")
        print("--------------------------------------------------\n")


signal.signal(signal.SIGINT, signal.SIG_DFL)
downloader = Downloader()
while True:
    downloader.start()
    if input("Press y to download another video.").lower().strip() != "y":
        break
