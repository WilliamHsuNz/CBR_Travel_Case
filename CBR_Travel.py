import xlrd
from Case import Case
"""
CBR Travel Case
Author: William Hsu
19/August/2016
"""
		
cases = []
def read_in_cases():
	#workbook = xlrd.open_workbook('CASE/Test_Workbook.xlsx')
	workbook = xlrd.open_workbook('CASE/TRAVEL.XLS')
	print(workbook.nsheets)
	sheet = workbook.sheet_by_index(0)
	print(sheet.ncols)
	print(sheet.nrows)
	for row_index in range(0, sheet.nrows):
		if sheet.cell(row_index, 1).value == 'case':
			case = sheet.cell(row_index, 2).value
			journey_code = sheet.cell(row_index + 1, 2).value
			holiday_type = sheet.cell(row_index + 2, 2).value
			price = sheet.cell(row_index + 3, 2).value
			number_of_persons = sheet.cell(row_index + 4, 2).value
			region = sheet.cell(row_index + 5, 2).value
			transportation = sheet.cell(row_index + 6, 2).value
			duration = sheet.cell(row_index + 7, 2).value
			season = sheet.cell(row_index + 8, 2).value
			accommodation = sheet.cell(row_index + 9, 2).value
			hotel = sheet.cell(row_index + 10, 2).value
			#print(case, journey_code, holiday_type, price, number_of_persons, 
			#	region,transportation, duration, season, accommodation, hotel)
			cases.append(Case(case, journey_code, holiday_type, price, 
							number_of_persons, region, transportation, 
							duration, season, accommodation, hotel))
			#print(x.case, x.journey_code, x.holiday_type, x.price, x.number_of_persons, 
			#	x.region, x.transportation, x.duration, x.season, x.accommodation, x.hotel)
	print(len(cases))
	return cases
#def similarity_calculation(target_case, cases):
	#for case in cases:
			
		
