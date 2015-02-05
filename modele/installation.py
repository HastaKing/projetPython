class installation:
    def __init__(	self, 
    				actCode, 
    				actLib, 
    				actNivLib, 
    				comInsee, 
    				comLib, 
    				equActivitePraticable, 
    				equActivitePratique, 
    				equActiviteSalleSpe, 
    				equNbEquIdentique, 
    				equipementId):
        self.actCode = actCode
        self.actLib = actLib
        self.actNivLib = actNivLib
        self.comInsee = comInsee
        self.comLib = comLib
        self.equActivitePraticable = equActivitePraticable
        self.equActivitePratique = equActivitePratique
        self.equActiviteSalleSpe = equActiviteSalleSpe
        self.equNbEquIdentique = equNbEquIdentique
        self.equipementId = equipementId


    def __repr__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {} - {}".format(	self.actCode, 
        															self.actLib, 
        															self.actNivLib, 
        															self.comInsee, 
        															self.comLib, 
        															self.equActivitePraticable, 
        															self.equActivitePratique, 
        															self.equActiviteSalleSpe, 
        															self.equNbEquIdentique, 
        															self.equipementId)