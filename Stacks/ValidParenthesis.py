# 20. Valid Parentheses

# MAKE IT MORE EFFICIENT
def isValid(s: str) -> bool:
    stack = []
    if len(s) % 2 == 1:
        return False
    for ch in s:
        if ch == '(' or ch == '[' or ch == '{':
            stack.append(ch)
        elif len(stack) > 0:
            if ch == ')':
                if stack.pop() == '(':
                    continue
                else:
                    return False
            elif ch == ']':
                if stack.pop() == '[':
                    continue
                else:
                    return False
            elif ch == '}':
                if stack.pop() == '{':
                    continue
                else:
                    return False
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False


# For shorter code, I need to check if each closing bracket matches a popped value
def isValid2(s: str) -> bool:
    stack = []
    hmap = {')': '(',
            '}': '{',
            ']': '['}

    for ch in s:
        if ch in hmap:  # Check if bracket is in hashmap
            if stack and stack[-1] == hmap[ch]:  # If stack is not empty and last value of stack = corresponding opening bracket, remove from stack, or return False
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    return True if not stack else False  # if stack is empty can return true, or else its false



str = '()'
print(isValid2(str))
