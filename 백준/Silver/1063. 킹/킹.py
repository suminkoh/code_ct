king_pos, stone_pos, n = input().split()

# 1. 초기 위치 설정 (A1 -> 1, 1)
kx = ord(king_pos[0]) - ord('A') + 1
ky = int(king_pos[1])
sx = ord(stone_pos[0]) - ord('A') + 1
sy = int(stone_pos[1])

# 2. 이동 방향 정의 (알파벳 방향 x, 숫자 방향 y)
# R, L, B, T, RT, LT, RB, LB 순서
move_list = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

# 3. N번만큼 명령 수행
for _ in range(int(n)):
    move = input()
    idx = move_list.index(move) # 입력받은 명령의 인덱스 찾기
    
    nkx = kx + dx[idx]
    nky = ky + dy[idx]
    
    # 킹이 체스판 안에 있는지 확인
    if 1 <= nkx <= 8 and 1 <= nky <= 8:
        # 킹이 이동할 자리에 돌이 있다면?
        if nkx == sx and nky == sy:
            nsx = sx + dx[idx]
            nsy = sy + dy[idx]
            
            # 돌도 체스판 안에 있는지 확인
            if 1 <= nsx <= 8 and 1 <= nsy <= 8:
                kx, ky = nkx, nky
                sx, sy = nsx, nsy
            # 돌이 밖으로 나가면 킹도 못 움직임 (아무 작업 안 함)
        else:
            # 돌이 없다면 킹만 이동
            kx, ky = nkx, nky

# 4. 숫자 좌표를 다시 체스판 좌표(A1)로 변환하여 출력
print(f"{chr(kx + 64)}{ky}")
print(f"{chr(sx + 64)}{sy}")