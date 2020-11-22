from game import playAi
while True:
    playAi()
    want=input()
    if want=="":
        continue
    else:
        print("Game over")
        break