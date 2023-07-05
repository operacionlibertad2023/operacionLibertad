import pygame
import Mapa_Zelda
from soporte import import_folde
class Link(pygame.sprite.Sprite):
    def __init__(self, pos,groups,Obstaculos):
        super().__init__(groups)
        
        self.image = pygame.image.load("c:\operación libertad\p0.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        
 #       self.import_player_assets()
 #       self.status = 'down'
 #       self.frame_index = 0
 #       self.animation_speed = 0.15
        
        
        self.direccion = pygame.math.Vector2()
        self.velocidad = 5
        
        self.Obstaculos = Obstaculos
        
   # def import_player_assets(self):
    #    character_path = "C:\operación libertad\principal/"
     #   self.animations = {'up':[],'down':[],'left':[],'right':[],
      #       'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[]}
      #  
      #  for animation in self.animations.keys():
      #      full_path = character_path + animation
      #      self.animations[animation] = import_folde(full_path)
    def teclado(self):
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_UP]:
            self.direccion.y = -1
            self.status = 'up'
        
        elif keys[pygame.K_DOWN]:
            self.direccion.y = 1
            self.status = 'down'
        
        else:
            self.direccion.y = 0
        
        if keys[pygame.K_RIGHT]:
            self.direccion.x = 1
            self.status = 'right'
        
        elif keys[pygame.K_LEFT]:
            self.direccion.x = -1
            self.status = 'left'
        
        else:
            self.direccion.x = 0
        
#    def get_status(self):
#        
#        if self.direccion.x == 0 and self.direccion.y == 0:
#            if not 'idle' in self.status:
#                self.status = self.status + '_idle'
#                
#        
        
    def mover(self, velocidad):
        if self.direccion.magnitude() != 0:
            self.direccion = self.direccion.normalize()
            
        self.rect.x += self.direccion.x * velocidad
        self.coliciones("horizontal")
        
        self.rect.y += self.direccion.y * velocidad
        self.coliciones("vertical")
                        
    def coliciones(self, direccion):
        if direccion == "horizontal":
            for sprite in self.Obstaculos:
                if sprite.rect.colliderect(self.rect):
                    if self.direccion.x > 0:
                        self.rect.right = sprite.rect.left
                        
                    if self.direccion.x < 0:
                        self.rect.left = sprite.rect.right
                        
        if direccion == "vertical":
            for sprite in self.Obstaculos:
                if sprite.rect.colliderect(self.rect):
                    if self.direccion.y > 0:
                        self.rect.bottom = sprite.rect.top
                        
                    if self.direccion.y < 0:
                        self.rect.top = sprite.rect.bottom
        
 #   def  animate(self):
 #       animation = self.animations[self.status]
 #        
 #       self.frame_index += self.animation_speed
 #       if self.frame_index >= len(animation):
 #           self.frame_index = 0
 #           
 #       self.image = animation[int(self.frame_index)] 
 #       self.rect = self.image.get_rect(center = self.hitbox.center)
 #       
        
    def update(self):
        self.teclado()
   #     self.get_status()
  #      self.animate()
        self.mover(self.velocidad)