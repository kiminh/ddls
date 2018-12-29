from hpps.zoo import Zoo
from hpps.array_table import ArrayTable, create_array_table
from hpps.feeder.tensor import Tensor
import numpy as np

zoo = Zoo()

array_table = create_array_table(100, np.float32)
zoo.barrier()

data = Tensor(shape = [100], type= np.float32)
array_table.get(data)
print data.asnumpy()

grad = Tensor(shape = [100], type = np.float32)
grad.load_numpy(np.ones([100], np.float32))
array_table.add(grad)

array_table.get(data)
print data.asnumpy()
