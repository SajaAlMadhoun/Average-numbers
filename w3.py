def askuser():
  n=int(input('list length:'))
  mylist=[]
  for item in range(n):
      y='list item '+str(item+1)+':'
      mylist.append(int(input(y)))
  return mylist

def cal_avg(i=[]):
    return(sum(i)/len(i))
print(cal_avg(askuser()))

