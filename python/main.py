import json
import matplotlib.pyplot as plt
import seaborn as sns

with open('../js/data.json', 'r') as f:
  data = json.load(f)

x_values = [point['x'] for point in data]
y_values = [point['y'] for point in data]