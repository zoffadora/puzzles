import os
import pygame
import random


def draw_swaps():
    font = pygame.font.SysFont('Arial', 64)
    text = font.render(f"Количество перестановок: {swaps}", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
    pygame.draw.rect(screen, (255, 255, 255), text_rect.inflate(4, 4))
    screen.blit(text, text_rect)


def game_over():
    font = pygame.font.SysFont('Arial', 64)
    text = font.render("Ура, картинка собрана!", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.draw.rect(screen, (255, 255, 255), text_rect.inflate(4, 4))
    screen.blit(text, text_rect)


def draw_tiles():
    for i in range(len(tiles)):
        tile = tiles[i]
        row = i // ROWS
        col = i % COLS
        x = col * (TILE_WIDTH + MARGIN) + MARGIN
        y = row * (TILE_HEIGHT + MARGIN) + MARGIN
        if i == selected:
            pygame.draw.rect(screen, (0, 255, 0),
                             (x - MARGIN, y - MARGIN, TILE_WIDTH + MARGIN * 2, TILE_HEIGHT + MARGIN * 2))
        screen.blit(tile, (x, y))


def run_menu():
    # Создаем прямоугольники-кнопки
    start_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 80, 200, 60)
    level_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 60)
    quit_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 80, 200, 60)

    in_menu = True
    while in_menu:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, None
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_click = True

        # Проверяем colliderect
        if mouse_click:
            mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)

            if mouse_rect.colliderect(start_rect):
                return True, None  # Начинаем игру с выбором уровня
            elif mouse_rect.colliderect(level_rect):
                return True, "level_select"  # Переходим к выбору уровня
            elif mouse_rect.colliderect(quit_rect):
                return False, None  # Выходим

        # Отрисовка меню - белый фон
        screen.fill((255, 255, 255))

        # Рисуем кнопки без контура
        if start_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (0, 255, 0), start_rect)
        else:
            pygame.draw.rect(screen, (0, 100, 0), start_rect)

        if level_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (255, 165, 0), level_rect)
        else:
            pygame.draw.rect(screen, (139, 69, 19), level_rect)

        if quit_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (255, 0, 0), quit_rect)
        else:
            pygame.draw.rect(screen, (100, 0, 0), quit_rect)

        # Рисуем текст
        font = pygame.font.SysFont('Arial', 36)
        start_text = font.render("Старт", True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=start_rect.center)
        screen.blit(start_text, start_text_rect)

        level_text = font.render("Уровень", True, (255, 255, 255))
        level_text_rect = level_text.get_rect(center=level_rect.center)
        screen.blit(level_text, level_text_rect)

        quit_text = font.render("Выход", True, (255, 255, 255))
        quit_text_rect = quit_text.get_rect(center=quit_rect.center)
        screen.blit(quit_text, quit_text_rect)

        # Заголовок
        title_font = pygame.font.SysFont('Arial', 72)
        title = title_font.render("Пятнашки", True, (0, 0, 255))
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title, title_rect)

        pygame.display.flip()
        clock.tick(60)


