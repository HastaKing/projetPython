class Activite:
	def __init__(self, equipementId):
		self.equipementId = equipementId

	def setActCode(self, new):
		self.actCode = 	

	def setActLib(self, new):
		self.actLib = new

	def setEquipementId(self, new):
		self.equipementId = new

	def getActCode(self):
		return self.actCode

	def getActLib(self):
		return self.actLib

	def getEquipementId(self):
		return self.equipementId

	def __repr__(self):
		return "{} - {} - {}".format(self.actCode, 
									self.actLib, 
									self.equipementId)