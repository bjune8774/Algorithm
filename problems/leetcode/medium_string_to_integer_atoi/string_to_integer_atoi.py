class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        
        is_minus = False
        is_started = False
        
        result = ""

        for i in range(len(str)):
            if is_started:
                if str[i].isdigit():
                    result += str[i]
                elif str[i] == '.' or not str[i].isdigit():
                    break
            elif not is_started:
                if str[i].isdigit():
                    is_started = True
                    result += str[i]
                elif str[i] == '+':
                    is_started = True
                    is_minus = False
                elif str[i] == '-':
                    is_started = True
                    is_minus = True
                elif str[i] == ' ':
                    continue
                else:
                    break
        
        try:
            result = int(result)
        except:
            result = 0
            
        if is_minus:
            result *= -1
            
        if result > INT_MAX :
            result = INT_MAX
        elif result < INT_MIN :
            result = INT_MIN 
        
        
        return result
