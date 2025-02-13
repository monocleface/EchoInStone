from abc import ABC, abstractmethod

class DiarizerInterface(ABC):
    @abstractmethod
    def diarize(self, audio_path: str):
        """Performs speaker diarization on the given audio file.

        Args:
            audio_path (str): Path to the audio file to diarize.

        Returns:
            Diarization result or None if diarization fails.
        """
        pass
