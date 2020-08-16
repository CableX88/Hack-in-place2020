

class User:
	def __init__(self, 
				fullName, 
				email,
				campus, 
				year, 
				major, 
				clubsAndOrganizations="", 
				canHelp="", 
				needHelp="", 
				interests=""): 
		self.fullName = fullName
		self.email = email 
		self.campus = campus
		self.year = year
		self.major = major
		self.clubsAndOrganizations = clubsAndOrganizations
		self.canHelp = canHelp
		self.needHelp = needHelp
		self.interests = interests


class Club:
	def __init__(self, 
				clubName,
				members):
		self.clubName = clubName
		self.members = members