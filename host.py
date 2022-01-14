from event import Event
from hostConsole import hostConsole
class Host():
    def __init__(self,name,phoneNumber,email):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.events = set()
        self.console = hostConsole(self)
    
    def hostCreateEvent(self, hostInstance, name, date, address, county, state, numVaxRequired, recentTestRequired):
        self.events.add(Event(self, name, date, address, county, state, numVaxRequired, recentTestRequired))
    
    def hostDeleteEvent(self, eventInstance):
        self.events.remove(eventInstance)
    
    
        
        
        