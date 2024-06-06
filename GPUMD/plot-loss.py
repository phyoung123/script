"""
原来用的画图脚本，virial只画对角元 xx, yy, zz
"""

from pylab import *

figure(figsize=(12, 10))
subplot(2, 2,1)
loss = loadtxt('loss.out')
loglog(loss[:,1:6])
loglog(loss[:,7:9])
xlabel('Generation/100')
ylabel('Loss')
legend(['Total', 'L1-regularization', 'L2-regularization', 'Energy-train', 'Force-train', 'Energy-test', 'Force-test'])
tight_layout()
#show()
#savefig('Loss.png',dpi=900)

subplot(2, 2,2)
energy_test = loadtxt('energy_train.out')
plot(energy_test[:, 1], energy_test[:, 0], '.')
plot(linspace(-7.2,-5.8), linspace(-7.2,-5.8), '-')
xlabel('DFT energy (eV/atom)', font='Arial')
ylabel('NEP energy (eV/atom)',font='Arial')
# xlim(-7.2,-5.8)
# ylim(-7.2,-5.8)
tight_layout()

subplot(2, 2,3)
force_test = loadtxt('force_train.out')
plot(force_test[:, 3:6], force_test[:, 0:3], '.')
plot(linspace(-27,31), linspace(-27,31), '-')
xlabel('DFT force (eV/A)')
ylabel('NEP force (eV/A)')
# xlim(-27,31)
# ylim(-27,31)
legend(['x direction', 'y direction', 'z direction'])
tight_layout()

subplot(2, 2,4)
virial = loadtxt('virial_train.out')
plot(virial[:, 6:9], virial[:, 0:3], '.')
plot(linspace(0, 7), linspace(0, 7), '-')
xlabel('DFT virial (eV/atom)')
ylabel('NEP virial (eV/atom)')
# xlim(0, 7)
# ylim(0, 7)
legend(['xx direction', 'yy direction', 'zz direction'])
tight_layout()

savefig('all-train-virial.png',dpi=600)


