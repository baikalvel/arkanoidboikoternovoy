import os
import sys
import pygame
from random import randrange as rnd

pygame.mixer.init()


class Game:
    def __init__(self, Choice, volumemus, volumeeffect):
        self.Choice = Choice
        self.volumemus = volumemus
        self.volumeeffect = volumeeffect

    def Arkanoid(self):
        sound1 = pygame.mixer.Sound('data/фонК.mp3')
        sound2 = pygame.mixer.Sound('data/удар.mp3')
        if self.volumemus:
            sound1.play()
        Choice = self.Choice
        Mnoz = 1
        pygame.font.init()
        pygame.mixer.init()
        GameFont = pygame.font.SysFont('calibri', 30)
        WIDTH, HEIGHT = 800, 600
        fps = 60
        # paddle settings
        paddle_w = 330
        paddle_h = 35
        paddle_speed = 15
        # ball settings
        ball_radius = 20
        ball_speed = 5
        ball_rect = int(ball_radius * 2 ** 0.5)
        if Choice == 0:
            paddle_w = 500
            paddle_speed = 15
            ball_speed = 3
            Mnoz = 1
        if Choice == 1:
            paddle_w = 250
            paddle_speed = 15
            ball_speed = 7
            Mnoz = 5
        if Choice == 2:
            paddle_w = 200
            paddle_speed = 20
            ball_speed = 9
            Mnoz = 10
        if Choice == 3:
            paddle_w = 100
            paddle_speed = 30
            ball_speed = 10
            Mnoz = 30
        paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)
        ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
        dx, dy = 1, -1
        # blocks settings
        block_list = [pygame.Rect(5 + 80 * i, 5 + 50 * j, 70, 30) for i in range(10) for j in range(4)]
        color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(4)]
        pygame.init()
        sc = pygame.display.set_mode((WIDTH, HEIGHT))
        img = pygame.image.load('data/main.jpg').convert()
        running = True
        clock = pygame.time.Clock()
        vs = 200
        ts = 1

        def detect_collision(dx, dy, ball, rect):
            if self.volumeeffect == True:
                sound2.play()
            if dx > 0:
                delta_x = ball.right - rect.left
            else:
                delta_x = rect.right - ball.left
            if dy > 0:
                delta_y = ball.bottom - rect.top
            else:
                delta_y = rect.bottom - ball.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = -dx, -dy
            elif delta_x > delta_y:
                dy = -dy
            elif delta_y > delta_x:
                dx = -dx
            return dx, dy

        Record = 0
        Okno = True
        while Okno:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sound1.stop()
                    Okno = False

            sc.blit(img, (0, 0))
            [pygame.draw.rect(sc, color_list[color], block) for color, block in enumerate(block_list)]
            pygame.draw.rect(sc, pygame.Color('darkorange'), paddle)
            pygame.draw.circle(sc, pygame.Color('white'), ball.center, ball_radius)
            ball.x += ball_speed * dx
            ball.y += ball_speed * dy
            if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
                dx = -dx
            if ball.centery < ball_radius:
                dy = -dy
            if ball.colliderect(paddle) and dy > 0:
                dx, dy = detect_collision(dx, dy, ball, paddle)
            hit_index = ball.collidelist(block_list)
            if hit_index != -1:
                Record += (1 * Mnoz)
                hit_rect = block_list.pop(hit_index)
                hit_color = color_list.pop(hit_index)
                dx, dy = detect_collision(dx, dy, ball, hit_rect)
                hit_rect.inflate_ip(ball.width * 3, ball.height * 3)
                pygame.draw.rect(sc, hit_color, hit_rect)
                fps += 2
            ScoreText = GameFont.render('Очки: ' + str(Record), 1, (255, 255, 255))
            if ball.bottom > HEIGHT:
                sound1.stop()
                sc.blit(img, (0, 0))
                r = Menu(Record)
                r.Menua()

            elif not len(block_list):
                sc.blit(img, (0, 0))
                sound1.stop()
                r = Menu(Record)
                r.Menua()
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and paddle.left > 0:
                paddle.left -= paddle_speed
            if key[pygame.K_RIGHT] and paddle.right < WIDTH:
                paddle.right += paddle_speed
            sc.blit(ScoreText, (20, 20))
            pygame.display.flip()
            clock.tick(fps)


Choice = 0
pygame.font.init()
GameFont = pygame.font.SysFont('data/sdsad.ttf', 25)
GameFont2 = pygame.font.SysFont('data/sdsad.ttf', 40)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)

    else:
        image = image.convert_alpha()
    return image


