#!/usr/bin/python
import os
import string

lstLines = []
lstYears = []
lstMakes = []
lstModels = []
lstEngines = []
lstTrans = []

def view_cars():
    # Displays current inventory
    os.system('clear')
    num = len(lstYears)
    counter = 0
    print "#   Year %20s %20s %15s %14s" % ("Make", "Model", "Engine", "Transmission")
    while counter < num:
        print "%s)  %-4s %20s %20s %15s %14s" % (counter+1, lstYears[counter], \
            lstMakes[counter], lstModels[counter], lstEngines[counter], lstTrans[counter])
        counter += 1

    raw_input("Press Enter to return to the home screen...")
    home()

def rerun(x):
    option = raw_input("\nWould you like to %s another vehicle? (y/N): " % (x))
    if option.lower() == "yes" or option.lower() == "y" :
        if x == "add":
            new_car()
        elif x == "remove":
            remove_car()
    else:
        return "break"

def new_car():
    # Adds a vehicle to the inventory
    while True:
        year = raw_input("\nEnter Vehicle Year: ")
        if year.isdigit() == True and len(year) == 4:
            break
        else:
            print "%s is not a valid vehicle year." % (year)
    make = raw_input("\nEnter Vehicle Make: ").capitalize()
    model = raw_input("\nEnter Vehicle Model: ").capitalize()
    engine = raw_input("\nEnter Vehicle Engine Size: ").upper()
    while True:
        trans = raw_input("\nEnter Vehicle Transmission Type: ").capitalize()
        if trans.lower() == "manual" or trans.lower() == "automatic" or trans.lower() == "auto":
            break
        else:
            print "Valid options are Manual or Automatic."

    lstYears.append(int(year))
    lstMakes.append(make)
    lstModels.append(model)
    lstEngines.append(engine)
    lstTrans.append(trans)

    # Write the vehicle to file
    with open("cars_inv.csv", "a+") as f:
        f.write("%s,%s,%s,%s,%s\n" % (year, make, model, engine, trans))

def remove_car():
    # Deletes all of the selected vehicle's information
    num = 0
    ind = 0
    while True:
        num = raw_input("Please enter the inventory number of the vehicle you want to delete: ")
        try:
            ind = string.atoi(num) - 1
            if ind >= len(lstYears) or num == "0":
                print "Not a valid inventory number"
            else:
                break
        except:
            print "Please enter a single number only"

    confirm = raw_input("Deleting %s %s %s with a %s and %s transmission.\nAre you sure? (y/N): " \
        % (lstYears[ind], lstMakes[ind], lstModels[ind], lstEngines[ind], lstTrans[ind].lower()))
    if confirm.lower() == "y" or confirm.lower() == "yes":
        with open("cars_inv.csv", "w") as f:
            lines = len(lstYears)
            counter = 0
            while counter < lines:
                if counter != ind:
                    f.write("%s,%s,%s,%s,%s\n" % (lstYears[counter], lstMakes[counter], \
                        lstModels[counter], lstEngines[counter], lstTrans[counter]))
                counter += 1
        lstYears.pop(ind)
        lstMakes.pop(ind)
        lstModels.pop(ind)
        lstEngines.pop(ind)
        lstTrans.pop(ind)

def home():
    # Default screen
    os.system('clear')
    while True:
        print "Vehicle Inventory Manger\n\nPlease select an option:"
        print "1)  View the Current Inventory"
        print "2)  Add a Vehicle to the Inventory"
        print "3)  Remove a Vehicle from the Inventory"

        selection = raw_input("Please select an option: ")
        print "\n"
        try:
            if int(selection) == 1:
                view_cars()
            elif int(selection) == 2:
                new_car()
                while True:
                    key = rerun("add")
                    if key == "break":
                        break
            elif int(selection) == 3:
                remove_car()
                while True:
                    key = rerun("remove")
                    if key == "break":
                        break
            else:
                print "Invalid selection\n"
        except ValueError:
            print "Please select an option using numbers only\n"

# Load the CSV inventory
file = "cars_inv.csv"
try:
    with open(file, 'r') as f:
        lstLines = [line.strip() for line in f]
    for x in lstLines:
        car = x.split(',')
        lstYears.append(car[0])
        lstMakes.append(car[1])
        lstModels.append(car[2])
        lstEngines.append(car[3])
        lstTrans.append(car[4])
except IOError:
    pass

home()
