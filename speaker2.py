from gtts import gTTS
import random
import time
import time
import playsound
import calendar

def listen_command():
    return input("Скажите вашу команду: ")

def do_this_command(message):
    message = message.lower()
    if "привет" in message:
        say_message("Привет повелитель")
    elif "пока" in message:
        say_message("Пока!")
        exit()
    elif 'как дела' in message:
        say_message("Супер")
    elif 'кто ты' in message:
        say_message("Я Кеша.")
    elif 'таймер' in message:
        say_message("Сейчас")
        qwe = int(input("время в мин: "))
        weqr = qwe*60
        for i in range(weqr,0,-1):
            print(i)
            time.sleep(1)
        say_message("Время")
    elif 'мирзо улугбек' in message:
        say_message("Улугбек — среднеазиатский государственный деятель, правитель тюркской державы Тимуридов, сын Шахруха, внук Тамерлана. Известен как выдающийся математик, астроном, просветитель и поэт своего времени, также интересовался историей и поэзией. Основал одну из важнейших обсерваторий средневековья")
    elif "ехо" in message:
        say_message("Давайте")
        for i in range(1111111111111111111111111):
            ww = input("Слово: ")
            say_message(ww)
            if "++" in ww:
                command = listen_command()
                do_this_command(command)
    elif 'кальк' in message:
        a = int(input("1число: "))
        b = int(input("2число: "))
        c = input("Действие: ")
        if c == '+':
            say_message(str(a+b))
        elif c == '-':
            say_message(str(a-b))
        elif c == '*':
            say_message(str(a*b))
        elif c == '/':
            say_message(str(a/b))
    elif 'умножение' in message:
        for i in range(2, 10):
            print('')
            for j in range(1, 11):
                print(i, "*", j, '=', i*j)
    elif 'календарь' in message:
        calend = int(input('Какой год: '))
        print(calendar.calendar(calend))
    if 'рандом' in message:
        q = 0
        for i in range(10000000):
            r = random.randint(1,10)
            a = int(input("Число: "))
            if r==a:
                print("Молодец")
                print("Я выбирал:",r)
                print("У тебя",q,'балла')
                q=q+5
            elif a==0:
                print("Твой счёт:", q)
            else:
                print("Эх, не повезло")
                print("Я выбирал:",r)
                q = q-1
                print('У тебя осталось',q,"балла")
    else:
        say_message("Команда не распознана!")
    
    
def say_message(message):
    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_"+str(time.time())+"_"+str(random.randint(0,100000))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print("Голосовой ассистент: "+message)

if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
