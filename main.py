class Car:
#
  def __init__(self, make, year_model):
    self.__make = make
    self.__year_model = year_model
    self.__speed = 0

  def accelerate(self):
    self.__speed += 5

  def brake(self):
    self.__speed -= 5

  def get_speed(self):
    return self.__speed

skyline = Car('Nissan', '2002 R34 Skyline GT-R')

print('\033[4mTime (s)\033[0m  \033[4mSpeed (mph)\033[0m')
for i in range(5):
  skyline.accelerate()
  speed = skyline.get_speed()
  print(format(i+1, '4d'), format(speed, '13d'))
for i in range(5):
  skyline.brake()
  speed = skyline.get_speed()
  print(format(i+6, '4d'), format(speed, '13d'))
