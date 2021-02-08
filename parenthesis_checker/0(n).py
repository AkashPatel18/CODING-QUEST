def ispar(x):
    # code here

    opening = "([{"
    closing = ")]}"

    matching = {

        ")": "(",
        "]": "[",
        "}": "{"

    }

    stack = []

    for i in x:
        if i in opening:
            stack.append(i)

        elif i in closing:
            if len(stack) == 0:
                return False
            if stack[-1] == matching[i]:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False
