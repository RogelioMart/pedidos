import openpyxl

'''Class Producto
creates the object for Producto and its initializer
'''
class Producto:

    cant = 0
    tipo = ""
	code = ""
    nom = ""
    nextVal = None

    # Class initializer
    def initProducto(self, tipo, nom, code, cant):
        self.tipo = tipo
        self.nom = nom
        self.cant = cant
        self.nextVal = None

''' Ends class producto '''


'''Class slList
 definition of the single linked list
'''
class slList:

    def __init__(self):

        self.headVal = None
        self.lastVal = None

'''ENDS class slList'''


''' makeProducto
@:param String tipo
@:param String nom
@:param String code
@:param Integer cant
@:return Producto newProducto
'''
def makeProducto(tipo, nom, code, cant):

    newProducto = Producto(tipo, nom, code, cant)

    return (newProducto)

'''Ends makeProducto function'''


''' getInput
@:return String retVal
asks the user for the main menu's input
'''
def getInput():
    retVal = 0

    retVal = input("Please Choose an input: ")

    return (retVal)

'''ENDS getInput()'''


''' displayMenu
Displays the main menu options
'''
def displayMenu():

    print("\n\n1: Insert Value\n2: Display List\n3: Search Value\n4: Display Size of The List\n5: Remove Value\n6: Modify Value\n7: Quit")

'''ENDS displayMenu'''

'''getCode
@:param String mTipo
@:return String retVal
Based on the type input name the function will decide
a code.
'''
def getCode(mTipo):
	
	retVal = "Undefined"
	
	if (mTipo == "Banda"):
	
		retVal = DDR
	
	elif(mTipo == "Bomba de Agua"):
	
		retVal = "NWP"
	
	elif(mTipo == "Amortiguador"):
	
		retVal = "MON"
	
	elif(mTipo == "Bujias"):
	
		retVal = "PLU"
		
	elif(mTipo == "Balatas"):
	
		retVal = "WVR"
		
	elif(mTipo == "Filtro de Aciete"):
	
		retVal = "CFI"

	else:
		print("\nTHE CODE ENDED UP BEING UNDEFINED\n")
	
	return(retVal)
	
'''ENDS getCode'''

''' getProduct
@:return Producto temp
Asks the user for the input and takes it in to make
the new Producto object
'''
def getProducto():

    temp = Producto() #initializes the Producto object

    # gets data to make Producto
    temp.tipo = input("Input type: ")

    temp.nom = input("Input name: ")
	
	temp.code = getCode(temp.tipo)

    temp.cant = int(input("Input quantity: "))

    temp.nextVal = None

    return (temp)

'''ENDS getProducto()'''


''' search
@:param slList productList
@:param Producto node
@:return Producto retVal
Searches in the Linked List to find if the node
already exits.
'''
def search(productList, node):

    #Local Variables
    current = Producto()

    retVal = None

    exitLoop = False

    #Local Code
    if(productList.headVal != None):

        current = productList.headVal

        while((current != None) and (exitLoop == False) ): # iterates through the list to see if the element exists

            if((current.tipo == node.tipo) and (current.nom == node.nom)):

                exitLoop = True

                retVal = current

            current = current.nextVal
        #ENDS while loop

    return(retVal)

'''ENDS search()'''


'''insert function
@param slList productList
@param Producto toLinkList
@return slList productList
This function puts the Producto object into the linked
list and returns the linked list in alphabetical order.
'''
def insert(productList, toLinkList):

    #Local Variables
    current = Producto()

    preCurrent = Producto()

    #Local Code

    current = search(productList, toLinkList)

    if(current == None): # True if the element does not exist in the list

        if(productList.headVal == None): #runs if there is nothing in the link list

            productList.headVal = toLinkList

            productList.lastVal = toLinkList

        else: #runs if there is at least 1 element in the link list

            current = productList.headVal

            if(toLinkList.nom < current.nom): #if object to be inserted goes before the head

                toLinkList.nextVal = current

                productList.headVal = toLinkList

            else: #runs if the object will be inserted in the middle of the list or at the end

                preCurrent = productList.headVal

                current = current.nextVal

                while((current != None) and (toLinkList.nom > current.nom)): #searches for the place to insert the object

                    current = current.nextVal

                    preCurrent = preCurrent.nextVal

                #ENDS while loop

                toLinkList.nextVal = current

                preCurrent.nextVal = toLinkList

                if(current == None): #runs if new node is inserted at the ends of the list

                    productList.lastVal = toLinkList

            #ENDS else

    return (productList)

