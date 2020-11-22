from ai import aiBot,checkBoard,checkWin
class play:
    board=[".",".",".",".",".",".",".",".","."]
    def showBoard(self):
        board=self.board
        print("*"*20)
        print(" ", board[0], " ", " ", board[1], " ", " ", board[2], " ")
        print(" ", board[3], " ", " ", board[4], " ", " ", board[5], " ")
        print(" ", board[6], " ", " ", board[7], " ", " ", board[8], " ")
        print("*" * 20)
    def makeChance(self,who,where):
        board= self.board
        if where-1in range(9):
            if board[where-1]==".":
                board[where-1]=who
                return True
            else:
                return False
def playAi():
    playing = True
    pla = play()
    board = pla.board
    pla.showBoard()
    while playing:
        chance="O"

        chance = "X"
        x = input("Your chance :")
        if x == "" or x == " ":
            continue
        x = int(x)
        if pla.makeChance(chance, x):
            pla.showBoard()
            if chance == "O":
                chance = "X"
            else:
                chance = "O"
        else:
            continue
        if checkWin(pla.board, "X"):
            print("X won the game")
            break

        elif (checkWin(pla.board, "O")):
            print("O won the game")
            break


        aiBot(pla.board)
        pla.showBoard()

        if checkWin(pla.board, "X"):
            print("X won the game")
            break

        elif (checkWin(pla.board, "O")):
            print("O won the game")
            break
        
        """while True:
                    x = input("Your chance :")
                    if x == "" or x == " ":
                        continue
                    x = int(x)
                    if pla.makeChance(chance, x):
                        pla.showBoard()
                        if chance == "O":
                            chance = "X"
                        else:
                            chance = "O"
                        break
                    else:
                        continue
        
        
"""
        pla.showBoard()
        if checkWin(pla.board,"O"):
            print("O won the game")
            break
        if (checkWin(pla.board,"X")):
            print("X won the game")
            break
        elif (checkWin(pla.board,"O")):
            print("O won the game")
            break
        elif not (checkBoard(pla.board)):
            print("Khichdi ban gai lol LMAO")
            break