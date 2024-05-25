'''
Merge Sort Algortihm
Author Andrew Morrison
'''

import random

def merge(list1,list2):
    #compare lists first elements and append onto result list resp to merge lists
    result = []
    while(list1 and list2):
        if list1[0]<=list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    result.extend(list1)
    result.extend(list2)
    return result

def merge_sort(list):
    if len(list)<2:
        #then list is atomic and doesnt need sorted, so return list
        return list
    #generate key using random between 0 and n where n = no elements in list
    r = list[random.randint(0,len(list)-1)]
    #Lists to hold elements equal to, to the left/right of key 
    left,right,mid = [],[],[]
    #loop through elements and create appropriate sublists
    for i in list:
        if i < r :
            #add all elements < key to lefthand list
            left.append(i)
        elif i == r:
            #add elements equal to key to mid list
            mid.append(i)
        else:
            #add elements > key to right hand list
            right.append(i)
    #recursive calls to fully sort each sublist   
    left = merge_sort(left)
    left.extend(mid)
    right = merge_sort(right)
    sorted_list = merge(left,right)
    return sorted_list

if __name__ == "__main__":
    list = []
    invalid = True
    while invalid:
        try:
            n = input("please input integer number list: ")
            list.extend([int(i) for i in n.split()])
            # Set invalid to False after successful input processing
            invalid = False 
        except ValueError:
            print("Something went wrong.. check input")
    print("Unsorted: ", list)
    print("Sorted: ", merge_sort(list))

