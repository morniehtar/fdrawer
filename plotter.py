import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('QtCairo')

def draw_ampl(x, y, z):
    xx, yy = np.meshgrid(x, y)
    i = 0+1j
    zz = np.abs(z(xx + i*yy))

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('|f(x+iy)|')

    sfc = ax.plot_surface(xx, yy, zz, cmap=mpl.cm.coolwarm, linewidth=0, antialiased=False)
    #fig.colorbar(sfc, shrink=0.5, aspect=5)
    
    plt.tight_layout()
    plt.show()


def draw_real(x, y, z):
    xx, yy = np.meshgrid(x, y)
    i = 0+1j
    zz = z(xx + i*yy).real

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Re f(x+iy)')

    sfc = ax.plot_surface(xx, yy, zz, cmap=mpl.cm.coolwarm, linewidth=0, antialiased=False)
    #fig.colorbar(sfc, shrink=0.5, aspect=5)
    
    plt.tight_layout()
    plt.show()


def draw_imag(x, y, z):
    xx, yy = np.meshgrid(x, y)
    i = 0+1j
    zz = z(xx + i*yy).imag

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Im f(x+iy)')

    sfc = ax.plot_surface(xx, yy, zz, cmap=mpl.cm.coolwarm, linewidth=0, antialiased=False)
    #fig.colorbar(sfc, shrink=0.5, aspect=5)
    
    plt.tight_layout()
    plt.show()


def draw_surface(x, y, z):
    xx, yy = np.meshgrid(x, y)
    zz = z(xx, yy)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('f(x, y)')

    sfc = ax.plot_surface(xx, yy, zz, cmap=mpl.cm.coolwarm, linewidth=0, antialiased=False)
    #fig.colorbar(sfc, shrink=0.5, aspect=5)
    
    plt.tight_layout()
    plt.show()


def draw_plot(x, y):
    yy = y(x)

    fig, ax = plt.subplots()

    ax.plot(x, yy, label='f(x)', c='lime')

    ax.set_xlabel('x')
    ax.grid()
    ax.legend()

    plt.tight_layout()
    plt.show()

