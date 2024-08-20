import os
import re
import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return cosine_sim[0][0]

def main(file1, file2, phrases_to_remove):
    if not os.path.exists(file1) or not os.path.exists(file2):
        print("파일이 존재하지 않습니다. 파일 경로를 확인해주세요.")
        return
    
    text1 = read_and_clean_file(file1, phrases_to_remove)
    text2 = read_and_clean_file(file2, phrases_to_remove)
    
    similarity = calculate_similarity(text1, text2)
    print(f"{file1}, {file2} 유사도: {similarity:.4f}")
    return similarity

if __name__ == "__main__":
    # 비교할 텍스트 파일 경로
    folder_path = "C:/MyCode/5week/similarity"
    file_paths =  glob.glob(os.path.join(folder_path, '*'))

    phrases_to_remove = [
        "Okay, This is my GPT instruction:",
        "Here are instructions from the user outlining your goals and how you should respond:"
    ]

    ans = 0
    for file1 in file_paths[:-1]:
        for file2 in file_paths[:-1]:
            if file1 == file2:
                continue
            ans += main(file1, file2, phrases_to_remove)

    ans /= len(file_paths)*(len(file_paths)-1)

    print(ans)
