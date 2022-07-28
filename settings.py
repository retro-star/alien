class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 外星人设置
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        # 开火速度
        self.fire_speed = 50
