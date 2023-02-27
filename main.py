# num = int(input())
for j in range(1, 11):
    print("Таблица умножения на:", j)
    for i in range(1, 11):

        print(f"Сколько будет: {i} * {j} = ?")
        num = int(input())
        if i * j == num:
            print("Правильно!!!")

        else:
            print(f"Вы ошиблись :( \n Ответ: {i * j} ")

    print()