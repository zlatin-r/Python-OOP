from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):

    def __init__(self, name):
        super().__init__(name, 150)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength = (self.strength - 30) * 2.5

        if peak.difficulty_level == "Advanced":
            self.strength = (self.strength - 30) * 1.3

        self.conquered_peaks.append(peak)
