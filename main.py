import sys
import csv
from sklearn.tree import DecisionTreeClassifier

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

def DTClassify(X,y):
	clf = DecisionTreeClassifier(criterion="entropy")
	clf.fit(X,y)

def getClass(type):
	if type == "Regular":
		return 0
	elif type == "Foreclosure":
		return 1
	elif type == "Short Sale":
		return 2
	else: return 3

def main():
	propDict = {}
	X = []
	y = []
	with open("RealEstate.csv","rb") as readFile:
		readList = csv.reader(readFile,delimiter=',')
		#print readList.next()
		for row in readList:
			propDict[int(row[0])] = Property(int(row[0]),row[1],float(row[2]),float(row[3]),float(row[4]),int(row[5]),float(row[6]),row[7])
	for key in propDict:
		elt = propDict[key]
		X_vec = [elt.price,elt.bedrooms,elt.bathrooms,elt.totalSqft,elt.pricePerSqft]
		y_elt = getClass(elt.status)
		X.append(X_vec)
		y.append(y_elt)
		DTClassify(X,y)
		print X
		print y

if __name__ == "__main__":
	main()

	