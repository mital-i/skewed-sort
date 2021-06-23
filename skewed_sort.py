#skewed sort

a=[5, 6, 7, 8, 3, 4, 2, 1]
def check_randl(arr, low, high):
    mid = int((high+low)/2)
    
    for i in range(mid-low):
        if a[i+mid] > a[low+i]: 
            return False
    return True
    
def skewed_sort(a, low, high):
    if low >= high: 
        return 
    
    mid = int((high+low)/2)
    if check_randl(a, low, high)==True: 
        for i in range(mid-low): 
            a[low+i], a[mid+i] = a[mid+i], a[low+i]
            
        print(a)
    
    skewed_sort(a, low, mid)
    #skewed_sort(a, mid, high)
    
skewed_sort(a, 0, 8)
