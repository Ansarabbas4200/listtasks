# # TODO 1: write a method with take key, value from the user and add that value in the list..
# #  if key is already filled should return message to user to chose another key.
# #  length of list will be 10
# user_data = {}
# user_list = []
#
#
# def is_empty(value):
#     """Check if the user input is empty"""
#     entered_value = value
#     return entered_value == ""
#
#
# def is_in_data(value):
#     """Check Keys and return True if Key is already occupied"""
#     entered_value = value
#     return entered_value in user_data
#
#
# def manipulation():
#     small_user_key_list.append(new_ID)
#     small_user_key_list.pop(0)
#     small_user_value_list.append(new_value)
#     small_user_value_list.pop(0)
#
#
# # def create_list():
# #     """Take values from the data and returns the list"""
# #
# #     return user_list
#
# while len(user_list) < 10:
#     user_ID = input("Enter a key: ")
#     if is_empty(user_ID):
#         print("! Empty Key is not acceptable. ")
#         continue
#     elif is_in_data(user_ID):
#         print("This key is already occupied. Enter another Key")
#         continue
#     user_value = input("Enter a Value: ")
#     if is_empty(user_value):
#         print("! Empty value is not acceptable. ")
#         continue
#     user_data[user_ID] = user_value
#     user_list.append(user_value)
#
# print(f"Here is the list of values \n{user_list}\n")
#
# # TODO 2: write a method with fixed length of list 5.
# #  if user enter more then 5th value in the list bottom value should be removed
# #  and new value should be added at the top of list
#
# # Slicing dictionary up to 5 items
# small_user_data = {user_ID: user_data[user_ID] for user_ID in sorted(user_data.keys())[:5]}
#
# small_user_key_list = list(small_user_data.keys())
# small_user_value_list = list(small_user_data.values())
# print("We are going to perform LIFO on this list. \n")
# print(small_user_value_list)
#
# is_game_on = True
# while True:
#     new_ID = input("Enter a new key: ")
#     if is_empty(new_ID):
#         print("! Empty Key is not acceptable. ")
#         continue
#     elif is_in_data(new_ID):
#         print("This key is already occupied. Enter another Key")
#         continue
#     new_value = input("Enter a new Value: ")
#     if is_empty(new_value):
#         print("! Empty value is not acceptable. ")
#         continue
#     elif is_in_data(new_value):
#         print("! This value is already in the list.")
#         continue
#     manipulation()
#     print(small_user_value_list)
#
#     final_data = dict(zip(small_user_key_list, small_user_value_list))
#
#     if new_ID == "done":
#         break
#
num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))
my_array = []
for i in range(num_rows):
    row = []
    for j in range(num_cols):
        row.append(0)
    my_array.append(row)

for i in range(num_rows):
    for j in range(num_cols):
        print(my_array[i][j], end=' ')
    print()
