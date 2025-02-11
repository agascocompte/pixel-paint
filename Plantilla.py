import pygame


class Plantilla:
    def __init__(self,screen,ANCHO,ALTO):
        self.x=int(ANCHO/5)-10
        self.y=int(ALTO/50)
        self.weidgh=int(ANCHO-self.x-(9500/ANCHO)+6)
        self.height=int(ALTO-(2*self.y))        
        self.rect=(self.x,self.y,self.weidgh,self.height)
        pygame.draw.rect(screen,(1,0,0),self.rect,1)        
        
    def dentro_plantilla(self,pos):                        
        if pos[0]>self.x+5 and pos[0]<self.x+self.weidgh-5 and pos[1]>self.y+5 and pos[1]<self.y+self.height-5:            
            return True
        else: return False
        
    def limpiar_plantilla(self,screen):
        pygame.draw.rect(screen,(255,255,255),(self.x+1,self.y+1,self.weidgh-2,self.height-2))
        
    def guardar_plantilla(self,screen):
        sub=screen.subsurface(self.x+1,self.y+1,self.weidgh-2,self.height-2)
        sub=pygame.transform.scale(sub,(32,32))      
        pygame.image.save(sub, "dibujo.png")        
        print("Imagen GUARDADA en formato PNG en la carpeta del proyecto")
        
    def rejilla(self,screen):        
        for i in range(int(self.weidgh/31),self.weidgh,int(self.weidgh/31)):
            pygame.draw.line(screen,(1,0,0),(i+self.x,self.y+1),(i+self.x,self.y+self.height-2))
            for j in range(int(self.height/31),self.height,int(self.height/31)):
                pygame.draw.line(screen,(1,0,0),(self.x+1,j+self.y),(self.x+self.weidgh-2,j+self.y))                 
                
    def quitar_rejilla(self,screen):
        for i in range(self.weidgh-2):
            for j in range(self.height-2):
                if screen.get_at((self.x+i+1,self.y+j+1))==(1,0,0):
                    if screen.get_at((self.x+i+2,self.y+j+1))!=(1,0,0):
                        color=screen.get_at((self.x+i+2,self.y+j+1))
                        pygame.draw.line(screen,color,(self.x+i+1,self.y+j+1),(self.x+i+1,self.y+j+1))
                    else:
                        if screen.get_at((self.x+i+1,self.y+j+2))!=(1,0,0):
                            color=screen.get_at((self.x+i+1,self.y+j+2))
                            pygame.draw.line(screen,color,(self.x+i+1,self.y+j+1),(self.x+i+1,self.y+j+1))
                        else:
                            color=screen.get_at((self.x+i+2,self.y+j+2))
                            pygame.draw.line(screen,color,(self.x+i+1,self.y+j+1),(self.x+i+1,self.y+j+1))     
                
    def celda(self,screen,pos):
        x=0
        y=0
        weidgh=0
        height=0       
            
        for i in range (pos[0],self.x,-1):
            if screen.get_at((i-1,pos[1]))==(1,0,0):
                x=i
                break
            
        for i in range(pos[1],self.y,-1):
            if screen.get_at((pos[0],i-1))==(1,0,0):
                y=i
                break
            
        for i in range (pos[0],+self.x+self.weidgh):            
            if screen.get_at((i+1,pos[1]))==(1,0,0):
                weidgh=i-x+1
                break
            
        for i in range (pos[1],self.y+self.height):
            if screen.get_at((pos[0],i+1))==(1,0,0):
                height=i-y+1
                break    
            
        return (x,y,weidgh,height) 
    