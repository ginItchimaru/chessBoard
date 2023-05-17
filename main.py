#!/usr/bin/python3

import pygame
from sys import exit

pygame.init() # initializing the pygame module
screen = pygame.display.set_mode((800, 800)) # screen size
pygame.display.set_caption("Chess") # Game name
clock = pygame.time.Clock() # frame rate

# board
board_surface = pygame.image.load("images/chessboard/chessboardgreen.png").convert()
board_height = int(board_surface.get_height() * 0.685)
board_width = int(board_surface.get_width() * 0.685)
board_size = (board_width, board_height)
board_surface = pygame.transform.scale(board_surface, board_size)

# classes
class pawn(pygame.sprite.Sprite):
  
  def __init__(self, pos, color):
    super().__init__()

    self.color = color
    
    if self.color == "black":
      self.image_orig = pygame.image.load("images/pieces/blackPawn.png").convert_alpha()
      self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.5)))
      self.rect = self.image.get_rect()
      self.rect.center = pos

    elif self.color == "white":
      self.image_orig = pygame.image.load("images/pieces/whitePawn.png").convert_alpha()
      self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.5)))
      self.rect = self.image.get_rect()
      self.rect.center = pos
    
    self.mouse_click = False
    self.piece_selected = False
  
  def move(self):
    self.mouse_pos = pygame.mouse.get_pos()
    self.mouse_buttons = pygame.mouse.get_pressed()
    self.piece_pos = self.rect.center
    
    if self.rect.collidepoint(self.mouse_pos) and self.mouse_buttons[0] and not self.mouse_click:
      self.mouse_click = True
      self.piece_selected = True
    
    if self.mouse_buttons[0] and self.piece_selected and not self.mouse_click:
      self.y = ((self.mouse_pos[0] // 100) * 100) + 50
      self.x = ((self.mouse_pos[1] // 100) * 100) + 50
      self.rect.center = (self.y, self.x) 
      self.piece_selected = False
      self.mouse_click = True

    if not self.mouse_buttons[0]:
      self.mouse_click = False
    
  def highlight_piece(self):
    if self.piece_selected:
      pygame.draw.rect(screen, "Green", self.rect, 3)

  def take_piece(self): 
    for sprite in pieces.sprites():
      if sprite != self and self.rect.colliderect(sprite.rect) and not self.piece_selected:
        if sprite.color != self.color:
          sprite.kill()
        else:
          self.rect.center = self.piece_pos

  def update(self):
    self.move()
    self.highlight_piece()
    self.take_piece()

class knight(pygame.sprite.Sprite):
  
  def __init__(self, pos, color):
    super().__init__()
    
    self.color = color

    if self.color == "black":
      self.image_orig = pygame.image.load("images/pieces/blackKnight.png").convert_alpha()
      self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.5)))
      self.rect = self.image.get_rect()
      self.rect.center = pos
    
    elif self.color == "white":
      self.image_orig = pygame.image.load("images/pieces/whiteKnight.png").convert_alpha()
      self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.5)))
      self.rect = self.image.get_rect()
      self.rect.center = pos

    self.mouse_click = False
    self.piece_selected = False
  
  def move(self):
    self.mouse_pos = pygame.mouse.get_pos()
    self.mouse_buttons = pygame.mouse.get_pressed()
    self.piece_pos = self.rect.center
   
    if self.rect.collidepoint(self.mouse_pos) and self.mouse_buttons[0] and not self.mouse_click:
      self.mouse_click = True
      self.piece_selected = True
    
    if self.mouse_buttons[0] and self.piece_selected and not self.mouse_click:
      self.y = ((self.mouse_pos[0] // 100) * 100) + 50
      self.x = ((self.mouse_pos[1] // 100) * 100) + 50
      self.rect.center = (self.y, self.x)
      self.piece_selected = False
      self.mouse_click = True

    if not self.mouse_buttons[0]:
      self.mouse_click = False
  
  def highlight_piece(self):
    if self.piece_selected:
      pygame.draw.rect(screen, "Green", self.rect, 3)

  def take_piece(self): 
    for sprite in pieces.sprites():
      if sprite != self and self.rect.colliderect(sprite.rect) and not self.piece_selected:
        if sprite.color != self.color:
          sprite.kill()
        else:
          self.rect.center = self.piece_pos

  def update(self):
    self.move()
    self.highlight_piece()
    self.take_piece()

class bishop(pygame.sprite.Sprite):

  def __init__(self, pos, color):
    super().__init__()

    self.color = color
    
    if self.color == "black":
      self.image_orig = pygame.image.load("images/pieces/blackBishop.png").convert_alpha()
      self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.5)))
      self.rect = self.image.get_rect()
      self.rect.center = pos
    
    elif self.color == "white":
      self.image_orig = pygame.image.load("images/pieces/whiteBishop.png").convert_alpha()
      self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.5)))
      self.rect = self.image.get_rect()
      self.rect.center = pos

    self.mouse_click = False
    self.piece_selected = False
  
  def move(self):
    self.mouse_pos = pygame.mouse.get_pos()
    self.mouse_buttons = pygame.mouse.get_pressed()
    self.piece_pos = self.rect.center
    
    if self.rect.collidepoint(self.mouse_pos) and self.mouse_buttons[0] and not self.mouse_click:
      self.mouse_click = True
      self.piece_selected = True
    
    if self.mouse_buttons[0] and self.piece_selected and not self.mouse_click:
      self.y = ((self.mouse_pos[0] // 100) * 100) + 50
      self.x = ((self.mouse_pos[1] // 100) * 100) + 50
      self.rect.center = (self.y, self.x)
      self.piece_selected = False
      self.mouse_click = True

    if not self.mouse_buttons[0]:
      self.mouse_click = False
  
  def highlight_piece(self):
    if self.piece_selected:
      pygame.draw.rect(screen, "Green", self.rect, 3)
  
  def take_piece(self): 
    for sprite in pieces.sprites():
      if sprite != self and self.rect.colliderect(sprite.rect) and not self.piece_selected:
        if sprite.color != self.color:
          sprite.kill()
        else:
          self.rect.center = self.piece_pos

  def update(self):
    self.move()
    self.highlight_piece()
    self.take_piece()

class rook(pygame.sprite.Sprite):

  def __init__(self, pos, color):
    super().__init__()

    self.color = color
    
    if color == "black":
      self.image_orig = pygame.image.load("images/pieces/blackRook.png").convert_alpha()
      self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.5)))
      self.rect = self.image.get_rect()
      self.rect.center = pos
  
    elif color == "white":
      self.image_orig = pygame.image.load("images/pieces/whiteRook.png").convert_alpha()
      self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.5)))
      self.rect = self.image.get_rect()
      self.rect.center = pos

    self.mouse_click = False
    self.piece_selected = False
  
  def move(self):
    self.mouse_pos = pygame.mouse.get_pos()
    self.mouse_buttons = pygame.mouse.get_pressed()
    self.piece_pos = self.rect.center
    
    if self.rect.collidepoint(self.mouse_pos) and self.mouse_buttons[0] and not self.mouse_click:
      self.mouse_click = True
      self.piece_selected = True
    
    if self.mouse_buttons[0] and self.piece_selected and not self.mouse_click:
      self.y = ((self.mouse_pos[0] // 100) * 100) + 50
      self.x = ((self.mouse_pos[1] // 100) * 100) + 50
      self.rect.center = (self.y, self.x)
      self.piece_selected = False
      self.mouse_click = True

    if not self.mouse_buttons[0]:
      self.mouse_click = False

  def highlight_piece(self):
    if self.piece_selected:
      pygame.draw.rect(screen, "Green", self.rect, 3)
  
  def take_piece(self): 
    for sprite in pieces.sprites():
      if sprite != self and self.rect.colliderect(sprite.rect) and not self.piece_selected:
        if sprite.color != self.color:
          sprite.kill()
        else:
          self.rect.center = self.piece_pos

  def update(self):
    self.move()
    self.highlight_piece()  
    self.take_piece()

class queen(pygame.sprite.Sprite):

  def __init__(self, pos, color):
    super().__init__()

    self.color = color
    
    if self.color == "black":
      self.image_orig = pygame.image.load("images/pieces/blackQueen.png").convert_alpha()
      self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.45)))
      self.rect = self.image.get_rect()
      self.rect.center = pos
    
    elif self.color == "white":
      self.image_orig = pygame.image.load("images/pieces/whiteQueen.png").convert_alpha()
      self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.45)))
      self.rect = self.image.get_rect()
      self.rect.center = pos

    self.mouse_click = False
    self.piece_selected = False
  
  def move(self):
    self.mouse_pos = pygame.mouse.get_pos()
    self.mouse_buttons = pygame.mouse.get_pressed()
    self.piece_pos = self.rect.center
    
    if self.rect.collidepoint(self.mouse_pos) and self.mouse_buttons[0] and not self.mouse_click:
      self.mouse_click = True
      self.piece_selected = True
    
    if self.mouse_buttons[0] and self.piece_selected and not self.mouse_click:
      self.y = ((self.mouse_pos[0] // 100) * 100) + 50
      self.x = ((self.mouse_pos[1] // 100) * 100) + 50
      self.rect.center = (self.y, self.x)
      self.piece_selected = False
      self.mouse_click = True

    if not self.mouse_buttons[0]:
      self.mouse_click = False

  def highlight_piece(self):
    if self.piece_selected:
      pygame.draw.rect(screen, "Green", self.rect, 3)

  def take_piece(self): 
    for sprite in pieces.sprites():
      if sprite != self and self.rect.colliderect(sprite.rect) and not self.piece_selected:
        if sprite.color != self.color:
          sprite.kill()
        else:
          self.rect.center = self.piece_pos

  def update(self):
    self.move()
    self.highlight_piece()
    self.take_piece()

class king(pygame.sprite.Sprite):

  def __init__(self, pos, color):
    super().__init__()

    self.color = color
    
    if self.color == "black":
      self.image_orig = pygame.image.load("images/pieces/blackKing.png").convert_alpha()
      self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.45)))
      self.rect = self.image.get_rect()
      self.rect.center = pos
    
    elif self.color == "white":
      self.image_orig = pygame.image.load("images/pieces/whiteKing.png").convert_alpha()
      self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.45)))
      self.rect = self.image.get_rect()
      self.rect.center = pos

    self.mouse_click = False
    self.piece_selected = False
  
  def move(self):
    self.mouse_pos = pygame.mouse.get_pos()
    self.mouse_buttons = pygame.mouse.get_pressed()
    self.piece_pos = self.rect.center
    
    if self.rect.collidepoint(self.mouse_pos) and self.mouse_buttons[0] and not self.mouse_click:
      self.mouse_click = True
      self.piece_selected = True
    
    if self.mouse_buttons[0] and self.piece_selected and not self.mouse_click:
      self.y = ((self.mouse_pos[0] // 100) * 100) + 50
      self.x = ((self.mouse_pos[1] // 100) * 100) + 50
      self.rect.center = (self.y, self.x)
      self.piece_selected = False
      self.mouse_click = True

    if not self.mouse_buttons[0]:
      self.mouse_click = False
  
  def highlight_piece(self):
    if self.piece_selected:
      pygame.draw.rect(screen, "Green", self.rect, 3)

  def take_piece(self): 
    for sprite in pieces.sprites():
      if sprite != self and self.rect.colliderect(sprite.rect) and not self.piece_selected:
        if sprite.color != self.color:
          sprite.kill()
        else:
          self.rect.center = self.piece_pos

  def update(self):
    self.move()
    self.highlight_piece()
    self.take_piece()

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
  
  # board
  screen.blit(board_surface, (0, 0))
  pieces.draw(screen)
  pieces.update()
  
  pygame.display.update()
  clock.tick(60)  # set maximum framerate