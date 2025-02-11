import pygame,sys, asyncio
from pygame.locals import *
from Plantilla import *
from Paleta import *       

ANCHO,ALTO=1000,700
screen=pygame.display.set_mode((ANCHO,ALTO))
clock = pygame.time.Clock()
screen.fill((255,255,255))

async def main():
    color=(0,0,0)
    rejilla=True

    plantilla=Plantilla(screen,ANCHO,ALTO)
    paleta=Paleta(screen,ANCHO,ALTO)

    plantilla.rejilla(screen)

    while 1:  
        
        mouse=pygame.mouse.get_pressed()
        pos=pygame.mouse.get_pos() 
            
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                sys.exit()
            
            if event.type==KEYDOWN and event.key==K_c:
                plantilla.limpiar_plantilla(screen)
                if rejilla==True:
                    plantilla.rejilla(screen)
                
            if event.type==KEYDOWN and event.key==K_s:
                plantilla.guardar_plantilla(screen)
                
            if event.type==KEYDOWN and event.key==K_r and rejilla==False:
                plantilla.rejilla(screen)
                rejilla=True
                
            if event.type==KEYDOWN and event.key==K_p and rejilla==True:
                plantilla.quitar_rejilla(screen)
                rejilla=False                        
                    
            if event.type==MOUSEBUTTONUP:                   
                if paleta.dentro_paleta(pos):
                    color=paleta.elegir_color(screen,pos)                
                    
            if mouse[0]==1:                    
                if plantilla.dentro_plantilla(pos):
                    if rejilla==False:
                        pygame.draw.circle(screen,color,pos,5)
                    else:
                        if screen.get_at((pos[0],pos[1]))!=(1,0,0):
                            celda=plantilla.celda(screen,pos)
                            pygame.draw.rect(screen,color,celda)                                 
            
        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main())