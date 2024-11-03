def hanoi_tower(disks, rods, start = 1, end=None, output = None):
    if end is None:
        end = rods

    # Если только 3 стержня
    if rods == 3:
        hanoi_3(disks, start, end)
    else:
        hanoi_more_rods(disks, rods, start, end)


def hanoi_3(n, start, end, helper = 2):
    if n == 1:
        print(f"Блин 1: Стержень {start} -> Стержень {end}")
    else:
        hanoi_3(n - 1, start, helper, end)
        print(f"Блин {n}: Стержень {start} -> Стержень {end}")
        hanoi_3(n - 1, helper, end, start)


def hanoi_more_rods(disks, rods, start, end):
    if disks == 0:
        return
    elif disks == 1:
        print(f"Блин 1: Стержень {start} -> Стержень {end}")
        return

    # Находим промежуточный стержень
    intermediate_rod = get_intermediate_rods(rods, start, end)

    # Переместить первые n - 1 дисков на промежуточный стержень
    hanoi_more_rods(disks - 1, rods, start, intermediate_rod)

    # Переместить последний диск на конечный стержень
    print(f"Блин {disks}: Стержень {start} -> Стержень {end}")

    # Переместить n-1 дисков с промежуточного стержня на конечный
    hanoi_more_rods(disks - 1, rods, intermediate_rod, end)


def get_intermediate_rods(rods, start, end):
    # Находим промежуточный стержень, который не является начальным или конечным
    for rod in range(1, rods + 1):
        if rod != start and rod != end:
            return rod

# Ввод данных
if __name__ == "__main__":
    try:
        disks = int(input("Введите количество дисков: "))
        rods = int(input("Введите количество стержней: "))

        if disks < 1 or rods < 3:
            print("Должно быть как минимум 1 диск и минимум 3 стержня.")
        else:
            with open("решение.txt", "w") as file:
                file.write("Перемещение Ханойской башни:\n")
                hanoi_tower(disks, rods, output = file)
    except ValueError:
        print("Введите корректные числа.")

