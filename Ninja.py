import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "50, 100"
import pgzrun
from find_yx import Get_X_Y

# Screen
WIDTH = 500
HEIGHT = 500
TITLE = "Ninja"
WHITE = (255, 255, 255)

# Actors
ninja = Actor("ninja_left.png")
ninja.x = WIDTH / 10 * 9
ninja.y = HEIGHT / 10 * 9
ninja.vx = 0
ninja.vy = 0
attack_grey_3 = Actor("attack_grey_3r.png")
attack_grey_3.x = 0
attack_grey_3.y = HEIGHT + 50
attack_grey_2 = Actor("attack_grey_2r.png")
attack_grey_2.x = 0
attack_grey_2.y = HEIGHT + 50
attack_grey_1 = Actor("attack_grey_1r.png")
attack_grey_1.x = 0
attack_grey_1.y = HEIGHT + 50

ninja_red = Actor("ninja_red.png")
ninja_red.x = WIDTH / 10
ninja_red.y = HEIGHT / 10 * 9
ninja_red.vx = 0
ninja_red.vy = 0
attack_red_3 = Actor("attack_red_3r.png")
attack_red_3.x = 0
attack_red_3.y = HEIGHT + 50
attack_red_2 = Actor("attack_red_2r.png")
attack_red_2.x = 0
attack_red_2.y = HEIGHT + 50
attack_red_1 = Actor("attack_red_1r.png")
attack_red_1.x = 0
attack_red_1.y = HEIGHT + 50

# Environment
Bottom = Rect((0, HEIGHT / 10 * 9.5), (WIDTH, HEIGHT / 10 * 0.5))
Background = Actor("background.png")

get_xy = Get_X_Y()
x1 = get_xy.return_x1()
x2 = get_xy.return_x2()
x3 = get_xy.return_x3()
x4 = get_xy.return_x4()
x5 = get_xy.return_x5()
Base1 = Rect((x1, HEIGHT / 10 * 8.25), (120, 5))
Base2 = Rect((x2, HEIGHT / 10 * 8.25), (120, 5))
Base3 = Rect((x3, HEIGHT / 10 * 6.5), (150, 5))
Base4 = Rect((x4, HEIGHT / 10 * 4.75), (120, 5))
Base5 = Rect((x5, HEIGHT / 10 * 4.75), (120, 5))

