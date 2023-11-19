try:
    from pytube import YouTube
    import os
    import signal
except ModuleNotFoundError:
    print("Please install pytube, signal, and os modules.")


def getURL() -> str:
    # url input from user
    link = input("Enter the URL of the video you want to download: \n>> ")
    print(f"Correct URL? {link}")
    if input("Y/N: ").lower() == "y":
        return link
    return getURL()


def extractVideo(link: str):
    # extract not only audio
    try:
        yt = YouTube(link)
    except:
        print("Video is unavailable or link is invalid.\nTry Again.")
        link = getURL()
        return extractVideo(link)
    videos = yt.streams.filter(file_extension='mp4', progressive=True)
    return videos


def getSaveDirectory():
    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    destination = input(">> ")
    if destination == "":
        destination = os.getcwd()
    if os.path.isdir(destination):
        print(f"Confirm destination: {destination}")
        if input("Y/N: ").lower() == "y":
            return destination
        else:
            return getSaveDirectory()
    else:
        print(f"Directory {destination} does not exist.")
        return getSaveDirectory()


def startDownload(all_videos, dest):
    # download the file
    single_video = all_videos.get_highest_resolution()
    out_file = single_video.download(output_path=dest)
    return single_video, out_file


def confirmSuccess(yt, output):
    # result of success
    print(f"{yt.title} has been successfully downloaded to {output}.")


def handler(signum, frame):
    print("Download cancelled.")


signal.signal(signal.SIGINT, handler)

def showTips():
    print("YouTube Downloader-Ian Chen, 11/18/2023")
    print("Press Ctrl+C to cancel download.")
    print("--------------------------------------------------")
    print()

if __name__ == "__main__":
    showTips()
    url = getURL()
    all_videos = extractVideo(url)
    save_directory = getSaveDirectory()
    video, output_file = startDownload(all_videos, save_directory)
    confirmSuccess(video, output_file)
