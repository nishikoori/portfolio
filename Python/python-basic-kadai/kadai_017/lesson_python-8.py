class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def check_adult(self):
    if self.age >= 20:
      print(f"{self.name}は大人である")
    else:
      print(f"{self.name}は大人でない") 

human_1 = Human("太郎", 25)
human_2 = Human("花子", 28)
human_3 = Human("二郎", 19)
human_4 = Human("三郎", 16)

humans = [human_1, human_2, human_3, human_4]

for human in humans:
  human.check_adult()

    
  
  

