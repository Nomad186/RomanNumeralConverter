def checkInput(_str):
    invalidInput = False
    rNumsSplit = []

    for i in _str: 
        rNumsSplit.append(i.upper())

    for i in rNumsSplit: 
        if i not in ['I','V','X','L','C','D','M']: 
            invalidInput = True


    return invalidInput
    
def getRNumerals(): 
    rNums = input('enter roman numerals here: ')

    validInput = checkInput(rNums)

    while validInput == True: 
        rNums = input('please enter a valid response: ')

        validInput = checkInput(rNums)




    return rNums

split_List = []

RomanNumerals = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
    
}
def splitList(_str,lst): 
    for i in _str: 
        lst.append(i.upper())

    return lst

def check_amount_of_I (lst):     
    num = 0
    for i in lst:
        if i == 'I': 
            num += 1
    return num

processedRNums = []

def processRNums3(lst): 
    global processedRNums

    i = 0

    while i < (len(lst) - 1 ): 

        if lst[(i +1)] != 'I' and RomanNumerals[lst[(i + 1)]] > RomanNumerals[lst[i]]: 
            processedRNums.append((RomanNumerals[lst[i + 1]]) - RomanNumerals[lst[i]])

            del lst[i+1]
            del lst[i]
        
        i = i + 1

    return lst

def finalProcessRNums(lst): 
    global processedRNums

    for i in lst: 
        processedRNums.append(RomanNumerals[i])
    return processedRNums

def keepRunning():
    i = input('would you like to do another number?(y/n): ')

    while i.upper() != 'Y' and i.upper() != 'N': 
            i = input('please choose a valid option, (y or n): ')

    if i.upper() == 'Y': 
        return True
    if i.upper() == 'N': 
        return False
    
    return i

keepRunningG = True

def main(): 
    global keepRunningG
    global processedRNums
    global splitRNumerals
    global split_List
    splitRNumerals = []
    processedRNums = []
    r_nums = 0
    split_List = []
    r_nums = getRNumerals()
    splitRNumerals = []
    splitRNumerals = splitList(r_nums,split_List)
    splitRNumerals = processRNums3(splitRNumerals)
    print(sum(finalProcessRNums(splitRNumerals)))
    keepRunningG = keepRunning()

while keepRunningG == True:
    main()

if keepRunningG == False: 
    exit()

#end
