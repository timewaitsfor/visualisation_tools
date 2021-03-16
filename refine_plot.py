import numpy as np
import matplotlib.pyplot as plt
x1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y1=[80.1, 83.6, 84.8, 85.3, 85.7, 85.8, 86.2, 86.7, 87.4, 88.5, 89.4, 90.3]
x2=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y2=[86.6, 90.3, 90.5, 90.9, 92.1, 92.3, 92.8, 93.1, 93.5, 94.0, 94.1, 94.2]
x3=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y3=[91.5, 93.2, 93.4, 93.8, 94.0, 94.1, 94.3, 94.5, 94.8, 95.1, 95.7, 96.1]

x = np.arange(10,50)
y = [70, 80, 90, 100]
l1=plt.plot(x1,y1,'-', marker='v',label='ZH-EN', linewidth=3.0, markersize=10)
l2=plt.plot(x2,y2,'--', marker='o', label='JA-EN', linewidth=3.0, markersize=10)
l3=plt.plot(x3,y3,'.-', marker='s', label='FR-EN', linewidth=3.0, markersize=10)
# l1=plt.plot(x1,y1,label='type1')
# l2=plt.plot(x2,y2,label='type2')
# l3=plt.plot(x3,y3,label='type3')
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ('0', '1', '2', '4', '6', '8', '10', '12', '15', '20', '25', '30'))


# plt.grid(linestyle='-.', c='r')
plt.grid(linestyle='-.',linewidth = 3)
# plt.plot(x1,y1,'ro-',x2,y2,'g+-')
# plt.title('The Lasers in Three Conditions')
plt.xlabel('Refine layer numbers')
plt.ylabel('Hits@1')
plt.legend()

bwith = 2 #边框宽度设置为2
ax = plt.gca()#获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
ax.set_ylim(70, 100)
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

plt.show()