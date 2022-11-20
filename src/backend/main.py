import compareImage as comp
import time

start_time = time.time()
# print(comp.compareImage("././test/classes_pins_dataset/coba1","././test/classes_pins_dataset/coba2"))
# subtract = [[[0 for i in range(256)] for j in range(256)] for k in range(5)]
# print(len(subtract))
mirip = (100-comp.compareImage("../../test/classes_pins_dataset/coba1","../../test/classes_pins_dataset/coba2")/(256**2*5))
print("Tingkat kemiripan:   "+str(mirip)+"%")
if mirip>70:
    print("Mirip")
else:
    print("Tidak Mirip")
print("--- %s seconds ---" % (time.time() - start_time))