def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
	
    count = 0
	
    if word in wordList:
        newHand = hand.copy()
		
        for char in word:
            newHand[char] = newHand.get(char, 0) - 1
			
        for i in newHand.values():
            if i < 0:
                count += 1
				
            else:
                count += 0
				
        if count > 0:
            return False
			
        else:
            return True
			
    else:
        return False
