aaa = [[33.450500,126.569968],[33.450500,126.569968],[33.450500,126.569968]]

print(str(aaa))

bbb= "[[1,2],[3,4],[5,6]]"
ccc = eval(bbb)
print(ccc)


bbb2= [1.2,3.5,5.8]
ccc2 = map(int,bbb2)
print("bbb2",list(map(int,bbb2)),type(map(int,bbb2)))

for i in ccc2 :
    print(i)
