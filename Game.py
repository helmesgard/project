import random
import pygame
import sys
import pygame_menu

pygame.init()
bg_image = pygame.image.load("6.jpg")
size_block = 20
color = (100, 200, 0)
white = (255, 255, 255)
blue = (150, 155, 250)
black = (0, 0, 0)
header_color = (0, 204, 153)
blocks = 20
snake_color = (255, 0, 100)
otstup = 1
otstup_zag = 70
fps = 60
orange = (255, 165, 0)
size = [size_block * blocks + 2 * size_block + otstup * blocks,
        size_block * blocks + 2 * size_block + otstup * blocks + otstup_zag]
print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake_pro')
timer = pygame.time.Clock()
courier = pygame.font.SysFont("Arial", 36)
kolvo = 25

class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < size_block and 0 <= self.y < size_block

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


def draw_bl(colors, i, Block):
    pygame.draw.rect(screen, colors, [size_block + Block * size_block + otstup * (Block + 1),
                                      otstup_zag + size_block + i * size_block + otstup * (i + 1),
                                      size_block, size_block])


def start_the_game():
    def get_random_empty_block():
        x = random.randint(0, blocks - 1)
        y = random.randint(0, blocks - 1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake:
            empty_block.x = random.randint(0, blocks - 1)
            empty_block.y = random.randint(0, blocks - 1)
        return empty_block

    snake = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
    apple = get_random_empty_block()
    d_row = 0
    d_col = 1
    total = 0
    speed = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    d_row = -1
                    d_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    d_row = 1
                    d_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:
                    d_row = 0
                    d_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    d_row = 0
                    d_col = 1

        screen.fill(color)
        pygame.draw.rect(screen, header_color, [0, 0, size[0], otstup_zag])

        text_total = courier.render(f"Total: {total}", 0, white)
        text_speed = courier.render(f"Speed: {speed}", 0, white)
        screen.blit(text_total, (blocks, blocks))
        screen.blit(text_speed, (blocks + 230, blocks))

        for i in range(blocks):
            for Block in range(blocks):
                if (i + Block) % 2 == 0:
                    colors = blue
                else:
                    colors = white

                draw_bl(colors, i, Block)

        head = snake[-1]
        if not head.is_inside():
            break

        draw_bl(orange, apple.x, apple.y)
        for Block in snake:
            draw_bl(snake_color, Block.x, Block.y)

        pygame.display.flip()

        if apple == head:
            total += 1
            speed = total // 5 + 1
            snake.append(apple)
            apple = get_random_empty_block()

        d_row = d_row
        d_col = d_col
        new_head = SnakeBlock(head.x + d_row, head.y + d_col)

        if new_head in snake:
            break
        snake.append(new_head)
        snake.pop(0)
        pygame.display.flip()
        timer.tick(5 + speed)


def start_the_game_2():
    def get_random_empty_block():
        x = random.randint(0, blocks - 1)
        y = random.randint(0, blocks - 1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake:
            empty_block.x = random.randint(0, blocks - 1)
            empty_block.y = random.randint(0, blocks - 1)
        return empty_block

    def get_random_block():
        for i in range(kolvo):
            x = random.randint(0, blocks - 1)
            y = random.randint(0, blocks - 1)
            empty_block = SnakeBlock(x, y)
            while empty_block in snake:
                empty_block.x = random.randint(0, blocks - 1)
                empty_block.y = random.randint(0, blocks - 1)
            return empty_block

    snake = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
    apple = get_random_empty_block()
    BLOCK = get_random_block()
    ASD = get_random_block()
    ZXC = get_random_block()
    ert = get_random_block()
    qwe = get_random_block()
    xcv = get_random_block()
    tyu = get_random_block()
    d_row = 0
    d_col = 1
    total = 0
    speed = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    d_row = -1
                    d_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    d_row = 1
                    d_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:
                    d_row = 0
                    d_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    d_row = 0
                    d_col = 1

        screen.fill(color)
        pygame.draw.rect(screen, header_color, [0, 0, size[0], otstup_zag])

        text_total = courier.render(f"Total: {total}", 0, white)
        text_speed = courier.render(f"Speed: {speed}", 0, white)
        screen.blit(text_total, (blocks, blocks))
        screen.blit(text_speed, (blocks + 230, blocks))

        for i in range(blocks):
            for Block in range(blocks):
                if (i + Block) % 2 == 0:
                    colors = blue
                else:
                    colors = white

                draw_bl(colors, i, Block)

        head = snake[-1]
        if not head.is_inside():
            break

        draw_bl(orange, apple.x, apple.y)
        for Block in snake:
            draw_bl(snake_color, Block.x, Block.y)

        draw_bl(black, ert.x, ert.y)
        for Block in snake:
            draw_bl(snake_color, Block.x, Block.y)

        if ert == head:
            break

        draw_bl(black, xcv.x, xcv.y)
        for Block in snake:
            draw_bl(snake_color, Block.x, Block.y)

        if xcv == head:
            break

        draw_bl(black, qwe.x, qwe.y)
        for Block in snake:
            draw_bl(snake_color, Block.x, Block.y)

        if qwe == head:
            break

        draw_bl(black, tyu.x, tyu.y)
        for Block in snake:
            draw_bl(snake_color, Block.x, Block.y)

        if tyu == head:
            break

        draw_bl(black, ASD.x, ASD.y)
        for Block in snake:
            draw_bl(snake_color, Block.x, Block.y)

        draw_bl(black, ZXC.x, ZXC.y)
        for Block in snake:
            draw_bl(snake_color, Block.x, Block.y)

        draw_bl(black, BLOCK.x, BLOCK.y)
        for Block in snake:
            draw_bl(snake_color, Block.x, Block.y)

        pygame.display.flip()

        if apple == head:
            total += 1
            speed = total // 5 + 1
            snake.append(apple)
            apple = get_random_empty_block()

        if ASD == head:
            break

        if ZXC == head:
            break

        if BLOCK == head:
            break

        d_row = d_row
        d_col = d_col
        new_head = SnakeBlock(head.x + d_row, head.y + d_col)

        if new_head in snake:
            break
        snake.append(new_head)
        snake.pop(0)
        pygame.display.flip()
        timer.tick(5 + speed)


menu = pygame_menu.Menu('Добро пожаловать!', 460, 300,
                        theme=pygame_menu.themes.THEME_GREEN)

menu.add.text_input('Name :', default='Player 1')
menu.add.button('level 1', start_the_game)
menu.add.button('level 2', start_the_game_2)
menu.add.button('Quit', pygame_menu.events.EXIT)
while True:
    screen.blit(bg_image, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()
