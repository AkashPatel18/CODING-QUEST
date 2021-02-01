#https://practice.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1/?track=dsa-workshop-1-strings&batchId=308

def areRotations(s1, s2):
    #code here

    if len(s1) != len(s2):
        return 0
    else:
        temp = s1 + s1

        x = temp.count(s2)
        print(x)

        if x > 0:
            return 1
        else:
            return 0


s1 = input()
s2 = input()

print(areRotations(s1,s2))
