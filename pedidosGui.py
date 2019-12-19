#!/usr/bin/python

import tkinter as tk

from toExcel import *

#	I FUCKEN HATE GUIS

def getData():
	aTipo = str(tipoEntry.get())
	aNom = str(nomEntry.get())
	aCant = str(cantEntry.get())
	
	#print("Aqui estan los var\n" + aTipo + "\n" + aNom  + "\n" + aCant) # DEBUGGING
	
	evaluation(aTipo, aNom, aCant)
		
#ENDS getData function

#variables
tipo = "tipo" #StringVar()
nom =  "nom" #StringVar()
cant =  "1" #StringVar()

rootWin = tk.Tk() # creates the root window.

canvas = tk.Canvas(rootWin, height = 600, width = 700)

frame = tk.Frame(rootWin)

#Labels
tipoLabel = tk.Label(frame, text = "Tipo")
nomLabel = tk.Label(frame, text = "Nombre")
cantLabel = tk.Label(frame, text = "Cantidad")

#entrys (text boxes)
tipoEntry = tk.Entry(frame)
nomEntry = tk.Entry(frame)
cantEntry = tk.Entry(frame)

#Buttons
enterButton = tk.Button(rootWin, text = "Enter", command = getData)


#positioning
#place is better to positioning when the other cooler stuff is done
frame.place(relwidth = 1, relheight=1)
canvas.pack()
tipoLabel.grid(row = 0, column = 0)
nomLabel.grid(row = 0, column = 1)
cantLabel.grid(row = 0, column = 2)
tipoEntry.grid(row = 1, column = 0)
nomEntry.grid(row = 1, column = 1)
cantEntry.grid(row = 1, column = 2)
enterButton.pack()

rootWin.mainloop()
