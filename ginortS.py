import string


def wordFirstLittleFirstOddFirst(c):
    if c.isalpha():
        if c.islower():
            cVal = string.ascii_lowercase.index(c)
            return cVal
        else:
            cVal = string.ascii_uppercase.index(c)
            return cVal + 1000
    else:
        cInt = int(c)
        if cInt % 2 == 0:
            return cInt + 100000
        else:
            return cInt + 10000


inputString = input()
outputString = sorted(inputString, key=wordFirstLittleFirstOddFirst)
print(*outputString, sep='')