class Menu:
    def __init__(self, score):
        self.score = score
        pass

    def Menua(self):
        text_2 = 'Guide'
        text_3 = 'Developers'
        text_4 = 'Easy'
        text_5 = 'Medium'
        text_6 = 'Hard'
        WIDTH, HEIGHT = 1200, 800
        fps = 60
        pygame.init()
        menu = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("меню")
        clock = pygame.time.Clock()
        # background image
        img = pygame.image.load('data/1.jpg').convert()
        img_1 = pygame.image.load('data/1.jpg').convert()
        startimg = pygame.image.load('data/1.jpg').convert()
        platform_w = 330
        platform_h = 35
        platform_speed = 15
        platform = pygame.Rect(WIDTH // 2 - platform_w // 2, HEIGHT - platform_h - 10, platform_w, platform_h)
        P = False
        easy_lvl = pygame.Rect(100, 50, 200, 40)
        high_lvl = pygame.Rect(100, 100, 200, 40)
        ultrahight_lvl = pygame.Rect(100, 150, 200, 40)
        mega_lvl = pygame.Rect(100, 200, 200, 40)
        schet = pygame.Rect(100, 680, 600, 100)
        tabl = pygame.Rect(800, 50, 600, 430)
        obvod = pygame.Rect(90, 40, 220, 110)
        Menu = False
        Menu_setting = True
        Easy = GameFont.render('Легкая сложность', 1, (255, 255, 255))
        Hard = GameFont.render('Средняя сложность', 1, (255, 255, 255))
        Ultrahard = GameFont.render('Высокая сложность', 1, (255, 255, 255))
        Megahard = GameFont.render('Terminator', 1, (255, 255, 255))
        Version = GameFont2.render('Version : alpha_1.0 #inst:@new_erra #vk:vk.com/baikalvel', 1, (255, 0, 0))
        volume = True
        Play = True
        musik = True
        effect = True
        Choice = 0
        s = self.score
        add_score(self.score)
        pa = maksznah()
        while Play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    Play = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                    if musik:
                        musik = False
                    else:
                        musik = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_F2:
                    if effect:
                        effect = False
                    else:
                        effect = True

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    Ark = Game(Choice, musik, effect)
                    Ark.Arkanoid()
                    sys.exit()
                    Play = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    if Choice == 0 or Choice <= 0:
                        Choice = 3
                    else:
                        Choice -= 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    if Choice == 3 or Choice >= 3:
                        Choice = 0
                    else:
                        Choice += 1
                menu.blit(img_1, (0, 0))
                if Choice == 0:
                    obvod = pygame.Rect(95, 45, 210, 50)
                    pygame.draw.rect(menu, pygame.Color('white'), obvod)
                if Choice == 1:
                    obvod = pygame.Rect(95, 95, 210, 50)
                    pygame.draw.rect(menu, pygame.Color('white'), obvod)
                if Choice == 2:
                    obvod = pygame.Rect(95, 145, 210, 50)
                    pygame.draw.rect(menu, pygame.Color('white'), obvod)
                if Choice == 3:
                    obvod = pygame.Rect(95, 195, 210, 50)
                    pygame.draw.rect(menu, pygame.Color('white'), obvod)
                if effect:
                    effkl = 'Включена'
                else:
                    effkl = 'Выключена'
                if musik:
                    musvkl = 'Включена'
                else:
                    musvkl = 'Выключена'
                pygame.draw.rect(menu, pygame.Color('blue'), easy_lvl)
                pygame.draw.rect(menu, pygame.Color('purple'), high_lvl)
                pygame.draw.rect(menu, pygame.Color('red'), ultrahight_lvl)
                pygame.draw.rect(menu, pygame.Color('green'), mega_lvl)
                pygame.draw.rect(menu, pygame.Color('black'), schet)
                pygame.draw.rect(menu, pygame.Color('black'), tabl)
            Score = GameFont2.render('Очков в прошлой игре: ' + str(s), 1, (255, 255, 255))
            Record = GameFont2.render(f'Рекорд : ' + pa, 1, (255, 255, 255))
            Msk = GameFont.render(f'Музыка (F1) {musvkl}', 1, (255, 255, 255))
            Efk = GameFont.render(f'Звуковые эффекты (F2) {effkl}', 1, (255, 255, 255))
            menu.blit(Msk, (10, 430))
            menu.blit(Efk, (10, 400))
            menu.blit(Easy, (110, 60))
            menu.blit(Hard, (110, 110))
            menu.blit(Ultrahard, (110, 160))
            menu.blit(Megahard, (110, 210))
            menu.blit(Score, (320, 55))
            menu.blit(Record, (320, 110))
            menu.blit(Version, (0, 525))
            pygame.display.flip()
            clock.tick(fps)


def maksznah():
    slova_dva = []
    f = open('data/State.txt', 'r')
    slova = f.read().split('\n')
    for s in slova:
        if s == '\n' or s == '':
            pass
        else:
            slova_dva.append(s)
    f.close()
    slova_dva.sort(key=int, reverse=True)
    return slova_dva[0]


def add_score(score):
    slova_dva = []
    f = open('data/State.txt', 'r')
    slova = f.read().splitlines()
    slova.append(score)
    for s in slova:
        if s == '\n':
            pass
        else:
            slova_dva.append(s)
    f.close()
    f = open('data/State.txt', 'w')
    for i in slova_dva:
        if i == '\n':
            pass
        else:
            f.write(str(i) + '\n')


t = open('data/Score.txt', 'r')
s = t.read()
t.close()
slova = maksznah()
r = Menu(s)
r.Menua()
