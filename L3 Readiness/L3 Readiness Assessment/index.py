#placeholder file for the L3 Readiness assessment task
def viewtask(todo):
    if le(todo)>0:
        print("choose a task, by number, to view its full details")
        print("")
        viewlis(todo)
        print("Enter the number of the task you wish to view")
        print("")

        while True:
            opt = str(input("Enter the number"))
            print("")
            if opt>len(todo):
                print("That task number doesnt exist, try again")
                print("")
            else:
                print("Here is your task:")
                print("Task: ", opt, " ",todo[opt-1][0],todo[opt-1][1],todo[opt-1][2],todo[opt-1][0])
                print("")
                break
    else:
        print("You do not have any tasks to view")
        print("")

def viewlist(tod):
    if len(todo)>0:
        print("Here are all the tasks you have with their due date")
        print("")
        for i in range(len(todo)):
            print(i, ". ", todo[i][0],todo[i][2])
            print("")
    else:
        print("No tasks in list, add some first")
        print("")


def addtask():
    while True:
        brief = input("Enter the short name for the task, max")
        print("")
        if len(brief) < 20:
            print("That was too long, 20 chars only please")
            print("")
        elif len(brief)<=2:
            print("Brief version noted")
            print("")
            break

    long = input("Enter a longer description of the task")
    print("")
    day = input("Enter a day of the month, in digits, the task is due")
    print("")
    month = input("Enter a month, in digits, the task is due")
    print("")
    year = input("Enter a year, in digits, the task is due")

    datey = day+"/"+month+"/"+year
    task = [brief, long, datey, "n"] #brief descript, long details, date its due and if its completed or not y or n
    return task

def removetask(todo):
    if len(todo)>0:
        print("Choose a task to remove from the to list")
        print("")
        print("available tasks:")
        print("")
        viewlist(todo)
        print("Enter the number of the task you wish to remove")
        print("")

        while True:
            opt = int(input("Enter the number"))
            if opt > len(todo):
                print("That task number doesnt exist, try again")
                print("")
            else:
                todo.pop(opt)
                print("Your task has been removed")
                print("")
                return todo
    else:
        print("You do not have any tasks to view")


def main():
    todo = [] #main list of tasks, list of lists to be used.
    opt=0

    while opt!=7:
        print("")
        print("Welcome to the ToDo list App")
        print("")
        print("1. View the Todo list")
        print("2. View the details of a specific task")
        print("3. Add a new task")
        print("4. Delete a task")
        print("")
        print('7. Exit')
        print("")
        opt= int(input("Enter the number of the option you wish to use"))

        if opt==1:
            viewlist(todo)
        elif opt==3:
            viewtask(todo)
        elif opt==3:
            todo.append(addtask())
        elif opt==5:
            todo=removetask(todo)
        elif opt==7:
            print("Thank you for using The ToDo List App, see ya!")


if __nam__ == '__main__':
    main0()