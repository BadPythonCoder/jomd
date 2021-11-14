import threading, pygame

class WindowBase:
  root = None
  thread = None
  running = True
  drawings = {}
  def __init__(self, name, dimensions):
    self.name = name
    self.dimensions = dimensions
    self.x = dimensions[0]
    self.y = dimensions[1]
  def initialize(self):
    pygame.init()
    self.root = pygame.display.set_mode(self.dimensions)
    pygame.display.set_caption(self.name)
    self.thread = threading.Thread(target=self.Windowloop, daemon=True)
    self.thread.start()
  def WindowLoop(self):
    while self.running:
      self.root.fill((0,0,0))
      for event in pygame.event.get():
        if event.type == pygame.QUIT():
          self.running = False
          break

class Window(WindowBase):
  def __init__(self):
    self.initialize()