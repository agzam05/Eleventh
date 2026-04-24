import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()
radius=10
mode="draw"
color=(0,0,255)
points=[]
starts_pos=None
drawing=False
def Drawline(screen,points, color,radius):
    for i in range(len(points)-1):
        pygame.draw.line(screen, color, points[i], points[i+1], radius)
running=True
while running:
    for event in pygame.event.get():
        if event.type== QUIT:
            running=False
        if event.type==KEYDOWN:
            if event.key==K_r:
                mode="rect"
            elif event.key==K_c:
                mode="circle"
            elif event.key==K_d:
                mode="draw"
            elif event.key==K_e:
                mode="erase"
            elif event.key==K_1:
                color=(255, 0, 0)
            elif event.key==K_2:
                color=(0,255,0)
            elif event.key==K_3:
                color=(0,0,255)
            elif event.key==K_UP:
                radius=min(200, radius+2)
            elif event.key==K_DOWN:
                radius=max(2, radius-2)
        if event.type==MOUSEBUTTONDOWN:
            starts_pos=event.pos
            drawing=True
            points=[event.pos]
        if event.type==MOUSEMOTION and drawing:
            if mode in ["draw", "erase"]:
                points.append(event.pos)
        if event.type==MOUSEBUTTONUP:
            drawing=False
            end_pos=event.pos
            if mode=="rect":
                rect=pygame.Rect(starts_pos[0], starts_pos[1], (end_pos[0]-starts_pos[0]), (end_pos[1]-starts_pos[1]))
                pygame.draw.rect(screen, color, rect, radius)
            elif mode=="circle":
                dx=end_pos[0]-starts_pos[0]
                dy=end_pos[1]-starts_pos[1]
                r=int(((dx**2)+(dy**2))**0.5)
                pygame.draw.circle(screen, color, starts_pos, r, radius)
        if drawing and mode in ["draw", "erase"]:
            if mode=="erase":
                color=(0,0,0)
            Drawline(screen, points, color, radius)
        pygame.display.flip()
        clock.tick(30)
pygame.quit()

        

