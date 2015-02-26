class Installation:
    def __init__(self, comInsee):
        self.comInsee = comInsee

    def setComInsee(self, new):
        self.comInsee = new

    def setComLib(self, new):
        self.comlib = new

    def setInsAccessibiliteAucun(self, new):
        self.insAccessibiliteAucun = new

    def setInsAccessibiliteHandiMoteur(self, new):
        self.insAccessibiliteHandiMoteur = new

    def setInsAccessibiliteHandiSens(self, new):
        self.insAccessibiliteHandiSens = new

    def setInsCodePostal(self, new):
        self.insCodePostal = new

    def setInsDateMaj(self, new):
        self.insDateMaj = new

    def setInsEmpriseFonciere(self, new):
        self.insEmpriseFonciere = new

    def setInsGardiennee(self, new):
        self.insGardiennee = new

    def setInsLibelleVoie(self, new):
        self.insLibelleVoie = new

    def setInsLieuDit(self, new):
        self.insLieuDit = new

    def setInsMultiCommune(self, new):
        self.insMultiCommune = new

    def setInsNbPlaceParking(self, new):
        self.insNbPlaceParking = new

    def setInsNbPlaceParkingHandi(self, new):
        self.insNbPlaceParkingHandi = new

    def setInsNoVoie(self, new):
        self.insNoVoie = new

    def setInsNumeroInstall(self, new):
        self.insNumeroInstall = new

    def setInsPartLibelle(self, new):
        self.insPartLibelle = new

    def setInsTransportAutre(self, new):
        self.insTransportAutre = new

    def setInsTransportBateau(self, new):
        self.insTransportBateau = new

    def setInsTransportBus(self, new):
        self.insTransportBus = new

    def setInsTransportMetro(self, new):
        self.insTransportMetro = new

    def setInsTransportTrain(self, new):
        self.insTransportTrain = new

    def setInsTransportTram(self, new):
        self.insTransportTram = new

    def setLatitude(self, new):
        self.latitude = new

    def setLongitude(self, new):
        self.longitude = new

    def setNb_Equipements(self, new):
        self.nb_Equipements = new

    def setNb_FicheEquipement(self, new):
        self.nb_FicheEquipement = new

    def set_l(self, new):
        self._l = new

    def setGeo(self, new):
        self.geo = new

    def __repr__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(	self.comInsee,
                                                                                                                                                                self.comlib,
                                                                                                                                                                self.insAccessibiliteAucun,
                                                                                                                                                                self.insAccessibiliteHandiMoteur,
                                                                                                                                                                self.insAccessibiliteHandiSens,
                                                                                                                                                                self.insCodePostal,
                                                                                                                                                                self.insDateMaj,
                                                                                                                                                                self.insEmpriseFonciere,
                                                                                                                                                                self.insGardiennee,
                                                                                                                                                                self.insLibelleVoie,
                                                                                                                                                                self.insLieuDit,
                                                                                                                                                                self.insMultiCommune,
                                                                                                                                                                self.insNbPlaceParking,
                                                                                                                                                                self.insNbPlaceParkingHandi,
                                                                                                                                                                self.insNoVoie,
                                                                                                                                                                self.insNumeroInstall,
                                                                                                                                                                self.insPartLibelle,
                                                                                                                                                                self.insTransportAutre,
                                                                                                                                                                self.insTransportBateau,
                                                                                                                                                                self.insTransportBus,
                                                                                                                                                                self.insTransportMetro,
                                                                                                                                                                self.insTransportTrain,
                                                                                                                                                                self.insTransportTram,
                                                                                                                                                                self.latitude,
                                                                                                                                                                self.longitude,
                                                                                                                                                                self.nb_Equipements,
                                                                                                                                                                self.nb_FicheEquipement,
                                                                                                                                                                self._l,
                                                                                                                                                                self.geo)