n = int(input())

i = 0

while i < n:
    x, op, y, igual, res = input().split()
    x = int(x)
    y = int(y)
    res = int(res)
    if op == '+':
        correto = x + y
    elif op == '-':
        correto = x - y
    elif op == 'x':
        correto = x*y

    qnt_r = correto - res
    qnt_r = abs(qnt_r) * 'r'
    i += 1

    print(f"E{qnt_r}ou!")
    