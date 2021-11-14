from jomd import screen


window = screen.Window("test", (200, 200))

while window.running:
  window.drawWindow()