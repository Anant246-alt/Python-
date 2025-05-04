def even_odd(integers):
    even = [x for x in integers if x % 2 == 0]
    odd = [x for x in integers if x % 2 != 0]
    return even[0] if len(even) == 1 else odd[0]
    
print(even_odd([2,4,5,6,8]))
print(even_odd([1,3,5,6,9]))