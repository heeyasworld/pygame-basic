import pygame
import random

pygame.init()  # 초기화 작업 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))  # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("Heeya Game")  # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
# background = pygame.image.load(
# "/Users/jeongheekim/Desktop/Python Workspace/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(
    "/Users/jeongheekim/Desktop/Python Workspace/pygame_basic/ghost70_107.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴 rect() 사각형.
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 세로 크기
character_x_pos = (screen_width / 2) - \
                  (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 캐릭터 위치 (가로축)
character_y_pos = screen_height - character_height  # 화면 세로 크기의 가장 아래에 위치 (세로축)

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6  # fps랑 무관하게 캐릭터의 속도는 일정하다

# 적 enemy 캐릭터
enemy = pygame.image.load(
    "/Users/jeongheekim/Desktop/Python Workspace/pygame_basic/cute.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴 rect() 사각형.
enemy_width = enemy_size[0]  # 캐릭터의 가로 크기
enemy_height = enemy_size[1]  # 세로 크기
# 화면 가로의 절반 크기에 해당하는 곳에 캐릭터 위치 (가로축)
enemy_x_pos = random.randint(0, (screen_width - enemy_width))
enemy_y_pos = 0  # 화면 세로 크기의 가장 아래에 위치 (세로축)

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성(폰트(디폴트), 크기)

# 총 시간
total_time = 30

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()  # 현재 tick 정보를 받아옴


# 이벤트 루프 (이걸 해야 게임창이 계속 켜져 있는다)
running = True  # 게임이 진행중이가?
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정
    # print("fps : "+str(clock.get_fps())) # 터미널에 frp 표시해줌

    # 캐릭터가 1초동안 100만큼 이동을 해야 함
    # 10 fps : 1초동안 10번 동작 -> 1번에 몇 만큼 이동? 10만큼! 10 * 10 = 100 => 부자연스럽게 뚝뚝 끊김
    # 20 fps : 1초동안 20번 동작 -> 1번에 5만큼 이동! 5 * 20 = 100 => 자연스럽게 이동됨

    # 프레임수가 높으면 캐릭터 동작이 자연스럽게 이어지고 끊김 현상이 적다
    # 프레임수가 적으면 캐릭터 동작이 끊기는 느낌 줄 수 있다

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로 이동
                to_x -= character_speed  # to_x = to_x - 5 / 5만큼 왼쪽 이동
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:  # 방향키를 내 손가락에서 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0  # 더이상 움직이지 않는다
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt  # 여기 dt는 왜 곱하는 거임??
    character_y_pos += to_y * dt

    # 가로 경계값 처리 (캐릭터가 화면 밖으로 탈주 못하도록!)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()  # 실제 캐릭터가 화면상에서 위치하고 있는 렉텡글 정보를 업데이트함
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    # 사각형 기준으로 충돌이 있었는지 체크해줌 character_rect 가 (enemy_rect)랑 충돌이 있었는지 colliderect가 봐줌
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False  # 게임종료

    screen.fill((0, 0, 255))  # RGB 색깔 넣기 / 파란색
    # screen.blit(background, (0, 0))  # 배경 그리기 = 위 코드랑 결과 동일
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 위치
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # location of enemy

    # 타이머 집어 넣기
    # 경과 시간 넣기 elapse[일랩스] 시간이 흐르다, 경과하다 / elapsed time [일랩스드 타임] 경과 시간
    # 1000으로 나눠야 우리 시간 기준 '초'로 출력됨, 원래는 ms(밀리세컨드)로 나옴.
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과시간 = 현재 시간 - 시작 시간 = 현재 9:05 - 시작시간 9:01 = 경과시간은 4분

    timer = game_font.render(
        str(int(total_time - elapsed_time)), True, (255, 255, 255))  # 출력할 글자(시간), True, 글자 색상(rgb 흰색)
    # render : 실제로 글자를 그려주는 것
    screen.blit(timer, (10, 10))  # timer 위치

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("time out")
        running = False

    pygame.display.update()  # 게임화면을 다시 그리기!(반드시 계속 호출되어야 하는 부분)

# 잠시 대기 : 게임 시간 초과되더라도 바로 안 꺼지고 0초인 상태로 2초 뒤 꺼지게 함
pygame.time.delay(2000)  # 2초 정도 대기 (2000ms)

# pygame 종료
pygame.quit()
