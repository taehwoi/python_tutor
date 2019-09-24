prec = {'(':1, '+':2, '-':2, '*':3, '/':3, '^':4}
def infix_postfix(tokens):
    output = []
    stack = []
    for item in tokens:
        #pop elements while elements have lower precedence
        if item in prec:
            while stack and prec[stack[-1]] >= prec[item]:
                output.append(stack.pop())
            stack.append(item)
        #delay precedence. append to stack
        elif item == "(":
            stack.append("(")
        #flush output until "(" is reached
        elif item == ")":
            toptoken = stack.pop()
            while stack and toptoken != "(":
                output.append(toptoken)
                toptoken = stack.pop()
            #should be "("
        #operand. append to output stream
        else:
            output.append(item)
    #flush stack to output
    while stack:
        output.append(stack.pop())
    return output

def infix_prefix(exp):
    #exchange the parentheses
    exp = list(exp)
    for i in range(len(exp)):
        if exp[i] == '(':
            exp[i] = ')'
        elif exp[i] == ')':
            exp[i] = '('
    print(exp[::-1])
    return infix_postfix(exp[::-1])[::-1]



print (infix_prefix("A*((B+C))"))
    print(operands)
