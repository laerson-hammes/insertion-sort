def sortList(unorderedList):
   for index, _ in enumerate(unordered_list):
      if index + 1 < len(unordered_list):
         if unordered_list[index] > unordered_list[index + 1]:
            nextItem = unordered_list[index + 1]
            unordered_list[index + 1] = unordered_list[index]
            unordered_list[index] = nextItem
            sortList(unordered_list)
   
   return unordered_list


unordered_list = [6, 5, 8, 0, 1, 9, 4, 3, 2, 7]
endList = sortList(unordered_list)
print(endList)