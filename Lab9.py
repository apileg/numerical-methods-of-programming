import matplotlib.pyplot as pltfrom scipy.interpolate
import UnivariateSplineimport numpy as np

x = [0,1.4,2.3,3.3,4.5]
y = [1,1.155,0.079,-1.145,-1.188]
spl = UnivariateSpline(x, y)
xs = np.linspace(0, 4.5, 1000)
plt.plot(x,y,'ro', xs, spl(xs), 'g')
plt.show()
