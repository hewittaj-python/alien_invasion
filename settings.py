class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Alien Settings
        self.fleet_drop_speed = 20

        # Bullet Settings
        self.bullets_allowed = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_height = 15
        self.bullet_width = 3

        # Screen settings
        self.bg_color = (230, 230, 230)
        self.screen_height = 800
        self.screen_width = 1200
        
        # Ship settings
        self.ship_limit = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # Fleet direction of 1 represents right, -1 represents left.
        self.alien_speed = 1.0
        self.bullet_speed = 10
        self.fleet_direction = 1
        self.ship_speed = 4.5
        
