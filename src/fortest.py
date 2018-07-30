import time
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
       'v', 'w', 'x', 'y', 'z']
p=".*dd..*ea*a*a*w.fr....fr.e*.*d*.we.*..***.**.a*a**.*b"
c="a"
print(c.islower())
for i in arr:
    while "..*" in p or ".*." in p or "**" in p or (i + "*.*") in p or ".*" + i+"*" in p or (i + "*" + i + "*") in p:
        p = p.replace("..*", ".*")
        p = p.replace(".*.", ".*")
        p = p.replace("**", "*")
        p = p.replace(i + "*.*", ".*")
        p = p.replace(".*" + i+"*", ".*")
        p = p.replace(i + "*" + i + "*", i + "*")
print(time.time())
print(p)