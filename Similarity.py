"""
Python Similarity methods
Author: William Hsu
21/August/2016
"""

def holiday_type(query_case, source_case):
	holiday_type_dict = {'Active': 0, 'Bathing': 1, 'Education': 2, 'Language': 3,
	 					'Recreation': 4, 'Skiing': 5, 'Wandering': 6}
	query_case_holiday_type = holiday_type_dict[query_case.holiday_type]
	source_case_holiday_type = holiday_type_dict[source_case.holiday_type]
	holiday_type_matrix =  [[1.0, 0.5, 0.0, 0.0, 0.5, 1.0, 0.7],
							[0.5, 1.0, 0.0, 0.0, 0.9, 0.3, 0.6],
							[0.0, 0.0, 1.0, 0.8, 0.1, 0.2, 0.1],
							[0.0, 0.0, 1.0, 1.0, 0.5, 0.0, 0.0],
							[0.5, 0.9, 0.1, 0.5, 1.0, 0.6, 0.9],
							[1.0, 0.3, 0.2, 0.0, 0.6, 1.0, 0.3],
							[0.7, 0.2, 0.1, 0.2, 0.9, 0.3, 1.0]]
	similarity = holiday_type_matrix[query_case_holiday_type][source_case_holiday_type]
	return similarity

def price(query_case, source_case):
	query_price = query_case.price	
	source_price = source_case.price
	if source_price <= query_price:
		similarity = 1.0
	else:
		upper_bound = query_price * 1.5
		if source_price >= upper_bound:
			similarity = 0.0
		else:
			difference_tolerance = upper_bound - query_price
			difference = source_price - query_price
			similarity = (difference_tolerance - difference)/difference_tolerance
	return similarity

def number_of_persons(query_case, source_case):
	query_number_of_persons = query_case.number_of_persons
	source_number_of_persons = source_case.number_of_persons
	if source_number_of_persons < query_number_of_persons:
		similarity = 0.0
	elif source_number_of_persons == query_number_of_persons:
		similarity = 1.0
	else:
		upper_bound = query_number_of_persons * 1.5
		if source_number_of_persons >= upper_bound:
			similarity = 0.0
		else:
			difference_tolerance = upper_bound - query_number_of_persons
			difference = source_number_of_persons - query_number_of_persons
			similarity = (difference_tolerance - difference)/difference_tolerance
	return similarity

def region(query_case, source_case):
	
	Island = ["Attica", "Bornholm", "Corfu", "Corsica", "Crete", "Cyprus", "Fuerteventura", "GranCanaria",
			  "Ibiza", "Ireland", "Lanzarote", "Lolland", "Mallorca", "Malta", "Rhodes", "Teneriffe"]
	Mountains = ["Alps", "Attica", "Bavaria", "BlackForest", "Carinthia", "Chalkidiki", "Corfu", "Corisca",
				"Crete", "Cyprus", "Dolomites", "ErzGebirge", "GiantMountains", "Harz", "Lanzarote", 
				"LowerAustria", "Rhodes", "SalzbergerLand", "Salzkammergut", "Tyrol"]
	City = ["Cairo", "London", "Paris"]
	Country = ["Allgaeu", "Algarve", "Bavaria", "BlackForest", "Bornholm", "Brittany", "Carinthia", "Corfu",
			   "Corsica", "CostaBlanca", "CostaBrava", "CotedAzur", "Crete", "Cyprus", "Fuerteventura", 
			   "GranCanaria", "Harz", "HighTatra", "Normandy", "Lanzarote", "Lolland", "LowerAustria",
			   "Madeira", "Mallorca", "Malta", "SalzbergerLand", "Salzkammergut", "Teneriffe", "Thuringia",
			   "Tunisia", "Tyrol", "Wales"]
	Coast = ["AdriaticSea", "Algarve", "Attica", "Bornholm", "Brittany", "Chalkidiki", "Corfu", "CostaBlanca",
			 "CostaBrava", "CotedAzur", "Crete", "Cyprus", "Fano", "Fuerteventura", "GranCanaria", "Ibiza",
			 "Normandy", "Lanzarote", "Lolland", "Madeira", "Malta", "Rhodes", "Riviera", "Salzkammergut",
			 "Teneriffe", "Tunisia", "TurkishRiveria", "Wales"]
	Waters = ["AdriaticSea", "Algarve", "Attica", "Balaton", "BlackForest", "Bornholm", "Brittany", "Cairo", 
			  "Carinthia", "Chalkidiki", "Corfu", "CostaBlanca", "CostaBrava", "CotedAzur", "Crete", "Cyprus", 
			  "Fano", "Fuerteventura", "Harz", "HighTatra", "Normandy", "LakeGarda", "GranCanaria", "Ibiza",
			  "Lanzarote", "Lolland", "LowerAustria", "Madeira", "Mallorca", "Malta", "Paris", "Rhodes", 
			  "Riviera", "Salzkammergut","Styria", "Teneriffe", "Thuringia", "Tunisia", "TurkishRiveria", "Wales"]
	Lake = ["Balaton", "BlackForest", "Carinthia", "Crete", "Harz", "HighTatra", "LakeGarda", "Salzkammergut",
			"Styria"     ]
	Sea = ["AdriaticSea", "Atlantic", "BalticSea", "MediterraneanSea", "NorthSea", "TurkishAegeanSea"]
	#Nation categories
	"""
	Austria = ["Allgaeu", "Alps", "Carinthia", "LowerAustria", "SalzbergerLand", "Salzkammergut", "Styria",
			   "Tyrol", "Mountains", "Country", "Lake", "Waters"]
	Belgium = ["Atlantic", "NorthSea", "Coast", "Waters"]
	Bulgaria = ["Allgaeu", "Mountains", "Country", "Coast", "Waters"]
	Malta = ["MediterraneanSea", "Island", "Coast", "Waters"]
	Cyprus = ["MediterreaneanSea", "Island", "Coast", "Waters", "Mountains"]
	Czechia = ["ErzGebirge", "GiantMountains", "Country", "Mountains"]
	Denmark = ["BalticSea", "Bornholm", "Lolland", "Coast", "Waters"]
	Egypt = ["Cairo", "Coast", "Waters", "City", "MediterraneanSea"]
	France = ["Alps", "Atlantic", "Brittany", "Corsica", "CotedAzur", "Normandy", "NorthSea", "Paris", "Riviera",
			  "City", "Country", "Coast", "Mountains", "Waters"]
	Germany = ["Allgaeu", "Alps", "Atlantic", "BalticSea", "Bavaria", "BlackForest", "ErzGebirge", "Harz", 
			   "NorthSea", "Thuringia", "Lake", "Country", "Coast", "Mountains", "Waters"]
	Greece = [" 
	Holland = ["Atlantic", "NorthSea", "Coast", "Waters", "Country"]
	Hungaria = ["Balaton", "Country", "Lake"]
	Ireland = ["Alantic", "Island", "Country"]
	Italy = ["AdriaticSea", "Dolomites", "Fano", "LakeGarda", "Riviera", "Tyrol", "Coast", "Waters", "Mountain",
			 "Lake"] 
	Malta = ["MediterraneanSea", "Island", "Coast", "Waters"]
	Morocco = ["Atlantic", "Coast", "Waters"]
	Poland = ["BalticSea", "GiantMountains", "HighTatra", "Coast", "Country", "Mountains", "Lake", "Waters"]
	Portugal = ["Algarve", "Atlantic", "Madeira", "Coast", "Waters"]
	Slowakei = ["Country", "Mountain"]
	Spain = ["Atlantic", "CostaBlanca", "CostaBrava", "Fuerteventura", "GranCanaria", "Ibiza", "Lanzarote", 
			 "Mallorca", "Teneriffe", "Coast", "MediterraneanSea", "Country", "Waters"]
	Sweden = ["BalticSea", "NorthSea", "Coast", "Country", "Waters"]
	Switzerland = ["Alps", "Country", "Mountains"]
	Tunisia = ["Country", "Coast", "Waters", "MediterraneanSea"]
	Turkey = ["TurkishAegeanSea", "TurkishRiviera", "MediterraneanSea", "Coast", "Waters"]
	UnitedKingdom = ["Atlantic", "England", "Wales", "Scotland", "Ireland", "NorthSea", "London", "City"]
	Atlantic = ["Sweden", "Spain", "Morocco", "Ireland", "Holland", "Germany", "France", "Belgium", "BalticSea",
				"Bornholm", "Brittany", "Fuerteventura", "GranCanaria", "NorthSea", "Madiera", "Teneriffe"]
	BalticSea = ["Bornholm", "Poland", "Sweden", "Germany", "Holland", "Lolland"]
	MediterraneanSea = ["Corsica", "CostaBlanca", "CotedAzur", "Crete", "Cyprus", "Ibiza", "Tunisia", "Mallorca",
						"Maltas", "TurkishRiviera", "Tunisia"]
	"""
