# Subtrajectory clustering

Code for clustering **sub**trajectories in a trajectory data set. These subtrajectory clusters capture common movement patterns among trajectories. Based on the paper [here](https://dl.acm.org/citation.cfm?id=3196972), or go over the presentation [here.](https://github.com/abhi1991nath/subtrajectory_clustering/blob/master/presentation.pdf)

Updated to work with Python 3.8
Major changes
    - optionally imports cPickle, falls back to Pickle if not
    - remove depricated python2.7 syntax (sets, print, xrange, has_key, iteritems)
    - edited canonise to roundown


