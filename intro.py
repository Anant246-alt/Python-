import sys
sys.path.append('C:/Users/Admin/Desktop/My_module')

from my_module import find_index as fi, test
import sys

courses = ['OOP','DM','WP','IP']

index = fi(courses, 'IP')
#print(index)
#print(test)

print(sys.path)  