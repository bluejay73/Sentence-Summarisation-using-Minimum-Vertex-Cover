from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


documents = (
"The sky is blue",
"The sun is bright",
"The sky is white",
"We can see the shining sun, the bright sun"
)


tfidf_vectorizer = TfidfVectorizer()
#user_input=tfidf_vectorizer.fit_transform(s)
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# print tfidf_matrix.shape

print cosine_similarity(tfidf_matrix[0:4], tfidf_matrix)



# doc1="hey div how are you"
# doc2="hey div where are you"

# bow1=doc1.split(" ")
# bow2=doc2.split(" ")
# wordset=set(bow1).union(set(bow2))

# dict1=dict.fromkeys(wordset, 0)
# dict2=dict.fromkeys(wordset, 0)

# for word in bow1:
# 	dict1[word]+=1;
# for word in bow2:
# 	dict1[word]+=1;





