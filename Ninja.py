import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "50, 100"
import pgzrun
from find_yx import Get_X_Y

class PLAYER1:
    def __init__(self, ninja_color):
        self.ninja_color = ninja_color
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
            ninja1.x += 3.8
            self.direction = 0
            self.turned = True
            self.directions()
        if keyboard.LEFT:
            ninja1.x -= 3.8
            self.direction = 1
            self.turned = True
            self.directions()
        if keyboard.UP and self.on_ground and not self.jumping:
            self.on_base = False
            self.jumping = True
            self.on_ground = False
            ninja1.vy = self.jump_strength
            self.falling = False
         
                   
    def ninja_move(self):
        if not self.on_ground or self.jumping:
            ninja1.vy += self.gravity
            ninja1.y += ninja1.vy
            
            if ninja1.y > HEIGHT - ninja1.height / 2:  
                ninja1.y = HEIGHT - ninja1.height / 2
                self.on_ground = True
                self.jumping = False
                ninja1.vy = 0
                self.on_base = True
                self.falling = False
                            
            if ninja1.vy >= 0:
                collided = False
                if ninja1.colliderect(Base1) and ninja1.y < Base1.y and not self.falling:
                    ninja1.y = Base1.y - 15
                    collided = True
                    self.off = 1
                if ninja1.colliderect(Base2) and ninja1.y < Base2.y and not self.falling:
                    ninja1.y = Base2.y - 15
                    collided = True
                    self.off = 2
                if ninja1.colliderect(Base3) and ninja1.y < Base3.y and not self.falling:
                    ninja1.y = Base3.y - 15
                    collided = True
                    self.off = 3
                if ninja1.colliderect(Base4) and ninja1.y < Base4.y and not self.falling:
                    ninja1.y = Base4.y - 15
                    collided = True
                    self.off = 4
                if ninja1.colliderect(Base5) and ninja1.y < Base5.y and not self.falling:
                    ninja1.y = Base5.y - 15
                    collided = True
                    self.off = 5
                if collided:   
                    self.on_ground = True
                    self.jumping = False
                    ninja1.vy = 0
                    self.falling = True
        
        if self.falling:            
            if self.off == 1 and (ninja1.x > Base1.x + 130 or ninja1.x < Base1.x - 10):
                self.fell = True           
            if self.off == 2 and (ninja1.x > Base2.x + 130 or ninja1.x < Base2.x - 10):
                self.fell = True
            if self.off == 3 and (ninja1.x > Base3.x + 160 or ninja1.x < Base3.x - 10):
                self.fell = True
            if self.off == 4 and (ninja1.x > Base4.x + 130 or ninja1.x < Base4.x - 10):
                self.fell = True
            if self.off == 5 and (ninja1.x > Base5.x + 130 or ninja1.x < Base5.x - 10):
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
            if abs(attack1_3.y - ninja2.y) <= 10 and abs(attack1_3.y - ninja2.y) >= 0:
                if attack1_3.x >= ninja2.x - 25 and attack1_3.x <= ninja2.x + 25:
                    hit_him = True
                elif attack1_2.x >= ninja2.x - 25 and attack1_2.x <= ninja2.x + 25:
                    hit_him = True
                elif attack1_1.x >= ninja2.x - 25 and attack1_1.x <= ninja2.x + 25:
                    hit_him = True
                    
        if self.direction == 1:
            if abs(ninja2.y - attack1_3.y) <= 10 and abs(ninja2.y - attack1_3.y) >= 0:
                if attack1_3.x <= ninja2.x + 25 and attack1_3.x >= ninja2.x - 25:
                    hit_him = True
                elif attack1_2.x <= ninja2.x + 25 and attack1_2.x >= ninja2.x - 25:
                    hit_him = True
                elif attack1_1.x <= ninja2.x + 25 and attack1_1.x >= ninja2.x - 25:
                    hit_him = True
        if hit_him:
            instance_of_player2.life_minus()
            hit_him = False

            
    def directions(self):
        if self.mode == 1 and self.hitting:
            if self.direction == 0:
                ninja1.image = f"ninja_{self.ninja_color}_hit.png"
            if self.direction == 1:
                ninja1.image = f"ninja_{self.ninja_color}_left_hit.png"                
        if self.mode == 0 and self.hitting:
            if self.direction == 0:
                ninja1.image = f"ninja_{self.ninja_color}.png"
            if self.direction == 1:
                ninja1.image = f"ninja_{self.ninja_color}_left.png"
            
        if self.direction == 0 and self.turned and not self.hitting:
            ninja1.image = f"ninja_{self.ninja_color}.png"
            self.turned = False
        if self.direction == 1 and self.turned and not self.hitting:
            ninja1.image = f"ninja_{self.ninja_color}_left.png"
            self.turned = False        

    def swap(self):
        if ninja1.x < 0:
            ninja1.x = WIDTH
        if ninja1.x > WIDTH:
            ninja1.x = 0
            
    def get_attack_xcoords(self):       
        if self.direction == 0:
            attack1_3.x = ninja1.x + 30
            attack1_3.image = f"attack_{self.ninja_color}_3r.png"
            attack1_2.x = attack1_3.x + 12
            attack1_2.image = f"attack_{self.ninja_color}_2r.png"
            attack1_1.x = attack1_2.x + 12
            attack1_1.image = f"attack_{self.ninja_color}_1r.png"
        if self.direction == 1:
            attack1_3.x = ninja1.x - 25
            attack1_3.image = f"attack_{self.ninja_color}_3l.png"
            attack1_2.x = attack1_3.x - 9
            attack1_2.image = f"attack_{self.ninja_color}_2l.png"
            attack1_1.x = attack1_2.x - 9
            attack1_1.image = f"attack_{self.ninja_color}_1l.png"
        attack1_3.y = ninja1.y + 5
        clock.schedule(self.get_attack_2ycoords, 0.1)
    
    def get_attack_2ycoords(self):        
        attack1_2.y = ninja1.y + 7
        clock.schedule(self.get_attack_1ycoords, 0.1)
        
    def get_attack_1ycoords(self):
        attack1_1.y = ninja1.y + 9
        attack1_3.y = HEIGHT + 50
        clock.schedule(self.get_attack_3ycoords, 0.1)
        
    def get_attack_3ycoords(self):
        attack1_2.y = HEIGHT + 50
        clock.schedule(self.delete_last_attack, 0.1)
        
    def delete_last_attack(self):
        attack1_1.y = HEIGHT + 50
        
    def update_life(self):
        self.life_as_str = str(self.life)
        return self.life_as_str
    
    def life_minus(self):
        global game_mode, winning_color, winner
        self.life -= 1
        if self.life == 0:
            game_mode = 2
            winning_color = ChosenColor_2
            winner = player2_name
    
    def update(self):
        self.update_life()
        self.directions()
        self.ninja_move()
        self.control_ninja()
        self.hit()
        self.swap()


