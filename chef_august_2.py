import sys


def output(x,y):
    '''Prints the output in the form of string.
    YES, if point lies in the path
    NO, otherwise.'''

    abs_x = abs(x)
    abs_y = abs(y)
    tempx = x
    tempy = y
    

    if (x==0 and y==0):
        print "YES"
    else:
        step = 1
        mult = -1
        for i in range(0,abs_x):
            tempx += step*mult
            step+=2
            mult*=(-1)

        step=0
        mult=1
        for i in range(0,abs_y):
            tempy += step*mult
            step+=2
            mult*=(-1)
            
        print abs_x, abs_y
        print tempx, tempy
        if (tempx == 0 and abs_y<=abs_x) or (tempy == 0 and abs_x<=abs_y):
            print "YES"
        else:
            print "NO"

def main():

      cases = int(sys.stdin.readline().translate(None,"\n"))

      if cases<1 or cases>10**5:
          print "NO"
          return
        
      for case in range(0,cases):
          x,y = sys.stdin.readline().translate(None,"\n").split(" ")
          x=int(x); y = int(y)

          if x > 10**9 or y > 10**9:
              print "NO"
              break
            
          output(x,y)
    
if __name__ == "__main__":
    main()
