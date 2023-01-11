from typing import List
class queue(List):
    def enqueue(self,value):
        super().append(value)
    def dequeue(self):
        super().reverse()
        super().pop()
        super().reverse()
    def top(self):
        lst=super().copy()
        print(lst[0])
    def isEmpty(self):
        lst=list()
        lst=super().copy()
        if(len(lst)==0):
            return True
        return False
class costumer(object):
    def __init__(self,name,surname,id,process):
        self.name=name
        self.surname=surname
        self.id=id
        self.process=process
    def __str__(self):
        return "name:"+str(self.name)+" "+"surname:"+str(self.surname)+" "+"id:"+str(self.id)+" "+"process:"+str(self.process)
q1=queue()
def insert():
    name=input("Enter your name:")
    surname=input("Enter your surname:")
    id=input("Enter your id number:")
    process=input("Please Enter what you wanna do:(money_transfer,withdraw_money,to_refer)")
    new_costomer=costumer(name,surname,id,process)
    q1.enqueue(new_costomer)
def printf():
    for i in q1:
        print(i)
def count():
    print("there are {} people in this queue".format(counter))
def call():
    if(q1.isEmpty==True):
        print("There is no person in the queue")
    else:
        print("the Turn is on -->")
        q1.top()
        q1.dequeue()
counter=0
print("*************Bank queue system*************")
print("1-)Add new costumer to the queue:")
print("2-)call the next costumer:")
print("3-)Display all cotummers in the queue:")
print("4-)How many costumers are there in the queue:")
print("0-)Exit:")
while(True):
    control=int(input())
    if(control==1):
        insert()
        counter+=1
    if(control==2):
        call()
        counter-=1
    if(control==3):
        printf()
    if(control==4):
        count()
    if(control==0):
        break
   




        
        
        
        
