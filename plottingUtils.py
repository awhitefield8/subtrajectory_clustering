import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def trajs_to_df(traj_dict):
    '''
    takes in list of trajectories, and adds to data.frame for plotting
    '''
    df = pd.DataFrame(columns = ['new_id', 'x_coord', 'y_coord','id'])
    counter = 1
    
    for k,v in traj_dict.items():
        for p in v.pts:
            new_row = {'new_id':counter, 'x_coord':p.lat, 'y_coord': p.lon,'id': p.trajID}
            df = df.append(new_row, ignore_index = True)
            counter = counter + 1
            
    return(df)
    
def pathlet_to_df(pth,pth_name,traj_dict):
    """ takes in a pathlet, converts to object we can plot
    Args:
        pth = pathlet object
        pth_name = name of the path for the dataframe
        traj_dict = trajectory dictionary

    Returns:
        An data.frame for plotting 
    """
    tid = pth.trajID
    b = pth.bounds
    
    df = pd.DataFrame(columns = ['new_id', 'x_coord', 'y_coord','id'])
    counter = 1
    
    for i in range(b[0],b[1]):
        p = traj_dict[tid].pts[i]
        new_row = {'new_id':counter, 'x_coord':p.lat, 'y_coord': p.lon,'id': pth_name}
        df = df.append(new_row, ignore_index = True)
        counter = counter + 1
        
    return(df)



def plot_traj(traj_dict):
    '''
    plot trajectories function
    '''
    
    df_traj = trajs_to_df(traj_dict)
    
    return(sns.lineplot(data=df_traj,
                        x="x_coord",
                        y="y_coord",
                        hue="id",
                        legend=False,
                        linewidth = 0.1).set(xlabel ="day", ylabel = "returns")
          )


def plot_clust_result(greedy_result,traj_dict):
    ''' Plots clustering result
    
    Args:
        greedy_result: output of the greedy algorithm
        traj_dict: trajectory dictionary

    Returns:
        A seaborn plot
    
    '''
    pthAssignments = greedy_result[0] #extract clustering result
    
    plot_traj(traj_dict) #plot trajectories
    
    #next, overlay pathlets
    pth_counter = 1
    for k,v in pthAssignments.items():
        pth_df = pathlet_to_df(k,pth_name = pth_counter,traj_dict=traj_dict)
        sns.lineplot(data=pth_df,
                     x="x_coord",
                     y="y_coord",
                     hue="id",
                     legend=False,
                     linewidth = 1)
        pth_counter = pth_counter + 1