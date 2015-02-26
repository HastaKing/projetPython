class Activite:
    def __init__(self, equipementId):
        self.equipementId = equipementId

    def setActCode(self, new):
        self.actCode = new

    def setActLib(self, new):
        self.actLib = new

    def setActNivLib(self, new):
        self.actNivLib = new

    def setComInsee(self, new):
        self.comInsee = new

    def setComLib(self, new):
        self.comlib = new

    def setEquActivitePraticable(self, new):
        self.equActivitePraticable = new

    def setEquActivitePratique(self, new):
        self.equActivitePratique = new

    def setEquActiviteSalleSpe(self, new):
        self.equActiviteSalleSpe = new

    def setEquNbEquIdentique(self, new):
        self.equNbEquIdentique = new

    def setEquipementId(self, new):
        self.equipementId = new

    def __repr__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(self.actCode, 
            															self.actLib, 
            															self.actNivLib, 
            															self.comInsee, 
                                                                        self.comLib,
            															self.equActivitePraticable, 
            															self.equActivitePratique, 
            															self.equActiviteSalleSpe, 
            															self.equNbEquIdentique, 
            															self.equipementId)