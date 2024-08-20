'''
Number combo: for number 1 to 4, how many different 3 digit numbers with no repeating
digits in each number? What are they?
'''
# nested loop

total=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if ((i!=j)and(j!=k)and(k!=i)):
                print(i,j,k)
                total+=1
print('Total of the three digit number: ',total)
