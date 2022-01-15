class hostConsole():
    def __init__(self,hostInstance):
        self._hostInstance = hostInstance
        #use this console for displaying information of the host
    
    
    def GUI(self):
        pass
        #create user interface for host's interaction with app
        host = self._hostInstance
        print(host.hostName, host.hostPhoneNumber)