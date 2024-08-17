import random
import pygame
import os
from pygame import mixer

mixer.init()
pygame.init()

# GLOABL VARIABLES
fps = 60
screen_width = 289
screen_height = 511
# game_running = True
clock = pygame.time.Clock()
# bird_x = 30
# bird_y = 100
# bird_fall_vel = 20

# IMAGES
Bird_img = pygame.image.load("Flappy bird.png")
bird_img = pygame.transform.scale(Bird_img, (30, 25))

# bird_fall_img = pygame.transform.rotate(Bird_img, -10)
# bird_fall_imgb = pygame.transform.scale(bird_fall_img, (30, 25))


Background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(Background_img, (screen_width, screen_height))

Home_screen = pygame.image.load("homescreen.jpg")
home_screen = pygame.transform.scale(Home_screen, (screen_width, screen_height))

Base = pygame.image.load("base.jpg")
base_img = pygame.transform.scale(Base, (500, 120))

Pipe_img = pygame.image.load("pillar.png")
upperpipe_img = pygame.transform.scale(Pipe_img, (400, 300))
upperpipe2_img = pygame.transform.scale(Pipe_img, (400, 300))

Lowerpipe = pygame.transform.rotate(pygame.image.load("pillar.png"), 180)
lowerpipe_img = pygame.transform.scale(Lowerpipe, (400, 300))
lowerpipe2_img = pygame.transform.scale(Lowerpipe, (400, 300))

# DISPLAY
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FlappyBird by Suzaan Khan")
pygame.display.set_icon(pygame.image.load("Flappy bird.png"))

font = pygame.font.SysFont("sigmar one", 23)
font2 = pygame.font.SysFont("sigmar one", 40)
font3 = pygame.font.SysFont("sigmar one", 27)

if (not os.path.exists("birdscore.py")):
    with open("birdscore.py", "w") as f:
        f.write("0")
with open("birdscore.py", "r") as f:
    hiscore = f.read()


