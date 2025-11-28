from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not hand:
            return False
        
        elif len(hand) % groupSize != 0:
            return False

        else:
            freq = Counter(hand) # Counter({2: 2, 3: 2, 1: 1, 6: 1, 4: 1, 7: 1, 8: 1})

            for idx in sorted(freq): # [1, 2, 3, 4, 6, 7, 8]
                check = freq[idx]

                if check == 0:
                    continue

                for i in range(groupSize):
                    if freq.get(idx+i, 0) < check:
                        return False

                    freq[idx + i] -= check
            
        return True
            

                




        