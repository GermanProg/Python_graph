graph_3 = [
	[0 , 20 , 0 , 0, 0, 34, 0, 0, 9],
	[20 , 0 , 11 , 0, 0, 0, 3, 0, 0],
	[0 , 11 , 0 , 7, 0, 0, 3, 0, 0],
	[0 , 0 , 7 , 0, 3, 0, 0, 0, 9],
	[0 , 0 , 0 , 3, 0, 26, 0, 0, 5],
	[34 , 0 , 0 , 0, 24, 0, 0, 0, 5],
	[0 , 3 , 3 , 0, 0, 0, 0, 1, 0],
	[0 , 0 , 0 , 0, 0, 0, 1, 0, 1],
	[9 , 0 , 0 , 9, 5, 5, 0, 1, 0]
]
#2.количество вершин 
graph_l = len(graph_3)
print(f"Количество вершин: {graph_l}")

#3.количество вершин , у которых степень 3
vertices_3 = 0

for row in graph_3:
	degree = 0
	for weight in row:
		if weight > 0:
			degree += 1

	if degree == 3:
		vertices_3 += 1
print(f"Количество вершин степень которых три:{vertices_3}")

#4. Количество ребер

count = 0

for i in range(len(graph_3)):
	for j in range(len(graph_3[i])):
		if graph_3[i][j] > 0:
			count += 1
edges_count = count // 2
print(f"Количество ребер:{edges_count}")

#5.Cумма весов всех ребер
graph_edges = sum(sum(row) for row in graph_3) // 2
print(f"Сумма весов всех ребер: {graph_edges}")
#6 Ближайшие к F
n = 0
for i in graph_3[5]:
	if i > 0:
		n += 1
print(f"Ближайшие к F:{n}")