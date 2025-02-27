from domain import SmartHouse

DEMO_HOUSE = SmartHouse()

# Building house structure

#Floors
ground_floor = DEMO_HOUSE.register_floor(1)
second_floor = DEMO_HOUSE.register_floor(2)

#Rooms
entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
living_room = DEMO_HOUSE.register_room(ground_floor, 25.0, "Living Room")

#Devices
motion_sensor = DEMO_HOUSE.register_device("cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5", "NebulaGuard Innovations", "MoveZ Detect 69", "Motion Sensor", "sensor", living_room, )
bulp = DEMO_HOUSE.register_device("6b1c5f6b-37f6-4e3d-9145-1cfbe2f1fc28", "Elysian Tech", "Lumina Glow 4000", "Light Bulp", "actuator", living_room)
termostat = DEMO_HOUSE.register_device("4d8b1d62-7921-4917-9b70-bbd31f6e2e8e", "Elko", "ZigBee Plus", "Thermostat", "sensor", living_room)
heat_pump = DEMO_HOUSE.register_device("5e13cabc-5c58-4bb3-82a2-3039e4480a6d", "Panasonic", "flagship", "Heat Pump", "actuator", living_room)


# TODO: continue registering the remaining floor, rooms and devices

