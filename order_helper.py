#!/usr/bin/env python3
# Author: Mike Graham esq
# Date: 

# This program is intended to make ordering supplies at Fun Run in Blue Springs more efficient 



# Imports
from tkinter import *



# tkinter
root = Tk()
root.geometry("600x600")
root.title("Fun Run Order Helper")



# Labels
kitchen_label = Label(root, padx=5, text="Kitchen:")
breakroom_label = Label(root, padx=5, text="Break Room:")
deepfreeze_label = Label(root, padx=5, text="Deep Freeze:")
#totals_label = Label(root, padx=5, text="TOTALS:")

chz_label = Label(root, text="Cheese Pizza: ", anchor="w")
pep_label = Label(root, text="Pepperoni Pizza: ", anchor="w")
sup_label = Label(root, text="Supreme Pizza: ", anchor="w")
mt_label = Label(root, text="Meat Pizza: ", anchor="w")
#break_label = Label(root, text="", anchor="w", pady=1)



# Entry Fields
chz_kitchen_entry = Entry(root, width=3, borderwidth=1)
pep_kitchen_entry = Entry(root, width=3, borderwidth=1)
sup_kitchen_entry = Entry(root, width=3, borderwidth=1)
mt_kitchen_entry = Entry(root, width=3, borderwidth=1)

chz_breakroom_entry = Entry(root, width=3, borderwidth=1)
pep_breakroom_entry = Entry(root, width=3, borderwidth=1)
sup_breakroom_entry = Entry(root, width=3, borderwidth=1)
mt_breakroom_entry = Entry(root, width=3, borderwidth=1)

chz_deepfreeze_entry = Entry(root, width=3, borderwidth=1)
pep_deepfreeze_entry = Entry(root, width=3, borderwidth=1)
sup_deepfreeze_entry = Entry(root, width=3, borderwidth=1)
mt_deepfreeze_entry = Entry(root, width=3, borderwidth=1)



# Buttons actions
def add_chz():
    chz_kitchen_total = int(chz_kitchen_entry.get())
    chz_breakroom_total = int(chz_breakroom_entry.get())
    chz_deepfreeze_total = int(chz_deepfreeze_entry.get())
    chz_total = chz_kitchen_total + chz_breakroom_total + chz_deepfreeze_total
    chz_total_label = Label(root, text=chz_total)
    chz_total_label.grid(row=1, column=5)



# Buttons
chz_button = Button(root, text="Cheese TOTAL", padx=2, pady=1, anchor="w", command=add_chz)
pep_button = Button(root, text="Pepperoni TOTAL", padx=2, pady=1, anchor="w")
sup_button = Button(root, text="Supreme TOTAL", padx=2, pady=1, anchor="w")
mt_button = Button(root, text="Meat TOTAL", padx=2, pady=1, anchor="w")




# Grid
kitchen_label.grid(row=0, column=1)
breakroom_label.grid(row=0, column=2)
deepfreeze_label.grid(row=0, column=3)
#totals_label.grid(row=0, column=4)

chz_label.grid(row=1, column=0, sticky="w")
pep_label.grid(row=2, column=0, sticky="w")
sup_label.grid(row=3, column=0, sticky="w")
mt_label.grid(row=4, column=0, sticky="w")
#break_label.grid(row=5, column=0, sticky="w")

chz_kitchen_entry.grid(row=1, column=1)
pep_kitchen_entry.grid(row=2, column=1)
sup_kitchen_entry.grid(row=3, column=1)
mt_kitchen_entry.grid(row=4, column=1)

chz_breakroom_entry.grid(row=1, column=2)
pep_breakroom_entry.grid(row=2, column=2)
sup_breakroom_entry.grid(row=3, column=2)
mt_breakroom_entry.grid(row=4, column=2)

chz_deepfreeze_entry.grid(row=1, column=3)
pep_deepfreeze_entry.grid(row=2, column=3)
sup_deepfreeze_entry.grid(row=3, column=3)
mt_deepfreeze_entry.grid(row=4, column=3)


chz_button.grid(row=1, column=4, sticky="w")
pep_button.grid(row=2, column=4, sticky="w")
sup_button.grid(row=3, column=4, sticky="w")
mt_button.grid(row=4, column=4, sticky="w")










root.mainloop()

# Pizzas On Hand; Kitchen
#chz_pizza_oh_kitchen = float(input("Cheese Pizza on hand; Kitchen: "))
#pep_pizza_oh_kitchen = float(input("Peperoni Pizza on hand; Kitchen: "))
#sup_pizza_oh_kitchen = float(input("Supreme Pizza on hand; Kitchen: "))
#mt_pizza_oh_kitchen = float(input("Meat Pizza on hand; Kitchen: "))

# Pizzas On Hand; Breakroom Freezer
#chz_pizza_oh_brfz = float(input("Cheese Pizza on hand; Breakroom Freezer: "))
#pep_pizza_oh_brfz = float(input("Peperoni Pizza on hand; Breakroom Freezer: "))
#chz_pizza_oh_brfz = float(input("Supreme Pizza on hand; Breakroom Freezer: "))