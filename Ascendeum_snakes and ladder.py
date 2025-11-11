import numpy as np
import random
import pandas as pd

n = 4
grid = 4
arr= []
dummy_arr = []
winning_status = []
Players =[]
for i in range(n):
  arr.append([])
  dummy_arr.append([])
  winning_status.append(0)
  Players.append(f'Player {i+1}')
status = True
while status:
  for i in range(n):
    dice = random.randint(1, 6)
    dummy_arr[i].append(dice)
    if len(arr[i])>0:
      if arr[i][-1]+dice<=grid*grid:
        arr[i].append(arr[i][-1]+dice)
      else:
        arr[i].append(arr[i][-1])
    elif len(arr[i])==0:
      arr[i].append(dice)
    if arr[i][-1]==grid*grid:
      print(f'Player {i} is winner')
      winning_status[i]=1
      status = False
      break
    
df = pd.DataFrame(columns=('Players', 'Dice Roll History', 'Position History', 'Win Status'))
df['Dice Roll History']= dummy_arr
df['Position History']= arr
df['Win Status']= winning_status
df['Players'] = Players

print(df)

  

  
    
    
  
  