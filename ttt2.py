# Class board begin
class board:
    def __init__(self):
        self.__matrix = [['\0','\0','\0'], ['\0','\0','\0'],['\0','\0','\0']]
        # variable to hold line data
        # 'a' = available, 'b' = blocked, 'X' or 'O' = winner
        self.__line_array = ['a','a','a','a','a','a','a','a']

        # 0 = playable, 1 = winner, 2 = draw
        self.__status = 0
        self.__winner = None

    def instructions(self):
        print("   |   |   ")
        print(" {0} | {1} | {2} ".format("1","2","3"))
        print("---|---|---")
        print(" {0} | {1} | {2} ".format("4","5","6"))
        print("---|---|---")
        print(" {0} | {1} | {2} ".format("7","8","9"))
        print("   |   |  ")

    def print(self):
        bm = self.__matrix
        print("   |   |   ")
        print(" {0} | {1} | {2} ".format( " " if bm[0][0] == "\0" else bm[0][0], " " if bm[0][1] == "\0" else bm[0][1], " " if bm[0][2] == "\0" else bm[0][2]))
        print("---|---|---")
        print(" {0} | {1} | {2} ".format(" " if bm[1][0] == "\0" else bm[1][0], " " if bm[1][1] == "\0" else bm[1][1], " " if bm[1][2] == "\0" else bm[1][2]))
        print("---|---|---")
        print(" {0} | {1} | {2}".format( " " if bm[2][0] == "\0" else bm[2][0], " " if bm[2][1] == "\0" else bm[2][1], " " if bm[2][2] == "\0" else bm[2][2]))
        print("   |   |  ")

    def insert(self, index, symbol):
        row = int((index - 1) / 3) if int(index % 3 ) == 0 else int(index / 3)
        col = 2 if int(index % 3) == 0 else int(index % 3) - 1
        self.__matrix[row][col] = symbol if self.__matrix[row][col] == '\0' else self.__matrix[row][col]
        self.print()
        self.__update()

    
    def status(self):
        return self.__status

    def __update(self):
        la = self.__line_array
        def cl(ln):
            def uc(arr):
                _a = []
                for i in range(3):
                    if(arr[i] != '\0'):
                        _a.append(i)
                return _a
            _uc = uc(ln)
            if(len(_uc) <= 1):
                return 'a'
            elif(len(_uc) == 2):
                return 'b' if ln[_uc[0]] != ln[_uc[1]] else 'a'
            elif(len(_uc) == 3):
                return ln[_uc[0]] if ln[_uc[0]] == ln[_uc[1]] and ln[_uc[0]] == ln[_uc[2]] else 'b'

            # Rows
        m = self.__matrix
        for i in range(3):
            la[i] = cl(m[i])
        # Columns
        for a in range(3):
            la[a+3] = cl([m[0][a], m[1][a], m[2][a]])
        # Diagonals
        la[6] = cl([m[0][0], m[1][1], m[2][2]])
        la[7] = cl([m[0][2], m[1][1], m[2][0]])

        # set status
        ld = True
        for i in range(len(la)):
            if(la[i] != 'a' and la[i] != 'b' and la[i] != '\0'):
                self.__winner = la[i]
                self.__status = 1
                return None
            if(la[i] == 'a'):
                ld = False
        self.__status = 2 if ld == True else 0
        return None
            
class player:
    def __init__(self, symbol):
        self.__symbol = symbol
        
    def symbol(self):
        return self.__symbol

print("\033[2J")

p1 = player(input("Player 1, what symbol would you like to use?  ").upper())
p2 = player(input("Player 2, what symbol would you like to use?").upper())
players = [p1,p2]

brd = board()

#brd.instructions()
cp = players[0]

while(brd.status() == 0):
    print("\033[2J")
    brd.instructions()
    print("\n\n")
    brd.print()

    brd.insert(int(input("Player " +cp.symbol() + " make a move.  ")), cp.symbol())

    if(brd.status() == 1):
        print("Player " + cp.symbol() + " wins!")
        continue
    elif(brd.status() == 2):
        print("DRAW")
        continue
    cp = players[1] if players[0].symbol() == cp.symbol() else players[0]