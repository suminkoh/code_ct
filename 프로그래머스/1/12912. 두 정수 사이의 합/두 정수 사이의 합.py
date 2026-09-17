def solution(a, b):
    answer = 0
    for n in range (min(a,b), max(a,b)+1):
        answer = answer + n
    # a + a+1 + a+2...+b
    return answer