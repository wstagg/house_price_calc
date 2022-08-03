from tkinter import *
from tkinter import ttk
from unittest.loader import VALID_MODULE_NAME

def calculate_house_budget(*args):
    try:
        save_1 = int(savings_1.get())
        save_2 = int(savings_2.get())
        equit = int(equity.get())
        fee = int(fees.get())
        mort = int(mortgage.get())
        house_budget.set((save_1 + save_2 + equit + mort)-fee) 
    except ValueError:
        pass

def calulate_total_deposit(*args):
    try:
        save_1 = int(savings_1.get())
        save_2 = int(savings_2.get())
        equit = int(equity.get())
        deposit_total.set(save_1 + save_2 + equit)
    except ValueError:
        pass

def calculate_amount_to_save(*args):
    try:
        current_house_budget = ((int(savings_1.get()) + int(savings_2.get()) + int(equity.get()) + int(mortgage.get())) - int(fees.get()))
        if int(goal.get()) > current_house_budget:
            total_to_save.set(int(goal.get()) - current_house_budget)
        else:
            total_to_save.set(0)
    except ValueError:
        pass

root = Tk()
root.title("House Budget Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create entry boxes
savings_1 = StringVar()
savings_1_entry = ttk.Entry(mainframe, width=7, textvariable=savings_1)
savings_1_entry.grid(column=2, row=1, sticky=(E, W))

savings_2 = StringVar()
savings_2_entry = ttk.Entry(mainframe, width=7, textvariable=savings_2)
savings_2_entry.grid(column=2, row=2, sticky=(E, W))

equity = StringVar()
equity_entry = ttk.Entry(mainframe, width=7, textvariable=equity)
equity_entry.grid(column=2, row=3, sticky=(E, W))

fees = StringVar()
fees_entry = ttk.Entry(mainframe, width=7, textvariable=fees)
fees_entry.grid(column=2, row=4, sticky=(E, W))

mortgage = StringVar()
mortgage_entry = ttk.Entry(mainframe, width=7, textvariable=mortgage)
mortgage_entry.grid(column=2, row=5, sticky=(E, W))

goal = StringVar()
goal_entry = ttk.Entry(mainframe, width=7, textvariable=goal)
goal_entry.grid(column=2, row=6, sticky=(E, W))

# Create Buttons
ttk.Button(mainframe, text="Calculate house budget", command=calculate_house_budget).grid(column=1, row=7, sticky=W)
ttk.Button(mainframe, text="Calculate deposit", command=calulate_total_deposit).grid(column=1, row=8, sticky=W)
ttk.Button(mainframe, text="Calculate amount left to save", command=calculate_amount_to_save).grid(column=1, row=9, sticky=W)

# Create output labels 
house_budget = StringVar()
ttk.Label(mainframe, textvariable=house_budget).grid(column=2, row=7, sticky=(W, E))

deposit_total = StringVar()
ttk.Label(mainframe, textvariable=deposit_total).grid(column=2, row=8, sticky=(W, E))

total_to_save = StringVar()
ttk.Label(mainframe, textvariable=total_to_save).grid(column=2, row=9, sticky=(W, E))

# Create text labels 
ttk.Label(mainframe, text="Savings #1").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Savings #2").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Equity").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Fees").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Mortgage").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Goal").grid(column=1, row=6, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()