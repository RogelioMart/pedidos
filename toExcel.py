import openpyxl

#used to evaluate data and put it into the excel file


#class for the product
class Producto(object):
	tipo = ""
	nom = ""
	cant = 0
	
	#Class initializer
	def initProducto(self, tipo, nom, cant):
		self.tipo = tipo
		self.nom = nom
		self.cant = cant
#Ends class producto
		
#makes the producto
def makeProducto(tipo, nom, cant):
	producto = Producto(tipo, nom, cant)
	return(producto)
#Ends makeProducto function
		
def isInt(mCant):
	
	retVal = True
	
	for iterator in range(len(mCant)):
		
		if (mCant[iterator].isdigit() != True):
			
			iterator = len(mCant) + 2
			
			retVal = False
		
		#if statement ends here
	
	#for loop ends here

	return(retVal)

#Ends isInt function

def evaluation(mTipo, mNom, mCant):
	
	#print("toExcel got\n" + mTipo + "\n" + mNom + "\n" + mCant) #DEBUGGING
	
	isItInt = False
	
	isItInt = isInt(mCant)
	
	if(isItInt == True):
		print("si es un numero") #DEBUGGING
	
	else:
		print("no hay numero") #DEBUGGING
	
#ends evaluation function

