# 117269번
import sys

# DP 테이블 생성
dp = [0] * 1001

# 초기값 설정
dp[1] = 1  # 1
dp[2] = 2  # 1+1, 2


for i in range(3, 1001):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

input_data = sys.stdin.read().split()

# 바텀업 방식
if input_data:
    n = int(input_data[0])
    print(dp[n])