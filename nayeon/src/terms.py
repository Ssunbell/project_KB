import os
import numpy as np
import json
from konlpy.tag import Okt
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

os.chdir('../data')
okt = Okt()

class TermsSearcher():
    def __init__(self):
        with open('terms.json', 'r', encoding='utf-8') as f:
            self.terms = json.load(f)

        with open('terms_vectors.json', 'r', encoding='utf-8') as f:
            self.terms_vectors = json.load(f)
        
        self.titles = list(self.terms.keys())

        self.model = Word2Vec.load('terms_w2v')

        self.word_dict ={}
        for vocab in self.model.wv.index_to_key:
            self.word_dict[vocab] = self.model.wv[vocab]

        user_input = input('검색어를 입력하세요: ')
        self.input_tokens = okt.nouns(user_input)
        self.tokenized_input = ' '.join(self.input_tokens)

    def find_term(self):
        tokenized_titles = [' '.join(okt.nouns(title)) for title in self.titles]
        
        tfidf = TfidfVectorizer()
        tfidfv = tfidf.fit_transform(tokenized_titles)

        similarity = {}
        for i in range(len(self.titles)):
            sim = cosine_similarity(tfidf.transform([self.tokenized_input]).toarray(), 
                                    [i.toarray() for i in tfidfv][i])
            similarity[self.titles[i]] = float(sim)
        
        similarity = {key: value for key, value in sorted(similarity.items(), key=lambda item: item[1], reverse=True)}
        rating = [str(key) for key, value in sorted(similarity.items(), key=lambda item: item[1], reverse=True)]
        top = rating[0]

        self.find_detail(top)

    def find_detail(self, title):
        input_vectors = []
        for token in self.input_tokens:
            if token in self.word_dict.keys():
                input_vectors.append(self.word_dict[token])
        
        if len(input_vectors) != 0:
            user_vector = (np.sum(input_vectors, axis=0) / len(input_vectors)).tolist()
        else:
            user_vector = 0

        detail_similarity = {}
        if user_vector == 0:
            result = 0
        else:
            for key, value in self.terms_vectors[title].items():
                try:
                    detail_sim = cosine_similarity(np.array(user_vector).reshape(1, -1), 
                                           np.array([float(i) if i != '.' else float('0.0') for i in str(value)[1:-1].split(',')]).reshape(1, -1))
                except:
                    detail_sim = 0
                detail_similarity[key] = float(detail_sim)
            detail_similarity = {key: value for key, value in sorted(detail_similarity.items(), key=lambda item: item[1], reverse=True)}
            detail_rating = [str(key) for key, value in sorted(detail_similarity.items(), key=lambda item: item[1], reverse=True)]
            detail_top = detail_rating[:3]
            result = (title, detail_top)

        self.show_result(result)
    
    def show_result(self, result):
        if result == 0:
            print('일치하는 검색 결과가 없습니다.')
        else:
            print(result[0].strip(), '\n')
            for detail in result[1]:
                print(f'{detail}: {self.terms[result[0]][detail]}\n')
    
ts = TermsSearcher()
ts.find_term()