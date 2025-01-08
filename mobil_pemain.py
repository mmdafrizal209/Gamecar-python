import pygame
import random
import sys

# Inisialisasi pygame
pygame.init()

# Ukuran layar
lebar_layar = 400
tinggi_layar = 600
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption('Game Balap Mobil')

# Warna
hitam = (0, 0, 0)
putih = (255, 255, 255)
merah = (255, 0, 0)
hijau = (0, 255, 0)

# Memuat gambar mobil
mobil_pemain_image = pygame.image.load("mobil_pemain.png")  # Pastikan gambar ini ada di direktori
mobil_pemain_image = pygame.transform.scale(mobil_pemain_image, (50, 100))

mobil_musuh_image = pygame.image.load("mobil_musuh.png")  # Pastikan gambar ini ada di direktori
mobil_musuh_image = pygame.transform.scale(mobil_musuh_image, (50, 100))

# Mobil pemain
mobil_pemain = pygame.Rect(lebar_layar // 2 - 25, tinggi_layar - 100, 50, 100)

# Rintangan
rintangan_width = 50
rintangan_height = 50
rintangan_speed = 5
rintangan_list = []

# Musuh
mobil_musuh_width = 50
mobil_musuh_height = 100
mobil_musuh_speed = 5
mobil_musuh = pygame.Rect(random.randint(0, lebar_layar - mobil_musuh_width), -mobil_musuh_height, mobil_musuh_width, mobil_musuh_height)

# Skor
skor = 0
font = pygame.font.Font(None, 36)

# Level
level = 1
kecepatan_tambah = 0.1  # Kecepatan bertambah setiap level

# Loop utama game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Kontrol mobil pemain
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and mobil_pemain.left > 0:
        mobil_pemain.x -= 5
    if keys[pygame.K_RIGHT] and mobil_pemain.right < lebar_layar:
        mobil_pemain.x += 5

    # Gerakan mobil musuh
    mobil_musuh.y += mobil_musuh_speed
    if mobil_musuh.top > tinggi_layar:
        mobil_musuh.x = random.randint(0, lebar_layar - mobil_musuh_width)
        mobil_musuh.y = -mobil_musuh_height
        skor += 1  # Tambah skor saat mobil musuh melewati
        if skor % 5 == 0:  # Setiap 5 skor, tambah level dan kecepatan
            level += 1
            mobil_musuh_speed += kecepatan_tambah

    # Rintangan baru muncul secara acak
    if random.random() < 0.02:  # 2% kemungkinan untuk menambah rintangan setiap frame
        rintangan_x = random.randint(0, lebar_layar - rintangan_width)
        rintangan_y = -rintangan_height
        rintangan_list.append(pygame.Rect(rintangan_x, rintangan_y, rintangan_width, rintangan_height))

    # Pergerakan rintangan
    for rintangan in rintangan_list:
        rintangan.y += rintangan_speed
        if rintangan.top > tinggi_layar:
            rintangan_list.remove(rintangan)

    # Tabrakan dengan rintangan
    for rintangan in rintangan_list:
        if mobil_pemain.colliderect(rintangan):
            print("Game Over! Skor Anda:", skor)
            pygame.quit()
            sys.exit()

    # Tabrakan dengan mobil musuh
    if mobil_pemain.colliderect(mobil_musuh):
        print("Game Over! Skor Anda:", skor)
        pygame.quit()
        sys.exit()

    # Gambar objek
    layar.fill(hitam)
    layar.blit(mobil_pemain_image, mobil_pemain)  # Gambar mobil pemain
    layar.blit(mobil_musuh_image, mobil_musuh)    # Gambar mobil musuh

    # Gambar rintangan
    for rintangan in rintangan_list:
        pygame.draw.rect(layar, merah, rintangan)

    # Tampilkan skor dan level
    skor_text = font.render(f"Skor: {skor}", True, putih)
    level_text = font.render(f"Level: {level}", True, putih)
    layar.blit(skor_text, (10, 10))
    layar.blit(level_text, (10, 50))

    pygame.display.flip()
    pygame.time.delay(30)
