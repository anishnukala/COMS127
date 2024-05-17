#ultimateTODO.py
#Anish Reddy Nukala              04-12-2024
#Assignment 5
#Description: This program is a console-based task management tool that allows users to communicate via command line menus. The program is divided into functions such as backlog,todo,in progress,in review,done. Users may manage and track their progress of work.

import sys
import pickle

def printTitleMaterial():
   
    print("The Ultimate TODO List!")
    print()
    print("By: Anish Reddy Nukala")
    print("[COM S 127 B]")
    print()

def initList():
    
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

def checkIfListEmpty(todoList):
    
    if (len(todoList["backlog"]) > 0 or 
        len(todoList["todo"]) > 0 or
        len(todoList["in_progress"]) > 0 or
        len(todoList["in_review"]) > 0 or
        len(todoList["done"]) > 0):
        return False
    return True

def saveList(todoList):
    
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

def checkItem(item, todoList):
    
    itemFound = False
    keyName = ""
    index = -1
    for key, lst in todoList.items():
        if item in lst:
            itemFound = True
            keyName = key
            index = lst.index(item)
            break

    return itemFound, keyName, index

def addItem(item, toList, todoList):
    
    itemFound, _, _ = checkItem(item, todoList)

    if not itemFound:
        todoList[toList].append(item)
    else:
        print(f"ERROR: Item '{item}' already exists in the '{toList}' list at index {_}.")
    
    return todoList

def deleteItem(item, todoList):
    
    itemFound, _, _ = checkItem(item, todoList)

    if itemFound:
        for key, lst in todoList.items():
            if item in lst:
                lst.remove(item)
                print(f"Item '{item}' deleted from the '{key}' list.")
    else:
        print(f"ERROR: Item '{item}' not found in any list.")

    return itemFound, todoList

def moveItem(item, toList, todoList):
    
    itemFound, keyName, index = checkItem(item, todoList)

    if itemFound:
        todoList[keyName].remove(item)
        todoList[toList].append(item)
        print(f"Item '{item}' moved from '{keyName}' to '{toList}' list.")
    else:
        print(f"ERROR: Item '{item}' not found in any list.")

    return todoList

def printTODOList(todoList):
    
    for key, lst in todoList.items():
        print(f"{key}: {lst}")
    
    return None

def runApplication(todoList):
    
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a":
            item = input("Enter item to add to backlog: ")
            todoList = addItem(item, "backlog", todoList)
            printTODOList(todoList)
        elif choice == "m":
            if not checkIfListEmpty(todoList):
                item = input("Enter item to move: ")
                while True:
                    itemFound, _, _ = checkItem(item, todoList)
                    if not itemFound:
                        print(f"ERROR: Item '{item}' not found in any list.")
                        item = input("Enter a different item to move: ")
                    else:
                        break

                toList = input("Enter list to move item to: ")
                while toList not in todoList.keys():
                    print(f"ERROR: List '{toList}' does not exist.")
                    toList = input("Enter a valid list to move item to: ")

                todoList = moveItem(item, toList, todoList)
                printTODOList(todoList)
            else:
                print("ERROR: No items to move!")
        elif choice == "d":
            if not checkIfListEmpty(todoList):
                item = input("Enter item to delete: ")
                itemFound, _, _ = deleteItem(item, todoList)
                if itemFound:
                    printTODOList(todoList)
            else:
                print("ERROR: No items to delete!")
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
   
    taskOver = False

    printTitleMaterial()

    while not taskOver:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()
            printTODOList(todoList)
            todoList = runApplication(todoList)
        elif choice == "l":
            todoList = loadList()
            printTODOList(todoList)
            todoList = runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()