import sympy as sp
import numpy as np

def bstr_divider(x: str) -> list[str]:
    pass

def calculate_valid_positions_1(x: str) -> list[tuple[int, int]]:
    """
    9자리 2진수 문자열을 받아서 블럭이 유효한 위치를 반환하는 함수
    """
    x_decimal = binary_to_decimal(x[:4]) + 2
    y_decimal = binary_to_decimal(x[4:]) + 2
    if x[-1]:
        return [(x_decimal, y_decimal), (x_decimal+1, y_decimal)]
    else:
        return [(x_decimal, y_decimal), (x_decimal, y_decimal+1)]
def calculate_valid_positions_2(x: str) -> list[tuple[int, int]]:
    pass
def calculate_valid_positions_4(x: str) -> list[tuple[int, int]]:
    pass
def calculate_valid_positions_5(x: str) -> list[tuple[int, int]]:
    pass
def calculate_valid_positions_6(x: str) -> list[tuple[int, int]]:
    pass
def calculate_valid_positions_7(x: str) -> list[tuple[int, int]]:
    pass
def calculate_valid_positions_8(x: str) -> list[tuple[int, int]]:
    pass



def calculate_valid_positions_3(x: str) -> list[tuple[int, int]]:
    """
    8자리 2진수 문자열을 받아서 블럭이 유효한 위치를 반환하는 함수
    """
    x_decimal = binary_to_decimal(x[:4])+2
    y_decimal = binary_to_decimal(x[4:])+2
    return [(x_decimal, y_decimal), (x_decimal+1, y_decimal+1), (x_decimal+0, y_decimal+1), (x_decimal+1, y_decimal+0)]


# 문자열로 표현된 2진수를 다루는 함수 예시
def binary_to_decimal(binary_str: str) -> int:
    """
    2진수 문자열을 10진수 정수로 변환하는 함수
    
    Args:
        binary_str: '0'과 '1'로만 구성된 2진수 문자열
        
    Returns:
        변환된 10진수 정수 값
        
    Examples:
        >>> binary_to_decimal('1010')
        10
        >>> binary_to_decimal('11111111')
        255
    """
    # 입력 검증
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
rows, cols = 17, 12  # 15x10 그리드 + 상하좌우 2칸씩 패딩
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





