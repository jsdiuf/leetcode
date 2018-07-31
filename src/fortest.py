num=2080
q = num // 1000
num=num-q*1000
b = num // 100
num=num-b*100
s = num // 10
num=num-s*10
g = num % 10
print(q,b,s,g)
