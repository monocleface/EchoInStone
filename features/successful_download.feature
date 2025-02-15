Feature: Successful Download
  As a user
  I want to download files successfully
  So that I can process them further

  Scenario: Successful YouTube download
    Given the URL is a valid YouTube URL
    When the file is downloaded
    Then the download should be successful
