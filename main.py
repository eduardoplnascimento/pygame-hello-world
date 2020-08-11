import pygame

pygame.init()
window = pygame.display.set_mode([800, 580])

while True:
  window.fill((255, 255, 255))

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