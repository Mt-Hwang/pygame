# 우주게임 - 화면 구성

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 360))

pygame.display.set_caption("우주게임 - 화면 구성!")


# 이미지 불러오기
man = pygame.image.load("image/man.png")
rocket = pygame.image.load("image/rocket.png")
star = pygame.image.load("image/star.png")
ball = pygame.image.load("image/ball.png")
moon = pygame.image.load("image/moon.png")

# 이미지 크기 조정
man2 = pygame.transform.scale(man, (100, 75))
rocket2 = pygame.transform.scale(rocket, (80, 80))
star2 = pygame.transform.scale(star, (20, 20))
ball2 = pygame.transform.scale(ball, (20, 20))
moon2 = pygame.transform.scale(moon, (480, 360))

# 이미지 가로, 세로 크기 구하기
man_l = man2.get_rect().size[0]
man_h = man2.get_rect().size[1]
rocket_l = rocket2.get_rect().size[0]
rocket_h = rocket2.get_rect().size[1]
star_l = star2.get_rect().size[0]
star_h = star2.get_rect().size[1]
ball_l = ball2.get_rect().size[0]
ball_h = ball2.get_rect().size[1]
moon_l = moon2.get_rect().size[0]
moon_h = moon2.get_rect().size[1]

# 이미지 좌표
man_x = moon_l/2 - man_l/2
man_y = moon_h - man_h
rocket_x = moon_l/2 - rocket_l/2
rocket_y = 0
star_x = moon_l/2 - star_l/2
star_y = moon_h - man_h - star_h
ball_x = moon_l/2 - ball_l/2
ball_y = rocket_h
moon_x = 0
moon_y = 0

running = True

def runGame() :
    global running
    global moon_x, moon_y, moon_l, moon_h
    global man_x, man_y, man_l, man_h
    global rocket_x, rocket_y, rocket_l, rocket_h
    global ball_x, ball_y, ball_l, ball_h
    global moon_x, moon_y, moon_l, moon_h

    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        # 이미지 입력
        screen.fill((0, 0, 0))
        screen.blit(moon2, (moon_x, moon_y))
        screen.blit(man2, (man_x, man_y))
        screen.blit(rocket2, (rocket_x, rocket_y))
        screen.blit(star2, (star_x, star_y))
        screen.blit(ball2, (ball_x, ball_y))
        
        pygame.display.update()

    pygame.quit()

runGame()

