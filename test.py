import pandas as pd
import os 
import json

#os.system("clear")
list1=[]
list2=[]
list3=[]

for i in range(1000):
    ages = input("What is your age? ")
    names = input("Tell me your name:  ")
    mon = input("How much money you own? ")
    list1.append(ages)
    list2.append(names)
    list3.append(mon)
    x = input("Do you want to continue? [no/No] ")
    if x == 'no' or x == 'No':
        break
   
df = pd.DataFrame(list(zip(list1 ,  list2 ,  list3)),
                  columns=['Age', 'Name', 'Money'])

print(df)


js = df.to_json(orient= 'records')

    
    
exit() 
	 
	 
	
  
    
