"""
본 코드는 블럭의 위치를 행렬에 기반하여 작성하였습니다. 이게 numpy 행렬로 다루기 더 쉽더라구요...
예를 들면
a b c
d e f
g h i
a:0행0열, b:0행1열, c:0행2열, d:1행0열, e:1행1열, f:1행2열, g:2행0열, h:2행1열, i:2행2열 ...
과 같이 봐주시면 감사하겠습니다.
또한 블럭의 reference? 기준점?은 가장 왼쪽에 있는 점, 왼쪽에 있는 점 중에서는 가장 위에 있는 점을 기준으로 하였습니다.

그리드 크기는 15x10이며, 상하좌우 2칸씩 패딩을 추가하여 총 19x14 크기로 설정하였습니다.
유효한 좌표 범위는 row=2~16, col=2~11입니다.

sympy는 어디서 어떻게 써야할 지 몰라서 일단 안썼습니다... 의견 제시 부탁드립니다
"""

import sympy as sp
import numpy as np

def calculate_valid_positions_1(x: str) -> list[tuple[int, int]]:
    """
    9자리 2진수 문자열을 받아서 1번 블럭이 유효한 위치를 반환하는 함수
    """
    row = binary_to_decimal(x[:4]) + 2
    col = binary_to_decimal(x[4:8]) + 2
    if x[-1]=="0":
        return [(row, col), (row, col+1)]
    else:
        return [(row, col), (row+1, col)]

def calculate_valid_positions_2(x: str) -> list[tuple[int, int]]:
    """
    9자리 2진수 문자열을 받아서 2번 블럭이 유효한 위치를 반환하는 함수
    """
    row = binary_to_decimal(x[:4]) + 2
    col = binary_to_decimal(x[4:8]) + 2
    if x[-1]=="0":
        return [(row, col), (row, col+1), (row,col+2), (row, col+3)]
    else:
        return [(row, col), (row+1, col), (row+2, col), (row+3, col)]

def calculate_valid_positions_3(x: str) -> list[tuple[int, int]]:
    """
    8자리 2진수 문자열을 받아서 3번 블럭이 유효한 위치를 반환하는 함수
    """
    row = binary_to_decimal(x[:4])+2
    col = binary_to_decimal(x[4:])+2
    return [(row, col), (row+1, col+1), (row, col+1), (row+1, col)]

def calculate_valid_positions_4(x: str) -> list[tuple[int, int]]:
    """
    10자리 2진수 문자열을 받아서 4번 블럭이 유효한 위치를 반환하는 함수
    """
    row = binary_to_decimal(x[:4]) + 2
    col = binary_to_decimal(x[4:8]) + 2
    if x[-2:]=="00":
        return [(row, col), (row, col+1), (row+1, col)]
    elif x[-2:]=="01":
        return [(row, col), (row, col+1), (row+1, col+1)]
    elif x[-2:]=="10":
        return [(row, col), (row, col+1), (row-1, col+1)]
    else:
        return [(row, col), (row+1, col), (row+1, col+1)]

def calculate_valid_positions_5(x: str) -> list[tuple[int, int]]:
    """
    10자리 2진수 문자열을 받아서 5번 블럭이 유효한 위치를 반환하는 함수
    """
    row = binary_to_decimal(x[:4]) + 2
    col = binary_to_decimal(x[4:8]) + 2
    if x[-2:]=="00":
        return [(row, col), (row, col+1), (row+1, col+1), (row+1, col+2)]
    elif x[-2:]=="01":
        return [(row, col), (row+1, col), (row, col+1), (row-1, col+1)]
    elif x[-2:]=="10":
        return [(row, col), (row, col+1), (row-1, col+1), (row-1, col+2)]
    else:
        return [(row, col), (row+1, col), (row+1, col+1), (row+2, col+1)]

def calculate_valid_positions_6(x: str) -> list[tuple[int, int]]:
    """
    10자리 2진수 문자열을 받아서 6번 블럭이 유효한 위치를 반환하는 함수
    """
    row = binary_to_decimal(x[:4]) + 2
    col = binary_to_decimal(x[4:8]) + 2
    if x[-2:]=="00":
        return [(row, col), (row, col+1), (row+1, col), (row+2, col), (row+2, col+1)]
    elif x[-2:]=="01":
        return [(row, col), (row+1, col), (row, col+1), (row, col+2), (row+1, col+2)]
    elif x[-2:]=="10":
        return [(row, col), (row, col+1), (row+1, col+1), (row+2, col+1), (row+2, col)]
    else:
        return [(row, col), (row+1, col), (row+1, col+1), (row+1, col+2), (row, col+2)]

def calculate_valid_positions_7(x: str) -> list[tuple[int, int]]:
    """
    10자리 2진수 문자열을 받아서 7번 블럭이 유효한 위치를 반환하는 함수
    """
    row = binary_to_decimal(x[:4]) + 2
    col = binary_to_decimal(x[4:8]) + 2
    if x[-2:]=="00":
        return [(row, col), (row+1, col), (row+1, col+1), (row+2, col)]
    elif x[-2:]=="01":
        return [(row, col), (row, col+1), (row, col+2), (row+1, col+1)]
    elif x[-2:]=="10":
        return [(row, col), (row, col+1), (row-1, col+1), (row+1, col+1)]
    else:
        return [(row, col), (row, col+1), (row, col+2), (row-1, col+1)]