def choose_level():
    """Меню выбора уровня сложности"""
    easy_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 80, 200, 60)
    medium_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 60)
    hard_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 80, 200, 60)
    back_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 160, 200, 50)

    selecting = True
    while selecting:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_click = True

        if mouse_click:
            mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)

            if mouse_rect.colliderect(easy_rect):
                return 3  # Легкий
            elif mouse_rect.colliderect(medium_rect):
                return 6  # Средний
            elif mouse_rect.colliderect(hard_rect):
                return 9 # Сложный
            elif mouse_rect.colliderect(back_rect):
                return "back"  # Вернуться в главное меню

        # Отрисовка
        screen.fill((255, 255, 255))

        # Заголовок
        title_font = pygame.font.SysFont('Arial', 60)
        title = title_font.render("Выберите уровень сложности", True, (0, 0, 255))
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        screen.blit(title, title_rect)

        # Кнопки без контура
        if easy_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (0, 255, 0), easy_rect)
        else:
            pygame.draw.rect(screen, (0, 150, 0), easy_rect)

        if medium_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (255, 165, 0), medium_rect)
        else:
            pygame.draw.rect(screen, (200, 100, 0), medium_rect)

        if hard_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (255, 0, 0), hard_rect)
        else:
            pygame.draw.rect(screen, (150, 0, 0), hard_rect)

        if back_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (128, 128, 128), back_rect)
        else:
            pygame.draw.rect(screen, (100, 100, 100), back_rect)

        # Текст на кнопках
        font = pygame.font.SysFont('Arial', 32)
        easy_text = font.render("Легкий)", True, (255, 255, 255))
        easy_text_rect = easy_text.get_rect(center=easy_rect.center)
        screen.blit(easy_text, easy_text_rect)

        medium_text = font.render("Средний )", True, (255, 255, 255))
        medium_text_rect = medium_text.get_rect(center=medium_rect.center)
        screen.blit(medium_text, medium_text_rect)

        hard_text = font.render("Сложный )", True, (255, 255, 255))
        hard_text_rect = hard_text.get_rect(center=hard_rect.center)
        screen.blit(hard_text, hard_text_rect)

        back_text = font.render("Назад", True, (255, 255, 255))
        back_text_rect = back_text.get_rect(center=back_rect.center)
        screen.blit(back_text, back_text_rect)

        pygame.display.flip()
        clock.tick(60)


def start_game(size):
    """Запускает игру с выбранным размером поля"""
    global ROWS, COLS, TILE_WIDTH, TILE_HEIGHT, tiles, origin_tiles, selected, swaps

    ROWS = size
    COLS = size

    # Загрузка картинки
    pictures = os.listdir('pictures')
    picture = random.choice(pictures)
    image = pygame.image.load('pictures/' + picture)

    # Масштабируем картинку под размер экрана
    max_tile_size = min(SCREEN_WIDTH // COLS, SCREEN_HEIGHT // ROWS) - MARGIN * 2
    TILE_WIDTH = max_tile_size
    TILE_HEIGHT = max_tile_size

    image = pygame.transform.scale(image, (TILE_WIDTH * COLS, TILE_HEIGHT * ROWS))

    # Создаем тайлы
    tiles = []
    for i in range(ROWS):
        for j in range(COLS):
            rect = pygame.Rect(j * TILE_WIDTH, i * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
            tile = image.subsurface(rect)
            tiles.append(tile)

    origin_tiles = tiles.copy()
    random.shuffle(tiles)

    selected = None
    swaps = 0

    # Игровой цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i in range(len(tiles)):
                    row = i // ROWS
                    col = i % COLS
                    x = col * (TILE_WIDTH + MARGIN) + MARGIN
                    y = row * (TILE_HEIGHT + MARGIN) + MARGIN

                    if x <= mouse_x <= x + TILE_WIDTH and y <= mouse_y <= y + TILE_HEIGHT:
                        if selected is not None and selected != i:
                            tiles[i], tiles[selected] = tiles[selected], tiles[i]
                            selected = None
                            swaps += 1
                        elif selected == i:
                            selected = None
                        else:
                            selected = i

        screen.fill((255, 255, 255))
        draw_tiles()
        draw_swaps()

        if tiles == origin_tiles:
            game_over()
            pygame.display.flip()
            pygame.time.wait(3000)
            return True  # Возвращаемся в меню

        pygame.display.flip()
        clock.tick(60)

    return True


# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MARGIN = 2
ROWS = 3
COLS = 3
TILE_WIDTH = 0
TILE_HEIGHT = 0

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Пятнашки')
clock = pygame.time.Clock()

# Глобальные переменные
tiles = []
origin_tiles = []
selected = None
swaps = 0

# Главный цикл меню
game_running = True
while game_running:
    result, action = run_menu()

    if not result:  # Выход из игры
        game_running = False
    elif action == "level_select":  # Выбор уровня
        level = choose_level()
        if level == "back":
            continue
        elif level is not None:
            # Запускаем игру с выбранным уровнем
            if not start_game(level):
                game_running = False
    else:  # Обычный старт (легкий уровень по умолчанию)
        if not start_game(3):  # По умолчанию 8x8
            game_running = False

pygame.quit()