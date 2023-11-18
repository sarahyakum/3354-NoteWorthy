# this file is the unit test code for a sample unit (written in the file get_top.py)
# this unit test uses both the standard python unittest library as well as the built-in pandas testing module to compare the equivalence of two dataframes
# assumptions: this is not a comprehensive implementation of all possible tests we would run; this is only a select group that is representative of the majority of test cases, including edge cases where only one item in the database is displayed or returned

import unittest
import pandas as pd
from get_top import Chart

class TestGetTop(unittest.TestCase):
	def setUp(self):
		self.chart = Chart("spotify-2023.csv")

	def test_top5songs_success(self):
		expected_df = pd.DataFrame.from_dict({"track_name": {1: "Blinding Lights", 2: "Shape of You", 3: "Someone You Loved", 4: "Dance Monkey", 5: "Sunflower - Spider-Man: Into the Spider-Verse"}, "artist(s)_name": {1: "The Weeknd", 2: "Ed Sheeran", 3: "Lewis Capaldi", 4: "Tones and I", 5: "Post Malone, Swae Lee"}, "streams": {1: 3703895074.0, 2: 3562543890.0, 3: 2887241814.0, 4: 2864791672.0, 5: 2808096550.0}})
		try:
			pd.testing.assert_frame_equal(self.chart.get_top(5, "songs"), expected_df)
		except AssertionError:
			raise AssertionError("FAILED: query for top 5 songs")
	def test_top5songs_failure(self):
		expected_df = pd.DataFrame.from_dict({"track_name": {1: "Blinding Lights", 2: "Shape of You", 3: "Someone You Loved", 4: "Hotel Room Service", 5: "Sunflower - Spider-Man: Into the Spider-Verse"}, "artist(s)_name": {1: "The Weeknd", 2: "Ed Sheeran", 3: "Lewis Capaldi", 4: "Pitbull", 5: "Post Malone, Swae Lee"}, "streams": {1: 3703895074.0, 2: 3562543890.0, 3: 2887241814.0, 4: 2864791672.0, 5: 2808096550.0}})
		try:
			pd.testing.assert_frame_equal(self.chart.get_top(5, "songs"), expected_df)
		except AssertionError:
			raise AssertionError("FAILED: query for top 5 songs") 

	def test_top10songs_success(self):
		expected_df = pd.DataFrame.from_dict({"track_name": {1: "Blinding Lights", 2: "Shape of You", 3: "Someone You Loved", 4: "Dance Monkey", 5: "Sunflower - Spider-Man: Into the Spider-Verse", 6: "One Dance", 7: "STAY (with Justin Bieber)", 8: "Believer", 9: "Closer", 10: "Starboy"}, "artist(s)_name": {1: "The Weeknd", 2: "Ed Sheeran", 3: "Lewis Capaldi", 4: "Tones and I", 5: "Post Malone, Swae Lee", 6: "Drake, WizKid, Kyla", 7: "Justin Bieber, The Kid Laroi", 8: "Imagine Dragons", 9: "The Chainsmokers, Halsey", 10: "The Weeknd, Daft Punk"}, "streams": {1: 3703895074.0, 2: 3562543890.0, 3: 2887241814.0, 4: 2864791672.0, 5: 2808096550.0, 6: 2713922350.0, 7: 2665343922.0, 8: 2594040133.0, 9: 2591224264.0, 10: 2565529693.0}})
		try:
			pd.testing.assert_frame_equal(self.chart.get_top(10, "songs"), expected_df)
		except AssertionError:
			raise AssertionError("FAILED: query for top 10 songs")
	def test_top10songs_failure(self):
		expected_df = pd.DataFrame.from_dict({"track_name": {1: "Never Gonna Give You Up", 2: "Shape of You", 3: "Someone You Loved", 4: "Dance Monkey", 5: "Sunflower - Spider-Man: Into the Spider-Verse", 6: "One Dance", 7: "STAY (with Justin Bieber)", 8: "Believer", 9: "Closer", 10: "Starboy"}, "artist(s)_name": {1: "Rick Astley", 2: "Ed Sheeran", 3: "Lewis Capaldi", 4: "Tones and I", 5: "Post Malone, Swae Lee", 6: "Drake, WizKid, Kyla", 7: "Justin Bieber, The Kid Laroi", 8: "Imagine Dragons", 9: "The Chainsmokers, Halsey", 10: "The Weeknd, Daft Punk"}, "streams": {1: 3703895074.0, 2: 3562543890.0, 3: 2887241814.0, 4: 2864791672.0, 5: 2808096550.0, 6: 2713922350.0, 7: 2665343922.0, 8: 2594040133.0, 9: 2591224264.0, 10: 2565529693.0}})
		try:
			pd.testing.assert_frame_equal(self.chart.get_top(10, "songs"), expected_df)
		except AssertionError:
			raise AssertionError("FAILED: query for top 10 songs") 

	def test_top3artists_success(self):
		expected_df = pd.DataFrame.from_dict({"artist(s)_name": {0: "Bad Bunny", 1: "Taylor Swift", 2: "The Weeknd"}, "songs": {0: 40, 1: 38, 2: 37}})
		try:
			pd.testing.assert_frame_equal(self.chart.get_top(3, "artists"), expected_df)
		except AssertionError:
			raise AssertionError("FAILED: query for top 3 artists")
	def test_top3artists_failure(self):
		expected_df = pd.DataFrame.from_dict({"artist(s)_name": {0: "Bugs Bunny", 1: "SpongeBob SquarePants", 2: "The Weeknd"}, "songs": {0: 40, 1: 38, 2: 37}})
		try:
			pd.testing.assert_frame_equal(self.chart.get_top(3, "artists"), expected_df)
		except AssertionError:
			raise AssertionError("FAILED: query for top 3 artists") 

	def test_top1artist_success(self):
		expected_df = pd.DataFrame.from_dict({"artist(s)_name": {0: "Bad Bunny"}, "songs": {0: 40}})
		try:
			pd.testing.assert_frame_equal(self.chart.get_top(1, "artists"), expected_df)
		except AssertionError:
			raise AssertionError("FAILED: query for number 1 artist")
	def test_top1artist_failure(self):
		expected_df = pd.DataFrame.from_dict({"artist(s)_name": {0: "Bad Bunny"}, "songs": {0: 12}})
		try:
			pd.testing.assert_frame_equal(self.chart.get_top(1, "artists"), expected_df)
		except AssertionError:
			raise AssertionError("FAILED: query for number 1 artist") 

suite = unittest.TestLoader().loadTestsFromTestCase(TestGetTop)
runner = unittest.TextTestRunner()
runner.run(suite)