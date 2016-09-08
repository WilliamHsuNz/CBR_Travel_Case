import math
"""
Python Similarity methods
Author: William Hsu
21/August/2016
"""

def holiday_type(query_case, source_case):
	type_list = ['Arbitrary', 'Active', 'Adventure', 'Bathing', 'City', 'Diving', 
				'Education', 'Language', 'Recreation', 'Skiing', 'Shopping', 
				'Surfing', 'Wandering']
	holiday_type_dict = {'Arbitrary': 0, 'Active': 1, 'Adventure': 2, 'Bathing': 3,
	 					'City': 4, 'Diving': 5, 'Education': 6, 'Language': 7,
				 		'Recreation': 8, 'Skiing': 9, 'Shopping': 10, 'Surfing': 11,
						'Wandering': 12}
	holiday_type_matrix =  [[0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
							[0.0, 1.0, 0.8, 0.5, 0.0, 0.4, 0.0, 0.0, 0.7, 0.4, 0.0, 0.4, 0.4],
							[0.0, 0.7, 1.0, 0.4, 0.0, 0.5, 0.0, 0.0, 0.6, 0.5, 0.0, 0.5, 0.4],
							[0.0, 0.5, 0.3, 1.0, 0.5, 0.7, 0.0, 0.0, 0.4, 0.0, 0.0, 0.7, 0.0],
							[0.0, 0.0, 0.0, 0.4, 1.0, 0.0, 0.5, 0.5, 0.3, 0.0, 0.7, 0.0, 0.0],
							[0.0, 0.5, 0.4, 0.7, 0.0, 1.0, 0.0, 0.0, 0.4, 0.0, 0.0, 0.7, 0.0],
							[0.0, 0.0, 0.0, 0.0, 0.4, 0.0, 1.0, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0],
							[0.0, 0.0, 0.0, 0.0, 0.4, 0.0, 0.7, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
							[0.0, 0.7, 0.7, 0.5, 0.5, 0.5, 0.0, 0.0, 1.0, 0.5, 0.5, 0.5, 0.5],
							[0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.3],
							[0.0, 0.0, 0.0, 0.0, 0.8, 0.0, 0.0, 0.0, 0.3, 0.0, 1.0, 0.0, 0.0],
							[0.0, 0.5, 0.5, 0.7, 0.0, 0.8, 0.0, 0.0, 0.5, 0.0, 0.0, 1.0, 0.0],
							[0.0, 0.6, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.2, 0.0, 0.0, 1.0],
							[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
	if query_case.holiday_type not in type_list:
		query_case_holiday_type = 13 #'Other'
	else:
		query_case_holiday_type = holiday_type_dict[query_case.holiday_type]
		source_case_holiday_type = holiday_type_dict[source_case.holiday_type]
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
	else:
###############################################################################	
		Nations = ["Austria", "Belgium", "Bulgaria", "Cyprus", "Czechia", "Denmark", 
				   "Egypt", "England", "France", "Germany", "Greece", "Holland", 
				   "Hungaria", "Ireland", "Italy", "Malta", "Morocco", "Poland",
				   "Portugal", "Scotland", "Slowakei", "Spain", "Sweden", 
				   "Switzerland", "Tunisia", "Turkey", "UnitedKingdom", "Wales"]
		Nations_List = []
		Nations_List.append(["Carinthia", "LowerAustria", "SalzbergerLand", 
							 "Salzkammergut", "Styria", "Tyrol"]) # Austria
		Nations_List.append([]) #Belgium
		Nations_List.append([]) #Bulgaria
		Nations_List.append([])#Cyprus
		Nations_List.append(["ErzGebirge"]) #Czechia
		Nations_List.append(["Bornholm", "Lolland"])#Denmark
		Nations_List.append(["Cairo"])#Egypt
		Nations_List.append([])#England added London
		Nations_List.append(["Brittany", "Corsica", "CotedAzur", "Normandy", "Paris"])#France
		Nations_List.append([ "Bavaria", "BlackForest", "ErzGebirge", "Harz", "Thuringia"])#Germany
		Nations_List.append(["Attica", "Chalkidiki", "Corfu", "Crete", "Rhodes"])#Greece
		Nations_List.append([])#Holland
		Nations_List.append(["Balaton"])#Hungaria
		Nations_List.append([])#Ireland
		Nations_List.append(["Dolomites", "Fano", "LakeGarda"])#Italy
		Nations_List.append([])#Malta
		Nations_List.append([])#Morocco
		Nations_List.append(["HighTatra"])#Poland
		Nations_List.append(["Algarve", "Madeira"])#Portugal
		Nations_List.append([])#Scotland
		Nations_List.append([])#Slowakei
		Nations_List.append(["CostaBlanca", "CostaBrava", "Fuerteventura", "GranCanaria", 
							 "Ibiza", "Lanzarote", "Mallorca", "Teneriffe"])#Spain
		Nations_List.append([])#Sweden
		Nations_List.append([])#Switzerland
		Nations_List.append([])#Tunisia
		Nations_List.append(["TurkishAegeanSea", "TurkishRiviera"])#Turkey
		Nations_List.append(["England", "Wales", "Scotland", "Ireland", "London"])#UnitedKingdom
		Nations_List.append([])#Wales
		#check "is" relationship (regions that belong to nations) 
		if query_case_region in Nations:# bug when using England
			index = Nations.index(query_case_region)
			if source_case_region in Nations_List[index]:
				similarity = 1.0
				return similarity
		#handle case where the holiday type is Language
		if query_case.holiday_type == "Language": #changed from elif to if 
			similarity = 0.0
			for n in Nations_List:
				if query_case_region in n:
					if source_case_region in n:
						similarity = 1.0
						return similarity
					else:
						similarity = 0.0
						return similarity
			#return similarity		
		else:  #changed from else to elif
###############################################################################	
			#check "has" relationship (regions that shares similar features)   
			Island = ["Bornholm", "Corfu", "Corsica", "Crete", "Cyprus", 
					  "Fuerteventura", "GranCanaria", "Greece", "Ibiza", "Ireland",
					  "Lanzarote", "Lolland", "Mallorca", "Malta", "Rhodes", 
					  "Spain", "Teneriffe"]
			Mountains = ["Allgaeu", "Alps", "Austria", "Bavaria", "BlackForest", 
						 "Carinthia", "Chalkidiki", "Czechia", "Dolomites", 
						 "ErzGebirge", "France", "Germany", "GiantMountains", 
						 "Harz", "Italy",  "LowerAustria", "Poland", 
						 "SalzbergerLand", "Salzkammergut","Slowakei", "Switzerland",
						 "Thuringia", "Tyrol"]
			City = ["Cairo", "London", "Paris", "Egypt", "England", "France", 
					"UnitedKingdom"]
			Country = ["Austria", "Belgium","Bulgaria", "Czechia", "Denmark", 
					   "France", "Germany", "Greece", "Holland", "Hungaria", 
					   "Ireland", "Italy", "Morocco", "Poland", "Portugal", 
					   "Slowakei", "Spain", "Sweden", "Switzerland","Scotland", 
					   "Turkey", "Tyrol", "UnitedKingdom", "Wales"]
			Coast = ["AdriaticSea", "Algarve", "Attica", "Belgium", 
					 "Bulgaria", "Brittany", "Chalkidiki", "CostaBlanca", 
					 "CostaBrava", "CotedAzur", "Denmark", "Egypt", 
					 "Fano", "France", "Germany",  
					 "Greece", "Holland", "Ireland", "Italy", "Normandy", 
					 "Lanzarote", "Madeira", "Morocco","Poland",
					 "Portugal", "Riviera", "Salzkammergut", "Spain", 
					 "Sweden", "Tunisia", "Turkey", "TurkishRiveria"]
			Waters = ["AdriaticSea", "Austria", "Belgium", "Brittany","Bulgaria", 
					  "Cairo", "Corfu", "Denmark", "Egypt", "France", "Germany", 
					  "Greece", "Holland", "Ireland", "Italy", "Madeira", "Mallorca", 
					  "Malta", "Morocco", "Poland", "Portugal", "Riviera", 
					  "Salzkammergut", "Spain", "Sweden","Turkey", "TurkishRiveria", 
					  "UnitedKingdom", "Wales"]
			Lake = ["Austria", "Balaton", "BlackForest", "Carinthia", "Crete", "Germany",
					"Harz", "HighTatra", "Hungaria","Italy", "LakeGarda", "Poland", 
					"Salzkammergut", "Styria"]
			Sea = ["AdriaticSea", "Atlantic", "BalticSea", "MediterraneanSea", "NorthSea", 
				   "TurkishAegeanSea"]
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
###############################################################################			

def transportation(query_case, source_case):
	transportation_dict = {"Arbitrary": 0, "Car": 1, "Coach": 2, "Train": 3, "Plane": 4}
	query_case_transportation = transportation_dict[query_case.transportation]
	source_case_transportation = transportation_dict[source_case.transportation]
	#handle cases where transport is restricted to plane
	islands_accessible_only_by_plane = ["Attica", "Corfu", "Corsica", "Crete", 
										"Cyprus", "Fuerteventura", "GranCanaria", 
										"Ibiza", "Ireland", "Lanzarote", "Lolland", 
										"Mallorca", "Malta", "Rhodes", "Teneriffe"]
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