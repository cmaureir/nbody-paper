import matplotlib.pyplot as p
from pylab import title,legend,grid,xlabel,ylabel


n=[16,32,64,128,256,512,1024,2048,4096]
t_s = [0.0250,0.0875,0.3750,1.4625,5.8000,23.4750,93.7375,374.6500,1478.362]
t_c=[0.0494,0.1024,0.1976,0.3871,0.8017,1.9284,5.6289,20.9967,82.1908]

t = []

for i in range(len(t_c)):
	t.append((t_s[i]/t_c[i]))
plot0 = p.plot(n,t,'o-',label=r'$\Psi(\delta,N)$')

title('CUDA Implementation',fontsize=14)
legend(fancybox=True,loc='center right')
grid(True)
p.axis([0,4096,0,20],0.01)
xlabel(r'$Number\ of\ particles$',fontsize=12)
ylabel(r'$Acceleration\ factor\ \left(\Psi\right)$',fontsize=12)
p.show()

