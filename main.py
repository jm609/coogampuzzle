"""
본 코드는 블럭의 위치를 카르테시안 좌표계(1사분면)에 기반하여 작성하였습니다.
예를 들면 (x, y) 좌표에서:
- x는 왼쪽에서 오른쪽으로 증가
- y는 아래에서 위로 증가
과 같이 봐주시면 감사하겠습니다.
또한 블럭의 reference? 기준점?은 가장 왼쪽에 있는 점, 왼쪽에 있는 점 중에서는 가장 아래에 있는 점을 기준으로 하였습니다.
sympy는 어디서 어떻게 써야할 지 몰라서 일단 안썼습니다... 의견 제시 부탁드립니다다
"""

import sympy as sp
import numpy as np

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

def bstr_divider(x: str) -> list[str]:
    """
    385자리의 이진문자열을 적절히 나눠주는 함수
    """
    pass

# 행렬 좌표를 카르테시안 좌표로 변환하는 함수 추가
def matrix_to_cartesian(matrix_coords, grid_height):
    """
    행렬 좌표를 카르테시안 좌표로 변환하는 함수
    Args:
        matrix_coords: 행렬 좌표 리스트 [(row1, col1), (row2, col2), ...]
        grid_height: 그리드의 높이
    Returns:
        카르테시안 좌표 리스트 [(x1, y1), (x2, y2), ...]
    """
    cartesian_coords = []
    for row, col in matrix_coords:
        # x는 col과 동일, y는 grid_height에서 row를 뺀 값
        x = col
        y = grid_height - row
        cartesian_coords.append((x, y))
    return cartesian_coords

def calculate_valid_positions_1(x: str) -> list[tuple[int, int]]:
    """
    9자리 2진수 문자열을 받아서 1번 블럭이 유효한 위치를 반환하는 함수
    카르테시안 좌표계 기준
    """
    col = binary_to_decimal(x[:4]) + 2  # x 좌표
    row = binary_to_decimal(x[4:8]) + 2  # 임시 y 좌표 (행렬 기준)
    
    # 그리드 높이 (패딩 포함)
    grid_height = 17 - 1  # 0-indexed
    
    if x[-1]=="0":
        # 수평 배치 (오른쪽으로 1칸)
        matrix_coords = [(row, col), (row, col+1)]
    else:
        # 수직 배치 (위로 1칸)
        matrix_coords = [(row, col), (row-1, col)]  # 카르테시안에서는 y가 위로 증가하므로 row 감소
    
    return matrix_to_cartesian(matrix_coords, grid_height)

def calculate_valid_positions_2(x: str) -> list[tuple[int, int]]:
    """
    9자리 2진수 문자열을 받아서 2번 블럭이 유효한 위치를 반환하는 함수
    카르테시안 좌표계 기준
    """
    col = binary_to_decimal(x[:4]) + 2  # x 좌표
    row = binary_to_decimal(x[4:8]) + 2  # 임시 y 좌표 (행렬 기준)
    
    # 그리드 높이 (패딩 포함)
    grid_height = 17 - 1  # 0-indexed
    
    if x[-1]=="0":
        # 수평 배치 (오른쪽으로 3칸)
        matrix_coords = [(row, col), (row, col+1), (row, col+2), (row, col+3)]
    else:
        # 수직 배치 (위로 3칸)
        matrix_coords = [(row, col), (row-1, col), (row-2, col), (row-3, col)]
    
    return matrix_to_cartesian(matrix_coords, grid_height)

def calculate_valid_positions_3(x: str) -> list[tuple[int, int]]:
    """
    8자리 2진수 문자열을 받아서 3번 블럭이 유효한 위치를 반환하는 함수
    카르테시안 좌표계 기준
    """
    col = binary_to_decimal(x[:4]) + 2  # x 좌표
    row = binary_to_decimal(x[4:]) + 2  # 임시 y 좌표 (행렬 기준)
    
    # 그리드 높이 (패딩 포함)
    grid_height = 17 - 1  # 0-indexed
    
    # 2x2 정사각형
    matrix_coords = [(row, col), (row-1, col), (row, col+1), (row-1, col+1)]
    
    return matrix_to_cartesian(matrix_coords, grid_height)

def calculate_valid_positions_4(x: str) -> list[tuple[int, int]]:
    """
    10자리 2진수 문자열을 받아서 4번 블럭이 유효한 위치를 반환하는 함수
    카르테시안 좌표계 기준
    """
    col = binary_to_decimal(x[:4]) + 2  # x 좌표
    row = binary_to_decimal(x[4:8]) + 2  # 임시 y 좌표 (행렬 기준)
    
    # 그리드 높이 (패딩 포함)
    grid_height = 17 - 1  # 0-indexed
    
    if x[-2:]=="00":
        # L 모양 (오른쪽으로 1칸, 위로 1칸)
        matrix_coords = [(row, col), (row, col+1), (row-1, col)]
    elif x[-2:]=="01":
        # ┘ 모양
        matrix_coords = [(row, col), (row, col+1), (row-1, col+1)]
    elif x[-2:]=="10":
        # ┌ 모양
        matrix_coords = [(row, col), (row, col+1), (row+1, col+1)]
    else:
        # ┐ 모양
        matrix_coords = [(row, col), (row-1, col), (row-1, col+1)]
    
    return matrix_to_cartesian(matrix_coords, grid_height)

