# 캐릭터 충돌

import pygame

pygame.init()

screen = pygame.display.set_mode((512, 512))

pygame.display.set_caption("캐릭터 충돌!")

clock = pygame.time.Clock()

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

running = True

def runGame() :
    global running
    global monkey_x, monkey_y, banana_x, banana_y
    global banana_xx, banana_yy
    global to_x

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
        # 가로 벽
        if banana_y >= field_h - banana_h :
            banana_yy = -banana_yy
            banana_y = field_h - banana_h
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
            
        screen.fill((255, 255, 255))
        screen.blit(field2, (0,0))

        screen.blit(monkey2, (monkey_x, monkey_y))
        screen.blit(banana2, (banana_x, banana_y))
            
        pygame.display.update()

    pygame.quit()

runGame()
