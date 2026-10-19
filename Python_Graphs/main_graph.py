graph_1 = [
	[0 , 4 , 0 , 0, 7, 0, 0],
	[4 , 0 , 1 , 8, 8, 0, 0],
	[0 , 1 , 0 , 0, 0, 3, 0],
	[0 , 8 , 0 , 0, 13, 16, 0],
	[7 , 8 , 0 , 13, 0, 0, 0],
	[2 , 0 , 3 , 16, 0, 0, 1],
	[0 , 0 , 0 , 0, 0, 1, 0],
]
#2.количество вершин 
graph_l = len(graph_1)
print(f"Количество вершин: {graph_l}")

#3.количество вершин , у которых степень 3
vertices_3 = 0

for row in graph_1:
	degree = 0
	for weight in row:
		if weight > 0:
			degree += 1

	if degree == 3:
		vertices_3 += 1
print(f"Количество вершин степень которых три:{vertices_3}")

#4. Количество ребер

count = 0

for i in range(len(graph_1)):
	for j in range(len(graph_1[i])):
		if graph_1[i][j] > 0:
			count += 1
edges_count = count // 2
print(f"Количество ребер:{edges_count}")

#5.Cумма весов всех ребер
graph_edges = sum(sum(row) for row in graph_1) // 2
print(f"Сумма весов всех ребер: {graph_edges}")

