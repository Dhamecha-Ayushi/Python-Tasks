import threading
import time

def cooking_time(seconds):
    for i in range(1,4):
        print(f"Dish {i} making time is:{seconds} seconds")
    time.sleep(seconds)


#normal method
# cooking_time(4)
# cooking_time(2)
# cooking_time(1)
# print(time1)
time1 = time.perf_counter()
#sa,e code with threading
t1 = threading.Thread(target=cooking_time,args=[4])
t2 = threading.Thread(target=cooking_time,args=[2])
t3 = threading.Thread(target=cooking_time,args=[1])


t1.start()
t2.start()
t3.start()

# t1.join()
# t2.join()
# t3.join()
time2 = time.perf_counter()

print("Diff",time2-time1)

