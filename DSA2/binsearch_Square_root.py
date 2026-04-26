# find integral part of square root of a number using binary search
# input is N
# we start from lo=1 and hi=N
# take mid, if mid square = N return mid, 
# if mid quare is more than N, then hi = mid -1
# if mid square is less than N, ans = mid, lo = mid + 1 otherwise mi
def integral_square(N):
    lo = 1
    hi = N
    ans = -1
    while lo <= hi:
        mid = (lo+hi)//2
        print(lo,mid,hi)
        if mid*mid == N:
            return mid
        elif mid*mid < N:
            ans = mid
            lo = mid +1
        elif mid*mid > N:
            hi = mid -1
    return ans
print(integral_square(100))