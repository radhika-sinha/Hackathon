class Guest():
    def __init__(self, name, phoneNumber, email, willShareVaxInfo, numVaccines, recentTestNegative):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.willShareVaxInfo = willShareVaxInfo #true or false
        self.numVaccines = numVaccines #int
        self.recentTestNegative = recentTestNegative #true or false
        