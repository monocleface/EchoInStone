from abc import ABC, abstractmethod

class AudioTranscriberInterface(ABC):
    @abstractmethod
    def transcribe(self, audio_path: str) -> tuple:
        """Transcribes audio from a given file path.

        Args:
            audio_path (str): Path to the audio file to transcribe.

        Returns:
            tuple: A tuple containing the transcription text and timestamps.
        """
        pass
