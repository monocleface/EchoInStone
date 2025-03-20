from abc import ABC, abstractmethod

class DownloaderInterface(ABC):
    @abstractmethod
    def download(self, url: str) -> str:
        """Downloads a file from a URL or source path.

        Args:
            url (str): URL or source path of the file to download.
            output_path (str): Destination path to save the downloaded file.

        Returns:
            bool: True if the download was successful, False otherwise.
        """
        pass

    @abstractmethod
    def validate_url(self, url: str) -> bool:
        """Validates if a URL is valid for this downloader.

        Args:
            url (str): URL to validate.

        Returns:
            bool: True if the URL is valid, False otherwise.
        """
        pass
