def SubsequenceLength(s):
    #Codee here
    lastseen = {}
    startIndex = 0
    longest = [0, 1]

    if s == "":
        return 0

    for i, char in enumerate(s):
        if char in lastseen:
            startIndex = max(startIndex, lastseen[char] + 1)
            print("this is starttinsg index",startIndex)
        if longest[1] - longest[0] < i+1-startIndex:
            longest = [startIndex, i+1]
            print("this is longest",longest)
        lastseen[char] = i
        print(lastseen)

    return longest[1] - longest[0]
    


s = "geeksforgeeks"
print(SubsequenceLength(s))
