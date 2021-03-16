import matplotlib.pyplot as plt

def fold_line_plot(xs, ys, x_coo):
    l1 = plt.plot(x1, y1, 'r--', label='type1')
    l2 = plt.plot(x2, y2, 'g--', label='type2')
    # l1=plt.plot(x1,y1,label='type1')
    # l2=plt.plot(x2,y2,label='type2')
    # l3=plt.plot(x3,y3,label='type3')

    # plt.grid(linestyle='-.', c='r')
    plt.grid(linestyle='-.', linewidth=2)
    plt.plot(x1, y1, 'ro-', x2, y2, 'g+-')
    plt.title('The Lasers in Three Conditions')
    plt.xlabel('row')
    plt.ylabel('column')
    plt.legend()

    bwith = 2  # 边框宽度设置为2
    ax = plt.gca()  # 获取边框
    # ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
    # ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
    ax.spines['bottom'].set_linewidth(bwith)
    ax.spines['left'].set_linewidth(bwith)
    ax.spines['top'].set_linewidth(bwith)
    ax.spines['right'].set_linewidth(bwith)

    plt.show()

    pass