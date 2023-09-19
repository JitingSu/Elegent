class Solution:
    def integer_break(self, n: int) -> int:
        ans = 0
        # 拆分成i份
        for i in range(2, n + 1):
            # 每份的份额为share
            share = n // i
            # 总共多余的部分extra
            extra = n % i
            # 有extra份额外加1，剩下的i-extra份仍然保持原有份额share
            tmp = (share + 1) ** extra * share ** (i - extra)
            ans = max(ans, tmp)
        return ans


def main():
    solution = Solution()

    n = 5  # 用你希望测试的整数替换这里
    result = solution.integer_break(n)
    print("最大乘积:", result)


if __name__ == "__main__":
    main()
