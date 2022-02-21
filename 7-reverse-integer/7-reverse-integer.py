class Solution:
    def reverse(self, x: int) -> int:
        maxInt = (2**31)-1
        rev = 0
        neg = x < 0
        x = abs(x)
        while x != 0:
            rem = x % 10
            x //= 10
            if(neg and rev > maxInt+1/10 or (rev == maxInt+1/10 and rem > 8)):
                return 0
            if(rev > maxInt/10 or (rev == maxInt/10 and rem > 7)):
                return 0
            rev = rev*10 + rem
            print(x)
        return rev*-1 if neg else rev