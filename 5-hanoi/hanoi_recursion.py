# 递归法解hanoi塔问题
def move(n,fromSpike,toSpike):
    global count,top
    count+=1
    print(f"第{count}回合：{n} 从{fromSpike} 移到 {toSpike}")
    top[fromSpike]= '0' if str(n+1) in top.values() else str(n+1)
    top[toSpike]=str(n)

def tower(n,fromSpike,spareSpike,toSpike):
    if n==1:
        move(1,fromSpike,toSpike)
    else:
        tower(n-1,fromSpike,toSpike,spareSpike)
        move(n,fromSpike,toSpike)
        tower(n-1,spareSpike,fromSpike,toSpike)

count = 0
top={'A':'1','B':'0','C':'0'}
tower(4,'A','B','C')