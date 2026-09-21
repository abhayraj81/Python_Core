def runner_up(arr_stu):
    arr_stu = list(arr_stu)
    arr_stu.sort(reverse=True)
    for score in range(len(arr_stu)):
        if arr_stu[score] != arr_stu[score+1]:
            runner_up = arr_stu[score+1]
            break
        else:
            continue
            
    print(runner_up)     
        

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
    runner_up(arr)