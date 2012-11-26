import matplotlib.pyplot as p
from pylab import title,legend,grid,xlabel,ylabel


n=[16,32,64,128,256,512,1024,2048,4096]
c=[1,2,4,6,8,10,12,14,16]
t_s = [0.0250,0.0875,0.3750,1.4625,5.8000,23.4750,93.7375,374.6500,1478.362]


t_16=[0.0625,0.0625,0.0625,0.0125,0.1625,0.2250,0.2750,0.3125,0.3750]
t_32=[0.1250,0.1250,0.1500,0.1875,0.2125,0.2625,0.3000,0.3750,0.4000]
t_64=[0.4750,0.2625,0.3750,0.3875,0.4250,0.4375,0.5000,0.5000,0.5875]
t_128=[1.5250,1.0125,1.0250,1.0375,1.0500,1.0625,1.0875,1.1625,1.2250]
t_256=[5.6250,3.3750,2.4000,2.2375,2.5625,2.5250,2.6000,2.5500,2.8250]
t_512=[22.0125,11.9875,7.0750,5.6250,5.4000,5.5375,5.4875,5.3250,5.5500]
t_1024=[85.9500,47.0875,24.4250,18.2250,15.4375,14.3000,14.1750,14.0250,14.0000]
t_2048=[335.0500,188.0876,93.7375,65.1125,53.2125,46.4500,41.3375,39.2250,42.1750]
t_4096=[1364.0000,750.2500,353.3750,243.7500,178.8750,172.3750,147.3750,134.6250,129.1250]

tt_16 = []
tt_32 = []
tt_64 = []
tt_128 = []
tt_256 = []
tt_512 = []
tt_1024 = []
tt_2048 = []
tt_4096 = []

for i in range(len(t_s)):
	tt_16.append((t_s[0]/t_16[i]))
	tt_32.append((t_s[1]/t_32[i]))
	tt_64.append((t_s[2]/t_64[i]))
	tt_128.append((t_s[3]/t_128[i]))
	tt_256.append((t_s[4]/t_256[i]))
	tt_512.append((t_s[5]/t_512[i]))
	tt_1024.append((t_s[6]/t_1024[i]))
	tt_2048.append((t_s[7]/t_2048[i]))
	tt_4096.append((t_s[8]/t_4096[i]))


tmp = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

plot00 = p.plot(tmp,tmp,label="-")

#plot0 = p.plot(c,tt_16,'o-',label='16 particles')
#plot1 = p.plot(c,tt_32,'o-',label='32 particles')
#plot2 = p.plot(c,tt_64,'o-',label='64 particles')
plot3 = p.plot(c,tt_128,'o-',label='128 particles')
#plot4 = p.plot(c,tt_256,'o-',label='256 particles')
plot5 = p.plot(c,tt_512,'o-',label='512 particles')
#plot6 = p.plot(c,tt_1024,'o-',label='1024 particles')
#plot7 = p.plot(c,tt_2048,'o-',label='2048 particles')
plot8 = p.plot(c,tt_4096,'o-',label='4096 particles')

title('Pthreads Implementation',fontsize=14)
legend(fancybox=True,loc='upper left')
grid(True)
p.axis([0,16,0,16],0.01)
xlabel(r'$Number\ of\ cores$',fontsize=12)
ylabel(r'$Speed\ up\ \left(\frac{Serial\ Time}{Parallel\ Time}\right)$',fontsize=12)
p.show()

