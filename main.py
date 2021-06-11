import math
import matplotlib.pyplot as plt

def graph(p):   #그래프 그리는 함수
    for i in p:
        plt.scatter(i[1],i[2])   #점찍기
        plt.annotate(i[0],xy=(i[1],i[2]))   #점에 설명 쓰기
    plt.xlim(0,)   #x축 범위 설정(0부터 표시)
    plt.ylim(0,)   #y축 범위 설정(0부터 표시)
    plt.grid()   #격자 표시

def knn(id,x,y):
    p = [['A(normal)',2,1,'정상'],['B(normal)',1,3,'정상'],['C(normal)',3,1,'정상'],['D(cancer)',3,4,'암환자'],['E(cancer)',5,5,'암환자']]
    distance = []
    for i in p:
        r = math.sqrt((i[1]-x)**2 + (i[2]-y)**2)   #유클리드 거리 계산
        distance.append(r)   #계산한 결과를 리스트에 입력
    for i in range(len(distance)):   #진단결과 출력
        if min(distance) == distance[i]:   #최소거리(가장 가까운 거리)가 나온 순번이면,
            print('진단결과:', p[i][3])   #환자데이터에서 해당하는 순번의 검사결과를 출력
    p.append([id,x,y])   #입력한 환자의 데이터도 환자데이터에 포함해서 그래프 그리기
    graph(p)

knn('F', 3, 3)