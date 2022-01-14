class Event():
    def __init__(self, hostInstance, name, date, address, county, state, numVaxRequired, recentTestRequired):
        self.hostName = hostInstance.name
        self.hostPhoneNumber = hostInstance.phoneNumber
        self.hostEmail = hostInstance.email
        self.name = name
        self.date = date
        self.address = address
        self.county = county
        self.state = state
        self.numVaxRequired = numVaxRequired
        self.recentTestRequired = recentTestRequired
        
        
        