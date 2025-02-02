Тестовое задание

1.Проверка на корректность заполнения поля.
Задача:
Необходимо провести верификацию введенных пользователем данных. Проверяются ключи на предмет соответствия написания с
определенными в list_keys значениями, а также наличие открывающих и закрывающих скобок.
Исходные данные:
Test_text = '''{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}'''
list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']
Пример:
{name} – корректно,
{Name} – ошибка,
{nme} – ошибка,
{name – ошибка
Результат:
На выходе метод должен возвращать тест, если все проверки пройдены, ошибку, если где-то есть некорректные данные.

2.Подсчет элементов
Задача:
Сгрупировать по уникальности пары id, version в list_version
Исходные данные:
Имеется список содержащий пары значений id, version, минимум 30 элементов
list_version = [[id, version], [id, version], …]
id: str
version: int
Пример:
[[‘665587’, 2], [‘669532’, 1], [‘669537’, 2], [‘669532’, 1], [‘665587’, 1]]
Результат:
Набор сгруппированных значений в формате: [[id, version, count], …],
Где count – количество одинаковых пар [id, version]
Для примера выход работы метода будет:
[[‘665587’, 2, 1], [‘669532’, 1, 2], [‘669537’, 2, 1], [‘665587’, 1, 1]]

3.Поиск разницы между 2мя json
Задача:
Найти различия между 2мя json. Если различающиеся параметры входят в diff_list, вывести различие. Иными словами, нужно
отловить изменение определенных параметров и вывести значение что изменилось и на что. Набор ключей в обоих json
идентичный, различаются лишь значения
Исходные данные:
json = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create', 'data': {'id':
11111111, 'company_id': 111111, '
services': [{'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], '
goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'}, 'client': {'id': 130345867, 'name': 'Клиент', '
phone': '79111111111', 'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '
2022-01-25T11:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 0, 'confirmed':
1, 'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443, '
deleted': False, 'paid_full': 0, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '
2022-01-22 10:00:00'}}
diff_list = [‘services’, ‘staff’, ‘datetime’]
Пример:
Json_old = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create', 'data': {'id':
11111111, 'company_id': 111111, '
services': [{'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], '
goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'}, 'client': {'id': 130345867, 'name': 'Клиент', '
phone': '79111111111', 'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '
2022-01-25T11:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 0, 'confirmed':
1, 'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443, '
deleted': False, 'paid_full': 0, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '
2022-01-22 10:00:00'}}
Json_new = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create', 'data': {'id':
11111111, 'company_id': 111111, '
services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], '
goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'}, 'client': {'id': 130345867, 'name': 'Клиент', '
phone': '79111111111', 'success_visits_count': 2, 'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '
2022-01-25T13:00:00+03:00', 'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 2, 'confirmed':
1, 'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049, 'created_user_id': 10573443, '
deleted': False, 'paid_full': 1, 'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '
2022-01-22 10:00:00'}}
Результат:
Словарь {параметр: новое_значение, ….}
Для примера выход работы метода будет:
Result =
{'services': [{'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}], '
datetime': '2022-01-25T13:00:00+03:00'}
Обратите внимание, что в result представлены не все изменившиеся поля, а лишь те, что объявлены в diff_list.

4.Очистка БД
Задача:
Предложите систему для очистки данных из MongoDB по истечению заданного времени.
Пример:
Есть документ, который необходимо удалить по истечению 24ч.
Схема кода
Задача:

5.Предложите архитектуру обработки входящих веб хуков с использованием одного endpoint.
Пример:
Вебхуки идут на адрес ‘/Datalore’, полученный хук имеет поле ‘function’, значение которого соответствует выполняемой
функции. Необходимо на основании полученных данных сделать роутинг для вызова конкретной функции.

1-я задача отображена в файле verify_text
2-я задача отображена в файле couting_elements
3-я задача отображена в файле differences_json
4-я задача отображена в файле delete_24для запуска данной задачи необходимо установить зависимости из файла
pyproject.toml

5-я задача отображена в файлеscheme_cod для запуска данной задачи необходимо установить зависимости из файла
pyproject.toml и выполнить команду uvicorn scheme_cod:app --reload
проверить работоспособность можно через Postman