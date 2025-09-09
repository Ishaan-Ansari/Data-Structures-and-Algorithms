class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negetive = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            # double the divisor until it's larger than dividend
            while dividend >= (temp << 1):    
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            quotient += multiple

        if negetive:
            quotient = -quotient

        # clamp to 32-bit integer range
        return max(INT_MIN, min(INT_MAX, quotient))
        