class Equipement:
    def __init__(self, equipementId):
        self.equipementId = equipementId

    def setEquNom(self, new):
        self.equNom = new

    def setEquipementId(self, new):
        self.equipementId = new

    def setInsNumeroInstall(self, new):
        self.insNumeroInstall = new

    def getEquNom(self):
        return self.equNom

    def getEquipementId(self):
        return self.equipementId

    def getInsNumeroInstall(self):
        return self.insNumeroInstall

    def __repr__(self):
        return "{} - {} - {}".format(   self.equNom,
                                        self.equipementId,
                                        self.insNumeroInstall)