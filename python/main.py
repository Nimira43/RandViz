import json
import matplotlib.pyplot as plt
import seaborn as sns

with open('../js/data.json', 'r') as f:
  data = json.load(f)