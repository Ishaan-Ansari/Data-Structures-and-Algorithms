class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # intialize the INT_MIN and INT_MAX
        INT_MIN = -2**31
        INT_MAX = 2**31-1

        # check for the edge case where dividend is INT_MIN and divisor is -1
        # It can create a overflow error, we can simply return INT_MAX
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # create a flag for negative quotient
        negative = (dividend<0) != (divisor<0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        # smth.. smth..
        # instead of substracting one-by-one we can multiply it by 2 
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while(dividend >= (temp<<1)):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        if negative:
            quotient = -quotient

        return max(INT_MIN, min(INT_MAX, quotient))

