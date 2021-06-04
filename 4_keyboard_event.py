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

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(
    "/Users/jeongheekim/Desktop/Python Workspace/pygame_basic/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴 rect() 사각형.
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 세로 크기
character_x_pos = (screen_width / 2) - \
                  (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 캐릭터 위치 (가로축)
character_y_pos = screen_height - character_height  # 화면 세로 크기의 가장 아래에 위치 (세로축)

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프 (이걸 해야 게임창이 계속 켜져 있는다)
running = True  # 게임이 진행중이가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로 이동
                to_x -= 5  # to_x = to_x - 5 / 5만큼 왼쪽 이동
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP:  # 방향키를 내 손가락에서 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0  # 더이상 움직이지 않는다
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.fill((0, 0, 255))  # RGB 색깔 넣기 / 파란색
    # screen.blit(background, (0, 0))  # 배경 그리기 = 위 코드랑 결과 동일
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 위치
    pygame.display.update()  # 게임화면을 다시 그리기!(반드시 계속 호출되어야 하는 부분)

# pygame 종료
pygame.quit()
