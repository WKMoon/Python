
import random 
def saperate(path,o_list, counter):
    strMsg = str(counter)
    strMsg += ": "
    strMsg += path
    counter += 1
    o_list.append(strMsg)
    return(o_list, counter)
def main():
    omitlist = []
    objFile = open("Original Text.txt","r")
    print("----------------------------------")
    print("Original Text")
    print("----------------------------------")
    print(objFile.read())
    line_counter = 1
    objFile.seek(0)
    objoutFile = open("Altered Text.txt","w")
    for line in objFile:
        length = len(line)
        if length > 20:
            line = line.lower()
        else:
            line = line.upper() 
        omitlist, line_counter = saperate(line,omitlist,line_counter)
    listnumber = len(omitlist)
    omitNumber = random.randint(1, listnumber)
    n = 1
    for c in omitlist:
        if n == omitNumber:
            c = " "
            c += "\n"
        else : 
            c = c
        n += 1
        objoutFile.write(c)
    objFile.close()
    objoutFile.close()
    objoutFile = open("Altered Text.txt")
    print("----------------------------------")
    print("Altered Text")
    print("----------------------------------")
    print(objoutFile.read())
    objoutFile.close()
if __name__ == "__main__":
    main()