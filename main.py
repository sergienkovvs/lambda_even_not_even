import random

nums_ran = random.randint(0,400)

num = lambda: "Не чётное" if nums_ran % 2 else "Чётное"

print(num(), nums_ran)
