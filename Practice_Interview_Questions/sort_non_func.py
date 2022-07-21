# list = [100,12,10,-10,0.5,0.1,12.3] #computer put in a memory
# sortList = []
# #i = 0
# while list:
#     firstIndex = list[0]
#     for i in list: # i = 12 respectively
#         #firstIndex = list[0]
#         # secondIndex = list.index(100.0, firstIndex + 1)
#         if firstIndex > i:
#             firstIndex = i # to find the new minimum, first 12 is the smallest, then it swaps to the smaller
#     sortList.append(firstIndex)
#     list.remove(firstIndex)
        
# print(sortList)

#-------------------------------------------------------------

#reverse
    
list = [100,12,10,-10,0.5,0.1,12.3] #computer put in a memory
sortList = []
#i = 0
while list:
    firstIndex = list[0]
    for i in list: # i = 12 respectively
        #firstIndex = list[0]
        # secondIndex = list.index(100.0, firstIndex + 1)
        if firstIndex < i:
            firstIndex = i # to find the new minimum, first 12 is the smallest, then it swaps to the smaller
    sortList.append(firstIndex)
    list.remove(firstIndex)
        
print(sortList)       