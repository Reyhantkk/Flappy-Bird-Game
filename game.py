import pygame
import random

pygame.init()


genislik, yukseklik = 400, 600
ekran = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption("Flappy Bird")

beyaz = (255, 255, 255)
mavi = (0, 0, 255)


kus_y = yukseklik // 2
kus_hiz = 0
yer_cekimi = 0.25
zemin = yukseklik - 70
oyun_devam = True
engeller = []
engel_genislik = 70
engel_aralik = 200
engel_hiz = -2
puan = 0
font = pygame.font.SysFont("Arial", 32)


def engel_olustur():
    engel_yukseklik = random.randint(150, 450)
    ust_engel = engel_yukseklik - engel_aralik // 2
    alt_engel = yukseklik - engel_yukseklik - engel_aralik // 2
    engeller.append([genislik, ust_engel, engel_genislik, alt_engel])


while oyun_devam:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oyun_devam = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                kus_hiz = -5


    kus_y += kus_hiz
    kus_hiz += yer_cekimi
    if kus_y > zemin:
        kus_y = zemin
        kus_hiz = 0

    
    if not engeller or engeller[-1][0] < genislik - 300:
        engel_olustur()
    for engel in engeller:
        engel[0] += engel_hiz
    
        if kus_y < engel[1] or kus_y > engel[1] + engel_aralik:
            if engel[0] <= 50 + 25 and engel[0] + engel_genislik >= 50:
                oyun_devam = False
        if engel[0] + engel_genislik < 0:
            engeller.remove(engel)
            puan += 1



  
    ekran.fill(beyaz)

    
    for engel in engeller:
        pygame.draw.rect(ekran, mavi, (engel[0], 0, engel_genislik, engel[1]))
        pygame.draw.rect(ekran, mavi, (engel[0], yukseklik - engel[3], engel_genislik, engel[3]))

    
    pygame.draw.circle(ekran, mavi, (50, kus_y), 25)

    
    puan_yazisi = font.render(f"Puan: {puan}", True, mavi)
    ekran.blit(puan_yazisi, (10, 10))

    pygame.display.update()
    pygame.time.Clock().tick(30)

pygame.quit()
