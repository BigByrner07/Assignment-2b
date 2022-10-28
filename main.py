round = "yes"
round = "Yes"
while round == "yes" or round == "Yes":
  print(' Welcome To Calc Bot By Owen Byrne, Please type "Hi" to continue: ')
  print() 
  print()
  choice = input()
  print() 
  print()
  PI = 3.14
  if choice == "Hi" or choice == "hi":
    radius = float(input(' Please Enter the radius of a circle: '))


  circumference = 2 * PI * radius
  area = PI * radius * radius
  print() 
  print() 
  print(" Circumference Of a Circle = %.2f" %circumference)
  print() 
  print() 
  print() 
  print(" Area Of a Circle = %.2f" %area)
  print() 
  print()
  print()

  print("Would you like to enter a new Radius?(Y/N)")
  print()
  round = input()
  if round == "yes" or round == "Yes":
    print()
    print()
if round == "no" or round == "No":
  print()
  print("Have a nice day!")