def calculate_valid_positions_5(x: str) -> list[tuple[int, int]]:
    """
    10자리 2진수 문자열을 받아서 5번 블럭이 유효한 위치를 반환하는 함수
    카르테시안 좌표계 기준
    """
    col = binary_to_decimal(x[:4]) + 2  # x 좌표
    row = binary_to_decimal(x[4:8]) + 2  # 임시 y 좌표 (행렬 기준)
    
    # 그리드 높이 (패딩 포함)
    grid_height = 17 - 1  # 0-indexed
    
    if x[-2:]=="00":
        matrix_coords = [(row, col), (row, col+1), (row-1, col+1), (row-1, col+2)]
    elif x[-2:]=="01":
        matrix_coords = [(row, col), (row-1, col), (row, col+1), (row+1, col+1)]
    elif x[-2:]=="10":
        matrix_coords = [(row, col), (row, col+1), (row+1, col+1), (row+1, col+2)]
    else:
        matrix_coords = [(row, col), (row-1, col), (row-1, col+1), (row-2, col+1)]
    
    return matrix_to_cartesian(matrix_coords, grid_height)

def calculate_valid_positions_6(x: str) -> list[tuple[int, int]]:
    """
    10자리 2진수 문자열을 받아서 6번 블럭이 유효한 위치를 반환하는 함수
    카르테시안 좌표계 기준
    """
    col = binary_to_decimal(x[:4]) + 2  # x 좌표
    row = binary_to_decimal(x[4:8]) + 2  # 임시 y 좌표 (행렬 기준)
    
    # 그리드 높이 (패딩 포함)
    grid_height = 17 - 1  # 0-indexed
    
    if x[-2:]=="00":
        matrix_coords = [(row, col), (row, col+1), (row-1, col), (row-2, col), (row-2, col+1)]
    elif x[-2:]=="01":
        matrix_coords = [(row, col), (row-1, col), (row, col+1), (row, col+2), (row-1, col+2)]
    elif x[-2:]=="10":
        matrix_coords = [(row, col), (row, col+1), (row-1, col+1), (row-2, col+1), (row-2, col)]
    else:
        matrix_coords = [(row, col), (row-1, col), (row-1, col+1), (row-1, col+2), (row, col+2)]
    
    return matrix_to_cartesian(matrix_coords, grid_height)

def calculate_valid_positions_7(x: str) -> list[tuple[int, int]]:
    """
    10자리 2진수 문자열을 받아서 7번 블럭이 유효한 위치를 반환하는 함수
    카르테시안 좌표계 기준
    """
    col = binary_to_decimal(x[:4]) + 2  # x 좌표
    row = binary_to_decimal(x[4:8]) + 2  # 임시 y 좌표 (행렬 기준)
    
    # 그리드 높이 (패딩 포함)
    grid_height = 17 - 1  # 0-indexed
    
    if x[-2:]=="00":
        matrix_coords = [(row, col), (row-1, col), (row-1, col+1), (row-2, col)]
    elif x[-2:]=="01":
        matrix_coords = [(row, col), (row, col+1), (row, col+2), (row-1, col+1)]
    elif x[-2:]=="10":
        matrix_coords = [(row, col), (row, col+1), (row+1, col+1), (row-1, col+1)]
    else:
        matrix_coords = [(row, col), (row, col+1), (row, col+2), (row+1, col+1)]
    
    return matrix_to_cartesian(matrix_coords, grid_height)

def calculate_valid_positions_8(x: str) -> list[tuple[int, int]]:
    """
    11자리 2진수 문자열을 받아서 8번 블럭이 유효한 위치를 반환하는 함수
    카르테시안 좌표계 기준
    """
    col = binary_to_decimal(x[:4]) + 2  # x 좌표
    row = binary_to_decimal(x[4:8]) + 2  # 임시 y 좌표 (행렬 기준)
    
    # 그리드 높이 (패딩 포함)
    grid_height = 17 - 1  # 0-indexed
    
    if x[-3:]=="000":
        matrix_coords = [(row, col), (row-1, col), (row-2, col), (row, col+1)]
    elif x[-3:]=="001":
        matrix_coords = [(row, col), (row, col+1), (row, col+2), (row-1, col+2)]
    elif x[-3:]=="010":
        matrix_coords = [(row, col), (row, col+1), (row+1, col+1), (row+2, col+1)]
    elif x[-3:]=="011":
        matrix_coords = [(row, col), (row-1, col), (row-1, col+1), (row-1, col+2)]
    elif x[-3:]=="100":
        matrix_coords = [(row, col), (row, col+1), (row-1, col+1), (row-2, col+1)]
    elif x[-3:]=="101":
        matrix_coords = [(row, col), (row, col+1), (row, col+2), (row+1, col+2)]
    elif x[-3:]=="110":
        matrix_coords = [(row, col), (row-1, col), (row-2, col), (row-2, col+1)]
    else:
        matrix_coords = [(row, col), (row-1, col), (row, col+1), (row, col+2)]
    
    return matrix_to_cartesian(matrix_coords, grid_height)

