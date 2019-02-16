from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from math import log10, floor
def cosine():
	f=open('doc', 'r')
	documents=f.readlines()

#print documents

	tfidf_vectorizer = TfidfVectorizer()
#user_input=tfidf_vectorizer.fit_transform(s)
	tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# print tfidf_matrix.shape

# def round_to_1(x):
# 	return round(x, 2-int(floor(log10(abs(x))))-1)
	a=cosine_similarity(tfidf_matrix[0:4], tfidf_matrix)
#print(a)
	for i in range(len(a)):
		for j in range(len(a[i])):
			print "%.2f"%a[i][j],
		print "\n"
def jaccard():
    documents= []
    with open('doc','r') as f:
        for line in f:
            documents.append(line)
    for i in range(len(documents)):
        for j in range(len(documents)):
            a=set(documents[i])
            b=set(documents[j])
            print('%.2f' %(1.0 * len(a&b)/len(a|b))),
        print("\n")
def levenshtein():
	from fuzzywuzzy import fuzz
	f=open('doc', 'r')
	documents=f.readlines()

	for i in range(len(documents)):
		for j in range(len(documents)):
			print float((fuzz.ratio(documents[i], documents[j])/100.0)),
		print"\n"
levenshtein()
jaccard()
cosine()