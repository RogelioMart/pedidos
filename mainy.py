from llist import dllist, dllistnode
import openpyxl

#----------------Producto Stuff------------------
#------------------------------------------------
# class for the product
class Producto:
    tipo = ""
    nom = ""
    cant = 0

    # Class initializer
    def initProducto(self, tipo, nom, cant):
        self.tipo = tipo
        self.nom = nom
        self.cant = cant


# Ends class producto

# makes the producto
def makeProducto(tipo, nom, cant):
    producto = Producto(tipo, nom, cant)
    return (producto)
# Ends makeProducto function

#-------------------getInput---------------------
#------------------------------------------------
def getInput():
    retVal = 0
    #print("Please Choose an input\n")
    retVal = input("Please Choose an input: ")
    return(retVal)
#ENDS getInput()

#-----------------displayMenu--------------------
#------------------------------------------------
def displayMenu():
    print("\n\n1: Insert Value")
    print("2: Display List")
    print("3: Remove Value")
    print("4: Modify Value")
    print("5: Quit")

#ENDS displayMenu

#-------------------getProducto---------------------
#------------------------------------------------
def getProducto():

    temp = Producto()

    #gets data to make Producto
    temp.tipo = input("Input type: ")
    temp.nom = input("Input name: ")
    temp.cant = int(input("Input quantity: "))

    return(temp)

#ENDS getProducto()

#--------------------insert----------------------
#------------------------------------------------
'''
This function puts the Producto object into the linked
list and returns the linked list in alphabetical order.
'''
def insert(productList):

    temp = Producto()#initializes Producto object

    temp = getProducto() #gets values of the object
	
	if(productList.size == 0):
		

    productList.insert(temp)

    return(productList)

#ENDS insert function

#-------------------dispList----------------------
#------------------------------------------------
def dispList(productList):

    listSize = 0
    iterator = 0
    listSize = productList.size #gets size of the list

    if(listSize != 0):

        current = productList.first

        while(iterator < listSize):

            #displays the linked list
            print((iterator + 1))
            print("   " + current.value.tipo)
            print("   " + current.value.nom)
            print("   " + str(current.value.cant) + "\n")

            current = current.next
            iterator = iterator + 1
        #ENDS while loop

    #ENDS if(listSize != 0)
    else:
        print("The list is empty")
    #ENDS else

#ENDS dispList(productList) function

#-----------------decisionMaker------------------
#------------------------------------------------
def decisionMaker(mSelect, productList):

    if(mSelect == "1"):
        #print("\nPlace holder for insert\n")
        insert(productList)
    elif(mSelect == "2"):
        #print("\nDisplay List\n")
        dispList(productList)
    elif (mSelect == "3"):
        print("\nRemove Value\n")
    elif (mSelect == "4"):
        print("\nModify Value\n")
    elif (mSelect == "5"):
        print("\nExiting the program.\n")
    else:
        print("\nWrong Input\n")

#ENDS decisionMaker

#####################MAIN#############################
######################################################
#MAIN BEGINS HERE

select = 0

productList = dllist()

while(select != "5"):
    displayMenu()

    select = getInput()

    decisionMaker(select, productList)

#ENDS while loop

#MAIN ENDS HERE