import csv

def read_csv(filename: str):
    with open(filename, newline='') as f:
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
        return list(x[0] for x in reader)

#Фильтр среднее арифметическое. Однократная выборка
def one_sample():
    B = 30 # объём выборки для средних арифм. фильтров
    def calc(value):
        sum = 0 #переменная sum
        for _ in range(0, B):  # согласно объёму выборки
            sum += value #суммируем значения
        return (sum / B)
    return calc

#Фильтр среднее арифметическое. Растянутая выборка
def stret_sample():
    B = 10
    counter = 0 # счётчик
    prevResult = 0#хранит предыдущее готовое значение
    sum = 0

    def calc(value):
        nonlocal counter, prevResult,sum,B
        sum += value # суммируем новое значение
        counter+=1 # счётчик++
        if counter == B:
            prevResult = sum / B # считаем среднее
            sum = 0 # обнуляем сумму
            counter = 0 # сброс счётчика
        return prevResult
    return calc

# бегущее среднее арифметическое
def run_middle():
    B = 4 #объём выборки
    idx = 0 # индекс
    arrayV = [0] * B # массив

    def calc(value): # принимает новое значение
        nonlocal idx, arrayV
        arrayV[idx] = value # пишем каждый раз в новую ячейку
        idx += 1
        if idx >= B:
            idx = 0 # перезаписываем самое старое значение
        average = 0 #обнуляем среднее
        for i in range(0, B):
            average += arrayV[i] #суммируем
        return average / B #возвращаем
    return calc

# Бегущее среднее с адаптивным коэффициентом
def exp_run_average_adaptive():
    filVal = 0
    def calc(value):
        nonlocal filVal
        k = 0
        # резкость фильтра зависит от модуля разности значений
        if abs(value - filVal) > 1.5:
            k = 0.9
        else:
            k = 0.03
        filVal += (value - filVal) * k
        return filVal
    return calc

# Медианный фильтр. Для медианы 3-го порядка
def median():
    array = [0] * 3
    count = 0

    def calc(value):
        nonlocal array, count
        array[count] = value
        count += 1
        if count >= 3: count = 0
        a = array[0]
        b = array [1]
        c = array [2]
        middle = 0 #алгоритм для медианы на 3 значения
        if a <= b and a <= c:
            middle = b if b <= c else c
        else:
            if b <= a and b <= c:
                middle = a if a <= c else c
            else:
                middle = a if a <= b else b
        return middle
    
    return calc

# Фильтр Калмана
def kalman():
    # переменные для фильтра калмана
    varVolt = 0.25  # примерный шум измерений (рассчитывается)
    varProcess = 0.05 # скорость изменения значений 0.001-1
    Pc = 0.0
    G = 0.0
    P = 1.0
    Xp = 0.0
    Zp = 0.0
    Xe = 0.0

    # переменные для калмана
    def calc(value):  #функция фильтрации
        nonlocal varVolt, varProcess, Pc, G, P, Xp, Zp, Xe

        Pc = P + varProcess
        G = Pc / (Pc + varVolt)
        P = (1 - G) * Pc
        Xp = Xe
        Zp = Xp
        Xe = G * (value - Zp) + Xp # "фильтрованное" значение
        return(Xe)

    return calc