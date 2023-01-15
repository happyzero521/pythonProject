import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化屏幕、设置和对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_width))
    pygame.display.set_caption("外星人入侵")
    # 创建飞船
    ship = Ship(ai_settings, screen)

    # 设置游戏主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


# 启动游戏程序
run_game()
