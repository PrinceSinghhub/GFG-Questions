s = "gfg"; t = "fg"
op = 0
for i in t:
    if i in s:
        continue
    else:
        op+=1
print(op)