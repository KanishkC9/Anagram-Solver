import time

def anagramSolverNormal(word): #iterating and recursing through the string 

    start = time.time()

    result = []
    def normalHelper(innerWord,addedString):
        if(len(innerWord) == 0):
            result.append(addedString)
            return

        for index,char in enumerate(innerWord):
            normalHelper( innerWord[:index] + innerWord[index+1:] , addedString + char) 

    
    normalHelper(word , '')
    end = time.time()
    print('Time Taken for Normal Anagram Solver ', end - start)
    return result


def anagramSolverDP(word): # using anagrams of n-1 string to calculate for nth string

    start = time.time()

    def DPHelper(innerWord):
        if(len(innerWord) == 1):
            return [innerWord]
        
        for index,elem in enumerate(innerWord):
            prevIterVal = DPHelper(innerWord[:-1])
            result = []
            for elem in prevIterVal:
                index = 0
                while(index <= len(elem)):  # can be considered constant if len of word is small
                    leftPart = elem[:index]
                    rightPart = elem[index:]
                    result.append(leftPart + innerWord[len(innerWord) - 1 ] + rightPart)
                    index+=1

        return result

    end = time.time()
    print('Time Taken for DP Anagram Solver ', end - start)

    return DPHelper(word)
                    


print((anagramSolverDP('tea')))
print((anagramSolverNormal('tea')))