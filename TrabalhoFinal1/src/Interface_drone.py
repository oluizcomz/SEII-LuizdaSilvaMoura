#Augusto Perez de Andrade 11611EMT009
#Larrisa Teodoro da Silva 11321EMT021 
#Luiz da Silva Moura 11611EMT028
#Matheus Santana de Aráujo 11611EMT026
#Pedro Henrique Silva Oliveira 11611EMT007

import pygame, os # pygame para interface, os para navegar nos arquivos e ter acesso as imagens 
from Planta_drone import Planta # classe da planta
import numpy as np 

pygame.init()
t = 5 
planta = Planta(t/1000) # criando o objeto da planta_drone passando 
x = - 1
y = 6

#inportando as imagens de simulação 
background = pygame.image.load('./TrabalhoFinal1/images/background.jpg')
drone = pygame.image.load(os.path.join('./TrabalhoFinal1/images','drone.png'))
Width = 800
Height= 600

#redimencionando as imagens
background = pygame.transform.scale(background, (Width,Height))
drone = pygame.transform.scale(drone, (50, 17))

#taamanho da janela
window = pygame.display.set_mode((Width,Height))
#titulo
pygame.display.set_caption("UpDrone")
t = 1
window_open = True
ptp = 0
ptpantes = -1 
planta.SetToPoint(True)

# Waypoints
r_ = np.array([[0., 10.],
                    [15., 10.],
                    [-50., 2.],
                    [-20., 15.],
                    [0., 0.]])

while(window_open):#enquanto a janela nao fecha
    pygame.time.delay(t)# tempo para recarregar a tela

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open=False
    #eventos de click
    commands = pygame.key.get_pressed()
    if commands[pygame.K_UP]:
        y+=0.01
    if commands[pygame.K_DOWN]:
        y-=0.01
    if commands[pygame.K_RIGHT]:
        x+= 0.1
    if commands[pygame.K_LEFT]:
        x-=0.1
    if commands[pygame.K_SPACE]:# cada vez que da spce se ja estiver no ponto muda o ponto para os estabelecidos
        if planta.GetToPoint() == True:
            planta.SetToPoint(False)
            x = r_[ptp][0]
            y = r_[ptp][1]
            ptp = ptp + 1
            if ptp > 4:
                ptp = 0 
    #x, y e angulo cauculado
    x_cal,yc_cal,angle = planta.GsxCs(np.array([x,y]))
    x_reg = ((x_cal +55)/ 75)*800
    y_reg =  ((yc_cal -0.5 )/16.5)*600
    y_reg = Height - y_reg
    if(planta.GetToPoint() and ptp != ptpantes):
        ptpantes = ptp
        print('chegou no ponto: {}'.format(ptp))

    window.fill((0,0,0))
    window.blit(background,(0,0))
    dronemov = pygame.transform.rotate(drone, angle *  180/np.pi)
    window.blit(dronemov,(int(x_reg),int(y_reg)))

    pygame.display.update()
    
pygame.quit()