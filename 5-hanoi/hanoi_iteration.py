# 迭代堆栈法解hanoi塔问题
class Task:
    def __init__(self,num,top,fromSpike,toSpike,bufferSpike):
        self.num = num
        self.top = top
        self.fromSpike = fromSpike
        self.toSpike = toSpike
        self.bufferSpike = bufferSpike
    
    def __str__(self):
        return f"{self.num} | {self.top} | {self.fromSpike} | {self.toSpike} | {self.bufferSpike}"

    def move(self,count):
        print(f"第{count}轮:{self.top}从{self.fromSpike} 移到 {self.toSpike}")

class Stack:
    q=[]
    def __init(self):
        #self.q = []
        pass
    
    def push(self,o):
        self.q.append(o)
        #print("push:",self.q[-1])
        return self
        
    def pop(self):
        #print("pop:",self.q[-1])
        return self.q.pop()

    def isEmpty(self):
        return len(self.q)==0

def hanoi(num):
    def push(n,i,f,t,b):
        t = Task(n,i,f,t,b)
        tasks.push(t)

    tasks = Stack()
    push(num,1,'A','C','B')
    count =1
    while not tasks.isEmpty():
        task = tasks.pop()
        
        if task.num==1:
            task.move(count)
            count+=1
        else:
            push(task.num-1,1,task.bufferSpike,task.toSpike,task.fromSpike)
            push(1,task.num,task.fromSpike,task.toSpike,task.toSpike)
            push(task.num-1,1,task.fromSpike,task.bufferSpike,task.toSpike)
hanoi(4)