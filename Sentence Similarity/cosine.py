from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from math import log10, floor

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




