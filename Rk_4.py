import matplotlib.pyplot as plt    # importing lib for ploting graph

x = 1.  # initial value of x
y = 1.  # initial value of y
z = 1.  # initial value of z
t = 0.  # initial value of t as the function is in respect to t

h = 0.0001  # step size for 10000
print('t', '\t', '\t', 'x', '\t', '\t', 'y', '\t', '\t', 'z', '\n')  # representation pf t, x, y, z
print(t, '\t', x, '\t', y, '\t', z)  # printing initial value of x,y,z,t

while (t < 1):  # no. of times the loop run according to step size
    m1 = 10. * (x - y)  # Eqn 1  dxdt = 10 (y-x)
    k1 = x * (28. - z) - y  # Eqn 2   dydt = x(28-z)-y
    l1 = (x * y) - ((8 / 3) * z)  # Eqn 3

    ft2 = t + (h / 2.)  # for function 1
    fx2 = x + (h / 2.) * m1  # for function 1
    fy2 = y + (h / 2.) * k1  # for function 1
    fz2 = z + (h / 2.) * l1  # for function 1
    m2 = 10. * (fx2 - fy2)

    gt2 = t + (h / 2.)  # for function 2
    gx2 = x + (h / 2.) * m1  # for function 2
    gy2 = y + (h / 2.) * k1  # for function 2
    gz2 = z + (h / 2.) * l1  # for function 2
    k2 = gx2 * (28. - gz2) - gy2

    rt2 = t + (h / 2.)  # for function 3
    rx2 = x + (h / 2.) * m1  # for function 3
    ry2 = y + (h / 2.) * k1  # for function 3
    rz2 = z + (h / 2.) * l1  # for function 3
    l2 = rx2 * (28. - rz2) - ry2

    ft3 = t + (h / 2.)         # for function 1
    fx3 = x + (h / 2.) * m2     # for function 1
    fy3 = y + (h / 2.) * k2     # for function 1
    fz3 = z + (h / 2.) * l2     # for function 1
    m3 = 10. * (fy3 - fx3)

    gt3 = t + (h / 2.)           # for function 2
    gx3 = x + (h / 2.) * m2       # for function 2
    gy3 = y + (h / 2.) * k2        # for function 2
    gz3 = z + (h / 2.) * l2          # for function 2
    k3 = gx3 * (28. - gz3) - gy3

    rt3 = t + (h / 2.)              # for function 3
    rx3 = x + (h / 2.) * m2          # for function 3
    ry3 = y + (h / 2.) * k2            # for function 3
    rz3 = z + (h / 2.) * l2              # for function 3
    l3 = (rx3 * ry3) - ((8 / 3) * rz3)

    ft4 = t + h                        # for function 1
    fx4 = x + h * m3                    # for function 1
    fy4 = y + h * k3                     # for function 1
    fz4 = z + h * l3                        # for function 1
    m4 = 10. * (fx4 - fy4)

    gt4 = t + h                     # for function 2
    gx4 = x + h * m3                # for function 2
    gy4 = y + h * k3                  # for function 2
    gz4 = z + h * l3                 # for function 2
    k4 = gx4 * (28. - gz4) - gy4

    rt4 = t + h                     # for function 3
    rx4 = x + h * m3                 # for function 3
    ry4 = y + h * k3                   # for function 3
    rz4 = z + h * l3                     # for function 3
    l4 = (rx4 * ry4) - ((8 / 3) * rz4)

    t = t + h

    x = x + (h / 6.) * (m1 + (2. * m2) + (2. * m3) + m4)     # x(n+1) = x(n) + 1/6(m1+2m2+2m3+m4)
    y = y + (h / 6.) * (k1 + (2. * k2) + (2. * k3) + k4)     # y(n+1) = y(n) + 1/6(k1+2k2+2k3+k4)
    z = z + (h / 6.) * (l1 + (2. * l2) + (2. * l3) + l4)     # z(n+1) = z(n) + 1/6(l1+2l2+2l3+l4)
    print(t, '\t', '\t', x, '\t', y, '\t', z)

    plt.plot(t, x, 'rs')   # graph between x and t
    plt.plot(t, y, 'bs')   # graph between y and t
    plt.plot(t, z, 'gs')   # graph between z and t

plt.show()
