# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_Anagram(word, anagram):
	
	if sorted(word) == sorted(anagram):
		print("Anagram")
		return True
		
	else:
		print("Not Anagram")
		return False
		
anagram = find_Anagram("below","elbow")
anagram = find_Anagram("hello","check")
print(anagram)