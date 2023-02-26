import time
import random
import numpy as np

class Elevator:
    """
    Elevator class : represents a single elevator
    It can do following:
    1. Move up and down.
    2. Represented by lift_number
    3. Decides which direction to move based on service_list and on_floor
    4. on_floor property denotes currently is on floor.
    5. open and close door.
    6. Start moving and stop moving
    """
    def __init__(self, lift_number, floor_min, floor_max, on_floor = 0):
        self.lift_number = lift_number
        self.is_operational = True
        self.floor_max = floor_max
        self.floor_min = floor_min
        self.is_selected = False
        self.is_running = False
        self.on_floor = on_floor
        self.direction = 1
        self.is_overload = False
        self.service_list = []

    from elevator.helpers.move import move_one_step

    from elevator.helpers.execute import execute_request

    # prints the current status
    def current_status(self):
        print("lift {} is currently @ floor {}".format(self.lift_number, self.on_floor))
        print("lift {} running status {} ".format(self.lift_number, self.is_running))

    # open door
    def open_door(self):
        print("lift {} door opening".format(self.lift_number))
        self.door_open = True

    # close door
    def close_door(self):
        print("lift {} door closing".format(self.lift_number))
        self.door_open = False

    def calculate_service_in_directions(self):
        """
        Creates 2 list from a single service list
        service_in_up_direction - contains all the floor number which are above
        service_in_down_direction - all floor which are below
        """
        self.service_list = np.sort(self.service_list)
        service_in_up_direction = list(self.service_list[self.service_list > self.on_floor])
        service_in_down_direction = list(self.service_list[self.service_list < self.on_floor])
        service_in_down_direction = service_in_down_direction[::-1]
        return service_in_up_direction, service_in_down_direction

    