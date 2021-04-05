
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((620, 340))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((255, 255, 255))
        bx = 0
        by = 0
        w = 620
        h = 340
        t = 1
        pygame.draw.line(screen, (0, 0, 0), (bx, by), (bx + w, by), 2 * t)
        pygame.draw.line(screen, (0, 0, 0), (bx, by), (bx, h), 2 * t)

        pygame.draw.line(screen, (0, 0, 0), (bx, by + h - 2 * t), (w, h - 2 * t), 2 * t)
        pygame.draw.line(screen, (0, 0, 0), (bx + w - 2 * t, by), (w - 2 * t, by + h), 2 * t)

        for i in range(33):
          y = 10 + 10 * i
          if i % 4 == 0:
            pygame.draw.line(screen, (0, 0, 0), (bx, y), (bx + w, y), 1 * t)
          if i % 4 == 1 or i % 4 == 3:
            pygame.draw.line(screen, (0, 0, 0), (bx, y), (bx + 3 * t, y), 1 * t)
            pygame.draw.line(screen, (0, 0, 0), (bx + w - 4 * t, y), (bx + w, y), 1 * t)
          if i % 4 == 2:
            pygame.draw.line(screen, (0, 0, 0), (bx, y), (bx + 5 * t, y), 1 * t)
            pygame.draw.line(screen, (0, 0, 0), (bx + w - 6 * t, y), (bx + w, y), 1 * t)

        pygame.draw.line(screen, (0, 0, 0), (bx, by + h / 2), (bx + w, by + h / 2), 2 * t)
        pygame.draw.line(screen, (0, 0, 0), (bx + w / 2, 0), (bx + w / 2, 340), 2 * t)

        for i in range(49):
          x = 10 + 12.5 * i
          if i % 8 == 0:
            pygame.draw.line(screen, (0, 0, 0), (x, by), (x, by + h), 1 * t)
          if i % 4 == 0:
            pygame.draw.line(screen, (0, 0, 0), (x, by), (x, by + 7 * t), 1 * t)
            pygame.draw.line(screen, (0, 0, 0), (x, by + h - 8 * t), (x, y + h), 1 * t)
          if i % 4 == 1 or i % 4 == 3:
            pygame.draw.line(screen, (0, 0, 0), (x, by), (x, by + 3 * t), 1 * t)
            pygame.draw.line(screen, (0, 0, 0), (x, by + h - 4 * t), (x, by + h), 1 * t)
          if i % 4 == 2:
            pygame.draw.line(screen, (0, 0, 0), (x, by), (x, by + 5 * t), 1 * t)
            pygame.draw.line(screen, (0, 0, 0), (x, by + h - 6 * t), (x, y + h), 1 * t)
        
        x1 = bx + 10
        y1 = by + h / 2
        while x1 <= 609:
          x2 = x1 + 1
          coord = x2 - w / 2 - w / 6 + 3
          y2 = by + h /2 + (math.sin(coord / 100 * math.pi)) * 160
          pygame.draw.aaline(screen, (150, 0, 0), (x1, y1), (x2, y2), 1 * t)
          x1 = x2
          y1 = y2

        x1 = bx + 10
        y1 = by + h / 2
        color = (0, 0, 150)     
        while x1 <= 609:
          x2 = x1 + 1
          if x2 % 8 == 2:
            color = (0, 0, 150)
          if x2 % 8 == 0:
            color = (255, 255, 255)
          coord = x2 - w / 2 - w / 12 + 1
          y2 = by + h /2 + (math.sin(coord / 100 * math.pi)) * 160
          pygame.draw.aaline(screen, color, (x1, y1), (x2, y2), 1 * t)
          x1 = x2
          y1 = y2


        

        pygame.display.flip()