def sort(a): 
    n = len(a) 
    swap = True
    start = 0
    end = n-1
    while (swap==True): 

        swap = False
  
        for i in range (start, end): 
            if (a[i] > a[i+1]) : 
                a[i], a[i+1]= a[i+1], a[i] 
                swap=True

        if (swap==False): 
            break

        swap = False
  
        end = end-1

        for i in range(end-1, start-1,-1): 
            if (a[i] > a[i+1]): 
                a[i], a[i+1] = a[i+1], a[i] 
                swap = True
  
        start = start+1
    return a

def binary_search(a,obj):
    mid = int((0 + len(a)) / 2)
    while True:
        if obj == a[mid]:
            return mid + 1
        if obj > a[mid]:
            mid = int((mid + len(a)) / 2)
        if obj < a[mid]:
            mid = int((0 + mid) / 2)
    return False

def sort_and_searh(a,obj):
    find = binary_search(sort(a),obj)
    return find

