print ("How many numbers should I sum up?")
numbers = int(input())

count = 0
total = 0
while count < numbers :
    count +=1
    print ("Please enter number "+ str(count) +" of "+ str(numbers))
    usernum = int(input())
    total += usernum

print ("The answer us"+ str(total))
