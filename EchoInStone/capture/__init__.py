# capture/__init__.py

from .downloader_interface import DownloaderInterface
from .youtube_downloader import YouTubeDownloader
from .podcast_downloader import PodcastDownloader
from .audio_downloader import AudioDownloader

__all__ = [
    'DownloaderInterface',
    'YouTubeDownloader',
    'PodcastDownloader',
    'AudioDownloader'
]
