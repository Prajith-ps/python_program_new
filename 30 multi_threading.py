# import threading
# import time
# def print_name(name,*args):
#     print(name, *args)
# name="tutorialspoint......"


# thread1=threading.Thread(target=print_name,args=(name,1))
# thread2=threading.Thread(target=print_name,args=(name,1,2))
# thread3=threading.Thread(target=print_name,args=(name,1,2,3))
# thread1.start()
# thread2.start()
# thread3.start()

# thread1.join()
# thread2.join()
# thread3.join()
# print("threads are finished ......exiting")



import threading
import time
def print_name(name,*args):
    print(name, *args)
    time.sleep(1)
    
name="tutorialspoint......"

thread1=threading.Thread(target=print_name,args=(name,1))
thread2=threading.Thread(target=print_name,args=(name,1,2))
thread3=threading.Thread(target=print_name,args=(name,1,2,3))
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
print("threads are finished ......exiting")
