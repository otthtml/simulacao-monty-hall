from random import randrange

class MontyHallProblem():
    def __init__(self) -> None:        
        self.distribution = [False, False, False] # True is where the car is
        self.choices = [False, False, False] # True is what we picked
        self.reveals = [False, False, False] # True is which door we picked
        self.cars_earned = 0

    def distribute(self):
        car = randrange(3)
        self.distribution[car] = True

    def pick_door(self):
        pick = randrange(3)
        self.choices[pick] = True

    def reveal_door(self):
        while True:
            door = randrange(3)
            if (self.choices[door] is False and self.distribution[door] is False):
                self.reveals[door] = True
                return

    def repick_unrevealed_door(self):
        for pos in range(3):
            if self.choices[pos] is False and self.reveals[pos] is False:
                self.choices = [False, False, False]
                self.choices[pos] = True
                return

    def compute_result(self) -> int:
        if self.choices == self.distribution:
            return 1
        else:
            return 0

    def scenario_1(self) -> int:
        self.distribute()
        self.pick_door()
        return self.compute_result()

    def scenario_2(self) -> int:
        self.distribute()
        self.pick_door()
        self.reveal_door()
        self.repick_unrevealed_door()
        return self.compute_result()        

if __name__ == '__main__':
    car_count = 0
    iterations = 100000
    for i in range(iterations):
        instance = MontyHallProblem()
        car_count += instance.scenario_1()
    print("\n Scenario 1:")
    print(f"You won {car_count} car(s)")
    print(f"Distribution {100*(car_count/iterations)}%")

    car_count = 0
    for i in range(iterations):
        instance = MontyHallProblem()
        car_count += instance.scenario_2()
    print("\n Scenario 2:")
    print(f"You won {car_count} car(s)")
    print(f"Distribution {100*(car_count/iterations)}%")
    