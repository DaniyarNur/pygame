import pygame
import math

pygame.init()
screen = pygame.display.set_mode((740, 450))
screen1 = pygame.Surface((620, 340), pygame.SRCALPHA)

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
        v_axis = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
        h_axis1 = ['-3pi', '-2pi', '-pi', '  0', ' pi', ' 2pi', ' 3pi']
        h_axis2 = ['-5pi/2', '-3pi/2', '-pi/2', 'pi/2', '3pi/2', '5pi/2']

        font = pygame.font.SysFont('arial', 15)
        text1 = font.render("sin x", True, (0, 0, 0))
        text2 = font.render("cos x", True, (0, 0, 0))
        

        screen.blit(screen1, (80, 10))
        screen.blit(text1, (500 - text1.get_width() // 2, 30 - text1.get_height() // 2))
        screen.blit(text2, (500 - text2.get_width() // 2, 50 - text2.get_height() // 2))

        #-3 -2 -1
        xx3 = font.render('-3', True, (0, 0, 0))
        xx2 = font.render('-2', True, (0, 0, 0))
        xx1 = font.render('-1', True, (0, 0, 0))
        screen.blit(xx3, (100, 200))
        screen.blit(xx2, (170, 200))
        screen.blit(xx1, (260, 200))

        pygame.draw.line(screen1, (0, 0, 0), (bx, by), (bx + w, by), 2 * t)
        pygame.draw.line(screen1, (0, 0, 0), (bx, by), (bx, h), 2 * t)

        pygame.draw.line(screen1, (0, 0, 0), (bx, by + h - 2 * t), (w, h - 2 * t), 2 * t)
        pygame.draw.line(screen1, (0, 0, 0), (bx + w - 2 * t, by), (w - 2 * t, by + h), 2 * t)


        counter = 0
        #horizontal lines
        for i in range(33):
          y = 10 + 10 * i
          if i % 4 == 0:
            pygame.draw.line(screen1, (0, 0, 0), (bx, y), (bx + w, y), 1 * t)
            text = font.render(v_axis[counter], True, (0, 0, 0))
            counter += 1
            screen.blit(text, (45, y + 3))

          if i % 4 == 1 or i % 4 == 3:
            pygame.draw.line(screen1, (0, 0, 0), (bx, y), (bx + 3 * t, y), 1 * t)
            pygame.draw.line(screen1, (0, 0, 0), (bx + w - 4 * t, y), (bx + w, y), 1 * t)
          if i % 4 == 2:
            pygame.draw.line(screen1, (0, 0, 0), (bx, y), (bx + 5 * t, y), 1 * t)
            pygame.draw.line(screen1, (0, 0, 0), (bx + w - 6 * t, y), (bx + w, y), 1 * t)

        pygame.draw.line(screen1, (0, 0, 0), (bx, by + h / 2), (bx + w, by + h / 2), 2 * t)
        pygame.draw.line(screen1, (0, 0, 0), (bx + w / 2, 0), (bx + w / 2, 340), 2 * t)

        counter = 0
        #vertical lines
        for i in range(49):
          x = 10 + 12.5 * i
          if i % 8 == 0:
            pygame.draw.line(screen1, (0, 0, 0), (x, by), (x, by + h), 1 * t)
            pygame.draw.line(screen1, (0, 0, 0), (bx, y), (bx + w, y), 1 * t)
            text = font.render(h_axis1[counter], True, (0, 0, 0))
            screen.blit(text, (68 + x, 360))

          if i % 4 == 0 and i % 8 != 0:
            pygame.draw.line(screen1, (0, 0, 0), (x, by), (x, by + 7 * t), 1 * t)
            pygame.draw.line(screen1, (0, 0, 0), (x, by + h - 8 * t), (x, y + h), 1 * t)
            pygame.draw.line(screen1, (0, 0, 0), (bx, y), (bx + w, y), 1 * t)
            text = font.render(h_axis2[counter], True, (0, 0, 0))
            counter += 1
            screen.blit(text, (68 + x, 360))

          if i % 4 == 1 or i % 4 == 3:
            pygame.draw.line(screen1, (0, 0, 0), (x, by), (x, by + 3 * t), 1 * t)
            pygame.draw.line(screen1, (0, 0, 0), (x, by + h - 4 * t), (x, by + h), 1 * t)
          if i % 4 == 2:
            pygame.draw.line(screen1, (0, 0, 0), (x, by), (x, by + 5 * t), 1 * t)
            pygame.draw.line(screen1, (0, 0, 0), (x, by + h - 6 * t), (x, y + h), 1 * t)
        
        #white corrective line
          pygame.draw.line(screen1, (255, 255, 255), (410, 11), (410, 49), 1)
        #functions defining lines 
          pygame.draw.line(screen1, (150, 0, 0), (445, 20), (470, 20), 2)
          pygame.draw.line(screen1, (0, 0, 150), (445, 40), (458, 40), 2)
          pygame.draw.line(screen1, (0, 0, 150), (462, 40), (470, 40), 2)
        #letter X
          xx = font.render('X', True, (0, 0, 0))
          screen.blit(xx, (390, 390))


        x1 = bx + 10
        y1 = by + h / 2
        while x1 <= 609:
          x2 = x1 + 1
          coord = x2 - w / 2 - w / 6 + 3
          y2 = by + h /2 + (math.sin(coord / 100 * math.pi)) * 160
          pygame.draw.aaline(screen1, (150, 0, 0), (x1, y1), (x2, y2), 1 * t)
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
          pygame.draw.aaline(screen1, color, (x1, y1), (x2, y2), 1 * t)
          x1 = x2
          y1 = y2
          

        pygame.display.flip()