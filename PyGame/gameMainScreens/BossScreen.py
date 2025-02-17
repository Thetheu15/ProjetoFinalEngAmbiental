from Elements.Button import Button
from Elements.Screen import Screen
from Elements.Text   import Text
from Elements.Audio  import Audio
from Elements.Image  import Image
from Elements.HealthBar import HealthBar
import pygame
import time

class BossScreen:
    def __init__(self, width=500, height=500, background_color=(200,100,50)):
        self.background_color = background_color

        self.mainScreen    = Screen(width, height, background_color)

        self.bossHealthBar = HealthBar(self.mainScreen.screen, (1070,75), 300)
        self.boss          = Image('Sprites/bossAnim1.png',
                                   position          = (1050,100), 
                                   spriteRows        = 2, 
                                   spriteColumns     = 2,
                                   animationSlowness = 20)
        self.boss.scale((700,700))

        self.dialogBox   = Image('Images/dialogBox.png', (500,30))

        self.bossMessage = Text((530,70), '', 25, color=(0,0,0), speed=0.01, max_chars_per_line=50)

        self.winMessage  = Text((390,70), '''Parabêns você derrotou o mostro do lixo! Aqui o problema se resolveu, 
                                              mas ainda a muito a ser feito no mundo real!!!''', 
                                 font_size=50, speed=0.03, max_chars_per_line=50)
        
        self.loseMessage = Text((390,70), '''Você foi derrotado e agora o mundo foi tomado pelo mostro do lixo!''', 
                                 font_size=50, speed=0.03, max_chars_per_line=50)

        self.textOption1 = Text((50,620), '', color=(255,255,255), font_size=35, speed=0.02, max_chars_per_line=60)
        self.textOption2 = Text((50,770), '', color=(255,255,255), font_size=35, speed=0.02, max_chars_per_line=55)
        self.textOption3 = Text((850,620), '', color=(255,255,255), font_size=35, speed=0.02, max_chars_per_line=60)
        self.textOption4 = Text((850,770), '', color=(255,255,255), font_size=35, speed=0.02, max_chars_per_line=60)

        self.playerHealthBar = HealthBar(self.mainScreen.screen, (158,185), 300)
        self.player          = Image('Images/playerBack.png', (150, 225))
        self.player.scale((300,300))

        self.playerWinPose = Image('Images/playerVenceu.png', (600,300))
        self.bossWinPose   = Image('Images/bossVenceu.png', (540,300))
 
        self.hitAnim = Image('Sprites/hit1.png',
                              position          = (700,-250), 
                              spriteRows        = 4, 
                              spriteColumns     = 4,
                              animationSlowness = 6)
        self.hitAnim1 = Image('Sprites/hit2.png',
                              position          = (-160,-100), 
                              spriteRows        = 4, 
                              spriteColumns     = 4,
                              animationSlowness = 6)
        
        self.start   = Button(self.mainScreen.screen, (200, 675), 400, 150, "Desafiar!", font_size=80) 
        self.run     = Button(self.mainScreen.screen, (1000, 675), 400, 150, "Desafiar!", font_size=80)
        self.battle  = Button(self.mainScreen.screen, (200,675), 1200, 150, "", font_size=80)
        self.option1 = Button(self.mainScreen.screen, (0,600), 800, 150, "text")
        self.option2 = Button(self.mainScreen.screen, (0,750), 800, 150, "text")
        self.option3 = Button(self.mainScreen.screen, (800,600), 800, 150, "text")
        self.option4 = Button(self.mainScreen.screen, (800,750), 800, 150, "text")

        self.backgroundMusic = Audio('Audios/musicBack.wav')
        self.backgroundMusic.play(loop=True)

        self.hitAnim_trigger = False 
        self.hitAnim1_trigger = False

        self.countFrame = 0
        self.countFrame1 = 0
        self.oldTime = 0
        
        self.subScreenState = 0
        self.runInteraction = False

        self.bossDied = False

    def draw(self):
        self.mainScreen.draw_background()
        
        # pygame.draw.line(self.mainScreen.screen, (0, 255, 0), (0, 600), (1600, 600), 1)
        # pygame.draw.line(self.mainScreen.screen, (255, 255, 255), (800, 0), (800, 900), 1)
        # pygame.draw.line(self.mainScreen.screen, (255, 255, 255), (0, 450), (1600, 450), 1)

        if (self.subScreenState == 0):
            self.drawFloor()

            self.drawStartChoiceOptions()

            self.boss.doAnimation(self.mainScreen.screen)
            self.player.draw(self.mainScreen.screen)
            self.drawEntitysHealthBars()


            if (self.runInteraction == True):
                self.drawDialogBox('Você pensou que poderia fugir de mim?? HA HA HA HA HA! HOJE É O SEU FIM!!')

                if (time.time() - self.oldTime > 5):
                    self.oldTime = time.time()
                    self.runInteraction = False

        elif (self.subScreenState == 1):
            self.drawFloor()
            self.drawDialogBox('''Então um embate teremos! Só poderá me derrotar se minhas perguntas corretamente responder!
                                  Se não você perecessá junto com o resto da humanidade!!, mas não pense que terá muito tempo para pensar...
                                  HA HA HA HA''')
            
            self.drawBeginBattle()

            self.boss.doAnimation(self.mainScreen.screen)
            self.player.draw(self.mainScreen.screen)
            self.drawEntitysHealthBars()
           
        elif (self.subScreenState == 2):
            self.drawFloor()
            self.drawDialogBox('''Tendo em vista as possíveis formas de contaminação por lixo eletrônico, na água, no solo e no ar. Qual é a alternativa mais certa?''')

            self.drawOptions(truthTable=(False,False,False,True),
                             textOption1='''A poluição na água, decorrente dos descarte de eletrônicos, se dá quando os metais pesados são depositados no meio líquido.
                                            Assim sendo, essa poluição está entre as principais responsáveis pela morte dos peixes nesse ambiente aquático.''',
                             textOption2='''A poluição do ar se caracteriza como a mais perigosa para os seres humanos, uma vez que grandes áreas podem ser afetadas, 
                                            a partir da queima não controlada de resíduos eletrônicos, o que libera poluentes como óxidos de mercúrio e chumbo.''',
                             textOption3='''A poluição do solo se dá, sobretudo, pelo acúmulo de resíduos eletrônicos que demoram décadas para se degradar.''',
                             textOption4='''A poluição da água causa mais impacto para as populações humanas, uma vez que os contaminantes podem ser distribuidos pelos
                                            lençois freáticos e cadeia alimentar.''')
                        

            self.boss.doAnimation(self.mainScreen.screen)
            self.player.draw(self.mainScreen.screen)

            self.drawEntitysHealthBars()

            self.doHitAnimation()
            self.doHitAnimation1()

        elif (self.subScreenState == 3):
            self.drawFloor()
            self.drawDialogBox('''O descarte inadequado de resíduos eletrônicos pode causar contaminação ambiental e desperdício de recursos valiosos. 
                               Diante desse desafio, qual das seguintes práticas representa a abordagem mais eficaz para mitigar esses impactos de forma 
                               sustentável e economicamente viável?''')

            self.drawOptions(truthTable=(False,True,False,False),
                             textOption1='''Implementar políticas de incentivo ao descarte de eletrônicos em aterros sanitários controlados, 
                                            minimizando a dispersão de substâncias tóxicas no meio ambiente.''',
                             textOption2='''Desenvolver e fortalecer sistemas de logística reversa, viabilizando a recuperação e o reaproveitamento de materiais.''',
                             textOption3='''Estabelecer restrições severas à produção de novos dispositivos eletrônicos, 
                                            reduzindo a disponibilidade de produtos no mercado e, consequentemente, a geração de resíduos.''',
                             textOption4='''Priorizar a incineração dos resíduos eletrônicos como solução paliativa, 
                                            pois a queima controlada neutraliza completamente os metais pesados e impede a contaminação do solo e da água.''')
                        

            self.boss.doAnimation(self.mainScreen.screen)
            self.player.draw(self.mainScreen.screen)

            self.drawEntitysHealthBars()

            self.doHitAnimation()
            self.doHitAnimation1()

        elif (self.subScreenState == 4):
            self.drawFloor()
            self.drawDialogBox('''O que é o(a) PNRS?''')

            self.drawOptions(truthTable=(True,False,False,False),
                             textOption1='Política Nacional de Resíduos Sólidos, que estabelece a responsabilidade compartilhada pelo ciclo de vida dos produtos.',
                             textOption2='''Produto Não Reciclável Salubre, classificação de um produto que não pode ser reciclado e que pode ser descartado normalmente
                                            pois nao apresenta nenhuma insalubridade ao ser humano.''',
                             textOption3='Baseado na lei federal nº 12.505/2015, estabelece as diretrizes que determinam que todos os produtos domésticos devem ser reciclados.',
                             textOption4='Nome do posto que é apropriado para o descarte de REEE (Resíduos de Equipamentos Elétricos e Eletrônicos).')
                        

            self.boss.doAnimation(self.mainScreen.screen)
            self.player.draw(self.mainScreen.screen)

            self.drawEntitysHealthBars()

            self.doHitAnimation()
            self.doHitAnimation1()

        elif (self.subScreenState == 5):
            self.drawFloor()
            self.drawDialogBox('''O Decreto nº 10.240/2020 estabelece regras para a logística reversa de eletroeletrônicos. 
                               Qual é o objetivo principal dessa regulamentação? ''')

            self.drawOptions(truthTable=(False,False,False,True),
                             textOption1='Incentivar o descarte regular de eletrônicos.',
                             textOption2='Responsabilizar os consumidores pelo tratamento dos resíduos.',
                             textOption3='Proibir a fabricação de eletroeletrônicos no Brasil.',
                             textOption4='Estruturar um sistema para a destinação ambientalmente adequada de produtos eletroeletrônicos pós-consumo.')
                        

            self.boss.doAnimation(self.mainScreen.screen)
            self.player.draw(self.mainScreen.screen)

            self.drawEntitysHealthBars()

            self.doHitAnimation()
            self.doHitAnimation1()

        elif (self.subScreenState == 6):
            self.drawFloor()
            self.drawDialogBox('''De acordo com a Política Nacional de Resíduos Sólidos no Brasil, 
                                  qual é a responsabilidade das empresas em relação ao descarte do lixo eletrônico? ''')

            self.drawOptions(truthTable=(False,False,True,False),
                             textOption1='Nenhuma, pois o consumidor deve se responsabilizar pelo descarte.',
                             textOption2='Apenas incentivar o uso prolongado dos eletrônicos, sendo o gerenciamento dos resíduos optativo.',
                             textOption3='Implementar a logística reversa, garantindo que os produtos descartados sejam corretamente reciclados ou reutilizados.',
                             textOption4='Reduzir a produção de eletrônicos para mitigar o acúmulo de resíduos.')
                        

            self.boss.doAnimation(self.mainScreen.screen)
            self.player.draw(self.mainScreen.screen)

            self.drawEntitysHealthBars()

            self.doHitAnimation()
            self.doHitAnimation1()

        elif (self.subScreenState == 7):
            self.drawFloor()
                        
            self.boss.doAnimation(self.mainScreen.screen)
            self.player.draw(self.mainScreen.screen)

            self.drawEntitysHealthBars()

            self.doHitAnimation()
            self.doHitAnimation1()

        if (self.checkIfBossDead() and (time.time() - self.oldTime < 3.05)):
            self.drawFloor()

            self.boss.fadeImageAnimation(self.mainScreen.screen, 5, is_animation=True)
            self.player.draw(self.mainScreen.screen)
            
            self.drawEntitysHealthBars()

            self.subScreenState = 100
        
        if (self.checkIfPlayerDead() and (time.time() - self.oldTime < 3.05)):
            self.drawFloor()

            self.player.fadeImageAnimation(self.mainScreen.screen, 5, is_animation=False)
            self.boss.doAnimation(self.mainScreen.screen)
            
            self.drawEntitysHealthBars()

            self.subScreenState = 101

        if (self.subScreenState == 100 and (time.time() - self.oldTime > 3.05)):
            self.drawPlayerWinSubScreen()
        if (self.subScreenState == 101 and (time.time() - self.oldTime > 3.05)):
            self.drawPlayerLoseSubScreen()
           
    def handleEvent(self, event):
        if (self.start.is_clicked(event) and self.subScreenState == 0):
            self.subScreenState += 1
            self.bossMessage.resetText()

        elif (self.run.is_clicked(event) and self.subScreenState == 0):
            self.runInteraction = True
            self.oldTime = time.time()
        
        elif (self.battle.is_clicked(event) and self.subScreenState == 1):
            self.subScreenState += 1
            self.bossMessage.resetText()
            self.oldTime = time.time()

        if self.option1.is_clicked(event) :
            if (self.option1.isCorrectAnswer == True):
                self.hitAnim_trigger = True

                self.bossHealthBar.doDamage()

                self.oldTime = time.time()

                self.subScreenState += 1
                self.textOption1.resetText()
                self.textOption2.resetText()
                self.textOption3.resetText()
                self.textOption4.resetText()
                self.bossMessage.resetText()

            elif (self.subScreenState > 1 and time.time() - self.oldTime > 1):
                self.hitAnim1_trigger = True

                self.playerHealthBar.doDamage()

                self.oldTime = time.time()
                
                self.subScreenState += 1
                self.textOption1.resetText()
                self.textOption2.resetText()
                self.textOption3.resetText()
                self.textOption4.resetText()
                self.bossMessage.resetText()

        if (self.option2.is_clicked(event) and self.subScreenState >= 2):
            if (self.option2.isCorrectAnswer == True):
                self.hitAnim_trigger = True

                self.bossHealthBar.doDamage()
                
                self.oldTime = time.time()

                self.subScreenState += 1
                self.textOption1.resetText()
                self.textOption2.resetText()
                self.textOption3.resetText()
                self.textOption4.resetText()
                self.bossMessage.resetText()

            elif (self.subScreenState > 1 and time.time() - self.oldTime > 1):
                self.hitAnim1_trigger = True

                self.playerHealthBar.doDamage()

                self.oldTime = time.time()

                self.subScreenState += 1
                self.textOption1.resetText()
                self.textOption2.resetText()
                self.textOption3.resetText()
                self.textOption4.resetText()
                self.bossMessage.resetText()

        if self.option3.is_clicked(event):
            if (self.option3.isCorrectAnswer == True):
                self.hitAnim_trigger = True

                self.bossHealthBar.doDamage()
                
                self.oldTime = time.time()

                self.subScreenState += 1
                self.textOption1.resetText()
                self.textOption2.resetText()
                self.textOption3.resetText()
                self.textOption4.resetText()
                self.bossMessage.resetText()

            elif (self.subScreenState > 1 and time.time() - self.oldTime > 1):
                self.hitAnim1_trigger = True

                self.playerHealthBar.doDamage()

                self.oldTime = time.time()

                self.subScreenState += 1
                self.textOption1.resetText()
                self.textOption2.resetText()
                self.textOption3.resetText()
                self.textOption4.resetText()
                self.bossMessage.resetText()

        if self.option4.is_clicked(event):
            if (self.option4.isCorrectAnswer == True):
                self.hitAnim_trigger = True

                self.bossHealthBar.doDamage()
                
                self.oldTime = time.time()

                self.subScreenState += 1
                self.textOption1.resetText()
                self.textOption2.resetText()
                self.textOption3.resetText()
                self.textOption4.resetText()
                self.bossMessage.resetText()

            elif (self.subScreenState > 1 and time.time() - self.oldTime > 1):
                self.hitAnim1_trigger = True

                self.playerHealthBar.doDamage()

                self.oldTime = time.time()

                self.subScreenState += 1
                self.textOption1.resetText()
                self.textOption2.resetText()
                self.textOption3.resetText()
                self.textOption4.resetText()
                self.bossMessage.resetText()

    def drawFloor(self):
        pygame.draw.ellipse(self.mainScreen.screen, (0, 0, 0), (1010, 400, 400, 100)) # Chão sobre o boss
        pygame.draw.ellipse(self.mainScreen.screen, (0, 0, 0), (120, 500, 350, 100))  # Chão sobre o player

    def drawDialogBox(self, text=''):
        pygame.draw.rect(self.mainScreen.screen,   (255,255,255), (512, 50, 473, 160))
        pygame.draw.circle(self.mainScreen.screen, (62, 61, 130),   (1150,200), 10)
        pygame.draw.circle(self.mainScreen.screen, (255, 255, 255), (1150,200), 5)
        pygame.draw.circle(self.mainScreen.screen, (62, 61, 130),   (1105,200), 15)
        pygame.draw.circle(self.mainScreen.screen, (255, 255, 255), (1105,200), 7.5)
        pygame.draw.circle(self.mainScreen.screen, (62, 61, 130),   (1050,200), 20)
        pygame.draw.circle(self.mainScreen.screen, (255, 255, 255), (1050,200), 10)
        self.bossMessage.changeText(text)
        self.bossMessage.draw(self.mainScreen.screen)
        self.dialogBox.draw(self.mainScreen.screen)

    def drawBeginBattle(self, textBeginBattle= 'Acho que não tenho escolha, pelo futuro!!!'):
        self.battle.draw(textBeginBattle)

    def drawStartChoiceOptions(self, startText='Desafiar!', runText='Fugir!'):
        self.start.draw(startText)
        self.run.draw(runText)

    def drawOptions(self, truthTable, textOption1='', textOption2='', textOption3='', textOption4=''):
        self.option1.draw()
        self.textOption1.changeText(textOption1)
        self.textOption1.draw(self.mainScreen.screen)
        self.option1.changeCorrectAnswerState(truthTable[0])

        self.option2.draw()
        self.textOption2.changeText(textOption2)
        self.textOption2.draw(self.mainScreen.screen)
        self.option2.changeCorrectAnswerState(truthTable[1])

        self.option3.draw()
        self.textOption3.changeText(textOption3)
        self.textOption3.draw(self.mainScreen.screen)
        self.option3.changeCorrectAnswerState(truthTable[2])

        self.option4.draw()
        self.textOption4.changeText(textOption4)
        self.textOption4.draw(self.mainScreen.screen)
        self.option4.changeCorrectAnswerState(truthTable[3])

    def drawEntitysHealthBars(self):
        self.bossHealthBar.draw()
        self.playerHealthBar.draw()
    
    def checkIfBossDead(self):
        if (self.bossHealthBar.currentHealth <= 1): return True
        else:                                       return False     
    def checkIfPlayerDead(self):
        if (self.playerHealthBar.currentHealth <= 1): return True
        else:                                         return False    

    def doHitAnimation(self):
        if self.hitAnim_trigger and self.countFrame <= self.hitAnim.totalNumFrames: 
            self.hitAnim.doAnimation(self.mainScreen.screen) 
            self.countFrame += 1
        else:
            self.hitAnim_trigger = False
            self.countFrame = 0
            self.hitAnim.resetAnimation()   
    def doHitAnimation1(self):
        if self.hitAnim1_trigger and self.countFrame1 <= self.hitAnim1.totalNumFrames: 
            self.hitAnim1.doAnimation(self.mainScreen.screen) 
            self.countFrame1 += 1
        else:
            self.hitAnim1_trigger = False
            self.countFrame1 = 0
            self.hitAnim1.resetAnimation()

    def drawPlayerWinSubScreen(self):
        pygame.draw.rect(self.mainScreen.screen,   (255,255,255), (380, 50, 830, 160))
        self.winMessage.draw(self.mainScreen.screen)
        self.playerWinPose.draw(self.mainScreen.screen)

    def drawPlayerLoseSubScreen(self):
        pygame.draw.rect(self.mainScreen.screen,   (255,255,255), (380, 50, 830, 160))
        self.loseMessage.draw(self.mainScreen.screen)
        self.bossWinPose.draw(self.mainScreen.screen)