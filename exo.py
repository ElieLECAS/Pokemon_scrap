# def solution(number):
#     l = [x for x in range(1,number)]
#     multiple_3 = []
#     multiple_5 = []    

#     for i in l:
#         if i % 3 == 0:
#             multiple_3.append(i)
#             # summ3 = sum(multiple_3)
            
#         if i % 5 == 0:
#             multiple_5.append(i)
#             # summ5 = sum(multiple_5)
            
#     multiple = set(multiple_3 + multiple_5)
#     summ = sum(multiple)

#     print(summ)

# solution(20)

def solution(number):
    l = [x for x in range(1,number)]
    multiple = []
      

    for i in l:
        if i % 3 == 0 or i % 5 == 0:
            multiple.append(i)            
    summ = sum(multiple)

    print(summ)

solution(20)