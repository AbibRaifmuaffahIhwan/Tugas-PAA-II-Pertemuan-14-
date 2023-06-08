# # Optimized Bubble sort in Python
# def bubbleSort(array):
#     # loop through each element of array
#     for i in range(len(array)):
#
#         # keep track of swapping
#         swapped = False
#
#         # loop to compare array elements
#         for j in range(0, len(array) - i - 1):
#
#             # compare two adjacent elements
#             # change > to < to sort in descending order
#             if array[j] > array[j + 1]:
#                 # swapping occurs if elements
#                 # are not in the intended order
#                 temp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = temp
#
#                 swapped = True
#
#         # no swapping means the array is already sorted
#         # so no need for further comparison
#         if not swapped:
#             break
#
#
# data = [-2, 45, 0, 11, -9]
# print("Data Original : ", data)
# bubbleSort(data)
# print('Sorted Array in Ascending Order : ', data)

def bs(list):
    iterasi = 0
    for j in range (len(list)-1):
        for i in range(len(list)-1-j):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
        iterasi+=1
        print(iterasi, list)

list = [9,17,2,42,1,7,3,4,67]
print('Data yang akan di sort :', list )
print('Bubble Sort :')
bs(list)