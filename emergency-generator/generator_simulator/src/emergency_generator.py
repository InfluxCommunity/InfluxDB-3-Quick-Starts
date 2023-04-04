from bdb import GENERATOR_AND_COROUTINE_FLAGS
import os
import threading
from threading import Event


from random import  randint
from time import sleep
from faker import Faker

from mqtt_producer import mqtt_publisher




generator_id_counter = 1
fake = Faker()



class emergency_generator():
    def __init__ (self) -> None:
        global generator_id_counter, fake
         
        self.coord = fake.local_latlng(country_code='US', coords_only=False)
        self.generator_id = "generator" + str(generator_id_counter)
        generator_id_counter+=1
        self.temperature = 0
        self.load = 0
        self.power = 0
        
        self.base_fuel = randint(900, 1000)
        self.current_fuel = None

    def returnGeneratorID(self):
        return self.generator_id

   
    def returnTemperature(self):
        currentLoad = self.load
        if currentLoad >= 75: self.temperature = randint(210, 300)
        elif currentLoad >= 50: self.temperature = randint(200, 210)
        elif currentLoad >= 25: self.temperature = randint(190, 200)
        elif currentLoad == 0: self.temperature = 160
        else: self.temperature = randint(170, 190)
        return self.temperature

    def simLoad(self):
        # TODO dont randomise    
        self.load = randint(0, 100)
       

    def returnPower(self):
        currentLoad = self.load
        if currentLoad >= 75: self.power = randint(2000, 2600)
        elif currentLoad >= 50: self.power = randint(1100, 2000)
        elif currentLoad >= 25: self.power = randint(500, 1100)
        elif currentLoad == 0: self.power = 0
        else: self.power = randint(100, 500)
        
        return self.power
    
        
    def returnFuelLevel(self):
        fuel_used = 0
        currentLoad = self.load
        if currentLoad >= 75: fuel_used = randint(90, 130)
        elif currentLoad >= 50: fuel_used = randint(75, 90)
        elif currentLoad >= 25: fuel_used = randint(50, 75)
        elif currentLoad == 0: fuel_used = 0
        else: self.fuel_used = randint(10, 50)

        if self.current_fuel == None:
            self.current_fuel = self.base_fuel - fuel_used
        else:
            if self.current_fuel <= 0:
                refill = randint(500, 1000)
                self.current_fuel = self.current_fuel + refill
            else:
                self.current_fuel = self.current_fuel - fuel_used


        return self.current_fuel

    def returnGenHealth(self):
        # trigger load first as needs to be constent:
        self.simLoad()
        return {"generatorID": self.returnGeneratorID(),
                "lat": float (self.coord[0]), 
                "lon": float(self.coord[1]),
                "temperature": self.returnTemperature(), 
                "power": self.returnPower(),
                "load": self.load, 
                "fuel": self.returnFuelLevel() }



def runEmergencyGenerator(mqtthost):
    emergencyGenerator = emergency_generator()

    mqttProducer = mqtt_publisher(address=mqtthost, port=1883, clientID=emergencyGenerator.returnGeneratorID())
    mqttProducer.connect_client()
    

    sleeptime = randint(5, 15)
    
    while (True):
        check_generator = emergencyGenerator.returnGenHealth()
        print(check_generator,flush=True)
       

        mqttProducer.publish_to_topic(topic="emergency_generator", data=check_generator)
        
        sleep(sleeptime)




    


if __name__ == "__main__":
    GENERATORS = os.getenv('GENERATORS', 1)
    BROKER = os.getenv('BROKER', "localhost")


    i =0
    while (i < int(GENERATORS)):
        generator = threading.Thread(target=runEmergencyGenerator, args=[BROKER], daemon=True)
        generator.start()
        i = i +1
            
    Event().wait()
