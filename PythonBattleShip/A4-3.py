def change(f_file,t_grid):
    for row in f_file:
        row = row.replace("\n","")
        rowAslist = row.split(",")
        t_grid.append(rowAslist)
    return(t_grid)
        
def main():
    missileCount = 0
    objFile = open("map.txt")
    targetGrid = []
    print("Let`s play Battleship!")
    scoreGrid = [[" " for r in range(0,10)] for c in range(0,10)]
    for count in range(30,0,-1):
        print(f"You have {count} missiles remaining")
        targetGrid = change(objFile,targetGrid)
        print("    A B C D E F G H I J")
        number = 0
        for line in scoreGrid:
            element = ""
            number += 1
            for zero in line:
                element += " "
                element += str(zero)
            print(f"{number:2d} {element}")
        verify = 1
        while verify < 2:
            cor = input("Choose your target (EX. A1): ")
            cor = cor.lower()
            if cor[1:] == "" or cor[0] == "":
                print("You have to enter the key.")
            elif cor[0].isnumeric():
                print("The letter position is not a letter. Please enter again.")
            elif not cor[1:].isnumeric():
                print("The number position is not a number. Please enter again.")
            elif int(cor[1:])-1 < 0 or int(cor[1:])-1 > 9:  
                print("The number position is passed the range of number. Please enter again.")  
            elif (ord(cor[0])-97) < 0 or (ord(cor[0])-97) > 9:
                print("The letter position is passed the range of letter. Please enter again.")
            elif int(cor[1:])-1 < 0 or int(cor[1:])-1 > 9:
                print("The number of key is incorrect.")
            else:
                rowLine = ord(cor[0])-97
                coloumLine = int(cor[1:])-1
                if scoreGrid[coloumLine][rowLine] == "x" or scoreGrid[coloumLine][rowLine] == "o":
                    print("You already have entered the key. Please enter another new key.")
                else:
                    verify += 1
        
        missilePoint = targetGrid[coloumLine][rowLine]
        if missilePoint == "1":
            missileCount += 1
            scoreGrid[coloumLine][rowLine]= "x"
            print("Hit!!!!!")
        else:
            scoreGrid[coloumLine][rowLine] = "o"
            print("Miss")
        if missileCount == 17 and count >= 1:
            print("YOU SANK MY ENTIRE FLEET!")
            print("You had 17 of 17 hits, which sank all the ship.")
            print("You won, congratulation!") 
        elif missileCount < 17 and count == 1:
            print("You have 0 missiles remaining")
            print("GAME OVER")
            print(f"You had {missileCount} of 17 hits, but didn`t sink all the ship")
            print("Better luck next time.")
        else:
            continue
        break
if __name__ == "__main__":
    main()