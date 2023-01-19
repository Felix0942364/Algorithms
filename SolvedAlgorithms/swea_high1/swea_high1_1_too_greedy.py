# call input
N = 9
weights = [1,2,3,4,5,6,7,8,9]

# setup cases to test
case = [[1]]
i = 1
r = 1
while i < N:
    i+=1
    r = r * i
    tmp1 = []
    for j in range(len(case)):
        for k in range(i):
            tmp2 = case[j][:]
            tmp2.insert(k, i)
            tmp1 += [tmp2[:]]
    case = tmp1[:]
del tmp1, tmp2
print(case)
# setup left right cases and count
count = 0
run = 0

while case:
    # call with weights
    print(count)
    tmp1 = []
    tmp2 = []
    tmp3 = []
    for i in case.pop():
        tmp1 += [weights[i-1]]
    
    # setup initial properties
    tmp2 = [tmp1.pop()]
    tmp3 = [tmp2[:]]+[[-tmp2.pop()]]
    # [1], [-1]
    while tmp1:
        tmp2 = tmp3[:]
        tmp3 = []
        a = tmp1.pop()
        while tmp2:
            # for i in range(len(tmp2)):
            b = tmp2.pop()
            tmp3 += [b+[a]] + [b+[-a]]
    # check left right

    for i in tmp3:
        test_tmp = 0
        run += 1
        for j in i:
            test_tmp += j 
            if test_tmp < 0:
                break
            if j == i[len(i)-1] :
                count += 1
print(count)