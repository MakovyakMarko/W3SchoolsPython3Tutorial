def CalcSumNumbers(A):
    if A == []:
        return 0
    else:
        summ = CalcSumNumbers(A[1:])
        summ = summ + A[0]
        return summ
L = [2,4,4,5,2,6,36]
summ = CalcSumNumbers(L)
print("summ = ", summ)

def CalcSumNegativeNumbers(A):
    if A ==[]:
        return 0
    else:
        count = CalcSumNegativeNumbers(A[1:])
        if A[0]<0:
            count = count + 1
        return count
L = [-2, 3, 5, -11, -3, 0]
n =CalcSumNegativeNumbers(L)
print("n = ", n)

def CalcSumNumbersInLists(A):
    summ = 0
    for t in A:
        if not isinstance(t, list):
            summ = summ + t
        else:
            summ = summ + CalcSumNumbersInLists(t)
    return summ
L = [-2,-3, 8, 11, [-4, 6,[2,[-5,4]]]]
summ =CalcSumNumbersInLists(L)
print("summ = ", summ)

def GetFibonacciList(n,L):
    count = len(L)
    if len(L)<2:
        return []
    num1=L[count-2]
    num2=L[count-1]
    if (num1+num2) < n:
        L = L + [num1+num2]
        return GetFibonacciList(n,L)
    else:
        return L
LL = GetFibonacciList(100, [0,1])
print("LL = ", LL)