# print("Hello world")
# print("Hayrli tong")
# print("Assalomu alleykum")
# print(2+4*2)
# print(19/5)
# print(2**4)
# print("\"Nexia\", \"Tico\", 'Damas' ko'rganlar qilar havas ")
# beshning darajasini topish
# print(5**4)
# 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
# print(22%4)
# Tomonlari 125 ga teng kvadratning yuzi va predmetrini  toping
# a = 125
# S = a**2
# P = 4 * a
# print(S,P)
# Diametri 12 ga teng bo'lgan doiraning yuzini toping (pi = 3.14)
# d = 12
# pi = 3.14
# S = pi*((d/2)**2)
# print(S)
#  Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)
# a = 6 
# b = 7 
# C = ((a**2)+(b**2))**(0.5)
# print(C)

# O'zgaruvchilar 

# matn = ("Hello world")
# print(matn)
# xabar = "Salom bevafo dunyo"
# print(xabar)
# class = "Salom dunyo"
# print(class)
# radius = 5 
# pi = 3.14159
# aylana_yuzi = pi * (radius**2)
# print(f"Radiusi,{radius} ga teng aylananing yuzi, {aylana_yuzi}")

# 05 String(Matn)

# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# kocha = input("ko'changizni nomini kiriting>>")
# mahalla = input("mahllangizni nomini kiriting>>")
# tuman = input("tumaningizni nomini kiritng>>")
# viloyat = input("viloyatingizni nomini kiriting>>")
# # manzil = f"{kocha.capitalize()} ko'chasi, \n{mahalla.capitalize()} mahallasi, \n{tuman.capitalize()} tumani, \n{viloyat.capitalize()} viloyati"
# # print(manzil)

# # manzil = f"{kocha.capitalize()} ko'chasi, \n{mahalla.capitalize()} mahallasi, \n{tuman.capitalize()} tumani, \n{viloyat.capitalize()} viloyati"
# # manzil = f"{kocha.title()} ko'chasi, \n{mahalla.title()} mahallasi, \n{tuman.title()} tumani, \n{viloyat.title()} viloyati"
# manzil = f"{kocha.upper()} ko'chasi, \n{mahalla.upper()} mahallasi, \n{tuman.upper()} tumani, \n{viloyat.upper()} viloyati"
# print(manzil)

# 06 Sonlar
# son = int(input("Istalgan sonni kiriting\n>>"))
# kvadrati = son**2
# kubi = son **3
# print(f"{son} ning kvadrati {kvadrati} ga teng\n{son} ning kubi {kubi} ga teng")

# yosh = int(input("Yoshingizni kiriting\n>>"))
# t_yil = 2025 - yosh
# print(f"Siz {t_yil} da tug'ilgansiz")

# birinchi_son = float(input("Birinchi sonni kiriting\n>>"))
# ikkinchi_son = float(input("Ikkinchi sonni kiriting\n>>"))
# result = f"{birinchi_son} + {ikkinchi_son} = {birinchi_son+ikkinchi_son}\n{birinchi_son} - {ikkinchi_son} = {birinchi_son-ikkinchi_son}\n{birinchi_son} * {ikkinchi_son} = {birinchi_son*ikkinchi_son}\n{birinchi_son} / {ikkinchi_son} = {birinchi_son/ ikkinchi_son}"
# print(result)

# 07 List (Ro'yxat)
# mevalar = ['olma','anjir','shaftoli',"o'rik"] #mevalar ro'yxati
# narhlar = [12000, 109000, 22000] #narhlar ro'yxati
# sonlar = ['bir', 'ikki', 4,7] # sonlar ro'yxati 
# ismlar = [] # bo'sh ro'yxat
# print(f"Birinchi meva: {mevalar[0]}")
# print(f"Ikkinchi meva: {mevalar[1]}")
# print(f"Birinchi meva: {mevalar[1].capitalize()}")
# print(f"Ikkinchi meva: {mevalar[2].upper()}")
# print(f"{narhlar[1]+narhlar[0]}")

# car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
# print(car_models[-2])

