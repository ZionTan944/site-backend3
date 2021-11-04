def merge_sort(list):
    # 1. Store the length of the list
    list_length = len(list)

    # 2. List with length less than is already sorted
    if list_length == 1:
        return list

    # 3. Identify the list midpoint and partition the list into a left_partition and a right_partition
    mid_point = list_length // 2

    # 4. To ensure all partitions are broken down into their individual components,
    # the merge_sort function is called and a partitioned portion of the list is passed as a parameter
    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    # 5. The merge_sort function returns a list composed of a sorted left and right partition.
    return merge(left_partition, right_partition)


# 6. takes in two lists and returns a sorted list made up of the content within the two lists
def merge(left, right):
    # 7. Initialize an empty list output that will be populated with sorted elements.
    # Initialize two variables i and j which are used pointers when iterating through the lists.
    output = []
    i = j = 0

    # 8. Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while i < len(left) and j < len(right):
        # 9. Compare the elements at every position of both lists during each iteration
        #left{i] 63 18 73  64 18 59
        if left[i].Points> right[j].Points :
            output.append(left[i])
            i += 1
        elif left[i].Points < right[j].Points :
            output.append(right[j])
            j += 1
        elif left[i].Points  == right[j].Points  and left[i].GoalDiff  > right[j].GoalDiff :
            output.append(left[i])
            i += 1
        elif left[i].Points  == right[j].Points  and left[i].GoalDiff  < right[j].GoalDiff :
            output.append(right[j])
            j += 1
        elif left[i].GoalDiff == right[j].GoalDiff and left[i].GoalsFor > right[j].GoalsFor:
            output.append(left[i])
            i += 1
        elif left[i].GoalDiff == right[j].GoalDiff and left[i].GoalsFor < right[j].GoalsFor:
            output.append(right[j])
            j += 1
        else:
            output.append(right[j])
            j += 1
    # 11. The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left[i:])
    output.extend(right[j:])

    return output



unsorted_list = [{'TeamInt': 'LIV', 'GP': 38, 'Wins': 19, 'Draws': 6, 'Losses': 13, 'GF': 73, 'GA': 55, 'GD': 18, 'Points': 63, 'Form': 20.9}, {'TeamInt': 'ARS', 'GP': 
38, 'Wins': 19, 'Draws': 6, 'Losses': 13, 'GF': 73, 'GA': 61, 'GD': 12, 'Points': 63, 'Form': 36}, {'TeamInt': 'LEI', 'GP': 38, 'Wins': 17, 'Draws': 8, 
'Losses': 13, 'GF': 71, 'GA': 56, 'GD': 15, 'Points': 59, 'Form': 44}, {'TeamInt': 'SHU', 'GP': 38, 'Wins': 14, 'Draws': 5, 'Losses': 19, 'GF': 53, 'GA': 72, 'GD': -19, 'Points': 47, 'Form': 23}, {'TeamInt': 'WBA', 'GP': 38, 'Wins': 8, 'Draws': 5, 'Losses': 25, 'GF': 49, 'GA': 79, 'GD': -30, 'Points': 29, 'Form': 20}, {'TeamInt': 'CRY', 'GP': 38, 'Wins': 18, 'Draws': 4, 'Losses': 16, 'GF': 66, 'GA': 71, 'GD': -5, 'Points': 58, 'Form': 47}, {'TeamInt': 
'CHE', 'GP': 38, 'Wins': 17, 'Draws': 13, 'Losses': 8, 'GF': 83, 'GA': 52, 'GD': 31, 'Points': 64, 'Form': 45.599999999999994}, {'TeamInt': 'WHU', 'GP': 38, 'Wins': 17, 'Draws': 9, 'Losses': 12, 'GF': 69, 'GA': 60, 'GD': 9, 'Points': 60, 'Form': 27.549999999999997}, {'TeamInt': 'SOU', 'GP': 38, 'Wins': 
12, 'Draws': 10, 'Losses': 16, 'GF': 55, 'GA': 66, 'GD': -11, 'Points': 46, 
'Form': 20}, {'TeamInt': 'FUL', 'GP': 38, 'Wins': 5, 'Draws': 7, 'Losses': 26, 'GF': 44, 'GA': 95, 'GD': -51, 'Points': 22, 'Form': 21.849999999999998}, {'TeamInt': 'BRI', 'GP': 38, 'Wins': 10, 'Draws': 5, 'Losses': 23, 'GF': 49, 'GA': 77, 'GD': -28, 'Points': 35, 'Form': 20}, {'TeamInt': 'LEE', 'GP': 38, 'Wins': 12, 'Draws': 7, 'Losses': 19, 'GF': 58, 'GA': 72, 'GD': -14, 'Points': 43, 'Form': 26}, {'TeamInt': 'TOT', 'GP': 38, 'Wins': 18, 'Draws': 10, 'Losses': 10, 'GF': 59, 'GA': 41, 'GD': 18, 'Points': 64, 'Form': 28}, {'TeamInt': 'AVL', 'GP': 38, 'Wins': 9, 'Draws': 8, 'Losses': 21, 'GF': 47, 'GA': 75, 'GD': -28, 'Points': 35, 'Form': 20}, {'TeamInt': 'NEW', 'GP': 38, 'Wins': 17, 'Draws': 7, 'Losses': 14, 'GF': 63, 'GA': 64, 'GD': -1, 'Points': 58, 'Form': 20}, {'TeamInt': 'MCI', 'GP': 38, 'Wins': 20, 'Draws': 9, 'Losses': 9, 'GF': 75, 'GA': 45, 'GD': 30, 'Points': 69, 'Form': 52.25}, {'TeamInt': 'EVE', 'GP': 38, 'Wins': 23, 'Draws': 6, 'Losses': 9, 'GF': 75, 'GA': 49, 
'GD': 26, 'Points': 75, 'Form': 100.69999999999999}, {'TeamInt': 'BUR', 'GP': 38, 'Wins': 8, 'Draws': 6, 'Losses': 24, 'GF': 39, 'GA': 81, 'GD': -42, 'Points': 30, 'Form': 20}, {'TeamInt': 'MUN', 'GP': 38, 'Wins': 26, 'Draws': 6, 'Losses': 6, 'GF': 93, 'GA': 41, 'GD': 52, 'Points': 84, 'Form': 142.5}, {'TeamInt': 'WOL', 'GP': 38, 'Wins': 20, 'Draws': 5, 'Losses': 13, 'GF': 74, 
'GA': 56, 'GD': 18, 'Points': 65, 'Form': 26.599999999999998}]
def run_merge_sort(arr):
##    print(unsorted_list)
    sorted_list = merge_sort(arr)
    # for i in sorted_list:
    #    print(i.Points, i["GD"],i["GF"])
    return sorted_list
# run_merge_sort(unsorted_list)
