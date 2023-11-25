# def triple(value):
#     return 3*value

# def tripleStuff(a_list):
    # new_seq = map(triple=>#function, a_list=>#argument)
#     mapคือกระบวนการที่นำfuntionกับargumentมาทำการiterate
#     return list(new_seq)

# def quadrupleStuff(a_list):
#     new_seq = map(lambda value: 4*value, a_list)
#     return list(new_seq)

# things = [2, 5, 9]
# things3 = tripleStuff(things)
# print(things3)
# things4 = quadrupleStuff(things)
# print(things4)
# def d(q):
#     for i in q:
#         q.append(i)
#     return q
# def f(x):
#     for i in range(len(x)):
#         if x[i] is list:
#             x[i]=map(d,x[i])
#         else:
#             x[i]=x[i]*2
#     return x
# lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
# greeting_doubled=f(lst)
# print(greeting_doubled) 
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
filter_testing=filter(lambda word:"w" in word ,lst_check)
print(list(filter_testing))