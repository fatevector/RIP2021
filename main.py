# Предметная область 10: 
# Браузер - компьютер
# Запросы Д:
#   1.«Браузер» и «Компьютер» связаны соотношением один-ко-многим.
#     Выведите список всех браузеров, у которых название заканчивается на "x", и названия компьютеров с этими браузерами.
#   2.«Браузер» и «Компьютер» связаны соотношением один-ко-многим.
#     Выведите список компьютеров со средней датой публикации браузеров в каждом компьютере, отсортированный по средней дате публикации.
#     (отдельной функции вычисления среднего значения в Python нет, нужно использовать комбинацию функций вычисления суммы и количества значений).
#   3. «Браузер» и «Компьютер» связаны соотношением многие-ко-многим.
#     Выведите список всех компьютеров, у которых название начинается с буквы «А», и список их браузеров.

from operator import itemgetter
from store.computer import computers
from store.browser import browsers
from store.browser_computer import computers_with_browsers

def main():
  print("\n \\/ \\/ \\/ \\/ \\/ \\/ \n")

  # Соединение данных один-ко-многим 
  browsers_join_computers = [{'browsers': o, 'computers': c}
    for o in browsers
    for c in computers 
    if o.computer_id == c.id
  ]

  print('Задание Д-1')
  # Выведем id, name, publication_year таблицы "Браузер"
  # для записей с name, заканчивающимся на 'x'.
  # И выведем компьютеры с этими браузерами
  D1 = [(x['browsers'].id, x['browsers'].name, x['browsers'].publication_year, x['computers'].name)
    for x in browsers_join_computers
    if x['browsers'].name.endswith('x')
  ]
  for x in D1:
    print(x)
  

  print('\nЗадание Д-2')
  # Выведем имя компьютера, среднее по дате публикации браузеров этого компьютера
  # Сортируя по этому среднему

  # Заведем таблицу с накапливаемой суммой дат и количеством браузеров:
  computer_sum_count_dict = {}
  for b_computers_row in browsers_join_computers:
    computer_name = b_computers_row['computers'].name
    publication_year = b_computers_row['browsers'].publication_year

    if computer_name in computer_sum_count_dict:
      computer_sum_count_dict[computer_name]['sum'] = computer_sum_count_dict[computer_name]['sum'] + publication_year
      computer_sum_count_dict[computer_name]['count'] = computer_sum_count_dict[computer_name]['count'] + 1
    else:
      computer_sum_count_dict[computer_name] = {'sum': publication_year, 'count': 1}

  D2 = sorted(
    [(computer_name, computer_sum_count_dict[computer_name]['sum'] / computer_sum_count_dict[computer_name]['count'])
      for computer_name in computer_sum_count_dict
      if computer_sum_count_dict[computer_name]['count'] != 0
    ],
    key=itemgetter(1), reverse=True
  )
  for x in D2:
    print(x)

  print('\nЗадание Д-3')

  # Соединение данных многие-ко-многим
  many_to_many = [(c.name, co.computer_id, co.browser_id)
    for c in computers
        for co in computers_with_browsers 
            if c.id == co.computer_id]

  computers_with_browsers_table = [(browser.name, browser.publication_year, computer_name)
    for computer_name, computer_id, browser_id in many_to_many
        for browser in browsers if browser.id == browser_id]

  D3 = {}
  for computer in computers:
    if computer.name.startswith('A'):
        browsers_of_computer = list(filter(lambda i: i[2] == computer.name, computers_with_browsers_table))
        browsers_names = [x for x, _, _ in browsers_of_computer]
        D3[computer.name] = browsers_names
  for d in D3:
    print(d, ':', D3[d])
    
  print("\n /\\ /\\ /\\ /\\ /\\ /\\ \n")
 
if __name__ == '__main__':
  main()