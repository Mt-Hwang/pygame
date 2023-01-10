# 이미지 적용하기

import pygame

pygame.init()

screen = pygame.display.set_mode((512, 512))

pygame.display.set_caption("이미지 적용하기!")

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


running = True

def runGame() :
    global running, pic_monkey2, pic_banana2, pic_field2
    global monkey_x, monkey_y, banana_x, banana_y
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        screen.fill((255, 255, 255))

        screen.blit(pic_field2, (0, 0))
        screen.blit(pic_monkey2, (monkey_x, monkey_y))
        screen.blit(pic_banana2, (banana_x, banana_y))
        screen.blit(pic_banana2, (70, monkey_y-40))
        screen.blit(pic_banana2, (120, monkey_y-180))
        screen.blit(pic_banana2, (banana_x+150, monkey_y-80))
        
        pygame.display.update()

    pygame.quit()

runGame()

