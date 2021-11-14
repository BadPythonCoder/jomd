import jomd
from jomd.D2 import draw
window = jomd.screen.Window("test", (200, 200))

draw.point(window, 5, 5)

while window.running:
  window.draw()