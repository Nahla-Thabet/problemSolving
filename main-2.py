import queue
from Queue_project import *
from PATIENT import *

import random
def ClinicSim(w,min):  # simulation for doctor clinic
    Doctork= Doctor(min)   #time for patient to enter the clinic
    PatientQ= queue()   #creating anew queue
    TimeWaiting=[]     # create alist
    for currentsec in range(w): # w is the time we enter ( 4 hours = 4*60 )
        if random.randrange(20,61)== 60 :  #chossing the random age
            patient=Patient(currentsec)
            PatientQ.enqueue(patient)      # adding the patient to the queue
            if (not Doctor.busy()) and (not PatientQ.isEmpty()):    # check if the doctor is not busy and if there is a patient

                Nextp=PatientQ.dequeue()    # delete patient from queue
                TimeWaiting.append(newp.waitTime(currentsec)) #error, but we didn't solve it   # adding the time to the list
                Doctork.newp(Nextp)
                Doctork.tick()
                averagewait=sum(TimeWaiting)/len(TimeWaiting)  #calculate the average wait
                
    print("Average Wait is ",averagewait,"min and ",PatientQ.size()," task remaining .")