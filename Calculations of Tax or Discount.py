print("What do you want to calculate? GST or Discount?\nHere G stands for GST and D stands for Discount\nCan we start to calculate")
a=input("enter to continue: ")
while a=="":
    if a=="":
        b=input("Type G / D or enter to close: ")
    if b=="G" or b=="g":
        print("\nWelcome to GST calculator\nHere, you can calculate the GST")
        n1=float(input("\nEnter the price of the item: "))
        n2=float(input("Quantity: "))
        n3=float(input("GST percentage: "))
        print("The gross amount is: ", n1+(n1*n2)*n3/100,"\nWhere, your GST amount is: ", (n1*n2)*n3/100)
    elif b=="D" or b=="d":
        print("\nWelcome to Discount calculator\nHere, you can calculate the Discount")
        n1=float(input("\nEnter the price of the item: "))
        n2=float(input("Quantity: "))
        n3=float(input("Discount percentage: "))
        print("The gross amount is: ", n1-(n1*n2)*n3/100,"\nWhere, your discount amount is: ", (n1*n2)*n3/100)
    elif b=="":
        break
