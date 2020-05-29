def main():
    def dictonary(g):
        g = g.replace("\n","")
        listLineContent = g.split(",")
        bigName = listLineContent[0]
        bigMembers = listLineContent[1:]
        bigSpace[bigName] = bigMembers

    print("The Itsy Bitsy Aardvark")
    origine = open("the_choices_file.csv")
    bigSpace = {}
    for line in origine:
        dictonary(line)
    answerList = []
    for eachline in bigSpace:
        print(f"Please choose {eachline}:")
        i = 1
        for eachword in bigSpace[eachline]:
            print(f"{i}) {eachword}")
            i += 1
        n = 1
        while n == 1:
            answer = input("Enter choice (1-5): ")
            if answer.isnumeric()==False:
                print("That was invalid answer. Please try again")
            elif int(answer) > 5:
                print("That was invalid answer. Please try again")        
            else:
                answer = int(answer)
                realAnswer = (bigSpace[eachline][answer-1])
                realAnswer = realAnswer.upper()
                answerList.append(realAnswer)
                n = 0    
    fixingStory = open("the_story_file.txt")
    startStory = fixingStory.read()
    for i in range(0,7):
        strPH = "_"
        strPH += str(i + 1)
        strPH += "_"
        startStory = startStory.replace(strPH, answerList[i])
        
    print("Your Completed Story:")
    print(f"\n{startStory}")
    origine.close()
    fixingStory.close()
if __name__ == "__main__":
    main()