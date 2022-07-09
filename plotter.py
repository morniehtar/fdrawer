import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('QtCairo')


def draw3D(x, y, z):
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    xx, yy = np.meshgrid(x, y)
    zz = z(xx, yy)
    #zz = np.sqrt(xx**2 + yy**2)
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('Re f(x)')

    sfc = ax.plot_surface(xx, yy, zz, cmap=mpl.cm.coolwarm, linewidth=0, antialiased=False)
    fig.colorbar(sfc, shrink=0.5, aspect=5)
    
    plt.tight_layout()
    plt.show()


def draw2D(x, y):
    yy = y(x)

    plt.plot(x, yy, label='f(x)', c='lime')

    plt.xlabel('x')
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.show()

