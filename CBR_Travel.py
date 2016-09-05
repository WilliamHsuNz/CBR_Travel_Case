import xlrd
from Case import Case
from tkinter import *
from tkinter import ttk
"""
CBR Travel Case
Author: William Hsu
19/August/2016
"""


class Application(Frame):
	"""A Gui application with three buttons"""
	def __init__(self, master):
		"""Initialize the Frame"""
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
	def create_widgets(self):
		
		self.Title = Label(self, text = "CBR for Travel Case Base", font =('Helvetica', 24))
		self.Title.grid(row = 0, column = 0, sticky = W)
		
		self.Instruction_Label = Label(self, text= "some instruction on how to use the application")
		self.Instruction_Label.grid(row = 1, column = 0, sticky = E)
		self.Weights_Label = Label(self, text = "weighting").grid(row = 2, column = 2, sticky = W)
		
		self.Holiday_Type = Label(self, text ="Holiday Type").grid(row = 3, column = 0, sticky = E)
		Holiday_Types = ('Arbitrary', 'Active', 'Adventure', 'Bathing', 'City', 'Diving', 'Education', 
						'Language', 'Recreation', 'Skiing', 'Shopping', 'Surfing', 'Wandering') 
		self.Holiday_Type_cb = ttk.Combobox(self, values = Holiday_Types, state= "normal")
		self.Holiday_Type_cb.grid(row = 3, column = 1, sticky = W)
		Weights = ("0","1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
		self.Holiday_Type_Weight_cb = ttk.Combobox(self, values = Weights, width = 3, state= "readonly")
		self.Holiday_Type_Weight_cb.grid(row=3, column = 2, sticky = W)
		
		self.Price = Label(self, text="Price").grid(row = 4, column = 0, sticky = E)
		self.Price_Entry = Entry(self, bd= 2)
		self.Price_Entry.grid(row=4, column = 1, sticky = W)
		self.Price_Weight_cb = ttk.Combobox(self, values = Weights, width = 3, state= "readonly")
		self.Price_Weight_cb.grid(row=4, column = 2, sticky = W)
		
		self.Number_Of_Persons = Label(self, text ="Number of Persons").grid(row = 5, column = 0, sticky = E)
		self.Number_Of_Persons_Entry = Entry(self, bd= 2)
		self.Number_Of_Persons_Entry.grid(row=5, column = 1, sticky = W)
		self.Number_Of_Persons_Weight_cb = ttk.Combobox(self, values = Weights, width = 3, state= "readonly")
		self.Number_Of_Persons_Weight_cb.grid(row=5, column = 2, sticky = W)
		
		self.Region = Label(self, text="Region").grid(row = 6, column= 0, sticky = E)
		Region = 	("Arbitrary", "AdriaticSea", "Algarve", "Allgaeu", "Alps", "Atlantic",
		 			"Attica", "Austria", "Balaton", "BalticSea", "Bavaria", "Belgium", 
					"BlackForest", "Bornholm", "Brittany", "Bulgaria", "Cairo", "Carinthia",
					"Chalkidiki", "City", "Coast", "Corfu", "Corsica", "CostaBlanca", "CostaBrava",
					"CotedAzur", "Country", "Crete", "Cyprus", "Czechia", "Denmark", "Dolomites",
					"Egypt", "England", "ErzGebirge", "Fano", "France", "Fuerteventura", 
					"Germany", "GiantMountains", "GranCanaria", "Greece", "Harz", "HighTatra", 
					"Holland", "Hungaria", "Ibiza", "Ireland", "Island", "Italy", "Lake", 
					"LakeGarda", "Lanzarote", "Lolland", "London", "LowerAustria", "Madeira",
					"Mallorca", "Malta", "MediterraneanSea", "Morocco", "Mountains", "Normandy", 
					"NorthSea", "Paris", "Poland", "Portugal", "Rhodes", "Riviera", "SalzbergerLand",
					"Salzkammergut", "Scotland", "Sea", "Slowakei", "Spain", "Sweden", "Switzerland",
					"Styria", "Teneriffe", "Thuringia", "Tunisia", "Turkey", "TurkishAegeanSea", 
					"TurkishRiviera", "Tyrol", "UnitedKingdom", "Wales", "Waters")
		self.Region_cb = ttk.Combobox(self, values = Region, state= "normal")
		self.Region_cb.grid(row = 6, column = 1, sticky = W)
		self.Region_Weight_cb = ttk.Combobox(self, values = Weights, width = 3, state= "readonly")
		self.Region_Weight_cb.grid(row=6, column = 2, sticky = W)
		
		self.Transportation = Label(self, text="Transportation").grid(row = 7, column= 0, sticky = E)
		Transportation= ("Arbitrary", "Car",  "Coach", "Plane", "Train")
		self.Transportation_cb = ttk.Combobox(self, values = Transportation, state= "normal")
		self.Transportation_cb.grid(row = 7, column = 1, sticky = W)
		self.Transportation_Weight_cb = ttk.Combobox(self, values = Weights, width = 3, state= "readonly")
		self.Transportation_Weight_cb.grid(row=7, column = 2, sticky = W)
		
		self.Duration = Label(self, text ="Duration").grid(row = 8, column = 0, sticky = E)
		self.Duration_Entry = Entry(self, bd= 2)
		self.Duration_Entry.grid(row= 8, column = 1, sticky = W)
		self.Duration_Weight_cb = ttk.Combobox(self, values = Weights, width = 3, state= "readonly")
		self.Duration_Weight_cb.grid(row=8, column = 2, sticky = W)
		
		self.Season = Label(self, text="Season").grid(row = 9, column = 0, sticky = E)
		Season =	("Arbitrary", "Spring", "Summer", "Autumn", "Winter", "January", "February", "March", 
					"April", "May", "June", "July", "August", "September", "October", "November", "December")
		self.Season_cb = ttk.Combobox(self, values = Transportation, state = "normal")
		self.Season_cb.grid(row = 9, column = 1, sticky = W)
		self.Season_Weight_cb = ttk.Combobox(self, values = Weights, width = 3, state= "readonly")
		self.Season_Weight_cb.grid(row=9, column = 2, sticky = W)
		
		self.Accommodation_Type = Label(self, text="Accommodation Type").grid(row = 10, column = 0, sticky = E)
		Accommodation_Type =	("Arbitrary", "HolidayFlat", "OneStar", "TwoStars", "ThreeStars", 
								"FourStars", "FiveStars")
		self.Accommodation_Type_cb = ttk.Combobox(self, values = Accommodation_Type, state = "normal")
		self.Accommodation_Type_cb.grid(row = 10, column = 1, sticky = W)
		self.Accommodation_Type_Weight_cb = ttk.Combobox(self, values = Weights, width = 3, state= "readonly")
		self.Accommodation_Type_Weight_cb.grid(row = 10, column = 2, sticky = W)
		
		self.Hotel = Label(self, text ="Hotel").grid(row = 11, column = 0, sticky = E)
		self.Hotel_Entry = Entry(self, bd= 2)
		self.Hotel_Entry.grid(row = 11 , column = 1, sticky = W)
		self.Hotel_Weight_cb = ttk.Combobox(self, values = Weights, width = 3, state= "readonly")
		self.Hotel_Weight_cb.grid(row = 11, column = 2, sticky = W)
		
		self.k = Label(self, text ="k").grid(row = 12, column = 0, sticky = E)
		self.k_Entry = Entry(self, bd = 2).grid(row = 12, column = 1, sticky = W)
		
		self.submit_button = Button(self, text = "Submit", command = self.reveal).grid(row = 13, column = 2, sticky = E)
		self.text = Text(self, width = 35, height = 11, wrap = WORD)
		self.text.grid(row = 14, column = 1, columnspan = 2, sticky = W)
	def reveal(self):
		cases_output = 	"Holiday Type: " + self.Holiday_Type_cb.get() + "\n" +\
						"Price: " + self.Price_Entry.get()  
		x = 'a string'
		print("this is x ") 
		print(type(x))
		print("this is combobox variable")
		print(type(str(self.Holiday_Type_cb.get())))				
		self.text.delete(0.0, END)
		self.text.insert(0.0, cases[0].holiday_type)
		
#read in cases from case base
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
	#create UI window
	root = Tk()
	root.title("CBR Travel Case")
	root.geometry("600x600")
	app = Application(root)
	app.grid()
	root.mainloop()

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

				
				
				
				
				