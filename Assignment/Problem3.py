import prob1
import Problem2
import numpy as np
from matplotlib import pyplot as plt
import plotly.graph_objects as go

sent = Problem2.sentiment
dist = [prob1.hubIndex1,prob1.hubIndex2,prob1.hubIndex3]
distscore = [[0 for i in range (5)]for i in range(3)]

#std mean dist
meandist=[]
stddist=[]
lowerbound=[]
upperbound=[]

maxs = max(sent)
mins = min(sent)


for i in range (3):
    meandist.append(np.mean(dist[i]))
    stddist.append(np.std(dist[i]))
    lowerbound.append(meandist[i]-stddist[i])
    upperbound.append(meandist[i]+stddist[i])


print(dist)
print(meandist)
print(stddist)
print(lowerbound)
print(upperbound)

for i in range (3):
    for j in range (5):
        if dist[i][j] > upperbound[i] :
            distscore[i][j]= 0
        elif dist[i][j] < lowerbound[i] :
            distscore[i][j]= maxs-mins
        else :
            distscore[i][j]= (maxs-mins)/2

print(distscore)

#std mean sent
# lowerbound = []
# upperbound = []
# meansent = []
# stdsent = []
# for i in range (5):
#     meansent.append(np.mean(sent))
#     stdsent.append(np.std(sent))
#     lowerbound.append(meansent[i]-stdsent[i])
#     upperbound.append(meansent[i]+stdsent[i])
# print(sent)
# print(lowerbound,upperbound)

# sentscore = []

# for i in range (5):
#     if sent[i] > upperbound[i] :
#         sentscore.append(3)
#     elif sent[i] < lowerbound[i] :
#         sentscore.append(1)
#     else :
#         sentscore.append(2)

# print (sentscore)

#total score (distance score + sent score)
totalscore = [[0 for i in range (5)] for i in range (3)]
for j in range (3):
    for i in range (5):
        totalscore[j][i] = sent[i] + distscore[j][i]
print(totalscore)

total = []
for j in range (3):
    n = 0
    for i in range (5):
        n += totalscore[j][i]
    total.append(n)
print(total)

probability = [[0 for i in range (5)] for i in range (3)]
for j in range (3):
    for i in range (5):
        probability[j][i] = round(((totalscore[j][i]/total[j])),2)
print(probability)

n =0
for i in range (3):

    fig = go.Figure([go.Bar(x=["jnt","citylink","dhl","poslaju","gdex"], y=probability[i])])
    fig.write_html(f'{n}probability.html', auto_open=True)
    n+=1