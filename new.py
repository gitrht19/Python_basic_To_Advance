def find_count(num):
    max_count = 0
    count = 0
    for i in num:
        if i ==2:
            count +=1
        else:
            max_count = max(max_count,count)
            count = 0
    return max(max_count,count)
num = [1,1,0,0,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,7,8,6,3,2,2]
print(find_count(num))