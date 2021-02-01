#Your task is to complete this function
#Your function should return a String
def convertRoman(n):


    m = ["", "M", "MM", "MMM"]

    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]

    i = ["", "I", "II", "III", "IV", "V",  "VI", "VII", "VIII", "IX"]

    a = m[n//1000]
    b = c[(n % 1000)//100]
    j = x[(n % 100)//10]
    k = i[n % 10]

    ans = (a+b+j+k)

    #print(a,b,j,k,end="")

    return ans

n = int(input())
print(convertRoman(n))
