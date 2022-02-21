class Solution:
    def myAtoi(self, s: str) -> int:
        maxInt = 2**31
        s = s.strip()
        rt = 0
        sign = 0
        count = 0
        for i in s:
            if(i == '+' or i == '-'):
                if(sign != 0 or count > 0):
                    break
                sign = -1 if i == '-' else 1
            elif(i.isdigit()):
                if(sign == -1 and (rt > maxInt//10 or (rt == maxInt//10 and int(i) > 8))):
                    return maxInt*-1
                elif(sign >= 0 and (rt > (maxInt-1)//10 or (rt == (maxInt-1)//10 and int(i) > 7))):
                    return maxInt - 1
                rt = rt*10 + int(i)
                count += 1
            else:
                break

        return rt*-1 if sign == -1 else rt
        