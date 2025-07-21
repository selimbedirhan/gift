import turtle
import pygame
import threading
import time
import random

# 🎵 Müzik fonksiyonu
def muzikCal():
    pygame.mixer.init()
    pygame.mixer.music.load("muzik.mp3")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)

# Müzik başlat
threading.Thread(target=muzikCal, daemon=True).start()

# 🖥️ Tam ekran ve sahne ayarları
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("#5DADE2")  # gökyüzü mavisi (biraz daha koyu)

objeler = []

# 🌿 Alt çim alanı (ekranın altını tamamen kapla)
grass = turtle.Turtle()
grass.hideturtle()
objeler.append(grass)
grass.penup()
grass.goto(-screen.window_width()//2, -screen.window_height()//2)
grass.color("#32CD32")
grass.begin_fill()
grass.pendown()
grass.forward(screen.window_width())
grass.left(90)
grass.forward(300)
grass.left(90)
grass.forward(screen.window_width())
grass.left(90)
grass.forward(300)
grass.end_fill()

# ☀️ Güneş (sol üst)
sun = turtle.Turtle()
sun.hideturtle()
objeler.append(sun)
sun.penup()
sun.goto(-screen.window_width()//2 + 60, screen.window_height()//2 - 120)
sun.color("gold")
sun.begin_fill()
sun.circle(50)
sun.end_fill()

# 🌱 Sap
stem = turtle.Turtle()
stem.hideturtle()
objeler.append(stem)
stem.color("green")
stem.pensize(10)
stem.penup()
stem.goto(0, -50)
stem.setheading(-90)
stem.pendown()
stem.forward(100)

# 🌼 Papatya yaprakları
flower = turtle.Turtle()
flower.speed(0)
flower.hideturtle()
objeler.append(flower)

def yaprak():
    flower.color("white")
    flower.begin_fill()
    flower.circle(30, 60)
    flower.left(120)
    flower.circle(30, 60)
    flower.left(120)
    flower.end_fill()

flower.penup()
flower.goto(0, 0)
flower.setheading(90)
for i in range(12):
    flower.penup()
    flower.goto(0, 0)
    flower.setheading(i * 30)
    flower.forward(40)
    flower.pendown()
    yaprak()

# 🌕 Orta sarı kısım
center = turtle.Turtle()
center.hideturtle()
objeler.append(center)
center.penup()
center.goto(0, -42)
center.color("yellow")
center.begin_fill()
center.circle(40)
center.end_fill()

# 🍃 Yapraklar
leaf = turtle.Turtle()
leaf.hideturtle()
objeler.append(leaf)
leaf.color("darkgreen")
leaf.penup()
leaf.goto(0, -80)
leaf.setheading(-160)
leaf.begin_fill()
leaf.circle(20, 60)
leaf.left(120)
leaf.circle(20, 60)
leaf.end_fill()

leaf.penup()
leaf.goto(0, -120)
leaf.setheading(-20)
leaf.begin_fill()
leaf.circle(20, 60)
leaf.left(120)
leaf.circle(20, 60)
leaf.end_fill()

# 💬 Yavaş yazı efekti
def yaziyiYavasYaz(text):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(0, -screen.window_height()//2 + 160)  # yazıyı daha yukarı al
    writer.color("#0C344F")  # fuşya
    writer.speed(0)

    birikimli = ""
    for harf in text:
        birikimli += harf
        writer.clear()
        writer.write(birikimli, align="center", font=("Verdana", 28, "bold"))
        time.sleep(0.17)
    objeler.append(writer)

# ✍️ Yazı: Seni Seviyorum Zühre 💜😽
yaziyiYavasYaz("Seni Seviyorum Sevgilim 💜😽")

# 🎬 Sahneyi yavaş yavaş sil
time.sleep(2)

for obje in reversed(objeler):
    obje.clear()
    obje.hideturtle()
    time.sleep(0.4)

# 🎭 Siyah perde
screen.bgcolor("gray20")

# ---🌌 Yeni Sahne: Ay Üzerinden Dünya Manzarası---



# Yeni sahne ekranı



objeler2 = []

# 🪐 Zemin (ayın yüzeyi)
moon_ground = turtle.Turtle()
moon_ground.hideturtle()
objeler2.append(moon_ground)
moon_ground.penup()
moon_ground.goto(-screen.window_width()//2, -screen.window_height()//2)
moon_ground.color("gray")
moon_ground.begin_fill()
moon_ground.pendown()
moon_ground.forward(screen.window_width())
moon_ground.left(90)
moon_ground.forward(300)
moon_ground.left(90)
moon_ground.forward(screen.window_width())
moon_ground.left(90)
moon_ground.forward(300)
moon_ground.end_fill()

# 🕳️ Ay kraterleri (basit daireler)
def ciz_krater(x, y, r):
    k = turtle.Turtle()
    k.hideturtle()
    objeler2.append(k)
    k.penup()
    k.goto(x, y)
    k.color("gray25")
    k.begin_fill()
    k.circle(r)
    k.end_fill()

ciz_krater(-470, -screen.window_height()//2 + 155, 22)
ciz_krater(-380, -screen.window_height()//2 + 250, 18)
ciz_krater(-190,  -screen.window_height()//2 + 188,  20)
ciz_krater(0,    -screen.window_height()//2 + 145, 14)
ciz_krater(160,   -screen.window_height()//2 + 130, 24)
ciz_krater(220,  -screen.window_height()//2 + 93,  16)
ciz_krater(410,  -screen.window_height()//2 + 255, 19)
ciz_krater(340,  -screen.window_height()//2 + 135, 12)
ciz_krater(-screen.window_width()//2 + 60,  -screen.window_height()//2 + 95, 17)
ciz_krater(screen.window_width()//2 - 100,  -screen.window_height()//2 + 90, 13)
ciz_krater(-220, -screen.window_height()//2 + 115, 21)
ciz_krater(-50,  -screen.window_height()//2 + 139, 20)
ciz_krater(370,   -screen.window_height()//2 + 227,  15)
ciz_krater(220,  -screen.window_height()//2 + 225, 23)




# 🌍 Sol üstte Dünya
earth = turtle.Turtle()
earth.hideturtle()
objeler2.append(earth)
earth.penup()
earth.goto(-screen.window_width()//2 + 60, screen.window_height()//2 - 120)
earth.color("deepskyblue")
earth.begin_fill()
earth.circle(50)
earth.end_fill()



# 🌍 Dünya üzerindeki kıtalar (yeşil şekiller)
def yesillik(x, y, r):
    k = turtle.Turtle()
    k.hideturtle()
    objeler2.append(k)
    k.penup()
    k.goto(x, y)
    k.color("green")
    k.begin_fill()
    k.circle(r)
    k.end_fill()

yesillik(-screen.window_width()//2 + 50, screen.window_height()//2 - 90, 8)
yesillik(-screen.window_width()//2 + 90, screen.window_height()//2 - 70, 6)
yesillik(-screen.window_width()//2 + 40, screen.window_height()//2 - 59, 7)
yesillik(-screen.window_width()//2 + 70, screen.window_height()//2 - 50, 8)

def yildiz_ekle(adet=30):
    for _ in range(adet):
        yildiz = turtle.Turtle()
        yildiz.hideturtle()
        yildiz.penup()
        yildiz.speed(0)
        yildiz.color("white")
        x = random.randint(-screen.window_width()//2 + 20, screen.window_width()//2 - 20)
        y = random.randint(0, screen.window_height()//2 - 20)
        yildiz.goto(x, y)
        yildiz.dot(random.randint(2, 5))  # Farklı boyutlarda nokta yıldız
        objeler2.append(yildiz)  # Sahne kapanışta silinsin diye listeye ekliyoruz


yildiz_ekle(29)

# 🌼 Papatyayı yeniden çiz (aynen önceki gibi)
# (yeni turtle objeleriyle, eskiye dokunmadan)

# Sap
stem2 = turtle.Turtle()
stem2.hideturtle()
objeler2.append(stem2)
stem2.color("green")
stem2.pensize(10)
stem2.penup()
stem2.goto(0, -50)
stem2.setheading(-90)
stem2.pendown()
stem2.forward(100)

# Yapraklar
leaf2 = turtle.Turtle()
leaf2.hideturtle()
objeler2.append(leaf2)
leaf2.color("darkgreen")
leaf2.penup()
leaf2.goto(0, -80)
leaf2.setheading(-160)
leaf2.begin_fill()
leaf2.circle(20, 60)
leaf2.left(120)
leaf2.circle(20, 60)
leaf2.end_fill()
leaf2.penup()
leaf2.goto(0, -120)
leaf2.setheading(-20)
leaf2.begin_fill()
leaf2.circle(20, 60)
leaf2.left(120)
leaf2.circle(20, 60)
leaf2.end_fill()

# Yaprak fonksiyonu ve çizimi
flower2 = turtle.Turtle()
flower2.speed(0)
flower2.hideturtle()
objeler2.append(flower2)

def yaprak2():
    flower2.color("white")
    flower2.begin_fill()
    flower2.circle(30, 60)
    flower2.left(120)
    flower2.circle(30, 60)
    flower2.left(120)
    flower2.end_fill()

flower2.penup()
flower2.goto(0, 0)
flower2.setheading(90)
for i in range(12):
    flower2.penup()
    flower2.goto(0, 0)
    flower2.setheading(i * 30)
    flower2.forward(40)
    flower2.pendown()
    yaprak2()

# Orta sarı kısım
center2 = turtle.Turtle()
center2.hideturtle()
objeler2.append(center2)
center2.penup()
center2.goto(0, -42)
center2.color("yellow")
center2.begin_fill()
center2.circle(40)
center2.end_fill()

# ✍️ Yazı: "Hangi gezegen olursa olsun seni seviyorum aşkım 💜😽"
def yaziyiYavasYaz2(text):
    writer2 = turtle.Turtle()
    writer2.hideturtle()
    writer2.penup()
    writer2.goto(0, -screen.window_height()//2 + 160)
    writer2.color("#FF69B4")  # Pembe (sevimli ton)
    writer2.speed(0)

    birikimli = ""
    for harf in text:
        birikimli += harf
        writer2.clear()
        writer2.write(birikimli, align="center", font=("Verdana", 24, "bold"))
        time.sleep(0.13)
    objeler2.append(writer2)

yaziyiYavasYaz2("Hangi Gezegende Olursa Olsun Seni Seviyorum Aşkıımmmm 💜😽")

# 🎬 Sahneyi yavaş yavaş sil (Ay sahnesi)
time.sleep(4)

for obje in reversed(objeler2):
    obje.clear()
    obje.hideturtle()
    time.sleep(0.1)

# 🎭 Siyah perde (son kapanış)
screen.bgcolor("black")

# ❤️ Kalp ve gölge turtle'ları
kalp = turtle.Turtle()
golge = turtle.Turtle()
for t in [kalp, golge]:
    t.hideturtle()
    t.speed(0)
    t.penup()

# ❤️ Kalp şekli çizimi
def kalp_sekli(t, scale=1.0, renk="#B22222", offset_x=0, offset_y=0):
    t.clear()
    t.color(renk)
    t.begin_fill()
    t.penup()
    t.goto(offset_x, offset_y)
    t.setheading(0)
    t.forward(0 * scale)
    t.left(45)
    t.pendown()
    t.forward(111.65 * scale)
    t.circle(50 * scale, 180)
    t.right(90)
    t.circle(50 * scale, 180)
    t.forward(111.65 * scale)
    t.end_fill()

# ❤️ Kalbi ve gölgeyi çiz
def ciz(scale):
    kalp_sekli(golge, scale, "#5A0000", 10 * scale, -10 * scale)
    kalp_sekli(kalp, scale, "#B22222", 0, 0)
    screen.update()

# ❤️ Nabız efekti ölçekleri
nabiz_dongusu = [1.0, 1.06, 1.12, 1.06, 1.0]

# 📸 7 adet resim ekle (resim1.gif ~ resim7.gif)
resimler = []
koordinatlar = [
    (-300, 200), (200, 220), (-250, -100), (250, -120),
    (-400, 50), (400, 30), (0, -250)
]

for i in range(1, 8):
    turtle.addshape(f"resim{i}.gif")
    t = turtle.Turtle()
    t.shape(f"resim{i}.gif")
    t.penup()
    t.goto(koordinatlar[i-1])
    t.showturtle()
    resimler.append(t)

# 🎵 Müzik çaldığı sürece kalp atsın
while pygame.mixer.music.get_busy():
    for s in nabiz_dongusu:
        ciz(s)
        time.sleep(0.25)

# 🎬 Müzik bitince uygulamayı kapat
turtle.bye()
