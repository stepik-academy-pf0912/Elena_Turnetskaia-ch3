videos = [
"How To Make a Concrete Fire Bowl http://youtu.be/DwJpy48GZF0",
"Making a table top FIRE PIT http://youtu.be/DwJpy48GZF0",
"MODERN Outdoor Concrete and Wood http://youtu.be/zD-lSfDSKn0",
"Diy LED Desk Lamp With Concrete Base http://youtu.be/a5yiMhJaGCo"
]
playlists = [
"Оборудование для мастерской своими руками",
"Литье металла",
"Работа по дереву"
]
print("""Привет, это Stepik ***,  портал видео про ****.
Введите 1, чтобы посмотреть видео, 
2 чтобы найти видео, 
3 чтобы посмотреть плейлисты
exit или 0, чтобы выйти""")
while True:
    a = str(input())
    if a == '1':
       print('У вас нашлось', len(videos), 'видео')
       for i in videos:
            print(i)
    elif a == '2':
         word = input('Введите слово для поиска')
         word = word.lower()
         for i in videos:
            words = i.split(' ')
            for k in words:  
                words = k.lower()
                if (word == words):
                    print(i)
    elif a == '3':
       print('У вас нашлось', len(playlists), 'плейлиста')
       for i in playlists:
            print(i)
    elif a == '0' or a == 'exit':
        print('break')  
        break