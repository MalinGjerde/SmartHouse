from pathlib import Path
import sys
sys.path.append(str(Path().parent.absolute()))
import sqlite3
from typing import Optional
from smarthouse.domain import Actuator, Sensor, ActuatorWithSensor, Device, Measurement, SmartHouse
from datetime import datetime

class SmartHouseRepository:
    """
    Provides the functionality to persist and load a _SmartHouse_ object 
    in a SQLite database.
    """

    def __init__(self, file: str) -> None:
        self.file = file 
        self.conn = sqlite3.connect(file, check_same_thread=False)

    def __del__(self):
        self.conn.close()

    def cursor(self) -> sqlite3.Cursor:
        """
        Provides a _raw_ SQLite cursor to interact with the database.
        When calling this method to obtain a cursors, you have to 
        rememeber calling `commit/rollback` and `close` yourself when
        you are done with issuing SQL commands.
        """
        return self.conn.cursor()
    
    def reconnect(self):
        self.conn.close()
        self.conn = sqlite3.connect(self.file)

    def load_smarthouse_deep(self):
        """
        Retrieves the SmartHouse object along with all rooms from the database.
        """
        house = SmartHouse()
        c = self.conn.cursor()
        

        
        c.execute("SELECT DISTINCT floor FROM rooms ORDER BY floor")
        floors = {}
        for (floor_level,) in c.fetchall():
            floor = house.register_floor(floor_level)
            floors[floor_level] = floor  

        
        rooms = {}
        c.execute("SELECT id, floor, area, name FROM rooms")
        for room_id, floor_level, room_size, room_name in c.fetchall():
            if floor_level in floors:
                room = house.register_room(floors[floor_level], room_size, room_name)
                rooms[room_id] = room  # Store rooms for device registration

        
        c.execute("SELECT id, room, kind, category, supplier, product FROM devices")
        for device_id, room_id, kind, category, supplier, product in c.fetchall():
            if room_id in rooms:
                
                if category.lower() == "actuator" and kind.lower() == 'heat pump':
                    device = ActuatorWithSensor(device_id, product, supplier, category, kind)
                    self.update_actuator_from_db(device)
                    

                elif category.lower() == "sensor":
                    device = Sensor(device_id, product, supplier, category, kind)
                elif category.lower() == "actuator":
                    device = Actuator(device_id, product, supplier, category, kind)
                    self.update_actuator_from_db(device)

                else:
                    device = Device(device_id, product, supplier, category)

                
                house.register_device(rooms[room_id], device)

        c.close()
        return house
    

    


    def get_latest_reading(self, device) -> Optional[Measurement]:
        """
        Retrieves the most recent sensor reading for the given sensor if available.
        Returns None if the given object has no sensor readings.
        """
        # TODO: After loading the smarthouse, continue here

        
        c = self.conn.cursor()

        
        c.execute("SELECT device, ts, value, unit FROM measurements")
        
        latest_time = None
        measurement = None
        for device_id, measurement_ts, Measurement_value, Measurement_unit in c.fetchall():
            
            if device_id == device.id:
                dt = datetime.strptime(measurement_ts, "%Y-%m-%d %H:%M:%S")
                
                if latest_time is None or dt > latest_time:
                    latest_time = dt
                    measurement = Measurement(measurement_ts,Measurement_value,Measurement_unit)    

        c.close()
        return measurement

    def update_actuator_from_db(self, device):
        c = self.conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='actuator'")
        if c.fetchone() is None:
            c.execute("CREATE TABLE actuator(id TEXT PRIMARY KEY, active BOOLEAN, value REAL)")

        c.execute("SELECT id FROM actuator WHERE id = ?", (device.id,))

        if c.fetchone() == None:
            c.execute("INSERT INTO actuator (id, active, value) VALUES (?, ?, ?)", (device.id, device.state, device.value))
        else:
            c.execute("SELECT id, active, value FROM actuator")
            for db_id, db_active, db_velue in c.fetchall():
                if db_id == device.id:
                    device.state = db_active
                    device.value = db_velue





    def update_actuator_state(self, device):
        """
        Saves the state of the given actuator in the database. 
        """
        # TODO: Implement this method. You will probably need to extend the existing database structure: e.g.
        #       by creating a new table (`CREATE`), adding some data to it (`INSERT`) first, and then issue
        #       and SQL `UPDATE` statement. Remember also that you will have to call `commit()` on the `Connection`
        #       stored in the `self.conn` instance variable.

        c = self.conn.cursor()

        
        
         

        c.execute("SELECT id FROM actuator WHERE id = ?", (device.id,))
        if c.fetchone() == None:
            
            
            c.execute("INSERT INTO actuator (id, active, value) VALUES (?, ?, ?)", (device.id, device.state, device.value))

        else:
            c.execute("UPDATE actuator SET active = ?, value = ? WHERE id = ?", (device.state, device.value, device.id))

        self.conn.commit()
        c.close()
       


    

    
    def calc_avg_temperatures_in_room(self, room, from_date: Optional[str] = None, until_date: Optional[str] = None) -> dict:
        """Calculates the average temperatures in the given room for the given time range by
        fetching all available temperature sensor data (either from a dedicated temperature sensor 
        or from an actuator, which includes a temperature sensor like a heat pump) from the devices 
        located in that room, filtering the measurement by given time range.
        The latter is provided by two strings, each containing a date in the ISO 8601 format.
        If one argument is empty, it means that the upper and/or lower bound of the time range are unbounded.
        The result should be a dictionary where the keys are strings representing dates (iso format) and 
        the values are floating point numbers containing the average temperature that day.
        """
        # TODO: This and the following statistic method are a bit more challenging. Try to design the respective 
        #       SQL statements first in a SQL editor like Dbeaver and then copy it over here.  

        if not from_date:
            from_date = '0'

        if not until_date:
            until_date = 'None'

        device = None
        

        for r in room.devices:
            if r.device_kind.lower() == "heat pump" or r.device_kind.lower() == "temperature sensor":
                device = r

        

        if device is None:
            return {}


        c = self.conn.cursor()
        c.execute('''
        SELECT DATE(ts) AS date, AVG(value) 
        FROM measurements
        WHERE device = ?
        AND DATE(ts) >= ?
        AND DATE(ts) <= ?
        GROUP BY date
        ''', (device.id, from_date, until_date))

        result = {row[0]: row[1] for row in c.fetchall()}
        
        

        c.close()
        return result


        

    
    def calc_hours_with_humidity_above(self, room, date: str) -> list:
        """
        This function determines during which hours of the given day
        there were more than three measurements in that hour having a humidity measurement that is above
        the average recorded humidity in that room at that particular time.
        The result is a (possibly empty) list of number representing hours [0-23].
        """
        # TODO: implement

        c = self.conn.cursor()
        device = None
        for r in room.devices:
            if r.device_kind.lower() == "humidity sensor":
                device = r


        c.execute('SELECT AVG(value) FROM measurements WHERE device = ? AND DATE(ts) = ?', (device.id, date))
        avg = c.fetchone()[0]

        c.execute('''
        SELECT strftime('%H', ts) AS hour
        FROM measurements
        WHERE device = ? AND DATE(ts) = ? AND value > ?
        GROUP BY hour
        HAVING COUNT(*) > 3
        ''', (device.id, date, avg))

        hours = [int(row[0]) for row in c.fetchall()]

        c.close()
        return hours





        

