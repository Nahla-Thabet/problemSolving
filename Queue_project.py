
class Doctor :
    def _init_(self ,p):  # defult state ( No patient & TimeRemaing ==0)
        self.Drate = p
        self.currentpatient = None
        self.timeReamaining = 0

    def tick(self) : # THe Time which is pass through 4 hours from 12pm -4pm)
        if self.currentpatient !=None:
            self.timeRemaining = self.timeRemaining -1 #
            if self.timeRemaining == 0:   #finally when time fenish
                self.currentpatient=None

    def busy(self): # Fn that makes sure if there's patient or not
        if self.currentpatient !=None:
            return True
        else:
            return False

    def Nextp(self,newp): # the Next one in queue to enter
        self.currentpatient = newp
        self.timeRemaining = newp.getpatient()*60/self.Drate


