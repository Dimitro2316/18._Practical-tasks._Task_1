import networkx as nx

# Создаем ориентированный граф
G = nx.DiGraph()

# Добавляем ребра
G.add_edges_from([(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 1)])

cycles = list(nx.simple_cycles(G))

print("Найденные простые циклы:")
for cycle in cycles:
    print(cycle)






