"""
CBR for the Travel domain
Case Class
Author: William Hsu
Date:  11/September/2016

For the program CBR_Travel.py		
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
