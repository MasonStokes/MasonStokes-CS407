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
		#This adds to the count for each char if the next item in the input string is an equal char.
		if(input_string[i] == input_string[i+1]):
			count += 1
		#This will add to the count to the stored char which is the compressed stirng, if a char doesn't have the same char following it.
		else:
			if(count >= 1):
				storechar += str(count)
			storechar += input_string[i+1]
			count = 1


	
	storechar += str(count)

	return storechar
