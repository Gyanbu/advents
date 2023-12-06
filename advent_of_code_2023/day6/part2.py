data = (63789468, 411127420471035)
# data = (71530, 940200) # test_data

class Car:
    def __init__(self, race_duration, record):
        self.race_duration = race_duration
        self.record = record

    def wind_up(self, time):
        speed = time
        distance = (self.race_duration - time) * speed
        return distance

    def how_many_new_records(self):
        start_index = 0
        end_index = 0
        for i in range(1, self.race_duration):
            if self.wind_up(i) > self.record:
                start_index = i
                break

        for i in range(self.race_duration - 1, 1, -1):
            if self.wind_up(i) > self.record:
                end_index = i
                break

        return end_index - start_index + 1



car = Car(data[0], data[1])
answer = car.how_many_new_records()
print(answer)
