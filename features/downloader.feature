Feature: Downloader Selection
  As a user
  I want the correct downloader to be selected
  So that I can download different types of audio files

  Scenario: Select YouTube downloader
    Given the URL is a YouTube URL
    When the downloader is selected
    Then the YouTube downloader should be returned

  Scenario: Select Podcast downloader
    Given the URL is a Podcast URL
    When the downloader is selected
    Then the Podcast downloader should be returned

  Scenario: Select Audio downloader
    Given the URL is an MP3 URL
    When the downloader is selected
    Then the Audio downloader should be returned