'''ENDS insert function'''


''' dispList
@:param slList productList
The function will display all the values in the linked
List.
'''
def dispList(productList):

    #Local Variables
    iterator = 0

    #Local Code

    if (productList.headVal != None):

        current = productList.headVal

        while (current != None):

            print(iterator)

            print("   " + current.tipo)

            print("   " + current.nom)

            print("   " + str(current.cant) + "\n")

            current = current.nextVal #updates value

            iterator = iterator + 1

    # ENDS if(listSize != 0)

    else:

        print("The list is empty")

    # ENDS else

'''ENDS dispList(productList) function'''


''' listSize
@:param slList productList
@:return integer iterator
Counts the number of elements in the linked List
'''
def listSize(productList):
    # Local Variables

    current = productList.headVal

    iterator = 0

    # Local Code

    while (current != None):
        iterator = iterator + 1

        current = current.nextVal

    return (iterator)

'''Ends listSize function'''

''' removeElement
@:param slList productList
@:param Producto node
@:return Producto retVal
Removes specified element from the linked List
'''
def removeElement(productList, node):
    '''
    Might want
    to check if
    you have to
    dealocate memory
    '''

    # Local Variables

    llSize = listSize(productList)

    exitLoop = False

    current = Producto()

    preCurrent = Producto()

    retVal = None

    retVal = search(productList, node)

    if (retVal != None):

        if ((productList.headVal == node) and (llSize == 1)):  # If only 1 element left in the list

            productList.headVal = None

        else:

            if (productList.headVal == node):  # If removing head but there are still more elements in the list

                productList.headVal = (productList.headVal).nextVal

            else:  # Removes node from the middle

                current = (productList.headVal).nextVal

                preCurrent = productList.headVal

                while ((current != None) and (exitLoop == False)):

                    if ((current.tipo == node.tipo) and (current.nom == node.nom)):

                        preCurrent.nextVal = current.nextVal

                        retVal = current

                        exitLoop = True

                    else:

                        preCurrent = preCurrent.nextVal

                        current = current.nextVal

    return (retVal)

'''ENDS removeElement'''

''' modElement
@:param slList productList
@:param Producto ogNode
@:return Producto retVal
Modifies an element in the linked list
'''
def modElement(productList, ogNode):
    retVal = None

    modify = search(productList, ogNode)

    if (modify != None):

        modify.tipo = input("A que tipo quires cambiarlo")

        modify.nom = input("A que nombre quires cambiarlo")

        modify.cant = input("A que cant quires cambiarlo")


    return(modify)

'''ENDS modElement'''

'''initArray
@:return 
Initializes linked list of linked lists
'''
def init2DList(mLList):
	
	iter = 0
	
	for iter range(11):
	
		productList.append(slList())
	
'''ENDS initArray'''

''' decisionMaker
@:param String mSelect
@:param slList productList
Decides what functions to execute depending on the user's input
'''
def decisionMaker(mSelect, productList):

    if (mSelect == "1"):

        toLinkList = Producto() # initializes producto

        toLinkList = getProducto() #gives producto its values

        insert(productList, toLinkList) #inserts new object in the linked list

    elif (mSelect == "2"):

        dispList(productList) # displays all elements of the list

    elif(mSelect == "3"):

        lookFor = getProducto()

        lookFor = search(productList, lookFor) # Searches for an element in the list

        if(lookFor == None):
            print("\nproduct is not in the list\n")
        else:
            print("\nproduct exists\n")

    elif(mSelect == "4"):

        listSize(productList)

    elif (mSelect == "5"):

        print("\nRemove Value\n")

    elif (mSelect == "6"):

        print("\nModify Value\n")

    elif (mSelect == "7"):

        print("\nExiting the program.\n")

    else:

        print("\nWrong Input\n")

'''ENDS decisionMaker'''

#####################MAIN#############################
######################################################

select = 0 #Initializes variable

'''
0. Amortiguador
1. Balatas
2. Banda
3. Bomba de Agua
4. Bujias
5.Filtro de Aciete 
'''

productList = [] #creates list

#productList = slList()

while (select != "7"):
    displayMenu()

    select = getInput()

    decisionMaker(select, productList)

# ENDS while loop

'''MAIN ENDS HERE'''