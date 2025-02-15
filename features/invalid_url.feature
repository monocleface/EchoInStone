Feature: Invalid URL Handling
  As a user
  I want the system to handle invalid URLs gracefully
  So that I can be informed of errors without crashing the application

  Scenario: Invalid URL format
    Given the URL is an invalid format
    When the downloader is selected
    Then an exception should be raised
