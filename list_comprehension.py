# number = [1,3,5]
# doubled = [x * 2 for x in number]
# # for num in number:
# #     doubled.append( num * 2)
# print(list(doubled))


friends = ['Ramesh', 'Suresh', 'Samantha', 'Jen']

starts_s = [f for f in friends if f.startswith('S')]

# for f in friends:
#     if f.startswith('S'):
#         starts_s.append(f)
print(list(starts_s))
