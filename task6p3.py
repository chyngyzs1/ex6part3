# Balanced Brackets
openList = ["[","(","{"]
closeList = ["]",")","}"]
def balance(s):
    stack= []
    for i in s:
        if i in openList:
            stack.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if ((len(stack) > 0) and (openList[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
print(balance("{[()](){}}"))

# openList = ["[","{","("]
#     closeList = ["]","}",")"]
#     stack= []
#     for i in s:
#         if i in openList:
#             stack.append(i)
#         elif i in closeList:
#             pos = closeList.index(i)
#             if ((len(stack) > 0) and (openList[pos] == stack[len(stack)-1])):
#                 stack.pop()
#             else:
#                 return "NO"
#     if len(stack) == 0:
#         return "YES"