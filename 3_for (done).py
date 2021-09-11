"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school = [{'class':'1a', 'scores': [4,5,5,3]},{'class':'2a', 'scores': [3,5,5,3]}, {'class':'3a', 'scores': [4,2,3,3]}, {'class':'4a', 'scores': [2,2,5,3]}, {'class':'5a', 'scores': [5,5,5,4]}, {'class':'6a', 'scores': [3,3,5,3]}]
def main(lst):
      score_sum_all=0
      score_sum_all=0
      len_list_all=0
      list_scores=[]
      for i in lst:
            key=[k for k in i.keys()][1]
            for ls in i.get(key):
                score_sum_all+=ls
                len_list_all+=1
                score_avg_all = score_sum_all/len_list_all
            list_scores.append(i.get(key))
    
            score_avg_list=[]
            for elem in list_scores:
                score_sum =0
                len_list=0
                for l in elem:
                    len_list +=1
                    score_sum+=l
                    score_avg = score_sum/len_list
            
                score_avg_list.append(score_avg)
      return score_avg_all, score_avg_list
      
print(main(school))


      
 
"""
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
#     pass
    
# if __name__ == "__main__":
#     main()
