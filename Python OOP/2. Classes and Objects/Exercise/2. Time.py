# Create a class called Time. Upon initialization, it should receive hours, minutes, and seconds (integers). The class should also have class attributes max_hours equal to 23, max_minutes equal to 59, and max_seconds equal to 59. You should also create 3 additional instance methods:
# ⦁	set_time(hours, minutes, seconds) - updates the time with the new values
# ⦁	get_time() - returns "{hh}:{mm}:{ss}"
# ⦁	next_second() - updates the time with one second (use the class attributes for validation) and returns the new time (use the get_time() method)

# Test Code:
# time = Time(9, 30, 59)
# print(time.next_second())

# Desired Output:
# 09:31:00


# Test Code:
# time = Time(9, 30, 59)
# print(time.next_second())

# Desired Output:
# 11:00:00


# Test Code:
# time = Time(9, 30, 59)
# print(time.next_second())

# Desired Output:
# 00:00:00

class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{int(self.hours):02d}:{int(self.minutes):02d}:{int(self.seconds):02d}"

    def next_second(self):
        self.seconds = self.increment_min_sec(str(self.seconds))
        if self.seconds == "00":
            self.minutes = self.increment_min_sec(str(self.minutes))
            if self.minutes == "00":
                self.hours = self.increment_hours(str(self.hours))
        return self.get_time()

    def increment_min_sec(self, string: str):
        string = int(string) + 1

        if string > self.max_seconds:
            string = "00"
            return string

        return str(string)

    def increment_hours(self, string: str):
        string = int(string) + 1

        if string > self.max_hours:
            string = "00"
            return string

        return str(string)

