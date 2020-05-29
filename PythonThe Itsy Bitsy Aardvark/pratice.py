


# strTemplate = strTemplate.replace("_1_", choices[0])
# strTemplate = strTemplate.replace("_2_", choices[1])
# strTemplate = strTemplate.replace("_3_", choices[2])
# print(strTemplate)
choices = []

objFile = open("strTemplate.txt.txt","r")
strTemplate = objFile.read()
objFile.close()

for i in range(1,4):
    word = input("Enter word: ")
    choices.append(word)
n = 0
for d in choices:
    n += 1
    strTemplate = strTemplate.replace("_"+str(n)+"_",d)
    print(strTemplate)

objFile = open("strTemplate.txt.txt","w")
strTemplate = objFile.write(strTemplate)



objFile.close()



# objFile = open("odd.csv")
# dictTeams = {}
# for line in objFile:
#     line = line.replace("\n","")
#     listLineContent = line.split(",")
#     teamName = listLineContent[0]
#     teamMembers = listLineContent[1:]
#     dictTeams[teamName] = teamMembers
#     for team in dictTeams:
#         print(team)
#         for person in dictTeams[team]:
#             print(""+person)



