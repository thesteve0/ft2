__author__ = 'spousty'

import vertx
from core.event_bus import EventBus
from org.vertx.java.core.json import JsonArray
from org.vertx.java.core.json import JsonObject



def handler(msg):
    print "Received message"
    flights = JsonArray()
    for flight in msg.body:
        the_flight = JsonObject()
        #print str(flight)
        #the_flight.putString("name", flight.getString("callsign"))
        #the_flight.putString("planeType", flight.getString("equipment") )
        the_flight.putString("speed", flight.get("properties").get("direction"))
        the_flight.putString("alt",  flight.get("properties").get("route"))
        position_array =  flight.get("geometry").get("coordinates")
        #print position_array

        #There can sometimes be two positions readings but I am not sure what they do so I am just going to take the first
        #position =  position_array[0]

        the_flight.putNumber("lat", position_array[1])
        the_flight.putNumber("lon", position_array[0])
        


        flights.addObject(the_flight)

    #Sent the array on the EventBus - this is the one the page should subscribe to
    EventBus.publish('flights.updated', flights)
    print("published the flights")


EventBus.register_handler('raw.flights', handler=handler)
