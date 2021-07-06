import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    list = np.array(list).reshape((3,3))
    #Mean for Axis=0 
    l_mean = np.mean(list,axis=0).tolist()
    l_var = np.var(list,axis=0).tolist()
    l_std = np.std(list,axis=0).tolist()
    l_max = np.max(list,axis=0).tolist()
    l_min = np.min(list,axis=0).tolist()
    l_sum = np.sum(list,axis=0).tolist()

    #Mean for Axis=1
    r_mean = np.mean(list,axis=1).tolist()
    r_var = np.var(list,axis=1).tolist()
    r_std = np.std(list,axis=1).tolist()
    r_max = np.max(list,axis=1).tolist()
    r_min = np.min(list,axis=1).tolist()
    r_sum = np.sum(list,axis=1).tolist()

    #Mean for Flatten
    flat_mean = list.flatten().mean().tolist()
    flat_var = list.flatten().var().tolist()
    flat_std = list.flatten().std().tolist()
    flat_max = list.flatten().max().tolist()
    flat_min = list.flatten().min().tolist()
    flat_sum = list.flatten().sum().tolist()

    calculations = {

      'mean': [l_mean, r_mean, flat_mean],
      'variance': [l_var, r_var, flat_var],
      'standard deviation': [l_std, r_std, flat_std],
      'max': [l_max, r_max, flat_max],
      'min': [l_min, r_min, flat_min],
      'sum': [l_sum, r_sum, flat_sum]
                    }

  return calculations

#calculate([9,1,5,3,3,3,2,9,0])
