def amount():
    if person_age<=25 and tickets_count>=3:
        num = tickets_discount*990*tickets_count
    elif person_age>25 and tickets_count>=3:
        num = tickets_discount*1390*tickets_count
    elif person_age<=25 and tickets_count<3:
        num = 990*tickets_count
    elif person_age>25 and tickets_count<3:
        num = 1390*tickets_count
    return num
    
tickets_count = int(input("Введите кол-во билетов: "))
tickets_discount = 0.9
person_age = int(input("Ваш возраст: "))
final_amount = 0
if person_age>18:
    final_amount = amount()
    print("Сумма к оплате:",final_amount)
else:
    print("Сумма к оплате:",final_amount)