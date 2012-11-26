import matplotlib.pyplot as p
from pylab import title,legend,grid,xlabel,ylabel


n=[16,32,64,128,256,512,1024,2048,4096]
c=[1,2,4,6,8,10,12,14,16]
t_s = [0.0250,0.0875,0.3750,1.4625,5.8000,23.4750,93.7375,374.6500,1478.362]


t_16=[0.0125,0.0250,0.0250,0.0375,0.0500,0.0620,0.0625,0.0625,0.0625]
t_32=[0.0875,0.1125,0.1125,0.0875,0.0625,0.0750,0.0750,0.0625,0.0875]
t_64=[0.475,0.5125,0.3375,0.3,0.275,0.2375,0.2125,0.2,0.1875]
t_128=[1.7375,2.0375,1.3375,1.2125,1.0500,0.9000,0.7750,0.7375,0.6625]
t_256=[7.2250,7.7375,5.4500,4.7875,4.1875,3.5375,3.0625,2.5750,2.3125]
t_512=[27.4375,31.9750,21.4875,18.5250,16.5000,13.9875,11.7625,10.1750,8.9125]
t_1024=[102.5626,126.4626,84.1250,72.2625,65.9000,54.5625,46.6250,40.5375,35.6125]
t_2048=[428.2626,503.8750,335.2248,293.4126,263.1998,221.0252,184.1752,160.7498,143.0376]
t_4096=[1605.1980,2000.6500,1326.6500,1149.6480,1044.0740,871.7500,737.2500,638.3750,568.0000]

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
plot1 = p.plot(c,tt_32,'o-',label='32 particles')
#plot2 = p.plot(c,tt_64,'o-',label='64 particles')
plot3 = p.plot(c,tt_128,'o-',label='128 particles')
#plot4 = p.plot(c,tt_256,'o-',label='256 particles')
#plot5 = p.plot(c,tt_512,'o-',label='512 particles')
#plot6 = p.plot(c,tt_1024,'o-',label='1024 particles')
#plot7 = p.plot(c,tt_2048,'o-',label='2048 particles')
plot8 = p.plot(c,tt_4096,'o-',label='4096 particles')

title('OpenMP Implementation',fontsize=14)
legend(fancybox=True,loc='center right')
grid(True)
p.axis([0,16,0,16],0.01)
xlabel(r'$Number\ of\ cores$',fontsize=12)
ylabel(r'$Speed\ up\ \left(\frac{Serial\ Time}{Parallel\ Time}\right)$',fontsize=12)
p.show()

