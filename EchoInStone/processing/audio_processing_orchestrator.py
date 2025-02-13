from ..capture import DownloaderInterface
from .audio_transcriber_interface import AudioTranscriberInterface
from .diarizer_interface import DiarizerInterface
from ..utils import DataSaver
from .aligner_interface import AlignerInterface

import logging

logger = logging.getLogger(__name__)

class AudioProcessingOrchestrator:
    def __init__(self, downloader: DownloaderInterface,
                       transcriber: AudioTranscriberInterface,
                       diarizer: DiarizerInterface,
                       aligner: AlignerInterface,
                       saver: DataSaver,):
        self.downloader = downloader
        self.transcriber = transcriber
        self.diarizer = diarizer
        self.aligner = aligner
        self.saver = saver

    def extract_and_transcribe(self, echo_input: str):
        logger.debug("Downloading audio...")
        audio_path = self.downloader.download(echo_input)
        if audio_path:
            logger.debug("Transcribing downloaded audio...")
            transcription, timestamps = self.transcriber.transcribe(audio_path)
            logger.debug("Diarizing downloaded audio...")
            diarization = self.diarizer.diarize(audio_path)

            if logger.isEnabledFor(logging.DEBUG):
                logger.debug("Writing debug files.")
                self.saver.save_data("audio_transcription.txt", transcription)
                self.saver.save_data("audio_timestamps.json", timestamps)
                self.saver.save_data("audio_diarization.txt", str(diarization))

            return self.aligner.align(transcription, timestamps, diarization)
        return None
