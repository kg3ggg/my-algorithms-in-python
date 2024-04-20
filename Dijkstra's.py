import math


def arg_min(impossible, viewed):
    amin = -1
    m = math.inf  # максимальное значение
    for i, t in enumerate(impossible):
        if t < m and i not in viewed:
            m = t
            amin = i

    return amin


ruad = ((0, 3, 1, 3, math.inf, math.inf),
        (3, 0, 4, math.inf, math.inf, math.inf),
        (1, 4, 0, math.inf, 7, 5),
        (3, math.inf, math.inf, 0, math.inf, 2),
        (math.inf, math.inf, 7, math.inf, 0, 4),
        (math.inf, math.inf, 5, 2, 4, 0))

NumberVertices = len(ruad)  # число вершин в графе
ImpossibleVertex = [math.inf]*NumberVertices   # последняя строка таблицы

vertex = 0       # стартовая вершина (нумерация с нуля)
ViewedVertex = {vertex}     # просмотренные вершины
ImpossibleVertex[vertex] = 0    # нулевой вес для стартовой вершины
M = [0]*NumberVertices   # оптимальные связи между вершинами

while vertex != -1:          # цикл, пока не просмотрим все вершины
    for j, dw in enumerate(ruad[vertex]):   # перебираем все связанные вершины с вершиной v
        if j not in ViewedVertex:           # если вершина еще не просмотрена
            w = ImpossibleVertex[vertex] + dw
            if w < ImpossibleVertex[j]:
                ImpossibleVertex[j] = w
                M[j] = vertex        # связываем вершину j с вершиной v

    vertex = arg_min(ImpossibleVertex, ViewedVertex)            # выбираем следующий узел с наименьшим весом
    if vertex >= 0:                    # выбрана очередная вершина
        ViewedVertex.add(vertex)                 # добавляем новую вершину в рассмотрение

print(ImpossibleVertex)

# формирование оптимального маршрута:


def shot_path(s, e):
    start = s
    end = e
    res = [end]
    while end != start:
        end = M[res[-1]]
        res.append(end)

    return res


print(shot_path(0, 4))