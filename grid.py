"""creation of a grid """

def grid(xmin,xmax,ymin,ymax):
    #window
    plt.clf()
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    #params
    m = min(xmin,ymin)
    M = max(xmax,ymax)
    #with plt.style.context('dark_background'): dark mode
    y = np.array([M,m])
    x = np.array([m,M])
    for i in range (m,M+1):
        for k in range (m,M+1):
            plt.plot(np.array([i,i]),y,'k-')
            plt.plot(x,np.array([k,k]),'k-')
    plt.show()
