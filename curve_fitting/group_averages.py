
import matplotlib.pyplot as plt


def group_averages(x, y, num_groups):
  n = len(x)
  group_size = n // num_groups
  groups = [range(i * group_size, (i + 1) * group_size) for i in range(num_groups)]
  
  group_avg = []
  for group in groups:
    x_avg = sum(x[i] for i in group)/len(group)
    y_avg = sum(y[i] for i in group)/len(group)
    group_avg.append((x_avg, y_avg))

  x_avg_avg = sum(pair[0] for pair in group_avg)/len(group_avg)
  y_avg_avg = sum(pair[1] for pair in group_avg)/len(group_avg)

  return group_avg, x_avg_avg, y_avg_avg

def group_averages_linear(x, y, num_groups):
  group_avg, x_avg_avg, y_avg_avg = group_averages(x, y, num_groups)
      
  num = sum((pair[0] - x_avg_avg)*(pair[1] - y_avg_avg) for pair in group_avg)
  denom = sum((pair[0] - x_avg_avg)**2 for pair in group_avg)

  b = num / denom
  a = y_avg_avg - b*x_avg_avg

  return b, a, group_avg


def group_averages_quadratic(x, y, num_groups):
    group_avg, x_avg_avg, y_avg_avg = group_averages(x, y, num_groups)
    
    sum_x2 = sum(pair[0]**2 for pair in group_avg)
    sum_x = sum(pair[0] for pair in group_avg)
    sum_1 = len(group_avg)
    sum_y = sum(pair[1] for pair in group_avg)
    sum_x2y = sum(pair[0]**2 * pair[1] for pair in group_avg)
    sum_xy = sum(pair[0] * pair[1] for pair in group_avg)

    denominator = sum_x2 * sum_1 - sum_x**2
    if denominator == 0:
        raise ValueError("The data does not fit the quadratic model.")
    
    a = (sum_x2 * sum_y - sum_x * sum_xy) / denominator
    b = (sum_1 * sum_xy - sum_x * sum_y) / denominator
    c = (sum_x2y - sum_x * sum_y) / denominator

    return a, b, c, group_avg

  