class PLAYER2:
    def __init__(self, ninja_color):
        self.ninja_color = ninja_color
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
        
    def control_ninja(self):
        if keyboard.D:
            ninja2.x += 3.8
            self.direction = 0
            self.turned = True
            self.directions()
        if keyboard.A:
            ninja2.x -= 3.8
            self.direction = 1
            self.turned = True
            self.directions()
        if keyboard.W and self.on_ground and not self.jumping:
            self.on_base = False
            self.jumping = True
            self.on_ground = False
            ninja2.vy = self.jump_strength
            self.falling = False
         
                   
    def ninja_move(self):
        if not self.on_ground or self.jumping:
            ninja2.vy += self.gravity
            ninja2.y += ninja2.vy
            
            if ninja2.y > HEIGHT - ninja2.height / 2:  
                ninja2.y = HEIGHT - ninja2.height / 2
                self.on_ground = True
                self.jumping = False
                ninja2.vy = 0
                self.on_base = True
                self.falling = False
                            
            if ninja2.vy >= 0:
                collided = False
                if ninja2.colliderect(Base1) and ninja2.y < Base1.y and not self.falling:
                    ninja2.y = Base1.y - 15
                    collided = True
                    self.off = 1
                if ninja2.colliderect(Base2) and ninja2.y < Base2.y and not self.falling:
                    ninja2.y = Base2.y - 15
                    collided = True
                    self.off = 2
                if ninja2.colliderect(Base3) and ninja2.y < Base3.y and not self.falling:
                    ninja2.y = Base3.y - 15
                    collided = True
                    self.off = 3
                if ninja2.colliderect(Base4) and ninja2.y < Base4.y and not self.falling:
                    ninja2.y = Base4.y - 15
                    collided = True
                    self.off = 4
                if ninja2.colliderect(Base5) and ninja2.y < Base5.y and not self.falling:
                    ninja2.y = Base5.y - 15
                    collided = True
                    self.off = 5
                if collided:   
                    self.on_ground = True
                    self.jumping = False
                    ninja2.vy = 0
                    self.falling = True
        
        if self.falling:            
            if self.off == 1 and (ninja2.x > Base1.x + 130 or ninja2.x < Base1.x - 10):
                self.fell = True           
            if self.off == 2 and (ninja2.x > Base2.x + 130 or ninja2.x < Base2.x - 10):
                self.fell = True
            if self.off == 3 and (ninja2.x > Base3.x + 160 or ninja2.x < Base3.x - 10):
                self.fell = True
            if self.off == 4 and (ninja2.x > Base4.x + 130 or ninja2.x < Base4.x - 10):
                self.fell = True
            if self.off == 5 and (ninja2.x > Base5.x + 130 or ninja2.x < Base5.x - 10):
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
            if abs(attack2_3.y - ninja1.y) <= 10 and abs(attack2_3.y - ninja1.y) >= 0:
                if attack2_3.x >= ninja1.x - 25 and attack2_3.x <= ninja1.x + 25:
                    hit_him = True
                elif attack2_2.x >= ninja1.x - 25 and attack2_2.x <= ninja1.x + 25:
                    hit_him = True
                elif attack2_1.x >= ninja1.x - 25 and attack2_1.x <= ninja1.x + 25:
                    hit_him = True
                    
        if self.direction == 1:
            if abs(ninja1.y - attack2_3.y) <= 10 and abs(ninja1.y - attack2_3.y) >= 0:
                if attack2_3.x <= ninja1.x + 25 and attack2_3.x >= ninja1.x - 25:
                    hit_him = True
                elif attack2_2.x <= ninja1.x + 25 and attack2_2.x >= ninja1.x - 25:
                    hit_him = True
                elif attack2_1.x <= ninja1.x + 25 and attack2_1.x >= ninja1.x - 25:
                    hit_him = True
        if hit_him:
            instance_of_player1.life_minus()
            hit_him = False

            
    def directions(self):
        if self.mode == 1 and self.hitting:
            if self.direction == 0:
                ninja2.image = f"ninja_{self.ninja_color}_hit.png"
            if self.direction == 1:
                ninja2.image = f"ninja_{self.ninja_color}_left_hit.png"                
        if self.mode == 0 and self.hitting:
            if self.direction == 0:
                ninja2.image = f"ninja_{self.ninja_color}.png"
            if self.direction == 1:
                ninja2.image = f"ninja_{self.ninja_color}_left.png"
            
        if self.direction == 0 and self.turned and not self.hitting:
            ninja2.image = f"ninja_{self.ninja_color}.png"
            self.turned = False
        if self.direction == 1 and self.turned and not self.hitting:
            ninja2.image = f"ninja_{self.ninja_color}_left.png"
            self.turned = False        

    def swap(self):
        if ninja2.x < 0:
            ninja2.x = WIDTH
        if ninja2.x > WIDTH:
            ninja2.x = 0
            
    def get_attack_xcoords(self):       
        if self.direction == 0:
            attack2_3.x = ninja2.x + 30
            attack2_3.image = f"attack_{self.ninja_color}_3r.png"
            attack2_2.x = attack2_3.x + 12
            attack2_2.image = f"attack_{self.ninja_color}_2r.png"
            attack2_1.x = attack2_2.x + 12
            attack2_1.image = f"attack_{self.ninja_color}_1r.png"
        if self.direction == 1:
            attack2_3.x = ninja2.x - 25
            attack2_3.image = f"attack_{self.ninja_color}_3l.png"
            attack2_2.x = attack2_3.x - 9
            attack2_2.image = f"attack_{self.ninja_color}_2l.png"
            attack2_1.x = attack2_2.x - 9
            attack2_1.image = f"attack_{self.ninja_color}_1l.png"
        attack2_3.y = ninja2.y + 5
        clock.schedule(self.get_attack_2ycoords, 0.1)
    
    def get_attack_2ycoords(self):        
        attack2_2.y = ninja2.y + 7
        clock.schedule(self.get_attack_1ycoords, 0.1)
        
    def get_attack_1ycoords(self):
        attack2_1.y = ninja2.y + 9
        attack2_3.y = HEIGHT + 50
        clock.schedule(self.get_attack_3ycoords, 0.1)
        
    def get_attack_3ycoords(self):
        attack2_2.y = HEIGHT + 50
        clock.schedule(self.delete_last_attack, 0.1)
        
    def delete_last_attack(self):
        attack2_1.y = HEIGHT + 50
        
    def update_life(self):
        self.life_as_str = str(self.life)
        return self.life_as_str
    
    def life_minus(self):
        global game_mode, winning_color, winner
        self.life -= 1
        if self.life == 0:
            game_mode = 2
            winning_color = ChosenColor_1
            winner = player1_name
    
    def update(self):
        self.update_life()
        self.directions()
        self.ninja_move()
        self.control_ninja()
        self.hit()
        self.swap()

