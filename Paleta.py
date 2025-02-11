import pygame
from pygame.locals import *

negro=(0,0,0)
verde=(0,255,0)

class Paleta:
    def __init__(self,screen,ANCHO,ALTO):
        self.x=10
        self.y=int((ALTO/3))
        self.weidgh=int(10+(ANCHO/6))
        self.height=int(ALTO-(self.y+(9500/ALTO)))
        self.rect=(self.x,self.y,self.weidgh,self.height)        
        
        self.color1=0
        self.color2=0
        self.color3=0
        self.cuadrados=0  
        
        for i in range (self.weidgh):                        
            for j in range(self.height):
                if i%25==0:
                    pygame.draw.line(screen,negro,(self.x+i,self.y),(self.x+i,self.y+self.height-1))
                                               
                if j%56.5==0 or j%56.5==0.5:                    
                    pygame.draw.line(screen,negro,(self.x,self.y+j),(self.x+self.weidgh-1,self.y+j))
                    
                if i%25==0 and (j%56.5==0 or j%56.5==0.5) and j<self.height-1 and i<self.weidgh-1:
                    pygame.draw.rect(screen,(self.color1,self.color2,self.color3),(self.x+i,self.y+j,25,57))
                    
                    if self.cuadrados==0:
                        self.color1=64
                        self.color2=64
                        self.color3=64
                    if self.cuadrados==1:
                        self.color1=96
                        self.color2=96
                        self.color3=96
                    if self.cuadrados==2:
                        self.color1=128
                        self.color2=128
                        self.color3=128        
                    if self.cuadrados==3:
                        self.color1=160
                        self.color2=160
                        self.color3=160
                    if self.cuadrados==4:
                        self.color1=192
                        self.color2=192
                        self.color3=192
                    if self.cuadrados==5:
                        self.color1=224
                        self.color2=224
                        self.color3=224
                    if self.cuadrados==6:
                        self.color1=255
                        self.color2=255
                        self.color3=255
                    if self.cuadrados==7:
                        self.color1=102
                        self.color2=0
                        self.color3=0
                    if self.cuadrados==8:
                        self.color1=153
                        self.color2=0
                        self.color3=0
                    if self.cuadrados==9:
                        self.color1=204
                        self.color2=0
                        self.color3=0
                    if self.cuadrados==10:
                        self.color1=255
                        self.color2=0
                        self.color3=0
                    if self.cuadrados==11:
                        self.color1=255
                        self.color2=51
                        self.color3=51
                    if self.cuadrados==12:
                        self.color1=255
                        self.color2=102
                        self.color3=102
                    if self.cuadrados==13:
                        self.color1=255
                        self.color2=153
                        self.color3=153
                    if self.cuadrados==14:
                        self.color1=255
                        self.color2=204
                        self.color3=204
                    if self.cuadrados==15:
                        self.color1=102
                        self.color2=51
                        self.color3=0
                    if self.cuadrados==16:
                        self.color1=153
                        self.color2=76
                        self.color3=0
                    if self.cuadrados==17:
                        self.color1=204
                        self.color2=102
                        self.color3=0
                    if self.cuadrados==18:
                        self.color1=255
                        self.color2=128
                        self.color3=0
                    if self.cuadrados==19:
                        self.color1=255
                        self.color2=153
                        self.color3=51
                    if self.cuadrados==20:
                        self.color1=255
                        self.color2=178
                        self.color3=102
                    if self.cuadrados==21:
                        self.color1=255
                        self.color2=204
                        self.color3=153
                    if self.cuadrados==22:
                        self.color1=255
                        self.color2=229
                        self.color3=204
                    if self.cuadrados==23:
                        self.color1=102
                        self.color2=102
                        self.color3=0
                    if self.cuadrados==24:
                        self.color1=153
                        self.color2=153
                        self.color3=0
                    if self.cuadrados==25:
                        self.color1=204
                        self.color2=204
                        self.color3=0
                    if self.cuadrados==26:
                        self.color1=255
                        self.color2=255
                        self.color3=0
                    if self.cuadrados==27:
                        self.color1=255
                        self.color2=255
                        self.color3=51
                    if self.cuadrados==28:
                        self.color1=255
                        self.color2=255
                        self.color3=102    
                    if self.cuadrados==29:
                        self.color1=255
                        self.color2=255
                        self.color3=153
                    if self.cuadrados==30:
                        self.color1=255
                        self.color2=255
                        self.color3=204
                    if self.cuadrados==31:
                        self.color1=0
                        self.color2=102
                        self.color3=0
                    if self.cuadrados==32:
                        self.color1=0
                        self.color2=153
                        self.color3=0
                    if self.cuadrados==33:
                        self.color1=0
                        self.color2=204
                        self.color3=0
                    if self.cuadrados==34:
                        self.color1=0
                        self.color2=255
                        self.color3=0
                    if self.cuadrados==35:
                        self.color1=51
                        self.color2=255
                        self.color3=51
                    if self.cuadrados==36:
                        self.color1=102
                        self.color2=255
                        self.color3=102
                    if self.cuadrados==37:
                        self.color1=153
                        self.color2=255
                        self.color3=153
                    if self.cuadrados==38:
                        self.color1=204
                        self.color2=255
                        self.color3=204
                    if self.cuadrados==39:
                        self.color1=0
                        self.color2=51
                        self.color3=102
                    if self.cuadrados==40:
                        self.color1=0
                        self.color2=76
                        self.color3=153
                    if self.cuadrados==41:
                        self.color1=0
                        self.color2=128
                        self.color3=255
                    if self.cuadrados==42:
                        self.color1=0
                        self.color2=0
                        self.color3=255
                    if self.cuadrados==43:
                        self.color1=51
                        self.color2=51
                        self.color3=255
                    if self.cuadrados==44:
                        self.color1=51
                        self.color2=153
                        self.color3=255
                    if self.cuadrados==45:
                        self.color1=0
                        self.color2=255
                        self.color3=255
                    if self.cuadrados==46:
                        self.color1=153
                        self.color2=255
                        self.color3=255
                    if self.cuadrados==47:
                        self.color1=51
                        self.color2=0
                        self.color3=102
                    if self.cuadrados==48:
                        self.color1=153
                        self.color2=0
                        self.color3=153
                    if self.cuadrados==49:
                        self.color1=204
                        self.color2=0
                        self.color3=204
                    if self.cuadrados==50:
                        self.color1=255
                        self.color2=0
                        self.color3=255
                    if self.cuadrados==51:
                        self.color1=153
                        self.color2=51
                        self.color3=255
                    if self.cuadrados==52:
                        self.color1=255
                        self.color2=102
                        self.color3=255
                    if self.cuadrados==53:
                        self.color1=255
                        self.color2=153
                        self.color3=204
                    if self.cuadrados==54:
                        self.color1=255
                        self.color2=204
                        self.color3=204                                                                                                                                                                                                                                                           
                    
                    self.cuadrados+=1
    
    def dentro_paleta(self,pos):
        if pos[0]>self.x and pos[0]<self.x+self.weidgh and pos[1]>self.y and pos[1]<self.y+self.height:
            return True
        else: return False
                    
    def elegir_color(self,screen,pos):       
        color=screen.get_at((pos[0],pos[1]))        
        return color
        
        
                                                                
                           
            