#used to evaluate data and put it into the excel file

def isInt(mCant):
	
	retVal = True
	
	for iterator in range(len(mCant)):
		
		if (s[iterator].isdigit() != True):
			
			iterator = len(mCant) + 2
			
			retVal = False
		
		#if statement ends here
	
	#for loop ends here

	return(retVal)

#ends isInt function

def evaluation(mTipo, mNom, mCant):
	
	#print("toExcel got\n" + mTipo + "\n" + mNom + "\n" + mCant) #DEBUGGING
	
	isItInt = False
	
	isItInt = isInt(mCant)
	
	if(isItInt == True):
		appendToExcel()
	
#ends evaluation function

