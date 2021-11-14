import pygame

class Window:
  running = True
  root = None
  drawings = {}
  def __init__(self, name, dimensions):
    self.name = name
    self.dimensions = dimensions
    self.x = dimensions[0]
    self.y = dimensions[1]
    self.initialize()
  def initialize(self):
    pygame.init()
    self.root = pygame.display.set_mode(self.dimensions)
    pygame.display.set_caption(self.name)
  def drawWindow(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
    self.root.fill((0,0,0))
    