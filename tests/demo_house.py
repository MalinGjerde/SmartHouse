from smarthouse.domain import SmartHouse

DEMO_HOUSE = SmartHouse()

# Building house structure
ground_floor = DEMO_HOUSE.register_floor(1)
second_floor = DEMO_HOUSE.register_floor(2)

entrance = DEMO_HOUSE.register_room(ground_floor, 13.5, "Entrance")
living_room = DEMO_HOUSE.register_room(ground_floor, 25.0, "Living Room")
bathroom1 = DEMO_HOUSE.register_room(ground_floor, 6.3, "Bathroom 1")
guest_room1 = DEMO_HOUSE.register_room(ground_floor, 8, "Guest Room 1")
garage = DEMO_HOUSE.register_room(ground_floor, 19, "Garage")

office = DEMO_HOUSE.register_room(second_floor, 11.75, "Office")
bathroom2 = DEMO_HOUSE.register_room(second_floor, 9.25, "Bathroom 2")
guest_room2 = DEMO_HOUSE.register_room(second_floor, 8, "Guest Room 2")
guest_room3 = DEMO_HOUSE.register_room(second_floor, 10, "Guest Room 3")
dressing_room = DEMO_HOUSE.register_room(second_floor, 4, "Dressing Room")
master_bedroom = DEMO_HOUSE.register_room(second_floor, 17, "Master Bedroom")
hallway = DEMO_HOUSE.register_room(second_floor, 10, "Hallway")


#Devices

smart_lock = DEMO_HOUSE.register_device(entrance,"Guardian Lock 7000","4d5f1ac6-906a-4fd1-b4bf-3a0671e4c4f1", "MythicalTech", "Smart Lock", "actuator" )
co2_sensor = DEMO_HOUSE.register_device(living_room,"Smoke Warden 1000","8a43b2d7-e8d3-4f3d-b832-7dbf37bf629e", "ElysianTech", "CO2 sensor", "sensor" )
electricity_meter = DEMO_HOUSE.register_device(entrance,"Volt Watch Elite","a2f8690f-2b3a-43cd-90b8-9deea98b42a7", "MysticEnergy Innovations", "Electricity Meter", "sensor" )
heat_pump = DEMO_HOUSE.register_device(living_room, "Thermo Smart 6000", "5e13cabc-5c58-4bb3-82a2-3039e4480a6d", "ElysianTech", "Heat Pump", "actuator", )
motion_sensor = DEMO_HOUSE.register_device(living_room,"MoveZ Detect 69","cd5be4e8-0e6b-4cb5-a21f-819d06cf5fc5", "NebulaGuard Innovations", "Motion Sensor", "sensor" )
humidity_sensor = DEMO_HOUSE.register_device(bathroom1,"Aqua Alert 800","3d87e5c0-8716-4b0b-9c67-087eaaed7b45", "AetherCorp", "Humidity Sensor", "sensor" )
smart_oven = DEMO_HOUSE.register_device(guest_room1,"Pheonix HEAT 333","8d4e4c98-21a9-4d1e-bf18-523285ad90f6", "AetherCorp", "Smart Oven", "actuator" )
automatic_garage_door = DEMO_HOUSE.register_device(garage,"Guardian Lock 9000","9a54c1ec-0cb5-45a7-b20d-2a7349f1b132", "MythicalTech", "Automatic Garage Door", "actuator" )
smart_oven2 = DEMO_HOUSE.register_device(master_bedroom,"Ember Heat 3000","c1e8fa9c-4b8d-487a-a1a5-2b148ee9d2d1", "IgnisTech Solutions", "Smart Oven", "actuator" )
temperature_sensor = DEMO_HOUSE.register_device(master_bedroom, "SmartTemp 42", "4d8b1d62-7921-4917-9b70-bbd31f6e2e8e", "AetherCorp", "Temperature Sensor", "sensor" )
air_quality_sensor = DEMO_HOUSE.register_device(guest_room3, "AeroGuard Pro", "7c6e35e1-2d8b-4d81-a586-5d01a03bb02c", "CelestialSense Technologies", "Air Quality Sensor", "sensor" )
smart_plug = DEMO_HOUSE.register_device(office, "FlowState X", "1a66c3d6-22b2-446e-bf5c-eb5b9d1a8c79", "MysticEnergy Innovations", "Smart Plug", "actuator" )
dehumidifier = DEMO_HOUSE.register_device(bathroom2, "Hydra Dry 8000", "9e5b8274-4e77-4e4e-80d2-b40d648ea02a", "ArcaneTech Solutions", "Smart Plug", "actuator" )
bulp = DEMO_HOUSE.register_device(guest_room2, "Lumina Glow 4000","6b1c5f6b-37f6-4e3d-9145-1cfbe2f1fc28", "Elysian Tech", "Light Bulp", "actuator" )




# TODO: continue registering the remaining floor, rooms and devices

