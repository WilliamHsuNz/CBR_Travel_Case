"""
Python Similarity methods
Author: William Hsu
21/August/2016
"""

def holiday_type(query_case, source_case):
	holiday_type_dict = {'Active': 0, 'Bathing': 1, 'Education': 2, 'Language': 3,
	 					'Recreation': 4, 'Skiing': 5, 'Wandering': 6}
	holiday_type_matrix =  [[1.0, 0.5, 0.0, 0.0, 0.5, 1.0, 0.7],
							[0.5, 1.0, 0.0, 0.0, 0.9, 0.3, 0.6],
							[0.0, 0.0, 1.0, 0.8, 0.1, 0.2, 0.1],
							[0.0, 0.0, 1.0, 1.0, 0.5, 0.0, 0.0],
							[0.5, 0.9, 0.1, 0.5, 1.0, 0.6, 0.9],
							[1.0, 0.3, 0.2, 0.0, 0.6, 1.0, 0.3],
							[0.7, 0.2, 0.1, 0.2, 0.9, 0.3, 1.0]]
	similarity = holiday_type_matrix[holiday_type_dict[query_case.holiday_type]][holiday_type_dict[source_case.holiday_type]]
	return similarity
	
def season(query_case, source_case):
	season_dict =  {'January': 0, 'February': 1, 'March': 2, 'April': 3, 'May': 4, 
					'June': 5, 'July': 6, 'August': 7, 'September': 8, 'October': 9,
					'November': 10, 'December': 11}
	query_seaon = season_dict[query_case.season]
	source_season = season_dict[source_case.season]
	difference = abs(query_season - source_season) 
	if difference > 6:
		min_season = min(query_season, source_season)
		max_season = max(query_season, source_season)
		difference = abs(max_season - (min_season + 12))
	similarity = 1.0 - (difference * 0.2)
	if similarity < 0.0:
		similarity = 0.0
	return similarity
	