#number of ways to form a seven digit password using seven digits 0-6 such that 1st three digits are not all the same, 3th-5th digit are not all the same and last three digits are not all the same.
global answer
answer = 0
def recurse(index, bool, last):
  global answer
  if index == 7:#terminating
    answer +=1 
    return #get out of it
  bad_num = None
  if index  in [2, 4, 6]:
    for num in range(7):
      if bool[num] == 2:
        bad_num = num
        break;
    if bad_num is not None:
      for num in range(7):
        if num!= bad_num:
          bool[num] += 1
          recurse(index + 1,bool, num )
          bool[num] -= 1
    else:
      for num in range(7): #all will do
          bool[num] += 1
          recurse(index + 1,bool, num )
          bool[num] -= 1
  if index in [3, 5]:
    bool = [0 for _ in range(7)]
    bool[last] += 1
    for num in range(7): #all will do
          bool[num] += 1
          recurse(index + 1,bool, num )
          bool[num] -= 1
  if index in [0,1]:
    for num in range(7): #all will do
          bool[num] += 1
          recurse(index + 1,bool, num )
          bool[num] -= 1
  
    
    
      

bool = [0 for _ in range(7)] #counter
recurse(0, bool, None)
print(answer)

print((7**3 - 7)*(7**2 - 1)*(7**2 - 1))

#7 digits, 7 spaces, 3 groups 1-3 3-5 5-7
