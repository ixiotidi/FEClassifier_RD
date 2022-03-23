import os

#os.system("clear")
array1=[]
array2=[]
array3=[]

ans = raw_input("Do you want to delete any previous record? [y/N]: ")
if ans=='y':
    os.system("rm filetest.txt")

for i in range(1000):
    ages = raw_input("What is your age? ")
    names = raw_input("Tell me your name:  ")
    mon = raw_input("How much money you own? ")
    array1.append(ages)
    array2.append(names)
    array3.append(mon)
    x = raw_input("Do you want to continue? [no/No] ")
    if x == 'no' or x == 'No':
	break

f = open("filetest.txt", "a")
arraytotal = (array1, array2, array3)	   
print("Values provided by the user")
f.write("Name \t Age \t Money\n")
for i in range(0,len(array1)):
    print("Age: %d \t Name: %s \t Money: %f\n"%(int(array1[i]),str(array2[i]),float(array3[i])))
    f.write(str(array1[i])+"\t")
    f.write(str(array2[i])+"\t")    
    f.write(str(array3[i])+"\n")    

f.close()
exit() 
	 
	 
	
  
    
