# Method Overloading

class overloading:
    def sum(self,a=None,b=None,c=None):
        if (a!=None and b!=None and c!=None):
            s=a+b+c
        elif(a!=None and b!=None):
            s=a+b

        return s 

obj=overloading()
print(obj.sum(10,30))