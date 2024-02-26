class Time:

    max_hour = 23
    max_minute = 59
    max_seconds = 59

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def get_time(self):
        return f"{self.hour}:{self.minute}:{self}"

    def next_second(self):
        if self.second == Time.max_seconds:
            self.second = 00
            if self.minute == Time.max_minute:
                self.minute += 00
                if self.hour == Time.max_hour:
                    self.hour = 00
        else:
            self.second += 1
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())

