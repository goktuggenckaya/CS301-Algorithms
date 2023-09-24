import random

graph0= [[1,[2,3]],[2,[1,3]],[3,[1,2,4]],[4,[3,5]], [5,[4]]]
graph1 = [[1, [2, 3, 4]], [2, [1]], [3, [1, 4]], [4, [1, 3]]]
graph2 = [[1, [4, 5]], [2, [3, 4]], [3, [2, 5, 6, 7]], [4, [1, 2]], [5, [1, 3]], [6, [3, 7]], [7, [3, 6]]]
graph3 = [[1, [2, 3, 5, 6]], [2, [1, 3, 4, 6]], [3, [1, 2, 5]], [4, [2, 5, 6]], [5, [1, 3, 4]], [6, [1, 2, 4]]]
graph4 = [[1, []], [2, []], [3, []], [4, []]]

def Clique(graph):
    graphDict = dict()
    vertex = []
    for i in graph:
        graphDict[i[0]] = i[1]
        vertex.append(i[0])
    subsets = []
    x = len(vertex)
    for i in range(1, 1 << x):
        subsets.append([vertex[j] for j in range(x) if (i & (1 << j))])
    Cli = []
    for i in subsets:
        appen = True
        g = len(i)
        subvertex = []
        for j in i:
            subvertex.append(j)
        for k in subvertex:
            for l in subvertex:
                if k != l and l not in graphDict[k]:
                    appen = False
        if appen == True:
            Cli.append(i)
    ans = len(vertex)
    subsets1 = []
    x = len(Cli)
    for i in range(1, 1 << x):
        subsets1.append([Cli[j] for j in range(x) if (i & (1 << j))])
    ma = len(vertex) + 1
    gen_ans = []
    for i in subsets1:
        cont = 0
        d = 1
        ans = []
        a = []
        for j in i:
            for k in j:
                if k in a:
                    d = 0
                    break
                a.append(k)
            ans.append(j)
            cont += 1
        if d == 1 and len(a) == len(vertex):
            if cont < ma:
                ma = cont
                gen_ans = ans
    return (ma, gen_ans)

def randomGraph():
    num = random.randint(1, 7)
    A = []
    for i in range(1, num):
        for j in range(i + 1, num + 1):
            A.append((i, j))
    N = random.randint(0, len(A))
    edgeList = []
    for i in range(N):
        edge = random.choice(A)
        edgeList.append(edge)
        A.remove(edge)
    graph = []
    for i in range(num + 1):
        B = []
        for j in edgeList:
            if i == j[0]:
                B.append(j[1])
            elif i == j[1]:
                B.append(j[0])
        graph.append([i, B])
    return graph

