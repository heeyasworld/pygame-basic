import pygame
import random
#########################################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("You can be a special ghost")

# FPS
clock = pygame.time.Clock()
#########################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등 설정)

# 캐릭터 만들기
character = pygame.image.load(
    "/Users/jeongheekim/Desktop/Python Workspace/pygame_basic/ghost70_107.png")  # 70*107
character_size = character.get_rect().size  # 이미지의 크기를 구해옴 rect() 사각형.
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동 위치
to_x = 0

# 이동 속도
character_speed = 10  # fps랑 무관하게 캐릭터의 속도는 일정하다

# 적 enemy 캐릭터
enemy = pygame.image.load(
    "/Users/jeongheekim/Desktop/Python Workspace/pygame_basic/cute.png")  # 80*80
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴 rect() 사각형.
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, (screen_width - enemy_width))
enemy_y_pos = 0

enemy2 = pygame.image.load(
    "/Users/jeongheekim/Desktop/Python Workspace/pygame_basic/cute.png")  # 80*80
enemy2_size = enemy2.get_rect().size  # 이미지의 크기를 구해옴 rect() 사각형.
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_x_pos = random.randint(0, (screen_width - enemy2_width))
enemy2_y_pos = 0

enemy3 = pygame.image.load(
    "/Users/jeongheekim/Desktop/Python Workspace/pygame_basic/cute.png")  # 80*80
enemy3_size = enemy3.get_rect().size  # 이미지의 크기를 구해옴 rect() 사각형.
enemy3_width = enemy3_size[0]
enemy3_height = enemy3_size[1]
enemy3_x_pos = random.randint(0, (screen_width - enemy3_width))
enemy3_y_pos = 0

enemy4 = pygame.image.load(
    "/Users/jeongheekim/Desktop/Python Workspace/pygame_basic/cute.png")  # 80*80
enemy4_size = enemy4.get_rect().size  # 이미지의 크기를 구해옴 rect() 사각형.
enemy4_width = enemy4_size[0]
enemy4_height = enemy4_size[1]
enemy4_x_pos = random.randint(0, (screen_width - enemy4_width))
enemy4_y_pos = 0

# 이동 속도
enemy_speed = 10

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성(폰트(디폴트), 크기)

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()  # 현재 tick 정보를 받아옴

# win
win = pygame.image.load(
    "/Users/jeongheekim/Desktop/Python Workspace/pygame_basic/win.png")
win_size = win.get_rect().size
win_width = win_size[0]
win_height = win_size[1]

# lose
lose = pygame.image.load(
    "/Users/jeongheekim/Desktop/Python Workspace/pygame_basic/lose.png")
lose_size = lose.get_rect().size
lose_width = lose_size[0]
lose_height = lose_size[1]


running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    # 가로 경계값 처리 (캐릭터가 화면 밖으로 탈주 못하도록!)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed  # 이거만 해도 ..... 적이 밑으로 쭉쭉 내려옴 ㅅㅂ....뭐야..
    if enemy_y_pos == screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, (screen_width - enemy_width))

    enemy2_y_pos += enemy_speed
    if enemy2_y_pos == screen_height:
        enemy2_y_pos = 0
        enemy2_x_pos = random.randint(0, (screen_width - enemy2_width))

    enemy3_y_pos += enemy_speed
    if enemy3_y_pos == screen_height:
        enemy3_y_pos = 0
        enemy3_x_pos = random.randint(0, (screen_width - enemy3_width))

    enemy4_y_pos += enemy_speed
    if enemy4_y_pos == screen_height:
        enemy4_y_pos = 0
        enemy4_x_pos = random.randint(0, (screen_width - enemy4_width))

    # 5. 화면 그리기

    screen.fill((0, 0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos+50))
    screen.blit(enemy3, (enemy3_x_pos, enemy3_y_pos+70))
    screen.blit(enemy4, (enemy4_x_pos, enemy4_y_pos+70))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(
        str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))
    if total_time - elapsed_time <= 0:
        print("time out")
        running = False
        screen.blit(win, ((screen_width / 2) - (win_width / 2),
                    (screen_height / 2) - (win_height / 2)))

    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()  # 실제 캐릭터가 화면상에서 위치하고 있는 렉텡글 정보를 업데이트함
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos

    enemy3_rect = enemy3.get_rect()
    enemy3_rect.left = enemy3_x_pos
    enemy3_rect.top = enemy3_y_pos

    enemy4_rect = enemy4.get_rect()
    enemy4_rect.left = enemy4_x_pos
    enemy4_rect.top = enemy4_y_pos

    # 충돌 체크
    # 사각형 기준으로 충돌이 있었는지 체크해줌 character_rect 가 (enemy_rect)랑 충돌이 있었는지 colliderect가 봐줌
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
        screen.blit(lose, ((screen_width / 2) - (lose_width / 2),
                           (screen_height / 2) - (lose_height / 2)))  # 이거 작동안되서 4. 충돌처리 위로 5. 화면 그리기 올리니까 된다. 헐.
    elif character_rect.colliderect(enemy2_rect):
        print("충돌했어요")
        running = False
        screen.blit(lose, ((screen_width / 2) - (lose_width / 2),
                           (screen_height / 2) - (lose_height / 2)))
    elif character_rect.colliderect(enemy3_rect):
        print("충돌했어요")
        running = False
        screen.blit(lose, ((screen_width / 2) - (lose_width / 2),
                           (screen_height / 2) - (lose_height / 2)))
    elif character_rect.colliderect(enemy4_rect):
        print("충돌했어요")
        running = False
        screen.blit(lose, ((screen_width / 2) - (lose_width / 2),
                           (screen_height / 2) - (lose_height / 2)))
    pygame.display.update()

pygame.time.delay(4000)
# pygame 종료
pygame.quit()
