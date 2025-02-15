Feature: Transcription Output
  As a user
  I want to generate valid transcription output
  So that I can use it for further analysis

  Scenario: Valid transcription output
    Given the audio file is transcribed
    When the transcription is generated
    Then the output should be valid