# Game
class Player1:
    def __init__(self, keys):
        self.jumping = False
        self.on_ground = False
        self.attacking = False
        self.gravity = 0.3
        self.jump_strength = -7
        self.hitting = False
        self.direction = 1
        self.mode = 0
        self.turned = False
        self.falling = False
        self.off = 0
        self.on_base = True
        self.fell = False
        self.life = 3
        self.life_as_str = ""
        
    def control_ninja(self):
        if keyboard.RIGHT:
            ninja.x += 3.8
            self.direction = 0
            self.turned = True
            self.directions()
        if keyboard.LEFT:
            ninja.x -= 3.8
            self.direction = 1
            self.turned = True
            self.directions()
        if keyboard.UP and self.on_ground and not self.jumping:
            self.on_base = False
            self.jumping = True
            self.on_ground = False
            ninja.vy = self.jump_strength
            self.falling = False
         
                   
    def ninja_move(self):
        if not self.on_ground or self.jumping:
            ninja.vy += self.gravity
            ninja.y += ninja.vy
            
            if ninja.y > HEIGHT - ninja.height / 2:  
                ninja.y = HEIGHT - ninja.height / 2
                self.on_ground = True
                self.jumping = False
                ninja.vy = 0
                self.on_base = True
                self.falling = False
                            
            if ninja.vy >= 0:
                collided = False
                if ninja.colliderect(Base1) and ninja.y < Base1.y and not self.falling:
                    ninja.y = Base1.y - 15
                    collided = True
                    self.off = 1
                if ninja.colliderect(Base2) and ninja.y < Base2.y and not self.falling:
                    ninja.y = Base2.y - 15
                    collided = True
                    self.off = 2
                if ninja.colliderect(Base3) and ninja.y < Base3.y and not self.falling:
                    ninja.y = Base3.y - 15
                    collided = True
                    self.off = 3
                if ninja.colliderect(Base4) and ninja.y < Base4.y and not self.falling:
                    ninja.y = Base4.y - 15
                    collided = True
                    self.off = 4
                if ninja.colliderect(Base5) and ninja.y < Base5.y and not self.falling:
                    ninja.y = Base5.y - 15
                    collided = True
                    self.off = 5
                if collided:   
                    self.on_ground = True
                    self.jumping = False
                    ninja.vy = 0
                    self.falling = True
        
        if self.falling:            
            if self.off == 1 and (ninja.x > Base1.x + 130 or ninja.x < Base1.x - 10):
                self.fell = True           
            if self.off == 2 and (ninja.x > Base2.x + 130 or ninja.x < Base2.x - 10):
                self.fell = True
            if self.off == 3 and (ninja.x > Base3.x + 160 or ninja.x < Base3.x - 10):
                self.fell = True
            if self.off == 4 and (ninja.x > Base4.x + 130 or ninja.x < Base4.x - 10):
                self.fell = True
            if self.off == 5 and (ninja.x > Base5.x + 130 or ninja.x < Base5.x - 10):
                self.fell = True
            if self.fell:
                self.on_ground = False
                self.jumping = False
                self.on_base = False
                clock.schedule(self.detect_coll_again, 0.2)
                
                
    def detect_coll_again(self):
        self.falling = False
        self.fell = False
        self.on_ground = False
        self.jumping = False
        self.on_base = False
        
    def done(self):
        self.mode = 0
        self.directions()
        self.hitting = False
        
    def hit(self):
        if keyboard.rshift and not self.hitting:
            self.get_attack_xcoords()
            self.mode = 1
            self.directions()
            self.hitting = True
            clock.schedule(self.done, 1.0)
            self.did_i_hit(player2)
            
    def did_i_hit(self, instance_of_player2):
        hit_him = False
        if self.direction == 0:
            if abs(attack_grey_3.y - ninja_red.y) <= 10 and abs(attack_grey_3.y - ninja_red.y) >= 0:
                if attack_grey_3.x >= ninja_red.x - 25 and attack_grey_3.x <= ninja_red.x + 25:
                    hit_him = True
                elif attack_grey_2.x >= ninja_red.x - 25 and attack_grey_2.x <= ninja_red.x + 25:
                    hit_him = True
                elif attack_grey_1.x >= ninja_red.x - 25 and attack_grey_1.x <= ninja_red.x + 25:
                    hit_him = True
                    
        if self.direction == 1:
            if abs(ninja_red.y - attack_grey_3.y) <= 10 and abs(ninja_red.y - attack_grey_3.y) >= 0:
                if attack_grey_3.x <= ninja_red.x + 25 and attack_grey_3.x >= ninja_red.x - 25:
                    hit_him = True
                elif attack_grey_2.x <= ninja_red.x + 25 and attack_grey_2.x >= ninja_red.x - 25:
                    hit_him = True
                elif attack_grey_1.x <= ninja_red.x + 25 and attack_grey_1.x >= ninja_red.x - 25:
                    hit_him = True
        if hit_him:
            instance_of_player2.life_minus()
            hit_him = False

            
    def directions(self):
        if self.mode == 1 and self.hitting:
            if self.direction == 0:
                ninja.image = "ninja_hit.png"
            if self.direction == 1:
                ninja.image = "ninja_left_hit.png"                
        if self.mode == 0 and self.hitting:
            if self.direction == 0:
                ninja.image = "ninja.png"
            if self.direction == 1:
                ninja.image = "ninja_left.png"
            
        if self.direction == 0 and self.turned and not self.hitting:
            ninja.image = "ninja.png"
            self.turned = False
        if self.direction == 1 and self.turned and not self.hitting:
            ninja.image = "ninja_left.png"
            self.turned = False        

    def swap(self):
        if ninja.x < 0:
            ninja.x = WIDTH
        if ninja.x > WIDTH:
            ninja.x = 0
            
    def get_attack_xcoords(self):       
        if self.direction == 0:
            attack_grey_3.x = ninja.x + 30
            attack_grey_3.image = "attack_grey_3r.png"
            attack_grey_2.x = attack_grey_3.x + 12
            attack_grey_2.image = "attack_grey_2r.png"
            attack_grey_1.x = attack_grey_2.x + 12
            attack_grey_1.image = "attack_grey_1r.png"
        if self.direction == 1:
            attack_grey_3.x = ninja.x - 25
            attack_grey_3.image = "attack_grey_3l.png"
            attack_grey_2.x = attack_grey_3.x - 9
            attack_grey_2.image = "attack_grey_2l.png"
            attack_grey_1.x = attack_grey_2.x - 9
            attack_grey_1.image = "attack_grey_1l.png"
        attack_grey_3.y = ninja.y + 5
        clock.schedule(self.get_attack_2ycoords, 0.1)
    
    def get_attack_2ycoords(self):        
        attack_grey_2.y = ninja.y + 7
        clock.schedule(self.get_attack_1ycoords, 0.1)
        
    def get_attack_1ycoords(self):
        attack_grey_1.y = ninja.y + 9
        attack_grey_3.y = HEIGHT + 50
        clock.schedule(self.get_attack_3ycoords, 0.1)
        
    def get_attack_3ycoords(self):
        attack_grey_2.y = HEIGHT + 50
        clock.schedule(self.delete_last_attack, 0.1)
        
    def delete_last_attack(self):
        attack_grey_1.y = HEIGHT + 50
        
    def update_life(self):
        self.life_as_str = str(self.life)
        return self.life_as_str
    
    def life_minus(self):
        global game_mode, winner
        self.life -= 1
        if self.life == 0:
            game_mode = 2
            winner = "red"
        
    def update(self):
        self.update_life()
        self.directions()
        self.ninja_move()
        self.control_ninja()
        self.hit()
        self.swap()
        
