#program to add smallest unique number and smallest duplicate number
n='351886761'
unique=float('inf')
dup=float('inf')
for i in n:
    if n.count(i)==1:
        if int(i)<unique:
            unique=int(i)
    else:
        if int(i)<dup:
            dup=int(i)
print(dup+unique)
#small unique-3 and small duplicate-1
#1+3=4
 
        
        
   