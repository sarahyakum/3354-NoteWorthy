# this file implements a function that retrieves the top n artists/songs from the database (.csv file passed from another function)
import pandas as pd

class Chart:
	def __init__(self, filename):
		self.filename = filename
		df = pd.read_csv(filename, encoding="ISO-8859-1")

		df["streams"] = pd.to_numeric(df["streams"], errors="coerce", downcast="integer")
		self.df = df

	def get_top(self, n, category):
		df = self.df
		if category == "songs":
			topn = df.nlargest(n, "streams")[["track_name", "artist(s)_name", "streams"]]
			return topn.set_index(pd.Index(range(1, n+1)))
		elif category == "artists":
			counts = df["artist(s)_name"].str.split(", ").explode().value_counts()
			topn = counts.reset_index(name="songs").nlargest(n, "songs")
			return topn
		else:
			pass

# chart = Chart("spotify-2023.csv")
# c = chart.get_top(3, "artists")
# print(c.to_dict())