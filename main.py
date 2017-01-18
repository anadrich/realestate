import sys
import csv

class Property:
	def __init__(self,MLS,location,price,bedrooms,bathrooms,totalSqft,pricePerSqft,status):
		self.MLS = MLS
		self.location = location
		self.price = price
		self.bedrooms = bedrooms
		self.bathrooms = bathrooms
		self.totalSqft = totalSqft
		self.pricePerSqft = pricePerSqft
		self.status = status
	def printProp(self):
		print self.MLS, self.location, self.price, self.bedrooms, self.bathrooms, self.totalSqft, self.pricePerSqft, self.status

def main():
	propDict = {}
	with open("RealEstate.csv","rb") as readFile:
		readList = csv.reader(readFile,delimiter=',')
		print readList.next()
		for row in readList:
			propDict[int(row[0])] = Property(int(row[0]),row[1],float(row[2]),float(row[3]),float(row[4]),int(row[5]),float(row[6]),row[7])
	for key in propDict:
		propDict[key].printProp()

if __name__ == "__main__":
	main()

	