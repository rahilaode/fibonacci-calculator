import time
import numpy as np

time.sleep(5)
print("Start Program")

def fibonacci(n):
    if n <= 0:
        return "Masukkan bilangan bulat positif"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci_10 = fibonacci(10)
print(np.array(fibonacci_10))
print("Process 1 Finished")
time.sleep(3)
        
fibonacci_15 = fibonacci(15)
print(np.array(fibonacci_15))
print("Process 2 Finished")
time.sleep(3)

fibonacci_20 = fibonacci(20)
print(np.array(fibonacci_20))
print("Process 3 Finished")
time.sleep(3)

fibonacci_25 = fibonacci(25)
print(np.array(fibonacci_25))
print("Process 4 Finished")
time.sleep(3)

fibonacci_30 = fibonacci(30)
print(np.array(fibonacci_30))
print("Process 5 Finished")
time.sleep(3)

fibonacci_35 = fibonacci(35)
print(np.array(fibonacci_35))
print("Process 6 Finished")
time.sleep(5)

fibonacci_40 = fibonacci(40)
print(np.array(fibonacci_40))
print("Process 7 Finished")
time.sleep(5)

fibonacci_45 = fibonacci(45)
print(np.array(fibonacci_45))
print("Process 8 Finished")
time.sleep(8)

fibonacci_50 = fibonacci(50)
print(np.array(fibonacci_45))
print("Process 9 Finished")
time.sleep(8)

fibonacci_55 = fibonacci(55)
print(np.array(fibonacci_55))
print("Process 10 Finished")
time.sleep(8)