if __name__ == '__main__':
	cases = read_in_cases()
	#coordinates sourced from http://www.latlong.net/
	#For TurkishAegeanSea the search term Ege Denizi was used
	#For TurkishRiviera the coordinates were found through wikipedia.org
	#For Alps the coordinates were found through wikipedia.org
	coordinate_dict = {'Egypt': [26.820553, 30.802498], 'Cairo': [30.044420, 31.235712],
						'Belgium': [50.503887, 4.469936], 'Bulgaria': [42.733883, 25.485830],
						'Bornholm': [55.160428, 14.866884], 'Fano': [43.839816, 13.019420],
						'Lolland': [54.727543, 11.464930], 'Allgaeu': [46.842863, 14.843783],
						'Alps': [33.148179, -84.603261], 'Bavaria': [48.790447, 11.497889],
						'ErzGebirge': [50.580000, 13.000000], 'Harz': [51.809525, 10.238361],
						'NorthSea': [56.511018, 3.515625], 'BalticSea': [58.487952, 19.863281],
						'BlackForest': [39.013048, -104.700808], 'Thuringia': [51.010989, 10.845346],
						'Atlantic': [41.403601, -95.013878], 'CotedAzur': [33.244490, -97.895646],
						'Corsica': [42.039604, 9.012893], 'Normandy': [38.720884, -90.297336],
						'Brittany': [48.202047, -2.932644], 'Attica': [40.294204, -87.248899],
						'Chalkidiki': [40.369500, 23.287085], 'Corfu': [39.624984, 19.922346],
						'Crete': [35.240117, 24.809269], 'Rhodes': [36.434963, 28.217483],
						'England': [52.355518, -1.174320], 'Ireland': [53.412910, -8.243890],
						'Scotland': [56.490671, -4.202646], 'Wales': [52.130661, -3.783712],
						'Holland': [52.132633, 5.291266], 'AdriaticSea': [41.855090, 17.290284],
						'LakeGarda': [45.604939, 10.635141], 'Riviera': [27.298649, -97.814888],
						'Tyrol': [47.253741, 11.601487], 'Malta': [35.937496, 14.375416],
						'Carinthia': [46.722203, 14.180588], 'SalzbergerLand': [47.372607, 13.016474],
						'Styria': [47.359344, 14.469983], 'Algarve': [37.017954, -7.930834],
						'Madeira': [32.760707, -16.959472], 'Sweden': [60.128161, 18.643501],
						'CostaBlanca': [38.504384, -0.264345], 'CostaBrava': [-12.045785, -77.135707],
						'Fuerteventura':[28.358744, -14.053676], 'GranCanaria': [27.920220, -15.547437],
						'Ibiza': [38.906734, 1.420598], 'Mallorca': [39.695263, 3.017571],
						'Teneriffe': [-27.456388, 153.048609], 'GiantMountains': [50.767222, 15.622222],
						'TurkishAegeanSea': [40.694726, 29.872522], 'TurkishRiviera': [36.675, 31.630278],
						'Tunisia': [33.886917, 9.537499], 'Balaton': [46.830268, 17.734044], 
						'Denmark': [56.263920, 9.501785], 'Poland': [51.919438, 19.145136],
						'Slowakei': [48.669026, 19.699024], 'Czechia': [49.817492, 15.472962],
						'France': [46.227638, 2.213749]}
	#for categorical data find the range and value of entries
	holiday_type_list = []
	region_list = []
	transportation_list = []
	season_list = []
	accommodation_list = []
	hotel_list = []
	
	price_list = []
	number_of_persons_list = []
	duration_list = []
	#parse cases to see the range of fields
	
	for case in cases:
		#categorical variables
		if case.holiday_type not in holiday_type_list:
			holiday_type_list.append(case.holiday_type)
		if case.region not in region_list:
			region_list.append(case.region)
		if case.transportation not in transportation_list:
			transportation_list.append(case.transportation)
		if case.season not in season_list:
			season_list.append(case.season)
		if case.accommodation not in accommodation_list:
			accommodation_list.append(case.accommodation)
		if case.hotel not in hotel_list:
			hotel_list.append(case.hotel)
		#numeric variables
		if case.price not in price_list:
			price_list.append(case.price)
		if case.number_of_persons not in number_of_persons_list:
			number_of_persons_list.append(case.number_of_persons)
		if case.duration not in duration_list:
			duration_list.append(case.duration)
		
	
	print('There are ' + str(len(holiday_type_list)) + ' types of holidays: ',
		holiday_type_list)
	print('There are ' + str(len(price_list)) + ' different prices: ', 
		sorted(price_list))
	print('There are ' + str(len(number_of_persons_list)) + ' different number of people: ',
		sorted(number_of_persons_list))
	print('There are ' + str(len(region_list)) + ' different regions: ',
		sorted(region_list))
	print('There are ' + str(len(transportation_list)) + 'different transports: ',
		transportation_list)
	print('There are ' + str(len(duration_list)) + 'different durations: ',
		sorted(duration_list))
	print('There are ' + str(len(season_list)) + 'different seasons: ',
		season_list)
	print('There are ' + str(len(accommodation_list)) + 'different accommodations: ',
		accommodation_list)
	print('There are ' + str(len(hotel_list)) + 'different hotels: ', hotel_list)

	
	
#	target_holiday_type = input('Holiday Type: ')
#	target_price = input('Price:' )
#	target_number_of_persons = input('Number of Persons: ')
#	target_region = input('Region :')
#	target_transportation = input('Transportation: ')
#	target_duration = input('Duration: ')
#	target_season = input('Season: ')
#	target_accommodation = input('Accommodation: ')
#	target_hotel = input('Hotel: ')
#	target_case = case(None, None, target_holiday_type, target_price, 
#					target_number_of_persons, target_region, target_transportation, 
#					target_duration, target_season, target_accommodation, target_hotel)
#	similarity_calculation(target_case, cases)
				
				
				
				
				