signals = ['+', '-', '*', '/', '^', '(', ')']


def cleanExp(expression):
    exp = expression.replace('e+', '*10^+').replace('e-', '*10^-')
    return exp


def splitExp(expression):
    lastP, newExp = 0, list()
    try:
        for p, n in enumerate(expression):
            if n in signals:
                if expression[lastP:p] != '':
                    newExp.append(float(expression[lastP:p]))
                if (n == '-' or n == '+') and expression[lastP:p] == '':
                    continue
                newExp.append(n)
                lastP = p+1
            elif p == len(expression)-1:
                newExp.append(float(expression[lastP:p+1]))
        return newExp
    except:
        return ['Erro']


def doParenthesis(expression):
    pos, parPos = 0, list()
    try:
        while '(' in expression or ')' in expression:
            if expression[pos] == '(' or expression[pos] == ')':
                parPos.append(pos)
            if len(parPos) == 2:
                if '(' not in expression[parPos[0]+1:parPos[1]+1]:
                    addExp = doCalculate(expression[parPos[0]+1:parPos[1]])
                    del(expression[parPos[0]:parPos[1]+1])
                    expression.insert(parPos[0], addExp)
                    parPos, pos = list(), -1
                else:
                    pos = parPos[0]
                    parPos = list()
            pos += 1
        return expression
    except:
        return ['Erro']


def doCalculate(expression):
    try:
        pos = 0
        while '^' in expression:
            pos = expression.index('^')
            expression[pos] = pow(expression[pos-1], expression[pos+1])
            expression.pop(pos-1), expression.pop(pos)
        pos = 0
        while '*' in expression or '/' in expression:
            if expression[pos] == '*':
                expression[pos] = expression[pos-1]*expression[pos+1]
                expression.pop(pos-1), expression.pop(pos)
                pos -= 2
            elif expression[pos] == '/':
                expression[pos] = expression[pos-1]/expression[pos+1]
                expression.pop(pos-1), expression.pop(pos)
                pos -= 2
            pos += 1
        pos = 0
        while '+' in expression or '-' in expression:
            if expression[pos] == '+':
                expression[pos] = expression[pos-1]+expression[pos+1]
                expression.pop(pos-1), expression.pop(pos)
                pos -= 2
            elif expression[pos] == '-':
                expression[pos] = expression[pos-1]-expression[pos+1]
                expression.pop(pos-1), expression.pop(pos)
                pos -= 2
            pos += 1
        return expression[0] if len(expression) == 1 else 'Erro'
    except:
        return 'Erro'


def returnResult(expression):
    exp = cleanExp(expression)
    exp = splitExp(exp)
    exp = doParenthesis(exp)
    exp = str(doCalculate(exp))
    return exp
