import math
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
	query_price = float(query_case.price)	
	source_price = float(source_case.price)
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
	query_number_of_persons = float(query_case.number_of_persons)
	source_number_of_persons = float(source_case.number_of_persons)
	if source_number_of_persons < query_number_of_persons:
		similarity = 0.0
	elif source_number_of_persons == query_number_of_persons:
		similarity = 1.0
	#handle special cases when query number of persons is 2 and 3	
	elif query_number_of_persons == 1:
		if source_number_of_persons == 2:
			similarity = 0.5
		else:
			similarity = 0.0
	elif query_number_of_persons == 2:
		if source_number_of_persons == 3:
			similarity = 0.5
		else:
			similarity = 0.0
	else:
	#handle general cases of query number of persons
		upper_bound = query_number_of_persons * 1.5
		if source_number_of_persons >= upper_bound:
			similarity = 0.0
		else:
			difference_tolerance = upper_bound - query_number_of_persons
			difference = source_number_of_persons - query_number_of_persons
			similarity = (difference_tolerance - difference)/difference_tolerance
	return similarity

def region(query_case, source_case):
	query_case_region = query_case.region 
	source_case_region = source_case.region
	if query_case_region == source_case_region:
		similarity = 1.0
		return similarity
	Nations = ["Austria", "Belgium", "Bulgaria", "Cyprus", "Czechia", "Denmark", "Egypt", "England", "France",
			   "Germany", "Greece", "Holland", "Hungaria", "Ireland", "Italy", "Malta", "Morocco", "Poland",
			   "Portugal", "Scotland", "Slowakei", "Spain", "Sweden", "Switzerland", "Tunisia", "Turkey", "UnitedKingdom",
			   "Wales"]
	Nations_List = []
	Nations_List.append(["Allgaeu", "Alps", "Carinthia", "LowerAustria", "SalzbergerLand", "Salzkammergut", 
						 "Styria", "Tyrol", "Mountains", "Country", "Lake", "Waters"]) # Austria
	Nations_List.append(["Atlantic", "NorthSea", "Coast", "Waters"]) #Belgium
	Nations_List.append(["Allgaeu", "Mountains", "Country", "Coast", "Waters"]) #Bulgaria
	Nations_List.append(["MediterreaneanSea", "Island", "Coast", "Waters", "Mountains"])#Cyprus
	Nations_List.append(["ErzGebirge", "GiantMountains", "Country", "Mountains"]) #Czechia
	Nations_List.append(["BalticSea", "Bornholm", "Lolland", "Coast", "Waters"])#Denmark
	Nations_List.append(["Cairo", "Coast", "Waters", "City", "MediterraneanSea"])#Egypt
	Nations_List.append([])#England
	Nations_List.append(["Alps", "Atlantic", "Brittany", "Corsica", "CotedAzur", "Normandy", "NorthSea", "Paris", 
						 "Riviera","City", "Country", "Coast", "Mountains", "Waters"])#France
	Nations_List.append(["Allgaeu", "Alps", "Atlantic", "BalticSea", "Bavaria", "BlackForest", "ErzGebirge", "Harz", 
						 "NorthSea", "Thuringia", "Lake", "Country", "Coast", "Mountains", "Waters"])#Germany
	Nations_List.append(["Attica", "Chalkidiki", "Corfu", "Crete", "Cyprus", "Rhodes", "Coast", "Waters", 
						 "MediterraneanSea", "Mountains"])#Greece
	Nations_List.append(["Atlantic", "NorthSea", "Coast", "Waters", "Country"])#Holland
	Nations_List.append(["Balaton", "Country", "Lake"])#Hungaria
	Nations_List.append(["Alantic", "Island", "Country"])#Ireland
	Nations_List.append(["AdriaticSea", "Dolomites", "Fano", "LakeGarda", "Riviera", "Tyrol", "Coast", "Waters", 
						 "Mountain", "Lake"])#Italy
	Nations_List.append(["MediterraneanSea", "Island", "Coast", "Waters"])#Malta
	Nations_List.append(["Atlantic", "Coast", "Waters"])#Morocco
	Nations_List.append(["BalticSea", "GiantMountains", "HighTatra", "Coast", "Country", "Mountains", "Lake", "Waters"])#Poland
	Nations_List.append(["Algarve", "Atlantic", "Madeira", "Coast", "Waters"])#Portugal
	Nations_List.append([])#Scotland
	Nations_List.append(["Country", "Mountain"])#Slowakei
	Nations_List.append(["Atlantic", "CostaBlanca", "CostaBrava", "Fuerteventura", "GranCanaria", "Ibiza", "Lanzarote", 
			 			 "Mallorca", "Teneriffe", "Coast", "MediterraneanSea", "Country", "Waters"])#Spain
	Nations_List.append(["BalticSea", "NorthSea", "Coast", "Country", "Waters"])#Sweden
	Nations_List.append(["Alps", "Country", "Mountains"])#Switzerland
	Nations_List.append(["Country", "Coast", "Waters", "MediterraneanSea"])#Tunisia
	Nations_List.append(["TurkishAegeanSea", "TurkishRiviera", "MediterraneanSea", "Coast", "Waters"])#Turkey
	Nations_List.append(["Atlantic", "England", "Wales", "Scotland", "Ireland", "NorthSea", "London", "City"])#UnitedKingdom
	Nations_List.append([])#Wales
	
	#if the query region is a nation
	if query_case_region in Nations:  
		index = Nations.index(query_case_region)
		if source_case_region in Nations_List[index]:
			similarity = 0.5
		else:
			similarity = 0.0
	#if the query region is not a nation
	else:
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
		Category_List = []
		Category_List.append(Island)
		Category_List.append(Mountains)
		Category_List.append(City)
		Category_List.append(Country)
		Category_List.append(Coast)
		Category_List.append(Waters)
		Category_List.append(Lake)
		Category_List.append(Sea)
		
		#form step function based on how many categories the query_case_region associates
		number_of_category_count = 0
		shared_category_count = 0
		for x in range(len(Category_List)):
			if query_case_region in Category_List[x]:
				number_of_category_count = number_of_category_count + 1
				if source_case_region in Category_List[x]:
					shared_category_count = shared_category_count + 1
		number_of_steps = number_of_category_count + 1
		similarity_value_for_each_step = 1.0/number_of_steps
		similarity = similarity_value_for_each_step * shared_category_count
	return similarity
			
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
	Greece = ["Attica", "Chalkidiki", "Corfu", "Crete", "Cyprus", "Rhodes", "Coast", "Waters", "MediterraneanSea", "Mountains"] 
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
	#handle cases where transport is restricted to plane
	islands_accessible_only_by_plane = ["Attica", "Corfu", "Corsica", "Crete", "Cyprus", "Fuerteventura", 
										"GranCanaria", "Ibiza", "Ireland", "Lanzarote", "Lolland", "Mallorca", 
										"Malta", "Rhodes", "Teneriffe"]
	if query_case.region in islands_accessible_only_by_plane:
		transportation_matrix = [[0.0, 0.0, 0.0, 0.0, 1.0],
								 [0.0, 0.0, 0.0, 0.0, 0.0],
								 [0.0, 0.0, 0.0, 0.0, 0.0],
								 [0.0, 0.0, 0.0, 0.0, 0.0],
								 [0.0, 0.0, 0.0, 0.0, 1.0]]
		similarity = transportation_matrix[query_case_transportation][source_case_transportation]
	#general case
	else:
		transportation_matrix = [[1.0, 1.0, 1.0, 1.0, 1.0],
							 	[0.0, 1.0, 0.7, 0.5, 0.2],
							 	[0.0, 0.3, 1.0, 0.7, 0.5],
							 	[0.0, 0.3, 0.7, 1.0, 0.5],
							 	[0.0, 0.2, 0.5, 0.5, 1.0]]
		similarity = transportation_matrix[query_case_transportation][source_case_transportation]
	return similarity

def duration(query_case, source_case):  #range between 1 and 56
	query_case_duration = float(query_case.duration)
	source_case_duration = float(source_case.duration)
	if query_case_duration == 1:
		if source_case_duration == 1:
			similarity = 1.0
		elif source_case_duration == 2:
			similarity = 0.5
		else:
			similarity = 0.0
	else: # query_case_duration > 1:
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
	query_season = season_dict[query_case.season]
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