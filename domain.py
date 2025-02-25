class Measurement:
    """
    This class represents a measurement taken from a sensor.
    """

    def __init__(self, timestamp, value, unit):
        self.timestamp = timestamp
        self.value = value
        self.unit = unit

class Level:

    def __init__(self, number, size=0):
        self.number = number
        self.size = size
        self.rooms = []

class Rom:

    def __init__(self, name, size, floor):
        
        self.name = name
        self.size = size
        self.floor = floor  
        self.devices = []


class Device:

    def __init__(self, id, name, producer, unit, description_name):
        self.id = id
        self.name = name
        self.producer = producer
        self.unit = unit
        self.description_name = description_name

class Actuator(Device):

    def __init__(self, type, state, id, name, producer, unit, description_name):
        super().__init__(id, name, producer, unit, description_name)
        self.type = type
        self.state = state

class Sensor(Device):
    def __init__(self, type, value, id, name, unit, producer, description_name):
        super().__init__(id, name, producer, unit, description_name)
        self.type = type
        self.value = value


class SmartHouse:
    """
    This class serves as the main entity and entry point for the SmartHouse system app.
    Do not delete this class nor its predefined methods since other parts of the
    application may depend on it (you are free to add as many new methods as you like, though).

    The SmartHouse class provides functionality to register rooms and floors (i.e. changing the 
    house's physical layout) as well as register and modify smart devices and their state.
    """

    def __init__(self):
        self.floors = []  
        self.rooms = []   




    def register_floor(self, level):
        """
        This method registers a new floor at the given level in the house
        and returns the respective floor object.
        """
        new_floor = Level(level, 0)
        self.floors.append(new_floor)
        return new_floor

    def register_room(self, floor, room_size, room_name = None):
        """
        This methods registers a new room with the given room areal size 
        at the given floor. Optionally the room may be assigned a mnemonic name.
        """
        new_room = Rom(room_name, room_size, floor)
        floor.rooms.append(new_room)  # Add room to the floor
        self.rooms.append(new_room)  # Track all rooms in the house
        return new_room


    def get_floors(self):
        """
        This method returns the list of registered floors in the house.
        The list is ordered by the floor levels, e.g. if the house has 
        registered a basement (level=0), a ground floor (level=1) and a first floor 
        (leve=1), then the resulting list contains these three flors in the above order.
        """
        return sorted(self.floors, key=lambda floor: floor.number)


    def get_rooms(self):
        """
        This methods returns the list of all registered rooms in the house.
        The resulting list has no particular order.
        """
        return self.rooms


    def get_area(self):
        """
        This methods return the total area size of the house, i.e. the sum of the area sizes of each room in the house.
        """
        return sum(room.size for room in self.rooms)


    def register_device(self, room, device):
        """
        This methods registers a given device in a given room.
        """
        pass

    
    def get_device(self, device_id):
        """
        This method retrieves a device object via its id.
        """
        pass

