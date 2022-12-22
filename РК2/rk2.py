# Вариант 29 Фруктин А.Е. РТ5-31Б

from operator import itemgetter
import statistics

class Kafedra:
    """Кафедра"""

    def __init__(self, id, name, count_sotrud, fac_id):
        self.id = id
        self.name = name
        self.sotr = count_sotrud
        self.fac_id = fac_id


class Facultet:
    """Факультет"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class KafFac:
    """
       'Кафедры факультетов' для реализации
       связи многие-ко-многим
       """

    def __init__(self, id_kaf, id_fac):
        self.kaf_id = id_kaf
        self.fac_id = id_fac

#Кафедры
Kafedres = [
    Kafedra(1,'ИУ1-Системы автоматического управления',12, 1),
    Kafedra(2,'ИУ2 - Приборы и системы ориентации, стабилизации и навигации',15, 1),
    Kafedra(3,'Э9- Экология и промышленная безопасность',10, 3),
    Kafedra(4,'ИБМ5 - Финансы',11, 2),
    Kafedra(5,'ИБМ6 - Предпринимательство и внешнеэкономическая деятельность',22, 2),

]
Facultets = [
    Facultet(1,"Факультет: Информатика, искусственный интеллект и системы управления"),
    Facultet(2, "Факультет: Инженерный бизнес и менеджмент"),
    Facultet(3, "Факультет: Энергомашиностроение"),
    Facultet(11,"Факультет: Информатика, искусственный интеллект и системы управления(другие кафедры)"),
    Facultet(22, "Факультет: Инженерный бизнес и менеджмент(другие кафедры)"),
    Facultet(33, "Факультет: Энергомашиностроение(другие кафедры)"),
]

Kaf_Fac = [
    KafFac(1,1),
    KafFac(2,1),
    KafFac(3,3),
    KafFac(4,2),
    KafFac(5,2),
    KafFac(1,11),
    KafFac(2,11),
    KafFac(3,33),
    KafFac(4,22),
    KafFac(5,22),




]
# Соединение данных один-ко-многим
def one_to_many(Facultets,Kafedres):
    return [(kaf.name, kaf.sotr, fac.name)
               for fac in Facultets
               for kaf in Kafedres
               if kaf.fac_id == fac.id]

def e1(Facultets, Kafedres):
        print('Задание E1')
        res_1 = {}
        for fac in Facultets:
            if 'Факультет' in fac.name:
                fac_kafs = list(filter(lambda i: i[2] == fac.name, one_to_many(Facultets,Kafedres)))
                fac_kafs_names = [x for x, _, _ in fac_kafs]
                res_1[fac.name] = fac_kafs_names

        print(list(res_1))
        return list(res_1)
def e2(Facultets, Kafedres):
    print('Задание E2')
    res_2_unsorted = []
    for fac in Facultets:
        fac_kaf = list(filter(lambda i: i[2] == fac.name, one_to_many(Facultets,Kafedres)))
        if len(fac_kaf) > 0:

            kaf_count = [sotr for _, sotr, _ in fac_kaf]
            fac_sotr_mean = statistics.mean(kaf_count)
            res_2_unsorted.append((fac.name, fac_sotr_mean))

    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(list(res_2))
    return list(res_2)



if __name__ == '__main__':
    e1(Facultets, Kafedres)
    e2(Facultets,Kafedres)