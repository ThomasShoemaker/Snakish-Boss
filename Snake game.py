import pygame
import random
import time

pygame.init()
dis_width = 500
dis_height = 500
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()


def msg(message,colour,size,pos):
    font_style = pygame.font.SysFont(None, size, True)
    messge = font_style.render(message, True, colour)
    dis.blit(messge, pos)
gold=(255,223,0)
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
red=(255,0,0)
snake_block=20
snake_speed=20
pos=0
pygame.display.set_caption("SNAKE")

clock=pygame.time.Clock()
scores=[0]

def food():
    game_over = False
    game_close= False

    length=1
    x1 = random.randint(0, dis_width / 20) * 20
    y1 = random.randint(0, dis_height / 20) * 20
    x1_change = 0
    y1_change = 0
    fd=True
    pos=[[x1,y1]]
    while not game_over:
        if fd==True:
            while True:
                foodx = random.randint(0, (dis_width - snake_block) / 20) * 20
                foody = random.randint(0, (dis_height - snake_block) / 20) * 20
                if [foodx,foody] not in pos:
                    fd=False
                    opps=0
                    bruceybonus=False
                    break

        while game_close==True:
            print(scores)
            msg("YOU DIED",red,20,[10, 30])
            pygame.display.update()
            time.sleep(0.5)
            msg("Your score was: " + str(length),red,20,[10, 60])
            pygame.display.update()
            time.sleep(0.5)
            msg("Press ESC to quit or 'r' to play again",white,20,[10, 90])
            pygame.display.update()
            time.sleep(0.5)
            if length>max(scores):
                msg("Congratulations you have set a new high score!", gold, 20,[10, 120])
                scores.append(length)
            elif length==scores[-1]:
                pass
            else:
                msg("The high score is " + str(max(scores)) + " maybe you'll beat it next time",white,20,[10,120])

            pygame.display.update()
            time.sleep(0.5)


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_r:
                        food()
                        scores.append(length)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and pos[-1][0]!=x1-snake_speed:
                    x1_change = -snake_speed
                    y1_change= 0
                elif event.key==pygame.K_RIGHT and pos[-1][0]!=x1+snake_speed:
                    x1_change = snake_speed
                    y1_change=0
                elif event.key == pygame.K_UP and pos[-1][1]!=y1-snake_speed:
                    x1_change=0
                    y1_change = -snake_speed
                elif event.key == pygame.K_DOWN and pos[-1][1]!=y1+snake_speed:
                    x1_change=0
                    y1_change = snake_speed
                else:
                    print("Positions:", pos)
                    print("Snake length:", length)
                    print("Previous position: ", pos[-1][1])
                    print("Desired position: ", )
                    print(event)
                    print(x1,y1)
                    if event.key==pygame.K_q:
                        game_over=True
        if x1 > dis_width or x1<0 or y1<0 or y1>dis_height:
            game_close=True
        for i in range(length-1):
            if x1==pos[i][0] and y1==pos[i][1]:
                game_close=True
        if x1 == foodx and y1==foody:
            fd=True
            length+=1
            pos.append([x1,y1])
        prevpos=[x1,y1]
        x1 += x1_change
        y1 += y1_change
        for i in range(length-1):
            pos[-1]=prevpos
            pos[i]=pos[i+1]
        if random.randint(0,60)>59:
            bruceybonus=True
            while True:
                bbx = random.randint(0, (dis_width - snake_block) / 20) * 20
                bby = random.randint(0, (dis_height - snake_block) / 20) * 20
                if [bbx, bby] not in pos:
                    break

        dis.fill(black)

        if bruceybonus==True and opps<150:
            pygame.draw.rect(dis, gold, [bbx, bby, snake_block, snake_block])
            if x1 == bbx and y1 == bby:
                opps=0
                bruceybonus=False
                inc=int(random._exp(2))
                print(inc)

                if inc<length:
                    for i in range(inc):
                        pos.append([pos[-inc][0], pos[-inc][1]])
                else:
                    for i in range(inc):
                        pos.append([pos[0][0], pos[0][1]])
                length += inc
        opps+=1
        pygame.draw.rect(dis,blue,[foodx,foody,snake_block,snake_block])

        pygame.draw.rect(dis,white,[x1,y1,20,20])
        for i in range(length):
            pygame.draw.rect(dis, white, [pos[-i][0],pos[-i][1], 20, 20])
        msg("SCORE: " + str(length),white,20,[dis_width-90,20])
        msg("HIGH SCORE: " +str(max(scores)),gold,20, [dis_width-150,40])
        pygame.display.update()
        clock.tick(20)

    pygame.quit()
    quit()

food()