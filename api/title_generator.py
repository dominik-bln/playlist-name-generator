# -*- coding: utf-8 -*-
"""
@author: quintoe
"""

from __future__ import division
import pandas as pd
import numpy as np
# import gzip
# import json
import os
import gensim as gs
import nltk




class TitleGenerator():
    def __init__(self, *initial_data, **kwargs):
        # Initialise parameters from a config dictionary
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def load_data(self):
        # self.playlist_titles = pd.read_csv(self.playlist_titles_file, header=None,names=['user','playlist_uri','playlist_title'])
        self.playlist_titles = pd.read_csv(self.playlist_titles_file, header=0,names=['playlist_uri','playlist_title'])
        self.playlist_data = pd.read_csv(self.playlist_data_file)
        with open(os.path.join(self.centroids_mat_file), 'r') as f:
            self.centroid_mat = np.load(f) # Loads a binary file

    def load_word2vec_model(self,model_path):
        print 'loading Word2Vec model...'
        self.model = gs.models.KeyedVectors.load_word2vec_format(model_path, binary=True)

    def get_isrcs(self,input):
        '''Get the isrcs from data input'''
        isrcs=[]
        for d in input:
            isrcs.append(d['isrc'])
        return np.unique(isrcs)

    def get_paylist_uris(self,isrc):
        '''get the uris of playlists this isrc has been on'''
        playlist_uris = self.playlist_data.playlist_uri.loc[self.playlist_data.isrc==isrc].values
        return np.unique(playlist_uris)

    def get_playlist_titles(self,isrcs):
        '''get titles of playlists the isrcs have been on'''
        playlist_titles = []
        for isrc in isrcs:
            playlist_uris = self.get_paylist_uris(isrc)
            for playlist_uri in playlist_uris:
                playlist_titles.extend(self.playlist_titles.playlist_title.loc[self.playlist_titles.playlist_uri == playlist_uri].values)
        return np.unique(playlist_titles)

    def title_to_words(self,title):
        tokens = nltk.word_tokenize(title)
        return tokens

    def get_all_words(self, playlist_titles):
        words = []
        for playlist_title in playlist_titles:
            try:
                tokens = self.title_to_words(playlist_title)
                words.extend(tokens)
            except:
                pass
        return np.unique(words)

    def compute_vec(self,word):
        try:
            vec = self.model[word]
            return vec
        except:
            return np.array([None])

    def get_vecs(self,words):
        # print len(words)
        vecs = []
        for word in list(words):
            vec = self.compute_vec(word)
            if not (vec == None).any():
                vecs.append(list(vec))
        vecs = np.array(vecs)
        return vecs

    def match_centroids(self):
        title_words = []
        for k in range(np.shape(self.centroid_mat)[0]):
            title_word = self.model.most_similar(positive=[self.vec_mean,self.centroid_mat[k,:]], topn=1)[0][0]
            title_words.append(title_word)
        title = " ".join(title_words)
        return title


    def generate_title(self,input):
        print 'yyay'
        isrcs = self.get_isrcs(input)
        print 'yay isrcs'
        playlist_titles = self.get_playlist_titles(isrcs)
        print 'yay titles'
        words = self.get_all_words(playlist_titles)
        print 'yay words'
        vecs = self.get_vecs(words)
        print 'yay vecs'
        self.vec_mean = np.mean(vecs,axis=0)
        print ' Matching centroids'
        title = self.match_centroids()
        return title


_tg = None
def title_generator():
    global _tg
    if _tg is None:
        config = {
            'playlist_titles_file': '/data/playlist_titles_full.csv',
            'playlist_data_file': '/data/playlist_train_meta.csv',
            'centroids_mat_file': '/data/kmeans_mat'}

        google_model_path = '/data/GoogleNews-vectors-negative300.bin.gz'

        tg = TitleGenerator(config)
        tg.load_word2vec_model(google_model_path)
        print('Loading data...')
        tg.load_data()

if __name__ == "__main__":

    # config = {
    #     'playlist_titles_file': '/disk1/musicathon/data/playlist_titles_full.csv',
    #     'playlist_data_file': '/disk1/spotify_playlist_pitching/recommender/cf_recommender/playlists_raw_data/test_data23mar18/playlist_train_meta.csv',
    #     'savedir':'/disk1/musicathon/data'}
    # google_model_path = '/disk1/musicathon/word2vec_models/GoogleNews-vectors-negative300.bin.gz'

    config = {
        'playlist_titles_file': '/data/playlist_titles_full.csv',
        'playlist_data_file': '/data/playlist_train_meta.csv',
        'centroids_mat_file':'/data/kmeans_mat',
        'savedir': '/data'}
    google_model_path = '/data/GoogleNews-vectors-negative300.bin.gz'


    input = {"tracks":[{"isrc":"DELZ31500002","track_artist":"ASD","track_title":"Sneak Preview"},{"isrc":"GBAAP0100769","track_artist":"A","track_title":"Nothing"},{"isrc":"BRWMB1700345","track_artist":"Class A","track_title":"Nós dois"},{"isrc":"TWA471708011","track_artist":"A-Lin","track_title":"未單身"},{"isrc":"USRH11502698","track_artist":"a-ha","track_title":"Take on Me - Kygo Remix"},{"isrc":"SEBKA0013010","track_artist":"A*Teens","track_title":"Upside Down"},{"isrc":"TWA471607002","track_artist":"A-Lin","track_title":"天若有情 (電視劇「錦繡未央」主題曲) - Theme song of TV Drama \"Princess Weiyoung\""},{"isrc":"NLPM11620772","track_artist":"A Firma","track_title":"Fada"}]}

    tg = TitleGenerator(config)
    # tg.load_word2vec_model(google_model_path)
    print 'Loading data...'
    tg.load_data()
    tg.model = model
    print 'Running...'
    title = tg.generate_title(input['tracks'])



    print 'Saving data...'
    # ttv.save_data()
    # ttv.save_vec_mat()
