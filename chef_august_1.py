import sys

input = sys.stdin.readline

def parse(self):
    return self.replace("\n","").split()

T = parse(input())
T = int(T[0])

for t in range(0,T):
    in_ = parse(input())
    n = int(in_[0])
    k = int(in_[1])

    array_=[int(x) for x in parse(input())]
        
    cnt=0    
    for i,num in enumerate(array_):
        if num%2 == 0:
            cnt+=1
            print cnt 
            if i>1 and num < array_[i-1]:
                cnt=1
                print cnt
               
        if cnt==k:
            print "YES"
            break

    if cnt!=k:
        print "NO"    
