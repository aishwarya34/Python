from timeit import Timer


print("\n\n\nFibonacci  |  time efficiency  |  recursion  vs  list \n")


for i in range(1,41):
    s = "fibo("+str(i)+")"
    time1 = Timer(s,"from fibonacci import fibo").timeit(3)
    s = "fibo_iterative("+str(i)+")"
    time2 = Timer(s,"from fibonacci import fibo_iterative").timeit(3)
    s = "fibo_memory("+str(i)+")"
    time3 = Timer(s,"from fibonacci import fibo_memory").timeit(3)
    print("n=%2d, fibo: %8.6f , fibo_iterative: %7.6f, fibo_memo: %7.6f, percent12:%10.2f, percent32:%10.2f" % (i,time1,time2,time3,time1/time2, time3/time2))


