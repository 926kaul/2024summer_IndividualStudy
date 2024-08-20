import os
import re
import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_path = '7week/sim_lst.csv'
df = pd.read_csv(file_path, header=None, na_values='')
df = df.where(pd.notna(df), None)
sim_lst = df.values.tolist()

flat_sim_lst = [item for sublist in sim_lst for item in sublist if not pd.isna(item)]
real_sim_lst = [sim_lst[i][j] for i in range(3000) for j in range(3000) if not pd.isna(sim_lst[i][j]) and i<j<i+6]
print(len(real_sim_lst))
mean = np.mean(flat_sim_lst)
std_dev = np.std(flat_sim_lst)

plt.figure(figsize=(10, 6))
plt.hist(flat_sim_lst, bins=40, edgecolor='black', alpha=0.5, color='blue')
#plt.hist(real_sim_lst, bins=40, edgecolor='black', alpha=0.5, color='red')
plt.title('cosine similarity distribution')
plt.xlabel('similarity')
plt.ylabel('numbers')
plt.grid(True)
plt.show()