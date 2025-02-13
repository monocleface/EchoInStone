from EchoInStone.utils import configure_logging
import logging
from EchoInStone.processing import AudioProcessingOrchestrator, WhisperAudioTranscriber, PyannoteDiarizer, SpeakerAligner
from EchoInStone.capture import YouTubeDownloader
from EchoInStone.utils import DataSaver
from EchoInStone.utils import timer, log_time

# Configure logging
configure_logging(logging.DEBUG)
logger = logging.getLogger(__name__)

# Constants
#ECHO_INPUT = 'https://www.youtube.com/watch?v=ipXG9iQq-Tw'
ECHO_INPUT = 'https://www.youtube.com/watch?v=plZRCMx_Jd8'
TRANSCRIBE_OUTPUT = 'speaker_transcriptions.json'

@timer
def main():
    """
    Main function to orchestrate the audio processing pipeline.
    """
    # Initialize components
    downloader = YouTubeDownloader(output_dir="results")
    transcriber = WhisperAudioTranscriber()
    diarizer = PyannoteDiarizer()
    aligner = SpeakerAligner()
    data_saver = DataSaver(output_dir="results")

    # Create an instance of AudioProcessingOrchestrator
    orchestrator = AudioProcessingOrchestrator(downloader, transcriber, diarizer, aligner, data_saver)

    # Process YouTube URL
    logger.info("Starting transcription process...")
    speaker_transcriptions = orchestrator.extract_and_transcribe(ECHO_INPUT)
    if speaker_transcriptions:
        # Save the results to a file
        data_saver.save_data(TRANSCRIBE_OUTPUT, speaker_transcriptions)

        logger.info(f"Transcriptions have been saved to {TRANSCRIBE_OUTPUT}")

        # Display the results
        for speaker, start_time, end_time, segment_text in speaker_transcriptions:
            logger.info(f"Speaker {speaker} ({start_time:.2f}s to {end_time:.2f}s): {segment_text}")
    else:
        logger.warning("No transcriptions were generated.")

if __name__ == "__main__":
    main()
