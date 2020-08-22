def myPvAlign(pv, noteVec):
    import numpy as np

    pv = np.array(pv)
    noteVec = np.array(noteVec)

    data = np.zeros((len(noteVec), len(pv)))
    for i in range(len(pv)):
        for j in range(len(noteVec)):
            data[j][i] = abs(pv[i]-noteVec[j])
    dist = np.zeros(len(noteVec))
    # 處理第一列
    for i in range(1, len(pv)):
        data[0][i] = data[0][i-1] + data[0][i]
    # 處理每列初始值
    for i in range(1, len(noteVec)):
        data[i][i] += data[i-1][i-1]
    for i in range(1, len(noteVec)):
        for j in range(i+1, len(pv)):
            data[i][j] += min(data[i-1][j-1], data[i][j-1])
    for i in range(len(noteVec)):
        dist[i] = data[i][len(pv)-1]
    return min(dist)


'''
import numpy as np

pv = [float(val) for val in input().split()]
noteVec = [float(val) for val in input().split()]
pv = np.array(pv)
noteVec = np.array(noteVec)
data = np.zeros((len(noteVec), len(pv)))
for i in range(len(pv)):
    for j in range(len(noteVec)):
        data[j][i] = abs(pv[i]-noteVec[j])
dist = np.zeros(len(noteVec))
# 處理第一列
for i in range(1, len(pv)):
    data[0][i] = data[0][i-1] + data[0][i]
# 處理每列初始值
for i in range(1, len(noteVec)):
    data[i][i] += data[i-1][i-1]
for i in range(1, len(noteVec)):
    for j in range(i+1, len(pv)):
        data[i][j] += min(data[i-1][j-1], data[i][j-1])
for i in range(len(noteVec)):
    dist[i] = data[i][len(pv)-1]
print(min(dist))
==============================================================================================================================================================
input:
63.109468 62.090768 62.090768 62.090768 62.090768 62.090768 61.603068 61.603068 61.603068 61.603068 61.128768 61.603068 62.090768 61.603068 61.128768 61.128768 61.128768 61.128768 61.128768 61.128768 61.128768 61.128768 61.603068 62.090768 63.109468 64.191768 65.953868 65.953868 66.583468 66.583468 67.236868 67.236868 67.236868 67.236868 67.915868 67.915868 67.915868 67.915868 67.236868 68.622568 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.915868 67.915868 68.622568 69.359468 69.359468 69.359468 69.359468 69.359468 69.359468 69.359468 69.359468 69.359468 69.359468 69.359468 68.622568 68.622568 69.359468 69.359468 69.359468 69.359468 69.359468 69.359468 69.359468 69.359468 69.359468 69.359468 69.359468 69.359468 68.622568 67.915868 67.236868 66.583468 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 67.236868 66.583468 66.583468 65.953868 65.953868 65.953868 65.346368 64.759468 64.759468 64.759468 65.346368 65.346368 65.346368 65.346368 65.346368 65.346368 65.346368 65.346368 65.953868 65.953868 65.953868 65.346368 65.346368 65.346368 65.346368 65.346368 65.346368 65.346368 65.346368 64.759468 64.759468 63.642168 64.759468 64.191768 64.191768 64.191768 64.191768 64.191768 64.191768 64.191768 64.191768 64.191768 64.759468 63.642168 65.346368 64.191768 64.191768 64.191768 64.191768 64.191768 64.191768 64.191768 64.191768 64.191768 64.191768 63.642168 62.592568 64.191768 62.592568 62.090768 61.603068 61.603068 61.603068 62.090768 62.090768 62.090768 62.090768 62.090768 62.090768 61.603068 63.642168 62.592568 62.090768 62.090768 62.090768 62.090768 62.090768 62.090768 62.090768 62.090768 62.090768 62.090768 62.090768 61.128768 61.603068 60.667068 60.217368 60.667068 60.217368 60.667068 60.667068 60.667068 60.667068 60.667068 60.217368 60.217368 60.217368 60.217368 60.217368 60.217368 61.603068 
60 60 62 64 67 67 64 67 67 69 71 72 72 
output:
253.3754120000001
easy:
12 11 15 16 11 12 9 10
11 15 10 18
'''
