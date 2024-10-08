def couting_elements(list_version):
    result = []
    for id, version in list_version:
        found = False
        for item in result:
            if item[0] == id and item[1] == version:
                item[2] += 1
                found = True
                break
        if not found:
            result.append([id, version, 1])

    return result


# Исходные данные
list_version = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]

# Вывод
result = couting_elements(list_version)
print(result)
