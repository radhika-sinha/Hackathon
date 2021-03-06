class Event():
    def __init__(self, hostInstance, name, date, address, county, state, numVaxRequired, recentTestRequired):
        self._hostName = hostInstance.name
        self._hostPhoneNumber = hostInstance.phoneNumber
        self._hostEmail = hostInstance.email
        self._name = name
        self._date = date
        self._address = address
        self._county = county
        self._state = state
        self._numVaxRequired = numVaxRequired
        self._recentTestRequired = recentTestRequired
        self._guests = {}
    #getters and setters
    
    @property
    def eventHostName(self):
        return self._hostName
    
    #
    @property
    def eventGuests(self):
        return self._guests
    
    def deleteGuest(self, guestInstance): 
        self._guests.remove(guestInstance)
    
    