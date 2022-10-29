def shell_sort(arr):
    n = len(arr)
    div = 2
    gap = n//div
    while gap > 0:
      index_to_delete = []
      for i in range(gap, n):
        temp = arr[i]
        j = i
        while j >= gap and arr[j-gap] >= temp:
            if arr[j-gap] == temp:
                index_to_delete.append(j)
            arr[j] = arr[j-gap]
            j -= gap
        arr[j] = temp
      index_to_delete=list(set(index_to_delete))
      index_to_delete.sort()
      if index_to_delete:
          for i in index_to_delete[-1::-1]:
              del arr[i]
      div *= 2
      n = len(arr)
      gap = n//div

if __name__ == '__main__':
    elements = [8, 12, 1, 3, 5]

    print(f'Given unsorted list: {elements}')
    shell_sort(elements)
    print(f'List after Sorting : {elements}')

# 5/2 =2.5= 2
# 1era vuelta
# 8 < 1   no  [8, 12, 1, 3, 5]
# 12 < 3  no  [1, 12, 8, 3, 5]
# 8 < 5  no   [1, 3, 8, 12, 5]
# 2da vuelta
# 2/2=1
# 1 < 3 si    [1, 3, 5, 12, 8]
# 3 < 5 si    [1, 3, 5, 12, 8]
# 5 < 12 si   [1, 3, 5, 12, 8]
# 12 < 8 no   [1, 3, 5, 12, 8]
# [1, 3, 5, 8, 12]
