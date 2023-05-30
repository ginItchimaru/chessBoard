#!/usr/bin/python3

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))

board = pygame.image.load("images/chessboard/chessboardgreen.png").convert()
board_width = int(board.get_width() * 0.685)
board_height = int(board.get_height() * 0.685)
board_size = (board_width, board_height)

board = pygame.transform.scale(board, board_size)

class Piece(pygame.sprite.Sprite):

  def __init__(self, pos, color):
    super().__init__()

    self.color = color
    
    if self.color == "black":
      self.image_orig = pygame.image.load("images/pieces/blackRook.png").convert_alpha()
      self.image = pygame.transform.scale(self.image_orig, (int(self.image_orig.get_width() * 0.5), int(self.image_orig.get_height() * 0.5)))
      self.rect = self.image.get_rect()
      self.rect.center = pos
    
    elif self.color == "white":
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
      self.piece_selected = False
      self.mouse_click = True
      self.y = ((self.mouse_pos[0] // 100) * 100) + 50
      self.x = ((self.mouse_pos[1] // 100) * 100) + 50
      self.rect.center = (self.y, self.x)

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

pieces = pygame.sprite.Group()
pieces.add(Piece((50, 750), "white"))
pieces.add(Piece((750, 750), "white"))
pieces.add(Piece((50, 50), "black"))
pieces.add(Piece((750, 50), "black"))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(board, (0, 0))
  pieces.draw(screen)
  pieces.update()
  
  pygame.display.flip()


pygame.quit()