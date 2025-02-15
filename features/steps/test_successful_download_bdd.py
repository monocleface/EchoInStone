
import os
from pytest_bdd import scenarios, given, when, then
from EchoInStone.capture.downloader_factory import get_downloader


# Load the scenario from .feature file
# This function loads BDD scenarios defined in the specified feature file for testing successful downloads.
scenarios('../successful_download.feature')

# Shared variables
# Global variables to store the URL being tested, the selected downloader, the output directory,
# and the path of the downloaded file.
url = ""
downloader = None
output_dir = 'test_output'
downloaded_file_path = ""

@given('the URL is a valid YouTube URL')
def youtube_url():
    global url
    # Set the URL to a valid YouTube video URL for testing purposes.
    url = 'https://www.youtube.com/watch?v=plZRCMx_Jd8'

@given('the URL is a valid Podcast URL')
def podcast_url():
    global url
    # Set the URL to a valid podcast feed URL for testing purposes.
    url = 'https://radiofrance-podcast.net/podcast09/rss_13957.xml'

@given('the URL is a valid MP3 URL')
def mp3_url():
    global url
    # Set the URL to a direct MP3 file URL for testing purposes.
    url = 'https://media.radiofrance-podcast.net/podcast09/25425-13.02.2025-ITEMA_24028677-2025C53905E0006-NET_MFC_D378B90D-D570-44E9-AB5A-F0CC63B05A14-21.mp3'

@when('the file is downloaded')
def download_file():
    global downloader, url, output_dir, downloaded_file_path
    # Select the appropriate downloader based on the URL and download the file.
    downloader = get_downloader(url, output_dir=output_dir)
    downloaded_file_path = downloader.download(url)
    # Verify that the download method returns a valid file path.
    assert downloaded_file_path is not None, "The download method should return the file path"

@then('the download should be successful')
def check_download_success():
    # Verify that the file has been successfully downloaded by checking its existence.
    assert os.path.exists(downloaded_file_path), f"File {downloaded_file_path} does not exist"
