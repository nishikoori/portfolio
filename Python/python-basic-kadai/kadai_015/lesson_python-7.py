class Human:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    
    def set_name(self, name):
      self.name = name
    def set_age(self, age):
      self.age = age
    
    def printinfo(self):
      print(self.name)
      print(self.age)
         
# インスタンス化する
human = Human("侍太郎", 36)

# printinfoメソッドにアクセスし、値を出力する
human.printinfo()



 
 

