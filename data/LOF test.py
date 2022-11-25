import numpy as np
import matplotlib.pyplot as plt

def _scatter_plot(labels, x_axis, y_axis, points_size=None, x_min=None, x_max=None, y_min=None, y_max=None, title="", color='b', axhline=None):
    fig, ax = plt.subplots()
    if points_size is not None:
        ax.scatter(x_axis, y_axis, color=color, s=points_size * 10)
    else:
        ax.scatter(x_axis, y_axis, color=color)
    for i in range(len(labels)):
        ax.annotate(labels[i], (x_axis[i], y_axis[i]))
    if x_min and x_max:
        plt.xlim((x_min, x_max))
    if y_min and y_max:
        plt.ylim((y_min, y_max))
    if axhline:
        plt.axhline(y=axhline, color='r', linestyle='-')
    plt.title(title)
    try:
        z.show(plt)
        plt.close()
    except:
        plt.show()



array = np.load('C:/Users/PPiC/Desktop/IoT2022-main/work/1/data/array_joins_by_devices.npy')

def min_max_scaling(X:np.ndarray, a:float, b:float) -> np.ndarray:
    
    Xmax=X.max()
    Xmin=X.min()
    c=Xmax-Xmin
    scaled_array = a + (b-a)*(X-Xmin)/c
    
    
    return scaled_array

scaled_array = np.copy(array)
scaled_array["nb_records"] = min_max_scaling(scaled_array["nb_records"][:,np.newaxis], 0., 1.)[:,0]
scaled_array["nb_errors"] = min_max_scaling(scaled_array["nb_errors"][:,np.newaxis], 0., 1.)[:,0]

points = np.empty(shape=(scaled_array.shape[0], 2), dtype=np.float64)
points[:,0] = scaled_array["nb_records"]
points[:,1] = scaled_array["nb_errors"]







def LOF(points:np.ndarray, k:int) -> np.ndarray:
    n = len(points)
    # (1) -----------------------------------------------------------------------------
    # Find distance matrix:                                               (n, n)-matrix
    distMat = np.linalg.norm(points - points[:,None], axis = -1)  # L2 norm
    
    # (2) -----------------------------------------------------------------------------
    # Find k nearest points id matrix sorted by order:                    (n, k)-matrix
    M=np.where(distMat==0, np.Infinity, distMat)
    B=np.argsort(M)
    kFirstNeib = B[:,0:k]
    # Find k nearest point-distances
    kFistDist = np.array([[distMat[i,B[i,j]] for j in range(k)] for i in range(n) ])
    
    # (3) -----------------------------------------------------------------------------
    # Find k-distances                                                          n-array
    kD = np.array([distMat[i,B[i,k-1]] for i in range(n)])
    # Find reachability distances                                        (n, k)-matrix    
    RD = np.array([[max(kD[j],distMat[i,j]) for j in range(k)] for i in range(n)])
    
    # (4) -----------------------------------------------------------------------------
    # Find local reachability distances                                         n-array        
    RDmean = np.mean(RD, 1)
    LRD = np.array([1/i for i in RDmean])
    
    # (5) -----------------------------------------------------------------------------
    # Find local outlier factor                                                 n-array
    lof = np.array([[sum(LRD[B[i,j]] for j in range(k))/(k*LRD[i])] for i in range(n)])
    
    return lof

lof_scores = LOF(points, k=20)

_scatter_plot(
    labels=["Evil" if di == "Evil" else None for di in scaled_array['Downlink-CRM-ClientID']],
    x_axis=array["pct_errors"],
    y_axis=array["nb_records"],
    color=["r" if s > 1.5 else "b" for s in lof_scores],
    title="Local outlier factor"
)