x = [float(val) for val in input().split()]  # x vector
y = [float(val) for val in input().split()]  # y vector
data = [x, y]   # given


def circleFitByDss(data):
    from scipy import optimize

    def f1(a, x, y):
        d = 0
        for i in range(len(x)):
            d += abs(((x[i] - a[0])**2 + (y[i] - a[1])**2)**(1/2) - a[2])
        return d

    a0 = [0, 0, 0]  # initial guess: a, b, r = 0

    # 把initial guess 調整為所有點的平均
    for i in range(len(data[0])):
        a0[0] += (data[0][i] / len(data[0]))    # new a
        a0[1] += (data[1][i] / len(data[0]))    # new b
        a0[2] += ((data[0][i] - a0[0])**2 + (data[1][i] - a0[1])**2)**(1/2) / len(data[0])  # new r
    xopt = optimize.fmin(f1, a0, xtol=1e-8, args=(data[0], data[1],), disp=False)
    print(round(xopt[0], 1), round(xopt[1], 1), round(xopt[2], 1))

if __name__ == '__main__':
    circleFitByDss(data)
