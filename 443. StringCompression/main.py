class Solution:
    def compress(self, chars: List[str]) -> int:
        r, i = 0, 0

        #Iterating through the string 
        while(i < len(chars)):
            #setting variable currChar to chars[i] in order to compare 
            currChar = chars[i]
            currOcc = 0
            #Nested while loop that checks for occurences
            while((i < len(chars)) and (chars[i] == currChar)):
                currOcc += 1
                i += 1
            #setting r with the current char and moving onto next index 
            chars[r] = currChar 
            r += 1
            #checks if theres more than one occurence then adds that value to the ptr r 
            if(currOcc > 1):
                for j in str(currOcc):
                    chars[r] = j
                    r += 1
        return r
            