# Elementlarni o'zgartirish va qo'shish
# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = 13000 # 1 - qiymatni 13000 ga o'zgartiramiz
# narhlar[1] = 20000 # 2 - qiymatni 20000 ga o'zgartiramiz
# narhlar[3] = 30000 # 4 - qiymatni 30000 ga o'zgartiramiz
# print(narhlar)
# mevalar.append("tarvuz")
# print(mevalar)
# ismlar.append("Ozodbek")
# ismlar.append("Alisher")
# ismlar.append("G'anisher")
# print(ismlar)
# mevalar = []
# mevalar.append("o'rik")
# mevalar.append("shaftoli")
# mevalar.append("nok")
# print(mevalar)
# cars = ['Nexia1', 'Nexia2', 'Lacetti']
# cars.insert(1, 'Malibu')
# print(cars)
# del cars[0]
# del cars[1]
# print(cars)
# hayvonlar = ['it', 'it',  'mushuk', 'toti', 'it']
# hayvonlar.remove('it')
# print(hayvonlar)
# bozorlik = ['yog', 'banan', 'tuz', 'choy']
# mahsulot  = bozorlik.pop()
# print(f"Men {mahsulot} sotib oldim, \nOlinmagan mahsulotlar {bozorlik}")

# ismlar = ["Alisher", "Ozodbek", "Sarvar"]
# print(ismlar)
# print(f"Salom {ismlar[0]}, bugun choyxona bormi? \n{ismlar[1]}, choyxonaga borasizmi?")
# sonlar = [1, 4, -6, 2.3]
# print(sonlar)
# qoshish = sonlar[0] + sonlar[3]
# kopaytirish = sonlar[1] * sonlar[2]
# print(qoshish, kopaytirish)
# sonlar[0] = 8
# sonlar[3] = 15
# print(sonlar)
# sonlar[0], sonlar[1] = sonlar[3], sonlar[1]
# print(sonlar)

# t_shaxslar = ['Amir Temur',"Alisher Navoiy", "Jaloliddin Manguberdi"]
# z_shaxslar = ['Ozodbek', "Sarvar", "Jasurbek"]
# print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan \nzamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan suhbatlashishdi hohlayman")

# friends = []
# friends.append('Ozodbek')
# friends.append("John")
# friends.append("Fhill")
# friends.remove("Ozodbek")
# friends.remove("Fhill")
# print(friends)
# friends.insert(0,"Beckhem")
# friends.append("Messi")
# print(friends)

# mehmonlar = []
# mehmonlar.append(friends.pop(0))
# mehmonlar.append(friends.pop(2))
# mehmonlar.append(friends.pop(1))
# print(mehmonlar)

# 08 Ro'yxatlar bilan ishlash

# alifbo ketma ketligida tartiblash
# cars = ['bmw', 'mercedez benz', 'volvo', 'general motors', 'tesla', 'audio']
# cars.sort()
# print(cars)
# cars = ['bmw', 'mercedez benz', 'volvo', 'general motors', 'Tesla', 'audio']
# cars.sort()
# cars.sort(reverse=True)
# print(cars)
# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print(f"sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print(f"Asl ro'yxat o'zgarmas qoldi", mehmonlar)
# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print(sorted(mehmonlar, reverse=True))
# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))
# fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# print(fruits)
# fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# fruits.reverse()
# print(fruits)
# fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# result = len(fruits)
# print(result)
# fruit = 'pear'
# result  = len(fruit)
# print(result)
# sonlar = list(range(0, 10))
# print(sonlar)
# juft_sonlar = list(range(0,20,2)) #Juft sonlar
# print(juft_sonlar)
# toq_sonlar = list(range(1,20,2)) #Toq sonlar
# print(toq_sonlar)
# narhlar = [15000, 10000, 90000, 6000]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print(f"Eng arzoni {arzon}, eng qimmati {qimmat}, jami {jami}")
# cars = ['bmw', 'gm', 'ferrari', 'nexia','lacetti']
# my_cars = cars[0:3]
# print(my_cars)
# sonlar = [1,2,3,4,5]
# sonlar2 = sonlar[:]
# sonlar2.append(6)
# sonlar2.append(8)
# sonlar2.insert(0, 0)
# sonlar2.insert(0,-1)
# print(sonlar)
# print(sonlar2)
# tomonlar = (20,30,40)
# print(tomonlar)
# toys = ('bus', 'car', 'bear', 'dino', 'snake')
# toys = list(toys)
# toys[0]='lizard'
# print(tuple(toys))
# j_sonlar = list(range(120, 1200, 2)) #juft sonlar
# boshi = j_sonlar[:20]
# orta = j_sonlar[260:280]
# oxiri = j_sonlar[520:]
# print(boshi)
# print(orta)
# print(oxiri)
# print(len(j_sonlar))

