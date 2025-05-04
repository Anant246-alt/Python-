def index_list(list,index):
    if index < 0 or index >= len(list):
        return "Index out of range"
    else:
        return list[index]
    
print(index_list([7,18,45],1))
print(index_list([2,4,6,3],4))