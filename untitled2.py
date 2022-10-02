from tkinter import*
from tkinter import ttk
root= Tk()
root.geometry("1000x600")
root.title("Working on canvas using functions")

canvas= Canvas(root,width= 990, height= 490, bg= "white", highlightbackground= "grey")
canvas.pack()

label= Label(root, text= "Choose Colour")
label.place(relx= 0.6, rely= 0.9, anchor= CENTER)

fill_colour=["red","blue","green","yellow"]
colour_dropdown= ttk.Combobox(root,state= "readonly", value= fill_colour,width= 10)
color_dropdown.place(relx= 0.8, rely= 0.9, anchor= CENTER)

startx= Label(root, text="startx")
startx.place(relx= 0.1, rely= 0.8, anchor= CENTER)

coordinates_values= [10,50,100,200,300,400,500,600,700,800,900]

starty= Label(root, text="starty")
starty.place(relx= 0.3, rely= 0.8, anchor= CENTER)

endx= Label(root, text="endx")
endx.place(relx= 0.5, rely= 0.8, anchor= CENTER)

endy= Label(root, text="endy")
endy.place(relx= 0.7, rely= 0.8, anchor= CENTER)

