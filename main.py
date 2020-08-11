import pygame

pygame.init()
window = pygame.display.set_mode([800, 580])

while True:
  window.fill((255, 255, 255))

  for x in range(100, 110):
    for y in range(100, 180):
      window.set_at([x, y], (0, 0, 0))

  pygame.draw.line(
    window,
    (50, 200, 50),
    [300, 300],
    [400, 400],
    5
  )

  pygame.draw.line(
    window,
    (50, 50, 200),
    [400, 400],
    [500, 300],
    8
  )

  pygame.display.update()