# mevalar = ['olma', 'nok', 'banan', 'gilos']
# print(mevalar)
# sonlar = [10, 20, 30, 40, 50]
# sonlar.remove(10)
# sonlar.remove(50)
# print(sonlar)
# royxat = []
# royxat.append('Python')
# royxat.append('Java')
# royxat.append('C++')
# print(royxat)
# mevalar = ['olma', 'banan', 'gilos']
# mevalar.remove('banan')
# print(mevalar)
# ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# result = len(ismlar)
# print(result)
# shaharlar = ['Namangan', 'Toshkent', 'Andijon', 'Samarqand']
# # shaharlar.sort()
# print(sorted(shaharlar))
# sonlar = [1,2,3,4,5]
# sonlar[0]=sonlar[0]*2
# sonlar[1]=sonlar[1]*2
# sonlar[2]=sonlar[2]*2
# sonlar[3]=sonlar[3]*2
# sonlar[4]=sonlar[4]*2
# print(sonlar)
# nums = [12, 45, 23, 67, 34, 89, 11]
# eng_kattasi = max(nums)
# print(eng_kattasi)
# harflar = ['a','b','c','d', 'e']
# harflar.sort(reverse=True)
# print(sorted(harflar, reverse=True))
# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(f'Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorgi oshga taklif qilamiz')
#     print("Hurmat bilan Palonchivlar oilasi")
# sonlar = list(range(1,11))
# print(sonlar)
# for son in sonlar:
#     print(f"{son} ning 2 ga ko'paytmasi: {son*2}")
# ismlar = ['Ozodbek', 'Jasurbek', 'Alisher', 'Javohir', 'Sarvar']
# for ism in ismlar:
#     print(f'Salom, {ism}')
# print(f"{len(ismlar)} marta takrorlandi")

# toq_sonlar = list(range(11, 100, 2))
# for n in toq_sonlar:
#     print(n**3)
# # print(toq_sonlar)
# print("5 ta sevimli filmingizni kiriting")
# kinolar = []
# for n in range(5):
#     kinolar.append(input(f"{n+1}-sevimli film:"))
# print(kinolar)
# soni = input("Bugun nechta mijoz bilan suhbatlashdingiz??\n>>")
# royxat = []
# for n in range(soni):
#     ism.input(f"{n+1}-mijoz")
#     royxat.append(ism)
# print(royxat)
# soni = int(input("Bugun necha kishi bilan ga[lashdingiz\n>>"))
# royxat = []
# for n in range(soni):
#     ism = input(f'{n+1}-mijoz:')
#     royxat.append(ism)
# print(royxat)
# ism = input("Ismingizni kiriting\n>>")
# if ism.lower() == 'ali':
#     print(f"Salom {ism.capitalize()}")
# else:
#     print(f"Biz alini kutyapmiz:")
# javob = float(input("12X6 ning natijasi nechiga teng?\n>>"))
# if javob == 72:
#     print("Javob to'gri")
# else:
#     print('Sizning javobingiz xato')

# cars = ['toyoto', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.capitalize())
#     else:
#         print(f'{car.upper()}')

# login = input('Logindi kirting\n>>')
# if login.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilarni ro'yxatini ko'rasizmi? ")
# else:
#     print(f"Xush klibsiz, {login.capitalize()}!")

# print("Ikkita son kiriting")
# x = float(input("Birinchi sonni kiritng\n>>"))
# y = float(input("Ikkinchi sonni kiriting\n>>"))
# if x==y:
#     print(f"Sonlar teng: {x} == {y}")
# else:
#     print(f"Teng emas")

# son = float(input("Istallagan sonni kirting\n>>"))
# if son > 0:
#     print("Musbat son")
# else:
#     print('Manfiy son')

# son = float(input("Istalgon sonni kiriting\n>>"))
# if son > 0:
#     print(f'{son**(0.5)}')
# else:
#     print('Musbat son kiriting')

# son = float(input("Sonni kiritng\n>>"))
# if son%2 == 0:
#     print('Juft son')
# else:
#     print('Toq son')

# yosh = float(input("yoshingizni kiriting\n>>"))
# if yosh >=18:
#     print("Kattalarsiz")
# else:
#     print('Voyaga yetmagansiz')

# parol = input("Parolni kiritng\n>>")
# if (parol.lower() == "python2025"):
#     print("Xush kelibsiz")
# else:
#     print("Parol noto'g'ri")

# son = float(input("Son kiritng\n>>"))
# if son > 0:
#     print('Musbat son')
# elif(son<0):
#     print("Manfiy son")
# else:
#     print("Son 0 ga teng")

# son = int(input("Foydalanuvchi 3 ta son kiritsin\n >>"))
# for n in son:
#     print(son)


# login = input("Login kiriting\n>>")
# if login.lower() == "admin":
#     print('Assalomu aleykum, admin')
# else:
#     print('Xush kelibsiz foydalanuvchi!')

