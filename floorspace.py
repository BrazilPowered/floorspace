########################
##  FloorSpace Board  ##
##  Match Calculator  ##
########################
import re
import pprint
def main():
    fullBoard = 47.625
    floorLength = input("What is the length of this floor?")
    boardsLeft = loadValsFromFile("/Users/100031247/Documents/FUN/FloorSpace/left")#listBuilder()
    boardsRight= loadValsFromFile("/Users/100031247/Documents/FUN/FloorSpace/right")#listBuilder()
    #try:
    #   storeInFile(raw_input("Please give the full path to Left file:"))
    #except Exception as e:
        #print(e)
    print("Floor length: " + str(floorLength))
    pprint.pprint(compileCombos(boardsLeft,boardsRight,floorLength,fullBoard))



      
#Connect 
def compileCombos(listLeft, listRight, total, increment):
    middle,combos = 0,list()
    if (increment != None) and (increment*2 < total):
        while total >= increment*2:
            middle +=1
            total -= increment
        middle *= increment
    for x in listLeft:
        if(x <= total):
            left = x
            for y in listRight:
                if (total > increment) &(y >= float(total-increment-left)) & (y <= float(total-increment-left)+1):
                    right = y
                    combos.append([left,middle+increment,right,left+middle+increment+right])
                    listRight.remove(y)
                    listLeft.remove(x)
                    break
                elif (y >= float(total-left)-.5) & (y <= float(total-left)+1):
                    right = y
                    combos.append([left,middle,right, left+middle+right])
                    listRight.remove(y)
                    listLeft.remove(x)
                    break
                
    
    if (combos != None):
        return combos
    else:
        return combos
                
# Store lists in file; ; rORa should be w for write or a for append to the file, w by default
def storeInFile(filePath, wORa=None):
    if (wORa is not "a") or (wORa is not "a"):
        wORa = "a"
    with open(filePath, wORa) as f:
        try:
            while True:
                val = fracToDec(raw_input())
                if val is not None:
                    f.write(str(val)+"\n")
        except KeyboardInterrupt:
            pass

# Load list from file
def loadValsFromFile(filePath):
    lenList = list()
    with open(filePath, "r") as f:
        for line in f:
            lenList.append(float(line.strip()))
    return lenList


# Build your list of lengths of boards.
def listBuilder():
    print ("""
    Please enter the lengths for the wood boards, with a new line after each.
    Enter ^C (Keyboard Interrupt) to complete the sequence.""")
    boards = list()
    while True:
        try:
            input = fracToDec(raw_input())
            if input != None:
                boards.append(input)

        except KeyboardInterrupt:
            print("Input complete")
            break
        except Exception as e:
            print(e)
            continue
    return boards

# convert an input of format "1 2/3" into it's float equivalent
def fracToDec(input):
    if re.match("^([0-9]* )?[0-9]+/[0-9]+$", input):
        sp_index = input.find(' ')
        sl_index = input.find("/")
        result = float(input[sp_index+1:sl_index])/float(input[sl_index+1:])
        if (sp_index > 0):
            result += int(input[:sp_index])
        return result
    elif re.match("^[0-9]+$", input):
        return float(input)
    else:
        print("This may have been formatted incorrectly. Follow the format \'1 2/3\'")
        return None



if __name__ == "__main__":
    main()