class Player2:
    def __init__(self, keys):
        self.jumping = False
        self.on_ground = False
        self.attacking = False
        self.gravity = 0.3
        self.jump_strength = -7
        self.hitting = False
        self.direction = 0
        self.mode = 0
        self.turned = False
        self.falling = False
        self.off = 0
        self.on_base = True
        self.fell = False
        self.life = 3
        self.life_as_str = ""
        
    def control_ninja_red(self):
        if keyboard.D:
            ninja_red.x += 3.8
            self.direction = 0
            self.turned = True
            self.directions()
        if keyboard.A:
            ninja_red.x -= 3.8
            self.direction = 1
            self.turned = True
            self.directions()
        if keyboard.W and self.on_ground and not self.jumping:
            self.on_base = False
            self.jumping = True
            self.on_ground = False
            ninja_red.vy = self.jump_strength
            self.falling = False
         
                   
    def ninja_red_move(self):
        if not self.on_ground or self.jumping:
            ninja_red.vy += self.gravity
            ninja_red.y += ninja_red.vy
            
            if ninja_red.y > HEIGHT - ninja_red.height / 2:  
                ninja_red.y = HEIGHT - ninja_red.height / 2
                self.on_ground = True
                self.jumping = False
                ninja_red.vy = 0
                self.on_base = True
                self.falling = False
                            
            if ninja_red.vy >= 0:
                collided = False
                if ninja_red.colliderect(Base1) and ninja_red.y < Base1.y and not self.falling:
                    ninja_red.y = Base1.y - 15
                    collided = True
                    self.off = 1
                if ninja_red.colliderect(Base2) and ninja_red.y < Base2.y and not self.falling:
                    ninja_red.y = Base2.y - 15
                    collided = True
                    self.off = 2
                if ninja_red.colliderect(Base3) and ninja_red.y < Base3.y and not self.falling:
                    ninja_red.y = Base3.y - 15
                    collided = True
                    self.off = 3
                if ninja_red.colliderect(Base4) and ninja_red.y < Base4.y and not self.falling:
                    ninja_red.y = Base4.y - 15
                    collided = True
                    self.off = 4
                if ninja_red.colliderect(Base5) and ninja_red.y < Base5.y and not self.falling:
                    ninja_red.y = Base5.y - 15
                    collided = True
                    self.off = 5
                if collided:   
                    self.on_ground = True
                    self.jumping = False
                    ninja_red.vy = 0
                    self.falling = True
        
        if self.falling:            
            if self.off == 1 and (ninja_red.x > Base1.x + 130 or ninja_red.x < Base1.x - 10):
                self.fell = True           
            if self.off == 2 and (ninja_red.x > Base2.x + 130 or ninja_red.x < Base2.x - 10):
                self.fell = True
            if self.off == 3 and (ninja_red.x > Base3.x + 160 or ninja_red.x < Base3.x - 10):
                self.fell = True
            if self.off == 4 and (ninja_red.x > Base4.x + 130 or ninja_red.x < Base4.x - 10):
                self.fell = True
            if self.off == 5 and (ninja_red.x > Base5.x + 130 or ninja_red.x < Base5.x - 10):
                self.fell = True
            if self.fell:
                self.on_ground = False
                self.jumping = False
                self.on_base = False
                clock.schedule(self.detect_coll_again, 0.2)
                
                
    def detect_coll_again(self):
        self.falling = False
        self.fell = False
        self.on_ground = False
        self.jumping = False
        self.on_base = False
        
    def done(self):
        self.mode = 0
        self.directions()
        self.hitting = False
        
    def hit(self):
        if keyboard.lshift and not self.hitting:
            self.get_attack_xcoords()
            self.mode = 1
            self.directions()
            self.hitting = True
            clock.schedule(self.done, 1.0)
            self.did_i_hit(player1)
            
    def did_i_hit(self, instance_of_player1):
        hit_him = False
        if self.direction == 0:
            if abs(attack_red_3.y - ninja.y) <= 10 and abs(attack_red_3.y - ninja.y) >= 0:
                if attack_red_3.x >= ninja.x - 25 and attack_red_3.x <= ninja.x + 25:
                    hit_him = True
                elif attack_red_2.x >= ninja.x - 25 and attack_red_2.x <= ninja.x + 25:
                    hit_him = True
                elif attack_red_1.x >= ninja.x - 25 and attack_red_1.x <= ninja.x + 25:
                    hit_him = True
                    
        if self.direction == 1:
            if abs(ninja.y - attack_red_3.y) <= 10 and abs(ninja.y - attack_red_3.y) >= 0:
                if attack_red_3.x <= ninja.x + 25 and attack_red_3.x >= ninja.x - 25:
                    hit_him = True
                elif attack_red_2.x <= ninja.x + 25 and attack_red_2.x >= ninja.x - 25:
                    hit_him = True
                elif attack_red_1.x <= ninja.x + 25 and attack_red_1.x >= ninja.x - 25:
                    hit_him = True
        if hit_him:
            instance_of_player1.life_minus()
            hit_him = False
            
    def directions(self):
        if self.mode == 1 and self.hitting:
            if self.direction == 0:
                ninja_red.image = "ninja_red_hit.png"
            if self.direction == 1:
                ninja_red.image = "ninja_red_left_hit.png"                
        if self.mode == 0 and self.hitting:
            if self.direction == 0:
                ninja_red.image = "ninja_red.png"
            if self.direction == 1:
                ninja_red.image = "ninja_red_left.png"
            
        if self.direction == 0 and self.turned and not self.hitting:
            ninja_red.image = "ninja_red.png"
            self.turned = False
        if self.direction == 1 and self.turned and not self.hitting:
            ninja_red.image = "ninja_red_left.png"
            self.turned = False        

    def swap(self):
        if ninja_red.x < 0:
            ninja_red.x = WIDTH
        if ninja_red.x > WIDTH:
            ninja_red.x = 0
            
    def get_attack_xcoords(self):       
        if self.direction == 0:
            attack_red_3.x = ninja_red.x + 30
            attack_red_3.image = "attack_red_3r.png"
            attack_red_2.x = attack_red_3.x + 12
            attack_red_2.image = "attack_red_2r.png"
            attack_red_1.x = attack_red_2.x + 12
            attack_red_1.image = "attack_red_1r.png"
        if self.direction == 1:
            attack_red_3.x = ninja_red.x - 25
            attack_red_3.image = "attack_red_3l.png"
            attack_red_2.x = attack_red_3.x - 9
            attack_red_2.image = "attack_red_2l.png"
            attack_red_1.x = attack_red_2.x - 9
            attack_red_1.image = "attack_red_1l.png"
        attack_red_3.y = ninja_red.y + 5
        clock.schedule(self.get_attack_2ycoords, 0.1)
    
    def get_attack_2ycoords(self):        
        attack_red_2.y = ninja_red.y + 7
        clock.schedule(self.get_attack_1ycoords, 0.1)
        
    def get_attack_1ycoords(self):
        attack_red_1.y = ninja_red.y + 9
        attack_red_3.y = HEIGHT + 50
        clock.schedule(self.get_attack_3ycoords, 0.1)
        
    def get_attack_3ycoords(self):
        attack_red_2.y = HEIGHT + 50
        clock.schedule(self.delete_last_attack, 0.1)
        
    def delete_last_attack(self):
        attack_red_1.y = HEIGHT + 50
    
    def update_life(self):
        self.life_as_str = str(self.life)
        return self.life_as_str
    
    def life_minus(self):
        global game_mode, winner
        self.life -= 1
        if self.life == 0:
            game_mode = 2
            winner = "black"
            
    def update(self):
        self.update_life()
        self.directions()
        self.ninja_red_move()
        self.control_ninja_red()
        self.hit()
        self.swap()


