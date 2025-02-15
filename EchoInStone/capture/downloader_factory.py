from .podcast_downloader import PodcastDownloader
from .youtube_downloader import YouTubeDownloader
from .audio_downloader import AudioDownloader
from .downloader_interface import DownloaderInterface

def get_downloader(url: str, output_dir: str) -> DownloaderInterface:
    """
    Determine the appropriate downloader based on the URL.
    """
    if "youtube.com" in url or "youtu.be" in url:
        return YouTubeDownloader(output_dir=output_dir)
    elif url.endswith(".xml"):
        return PodcastDownloader(output_dir=output_dir)
    elif url.endswith(".mp3") or url.endswith(".wav"):
        return AudioDownloader(output_dir=output_dir)
    else:
        raise ValueError("Unsupported URL format")