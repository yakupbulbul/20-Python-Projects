# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a funcation that takes a list and target parameter
# multiple variables : middle, start, end, steps
# recursion or while loop 
# increase the steps each time a split is done 
# conditions to track target position 

def binary_search(list, element): 
    middle = 0
    start = 0
    end = len(list)
    print("Length: ", len(list))
    steps = 0


    while(start<=end):
        print("Steps", steps, ":", str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2
        print("Middle: ", middle)

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else: 
            start = middle + 1
    
    return - 1



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target = 6

binary_search(my_list, target)



# for i in my_list:
#     print("I: ",i)
#     if i == target:
#         print("Founded")
#         break