def create_coordinate_grid(rows, cols):
    # 초기에는 모든 값이 0인 그리드 생성
    grid = np.zeros((rows, cols), dtype=int)
    return grid

def mark_coordinate(grid, coordinates, value=1):
    """
    그리드의 여러 좌표에 값을 할당하는 함수 (카르테시안 좌표 입력)
    Args:
        grid: 값을 할당할 그리드
        coordinates: 카르테시안 좌표 리스트 [(x1,y1), (x2,y2), ...] 또는 단일 좌표 튜플 (x,y)
        value: 할당할 값 (기본값 1)
    Returns:
        값이 할당된 그리드
    """
    # 단일 좌표인 경우 리스트로 변환
    if isinstance(coordinates, tuple) and len(coordinates) == 2:
        coordinates = [coordinates]
    
    # 그리드 높이 (패딩 포함)
    grid_height = grid.shape[0] - 1  # 0-indexed
    
    # 각 좌표에 값 할당 (카르테시안 -> 행렬 변환)
    for x, y in coordinates:
        # 카르테시안 좌표를 행렬 좌표로 변환
        row = grid_height - y
        col = x
        
        if 0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]:
            grid[row, col] = value
    return grid

def check_padding_area(grid, padding_size=2):
    """
    패딩 영역에 1이 있는지 확인하는 함수
    Returns:
        - is_valid (bool): 패딩 영역이 모두 0이면 True, 1이 있으면 False
        - invalid_positions (list): 1이 있는 패딩 영역의 좌표 리스트 (카르테시안 좌표계)
    """
    rows, cols = grid.shape
    grid_height = rows - 1  # 0-indexed
    invalid_positions = []
    
    # 위쪽 패딩 확인 (카르테시안에서는 위쪽이 y값이 큰 영역)
    for i in range(padding_size):
        for j in range(cols):
            if grid[i, j] == 1:
                # 행렬 좌표를 카르테시안 좌표로 변환
                x = j
                y = grid_height - i
                invalid_positions.append((x, y))
    
    # 아래쪽 패딩 확인 (카르테시안에서는 아래쪽이 y값이 작은 영역)
    for i in range(rows - padding_size, rows):
        for j in range(cols):
            if grid[i, j] == 1:
                # 행렬 좌표를 카르테시안 좌표로 변환
                x = j
                y = grid_height - i
                invalid_positions.append((x, y))
    
    # 왼쪽 패딩 확인 (위아래 패딩 제외)
    for i in range(padding_size, rows - padding_size):
        for j in range(padding_size):
            if grid[i, j] == 1:
                # 행렬 좌표를 카르테시안 좌표로 변환
                x = j
                y = grid_height - i
                invalid_positions.append((x, y))
    
    # 오른쪽 패딩 확인 (위아래 패딩 제외)
    for i in range(padding_size, rows - padding_size):
        for j in range(cols - padding_size, cols):
            if grid[i, j] == 1:
                # 행렬 좌표를 카르테시안 좌표로 변환
                x = j
                y = grid_height - i
                invalid_positions.append((x, y))
    
    return len(invalid_positions) == 0, invalid_positions

# 카르테시안 좌표를 출력하는 함수 추가
def print_cartesian_coordinates(grid):
    """
    그리드에서 값이 1인 위치의 카르테시안 좌표를 출력하는 함수
    """
    rows, cols = grid.shape
    grid_height = rows - 1  # 0-indexed
    cartesian_coords = []
    
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 1:
                # 행렬 좌표를 카르테시안 좌표로 변환
                x = j
                y = grid_height - i
                cartesian_coords.append((x, y))
    
    print("\n카르테시안 좌표계 기준 블럭 위치:")
    for coord in sorted(cartesian_coords):
        print(f"x={coord[0]}, y={coord[1]}")

# 사용 예시
rows, cols = 17, 12  # 15x10 그리드 + 상하좌우 2칸씩 패딩
grid = create_coordinate_grid(rows, cols)

# 카르테시안 좌표계에서 블럭 배치 테스트
coordinatelist = (
    calculate_valid_positions_1("001000100") +  # 1번 블럭
    calculate_valid_positions_2("010001000") +  # 2번 블럭
    calculate_valid_positions_3("00000000") +   # 3번 블럭
    calculate_valid_positions_4("0000011000") + # 4번 블럭
    calculate_valid_positions_5("0000001000") + # 5번 블럭
    calculate_valid_positions_6("0000010000")   # 6번 블럭
)

grid = mark_coordinate(grid, coordinatelist)
print("전체 그리드 (카르테시안 좌표계 기준):")
print(grid)

# 패딩 영역 검사
is_valid, invalid_positions = check_padding_area(grid)
print("\n패딩 검사 결과:")
print(f"유효한 그리드인가?: {is_valid}")

if not is_valid:
    print("잘못된 위치(패딩 영역에 1이 있는 좌표):", invalid_positions)

# 카르테시안 좌표 출력
print_cartesian_coordinates(grid)
