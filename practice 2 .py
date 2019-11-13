print ("how many days remain until the next full moon?")
numday = int(input())
print ("We must count the days...")

while numday > 0:
    print ("The full moon will be upon us in" +str(numday)+ "Days")
    numday -= 1
if numday == 0:
    print ("It's a full moon. The beast has been unleashed!")
    print ("May it have mercy on our souls.")