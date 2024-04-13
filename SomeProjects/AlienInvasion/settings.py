class Settings:
    def __init__(self):
        # this class contains the setting of the game
        self.screen_w = 1200
        self.screen_h = 700
        self.bg_color = (230,230,230)

        # Ships Setting
        self.ship_speed = 1
        self.ship_speed_v = 2

        # bullets Things
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3


        #alien speed
        self.alien_speed = 1.0