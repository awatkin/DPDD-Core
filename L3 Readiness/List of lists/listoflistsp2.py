#carpark simulator upgraded
def viewcars(carpark):
    if len(carpark)>0:
        print("Here are the cars in the carpark right now")
        for i in range(len(carpark)):
            print(i+1, ". ", carpark[i])
    else:
        print("no cars in the carpark, please add some cars")

def addcar(carpark, maximum):
    if len(carpark)<maximum:
        regplate = input("Enter reg plate of car to add")
        carmake = input("Enter the make of car to add")
        carmodel = input("Enter the model of car to add")
        carcolour = input("Enter the colour of car to add")

        car = [regplate, carmake, carmodel, carcolour]
        carpark.append(car)
        print("Car added to the system")
        return carpark
    else:
        print("Carpark is full, please remove a car first")

def removecards(carpark):
    if len(carpark)>0:
        viewcars(carpark)
        while True:
            option = int(input("Enter the number of the car you want to remove"))
            if option>len(carpark):
                print("Not a valid choice, please try again")
            else:
                break
        carpark.pop(option-1)
        return carpark
    else:
        print("No cars in the carpark, please add some cars")

def closingtime():
    print("Car park closed, all cars have exited")
    carpark = []
    return carpark

def main():
    carpark=[]
    maximum=6
    opt=0

    while opt!=7:
        print("Welcome to the new upgraded car parking system")
        print("")
        print("1. Add a car in")
        print("2. Remove a car")
        print("3. View all carpark")
        print("4. Closing time")
        print("")
        print("7. Exit")
        opt=int(input("Enter your choice: "))

        if opt==1:
            carpark = addcar(carpark, maximum)
        elif opt==2:
            carpark = removecards(carpark)
        elif opt==3:
            viewcars(carpark)
        elif opt==4:
            carpark = closingtime()
        elif opt==7:
            print("thanks for using the system")


if __name__ == '__main__':
    main()