number = int(input("enter a positive number=>"))
count = 1
while count <= number:
	if count %2 == 0:
	    print(count, " is even by 3")
else:
		print(count," is not odd by 3")
count = count + 1

print("finished")