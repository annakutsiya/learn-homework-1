# school = [{'class':'1a', 'scores': [4,5,5,3]},{'class':'2a', 'scores': [3,5,5,3]}, {'class':'3a', 'scores': [4,2,3,3]}, {'class':'4a', 'scores': [2,2,5,3]}, {'class':'5a', 'scores': [5,5,5,4]}, {'class':'6a', 'scores': [3,3,5,3]}]

# # for i in school:
# #     key=[k for k in i.keys()][1]
# # print(key)
# score_sum_all=0
# len_list_all=0
# list_scores=[]
# for i in school:
#     key=[k for k in i.keys()][1]
#     for ls in i.get(key):
#         print(ls)
# #         score_sum_all+=ls
# #         len_list_all+=1
# #         score_avg_all = score_sum_all/len_list_all
# #     list_scores.append(i.get('scores'))
    
# #     score_avg_list=[]
# #     for elem in list_scores:
# #         score_sum =0
# #         len_list=0
# #         for l in elem:
# #             len_list +=1
# #             score_sum+=l
# #             score_avg = score_sum/len_list
            
# #         score_avg_list.append(score_avg)
# # print(score_avg_list)
# # print(len_list)
# questions_and_answers = {'Как дела?':'Нормально','Что делаешь?':'Учусь', 'Что ты ел на завтрак?':'Сырники','Какой твой любимый напиток?':'Чай'}
# for i in questions_and_answers.keys():
#     print(i)      
def cut_cake(people):
    try:
        parts=1/people
        print(f'Каждый получит {parts} пирога')
    except ZeroDivisionError:
        print('Не можем делить на 0')


cut_cake(0)

