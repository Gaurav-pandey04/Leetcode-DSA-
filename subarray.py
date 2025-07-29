# n = 5
# conflictingPairs = [[1,2],[2,5],[3,5]]

# len_subarray = (n*(n+1))/2

# for i, ele in enumerate(conflictingPairs):
#     a = conflictingPairs[i][0]
#     b = conflictingPairs[i][1]
#     if a > b: 
#         conflictingPairs[i] = b, a
    
# print(conflictingPairs)

# # max_score = 0
# # for a, b in conflictingPairs:
# #     result = len_subarray - a
# #     max_score = max(max_score, result)

# # print(int(max_score))

# minimum = []
# maximum = []
# minimum_index = 0
# for i in range(1, len(conflictingPairs)):
#     minimum = [conflictingPairs[0][0], conflictingPairs[0][1]]
#     if minimum[1]-minimum[0] > conflictingPairs[i][0]-conflictingPairs[i][1]:
#         minimum.clear()
#         minimum.append(conflictingPairs[i][0])
#         minimum.append(conflictingPairs[i][1])
#         minimum_index = i
#         continue
#     if len(conflictingPairs) > i and minimum[0] > conflictingPairs[i][0]:
#         minimum.clear()
#         minimum.append(conflictingPairs[i][0])
#         minimum.append(conflictingPairs[i][1])
#         minimum_index = i

# print(minimum_index)

# conflictingPairs.pop(minimum_index)

# print(conflictingPairs)

# # if len(conflictingPairs) == 1:
# #     maximum = [conflictingPairs[0][0], conflictingPairs[0][1]]

# # else:
# #     for i in range(1, len(conflictingPairs)):
# #         maximum = [conflictingPairs[0][0], conflictingPairs[0][1]]
# #         if len(conflictingPairs) > i and minimum[0] < conflictingPairs[i][0]:
# #             maximum.clear()
# #             maximum.append(conflictingPairs[i][0])
# #             maximum.append(conflictingPairs[i][1])

# # print(maximum)

# # result = len_subarray - maximum[0]
# # print(int(result))

n=5
bMin1 = [2**31 - 1] * (n + 1)
print(bMin1)