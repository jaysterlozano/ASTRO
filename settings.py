TITLE = "Astro"
# screen dims
WIDTH = 480
HEIGHT = 600
# frames per second
FPS = 60
# colors
WHITE = (0, 153, 0)
BLACK = (0,0,0)
REDDISH = (255,255,153)
SKY_BLUE = (143, 185, 252)
FONT_NAME = 'times new roman'
SPRITESHEET = "spritesheet_jumper.png"
SPRITESHEET2 = "spritesheet.png"
# data files
HS_FILE = "highscore.txt"
# player settings
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20
# game settings
BOOST_POWER = 60
POW_SPAWN_PCT = 13
COIN_SPAWN_PCT = 15
MOB_FREQ = 600
# layers - uses numerical value in layered sprites
PLAYER_LAYER = 2
#Platform Layers 
PLATFORM_LAYER = 1
MOVINGPFORM_LAYER = 1
# POW, MOB, and cloud layers 
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0

# platform settings
PLATFORM_LIST = [(0, HEIGHT - 40),
                 (65, HEIGHT - 300),
                 (20, HEIGHT - 350),
                 (200, HEIGHT - 150),
                 (200, HEIGHT - 450)]

# moving platform settings 
MOVINGPFORM_LIST = [(0, HEIGHT - 40),
                 (65, HEIGHT - 300),
                 (20, HEIGHT - 350),
                 (200, HEIGHT - 150),
                 (200, HEIGHT - 450)]
