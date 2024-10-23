

def find_solution_roots(a, b, c):
    return solution(a, b, c)
def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    discr_count = b ** 2 - 4 * a * c
    return discr_count

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    if discriminant(a, b, c) < 0:
        return 'корней нет'
    elif discriminant(a, b, c) == 0:
        return ((-b /2) + (discriminant(a, b, c) ** 0.5)) / a
    else:
        return ((-b + (discriminant(a, b, c) ** 0.5)) / (2 * a)), (-b - discriminant(a, b, c) ** 0.5) / (2 * a)


def ssd_models_checker(models: list, available: list, manufacturers: list):
    repair_count = 0  # количество дисков, которые купит сисадмин
    ssds = []  # модели дисков из списка models, которые купит сисадмин
    # код вашего решения ниже:
    for ssd_model, available_status in zip(models, available):
        for manufacturer in manufacturers:
            if available_status == 1 and manufacturer in ssd_model:
                repair_count += 1
                ssds.append(ssd_model)

    return ssds, repair_count


def find_palindroms(phrases: list):
    result = [] # список палиндромов
    for phrase in phrases: # пройдите циклом по всем фразам
        phrase_changed = phrase.replace(' ', '')
        if phrase_changed == phrase_changed[::-1]: # сравните фразу с ней же, развернутой наоборот (через [::-1])
           result.append(phrase)
    return result
