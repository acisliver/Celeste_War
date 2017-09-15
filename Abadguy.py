import pygame
import threading
import random
from Bullet import Bullet
from Timer import Timer

class Abadguy(pygame.Rect):
    speed=0
    screen = None
    bullets = []
    abadguy = pygame.image.load("resources/images/badguy.png")

    def __init__(self, screen, x, y, speed):
        super().__init__(self.abadguy.get_rect())     #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.top = x
        self.left = y
        self.speed = speed
        self.screen = screen

    def move(self):             #원거리몹 움직임 함수
        time=threading.Timer(1,self.move())  #1초마다 반복

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                time.cancel()               #1초마다 반복 취소

        time.start()                        #시작

        if self.count<=0:
            time.cancel()

        for bullet in self.bullets:
            bullet.move()



    def shot(self):                 #화살생성함수
        bullet = Bullet(self.screen, self.top, self.left, 30 )    #speed가 30인 화살 생성
        self.bullets.append(bullet)                               #list에 arrow객체 추가