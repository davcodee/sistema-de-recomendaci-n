#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd

PAINTINGS_MIN_AMOUNT = 50   # 2083 artistes  > garde 270
GENRES_MIN_AMOUNT = 1000   # garde 18/41 genres, vire 4100 peintures
STYLES_MIN_AMOUNT =  1760      #  128 styles, garde les 10 premiers

PATH = "all_data_info.csv"
"""
	animal painting              1005
	flower painting              1138
	design                       1214
	marina                       1234
	self-portrait                1250
	mythological painting        1305
	symbolic painting            1646
	figurative                   1668
	nude painting (nu)           1669
	illustration                 1707
	sketch and study             2411
	still life                   2508
	cityscape                    3551
	religious painting           5756
	abstract                     7989
	genre painting              10626
	landscape                   11349
	portrait                    12924

"""

def save_data(data):

	data.to_csv("data7.csv",sep="|")

def load_data():

	data = pd.read_csv(PATH)
	data = data.rename(columns={'artist':'artist', 'date':'date', 'genre':'genre', 'style':'style_name', 'title':'title'})   # data.style : object name already exists
	
	data = data.dropna()
	data = data.drop_duplicates()

	columns_name = ['artist','date','genre','style_name','title']

	data = data[columns_name]

	print("data shape"+str(data.shape[0]))

	return data

def clean_year_data(data):
	#virer les dates en c.1222

	data.date[data.date.str.contains("c")] = data.date.str[2:]

	#virer les données autre que forme "YYYY"

	a = data.date.str.match('^[0-9]{4}(\.[0])?$')
	data = data.loc[a.index]

	# reste forme Month YYY"

	data = data.drop(data.date[data.date.str.match('[a-zA-Z]')].index)

	data = data.dropna()

	return data

def data_selection(data):

	print("shape data "+str(data.shape))

	#virer les artistes avec moins de 5 peintures 
	artist = data.groupby('artist').size()
	data = data.drop(data[data.artist.isin(artist[artist < PAINTINGS_MIN_AMOUNT].index)].index)

	#virer genres avec moins de 1000 peintures
	genre = data.groupby('genre').size()
	data = data.drop(data[data.genre.isin(genre[genre < GENRES_MIN_AMOUNT].index)].index)

	#virer les styles avec moins de 

	style = data.groupby('style_name').size()
	data = data.drop(data[data.style_name.isin(style[style < STYLES_MIN_AMOUNT].index)].index)


	data = data.reset_index(drop = True)


	print("after selection, there is "+str(data.shape)+" paintings")

	return data


def analyse_style(data):
	style = data.groupby('style_name').size()
	style = style.sort_values()
	print("number of different styles :"+str(style.shape[0]))
	plt.figure(0)
	style.plot(x='styles',y='nb of paintings',rot=30)
	plt.title("style analyse")



def analyse_genre(data):
	genre = data.groupby('genre').size()
	genre = genre.sort_values()
	print("number of different genres : "+str(genre.shape[0]))
	plt.figure(1)
	genre.plot(x='genre',y='nb of paintings',rot=30)
	plt.title("genre analyse")

def analyse_artists(data):  # faire l'analize avec les données de départ, puis refaire apres
	artist = data.groupby('artist').size()
	artist = artist.sort_values()
	print("number of different artists : "+str(artist.shape[0]))
	plt.figure(2)
	artist.plot(x='artist',y='nb of paintings',rot=30)
	plt.title("artist analyse")


if __name__ == "__main__":

	data = load_data()

	print("Data analysis before cleaning :")
	analyse_genre(data)
	analyse_style(data)
	analyse_artists(data)
	plt.show()

	data = clean_year_data(data)
	data = data_selection(data)

	print("Data analysis after cleaning :")
	analyse_genre(data)
	analyse_style(data)
	analyse_artists(data)
	plt.show()

	save_data(data)
