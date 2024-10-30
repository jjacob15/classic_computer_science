#INSIGHT -> simple use of an array as a stack
#INSIGHT -> to make a queue out of two stacks, you add alll the values to one stack then, pop each one out and add it to the second stack. 
# That will invert the list.


def isBalanced(s):
    # Write your code here
    stack = []
    for c in s:
        if c == "{" or c== "(" or c == "[":
            stack.append(c)
        else:
            if len(stack) > 0:
                lastItem = stack.pop()
                if lastItem == "{" and c != "}":
                    return "NO"
                elif lastItem == "(" and c != ")":
                    return "NO"
                elif lastItem == "[" and c != "]":
                    return "NO"
            else:
                return "NO"
    
    if len(stack)== 0: return "YES"
    
    return "NO"    