# Screen
WIDTH = 500
HEIGHT = 500
TITLE = "Ninja"
WHITE = (255, 255, 255)

ChosenColor_1 = "white"
ChosenColor_2 = "white"
player1 = PLAYER1(ChosenColor_1)
player2 = PLAYER2(ChosenColor_2)

# Actors
ninja1 = Actor(f"ninja_{ChosenColor_1}_left.png")
ninja1.x = WIDTH / 10 * 9
ninja1.y = HEIGHT / 10 * 9
ninja1.vx = 0
ninja1.vy = 0
attack1_3 = Actor(f"attack_{ChosenColor_1}_3r.png")
attack1_3.x = 0
attack1_3.y = HEIGHT + 50
attack1_2 = Actor(f"attack_{ChosenColor_1}_2r.png")
attack1_2.x = 0
attack1_2.y = HEIGHT + 50
attack1_1 = Actor(f"attack_{ChosenColor_1}_1r.png")
attack1_1.x = 0
attack1_1.y = HEIGHT + 50

ninja2 = Actor(f"ninja_{ChosenColor_2}.png")
ninja2.x = WIDTH / 10
ninja2.y = HEIGHT / 10 * 9
ninja2.vx = 0
ninja2.vy = 0
attack2_3 = Actor(f"attack_{ChosenColor_2}_3r.png")
attack2_3.x = 0
attack2_3.y = HEIGHT + 50
attack2_2 = Actor(f"attack_{ChosenColor_2}_2r.png")
attack2_2.x = 0
attack2_2.y = HEIGHT + 50
attack2_1 = Actor(f"attack_{ChosenColor_2}_1r.png")
attack2_1.x = 0
attack2_1.y = HEIGHT + 50

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

