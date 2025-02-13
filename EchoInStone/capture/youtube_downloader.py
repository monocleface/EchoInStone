from pytubefix import YouTube
import os
import re
import logging
from pydub import AudioSegment
from ..capture import DownloaderInterface

logger = logging.getLogger(__name__)

class YouTubeDownloader(DownloaderInterface):
    def __init__(self, output_dir='data/videos'):
        """
        Initializes the YouTubeDownloader with a specified output directory.

        Args:
            output_dir (str): The directory where downloaded files will be saved.
        """
        self.output_dir = output_dir

    def download(self, url: str) -> str:
        """
        Downloads audio from a YouTube URL and converts it to WAV format.

        Args:
            url (str): YouTube URL to download audio from.

        Returns:
            str: Path to the saved WAV file if the download and conversion were successful, None otherwise.
        """
        try:
            yt = YouTube(url)
            video_stream = yt.streams.filter(only_audio=True).first()

            # Download the audio file
            audio_file = video_stream.download(output_path=self.output_dir)

            # Clean up the file name
            dir_path, base_name = os.path.split(audio_file)
            base, ext = os.path.splitext(base_name)
            safe_base = re.sub(r'[^\w\s-]', '', base).replace(' ', '_')
            new_file = os.path.join(dir_path, safe_base + '.mp3')
            os.rename(audio_file, new_file)

            # Convert the file to WAV
            audio = AudioSegment.from_file(new_file)
            wav_file = os.path.join(dir_path, safe_base + '.wav')
            audio.export(wav_file, format="wav")

            logger.info(f"Audio downloaded and converted to {wav_file}")
            return wav_file
        except Exception as e:
            logger.error(f"Error during download: {e}")
            return None

    def validate_url(self, url: str) -> bool:
        """
        Validates if a URL is a valid YouTube URL.

        Args:
            url (str): URL to validate.

        Returns:
            bool: True if the URL is a valid YouTube URL, False otherwise.
        """
        try:
            YouTube(url)
            return True
        except Exception:
            logger.warning(f"Invalid YouTube URL: {url}")
            return False
