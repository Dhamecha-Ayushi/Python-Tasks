import pickle

class demo:
    num = 25
    str = 'Hello'
    list = [1, 2, 3]
    dic = {10: 'Ten', 20: 'Twenty'}
    tup = (11, 22)

obj = demo()

pickled = pickle.dumps(obj) #Pickling object
print(f"Pickled object: \n{pickled}\n")

unpickled = pickle.loads(pickled)
print(f"dictionary of unpickled object: \n{unpickled.dic}\n")