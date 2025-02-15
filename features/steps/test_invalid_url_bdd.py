import pytest
from pytest_bdd import scenarios, given, when, then
from EchoInStone.capture.downloader_factory import get_downloader

# Load scenarios from the .feature file
# This function loads BDD scenarios defined in the specified feature file.
scenarios('../invalid_url.feature')

# Shared variables
# Global variable to store the URL being tested.
url = ""

@given('the URL is an invalid format')
def invalid_url():
    global url
    # Set the URL to an invalid format for testing purposes.
    url = 'invalid-url'

@when('the downloader is selected')
def select_downloader():
    # This step is a placeholder and does not perform any action.
    # It represents the action of selecting a downloader in the BDD scenario.
    pass

@then('an exception should be raised')
def check_exception():
    # Verify that a ValueError is raised when attempting to get a downloader for an invalid URL.
    # This ensures that the get_downloader function correctly handles invalid URLs.
    with pytest.raises(ValueError):
        get_downloader(url, output_dir='test_output')
