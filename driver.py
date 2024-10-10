import main

def main():
  print("Create a new Car object")
  skyline = main.Car('2002 R34 Skyline GT-R','Nissan', 10)

  for i in range(5):
    if(i==0):
      print('\nAccelerating the car...\n')
    else:
      print('\nAccelerating the car again...\n')
    skyline.accelerate()
    skyline.get_speed()

  for i in range(5):
    if(i==0):
      print('\nApplying the breaks...\n')
    else:
      print('\nApplying the breaks again...\n')
    skyline.brake()
    skyline.get_speed()
    
main()
