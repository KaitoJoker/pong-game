import pygame
import sys
from pygame.math import Vector2
import random




def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, comp_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()
    if ball.bottom >= height:
        comp_score += 1
        score_time = pygame.time.get_ticks()
    if ball.left <= 0 or ball.right >= width:
        ball_speed_x *= -1
    if ball.colliderect(tembokkanan) or ball.colliderect(tembokKiri):
        ball_speed_x *= -1
    if ball.colliderect(player1) or ball.colliderect(comp):
        ball_speed_y *= -1

def player1_animation():
    player1.x += speed
    if player1.right >= width-size:
        player1.right = width-size
    if player1.left <= size:
        player1.left = size

def comp_animation():
    if comp.right < ball.x:
        comp.right += comp_speed
    if comp.left > ball.x:
        comp.left -= comp_speed
    if comp.right >= width-size:
        comp.right = width-size
    if comp.left <= size:
        comp.left = size

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time
    current_time = pygame.time.get_ticks()
    ball.center = (width/2+size, height/2)

    if current_time - score_time < 500:
        number3 = font.render("3",False,(200,200,200))
        screen.blit(number3,(width/2+size,height/2+size))
    if 500 < current_time - score_time < 1000:
        number2 = font.render("2",False,(200,200,200))
        screen.blit(number2,(width/2+size,height/2+size))
    if 1000 < current_time - score_time < 1500:
        number1 = font.render("1",False,(200,200,200))
        screen.blit(number1,(width/2+size,height/2+size))

    if current_time - score_time < 1500:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 5 * random.choice((1,-1))
        ball_speed_x = 2 * random.choice((1,-1))
        score_time = None

pygame.init()
ball_speed_x = 5 * random.choice((1,-1))
ball_speed_y = 3 * random.choice((1,-1))
speed = 0
comp_speed = 6
size = 10
number = 30
height = 600
width = 600
player_score = 0
comp_score = 0
font = pygame.font.Font(None,32)
score_time = True

ball = pygame.Rect(width/2, height/2, size,size)
tembokkanan = pygame.Rect(int(width-size),0,size,height)
player1 = pygame.Rect(width-400,height-size,100,size)
comp = pygame.Rect(width-400,0,100,size)
tembokKiri = pygame.Rect(1,0,size,height)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ping-Pong")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed += 10
            if event.key == pygame.K_LEFT:
                speed -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                speed -= 10
            if event.key == pygame.K_LEFT:
                speed += 10

    ball_animation()
    player1_animation()
    comp_animation()

    screen.fill((0,0,0))
    if score_time:
        ball_restart()
    pygame.draw.rect(screen,(255,255,255),tembokkanan)
    pygame.draw.rect(screen,(255,255,255),tembokKiri)
    pygame.draw.rect(screen,(255,255,255),player1)
    pygame.draw.rect(screen,(255,255,255),comp)
    pygame.draw.ellipse(screen,(255,255,255),ball)
    player_teks = font.render(f"Player:{player_score}",False,(255,255,255))
    screen.blit(player_teks,(width-120, height-20))
    comp_teks = font.render(f"Computer:{comp_score}",False,(255,255,255))
    screen.blit(comp_teks,(size,0))
    pygame.display.flip()
    clock.tick(60)