def transportation(query_case, source_case):
	transportation_dict = {"Arbitrary": 0, "Car": 1, "Coach": 2, "Train": 3, "Plane": 4}
	query_case_transportation = transportation_dict[query_case.transportation]
	source_case_transportation = transportation_dict[source_case.transportation]
	transportation_matrix = [[1.0, 1.0, 1.0, 1.0, 1.0],
							 [0.0, 1.0, 0.7, 0.5, 0.2],
							 [0.0, 0.3, 1.0, 0.7, 0.5],
							 [0.0, 0.3, 0.7, 1.0, 0.5],
							 [0.0, 0.2, 0.5, 0.5, 1.0]]
	similarity = transportation_matrix[query_case_transportation][source_case_transportation]
	return similarity

def duration(query_case, source_case):  #range between 1 and 56
	query_case_duration = query_case.duration
	source_case_duration = source_case.duration
	if query_case_duration == 1:
		if source_case_duration == 1:
			similarity = 1.0
		elif source_case_duration == 2:
			similarity = 0.5
		else:
			similarity = 0.0
	elif query_case_duration > 1:# check 
		accept_range = math.ceil(query_case_duration *0.1)
		bound = accept_range + 1
		if source_case_duration > query_case_duration - bound and \
			source_case_duration < query_case_duration + bound:
			step_size = 1.0 /bound
			difference = math.fabs(query_case_duration - source_case_duration)
			similarity  = 1.0 - (difference * step_size)
		else:
			similarity = 0.0
	return similarity

#reconsider this method... use matrix		
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

def accommodation(query_case, source_case):
	accommodation_type_dict = {"Arbitrary": 0, "HolidayFlat": 0, "OneStar": 1, "TwoStars": 2,
	 							"ThreeStars": 3, "FourStars": 4, "FiveStars": 5}
	query_accommodation_type = accommodation_type_dict[query_case.accommodation]
	source_accommodation_type = accommodation_type_dict[source_case.accommodation]
	accommodation_type_matrix = [[1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
								 [0.7, 1.0, 1.0, 1.0, 1.0, 1.0],
								 [0.4, 0.7, 1.0, 1.0, 1.0, 1.0],
								 [0.1, 0.4, 0.7, 1.0, 1.0, 1.0],
								 [0.0, 0.1, 0.4, 0.7, 1.0, 1.0],
								 [0.0, 0.0, 0.1, 0.4, 0.7, 1.0]]
	similarity = accommodation_type_matrix[query_accommodation_type][source_accommodation_type]
	return similarity