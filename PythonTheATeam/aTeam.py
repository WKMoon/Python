# objFile = open("ateam.txt")
# strContents = objFile.read()
# print(strContents)
#w < write (overwrites or creates)
#r < read (default)
#a < write (appends or creates)
# objFile = open("test.txt")
# print(objFile.read())
# objFile.close()
# ==================
# objFile = open("test.txt", "r")
# strContent = objFile.read()
# print(strContent)
# ================
# inp_obj = open("test.txt")
# out_obj = open("newone.txt","a")            
# for line_str in inp_obj:
#     result_str = line_str
#     out_obj.write(result_str)

# inp_obj.close()
# out_obj.close()
# ======================
# out_obj = open("test.txt","w")
# number = int(input("Enter number"))
# i = 1
# while (i <= number):
#     i += 1
#     newStr = "can i get A+?"
#     out_obj.write(newStr)
# out_obj.close()
# ========================

# for line in objFile:
#     line1 = line.replace("n","N")
#     # print(line1)
#     # print("---------------------")
#     print(len(line))
#     print(line1,end = "")
#     # print("--------------------------")

# objFile.close()


# for line in objFile:
#     line1 = line.replace("n","N")
#     strMsg = "Length ("
#     strMsg += str(len(line))
#     strMsg += ") : " 
#     strMsg += line1
#     print(strMsg)
# objFile.close()
# ================================
# line_number = 0
# for line in objFile:
#     line_number += 1
#     line1 = line.replace("n","N")
    # strMsg = "("
    # strMsg += str(line_number)
    # strMsg += ") : "
    # strMsg += line1
#     print(strMsg)
# objFile.close()
# ===========================
# objFile = open("ateam.txt","r")
# objoutFile = open("out.txt","w")

# for line in objFile:
#     objoutFile.write(line)
# objFile.close()
# objoutFile.close()
# ===================
# objFile = open("ateam.txt","r")
# objoutFile = open("out.txt","w")
# line_counter = 1
# for line in objFile:
#     if (line_counter == 7):
#         objoutFile.write(line)
#     line_counter += 1
# objFile.close()
# objoutFile.close()

