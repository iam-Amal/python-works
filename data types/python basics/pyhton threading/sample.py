#pyhton threads :
#threads means part of a program or light weight process
#wo types of threading<single threading and multi threading
'''
from time import sleep
def task():
    #block for a moment
    sleep(2)
    #then display msg
    print('this is from another thread')

#task()

from threading import Thread
#creat a thread
obj=Thread(target=task)
#Next we can creat an instance of the threading.Thread class and specify
#our function nameas the 'target' argument in the constructor
#run the thread
obj.start()
'''

'''
from time import sleep
def task(sleep_time,msg):
    #block for a moment
    sleep(sleep_time)
    #display msg
    print(msg)

#creat thread
from threading import Thread
obj=Thread(target=task,args=(1.5,'New msg from another thread'))
obj.start()
#wait for the thread to finish
print('waiting for the thread....')
obj.join()
'''


import time
import threading
def cal_square(num):
    print('calculate the square root of the given number')
    for i in num:
        time.sleep(0.3)#at each itretaion it wait for 0.3 sec
        print('square is:',i * i)

def cla_cube(num):
    print('calculate the cube of given number')
    for i in num:
        time.sleep(0.3)
        print('cube is:',i * i * i)

lst1=[4,5,6,7,2]#given list

t1=time.time()#get total time to exicute function
obj1=threading.Thread(target=cal_square,args=(lst1,))
obj2=threading.Thread(target=cla_cube,args=(lst1,))
obj1.start()
obj2.start()
obj1.join()
obj2.join()
print('total time taken for threading:',time.time()-t1)
