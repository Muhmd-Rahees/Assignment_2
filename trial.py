# size = int(input("Enter the size of set : "))
# dict_demo = dict()

# for k,v in dict_demo.item() :
#     key= input("Enter the items : ")
#     value = input("Enter the values")

# size = int(input("Enter the size of the list : "))
# lst1 = []

# for i in range(0,size) :
#     elements = int(input("Enter the desired elements : "))
#     lst1.append(elements)
# print(lst1)

# unique_lst1 = []

# for i in lst1 :
#     if lst1.count(i) == 1 :
#         unique_lst1.append(i)
# print(unique_lst1)



# size = int(input("Enter the size of the list you need : "))
# lst = []

# for i in range(0,size) :
#     elements = int(input("Enter the desired elements  : "))
#     lst.append(elements)
#     print("The list is : ", lst)

# lst.reverse()
# print(lst)

# size = int(input("Enter the size of the list you need : "))
# lst = []

# for i in range(0,size) :
#     elements = int(input("Enter the elements : "))
#     lst.append(elements)
# print("og : " ,lst)

# rev_lst = []

# for i  in range(size-1,-1,-1) :
#     rev_lst.append(lst[i])
# print(rev_lst) 


# size = int(input("Enter the size of the list you need : "))
# lst = []

# for i in range(0,size) :
#     elements = int(input("Enter the elements : "))
#     lst.append(elements)
# print("og : " ,lst)

# rev_lst = []
# for i in range(1,len(lst)+1) :
#     rev_lst.append(lst[-i])
#     print(rev_lst)


# size_items = int(input("Enter the size of dictionary : "))
# my_dict = dict()

# for i in range(size_items) :
#     keys = input("Enter the keys :")
#     values = input("Enter the values : ")
#     my_dict[keys] = values 
    
# print("The dictionary is : ", my_dict)

# for i in my_dict:
#     if values == keys :
#         my_dict.pop(values)
# print(my_dict)






# Input list of non-empty tuples from the user
# input_list = []

# while True:
#     try:
#         num_tuples = int(input("Enter the number of tuples: "))
#         break
#     except ValueError:
#         print("Please enter a valid number.")

# for i in range(num_tuples):
#     while True:
#         try:
#             values = input(f"Enter the values for tuple {i + 1} (comma-separated): ")
#             tuple_values = tuple(map(int, values.split(',')))
#             input_list.append(tuple_values)
#             break
#         except ValueError:
#             print("Please enter valid integer values separated by commas.")

# # Sort the list based on the last element of each tuple
# sorted_list = sorted(input_list, key=lambda x: x[-1])

# # Display the sorted list
# print("Sorted list:", sorted_list)







# Input list of non-empty tuples
# input_list = [(1, 3), (7, 2), (5, 9), (4, 6)]

# # Initialize an empty list to store the sorted tuples
# sorted_list = []

# # Iterate over the input_list for sorting
# for _ in range(len(input_list)):
#     min_tuple = input_list[0]  # Start with the first tuple as the minimum
#     for tup in input_list:
#         if tup[-1] < min_tuple[-1]:
#             min_tuple = tup  # If a smaller last element is found, update min_tuple
#     sorted_list.append(min_tuple)  # Add the minimum tuple to the sorted list
#     input_list.remove(min_tuple)  # Remove it from the input_list

# # Display the sorted list
# print("Sorted list:", sorted_list)


