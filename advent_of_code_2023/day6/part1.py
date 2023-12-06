data = [(63, 411), (78, 1274), (94, 2047), (68, 1035)]
# test_data = [(7, 9), (15, 40), (30, 200)] # test_data

class Car:
    def __init__(self, race_duration, record):
        self.race_duration = race_duration
        self.record = record

    def wind_up(self, time):
        speed = time
        distance = (self.race_duration - time) * speed
        return distance

    def how_many_new_records(self):
        result = 0
        for i in range(1, self.race_duration - 1):
            if self.wind_up(i) > self.record:
                result += 1
        return result


answer = 1
for race in data:
    car = Car(race[0], race[1])
    answer *= car.how_many_new_records()
print(answer)
