# Python script to run all modules in one go, without generating intermediate files.
from base import *
from distance import *
from greedy import *
from ioUtils import *

try:
   import cPickle as pickle
except:
   import pickle




print("Loading trajectories ...")
trajs = readTrajsFromTxtFile("data/sp500_test.txt") #done!
        
rmin, rmax = 0.1, 100 #not sure what this does
        
print("Computing Frechet distances ...")
distPairs1 = process(trajs, rmin, rmax)


#distPairs1 is of form {(pth, straj):dist}, change it to distPairs2 of the form {(pth, trajID):[(straj, dist)]}
distPairs2 = {}
for k,v in distPairs1.items():
    pth, trID, dist, straj = k[0], k[1].trajID, v, k[1]
    if (pth, trID) in distPairs2:
        distPairs2[(pth, trID)].append((straj,dist))
    else:
        distPairs2[(pth, trID)] = [(straj,dist)]

print("Computing prerequisite data structures ...")

(strajCov, ptStraj, strajPth, trajCov) = preprocessGreedy(trajs, distPairs2)
        
c1,c2,c3 = 1,1,1
        
print("Running greedy algorithm ...")
retVal = runGreedy(trajs, distPairs2, strajCov, ptStraj, strajPth, trajCov, c1, c2, c3)
print(retVal)