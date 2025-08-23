class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keypad = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"],
        }
        
        def solve(idx):
            if idx == len(digits):
                return [""]
            
            letters = keypad.get(digits[idx], [])
            suffixes = solve(idx + 1)

            return [ch + suf for ch in letters for suf in suffixes]

        return solve(0)
