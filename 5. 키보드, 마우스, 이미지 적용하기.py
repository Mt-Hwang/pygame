# 마우스로 움직이기

import pygame

pygame.init()

screen = pygame.display.set_mode((512, 512))

pygame.display.set_caption("마우스로 움직이기")

clock = pygame.time.Clock()

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

to_x = 50
to_y = 50

running = True

def runGame() :
    global running, pic_monkey2, pic_banana2, pic_field2
    global monkey_x, monkey_y, banana_x, banana_y, to_x, to_y

    fps = clock.tick(60)
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

            # 마우스에 따른 변화 설정
            if event.type == pygame.MOUSEMOTION :
                monkey_x, monkey_y = pygame.mouse.get_pos()
                            
        screen.fill((255, 255, 255))

        screen.blit(pic_field2, (0, 0))
        screen.blit(pic_monkey2, (monkey_x-50, monkey_y-50))
        # -50은 그림이 마우스의 중심에 따라 움직이게 한 것임.
        # 50은 그림의 크기를 의미!
        screen.blit(pic_banana2, (banana_x, banana_y))
        screen.blit(pic_banana2, (70, 362-40)) # monkey_y-80
        screen.blit(pic_banana2, (120, 362-180)) # monkey_y-80
        screen.blit(pic_banana2, (banana_x+150, 362-80)) # monkey_y-80
        
        pygame.display.update()

    pygame.quit()

runGame()


# 키보드로 움직이기

import pygame

pygame.init()

screen = pygame.display.set_mode((512, 512))

pygame.display.set_caption("키보드로 움직이기")

clock = pygame.time.Clock()

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

to_x = 0
to_y = 0

running = True

def runGame() :
    global running, pic_monkey2, pic_banana2, pic_field2
    global monkey_x, monkey_y, banana_x, banana_y, to_x, to_y

    fps = clock.tick(60)
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

            # 키에 따른 변화 설정
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP :
                    to_y = -1
                elif event.key == pygame.K_DOWN :
                    to_y = 1
                elif event.key == pygame.K_RIGHT :
                    to_x = 1
                elif event.key == pygame.K_LEFT :
                    to_x = -1
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_UP :
                    to_y = 0
                elif event.key == pygame.K_DOWN :
                    to_y = 0
                elif event.key == pygame.K_RIGHT :
                    to_x = 0
                elif event.key == pygame.K_LEFT :
                    to_x = 0

        monkey_x = monkey_x + to_x
        monkey_y = monkey_y + to_y
                    
        screen.fill((255, 255, 255))

        screen.blit(pic_field2, (0, 0))
        screen.blit(pic_monkey2, (monkey_x, monkey_y))
        screen.blit(pic_banana2, (banana_x, banana_y))
        screen.blit(pic_banana2, (70, 362-40)) # monkey_y-80
        screen.blit(pic_banana2, (120, 362-180)) # monkey_y-80
        screen.blit(pic_banana2, (banana_x+150, 362-80)) # monkey_y-80
        
        pygame.display.update()

    pygame.quit()

runGame()

