class Settings():
    def __init__(self):
        # 设置屏幕参数
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_speed_factor = 1.5
        # 设置子弹参数
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # 外星人设置
