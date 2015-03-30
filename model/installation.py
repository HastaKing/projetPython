"""
    class installation
"""

class Installation:
    def __init__(self, comLib):
        self.comLib = comLib

    def setComLib(self, new):
        self.comlib = new

    def setInsCodePostal(self, new):
        self.insCodePostal = new

    def setInsLibelleVoie(self, new):
        self.insLibelleVoie = new

    def setInsNumeroInstall(self, new):
        self.insNumeroInstall = new

    def setInsPartLibelle(self, new):
        self.insPartLibelle = new

    def setLatitude(self, new):
        self.latitude = new

    def setLongitude(self, new):
        self.longitude = new

    def getComLib(self):
        return self.comLib

    def getInsCodePostal(self):
        return self.insCodePostal

    def getInsLibelleVoie(self):
        return self.insLibelleVoie

    def getInsNumeroInstall(self):
        return self.insNumeroInstall

    def getInsPartLibelle(self):
        return self.insPartLibelle

    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def __repr__(self):
        return "{} - {} - {} - {} - {} - {} - {}".format(	self.comlib,
                                                            self.insCodePostal,
                                                            self.insLibelleVoie,
                                                            self.insNumeroInstall,
                                                            self.insPartLibelle,
                                                            self.latitude,
                                                            self.longitude)