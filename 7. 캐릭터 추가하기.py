# 움직이는 바나나와 원숭이

import pygame

pygame.init()

screen = pygame.display.set_mode((512, 512))

pygame.display.set_caption("움직이는 바나나와 원숭이!")

# 이미지 파일 불러오기
pic_monkey = pygame.image.load("image/monkey.png")
pic_banana = pygame.image.load("image/banana.png")
pic_field = pygame.image.load("image/field.png")

# 이미지 파일 크기 조정
pic_monkey2 = pygame.transform.scale(pic_monkey, (100, 100))
pic_banana2 = pygame.transform.scale(pic_banana, (100, 100))
pic_field2 = pygame.transform.scale(pic_field, (512, 512))                       

# 이미지 파일 길이 따기
pic_monkey_width = pic_monkey2.get_rect().size[0]
pic_monkey_height = pic_monkey2.get_rect().size[1]
pic_banana_width = pic_banana2.get_rect().size[0]
pic_banana_height = pic_banana2.get_rect().size[1]
pic_field_width = pic_field2.get_rect().size[0]
pic_field_height = pic_field2.get_rect().size[1]

# 이미지 파일 좌표 따기
monkey_x = 256 - pic_monkey_width/2
monkey_y = 512 - pic_monkey_height - 50
banana_x = 256 - pic_banana_width/2
banana_y = 100

# 움직이는 바나나
banana_xx = 1
banana_yy = 1

to_x = 0

running = True

def runGame() :
    global running, pic_monkey2, pic_banana2, pic_field2
    global monkey_x, monkey_y, banana_x, banana_y, banana_xx, banana_yy, to_x
    global pic_banana_width, pic_banana_height, pic_field_height, pic_field_width
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

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

        if monkey_x < 0 :
            monkey_x = 0
        elif monkey_x > pic_field_width - pic_monkey_width :
            monkey_x = pic_field_width - pic_monkey_width
        else :
            monkey_x = monkey_x + to_x

        banana_x += banana_xx
        banana_y += banana_yy

        # 세로 벽에 부딪혔을 때
        if banana_x <= 0 :
            banana_xx = -banana_xx # 좌표 이동을 반대로
            banana_x = 0 # 바나나의 x 좌표를 일단 0으로 다시 시작
        elif banana_x >= pic_field_width - pic_banana_width : # 배경 가로 - 그림 크기
            banana_xx = -banana_xx
            banana_x = pic_field_width - pic_banana_width
        # 가로 벽에 부딪혔을 때
        if banana_y <= 0 :
            banana_yy = -banana_yy
            banana_y = 0 
        elif banana_y >= pic_field_height - pic_banana_height : 
            banana_yy = -banana_yy
            banana_y = pic_field_height - pic_banana_height
            
        screen.fill((255, 255, 255))

        screen.blit(pic_field2, (0, 0))
        
        screen.blit(pic_banana2, (banana_x, banana_y))
        
        screen.blit(pic_monkey2, (monkey_x, monkey_y+50))

        #screen.blit(pic_banana2, (70, monkey_y-40))
        #screen.blit(pic_banana2, (120, monkey_y-180))
        #screen.blit(pic_banana2, (banana_x+150, monkey_y-80))
        
        pygame.display.update()

    pygame.quit()

runGame()