def type_text(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    gamewindow.blit(screen_text, [x, y])


def type_text2(text, colour, x, y):
    screen_text = font2.render(text, True, colour)
    gamewindow.blit(screen_text, [x, y])


def type_text3(text, colour, x, y):
    screen_text = font3.render(text, True, colour)
    gamewindow.blit(screen_text, [x, y])

def stop_music():
    mixer.music.stop()

def welcome():
    welcome = True
    while welcome:
        gamewindow.blit(home_screen, (0, 0))
        type_text("HIGH SCORE: " + str(hiscore), (0, 0, 0), 90, 15)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    maingame()
            if event.type == pygame.QUIT:
                # welcome = False
                pygame.quit()


def point_sound():
    pygame.mixer.music.load("pointsoundeffect.wav")
    pygame.mixer.music.play()


def maingame():
    # INGAME VARIABLES
    game_running = True
    bird_x = 30
    bird_y = 100
    fly_velocity = 0
    fly = -11
    gravity = 1.7
    base_x_pos = 0
    playerflapped = False

    pipe_gap = 400
    pipe_gap2 = 400

    upperpipe_x = 140
    lowerpipe_x = 128

    upperpipe2_x = 126
    lowerpipe2_x = 111

    upperpipe_height = random.randint(-260, -20)
    lowerpipe_height = upperpipe_height + pipe_gap

    upperpipe2_height = random.randint(-260, -20)
    lowerpipe2_height = upperpipe2_height + pipe_gap2

    upperpipe_speed = 2
    lowerpipe_speed = 2

    upperpipe2_speed = 0
    lowerpipe2_speed = 0

    point_rect_x = 290
    point_rect_x2 = 290
    score = 0
    gameover = False
    global hiscore
    # COLOURS
    white = (255, 255, 255)
    black = (0, 0, 0)
    list = ('YOU DIED!', "      LOL", " HAHAHA", "NOOOOOB", "HUEHUEHU", "       XD", "    BRUH")
    random_message = random.choice(list)
    blue = (0, 128, 255)
    darkblue = (102, 102, 255)
    lightblue = (92, 136, 225)
    borderblue = (0, 0, 255)
    lightbrown = (255, 227, 146)
    darkbrown = (51, 25, 0)
    s = pygame.mixer.Sound("wingsoundeffect.wav")

    while game_running:
        if gameover:
            with open("birdscore.py", "w") as f:
                f.write(str(hiscore))
            main_box_rect_border = pygame.draw.rect(gamewindow, darkbrown, [5, screen_height / 2 - 55, 279, 110])
            main_box_rect = pygame.draw.rect(gamewindow, lightbrown, [10, screen_height / 2 - 50, 269, 100])
            random_text_rect_border = pygame.draw.rect(gamewindow, darkbrown, [5, 55, 279, 57])
            random_text_rect = pygame.draw.rect(gamewindow, lightbrown, [10, 60, 269, 47])
            score_rect_border = pygame.draw.rect(gamewindow, darkbrown, [5, 135, 279, 45])
            score_rect = pygame.draw.rect(gamewindow, lightbrown, [10, 140, 269, 35])
            home_rect_border = pygame.draw.rect(gamewindow, darkbrown, [5, 325, 279, 40])
            pygame.draw.rect(gamewindow, lightbrown, [10, 330, 269, 30])
            type_text3("Score: " + str(score) + "                 Best: " + str(hiscore), darkbrown, 18, 148)
            type_text2(random_message, darkbrown, 70, 70)
            type_text('YOU DIED! PRESS SPACE TO PLAY', darkbrown, 16, screen_height / 2 - 40)
            type_text('OR', darkbrown, 130, (screen_height / 2) - 12)
            type_text("PRESS ENTER TO EXIT", darkbrown, 55, screen_height / 2 + 20)
            type_text("PRESS 'H' TO GO HOME", darkbrown, 55, 337)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        stop_music()
                        maingame()
                    if event.key == pygame.K_RETURN:
                        game_running = False
                    if event.key == pygame.K_h:
                        stop_music()
                        welcome()
                    if event.key == pygame.K_r:
                        hiscore = 0

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        playerflapped = True
                        s.play()
                        if playerflapped:
                            gravity = 0
                            fly_velocity = fly

                if event.type == pygame.KEYUP:
                    gravity = 1.7
                    fly_velocity = 0

            if base_x_pos == -200:
                base_x_pos = 0

            bird_y = bird_y + fly_velocity
            bird_y = bird_y + gravity

            if point_rect_x <= bird_x or point_rect_x2 <= bird_x:
                pygame.mixer.music.load("pointsoundeffect_usethis.wav")
                point_sound()

            # if point_rect_x2 == bird_x:
            #     score = score + 1
            #     point_sound()

            upperpipe_x = upperpipe_x - upperpipe_speed
            lowerpipe_x = lowerpipe_x - lowerpipe_speed

            upperpipe2_x = upperpipe2_x - upperpipe2_speed
            lowerpipe2_x = lowerpipe2_x - lowerpipe2_speed

            point_rect_x = point_rect_x - lowerpipe_speed
            point_rect_x2 = point_rect_x2 - lowerpipe2_speed

            if upperpipe_x and lowerpipe_x < -225:
                score = score + 1
                if score > int(hiscore):
                    hiscore = score
                point_rect_x = 287
                upperpipe_height = random.randint(-220, -60)
                lowerpipe_height = upperpipe_height + pipe_gap
                upperpipe_x = 140
                lowerpipe_x = 128

            if upperpipe2_x and lowerpipe2_x < -225:
                upperpipe2_speed = 0
                lowerpipe2_speed = 0
                upperpipe2_height = random.randint(-220, -60)
                lowerpipe2_height = upperpipe2_height + pipe_gap2
                upperpipe2_x = 126
                lowerpipe2_x = 111
                point_rect_x2 = 290
                score = score + 1
                if score > int(hiscore):
                    hiscore = score

            if bird_y < 0 or bird_y > 375:
                gameover = True
                pygame.mixer.music.load("game over.wav")
                pygame.mixer.music.play()

            if score >= 15:
                pipe_gap = 395
                pipe_gap2 = 395

            if score >= 25:
                pipe_gap = 390
                pipe_gap2 = 390

            if score >= 30:
                pipe_gap = 385
                pipe_gap2 = 385

            if score >= 35:
                pipe_gap = 380
                pipe_gap2 = 380

            upperpipes_rect = pygame.draw.rect(gamewindow, (0, 0, 0), [upperpipe_x + 167, upperpipe_height, 50, 293])
            lowerpipes_rect = pygame.draw.rect(gamewindow, (0, 0, 0),
                                               [lowerpipe_x + 182, lowerpipe_height + 10, 50, 293])

            upperpipes2_rect = pygame.draw.rect(gamewindow, (0, 0, 0), [upperpipe2_x + 165, upperpipe2_height, 50, 293])
            lowerpipes2_rect = pygame.draw.rect(gamewindow, (0, 0, 0),
                                                [lowerpipe2_x + 180, lowerpipe2_height + 7, 50, 293])

            bird_rect = pygame.draw.rect(gamewindow, (0, 0, 0), [bird_x, bird_y, 25, 25])
            point_rect = pygame.draw.rect(gamewindow, (0, 0, 0), [point_rect_x, 0, 25, 25])
            point_rect2 = pygame.draw.rect(gamewindow, (0, 0, 0), [point_rect_x2, 0, 25, 25])
            gamewindow.blit(background_img, (0, 0))

            gamewindow.blit(upperpipe_img, (upperpipe_x, upperpipe_height))
            gamewindow.blit(lowerpipe_img, (lowerpipe_x, lowerpipe_height))

            gamewindow.blit(upperpipe2_img, (upperpipe2_x, upperpipe2_height))
            gamewindow.blit(lowerpipe2_img, (lowerpipe2_x, lowerpipe2_height))

            gamewindow.blit(bird_img, (bird_x, bird_y))

            type_text(str(score), (0, 0, 0), 140, 30)

            if bird_rect.colliderect(upperpipes_rect) or bird_rect.colliderect(lowerpipes_rect):
                gameover = True
                pygame.mixer.music.load("game over.wav")
                pygame.mixer.music.play()

            if bird_rect.colliderect(upperpipes2_rect) or bird_rect.colliderect(lowerpipes2_rect):
                gameover = True
                pygame.mixer.music.load("game over.wav")
                pygame.mixer.music.play()

            if upperpipe_x <= -50:
                upperpipe2_speed = 2
                lowerpipe2_speed = 2

            base_x_pos = base_x_pos - 2
            gamewindow.blit(base_img, (base_x_pos, 396))
            pygame.display.update()
            clock.tick(fps)
    pygame.quit()
    quit()

welcome()
