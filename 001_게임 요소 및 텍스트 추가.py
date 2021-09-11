import pygame as pg

# 이미지 초기화
def 스프라이트생성(이미지, 위치, 상태=None):
    스프라이트 = pg.sprite.Sprite()
    스프라이트.image = 이미지
    스프라이트.rect = 스프라이트.image.get_rect()
    스프라이트.rect.x, 스프라이트.rect.y = 위치[0], 위치[1]
    if 상태 != None:
        스프라이트.상태 = 상태
    return 스프라이트

pg.init()

# 게임기본설정
실행여부 = True
화면가로길이, 화면세로길이 = 952, 913
화면 = pg.display.set_mode([화면가로길이, 화면세로길이])
pg.display.set_caption('광석채굴!')

# 색깔 설정
흰색 = (255, 255, 255)
검은색 = (0, 0, 0)

# 글꼴 설정
글꼴 = pg.font.SysFont('hy얕은샘물m', 50)
작은글꼴 = pg.font.SysFont('hy얕은샘물m', 40)

# 게임 요소 초기화
소울곰위치 = [화면가로길이 // 2, 화면세로길이 // 2]

광석최대상태 = 5

코인 = 0

전체시간 = 0