# son = float(input("son kiriting\n>>"))
# if son == 1:
#     print("Dushanba")
# elif son ==2 :
#     print('Seshanba')
# elif son ==3:
#     print('Chorshanba')
# elif son==4 :
#     print('Payshanba')
# elif son==5:
#     print("Juma")
# elif son==6:
#     print('Shanba')
# elif son==7:
#     print('Yakshanba')
# else:
#     print('Bunday kun yoq')

# 11 Bir nechta shartlarni tekshirish
# age = float(input("Yoshingizni kiriting\n>>"))
# if age <=4:
#     price = 0
# elif age <=12:
#     price = 5000
# else:
#     price = 10000
# print(f"Sizga kirish {price} so'm")

# kun = input("Bugun qanaqa kun??\n>>")
# if (kun.lower() == "shanba" or kun.lower()== 'yakshanba'):
#     print(f'Bugun dam olish kuni')
# else:
#     print(f'Bugun ish kuni')

# kun = input('Bugun kun nima?\n>>')
# harorat = float(input('Havo harorati qandey?\n>>'))
# if (kun.lower() == 'yakshanba' and harorat>30):
#     print(f"Cho'milgani boramiz")
# else:
#     print('Bugun dam olamiz.')
# if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik")
# elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat<=30:
#     print("Uyda dam olamiz")
# narh = 15000
# choy =True
# salat=False
# non = True
# kampot = True
# assorti =False
# if choy:
#     print('Mijoz choy oldi')
#     narh = narh+3000
# if salat:
#     print('Mijoz salat oldi')
#     narh = narh+5000
# if non:
#     print("Mijoz non oldi")
#     narh = narh+10000
# if kampot:
#     print('Mijoz kampot oldi')
#     narh = narh +8000
# if assorti:
#     print('Mijoz assorti oldi')
#     narh = narh + 20000
# print( narh)
 
# menu = ['osh', 'shorvo', 'manti', 'mastava']
# mijoz = input("Qaysi ovqatdi yeysiz\n>>")
# if mijoz in menu:
#     print('Buyurtma qabul qilindi')
# else:
#     print("Bizda bunday taom yo'q")

# if mijoz not in menu:
#     print("Bizda bunday taom yo'q")
# else:
#     print('Buyurtma qabul qilindi')

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik', 'qazi']
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Bizda,{taom} bor")
#         else:
#             print(f'Kechirasiz, {taom} yoq')
# else:
#     print(f"Savatcha bo'sh!")

#Amaliyot
# son_kiriting = float(input("Juft son kiriting\n>>")) 
# if son_kiriting%2 == 0:
#     print(f"Raxmat")
# else:
#     print(f"Bu juft son emas")

# yosh = float(input('Yoshingizni kiriting\n>>'))
# if yosh<4 or yosh >60:
#     price=0
# elif yosh<18:
#     price=10000
# elif yosh>18:
#     price = 20000
# print(f"Sizga kirish {price} so'm")

# x = float(input("Birinchi sonni kiriting\n>>"))
# y = float(input('Ikkinchi sonni kiriting\n>>'))
# if x > y:
#     print(f"{x} > {y}")
# else:
#     print("Mavjud emas")

# mahsulot = ['olma', 'banan', 'limon', 'mandarin', 'kakos', 'uzum', 'nok', 'anjir']
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulot:"))
# for n  in savat:
#     if n in mahsulot:
#         print(f"Do'konimizda {n} bor")
#     else:
#         print(f"Kechirasiz, {n} yo'q")

# mahsulotlar = ['olma', 'anjir', 'behi', 'shaftoli', 'limon']
# savat = []
# for n in range(5):
#   savat.append(input(f"{n+1}-mahsulot:"))

# bor_mahsulotlar = []
# mavjud_emas = []

# for mahsulot in savat:
#   if mahsulot in mahsulotlar:
#     bor_mahsulotlar.append(mahsulot)
#   else:
#     mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# foydalanuvchi = ['admin', 'alisher', 'ozodbek', 'jasurbek', 'sarvar']
# free_list = []
# # yangi_login = input("Login kiriting\n>>")
# for n in range(5):
#     free_list.append(input(f"{n+1}-login:"))
# print(free_list)
# for name in free_list:
#     if name in foydalanuvchi:
#         print(f"{name} nomli Login band, yangi login tanlang!")
#     else:
#         print(f"Xush kelibsiz {name}")

# foydalanuvchi = float(input("Biror son kiriting\n>>"))
# for n in range(2,11):
#     if foydalanuvchi%n == 0:
#         print(f"{foydalanuvchi} soni {n} ga qoldiz bo'linadi")

print('Salom dunyo')