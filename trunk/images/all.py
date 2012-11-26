import matplotlib.pyplot as p
from pylab import title,legend,grid,xlabel,ylabel


n=[16,32,64,128,256,512,1024,2048,4096]
c=[1,2,4,6,8,10,12,14,16]
t_s=[0.0250,0.0875,0.3750,1.4625,5.8000,23.4750,93.7375,374.6500,1478.362]
t_c=[0.0494,0.1024,0.1976,0.3871,0.8017, 1.9284, 5.6289, 20.9967, 82.1908]
t_p=[0.3750,0.4000,0.5875,1.2250,2.8250, 5.5500,14.0000, 42.1750,129.1250]
t_o=[0.0625,0.0875,0.1875,0.6625,2.3125, 8.9125,35.6125,143.0376,568.0000]


plot1 = p.plot(n,t_s,'o-',label='Serial')
plot2 = p.plot(n,t_c,'o-',label='CUDA')
plot3 = p.plot(n,t_p,'o-',label='Pthreads')
plot4 = p.plot(n,t_o,'o-',label='OpenMP')

title('Implementations',fontsize=14)
legend(fancybox=True,loc='upper left')
grid(True)
p.axis([0,4096,0,1500],0.01)
xlabel(r'$Number\ of\ bodies$',fontsize=12)
ylabel(r'$Time\ (seconds)$',fontsize=12)
p.show()

