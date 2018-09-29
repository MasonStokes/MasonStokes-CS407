def encode(input_string):
    #Found code to reference on stackoverflow for help.
    #https://stackoverflow.com/questions/32855812/create-a-compress-function-in-python

	#store the first character to compare to fallowing characters.
	storechar = ""

	count = 1

	#store first char to as reference.
	storechar += input_string[0]

	#Iterate through loop, skipping last one.
	for i in range(len(input_string) - 1 ):
		if(input_string[i] == input_string[i+1]):
			count += 1
		else:
    		if(count >= 1):
    			storechar += str(count)
			storechar += input_string[i+1]
			count = 1

	#print last Char.
	if(count>1):
		storechar += str(count)

	return storechar
