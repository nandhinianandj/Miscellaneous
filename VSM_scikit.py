#Vector Space Model-- Text feature extraction
#Example using scikit from a blog post.

train_set = ("The sky is blue","The sun is bright")
test_set = ("The sun in the sky is bright","We can see the shining sun, the bright sun.")

from scikit.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
print vectorizer
#CountVectorizer(analyzer__min_n = 1,
#        analyzer__stop_words=set(['all','six','less','being','indeed','over','move','anyway','four','not','own','through','yourselves',(...)]))

vectorizer.fit_transform(train_set)
print vectorizer.vocabulary

smatrix = vectorizer.transform(test_set)
print smatrix

smatrix.todense()

