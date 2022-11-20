import compareImage as comp
import time

start_time = time.time()
print("Hello world")
# print(comp.compareImage("././test/classes_pins_dataset/coba1","././test/classes_pins_dataset/coba2"))
# subtract = [[[0 for i in range(256)] for j in range(256)] for k in range(5)]
# print(len(subtract))
print(100-comp.compareImage("../../test/classes_pins_dataset/coba1","../../test/small_dataset/10")/(256**2*5))
print("--- %s seconds ---" % (time.time() - start_time))