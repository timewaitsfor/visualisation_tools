import numpy as np
import matplotlib.pyplot as plt
x1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y1=[135, 57, 25, 21, 13, 8, 5, 0, 0, 0, 0, 0]
x2=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y3=[199, 94, 62, 54, 62, 69, 66, 83, 104, 131, 148, 170]
x3=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y2=[223, 109, 49, 25, 35, 37, 50, 78, 82, 121, 104, 125]

x = np.arange(10,50)
# y = [70, 80, 90, 100]
l1=plt.plot(x1,y1,'-', marker='v',label='episode 1', linewidth=3.0, markersize=10)
l2=plt.plot(x2,y2,'--', marker='o', label='episode 20', linewidth=3.0, markersize=10)
l3=plt.plot(x3,y3,'.-', marker='s', label='episode 50', linewidth=3.0, markersize=10)
# l1=plt.plot(x1,y1,label='type1')
# l2=plt.plot(x2,y2,label='type2')
# l3=plt.plot(x3,y3,label='type3')
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '20'))


# plt.grid(linestyle='-.', c='r')
plt.grid(linestyle='-.',linewidth = 3)
# plt.plot(x1,y1,'ro-',x2,y2,'g+-')
# plt.title('The Lasers in Three Conditions')
plt.xlabel('Boostrapping times')
plt.ylabel('Candidate nums')
plt.legend()

bwith = 2 #边框宽度设置为2
ax = plt.gca()#获取边框
# ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
# ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
# ax.set_ylim(70, 100)
ax.spines['bottom'].set_linewidth(bwith)
ax.spines['left'].set_linewidth(bwith)
ax.spines['top'].set_linewidth(bwith)
ax.spines['right'].set_linewidth(bwith)

plt.show()