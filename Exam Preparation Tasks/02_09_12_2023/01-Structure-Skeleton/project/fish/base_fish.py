from abc import ABC, abstractmethod


class BaseFish(ABC):
    def __init__(self, name: str, points: float, time_to_catch: int) -> None:
        self.name = name
        self.points = points
        self.time_to_catch = time_to_catch

    @abstractmethod
    def fish_details(self):
        pass
