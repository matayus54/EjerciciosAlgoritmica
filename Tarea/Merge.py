
def merge_sort(arr):

    if len(arr)<=1: #constante
        return

    mid = len(arr)//2 # constante

    left_arr = arr[:mid] #constante
    right_arr = arr[mid:] # constante

    print(left_arr, right_arr) # constante

    merge_sort(left_arr) # lineal
    merge_sort(right_arr) # lineal

    left_index = 0 #constante
    right_index = 0 # constante
    arr_index = 0 # constante

    while left_index < len(left_arr) and right_index < len(right_arr): # cuadratico

        if left_arr[left_index] < right_arr[right_index]: #constante
            arr[arr_index] = left_arr[left_index] #constante
            left_index += 1

        else:
            arr[arr_index] = right_arr[right_index] #constante
            right_index += 1 #constante

        arr_index += 1 #constante

    if left_index < len(left_arr): #constante
        del arr[arr_index:] # constante
        arr += left_arr[left_index:] #constante

    elif right_index < len(right_arr): #constante
        del arr[arr_index:] # constante
        arr += right_arr[right_index:] #constante

    return arr # constante

arreglo = [8, 12, 1, 3, 5]
print(merge_sort(arreglo))

# 5/2=2 se divide por la mitad
#   [8, 12]     [1, 3, 5]     formamos 2 grupos
# [8]    [12]  [1]   [3, 5]   se halla el orden de cada grupo
# [1, 3, 5, 8, 12]            Se unen los grupos ordenados
