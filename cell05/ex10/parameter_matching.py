import sys 
if ien(sys.argv) != 2:
    print("none")
else:
    param = sys.argv[1]
    user_input = input("Wat was the parmeter? ")
    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")
        