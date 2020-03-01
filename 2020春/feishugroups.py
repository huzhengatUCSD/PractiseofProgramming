seed='飞书'.encode('utf-8')
ls=list(seed)
group=[]
print(len(ls)//2)
for i in range(len(ls)//2): 
    group.append((ls[i]+ls[i+3]) % 27 +1)
group=list(set(group))
group.sort()
print('飞书项目组号为：%s' % group)