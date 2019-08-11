operators = {"+", "-", "*", "@"}
with open("4jr.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    stack = []
    line = line.strip()
    expression = line.strip().split()
    for i in range(len(expression)-1, -1, -1):
        if expression[i] in operators:
            if expression[i] == '+':
                val = int(stack[0]) + int(stack[1])
                stack = stack[2:]
                stack.insert(0, str(val))
            elif expression[i] == '-':
                val = int(stack[0]) - int(stack[1])
                stack = stack[2:]
                stack.insert(0, str(val))
            elif expression[i] == '*':
                val = int(stack[0]) * int(stack[1])
                stack = stack[2:]
                stack.insert(0, str(val))
            elif expression[i] == '@':
                if int(stack[0]) >= 0:
                    val = int(stack[1])
                else:
                    val = int(stack[2])
                stack = stack[3:]
                stack.insert(0, str(val))
        else:
            stack.insert(0, expression[i])
        print("at index:",i, "operator/number:", expression[i], "stack:",stack)
    print("Expression: ", line, "\nResult: \t", stack[0])
