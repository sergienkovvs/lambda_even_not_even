import random

nums_ran = random.randint(0,400)

var = (lambda nums_ran: nums_ran % 2)
if var(nums_ran):
    print("Не чётное")
else:
    print("Чётное")
var(nums_ran)
print(var(nums_ran))