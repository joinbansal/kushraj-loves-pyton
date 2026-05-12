print("Select your ride: ")
print("1. Bike")
print("2. Car")

choice = int( input("Enter your choice: ") )

if( choice == 1 ):
  print( "what type of bike? " )
  print("1.i love the avengers\n")
  print("2.i love forsaken\n")


  choice2=int(input("Enter you choice2: "))
  if choice2==1: #inner if statement
    print("you have selected scooty")
  else:
    print("you have selected forsaken")

elif( choice == 2 ):
  print( "what type of car?" )
  print("1.mercedes")
  print("2.van")
  choice3=int(input("enter your choice3: "))

  if choice3==1: #inner if statement
    print("you have selected mercedec")
  else:
    print("you have selected a van")
