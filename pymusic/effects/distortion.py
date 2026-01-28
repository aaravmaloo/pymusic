import numpy as np
from scipy import signal

class Distortion:
    def __init__(self, drive: float = 1.0, type: str = "soft"):
        self.drive = drive
        self.type = type

    def process(self, data: np.ndarray) -> np.ndarray:
        driven = data * self.drive
        if self.type == "soft":
            return np.tanh(driven)
        else:
            return np.clip(driven, -1.0, 1.0)

class Reverb:
    def __init__(self, room_size: float = 0.5, damping: float = 0.5):
        self.room_size = room_size
        self.damping = damping

    def process(self, data: np.ndarray, sample_rate: int) -> np.ndarray:
        delay_samples = int(0.05 * sample_rate)
        if len(data) <= delay_samples: return data
        
        out = np.copy(data)
        out[delay_samples:] += data[:-delay_samples] * self.room_size
        return out / (1.0 + self.room_size)
