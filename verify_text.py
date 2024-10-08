def verify_text(test_text, list_keys):
    if test_text.count('{') != test_text.count('}'):
        return "Ошибка: несоответствие количества открывающих и закрывающих скобок"
    start = 0
    while True:
        start = test_text.find('{', start)
        if start == -1:
            break
        end = test_text.find('}', start)
        if end == -1:
            return "Ошибка: незакрытая фигурная скобка"
        key = test_text[start + 1:end]
        if key not in list_keys:
            return f"Ошибка: некорректный ключ '{key}'"
        start = end + 1
    return "Все проверки пройдены"


# Исходные данные
test_text = '''{name}, ваша запись изменена:
️{day_month} в {start_time}
{master}
Услуги:
{services}
управление записью {record_link}'''

list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']

# Вывод
result = verify_text(test_text, list_keys)
print(result)
