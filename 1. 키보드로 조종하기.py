# 키보드로 조종하기

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 360))

pygame.display.set_caption("키보드로 조종하기!")

print(screen.get_size())

center_x = screen.get_size()[0]//2  # 240
center_y = screen.get_size()[1]//2  # 180

to_x = 0
to_y = 0

running = True

def runGame() :
    global running, center_x, center_y, to_x, to_y
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

            if event.type == pygame.KEYDOWN :
                print(event.key)

                if event.key == 97 :
                    print("a 누름")

                if event.key == pygame.K_UP :
                    print("UP")
                    center_y -= 10
                if event.key == pygame.K_DOWN :
                    print("DOWN")
                    center_y += 10
                if event.key == pygame.K_RIGHT :
                    print("RIGHT")
                    center_x += 10
                if event.key == pygame.K_LEFT :
                    print("LEFT")
                    center_x -= 10

        screen.fill((255, 255, 255))

        pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), 20)
        
        pygame.display.update()

    pygame.quit()

runGame()


# 계속 누른 상태로 조종하기

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 360))

pygame.display.set_caption("계속 누른 상태로 조종하기!")

print(screen.get_size())

center_x = screen.get_size()[0]//2  # 240
center_y = screen.get_size()[1]//2  # 180

to_x = 0
to_y = 0

running = True

fps = pygame.time.Clock()

def runGame() :
    global running, center_x, center_y, to_x, to_y
    
    while running :
        fps.tick(60)
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

            if event.type == pygame.KEYDOWN :
                print(event.key)

                if event.key == 97 :
                    print("a 누름")

                if event.key == pygame.K_UP :
                    print("UP")
                    to_y = -1
                if event.key == pygame.K_DOWN :
                    print("DOWN")
                    to_y = 1
                if event.key == pygame.K_RIGHT :
                    print("RIGHT")
                    to_x = 1
                if event.key == pygame.K_LEFT :
                    print("LEFT")
                    to_x = -1

            if event.type == pygame.KEYUP :
                if event.key == pygame.K_UP :
                    print("UP")
                    to_y = 0
                if event.key == pygame.K_DOWN :
                    print("DOWN")
                    to_y = 0
                if event.key == pygame.K_RIGHT :
                    print("RIGHT")
                    to_x = 0
                if event.key == pygame.K_LEFT :
                    print("LEFT")
                    to_x = 0

        center_x += to_x
        center_y -= to_y

        screen.fill((255, 255, 255))

        pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), 1)
        
        pygame.display.update()

    pygame.quit()

runGame()

