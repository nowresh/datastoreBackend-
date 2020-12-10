from threading import Thread
from Datastore import *
a=Datastore()
t1=Thread(target=a.create("nowresh",123))
t2=Thread(target=a.read("nowresh"))
t3=Thread(target=a.store_data())
t1.start()
t2.start()
t3.start()
t1.join()#Joining the threads to main thread
t2.join()
t3.join()#after joining the thread the next statement executes 
print("Process completed!")  
