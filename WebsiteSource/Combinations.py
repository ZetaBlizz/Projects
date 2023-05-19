def combination(n,k):
    if (k == 0) or (n == 0): return 1
    c = max(n-k,k)
    d = min(n-k,k)
    total = 1
    for i in range(c+1, n+1):
        total *= i
    
    divide = 1
    for i in range(1,d+1):
        divide *=i
    return int(total//divide)

def pascalLine(n):
    line = [1]
    for k in range(0,n):
        line.append(int(line[k]*(n-k)//(k+1)))
    return line

def binomialExpansion(expression, n):
    if "+" in expression:
        coefficients = expression.split("+")
        flag = 0
    else:
        coefficients = expression.split("-")
        flag = 1
    if len(coefficients[0]) ==1: coefficients[0].insert(0,1)
    if len(coefficients[1]) ==1: coefficients[1].insert(0,1)
    
    nums = pascalLine(n)
    total = ""
    
    for k in range(0, len(nums)):
        coefficient = nums[k]*(int(coefficients[0][:-1])**(n-k))*(int(coefficients[1][:-1])**k)
        total += f"{coefficient}{coefficients[0][-1]}^{n-k}{coefficients[1][-1]}^{k}"
        flag *= -1
        if flag >= 0:
            total += "+"
        else:
            total += "-"
    return total[:-1]

if __name__ == "__main__":
    print(binomialExpansion("23x-52y",1000))
    exit()
    for x in range(0,1000):
        line = ""
        for y in range(0,1000):
            if y > x:
                break
            line += str(combination(x,y))
        print(line)