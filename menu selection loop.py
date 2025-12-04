choice = int(input("enter your choice"))
choice = 0
while choice != 3:
    print("menu")
    print("1-start")
    print("2-help")
    print("3-exsit")
choice = int(input("enter your choice")) 
if choice == 1:
    print("start")
elif choice == 2:
    print("help")
elif choice == 3:
    print("exsit,goodbye")
else:
    print("invalid choice")            