## Programm
game_mode = 0
countdown_number = 3
countdown_as_str = ""
winner = None

player1 = Player1("")
player2 = Player2("")

player1.did_i_hit(player2)
player2.did_i_hit(player1)
    
def draw():
    global winner
    screen.clear()
    screen.fill(WHITE)
    screen.draw.rect(Bottom, "white")
    Background.draw()
    
    ninja.draw()
    attack_grey_3.draw()
    attack_grey_2.draw()
    attack_grey_1.draw()
    life_player1 = player1.update_life()
    if game_mode >=1:
        screen.draw.text(life_player1, (WIDTH / 10 * 9, HEIGHT / 10), fontsize=50, color=(0, 0, 0), owidth=1, ocolor="white")
    
    ninja_red.draw()
    attack_red_3.draw()
    attack_red_2.draw()
    attack_red_1.draw()
    life_player2 = player2.update_life()
    if game_mode >=1:
        screen.draw.text(life_player2, (WIDTH / 10, HEIGHT / 10), fontsize=50, color=(255, 0, 0), owidth=1, ocolor="white")
    
    
    screen.draw.filled_rect(Base1, "white")
    screen.draw.filled_rect(Base2, "white")
    screen.draw.filled_rect(Base3, "white")
    screen.draw.filled_rect(Base4, "white")
    screen.draw.filled_rect(Base5, "white")
    
    if game_mode == 0:
        screen.draw.text(countdown_as_str, (WIDTH / 2, HEIGHT / 2), fontsize=100, color="green", owidth=1, ocolor="white")
    
    if game_mode == 2:
        WINNER = f"Winner is {winner}!"
        if life_player1 == "0" and life_player2 == "0":
            WINNER = "Winner is no one!"
            winner = "purple"
        screen.draw.text(WINNER, (WIDTH / 4, HEIGHT / 4), fontsize=50, color=winner, owidth=1, ocolor="white")
    
def count_down():
    global game_mode, countdown_number, countdown_as_str
    if countdown_number == -1:
        game_mode = 1
    countdown_as_str = str(countdown_number)
    countdown_number -= 1
    if countdown_number >= -1:
        clock.schedule(count_down, 1.0)
        first = False    
        
def update():
    global game_mode, WINNER
    if game_mode == 0 and countdown_number == 3:
        count_down()       
    if game_mode == 1:
        player1.update()
        player2.update()
    if game_mode == 2:
        ninja.x = WIDTH / 10 * 9
        ninja.y = HEIGHT / 10 * 2
        ninja.image = "ninja_left.png"
        ninja_red.x = WIDTH / 10 
        ninja_red.y = HEIGHT / 10 * 2
        ninja_red.image = "ninja_red.png"
    
pgzrun.go()