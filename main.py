#!/usr/bin/python3

import pygame
from sys import exit

pygame.init() # initializing the pygame module
screen = pygame.display.set_mode((800, 850)) # screen size
pygame.display.set_caption("Chess") # Game name
clock = pygame.time.Clock() # frame rate

# board
board_surface = pygame.image.load("images/chessboard/chessboardgreen.png").convert()
board_height = int(board_surface.get_height() * 0.685)
board_width = int(board_surface.get_width() * 0.685)
board_size = (board_width, board_height)
board_surface = pygame.transform.scale(board_surface, board_size)

# classes
glob_piece_selected = False
glob_last_moved = None

class ChessPiece(pygame.sprite.Sprite):
  
  def __init__(self, pos, color, image_path):
    super().__init__()
    self.color = color
    self.image_orig = pygame.image.load(image_path).convert_alpha()
    self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.5)))
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.font = pygame.font.Font("fonts/ubuntuFont/Ubuntu-Bold.ttf", 20)
    self.mouse_left_click = False
    self.mouse_right_click = False
    self.piece_selected = False
    self.piece_moved = False
    self.previous_pos = self.rect.center
    self.previous_pos_xy = (self.rect.left, self.rect.top)

 
  def move(self):
    self.mouse_pos = pygame.mouse.get_pos()
    self.mouse_buttons = pygame.mouse.get_pressed()
    self.piece_pos = self.rect.center # for the take_piece function
    global glob_last_moved
    
    if self.rect.collidepoint(self.mouse_pos) and self.mouse_buttons[0] and not self.mouse_left_click:
      self.mouse_left_click = True
      self.piece_selected = True
    
    if self.mouse_buttons[0] and self.piece_selected and not self.mouse_left_click:
      self.piece_selected = False
      self.mouse_left_click = True

      if self.mouse_pos[1] < 800:
        self.y = ((self.mouse_pos[0] // 100) * 100) + 50
        self.x = ((self.mouse_pos[1] // 100) * 100) + 50
        self.rect.center = (self.y, self.x)
        self.piece_moved = True
        glob_last_moved = self
    
    if self.rect.collidepoint(self.mouse_pos) and self.mouse_buttons[2] and not self.mouse_right_click:
      self.piece_selected = False
      self.mouse_right_click = True

    if not self.mouse_buttons[2]:
      self.mouse_right_click = False
    
    if not self.mouse_buttons[0]:
      self.mouse_left_click = False   
  
  
  def highlight_piece(self):
    global glob_last_moved

    if self.piece_selected:
      pygame.draw.rect(screen, (0, 150, 0), self.rect, 3)
      self.previous_pos = self.rect.center
      self.previous_pos_xy = (self.rect.left, self.rect.top)
    
    elif self.rect.center != self.previous_pos and not glob_piece_selected and self == glob_last_moved:
      pygame.draw.rect(screen, (0, 255, 0), self.rect, 3)
      pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.previous_pos_xy, self.rect.size), 3)


  def write_move(self):
    
    def get_position_output(position):
      x_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
      y_names = ['8', '7', '6', '5', '4', '3', '2', '1']
      x_index = (position[0] - 50) // 100
      y_index = (position[1] - 50) // 100
      return x_names[x_index] + y_names[y_index]

    self.prev_pos_output = get_position_output(self.previous_pos)
    self.cur_pos_output = get_position_output(self.rect.center)
    self.output = self.prev_pos_output + "  :  " + self.cur_pos_output
    
    self.text_white = self.font.render(self.output, False, (255, 255, 255))
    self.text_white_background = pygame.Surface((self.text_white.get_width(), self.text_white.get_height()))
    self.text_black = self.font.render(self.output, False, (0, 0, 0))
    self.text_black_background = pygame.Surface((self.text_black.get_width(), self.text_black.get_height()))
  
    if self.piece_moved:
      
      if self.color == "white":
        self.text_white_background.fill((125, 150, 100))
        screen.blit(self.text_white_background, (15, 800))
        screen.blit(self.text_white, (15, 800))
      else:
        self.text_black_background.fill((125, 150, 100))
        screen.blit(self.text_black_background, (15, 800))
        screen.blit(self.text_black, (15, 800))
      
    if self.piece_selected:
      self.piece_moved = False

  
  def take_piece(self): 
    for sprite in pieces.sprites():
      if sprite != self and self.rect.colliderect(sprite.rect) and not self.piece_selected:
        if sprite.color != self.color:
          sprite.kill()
        else:
          self.rect.center = self.piece_pos


  def update(self):
    global glob_last_moved

    self.move()
    self.highlight_piece()
    if glob_last_moved == self:
      self.write_move()
    self.take_piece()


class pawn(ChessPiece):
  def __init__(self, pos, color):
    image_path = "images/pieces/blackPawn.png" if color == "black" else "images/pieces/whitePawn.png"
    super().__init__(pos, color, image_path)

class knight(ChessPiece):
  def __init__(self, pos, color):
    image_path = "images/pieces/blackKnight.png" if color == "black" else "images/pieces/whiteKnight.png"
    super().__init__(pos, color, image_path)

class bishop(ChessPiece):
  def __init__(self, pos, color):
    image_path = "images/pieces/blackBishop.png" if color == "black" else "images/pieces/whiteBishop.png"
    super().__init__(pos, color, image_path)

class rook(ChessPiece):
  def __init__(self, pos, color):
    image_path = "images/pieces/blackRook.png" if color == "black" else "images/pieces/whiteRook.png"
    super().__init__(pos, color, image_path)

class queen(ChessPiece):
  def __init__(self, pos, color):
    image_path = "images/pieces/blackQueen.png" if color == "black" else "images/pieces/whiteQueen.png"
    super().__init__(pos, color, image_path)

class king(ChessPiece):
  def __init__(self, pos, color):
    image_path = "images/pieces/blackKing.png" if color == "black" else "images/pieces/whiteKing.png"
    super().__init__(pos, color, image_path)

# Group
pieces = pygame.sprite.Group()

# black pieces
pieces.add(pawn((50, 150), "black"))
pieces.add(pawn((150, 150), "black"))
pieces.add(pawn((250, 150), "black"))
pieces.add(pawn((350, 150), "black"))
pieces.add(pawn((450, 150), "black"))
pieces.add(pawn((550, 150), "black"))
pieces.add(pawn((650, 150), "black"))
pieces.add(pawn((750, 150), "black"))

pieces.add(knight((150, 50), "black"))
pieces.add(knight((650, 50), "black"))

pieces.add(bishop((250, 50), "black"))
pieces.add(bishop((550, 50), "black"))

pieces.add(rook((50, 50), "black"))
pieces.add(rook((750, 50), "black"))

pieces.add(queen((350, 50), "black"))

pieces.add(king((450, 50), "black"))

# white pieces
pieces.add(pawn((50, 650), "white"))
pieces.add(pawn((150, 650), "white"))
pieces.add(pawn((250, 650), "white"))
pieces.add(pawn((350, 650), "white"))
pieces.add(pawn((450, 650), "white"))
pieces.add(pawn((550, 650), "white"))
pieces.add(pawn((650, 650), "white"))
pieces.add(pawn((750, 650), "white"))

pieces.add(knight((150, 750), "white"))
pieces.add(knight((650, 750), "white"))

pieces.add(bishop((250, 750), "white"))
pieces.add(bishop((550, 750), "white"))

pieces.add(rook((50, 750), "white"))
pieces.add(rook((750, 750), "white"))

pieces.add(queen((350, 750), "white"))

pieces.add(king((450, 750), "white"))


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit() # closing the game
      exit() # exiting the while loop
  
  screen.fill((125, 150, 100))
  screen.blit(board_surface, (0, 0))
  pieces.draw(screen)
  pieces.update()
  
  pygame.display.update()
  clock.tick(60)  # set maximum framerate