# Variabeln
game_mode = -3
countdown_number = 3
countdown_as_str = ""
winning_color = None
winner = None

# Zur Wahl stehende Farben
abstand = WIDTH / 50
rand = WIDTH / (WIDTH/90) / 2
breite = WIDTH / 10

red = Rect((rand , HEIGHT / 2), (breite, 20))
yellow = Rect((rand+breite+abstand, HEIGHT / 2), (breite, 20))
green = Rect((rand+2*breite+2*abstand, HEIGHT / 2), (breite, 20))
blue = Rect((WIDTH/2-breite/2, HEIGHT / 2), (breite, 20))
purple = Rect((WIDTH/2+breite/2+abstand, HEIGHT / 2), (breite, 20))
black = Rect((WIDTH-rand-2*breite-abstand, HEIGHT / 2),(breite, 20))
white = Rect((WIDTH-rand-breite , HEIGHT / 2),(breite, 20))
all_colors = [red, yellow, green, blue, purple, black, white]
possible_colors = [red, yellow, green, blue, purple, black, white]
dark_colors = ["red", "blue", "purple", "black"]
light_colors = [yellow, green, white]
above_rect = None

# Username
chosing_player = "Player 1"
searchbar = f"{chosing_player}, please type in your username"
letters = ["Q","W", "E", "R","T","Z", "U","I","O","P","A","S","D","F","G","H","J","K","L","Y","X","C","V","B","N","M"]
logs = {}
possible_logins = ""
first = True
no_username = "If you can't find your username or know that you don't have one, press 'SPACE' to create one."
player1_name = ""
player2_name = ""
instr_login = "Type in your name and press 'ENTER' to confirm"
create_login = ""

