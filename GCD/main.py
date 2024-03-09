class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        gcd = ''  
        possible_gcds = ['']

        #find the smaller lengthed string and iterate through the characters in order with longer string
        min_str = str1 if str1 <= str2 else str2
        max_str = str2 if str1 <= str2 else str1
        for i, char in enumerate(min_str):
            if char != max_str[i]: break
            else:
                gcd += char
                if len(max_str)%(len(gcd)) == 0 and len(min_str)%len(gcd)==0:
                    tmpstr =  gcd*(len(max_str)//len(gcd))
                    tmp2str =  gcd*(len(min_str)//len(gcd))
                    if tmpstr == max_str and tmp2str == min_str:
                        possible_gcds.append(gcd)
        return possible_gcds[-1]