from abc import ABC, abstractmethod

class AlignerInterface(ABC):
    @abstractmethod
    def align(self, transcription, timestamps, diarization):
        """
        Aligns the transcription with timestamps and speaker diarization.

        :param transcription: The complete text of the transcription.
        :param timestamps: List of text segments with their corresponding timestamps.
        :param diarization: List of diarization segments with speaker identifiers.
        :return: List of aligned segments with speaker identifiers and timestamps.
        """
        pass
