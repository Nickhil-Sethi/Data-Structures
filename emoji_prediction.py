import numpy as np
import pandas as pd

from collections import OrderedDict
from sklearn.feature_extraction.text import CountVectorizer

class TweetData(object):
	def __init__(self,tweet_file='/Users/Nickhil_Sethi/Documents/Datasets/emogi/tweets.txt',emoji_file='/Users/Nickhil_Sethi/Documents/Datasets/emogi/emoji.txt'):
		print "loading data..."
		self.tweets 		 = pd.read_table(tweet_file, header=False)
		self.emoji  		 = pd.read_table(emoji_file, header=False)
		print "data loaded.\n"
		
	# munge data, add features, and write to csv
	def process(self):
		self.data   		 = pd.DataFrame.join(self.tweets,self.emoji)
		self.data.columns 	 = ['tweet','emoji']
		
		print "adding has_url column..."
		self.data['has_url'] = pd.DataFrame([1. if 'http' in self.data.loc[idx,'tweet'] else 0. for idx in self.data.index])
		
		print "adding has_tag columns..."
		self.data['has_tag'] = pd.DataFrame([1. if '@' in self.data.loc[idx,'tweet'] else 0. for idx in self.data.index])

		self.data.to_csv('/Users/Nickhil_Sethi/Documents/Datasets/emogi/combined_data.csv',headers=True)
		return

	def vectorize(self,threshold=30,load_file='/Users/Nickhil_Sethi/Documents/Datasets/emogi/combined_data.csv'):
		self.data            = pd.read_csv(load_file)
		vocab 				 = OrderedDict()
		for i in self.data.index:
			for word in set(self.data.loc[i,'tweet'].split(' ')):
				if word in vocab:
					vocab[word] += 1
				else:
					vocab[word]  = 1

		for word in vocab:
			if vocab[word] < threshold:
				vocab.pop(word)

		countvec 		 	= CountVectorizer(vocabulary=vocab.keys())
		countvec.fit_transform(self.data['tweet'])

		print countvec.get_feature_names()
		print countvec.fit_transform()

	def shuffle(self):
		self.data 		    = self.data.sample(1.)

	def feature_normalization(self,train, test):
	    (N,p)   			= np.shape(train)
	    mins    			= np.amin(train,axis=0)
	    maxs    			= np.amax(train,axis=0) + mins
	    train   			= (train + mins)/maxs
	    test    			= (test  + mins)/maxs
	    return train, test

if __name__=='__main__':
	T 			= TweetData()
	T.vectorize()