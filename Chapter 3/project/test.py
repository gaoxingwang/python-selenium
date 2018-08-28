import sys
sys.path.append("./model")
from model import new_count
test = new_count.C(2,3)
print(test.mul())