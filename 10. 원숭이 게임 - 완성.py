# 원숭이 게임
# 게임 종료하기

import pygame

pygame.init()

screen = pygame.display.set_mode((512, 512))

pygame.display.set_caption("원숭이 게임!")

clock = pygame.time.Clock()

sysfont = pygame.font.SysFont(None, 30)
sysfont2 = pygame.font.SysFont(None, 80)

# 이미지 불러오기
monkey = pygame.image.load("image/monkey.png")
banana = pygame.image.load("image/banana.png")
field = pygame.image.load("image/field.png")

# 이미지 크기 보정 ( 사진은 이거 써야됨 )
monkey2 = pygame.transform.scale(monkey, (100, 100))
banana2 = pygame.transform.scale(banana, (100, 100))
field2 = pygame.transform.scale(field, (512, 512))

# 이미지 크기 추출
monkey_l = monkey2.get_rect().size[0]
monkey_h = monkey2.get_rect().size[1]
banana_l = banana2.get_rect().size[0]
banana_h = banana2.get_rect().size[1]
field_l = field2.get_rect().size[0]
field_h = field2.get_rect().size[1]

# 이미지 시작 좌표
monkey_x = field_l/2 - monkey_l/2
monkey_y = field_l - monkey_h
banana_x = field_l/2 - banana_l/2
banana_y = 0
# field는 좌표 (0. 0)으로 시작하면 됨

# 움직이는 바나나
banana_xx = 1
banana_yy = 1

# 움직이는 원숭이 - x 변화값
to_x = 0

# 점수
point = 0
gameover_text = sysfont2.render("GAME OVER", True, (255, 0, 0))

gameover_text_l = gameover_text.get_rect().size[0]
gameover_text_h = gameover_text.get_rect().size[1]
gameover_text_x = field_l/2 - gameover_text_l/2
gameover_text_y = field_h/2 - gameover_text_h/2

running = True

def runGame() :
    global running
    global monkey_x, monkey_y, banana_x, banana_y
    global banana_xx, banana_yy
    global to_x
    global point
    global gameover_text, gameover_text_l, gameover_text_h, gameover_text_x, gameover_text_y
    
    clock.tick(60)
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

            # 원숭이 움직이기
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    to_x = -1
                if event.key == pygame.K_RIGHT :
                    to_x = 1
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_LEFT :
                    to_x = 0
                if event.key == pygame.K_RIGHT :
                    to_x = 0
            
        # 벽에 부딪히는 원숭이 (세로 벽만 있음)
        if monkey_x < 0 :
            monkey_x = 0
        elif monkey_x > field_l - monkey_l :
            monkey_x = field_l - monkey_l
        else :
            monkey_x = monkey_x + to_x
            
        # 움직이는 바나나
        banana_x = banana_x + banana_xx
        banana_y = banana_y + banana_yy

        # 벽에 부딪히는 바나나
        # 세로 벽
        if banana_x >= field_l - banana_l :
            banana_xx = -banana_xx
            banana_x = field_l - banana_l
        elif banana_x <= 0 :
            banana_xx = -banana_xx
            banana_x = 0
        # 가로 벽, 바닥에 부딪히면 게임 종료 메세지 출력
        if banana_y >= field_h - banana_h :
            banana_yy = -banana_yy
            banana_y = field_h - banana_h
            screen.blit(gameover_text, (gameover_text_x, gameover_text_y))
            pygame.display.update()
            pygame.time.delay(10000)
            running = False
        elif banana_y <= 0 :
            banana_yy = -banana_yy
            banana_y = 0

        # 원숭이랑 바나나 사각형 처리하기
        monkey_rect = monkey2.get_rect()
        monkey_rect.left = monkey_x
        monkey_rect.top = monkey_y
        banana_rect = banana2.get_rect()
        banana_rect.left = banana_x
        banana_rect.top = banana_y

        # 원숭이랑 바나나 충돌
        if monkey_rect.colliderect(banana_rect) :
            banana_xx = -banana_xx
            banana_yy = -banana_yy
            point += 1
            
        screen.fill((255, 255, 255))
        screen.blit(field2, (0,0))

        screen.blit(monkey2, (monkey_x, monkey_y))
        screen.blit(banana2, (banana_x, banana_y))

        point_text = sysfont.render(str(point), True, (0, 0, 0))
        screen.blit(point_text, (10, 10))
            
        pygame.display.update()

    pygame.quit()

runGame()
