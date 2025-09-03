class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        n = len(num)
        ops = ["+", "-", "*"]

        def solve(i, evl, last, exp):
            # base case
            if i == n:
                if evl == target:
                    ans.append(exp)
                    return

            for j in range(i, n):
                if j!=i and num[i] == "0":
                    break

                cur_str = num[i: j+1]
                cur_val = int(cur_str)

                if i == 0:
                    solve(j+1, cur_val, cur_val, cur_str)

                else:
                    # plus
                    solve(j+1, evl+cur_val, cur_val, exp + "+" + cur_str)

                    # minus
                    solve(j+1, evl-cur_val, -cur_val, exp + "-" + cur_str)

                    # undo last operation and multiply
                    solve(j+1, evl - last + last * cur_val, last*cur_val, exp + "*" + cur_str)

        solve(0, 0, 0, "")
        return ans