# RGB color https://www.rapidtables.com/web/color/RGB_Color.html
import pygame
import time
import os
def button():
   pass

    #return butnX, butnY

def main():
    pygame.init()


    num = 0
    screen = pygame.display.set_mode((620,480))
    # button schtuff
    butnX = 200
    butnY = 100
    butnWdth = 150
    butnHeit = 125
    font = pygame.font.SysFont('Georgia', 22, bold='True')  # name size bold ital
    btnTxt = font.render('Start', True, 'white')
    button = pygame.Rect(butnX, butnY, butnWdth, butnHeit)  ##rect(surface, color, rect) -> Rect
    btn_activ = 0

    menuLoop = True  # Conditional sentinel to run pygame loop
    while menuLoop:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill((133, 112, 218))




        for event in pygame.event.get():
            if pygame.Rect.collidepoint(button, (mouse_pos)): #mouse and edge of button collision detected...
                #open PRNG.txt and write run
                file = open("PRNG.txt", mode='w');
                file.write("run") #write run to PRNG.txt
                file.flush()
                file.close()      #stop file instance so it isn't manipulated again

            #3. UI reads prng-service.txt to get the pseudo-random number
            #read PRNG.txt and get the number to write down in img-srv.txt
            with open('PRNG.txt') as f:
                lines = f.readlines() #lines is a list
                f.flush()
            f.close()

            #4. UI writes the pseudo-random number to image-service.txt
            file1 = open("image-service.txt", mode='w');  #open file back up
            if len(lines) > 0: #dont want to check index of lines before it contains anything!
                randNum = lines[0]
                print("num read is ", randNum )
                #file1.flush()
                file1.write(str(randNum)) #write the num PRNG.py generated into img.serv.txt
                file1.close()

            if event.type == pygame.QUIT:
                menuLoop = False


            #    _________ draw button _________
            #if (mouse_pos[0] <= butnX or mouse_pos[0] >= butnX +butnWdth) and (mouse_pos[1] <= butnY or mouse_pos[1] >= butnY +butnHeit):
            #if mouse_pos[0] <= butnX <= mouse_pos[0] + butnX + butnWdth and mouse_pos[1] <= butnY <= mouse_pos[1] + butnHeit:

            if butnX <=  mouse_pos[0] <= (butnX + butnWdth) and butnY <=  mouse_pos[1] <= (butnY + butnHeit) :
                pygame.draw.rect(screen, (17, 47, 227), button)
                print("!!!!!!!!!!!!!!!!!!!!!!!")
                # blit: draws a source Surface onto this Surface.
                screen.blit(btnTxt, (butnX + 10, butnY + 10))  # blit(source, dest, area=None, special_flags=0) -> Rect
                pygame.display.flip()
            else:
                pygame.draw.rect(screen, (127, 127, 127), button)
                # blit: draws a source Surface onto this Surface.
                screen.blit(btnTxt, (butnX + 10, butnY + 10))  # blit(source, dest, area=None, special_flags=0) -> Rect
                pygame.display.flip()
pygame.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
