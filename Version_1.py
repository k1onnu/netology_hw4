def hanoi_tower(disk, start, finish, helper):
    if disk > 0:
        hanoi_tower(disk - 1, start, helper, finish)
        print(f"Блин {disk}: Стержень {start} -> Стержень {finish}")
        hanoi_tower(disk - 1, helper, finish, start)

hanoi_tower(3,'1','3','2')

