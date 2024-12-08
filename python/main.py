import json
import matplotlib.pyplot as plt
import seaborn as sns

with open('../js/data.json', 'r') as f:
  data = json.load(f)

x_values = [point['x'] for point in data]
y_values = [point['y'] for point in data]

mean_x = sum(x_values) / len(x_values)
mean_y = sum(y_values) / len(y_values)

print(f'Mean of X values: {mean_x}')
print(f'Mean of Y values: {mean_y}')