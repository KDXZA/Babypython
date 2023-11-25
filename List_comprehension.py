# grammar_List_Comprehension=>map_function
# [<transformer_expression>for <var> in <seq>]
#       2                             1
# l=[2,4,6]
# new=[x*2 for x in l]
# new=map(lambda x:x*2,l)
# print(list(new))

# -------------------
# grammar_List_Comprehension=>filter_function
# [<transformer_expression>for <var> in <seq> if <filtration_expression>]
#          3                     1                     2
def keep_evens(nums):
    new_list=[num for num in nums if num % 2 ==0]
    return new_list

def keep_evens(nums):
    new_list=filter(lambda x:x % 2 ==0,nums)
    return list(new_list)


print(keep_evens([3,4,6,7,0,1]))