import pygame
import sys

# 제작 시간 10분의 기적의 콮

# 화면 크기 설정
WIDTH = 570
HEIGHT = 570

# 셀 크기 설정
CELL_SIZE = 30

# 오목판 크기 설정
BOARD_WIDTH = 19
BOARD_HEIGHT = 19

# 색상 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BACKGROUND = (212, 176, 104)

# 초기화
pygame.init()

# 화면 생성
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND)

# 폰트 생성
font = pygame.font.SysFont('arial', 36)


# 오목판 그리기
def draw_board():
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)


# 돌 그리기
def draw_stone(x, y, color):
    center = (x * CELL_SIZE, y * CELL_SIZE)
    pygame.draw.circle(screen, color, center, CELL_SIZE // 2)


def check_win(board):
    # 가로 체크
    for x in range(BOARD_WIDTH - 4):
        for y in range(BOARD_HEIGHT):
            if board[x][y] is not None and board[x][y] == board[x + 1][y] == board[x + 2][y] == board[x + 3][y] == board[x + 4][y]:
                return board[x][y]

    # 세로 체크
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT - 4):
            if board[x][y] is not None and board[x][y] == board[x][y + 1] == board[x][y + 2] == board[x][y + 3] == board[x][y + 4]:
                return board[x][y]

    # 대각선 체크
    for x in range(BOARD_WIDTH - 4):
        for y in range(BOARD_HEIGHT - 4):
            if board[x][y] is not None and board[x][y] == board[x + 1][y + 1] == board[x + 2][y + 2] == board[x + 3][y + 3] == board[x + 4][y + 4]:
                return board[x][y]

    # 역대각선 체크
    for x in range(BOARD_WIDTH - 4):
        for y in range(4, BOARD_HEIGHT):
            if board[x][y] is not None and board[x][y] == board[x + 1][y - 1] == board[x + 2][y - 2] == board[x + 3][y - 3] == board[x + 4][y - 4]:
                return board[x][y]

    return None


# 게임 실행
def run_game():
    # 흑돌부터 시작
    turn = 'black'

    # 오목판 초기화
    board = [[None] * BOARD_HEIGHT for i in range(BOARD_WIDTH)]

    while True:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = round(event.pos[0] / CELL_SIZE), round(event.pos[1] / CELL_SIZE)
                if board[x][y] is None:
                    board[x][y] = turn
                    draw_stone(x, y, BLACK if turn == 'black' else WHITE)
                    if check_win(board) is not None:
                        text = font.render(turn + ' win!', True, BLACK if turn == 'black' else WHITE)
                        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
                        pygame.display.update()
                        pygame.time.delay(3000)
                        pygame.quit()
                        sys.exit()
                    turn = 'white' if turn == 'black' else 'black'

        # 화면 그리기
        draw_board()
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_HEIGHT):
                if board[x][y] is not None:
                    draw_stone(x, y, BLACK if board[x][y] == 'black' else WHITE)
        pygame.display.update()


# 게임 실행
run_game()
