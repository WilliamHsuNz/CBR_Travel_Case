"""
Python Case Class
Author: William Hsu
19/August/2016		
"""
class Case:
	def __init__(self, case, journey_code, holiday_type, price, number_of_persons,
		region, transportation, duration, season, accommodation, hotel):
		self.case = case
		self.journey_code = journey_code
		self.holiday_type = holiday_type
		self.price = price
		self.number_of_persons = number_of_persons
		self.region = region
		self.transportation = transportation
		self.duration = duration
		self.season = season
		self.accommodation = accommodation
		self.hotel = hotel
