from pico2d import *
import game_world
import game_framework
import random
import common


class Ball:
    image = None

    def __init__(self, x = 400, y = 300, throwin_speed = 15, throwin_angle = 45):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100,common.court.w - 100), random.randint(100,common.court.h - 100)




    def draw(self):
        sx = self.x - common.court.window_left
        sy = self.y - common.court.window_bottom
        self.image.draw(sx, sy)


    def update(self):
        pass

    def get_bb(self):
        return self.x-10, self.y-10,self.x + 10,self.y + 10

    def handle_collision(self,group,other):
        if group == 'boy:ball':
            game_world.remove_object(self)
        elif group == 'grass:ball':
            self.stopped = True
        elif group == 'zombie:ball':
            if not self.stopped:
                game_world.remove_object(self)
