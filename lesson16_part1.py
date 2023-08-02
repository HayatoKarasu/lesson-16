class Cassa(object):
    kol = 1000
    
    def top_up(self):
        x = int(input("Введите сумму: "))
        dey.kol += x
        print(dey.kol)
        return
        
    def count_1000(self):
        a = dey.kol
        a //= 1000
        print("В кассе: ", a, "тыс. купюр")
        
        
    def take_away(self):
        x = int(input("Введите сумму: "))
        dey.kol -= x
        print(dey.kol)
        return
        
        
dey = Cassa()
        
while True:
    print("МЕНЮ:")
    print("1. Пополнить кассу")
    print("2. Сколько 1000 купюр в кассе")
    print("3. Изъять из кассы")
    print("4. Выход")
    
    choice = input("Выберите действие: ")
    
    if choice == '1':
        print("Вы выбрали пополнить кассу")
        dey.top_up()
        
    elif choice == '2':
        print("Вы выбрали сколько 1000 купюр")
        dey.count_1000()
        
    elif choice == '3':
        print("Вы выбрали изъять из кассы")
        dey.take_away()
         
    elif choice == '4':
        break
        
    else:
        print("Неправильный выбор.")
