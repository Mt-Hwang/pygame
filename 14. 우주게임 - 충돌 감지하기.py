# 충돌 감지하기

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((480, 360))

pygame.display.set_caption("충돌 감지하기!")

clock = pygame.time.Clock()

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

# 움직이는 로켓
rocket_to_x = 0
rocket_random = random.randrange(0, moon_l - rocket_l)

# 움직이는 우주인
man_to_x = 0

# 별 공격
stars = []

# 공 공격
balls = []
ball_time = 0
random_time = random.randrange(0, 100)

# 로켓 사각화
rocket_rect = rocket2.get_rect()
rocket_rect.topleft = (rocket_x, rocket_y)

# 우주인 사각화
man_rect = man2.get_rect()
man_rect.topleft = (man_x, man_y)

# 별, 공 사각화 리스트
stars_rect = []
balls_rect = []

# 우주인, 로켓 체력
man_hp = 10
rocket_hp = 10

running = True

def runGame() :
    global running
    global moon_x, moon_y, moon_l, moon_h
    global star_x, star_y, star_l, star_h
    global man_x, man_y, man_l, man_h, man_to_x
    global rocket_x, rocket_y, rocket_l, rocket_h, rocket_to_x, rocket_random
    global ball_x, ball_y, ball_l, ball_h
    global moon_x, moon_y, moon_l, moon_h
    global stars, balls, ball_time, random_time
    global man_rect, rocket_rect, man_hp, rocket_hp
    global stars_rect, balls_rect

    clock.tick(50)
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

            # 우주인 움직이기 to_x 사용
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT :
                    man_to_x = 0.5
                if event.key == pygame.K_LEFT :
                    man_to_x = -0.5

                # 스페이스 누르면 우주인이 공격
                if event.key == pygame.K_SPACE :
                    star_x = man_x + star_l/2
                    stars.append([star_x, star_y])

                    # 사각화 별 추가
                    stars_rect.append(star2.get_rect())

            if event.type == pygame.KEYUP :
                if event.key == pygame.K_RIGHT :
                    man_to_x = 0
                if event.key == pygame.K_LEFT :
                    man_to_x = 0

        # 벽에 부딪히는 우주인
        if man_x < 0 :
            man_x = 0
        elif man_x > moon_l - man_l :
            man_x = moon_l - man_l
        else :
            man_x += man_to_x
        man_rect.topleft = (man_x, man_y)

        # 로켓 자동으로 움직이기
        if rocket_x < rocket_random :
            rocket_x += 0.5
        elif rocket_x > rocket_random :
            rocket_x -= 0.5
        else :
            rocket_random = random.randrange(0, moon_l - rocket_l)

        rocket_rect.topleft = (rocket_x, rocket_y)

        # 볼 자동 공격
        ball_time += 0.5

        if ball_time == random_time :
            ball_time = 0

            ball_x = rocket_x + ball_l/2
            balls.append([ball_x, ball_y])

            # 사각화 볼 추가
            balls_rect.append(ball2.get_rect())
            
        # 이미지 입력
        screen.fill((0, 0, 0))
        screen.blit(moon2, (moon_x, moon_y))
        screen.blit(man2, (man_x, man_y))
        screen.blit(rocket2, (rocket_x, rocket_y))
        screen.blit(star2, (star_x, star_y))
        screen.blit(ball2, (ball_x, ball_y))

        # 별 공격하기 (좌표가 위로 올라감)
        if len(stars) :
            for star in stars :
                i = stars.index(star)
                
                star[1] -= 1 
                screen.blit(star2, (star[0], star[1]))

                stars_rect[i].topleft = (star[0], star[1])

                if stars_rect[i].colliderect(rocket_rect) :
                    stars.remove(star)
                    stars_rect.remove(stars_rect[i])
                    rocket_hp -= 1
                    

                # 하늘에 닿으면 별 사라져야 됨
                if star[1] <= 0 :
                    stars.remove(star)
                    stars_rect.remove(stars_rect[i])

        if len(balls) :
            for ball in balls :
                i = balls.index(ball)
                
                ball[1] += 1
                screen.blit(ball2, (ball[0], ball[1]))

                balls_rect[i].topleft = (ball[0], ball[1])

                if balls_rect[i].colliderect(man_rect) :
                    balls.remove(ball)
                    balls_rect.remove(balls_rect[i])
                    man_hp -= 1

                if ball[1] >= moon_h :
                    balls.remove(ball)
                    balls_rect.remove(balls_rect[i])

        print(rocket_hp, man_hp)
        
        pygame.display.update()

    pygame.quit()

runGame()

