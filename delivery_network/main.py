from graph import Graph, graph_from_file


data_path = "input/"
file_name = "network.01.in"

import time
import numpy.random


def time_test(g,n):
    T=[]
    for _ in range(n):
        src=numpy.random.randint(1,len(g.graph))
        dest=numpy.random.randint(1,len(g.graph))
        t1=time.perf_counter()
        g.min_power(src,dest)
        t2=time.perf_counter()
        T.append(t2-t1)
    return sum(T)/len(T)

def parcours(g,u,Visited):
    Visited.append(u)
    for i in g.graph[u]:
        if not i[0] in Visited:
            parcours(g,i[0],Visited)


def Trajet(g,visited,path,P,SRC,DEST,T):
    S=0
    if SRC==DEST:
        for i in range(len(path)-1):
            for j in g.graph[path[i]]:
                if j[0]==path[i+1]:
                    S+=j[1]
        if S<=P:
            return T.append([i for i in path])
    if len(T)==0:
        visited.append(SRC)
        for i in g.graph[SRC]:
            if not i[0] in visited:
                path.append(i[0])
                Trajet(g,visited,path,P,i[0],DEST,T)
                path.pop()
        visited.pop()


def Union(a,b,P):
    A=Find(P,a)
    B=Find(P,b)
    if A!=B:
        P[A-1]=B

def Find(P,i):
    if P[i-1]==i:
        return i
    return Find(P,P[i-1])

def kruskal(g):
    T=[]
    P=[i for i in range(1,len(g.graph)+1)]
    Q=[]
    for i in range(1,len(g.graph)+1):
        for j in range(len(g.graph[i])):
            T.append([i,g.graph[i][j][0],g.graph[i][j][1]])
    T.sort(key=lambda u:u[2])
    c1,c2=0,0
    while c2 < len(P) - 1:
        c1 = c1 + 1
        p = Find(P, T[c1][0]-1)
        q = Find(P, T[c1][1]-1)
        if p != q:
            c2 = c2 + 1
            Q.append(T[c1])
            Union(p,q,P)
    G=Graph([i for i in range(1,len(Q)+1)])
    for i in range(len(Q)):
        G.add_edge(Q[i][0],Q[i][1],Q[i][2])
    return G

def power_min_2(g,src,dest):
    G=kruskal(g)
    h=G.min_power(src,dest)
    return h
