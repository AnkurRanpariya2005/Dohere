if __name__ == "__main__":
    T=int(input())
    while(T>0):
        NS=[int(x) for x in input().strip().split()]
        n=NS[0]
        k=NS[1]
        list=[int(x) for x in input().strip().split()]
        last,start,start_sum,flag = 0, 0, 0, False

        for i in range(n):
            start_sum += list[i]
            if(start_sum>=k):
                last = i
                while(k<start_sum and start<last):
                    start_sum -= list[start]
                    start = start+1
                if(start_sum==k):
                    print(str(start+1) + " " + str(last+1))
                    flag=True
                    break

        if flag==False:
            print(-1)
        T=T-1

