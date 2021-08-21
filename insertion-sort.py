def insertion_sort(unordered_list):
   for index, _ in enumerate(unordered_list):
      if index + 1 < len(unordered_list) and unordered_list[index] > unordered_list[index + 1]:
         unordered_list[index + 1], unordered_list[index] = unordered_list[index], unordered_list[index + 1]
         insertion_sort(unordered_list)
   return unordered_list


print(insertion_sort(unordered_list := [6, 5, 8, 0, 1, 9, 4, 3, 1, 2, 7]))