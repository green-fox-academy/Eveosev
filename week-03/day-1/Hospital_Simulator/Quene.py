class Quene():

    def __init__(self):
        self.quene = {}
        self.patient_id = 0

    def addPatient(self,patient):
        self.quene[self.patient_id + 1] = patient
    
    def attractNextPatient(self):
        self.nextpatient = self.quene[list(self.quene.keys())[0]]
        del self.quene[list(self.quene.keys())[0]]
        return f"{self.nextpatient}"
    
