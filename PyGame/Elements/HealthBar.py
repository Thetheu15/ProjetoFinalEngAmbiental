import pygame

class HealthBar:
    def __init__(self, screen, position, maxHealth, height=30, hitDamage=100, backGroundColor=(50, 50, 50), healthBarColor=(0, 255, 0), damageColor=(255, 0, 0)):
        self.screen = screen
        self.position = position
        self.maxHealth = maxHealth
        self.currentHealth = maxHealth
        self.height = height
        self.hitDamage = hitDamage
        self.backGroundColor = backGroundColor
        self.healthColor = healthBarColor
        self.damageColor = damageColor

        self.healthDownCounter = 60
        self.postDamageCounter = 0
        self.countDamageTaken  = 0
        self.damageTaken       = False
    
    def draw(self):
        self.healthBarDinamics(self.hitDamage)
    
    def doDamage(self):
        self.damageTaken = True
        self.countDamageTaken += 1

    def healthBarDinamics(self, damage):
        if self.healthDownCounter > 0 and self.damageTaken == True:
            self.postDamageCounter = damage*0.4
            self.currentHealth -= damage/60

            pygame.draw.rect(self.screen, self.backGroundColor, (self.position[0], self.position[1], self.maxHealth, self.height))

            pygame.draw.rect(self.screen, self.healthColor, (self.position[0], self.position[1], 
                                                            (self.currentHealth + damage*0.4
                                                             if self.currentHealth < self.maxHealth - damage*self.countDamageTaken + damage*0.6 
                                                             else self.maxHealth - damage*(self.countDamageTaken - 1)), 
                                                             self.height))
            
            pygame.draw.rect(self.screen, self.damageColor, (self.position[0], self.position[1], self.currentHealth, self.height))
            
            self.healthDownCounter -= 1

        elif self.healthDownCounter == 0:
            pygame.draw.rect(self.screen,self.backGroundColor, (self.position[0], self.position[1], self.maxHealth, self.height))

            pygame.draw.rect(self.screen, self.healthColor, (self.position[0], self.position[1],
                                                             self.currentHealth + self.postDamageCounter, 
                                                             self.height))

            pygame.draw.rect(self.screen,  self.damageColor, (self.position[0], self.position[1], self.currentHealth, self.height))

            self.postDamageCounter -= 1

            if (self.postDamageCounter == 0):
                self.healthDownCounter = 60
                self.postDamageCounter = 60
                self.damageTaken = False

        elif self.damageTaken == False:
            pygame.draw.rect(self.screen, self.backGroundColor, (self.position[0], self.position[1], self.maxHealth, self.height))
            pygame.draw.rect(self.screen, self.healthColor, (self.position[0], self.position[1], self.currentHealth, self.height))

    