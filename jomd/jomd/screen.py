import pygame

class Window:
  running = True
  root = None
  drawings = []
  def __init__(self, name, dimensions):
    self.name = name
    self.dimensions = dimensions
    self.x = dimensions[0]
    self.y = dimensions[1]
    self.initialize()
  def dot(self, x, y):
    pygame.draw.circle(self.root, (255,255,255), (x, y), 5)
  def initialize(self):
    pygame.init()
    self.root = pygame.display.set_mode(self.dimensions)
    pygame.display.set_caption(self.name)
  def draw(self):
    self.root.fill((0,0,0))
    for drawing in self.drawings:
      drawing[0](
        drawing[1][0]+(self.x/2),
        drawing[1][1]+(self.y/2)
      )
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
    pygame.display.update()