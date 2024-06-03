class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add(self, other):
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes

        if total_minutes >= 60:
            total_hours += total_minutes // 60
            total_minutes %= 60

        return Time(total_hours, total_minutes)

    def display(self):
        print("Time:", self.hours, "hours", self.minutes, "minutes")


time1 = Time(2, 30)
time2 = Time(1, 45)
result = time1.add(time2)
result.display()
