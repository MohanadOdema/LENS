import mobo

#x = [36, 5, 1, 128, 7, 2, 1, 64, 5, 1, 0, 256, 100]		#ALEXNET
#x = [36, 5, 2, 1, 96, 5, 1, 0, 384, 11, 3, 1, 128, 5, 1, 1, 128, 7, 3, 1, 4096, 1024]	#71.83%, 70.38%(dropout(0.2)), 76.34%(data augmentation), 79.88%(batch normalization), 71.38%(all)
x = [64, 3, 2, 1, 128, 3, 2, 1, 256, 3, 3, 1, 512, 3, 3, 1, 512, 3, 3, 1, 4096, 4096]	#72.84%, 80.27%(data augmentation + batch normalization)

r2 = mobo.error(x)
#r3 = mobo.energy(x)
#r4 = mobo.latency(x)

#print(r1)
#print(r2)
#(r3)
#print(r4)
