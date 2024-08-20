import os
import re
import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_and_clean_file(text):
    phrases_to_remove = [
    "Okay, This is my GPT instruction:",
    "Here are instructions from the user outlining your goals and how you should respond:"
    ]
    # 특정 문장이나 구문 제거
    for phrase in phrases_to_remove:
        text = text.replace(phrase, "")
    # 줄 바꿈 및 공백 제거
    text = re.sub(r'\s+', ' ', text)  # 여러 공백, 줄 바꿈을 단일 공백으로 변환
    text = text.strip()  # 앞뒤 공백 제거
    return text

def calculate_similarity(text1, text2):
    if text1 == '' or text2 == '':
        return None
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return cosine_sim[0][0]


def main(text1, text2):
    similarity = calculate_similarity(text1, text2)
    return similarity

if __name__ == "__main__":
    # 비교할 텍스트 파일 경로
    file_path = '7week/original_data0~500.json'
    file_path2 = '7week/fixed_data.json'

    inst_lst = [''] * 3000
    sim_lst = [[None] * 3000 for _ in range(3000)]

    with open(file_path, 'r', encoding='utf-8') as file:
        original = json.load(file)
    for i in range(500):
        try:
            inst_lst[i*6] = read_and_clean_file(original[str(i)]["instructions"])
        except:
            continue
    
    with open(file_path2, 'r', encoding='utf-8') as file:
        merged = json.load(file)
    for i in range(500):
        try:
            for j in range(1,len(merged[str(i)])+1):
                try:
                    if original[str(i)]['ID'] == merged[str(i)][j-1]['ID']:
                        continue
                    inst_lst[i*6+j] = read_and_clean_file(merged[str(i)][j-1]["instructions"])
                except:
                    continue
        except:
            continue
    print(len([item for item in inst_lst if item]))
    print("insts done")

    
    for i in range(3000):
        for j in range(3000):
            if i >= j:
                continue
            sim_lst[i][j] = main(inst_lst[i],inst_lst[j])
        print(f"sim{i} done")

    df = pd.DataFrame(sim_lst)
    df.to_csv('sim_lst.csv', index=False, header=False)
    print("sim saved")
    
    flat_sim_lst = [item for sublist in sim_lst for item in sublist if item is not None]
    mean = np.mean(flat_sim_lst)
    std_dev = np.std(flat_sim_lst)

    plt.figure(figsize=(10, 6))
    plt.hist(flat_sim_lst, bins=10, edgecolor='black', alpha=0.7)
    plt.title('cosine similarity distribution')
    plt.xlabel('similarity')
    plt.ylabel('numbers')
    plt.grid(True)
    plt.show()