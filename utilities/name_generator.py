
category_list = ['C','P','N','S']
weeks = ['W3','W4','W5','W6']

# for week in weeks: 
#     for cat in category_list:
#         for i in range(1,6):
#             for j in range(1,4):
#                 print(f'{cat}{i}{week},{cat}{week},{j},,,,')

for week in weeks:
    for cat in category_list:
        for i in range(1,6):
            print(f'{cat}{i}{week}')