# data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
# new_list = []
#
# while data_list:
#     minimum = data_list[0]  # arbitrary number in list
#     for x in data_list:
#         if x < minimum:
#             minimum = x
#     new_list.append(minimum)
#     data_list.remove(minimum)
#
# print (new_list)

### ------------------------------------------------------------------

## To print in reverse order and excludnig 1-1 item
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
print(data_list[::-2])  ## [67, -6, 0, -23]

print(data_list[::2])   ## [-5, 5, 23, 23]

