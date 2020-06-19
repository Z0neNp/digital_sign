if __name__ == '__main__':

    def getConcatedArr(arr):
        concat_arr = []
        i=0
        size = len(arr)
        while i<size-1:
            concat_arr.append(arr[i]+arr[i+1])
            i += 2
        if (len(arr) % 3) == 1:
            concat_arr.append(arr[len(arr)-1])
        return concat_arr

    def strToNumbersArr(string):
        output_arr = []
        for character in string:
            output_arr.append(str(ord(character)))
        return output_arr

    def getSumOFArr(arr):
        tot = 0
        for value in arr:
            tot += int(value)
        return tot

    def getHashedValue(ןinput_str):
        numbers_arr = strToNumbersArr(input_str)
        concated_arr = getConcatedArr(numbers_arr)
        sum_of_array = getSumOFArr(concated_arr)
        return sum_of_array % 100000

    def easyPrint(string):
        print("\nOriginal string:")
        print(string)

        print("\nArr of string chars:")
        string_arr = []
        for character in string:
            string_arr.append(character)
        print(string_arr)

        print("\nString transformed to numbers arr (white space = '32'):")
        print(strToNumbersArr(input_str))

        print("\nString after concatenate two pairs of numbers")
        print(getConcatedArr(strToNumbersArr(input_str)))

        print("\nCalculate sum of elements:")
        tmpArr = getConcatedArr(strToNumbersArr(input_str))
        i=0
        for elem in tmpArr:
            i += 1
            print(elem, end=" + " if i != len(tmpArr) else " = ")
        print(getSumOFArr(tmpArr))

        print("\nCalculate modulo value of sum (finally our HASH value):")
        print(getSumOFArr(tmpArr), '% 100000 =', getSumOFArr(tmpArr) % 100000)

    input_str = "Java language"
    algoBug = "vaJa language"
    easyPrint(input_str)
    print(getHashedValue(algoBug))