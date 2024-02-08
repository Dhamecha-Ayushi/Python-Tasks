#Super()

class Subject:
    def __init__(self):
        self.sub1="Physics"
        self.sub2="Maths"

    def show(self):
        print("The subjects: ",self.sub1, self.sub2)

class Marks(Subject):
    def __init__(self,mark1,mark2):
          self.mark1=mark1
          self.mark2=mark2
          super().__init__()
          super().show()

    def disp(self):
         print("The marks: ",self.mark1, self.mark2)

S=Marks(18,18)
S.disp()