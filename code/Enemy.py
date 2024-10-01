#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.speed_y = ENTITY_SPEED[self.name] / 2  # Velocidade vertical inicial do Enemy3

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.name == 'Enemy3':
            self.rect.centery += self.speed_y
            if self.rect.bottom >= WIN_HEIGHT:  # Borda inferior da tela
                self.speed_y = -ENTITY_SPEED[self.name]  # Subindo com velocidade normal
            elif self.rect.top <= 0:  # Borda superior da tela
                self.speed_y = 2 * ENTITY_SPEED[self.name]  # Descendo com o dobro da velocidade
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
