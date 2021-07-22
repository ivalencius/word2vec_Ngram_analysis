import numpy
import scipy
import cython
import gensim
from gensim import models, similarities
import logging
import os
import re
import sys  
import itertools
import math
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.models import Word2Vec

# ***** SWITCH TO FASTTEXT: https://radimrehurek.com/gensim/models/fasttext.html *****
##year_1 and year_2 comprise the time period of ngrams to read##
year_1=1940
year_2=1949

# Make sure paths are absolute: using '/'
DATA_BASE_PATH = '/media/ilanv/Backup Plus/nGram_download_and_sort/sorted_nGrams'
MODEL_BASE_PATH = '/media/ilanv/Backup Plus/R_nGram_analysis/Models/'

#reload(sys)  
#sys.setdefaultencoding('utf8')
#.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# Switch to this
#from gensim.test.utils import datapath
#sentences = LineSentence(datapath('lee_background.cor'))
data_filename = os.path.join(DATA_BASE_PATH, str(year_1)+'_'+str(year_2)+'.txt')
# sentences = []
# with open(data_filename, 'r') as f:
#     for line in f:
#         sentences.append(line.split(' '))
# print("DONE SPLITING SENTENCES")

# ***** CREATE CALLBACKS *****
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# ***** CREATE ITERATOR *****
from gensim.test.utils import datapath
from gensim.models.word2vec import LineSentence
sentences = LineSentence(datapath(data_filename))
###Set parameters. Details here: https://radimrehurek.com/gensim/models/word2vec.html###
model = gensim.models.word2vec.Word2Vec(sentences,sg=1, vector_size=300, window=5, min_count=10, workers=4, hs=0, negative=8)

# Save Model
from gensim.models import KeyedVectors
new_model = Word2Vec.load('/media/ilanv/Backup Plus/R_nGram_analysis/Models/w2vmodel_ng5_1940_1949_full')
#new_model = KeyedVectors.load_word2vec_format('/media/ilanv/Backup Plus/R_nGram_analysis/Models/w2vmodel_ng5_1940_1949_full')
#word_vectors = new_model.wv
#word_vectors.save(MODEL_BASE_PATH+'1900_1949_vectors.kv')
#word_vectors.save(MODEL_BASE_PATH+'/1940-1949_vectors.bin')
new_model.KeyedVectors.save_word2vec_format(MODEL_BASE_PATH+'1940_1949_vectors.bin', binary=True)
#model.save(MODEL_BASE_PATH+'/w2vmodel_ng5_'+str(year_1)+'_'+str(year_2)+'_full')

#vector=word_vectors["war"]
##output vector space##
#vectors_object=new_model.wv.vectors
#numpy.savetxt('svectors_'+str(year_1)+'_'+str(year_2)+'_full.txt',vectors_object,delimiter=" ")

#output vocab list#
#vocab_list = model.wv.index2word
#for i in range(0,len(vocab_list)):
# 	if vocab_list[i] == '':
#		vocab_list[i] = "thisisanemptytoken"+str(i)
#
#with open('vocab_list_'+str(year_1)+'_'+str(year_2)+'_full.txt','wb') as outfile:
#    for i in range(0,len(vocab_list)):
#       outfile.write(vocab_list[i].encode('utf8')+"\n".encode('ascii'))
