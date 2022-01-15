class Guest():
    def __init__(self, name, phoneNumber, email, willShareVaxInfo, numVaccines, recentTestNegative):
        self._name = name
        self._phoneNumber = phoneNumber
        self._email = email
        self._willShareVaxInfo = willShareVaxInfo #true or false
        self._numVaccines = numVaccines #int
        self._recentTestNegative = recentTestNegative #true or false
        
    #getters and setters
    @property 
    def guestName(self):
        return self._name
    @guestName.setter
    def guestName(self,newName):
        self._name = newName
        
    @property
    def guestPhoneNumber(self):
        return self._phoneNumber
    @guestPhoneNumber.setter
    def guestPhoneNumber(self,newPhoneNumber):
        self._phoneNumber = newPhoneNumber
    
    @property
    def guestEmail(self):
        return self._email
    @guestEmail.setter
    def guestEmail(self,newEmail):
        self._email = newEmail
    
    