def open_logins():
    try:
        with open("people.txt", "r") as file:
            log_ins = {}
            lines = file.readlines()
            for line in lines:
                try:
                    if ", " in line:
                        name, wins = line.strip().split(", ")
                        log_ins[name] = int(wins)
                except ValueError:
                    pass
            return log_ins             
    except FileNotFoundError:
        return {}
    
def generate_logs(searchbar):
    global possible_logins
    log_ins = open_logins()
    filtered_logs = {name: wins for name, wins in log_ins.items() if name.startswith(searchbar)}
    possible_logins = next(iter(filtered_logs), "")
    return filtered_logs

def on_key_down(key):
    global searchbar, logs, first, game_mode, player1_name, player2_name, chosing_player, create_login
    if game_mode <= -2:
        if first:
            searchbar = ""
            first = False
        if key == keys.BACKSPACE:
            if game_mode > -4:
                searchbar = searchbar[:-1]
            if game_mode <= -4:
               create_login = create_login[:-1] 
        elif key.name in letters:
            if game_mode > -4:
                searchbar += key.name
            if game_mode <= -4:
                create_login += key.name
        elif key == keys.RETURN and possible_logins in logs:
            if game_mode == -3:
                game_mode = -2
                player1_name = possible_logins
                chosing_player = "Player 2"
                searchbar = f"{chosing_player}, please type in your username"
                first = True
            elif game_mode == -2:
                game_mode = -1
                player2_name = possible_logins
                chosing_player = player1_name
            elif game_mode == -4:
                player1_name = create_login
                chosing_player = "Player 2"
                first = True
                create_login = ""
                searchbar = f"{chosing_player}, please type in your username"
                game_mode = -3
            elif game_mode == -5:
                player2_name = create_login
                game_mode = -1
                chosing_player = player1_name

        logs = generate_logs(searchbar)
        if key == keys.SPACE:
            if chosing_player == "Player 1":
                game_mode = -4
            if chosing_player == "Player 2":
                game_mode = -5
    if key == keys.ESCAPE:
        quit()
            
# Cursor
cursor = Rect((550, 550), (1, 1))
colors_as_str = ["red", "yellow", "green", "blue", "purple", "black", "white"]
player1_choice = True
first_index=None

def on_mouse_move(pos):
    global cursor
    cursor_x, cursor_y = pos
    cursor = Rect((cursor_x, cursor_y), (1, 1))
    
def on_mouse_down(pos):
    global cursor, ChosenColor_1, ChosenColor_2, player1_choice, game_mode, chosen_rect_1, first_index, chosing_player, player1_name, player2_name
    if game_mode == -1:
        if player1_choice:
            for index, colored_rect in enumerate(possible_colors):
                if cursor.colliderect(colored_rect):
                    chosen_rect_1 = possible_colors.pop(index)
                    ChosenColor_1 = colors_as_str[index]
                    first_index = index
                    player1_choice = False
                    chosing_player = player2_name
        else:
            for index, colored_rect in enumerate(all_colors):
                if cursor.colliderect(colored_rect) and index != first_index:
                    ChosenColor_2 = colors_as_str[index]
                    game_mode = 0
        
# Programm   
def moving():
    global cursor, above, above_rect 
    above = False
    above_rect = None
    for colored_rect in possible_colors:
        if cursor.colliderect(colored_rect):
            above_rect = colored_rect
            above = True

def count_down():
    global game_mode, countdown_number, countdown_as_str
    if countdown_number == -1:
        game_mode = 1
    countdown_as_str = str(countdown_number)
    countdown_number -= 1
    if countdown_number >= -1:
        clock.schedule(count_down, 1.0)
        first = False
        
def initialize():
    global player1, player2
    player1 = PLAYER1(ChosenColor_1)
    player2 = PLAYER2(ChosenColor_2)
    player1.did_i_hit(player2)
    player2.did_i_hit(player1)

