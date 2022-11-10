# constants
LANE_SIZE = 100
LANE_CAR_LIST = []

FREE = 0
OCCUPIED = 1


class Car:
    def __init__(self, current_position, speed):
        self.current_position = current_position
        self.speed = speed

    def __str__(self):
        print("[position=", self.current_position, ", speed=", self.speed, end="]")


def create_lane():
    return [FREE for i in range(LANE_SIZE)]


def print_lane(lane):
    print("---------- Lane ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in range(LANE_SIZE):
        if i == 0:
            print("Start |", end="")
        value = lane[i]
        if value == FREE:
            print(" ", end="")
        if value == OCCUPIED:
            print("M", end="")
        print("|", end="")
    print(" End")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for car in LANE_CAR_LIST:
        car.__str__()
        print(", ", end="")
    print()
    print()


def insert_car(lane, car_list):
    for car in car_list:
        lane[car.current_position] = OCCUPIED
        LANE_CAR_LIST.append(car)


def step(lane):
    updated_lane = lane.copy()

    # loop through lane
    for i in range(LANE_SIZE):
        # if occupied, drive the car to the next cell according to its speed
        #   -> if new position occupied, go back till there is a free cell
        if lane[i] == OCCUPIED:
            for car in LANE_CAR_LIST:
                if i == car.current_position:
                    updated_lane = drive_to_next_position(lane, updated_lane, car)
        # if free, continue loop
        if lane[i] == FREE:
            continue

    return updated_lane


def drive_to_next_position(lane, updated_lane, car):
    # if occupied, drive the car to the next cell according to its speed
    #   -> if new position occupied, go back till there is a free cell

    best_pos = car.current_position + car.speed
    available_pos = car.current_position

    for i in range(car.current_position+1, best_pos+1):
        # if i > 99: 100 => 0, 101 => 1, etc.
        i = i % LANE_SIZE
        best_pos = best_pos % LANE_SIZE

        if lane[i] == FREE:
            available_pos = i
        if lane[i] == OCCUPIED:
            updated_lane[car.current_position] = FREE
            car.current_position = available_pos
            updated_lane[available_pos] = OCCUPIED
            break
        if i == best_pos:
            updated_lane[car.current_position] = FREE
            car.current_position = available_pos
            updated_lane[available_pos] = OCCUPIED

    return updated_lane


if __name__ == '__main__':

    lane = create_lane()
    print_lane(lane)

    car1 = Car(4, 1)
    car2 = Car(15, 0)
    car3 = Car(44, 5)
    car4 = Car(55, 3)
    car5 = Car(77, 4)

    index_list = [car1, car2, car3, car4, car5]

    insert_car(lane, index_list)
    print_lane(lane)

    for i in range(20):
        lane = step(lane)
        print(i)
        print_lane(lane)