def calculate_valid_positions_8(x: str) -> list[tuple[int, int]]:
    """
    11자리 2진수 문자열을 받아서 8번 블럭이 유효한 위치를 반환하는 함수
    """
    row = binary_to_decimal(x[:4]) + 2
    col = binary_to_decimal(x[4:8]) + 2
    if x[-3:]=="000":
        return [(row, col), (row+1, col), (row+2, col), (row, col+1)]
    elif x[-3:]=="001":
        return [(row, col), (row, col+1), (row, col+2), (row+1, col+2)]
    elif x[-3:]=="010":
        return [(row, col), (row, col+1), (row-1, col+1), (row-2, col+1)]
    elif x[-3:]=="011":
        return [(row, col), (row+1, col), (row+1, col+1), (row+1, col+2)]
    elif x[-3:]=="100":
        return [(row, col), (row, col+1), (row+1, col+1), (row+2, col+1)]
    elif x[-3:]=="101":
        return [(row, col), (row, col+1), (row, col+2), (row-1, col+2)]
    elif x[-3:]=="110":
        return [(row, col), (row+1, col), (row+2, col), (row+2, col+1)]
    else:
        return [(row, col), (row+1, col), (row, col+1), (row, col+2)]

def binary_to_decimal(binary_str: str) -> int:
    """
    2진수 문자열을 10진수 정수로 변환하는 함수
    Args:
        binary_str: '0'과 '1'로만 구성된 2진수 문자열
    Returns:
        변환된 10진수 정수 값
    """
    # 입력검증증
    if not all(bit in '01' for bit in binary_str):
        raise ValueError("입력은 '0'과 '1'로만 구성되어야 합니다.")
    result = 0

    for bit in binary_str:
        result = (result << 1) | int(bit)
    return result

def create_coordinate_grid(rows, cols):
    # 초기에는 모든 값이 0인 그리드 생성
    grid = np.zeros((rows, cols), dtype=int)
    return grid

def mark_coordinate(grid, coordinates, value=1):
    """
    그리드의 여러 좌표에 값을 할당하는 함수
    Args:
        grid: 값을 할당할 그리드
        coordinates: 좌표 리스트 [(x1,y1), (x2,y2), ...] 또는 단일 좌표 튜플 (x,y)
        value: 할당할 값 (기본값 1)
    Returns:
        값이 할당된 그리드
    """
    # 단일 좌표인 경우 리스트로 변환
    if isinstance(coordinates, tuple) and len(coordinates) == 2:
        coordinates = [coordinates]
    
    # 각 좌표에 값 할당
    for x, y in coordinates:
        if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:
            grid[x, y] = value
    return grid

def check_padding_area(grid, padding_size=2):
    """
    패딩 영역에 1이 있는지 확인하는 함수
    
    패딩 영역:
    - 위쪽: row=0~1
    - 아래쪽: row=17~18
    - 왼쪽: col=0~1 (위아래 패딩 제외)
    - 오른쪽: col=12~13 (위아래 패딩 제외)
    
    Returns:
        - is_valid (bool): 패딩 영역이 모두 0이면 True, 1이 있으면 False
        - invalid_positions (list): 1이 있는 패딩 영역의 좌표 리스트
    """
    rows, cols = grid.shape
    invalid_positions = []

    # 위쪽 패딩 확인
    for i in range(padding_size):
        for j in range(cols):
            if grid[i, j] == 1:
                invalid_positions.append((i, j))
    
    # 아래쪽 패딩 확인
    for i in range(rows - padding_size, rows):
        for j in range(cols):
            if grid[i, j] == 1:
                invalid_positions.append((i, j))
    
    # 왼쪽 패딩 확인 (위아래 패딩 제외)
    for i in range(padding_size, rows - padding_size):
        for j in range(padding_size):
            if grid[i, j] == 1:
                invalid_positions.append((i, j))
    
    # 오른쪽 패딩 확인 (위아래 패딩 제외)
    for i in range(padding_size, rows - padding_size):
        for j in range(cols - padding_size, cols):
            if grid[i, j] == 1:
                invalid_positions.append((i, j))
    
    return len(invalid_positions) == 0, invalid_positions

# 사용 예시
rows, cols = 19, 14  # 15x10 그리드 + 상하좌우 2칸씩 패딩
grid = create_coordinate_grid(rows, cols)

# 단일 좌표에 값 할당하는 예시
coordinatelist = calculate_valid_positions_3("00000000")

grid = mark_coordinate(grid, coordinatelist)
print("전체 그리드:")
print(grid)

# 패딩 영역 검사
is_valid, invalid_positions = check_padding_area(grid)
print("\n패딩 검사 결과:")
print(f"유효한 그리드인가?: {is_valid}")

if not is_valid:
    print("잘못된 위치(패딩 영역에 1이 있는 좌표):", invalid_positions)