# EchoInStone

**EchoInStone** is a comprehensive audio processing tool designed to transcribe, diarize, and align speaker segments from audio files with a focus on achieving the most accurate and faithful transcription possible. It supports various audio sources, including YouTube videos and podcasts, and provides a flexible pipeline for processing audio data, prioritizing precision and reliability over speed.

## Features

- **Transcription**: Convert audio files into text using state-of-the-art automatic speech recognition (ASR) model, `Whisper Large v3 Turbo`.
- **Diarization**: Identify and separate different speakers in an audio file with the cutting-edge model, `Pyannote Speaker Diarization 3.1`.
- **Alignment**: Align transcribed text with the corresponding audio segments using a customized algorithm tailored to be highly efficient and faithful to the outputs of Whisper and Pyannote, `SpeakerAlignement`.
- **Flexible and Extensible Pipeline**: Easily integrate new models or processing steps into an orchestrated pipeline, `AudioProcessingOrchestrator`.

> Note: The current version of EchoInStone is a preliminary release and does not yet support passing parameters as command-line arguments. Future updates will include more flexible configuration options and enhanced functionality.

## Installation

### Prerequisites

- Python 3.11 or higher
- Poetry (dependency management tool)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jeanjerome/EchoInStone.git
   cd EchoInStone
   ```

2. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```

3. **Configure logging** (optional):
   - The logging configuration is set up to output logs to both the console and a file (`app.log`). You can modify the logging settings in `logging_config.py`.

4. **Configure Hugging Face Token**:

  - Add your Hugging Face token to this file. You can obtain a token by following these steps:
     1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens).
     2. Click on "New token".
     3. Copy the generated token and paste it into the `EchoInStone/config.py` file as shown below:

```textplain
# EchoInStone/config.py

# Hugging Face authentication token
HUGGING_FACE_TOKEN = "your_token_here"
```

## Usage

### Basic Example

To transcribe and diarize a YouTube video, you can run the following command:

```bash
poetry run python main.py
```

This will process the audio from the specified YouTube URL, transcribe it, perform speaker diarization, and save the results to a file.

### Customization

- **Audio Input**: Modify the `ECHO_INPUT` constant in `main.py` to point to the YouTube video you want to process [\*].
- **Output Directory**: Change the `output_dir` parameter in the `DataSaver` initialization to specify where the results should be saved.

> \* This is a preliminary release. Future updates will include more flexible configuration options and enhanced functionality.

## Configuration

### Logging

Logging is configured to output messages to both the console and a file (`app.log`). You can adjust the logging level and format in the `logging_config.py` file.

### Models

- **Transcription Model**: The default transcription model is `openai/whisper-large-v3-turbo`. You can change this by modifying the `model_name` parameter in the `WhisperAudioTranscriber` initialization.
- **Diarization Model**: The default diarization model is `pyannote/speaker-diarization-3.1`. You can change this by modifying the model loading code in the `PyannoteDiarizer` class.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source community for the various libraries and models used in this project.
- Special thanks to the contributors and maintainers of the models and tools that make this project possible.

## Contact

For any questions or suggestions, please open an issue.
