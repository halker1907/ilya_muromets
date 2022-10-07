import _random
secret = random.randint(1, 100000000000000000)
attempts = 0
while True:
    answer = round(secret / 2)
    if answer == secret:
        break
    elif answer > round(secret / 2):
