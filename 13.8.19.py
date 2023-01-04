def amount():
    if person_age<=25 and tickets_count>=3:
        num = tickets_discount*990
    elif person_age>25 and tickets_count>=3:
        num = tickets_discount*1390
    elif person_age<=25 and tickets_count<3:
        num = 990
    elif person_age>25 and tickets_count<3:
        num = 1390
    return num
    
tickets_count = int(input("Введите кол-во билетов: "))
tickets_discount = 0.9
person_age = 0
final_amount = 0
for i in range(tickets_count):
    print("Билет №:",i+1)
    person_age = int(input("Ваш возраст: "))
    if person_age>18:
        final_amount += amount()
print("Сумма к оплате:",final_amount)