import os
import shutil
import logging
from pydub import AudioSegment
from . import DownloaderInterface

logger = logging.getLogger(__name__)

class AudioDownloader(DownloaderInterface):
    def __init__(self, output_dir='data/files'):
        """
        Initializes the AudioDownloader with a specified output directory.

        Args:
            output_dir (str): The directory where copied files will be saved.
        """
        self.output_dir = output_dir

    def download(self, file_path: str) -> str:
        """
        Copies an audio file from a local file path to the specified output path
        and converts it to WAV format for compatibility with PyAnnote.

        Args:
            file_path (str): Local file path to copy the file from.

        Returns:
            str: Absolute path to the copied and converted WAV file if successful, None otherwise.
        """
        try:
            # Ensure the output directory exists
            os.makedirs(self.output_dir, exist_ok=True)
            logger.debug(f"Output directory created or already exists: {self.output_dir}")

            # Get the file name from the file path
            file_name = os.path.basename(file_path)
            file_base, file_ext = os.path.splitext(file_name)
            destination_path = os.path.join(self.output_dir, file_name)

            # Copy the file to the destination path
            shutil.copy2(file_path, destination_path)
            logger.info(f"File copied to {destination_path}")
            
            # Always convert to WAV for PyAnnote compatibility
            audio = AudioSegment.from_file(destination_path)
            wav_file = os.path.join(self.output_dir, f"{file_base}.wav")
            audio.export(wav_file, format="wav")
            logger.info(f"File converted to WAV: {wav_file}")
            
            # Return the absolute path to the WAV file
            return os.path.abspath(wav_file)
        except Exception as e:
            logger.error(f"Error during file copy/conversion: {e}")
            return None

    def validate_url(self, file_path: str) -> bool:
        """
        Validates if a file path is valid and the file exists.

        Args:
            file_path (str): Local file path to validate.

        Returns:
            bool: True if the file path is valid and the file exists, False otherwise.
        """
        if os.path.isfile(file_path):
            logger.debug(f"File path is valid: {file_path}")
            return True
        else:
            logger.warning(f"Invalid file path: {file_path}")
            return False
