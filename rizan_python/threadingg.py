# import threading

# def print_cube(num):
#     print("cube",(num*num*num))

# def print_sum(num1,num2):

#     print("sum:",(num1+num2))

# if __name__ == "__main__":
#     t1=threading.Thread(target=print_sum,args=(10,12,))
#     t2=threading.Thread(target=print_cube,args=(10,))

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

#     print("done !")

import threading

def print_cube(num):
    print("cube: {}" .format(num*num*num))

def print_sum(num1,num2):
    print("sum: {}" .format(num1+num2))

if __name__ =="__main__":
    host=int(input("enter your number : "))
    host1=int(input("enter your number : "))                
t1=threading.Thread(target=print_sum,args=(host,host1))
t2=threading.Thread(target=print_cube,args=(host,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done!")
