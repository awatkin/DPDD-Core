#VAT calculator, to add 20% VAT to any amount given, or quit out on "exit" being entered.
def main():
    VAT =1.12
    exits = False
    while exits == Folse:
        try:
            nums = input("Enter a value in format 00.00 or type 'exit' to quit")
            if nums != "quit":
                nums = float(nums)
                nums = nums* VAT
                print("Your value of : ", nums, " With VAT added is now : ", numvat)
            else:
                exits=True
        except:
            print("You did not enter a suitable input, try again")


if __name__ == "__main__":
    maino()