import pygame

pygame.init()  # 초기화 작업 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))  # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("Heeya Game")  # 게임 이름

# 배경 이미지 불러오기
# background = pygame.image.load(
# "/Users/jeongheekim/Desktop/Python Workspace/pygame_basic/background.png")


# 이벤트 루프 (이걸 해야 게임창이 계속 켜져 있는다)
running = True  # 게임이 진행중이가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

    screen.fill((0, 0, 255))  # RGB 색깔 넣기 / 파란색
    # screen.blit(background, (0, 0))  # 배경 그리기
    pygame.display.update()  # 게임화면을 다시 그리기!(반드시 계속 호출되어야 하는 부분)

# pygame 종료
pygame.quit()
