from src.backend import compareImage as comp
import time

start_time = time.time()
# print(comp.compareImage("././test/classes_pins_dataset/coba1","././test/classes_pins_dataset/11"))
# subtract = [[[0 for i in range(256)] for j in range(256)] for k in range(5)]
# print(len(subtract))
idx,mirip = (comp.compareAllImage("../../test/classes_pins_dataset/coba1","../../test/small_dataset"))
print("Tingkat kemiripan:   "+str(mirip)+"%")
print(idx)
if mirip<0.253:
    print("Mirip")
else:
    print("Tidak Mirip")
print("--- %s seconds ---" % (time.time() - start_time))