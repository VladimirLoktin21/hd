meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ": "шутка",
            "АГРИТЬСЯ": "злиться",
            "EZ": "легко"
            }
            
            
            
word = input("Введите непонятное слово: ").upper()

if word in meme_dict.keys():
    print(meme_dict.get(word))
else:
    print('Такого слова нет в словаре(к сожлению)')
