from classes import calc

num = ""
while(num.upper() != "QUIT" and num.upper() != "Q"):
    num = input("Enter any number:\n")
    persistance = calc.getPersistance(num)
    print("Multiplication persistance = %d" % persistance)