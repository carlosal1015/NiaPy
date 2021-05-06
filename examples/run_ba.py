# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys

sys.path.append('../')
# End of fix

from niapy.algorithms.basic import BatAlgorithm
from niapy.task import StoppingTask
from niapy.benchmarks import Griewank

# we will run Bat Algorithm for 5 independent runs
for i in range(5):
    task = StoppingTask(max_iters=10000, enable_logging=True, dimension=10, benchmark=Griewank(Lower=-600, Upper=600))
    algo = BatAlgorithm()
    best = algo.run(task)
    print('%s -> %s' % (best[0], best[1]))