def draw():
    global winning_color    
    screen.clear()
    screen.fill(WHITE)
    Background.draw()
    if game_mode <= -4:
        screen.draw.text(instr_login, ((WIDTH/100), HEIGHT / 10), fontsize=30, color="orange")
        screen.draw.text(f"Username: {create_login}", ((WIDTH/100), HEIGHT / 4), fontsize=35, color="orange")
        
    if game_mode < -1 and game_mode > -4:
        logs_to_display = "\n".join([f"Username: {name}, Wins: {wins}" for name, wins in logs.items()])     
        screen.draw.text(no_username, ((WIDTH/100), HEIGHT / 10), fontsize=15, color="orange")
        if searchbar != "" and searchbar != f"{chosing_player}, please type in your username":
            screen.draw.text(possible_logins, ((WIDTH/100), HEIGHT / 8), fontsize=35, color=(127, 82, 0))
            screen.draw.text(logs_to_display, ((WIDTH/100), HEIGHT / 4), fontsize=30, color="orange")
        screen.draw.text(searchbar, ((WIDTH/100), HEIGHT / 8), fontsize=35, color="orange")
        screen.draw.line((0, HEIGHT/5), (WIDTH, HEIGHT/5), color="white")
        
        
    if game_mode == -1:
        screen.draw.filled_rect(red, "red")
        screen.draw.filled_rect(yellow, "yellow")
        screen.draw.filled_rect(green, "green")
        screen.draw.filled_rect(blue, "blue")
        screen.draw.filled_rect(purple, "purple")
        screen.draw.filled_rect(black, "black")
        screen.draw.filled_rect(white, "white")
        text = f"{chosing_player}, please choose your color."
        screen.draw.text(text, (10, HEIGHT / 4), fontsize=40, color="orange", owidth=1, ocolor="white")
        if above:
            outline = "white"
            if above_rect in light_colors:
                outline = "black"
            screen.draw.rect(above_rect, outline)
            
    if game_mode >= 0:
        screen.draw.rect(Bottom, "white")
        ninja1.draw()
        attack1_3.draw()
        attack1_2.draw()
        attack1_1.draw()
        life_player1 = player1.update_life()
        if game_mode >=1:
            o_color = "black"
            if ChosenColor_1 in dark_colors:
                o_color = "white"
            screen.draw.text(life_player1, (WIDTH - 2*rand, HEIGHT / 10), fontsize=50, color=ChosenColor_1, owidth=1, ocolor=o_color)
    
        ninja2.draw()
        attack2_3.draw()
        attack2_2.draw()
        attack2_1.draw()
        life_player2 = player2.update_life()
        if game_mode >=1:
            o_color = "black"
            if ChosenColor_2 in dark_colors:
                o_color = "white"
            screen.draw.text(life_player2, (rand, HEIGHT / 10), fontsize=50, color=ChosenColor_2, owidth=1, ocolor=o_color)  
        screen.draw.filled_rect(Base1, "white")
        screen.draw.filled_rect(Base2, "white")
        screen.draw.filled_rect(Base3, "white")
        screen.draw.filled_rect(Base4, "white")
        screen.draw.filled_rect(Base5, "white")
    
        if game_mode == 0:
            screen.draw.text(countdown_as_str, (WIDTH / 2, HEIGHT / 2), fontsize=100, color="orange", owidth=1, ocolor="white")
    
        if game_mode == 2:
            WINNER = f"Winner is {winner}!"
            if life_player1 == "0" and life_player2 == "0":
                WINNER = "Winner is no one!"
                winning_color = "orange"
            screen.draw.text(WINNER, (WIDTH / 5, HEIGHT / 4), fontsize=50, color=winning_color, owidth=1, ocolor=o_color)            
        
def update():
    global game_mode, WINNER
    if game_mode == -3:
        generate_logs(searchbar)
    if game_mode == -1:
        moving()      
    if game_mode == 0 and countdown_number == 3:
        initialize()
        ninja1.image = f"ninja_{ChosenColor_1}_left.png"
        ninja2.image = f"ninja_{ChosenColor_2}.png"
        count_down()       
    if game_mode == 1:
        player1.update()
        player2.update()
    if game_mode == 2:
        ninja1.x = WIDTH -rand
        ninja1.y = HEIGHT / 1.5
        ninja1.image = f"ninja_{ChosenColor_1}_left.png"
        ninja2.x = rand
        ninja2.y = HEIGHT / 1.5
        ninja2.image = f"ninja_{ChosenColor_2}.png"

pgzrun.go()