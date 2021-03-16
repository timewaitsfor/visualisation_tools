import numpy as np
import matplotlib.pyplot as plt
x1=[10, 20, 30, 40]
y1=[85, 90, 94, 96]
x2=[10, 20, 30, 40]
y2=[84, 86, 87, 87]
x=np.arange(10,50)
plt.figure(figsize=(6, 5))

l1=plt.plot(x1,y1,'-', marker='v',label='ERMC', linewidth=3.0, markersize=10)
l2=plt.plot(x2,y2,'--', marker='o', label='RNM', linewidth=3.0, markersize=10)
# l1=plt.plot(x1,y1,label='type1')
# l2=plt.plot(x2,y2,label='type2')
# l3=plt.plot(x3,y3,label='type3')


# plt.grid(linestyle='-.', c='r')
plt.grid(linestyle='-.',linewidth = 2)
# plt.plot(x1,y1,'ro-',x2,y2,'g+-')
plt.xlabel('Proportion of seed alignments')
plt.ylabel('Hits@1')
plt.legend()



bwith = 2 #边框宽度设置为2
ax = plt.gca()#获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
ax.set_ylim(80, 100)
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

plt.show()