from abc import ABC, abstractmethod
import coding_challenge  

class Demo(ABC):
    @abstractmethod
    def m1(self):
        pass
@coding_challenge.time_decorator
class demo1(Demo):
    def m1(self):
        coding_challenge.time.sleep(3)
        return "Abstract method..."

obj = demo1()

print(obj.m1())