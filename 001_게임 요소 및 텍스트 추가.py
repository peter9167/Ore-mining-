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

배경이미지 = pg.image.load('img/배경.png')
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이))

시간이미지 = pg.image.load('img/시간바.png')
시간이미지크기 = (337, 89)
시간이미지 = pg.transform.scale(시간이미지, 시간이미지크기)

코인이미지 = pg.image.load('img/코인바.png')
코인이미지크기 = (337, 89)
코인이미지 = pg.transform.scale(코인이미지, 코인이미지크기)

게임요소크기 = (152, 152)
소울곰이미지딕셔너리 = {"이동": [], "반대이동" : [], "캐기" : []}
소울곰멈춤이미지 = pg.image.load(f'img/소울곰_멈춘상태.png')
소울곰멈춤이미지 = pg.transform.scale(소울곰멈춤이미지, 게임요소크기)
소울곰이미지딕셔너리["멈춤"] = 소울곰멈춤이미지

for 인덱스 in range(4):
    소울곰뛰는모습이미지 = pg.image.load(f'img/소울곰_뛰는모습_{인덱스 + 1}.png')
    소울곰뛰는모습이미지 = pg.transform.scale(소울곰뛰는모습이미지, 게임요소크기)
    소울곰이미지딕셔너리["이동"].append(소울곰뛰는모습이미지)

    소울곰뛰는모습반전이미지 = pg.image.load(f'img/소울곰_뛰는모습_반전_{인덱스 + 1}.png')
    소울곰뛰는모습반전이미지 = pg.transform.scale(소울곰뛰는모습이미지, 게임요소크기)
    소울곰이미지딕셔너리["반대이동"].append(소울곰뛰는모습이미지)

for 인덱스 in range(3):
    소울곰캐는모습이미지 = pg.image.load(f'img/소울곰_캐는모습_{인덱스 + 1}.png')
    소울곰뛰는모습이미지 = pg.transform.scale(소울곰캐는모습이미지, 게임요소크기)
    소울곰이미지딕셔너리["캐기"].append(소울곰캐는모습이미지)

소울곰이미지상태 = "멈춤"
소울곰이미지인덱스 = 0
소울곰이미지흐름 = 1
소울곰스프라이트 = 스프라이트생성(소울곰이미지딕셔너리[소울곰이미지상태], 소울곰위치)

광석이미지리스트 = []
for 인덱스 in range(5):
    광석이미지 = pg.image.load(f'img/광석_{5 - 인덱스}.png')
    광석이미지 = pg.transform.scale(광석이미지, 게임요소크기)
    광석이미지리스트.append(광석이미지)
광석스프라이트리스트 = []
광석스프라이트리스트.append(스프라이트생성(광석이미지리스트[-1], (200, 200), 광석최대상태))

#오른쪽 하단 능력치 아이콘 이미지
능력치이미지 = pg.image.load('img/능력치.png')
능력치이미지크기 = (545, 190)
능력치이미지 = pg.transform.scale(능력치이미지, 능력치이미지크기)

시계 = pg.time.Clock()

while 실행여부:
    화면.blit(배경이미지, (0, 0))

    흐른시간 = 시계.tick(60) / 1000
    전체시간 += 흐른시간
    시간문자열 = '%02d:%05.2f' % (전체시간 / 60, 전체시간 % 60)
    게임시작시간글자 = 글꼴.render(시간문자열, True, 검은색)
    화면.blit(시간이미지, (30, 10))
    화면.blit(게임시작시간글자, (시간이미지크기[0] - 21 * len(시간문자열), 40))

    코인문자열 = str(코인)
    코인글자 = 글꼴.render(코인문자열, True, 검은색)
    화면.blit(코인이미지, (화면가로길이 - 30 - 코인이미지크기[0], 10))
    화면.blit(코인글자, (화면가로길이 - 70 - 21 * len(코인문자열), 40))

    for 광석_스프라이트 in 광석스프라이트리스트:
        화면.blit(광석_스프라이트.image, 광석_스프라이트.rect)

    소울곰스프라이트.rect.x, 소울곰스프라이트.rect.y = 소울곰위치[0], 소울곰위치[1]
    화면.blit(소울곰스프라이트.image, 소울곰스프라이트.rect)

    화면.blit(능력치이미지, (화면가로길이 - 능력치이미지크기[0], 화면세로길이 - 능력치이미지크기[1]))
    파워글자 = 작은글꼴.render(str(1), True, 검은색)
    화면.blit(파워글자, (500, 화면세로길이 - 능력치이미지크기[1] + 55))
    속도글자 = 작은글꼴.render(str(1), True, 검은색)
    화면.blit(속도글자, (610, 화면세로길이 - 능력치이미지크기[1] + 55))
    광석글자 = 작은글꼴.render(str(1), True, 검은색)
    화면.blit(광석글자, (720, 화면세로길이 - 능력치이미지크기[1] + 55))

    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            실행여부 = False

    pg.display.update

pg.display.quit()