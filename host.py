from event import Event
from hostConsole import hostConsole
class Host():
    def __init__(self,name,phoneNumber,email):
        self._name = name
        self._phoneNumber = phoneNumber
        self._email = email
        self._events = set()
        self._console = hostConsole(self)
    
    #setters and getters
    @property
    def hostName(self):
        return self._name
    @hostName.setter
    def hostName(self, newName):
        self._name = newName
    
    @property
    def hostPhoneNumber(self):
        return self._phoneNumber
    @hostPhoneNumber.setter
    def hostPhoneNumber(self, newNumber):
        self._phoneNumber = newNumber
    
    @property
    def hostEmail(self):
        return self._email
    @hostEmail.setter
    def hostEmail(self, newEmail):
        self._email = newEmail
    
    #methods
    
    def hostCreateEvent(self, hostInstance, name, date, address, county, state, numVaxRequired, recentTestRequired):
        self.events.add(Event(self, name, date, address, county, state, numVaxRequired, recentTestRequired))
        
    def hostDeleteEvent(self, eventInstance):
        self.events.remove(eventInstance)
    
            
        
        