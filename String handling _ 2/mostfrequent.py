'''5.Write the function mostFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated the same), 
returns a lowercase string containing the letters of s in most frequently used order. (In the event of a tie between two letters, follow alphabetic order.)
Eg - "We Attack at Dawn" is input. Output should be atwcdekn'''


'''plan:
	-- defining function named is mostfrequentletters
	-- need to remove space and '''
def mostFrequentLetters(s):
	countOfSame = 0
	new = ''
	string = s.lower()
	print(string)
	s=string.replace(" ",'')
	print(s)
	for i in s:
		if i not in new:
			countOfSame = s.count(i)
			print(f'count of {i}: {countOfSame}')
			new = new+i
	print(new)
	new = ''.join(sorted(new))
	output = ''.join(sorted(new, key=lambda x: s.count(x),reverse=True))
	print(output)

mostFrequentLetters(s=input("Enter the string :"))