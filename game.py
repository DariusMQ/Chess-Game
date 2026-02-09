
import pygame
#from stockfish import Stockfish 3
import chess
import ctypes
import os

class Piece(pygame.sprite.Sprite):
    def __init__(self, image, type, color,X,Y):
        pygame.sprite.Sprite.__init__(self)

        self.type = type
        self.color = color
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y
        self.orig_x = X
        self.orig_y = Y

    
    def update_captured(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def update(self, x, y): 
        self.rect.move_ip(x,y)

    def go_back(self):
        self.rect.x = self.orig_x
        self.rect.y = self.orig_y

    def get_value(self):
        match self.type:
            case chess.PAWN: return 1
            case chess.KNIGHT: return 3
            case chess.BISHOP: return 3
            case chess.ROOK: return 5
            case chess.QUEEN: return 9
    
class SelectionDot(pygame.sprite.DirtySprite):
    def __init__(self, type, color,X,Y,W,H,R,move):

        pygame.sprite.DirtySprite.__init__(self)

        self.image = pygame.Surface([W,H], pygame.SRCALPHA)
        self.color = color
        self.rect = self.image.get_rect() 
        self.rect.x = X
        self.rect.y = Y
        self.rect.width = W
        self.rect.height = H
        self.type = type
        self.radius = R
        self.move = move


    def draw(self,screen):
        if self.type != 10:
            pygame.draw.circle(screen,'gray',(self.rect.x+self.rect.width/2,self.rect.y+self.rect.height/2),self.radius)
        else:
            pygame.draw.circle(screen,'gray',(self.rect.x+self.rect.width/2,self.rect.y+self.rect.height/2+5),self.radius)

class Button(pygame.sprite.Sprite):
    def __init__(self, label,color,X,Y,W,H,action):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([W,H], pygame.SRCALPHA)
        self.color = color
        self.rect = self.image.get_rect() 
        self.rect.x = X
        self.rect.y = Y
        self.rect.width = W
        self.rect.height = H
        self.action = action
        
        self.label = label
        self.button_text = bold_font.render(self.label,True,"#00D300")
        self.button_text_rect = self.button_text.get_rect()
        self.button_text_rect.center=(W/2,H/2)
        
        pygame.draw.rect(self.image,self.color,(0,0,W,H))
        self.image.blit(self.button_text,self.button_text_rect)

myappid = 'globalITPro.Chess2k22.subapp.1'  
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
pygame.init()
pygame.mixer.init()

WIDTH = 1200
HEIGHT = 900
BOARD_COORDS = (100,130)
BLACK_PLAYER_ICON_COORDS = (105, 60, 60, 60)
WHITE_PLAYER_ICON_COORDS = (105, 760, 60, 60)
BLACK_PLAYER_NAME_COORDS = (170, 60)
WHITE_PLAYER_NAME_COORDS = (170, 760)
BLACK_PLAYER_CLOCK_COORDS = (573, 85, 140, 35)
WHITE_PLAYER_CLOCK_COORDS = (573, 755, 140, 35)
BLACK_PLAYER_CLOCK_TEXT_COORDS = (710, 102.5)
WHITE_PLAYER_CLOCK_TEXT_COORDS = (710, 772.5)

screen = pygame.display.set_mode([WIDTH,HEIGHT])
icon = pygame.image.load('./Icons/White_Pawn.png')
pygame.display.set_icon(pygame.transform.scale(icon,(32,32)))
pygame.display.set_caption('Chess 2k22')

font = pygame.font.Font('./Fonts/Roboto-Light.ttf', 20)
bold_font = pygame.font.Font('./Fonts/Roboto-Light.ttf', 20) 
bold_font.bold = True
big_font = pygame.font.Font('./Fonts/Roboto-Light.ttf', 50)
small_font = pygame.font.Font('./Fonts/Roboto-Light.ttf', 14)

timer = pygame.time.Clock()
fps = 60

black_queen = pygame.image.load('./Icons/Black_Queen.png')
black_queen = pygame.transform.scale(black_queen,(70,70))
black_queen_small = pygame.transform.scale(black_queen,(35,35))
black_king = pygame.image.load('./Icons/Black_King.png')
black_king = pygame.transform.scale(black_king,(70,70))
black_king_small = pygame.transform.scale(black_king,(35,35))
black_knight = pygame.image.load('./Icons/Black_Knight.png')
black_knight = pygame.transform.scale(black_knight,(70,70))
black_knight_small = pygame.transform.scale(black_knight,(35,35))
black_bishop = pygame.image.load('./Icons/Black_Bishop.png')
black_bishop = pygame.transform.scale(black_bishop,(70,70))
black_bishop_small = pygame.transform.scale(black_bishop,(35,35))
black_rook = pygame.image.load('./Icons/Black_Rook.png')
black_rook = pygame.transform.scale(black_rook,(70,70))
black_rook_small = pygame.transform.scale(black_rook,(35,35))
black_pawn = pygame.image.load('./Icons/Black_Pawn.png')
black_pawn = pygame.transform.scale(black_pawn,(70,70))
black_pawn_small = pygame.transform.scale(black_pawn,(35,35))

chess_board = pygame.image.load('./Icons/Chess_Board.png')

white_queen = pygame.image.load('./Icons/White_Queen.png')
white_queen = pygame.transform.scale(white_queen,(70,70))
white_queen_small = pygame.transform.scale(white_queen,(35,35))
white_king = pygame.image.load('./Icons/White_King.png')
white_king = pygame.transform.scale(white_king,(70,70))
white_king_small = pygame.transform.scale(white_king,(35,35))
white_knight = pygame.image.load('./Icons/White_Knight.png')
white_knight = pygame.transform.scale(white_knight,(70,70))
white_knight_small = pygame.transform.scale(white_knight,(35,35))
white_bishop = pygame.image.load('./Icons/White_Bishop.png')
white_bishop = pygame.transform.scale(white_bishop,(70,70))
white_bishop_small = pygame.transform.scale(white_bishop,(35,35))
white_rook = pygame.image.load('./Icons/White_Rook.png')
white_rook = pygame.transform.scale(white_rook,(70,70))
white_rook_small = pygame.transform.scale(white_rook,(35,35))
white_pawn = pygame.image.load('./Icons/White_Pawn.png')
white_pawn = pygame.transform.scale(white_pawn,(70,70))
white_pawn_small = pygame.transform.scale(white_pawn,(35,35))

PIECE_MAP = { 
    'r': (black_rook, chess.ROOK, False), 
    'n': (black_knight, chess.KNIGHT, False), 
    'b': (black_bishop, chess.BISHOP, False), 
    'q': (black_queen, chess.QUEEN, False), 
    'k': (black_king, chess.KING, False), 
    'p': (black_pawn, chess.PAWN, False), 
    'R': (white_rook, chess.ROOK, True), 
    'N': (white_knight, chess.KNIGHT, True), 
    'B': (white_bishop, chess.BISHOP, True), 
    'Q': (white_queen, chess.QUEEN, True), 
    'K': (white_king, chess.KING, True), 
    'P': (white_pawn, chess.PAWN, True)}    

sound_notify = pygame.mixer.Sound("./Sounds/GenericNotify.ogg")
sound_capture = pygame.mixer.Sound("./Sounds/Capture.ogg")
sound_move = pygame.mixer.Sound("./Sounds/Move.ogg")

white_images = pygame.sprite.LayeredUpdates()
black_images = pygame.sprite.LayeredUpdates()
move_images = pygame.sprite.Group()
promotion_images = pygame.sprite.Group()
buttons = pygame.sprite.Group()
white_images_small = []
black_images_small = []
selection = None
checked_square = None

board = chess.Board()
#stockfish = Stockfish(path = "/usr/games/stockfish")
position = board.fen()
moves_to_select = []
san_moves = []
san_number = 0
wait_for_promotion = None
time_flag = None
resignation_flag = None
draw_flag = False
draw_request = None
white_time = 10 * 60
black_time = 10 * 60
last_switch_ms = pygame.time.get_ticks()
score = [0,0]
result = None
matches_series = []

def draw_player_panels(): 
    pygame.draw.rect(screen, 'black', BLACK_PLAYER_ICON_COORDS) 
    pygame.draw.rect(screen, 'white', WHITE_PLAYER_ICON_COORDS) 

    screen.blit(font.render("Black_Name", True, 'black'), BLACK_PLAYER_NAME_COORDS) 
    screen.blit(font.render("White_Name", True, 'white'), WHITE_PLAYER_NAME_COORDS)
def draw_clock(time_value, color, rect, text_coords): 
    pygame.draw.rect(screen, color, rect)
    if time_value >= 30: 
        text = f"{int(time_value//60):02d}:{int(time_value%60):02d}" 
    else: 
        text = f"{time_value:.2f}" 
        
    surf = font.render(text, True, 'white' if color == 'black' else 'black') 
    rect = surf.get_rect(right=text_coords[0], centery=text_coords[1]) 
    screen.blit(surf, rect)
def draw_clocks(): 
    draw_clock(black_time, 'black', BLACK_PLAYER_CLOCK_COORDS, BLACK_PLAYER_CLOCK_TEXT_COORDS) 
    draw_clock(white_time, 'white', WHITE_PLAYER_CLOCK_COORDS, WHITE_PLAYER_CLOCK_TEXT_COORDS)
def draw_move_list(): 
    pygame.draw.rect(screen, "#006000", (800, 170, 230, 500), 2) 
    # Horizontal lines 
    for i in range(1, 20): 
        y = 170 + (500/20) * i 
        pygame.draw.line(screen, "#006000", (800, y), (1030, y)) 
    # Vertical lines 
    pygame.draw.line(screen, "#006000", (840, 170), (840, 670)) 
    pygame.draw.line(screen, "#006000", (935, 170), (935, 670)) 
    # Moves 
    for n, move in enumerate(san_moves[san_number:san_number+20]): 
        y = 173 + (500/20) * n 
        screen.blit(font.render(move['Number'], True, 'black'), (805, y)) 
        screen.blit(font.render(move['white_move'], True, 'black'), (845, y)) 
        screen.blit(font.render(move['black_move'], True, 'black'), (940, y))
def draw_game_result():
    global result

    if result is None:
        if board.is_game_over():
            result = board.result()
        elif time_flag == 'w':
            result = "0-1"
        elif time_flag == 'b':
            result = "1-0"
        elif resignation_flag == 'w':
            result = "0-1"
        elif resignation_flag == 'b':
            result = "1-0"
        elif draw_flag:
            result = "1/2-1/2"

    if result is None:
        return  # No result to draw yet

    # Draw result score
    screen.blit(bold_font.render(result, True, 'white'), (900, 680))

    # Determine message
    message = None

    if board.is_game_over():
        if board.outcome().termination.value == 1:
            winner = "White" if board.outcome().winner else "Black"
            message = f"{winner} is victorious"
            sub = "Checkmate!"
        else:
            message = "Draw"
            sub = "Draw"
    elif time_flag:
        sub = "White timed out!" if time_flag == 'w' else "Black timed out!"
    elif resignation_flag:
        sub = "White resigned!" if resignation_flag == 'w' else "Black resigned!"
    elif draw_flag:
        sub = "Draw"

    # Draw messages
    if message:
        screen.blit(font.render(message, True, 'black'), (835, 720))
    screen.blit(font.render(sub, True, 'black'), (840, 700))
def draw_highlights(): 
    if checked_square: 
        pygame.draw.rect(screen, 'red', checked_square) 
    if selection: 
        pygame.draw.rect(screen, 'gold', selection)
def build_piece_sprites(fen):
    black_images.empty() 
    white_images.empty()
    
    X=103
    Y=133

    for c in fen.split(' ')[0]:
        if str(c).isdigit():
            X+=77*int(c)
            continue

        if c == '/': 
            X = 103 
            Y += 77 
            continue 
        
        if c in PIECE_MAP: 
            image, ptype, is_white = PIECE_MAP[c] 
            group = white_images if is_white else black_images 
            group.add(Piece(image, ptype, is_white, X, Y)) 
            X += 77
def build_move_dots():
    if not moves_to_select or move_images.sprites():
        return

    for move in moves_to_select:
        x, y, w, h = square_to_coords(chess.SQUARE_NAMES[move.to_square])
        is_capture = board.piece_at(move.to_square)

        dot_type = 'b' if is_capture else 's'
        radius = 30 if is_capture else 10

        move_images.add(SelectionDot(dot_type, 'gray', x, y, w, h, radius, move))
def draw_move_dots():
    for dot in move_images:
        cx = dot.rect.x + dot.rect.width / 2
        cy = dot.rect.y + dot.rect.height / 2 + (5 if dot.type == 'b' else 0)
        pygame.draw.circle(screen, 'gray', (cx, cy), dot.radius)
def draw_captured_pieces():
    for piece in white_images_small:
        screen.blit(piece.image, piece.rect)

    for piece in black_images_small:
        screen.blit(piece.image, piece.rect)
def material_difference():
    white_score = sum(p.get_value() for p in white_images_small)
    black_score = sum(p.get_value() for p in black_images_small)
    return white_score - black_score
def draw_material_difference():
    if not white_images_small and not black_images_small:
        return

    diff = material_difference()
    if diff == 0:
        return

    if diff > 0:
        last = white_images_small[-1]
        color = 'white'
        text = f"+{diff}"
    else:
        last = black_images_small[-1]
        color = 'black'
        text = f"+{abs(diff)}"

    x = last.rect.x + last.rect.w
    y = last.rect.y + 15
    surf = small_font.render(text, True, color)
    screen.blit(surf, (x, y))


def draw_board():
    global board,screen,draw_flag,resignation_flag,time_flag,result

    screen.blit(chess_board, BOARD_COORDS)
    
    draw_player_panels() 
    draw_clocks()
    draw_move_list()
    draw_game_result()

    buttons.draw(screen)
def draw_pieces():
    
    draw_highlights()

    if(len(black_images.sprites()) == 0 or 
       len(white_images.sprites()) == 0):
        build_piece_sprites(position)
        
    
    if position.split(' ')[1] == 'w':
        black_images.draw(screen)
        white_images.draw(screen)
    else:
        white_images.draw(screen)
        black_images.draw(screen)
def draw_moves_to_select(): 
    build_move_dots() 
    draw_move_dots()
def draw_promotion():
    global promotion_images
    pygame.draw.rect(screen,"#006000",(207,40,400,80))
    promotion_images.draw(screen)
def draw_captured(): 
    draw_captured_pieces() 
    draw_material_difference()
def draw_pause():
    pygame.draw.rect(screen,'#008000',(500,300,200,330))
    pause_buttons.draw(screen)

def select_piece(rect):
    global selection,board,moves_to_select
    selection = (rect.x,rect.y,rect.width,rect.height)

    selected_square = chess.SQUARES[square_number(selection[0],selection[1])]
    moves_to_select = [move for move in board.legal_moves if move.from_square == selected_square]
def deselect_piece():
    global selection,moves_to_select

    selection = None
    move_images.remove(move_images.sprites())
    moves_to_select=[]
def make_move(move,promote_to=None):
    global board,position,white_images,black_images,wait_for_promotion
    global message,san_number,san_moves,checked_square
    if move.promotion != None and wait_for_promotion == None:
        if position.split(' ')[1] == 'w':
            promotion_images.add(Piece(white_queen,chess.QUEEN,True,227,40))
            promotion_images.add(Piece(white_rook,chess.ROOK,True,322,40))
            promotion_images.add(Piece(white_bishop,chess.BISHOP,True,417,40))
            promotion_images.add(Piece(white_knight,chess.KNIGHT,True,512,40))
        else:
            promotion_images.add(Piece(black_queen,chess.QUEEN,False,227,40))
            promotion_images.add(Piece(black_rook,chess.ROOK,False,322,40))
            promotion_images.add(Piece(black_bishop,chess.BISHOP,False,417,40))
            promotion_images.add(Piece(black_knight,chess.KNIGHT,False,512,40))
        wait_for_promotion = move
        return
    else:
        move.promotion = promote_to
        wait_for_promotion = None

    white_images.remove(white_images.sprites())
    black_images.remove(black_images.sprites())
    promotion_images.remove(black_images.sprites())

    if position.split(' ')[1] == 'w':
        san_moves.append({'Number':f'{position.split(' ')[-1]}.',
                          'white_move':board.san(move),
                          'black_move':None})
    else: san_moves[-1]['black_move'] = board.san(move)    
    if len(san_moves)>20 and san_moves[-1]['black_move']== None: san_number += 1 

    if board.is_capture(move):
        color = position.split(' ')[1] == 'w'
        captured = None
        if board.is_en_passant(move): 
            captured=chess.PAWN
        else: 
            captured=board.piece_type_at(move.to_square)
        match captured:
            case chess.PAWN: 
                if not color: 
                    offset = 170 
                    white_images_small.append(Piece(white_pawn_small,captured,color,offset,780))
                else: 
                    offset = 170 
                    black_images_small.append(Piece(black_pawn_small,captured,color,offset,80))
            case chess.KNIGHT: 
                if not color: 
                    offset = 170 
                    white_images_small.append(Piece(white_knight_small,captured,color,offset,780))
                else: 
                    offset = 170 
                    black_images_small.append(Piece(black_knight_small,captured,color,offset,80))
            case chess.BISHOP: 
                if not color: 
                    offset = 170 
                    white_images_small.append(Piece(white_bishop_small,captured,color,offset,780))
                else: 
                    offset = 170 
                    black_images_small.append(Piece(black_bishop_small,captured,color,offset,80))
            case chess.ROOK: 
                if not color: 
                    offset = 170 
                    white_images_small.append(Piece(white_rook_small,captured,color,offset,780))
                else: 
                    offset = 170 
                    black_images_small.append(Piece(black_rook_small,captured,color,offset,80))
            case chess.QUEEN: 
                if not color: 
                    offset = 170 
                    white_images_small.append(Piece(white_queen_small,captured,color,offset,780))
                else: 
                    offset = 170 
                    black_images_small.append(Piece(black_queen_small,captured,color,offset,80))
        white_images_small.sort(key=lambda piece: piece.type) 
        black_images_small.sort(key=lambda piece: piece.type) 

        x =170
        prev_type = None

        for piece in white_images_small:
            # Add extra spacing when piece type changes
            if prev_type is not None and piece.type != prev_type:
                x += 20  # extra gap between types
            piece.update_captured(x,80)
            x += 14  # normal spacing
            prev_type = piece.type

        x =170
        prev_type = None

        for piece in black_images_small:
            # Add extra spacing when piece type changes
            if prev_type is not None and piece.type != prev_type:
                x += 20  # extra gap between types
            piece.update_captured(x,780)
            x += 10 + 4  # normal spacing
            prev_type = piece.type
        
        sound_capture.play()
    else: sound_move.play()

    board.push(move)
    position = board.fen()

    if board.is_check():
        king_color = chess.WHITE if position.split(' ')[1] == 'w' else chess.BLACK
        king_square = chess.SQUARE_NAMES[board.king(king_color)]
        checked_square = square_to_coords(king_square)
    else: checked_square = None
    if board.is_game_over(): sound_notify.play()
def update_time():
    global time_flag,resignation_flag,board, draw_flag
    global black_time,white_time,last_switch_ms

    if (not resignation_flag and not time_flag and not 
        draw_flag and not board.is_game_over()):
        now = pygame.time.get_ticks()
        elapsed = now - last_switch_ms
        last_switch_ms = now
        elapsed = elapsed / 1000

        if position.split(' ')[1] == 'w':
            white_time -= elapsed
            if white_time <= 0: 
                white_time = 0
                time_flag = 'w'
        else:
            black_time -= elapsed
            if black_time <= 0: 
                black_time = 0
                time_flag = 'b'
    
    if time_flag: sound_notify.play()    

def square_number(X,Y):
    top,left = (133,103)
    #(133,210,287,364,441,518,595,672)
    #(103,180,257,334,441,488,565,642)
    return ((X-left)//77+(7-(Y-top)//77)*8)
def square_to_coords(sq):
    Y = int(sq[1])-1
    X = "abcdefgh".find(sq[0])
    return (103+X*77,672-Y*77,70,70)

pygame.sprite.Sprite.visible = True
run_game = True
active_image = None
message = None

def resign(): 
    global resignation_flag 
    resignation_flag = position.split(' ')[1]
def draw():
    global draw_request,draw_flag
    if draw_request == None: 
        draw_request = position.split(' ')[1]
        return
    if draw_request == position.split(' ')[1]: 
        draw_request = None
        return
    if draw_request != position.split(' ')[1]: 
        draw_flag = True
        return
def restart():
    global white_images,black_images,move_images,promotion_images,buttons,white_images_small
    global black_images_small,selection,checked_square,board,position,moves_to_select,san_moves
    global san_number,wait_for_promotion,time_flag,resignation_flag,draw_flag,draw_request,white_time
    global black_time,last_switch_ms,score,result,active_image,message

    white_images.remove(white_images.sprites())
    black_images.remove(black_images.sprites())
    buttons.remove(buttons.sprites())
    buttons.add(Button("Resign","#006000",760,750,150,70,resign))
    buttons.add(Button("Draw","#006000",920,750,150,70,draw))
    for image in white_images_small:
      image.kill()
    for image in black_images_small:
      image.kill()
    white_images_small = []
    black_images_small = []
    selection = None
    checked_square = None

    board.reset()
    position = board.fen()
    moves_to_select = []
    san_moves = []
    san_number = 0
    wait_for_promotion = None
    time_flag = None
    resignation_flag = None
    draw_flag = False
    draw_request = None
    white_time = 10 * 60
    black_time = 10 * 60
    last_switch_ms = pygame.time.get_ticks()
    
    aux = ''
    for move in san_moves:
        aux = aux + f'{move['Number']} {move['white_move']} ' 
        if move['black_move']:
            aux = aux + f'{move['black_move']} '
    else: 
        if result != None: aux = aux + result
    matches_series.append(aux)

    if result != None:
        w,b = result.split('-')
        score[0] += float(w) if w!='1/2' else 0.5
        score[1] += float(b) if b!='1/2' else 0.5 
    result = None
    
    active_image = None
    message = None
    sound_notify.play()
def quit():
    global run_game,matches_series,san_moves,result

    aux = ''
    for move in san_moves:
        aux = aux + f'{move['Number']} {move['white_move']} ' 
        if move['black_move']:
            aux = aux + f'{move['black_move']} '
        if result != None: aux = aux + result
    matches_series.append(aux)

    if result != None:
        w,b = result.split('-')
        score[0] += float(w) if w!='1/2' else 0.5
        score[1] += float(b) if b!='1/2' else 0.5 
    
    run_game = False
def resume():
    global pause
    pause = False
def p_restart():
    global matches_series,score,pause
    restart()
    matches_series = []
    score = [0,0]
    pause = False

buttons.add(Button("Resign","#006000",760,750,150,70,resign))
buttons.add(Button("Draw","#006000",920,750,150,70,draw))
def check_for_game_over():
    if (board.is_game_over() or time_flag != None or 
        resignation_flag != None or draw_flag) and buttons.sprites()[0].label != 'Rematch':
            buttons.remove(buttons.sprites())
            buttons.add(Button('Rematch','#006000',760,750,150,70,restart))
            buttons.add(Button('Quit','#006000',920,750,150,70,quit))
            sound_notify.play()

pause = False
pause_buttons = pygame.sprite.Group()
pause_buttons.add(Button('Resume',"#006000",525,310,150,70,resume))
pause_buttons.add(Button('Menu',"#006000",525,390,150,70,lambda: print("Menu")))
pause_buttons.add(Button('Restart',"#006000",525,470,150,70,p_restart))
pause_buttons.add(Button('Quit',"#006000",525,550,150,70,quit))

def draw_screen():
    screen.fill('#008000')

    check_for_game_over()
    draw_board()
    draw_captured()
    draw_moves_to_select()
    draw_pieces()
    
    if wait_for_promotion: draw_promotion()
    if pause: draw_pause()
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global run_game
            run_game = False

        if event.type == pygame.KEYDOWN:
            handle_keydown(event)

        if pause:
            handle_pause_events(event)
        elif board_active():
            handle_gameplay_events(event)
        else:
            handle_postgame_events(event)
def board_active():
    return (not board.is_game_over()
            and not time_flag
            and not resignation_flag
            and not draw_flag
            and not pause)
def handle_keydown(event):
    global pause
    if event.key == pygame.K_ESCAPE:
        pause = not pause
def handle_gameplay_events(event):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        handle_mouse_down(event)

    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        handle_mouse_up(event)

    elif event.type == pygame.MOUSEMOTION:
        handle_mouse_motion(event)
def handle_mouse_down(event):
    x, y = event.pos

    if wait_for_promotion:
        handle_promotion_click(x, y)
        return

    if is_white_turn():
        handle_piece_selection(white_images, x, y)
    else:
        handle_piece_selection(black_images, x, y)
def handle_piece_selection(group, x, y):
    global active_image

    for image in group.sprites():
        if image.rect.collidepoint(x, y):
            deselect_piece()
            select_piece(image.rect)
            active_image = image
            group.move_to_front(image)
            return

    for image in move_images:
        if image.rect.collidepoint(x, y):
            make_move(image.move)
            deselect_piece()
            return

    for button in buttons.sprites():
        if button.rect.collidepoint(x, y):
            button.action()
            deselect_piece()
            return

    deselect_piece()
def handle_mouse_up(event):
    global active_image

    if active_image is None:
        return

    x, y = event.pos

    for image in move_images:
        if image.rect.collidepoint(x, y):
            make_move(image.move)
            deselect_piece()
            active_image = None
            return

    active_image.go_back()
    active_image = None
def handle_mouse_motion(event):
    if active_image:
        active_image.update(event.rel[0], event.rel[1])
def handle_pause_events(event):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x, y = event.pos
        for button in pause_buttons.sprites():
            if button.rect.collidepoint(x, y):
                button.action()
def handle_postgame_events(event):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x, y = event.pos
        for button in buttons.sprites():
            if button.rect.collidepoint(x, y):
                button.action()
def update_time_if_needed():
    if not time_flag:
        update_time()
def is_white_turn():
    return position.split(' ')[1] == 'w'
def handle_promotion_click(x, y):
    global wait_for_promotion

    for image in promotion_images.sprites():
        if image.rect.collidepoint(x, y):
            make_move(wait_for_promotion, promote_to=image.type)
            deselect_piece()
            wait_for_promotion = None
            return

sound_notify.play()
while run_game:
    timer.tick(fps)
    draw_screen()
    handle_events()
    update_time_if_needed()
    pygame.display.flip()

pygame.quit()

for match in matches_series:
    print(match)
print(f'{score[0]}-{score[1]}')


# coordinates refactoring
# fix material calculation
# board flip
# move table navigation
# move variation mode (OPTIONAL)