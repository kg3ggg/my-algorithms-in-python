# -------------------------------------------------
# Алгоритм Прима поиска минимального остова графа
# -------------------------------------------------
import math


def get_min(_ways, _ramotrin_peaks):
    p_one = (math.inf, -1, -1)
    for p in _ramotrin_peaks:
        _edge_min = min(_ways, key=lambda x: x[0] if (x[1] == p or x[2] == p) and (x[1] not in _ramotrin_peaks or x[2] not in _ramotrin_peaks) else math.inf)
        if p_one[0] > _edge_min[0]:
            p_one = _edge_min

    return p_one


# список ребер графа (длина, вершина 1, вершина 2)
# первое значение возвращается, если нет минимальных ребер
ways = [(math.inf, -1, -1), (13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
        (26, 2, 3), (19, 2, 5), (30, 3, 4), (22, 4, 6)]

peaks = 6     # число вершин в графе
ramotrin_peaks = {1}   # множество соединенных вершин
res = []    # список ребер остова

while len(ramotrin_peaks) < peaks:
    edge_min = get_min(ways, ramotrin_peaks)       # ребро с минимальным весом
    if edge_min[0] == math.inf:    # если ребер нет, то остов построен
        break

    res.append(edge_min)             # добавляем ребро в остов
    ramotrin_peaks.add(edge_min[1])             # добавляем вершины в множество U
    ramotrin_peaks.add(edge_min[2])

print(res)
