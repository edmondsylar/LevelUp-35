class Person:

	def __init__(self, name, color):
		self.name = name
		self.color = color

		self.person = []

	def view(self):
		return '{} {}'.format(self.name, self.color)


class User(Person):
	def __init__(self, name, color, country, age, number):
		super().__init__(name, color)
		self.country = country
		self.age = age
		self.number =number

	def view_user(self):
		return '{} {} {} {} {}'.format(self.name, self.color, self.country, self.age, self.number)

# GuestList data structure for storing the guests 
class GuestList:
	def __init__(self):
		self.guest = dict()
		self.guests = []
		
# Adding a guest to the Guest list
	def add_guest(self, name, color, country, age, number):
			self.guest['name'] = name
			self.guest['color'] = color
			self.guest['country'] = country
			self.guest['age'] = age
			self.guest['number'] = number
			
			self.guests.append(self.guest)

	def view(self):
		return self.guests
			
# Checking for users in the Guest List.
	def get_user(self):
		return self.guests

# Deleting a selectded user by key='name'
	def delete_user(self, name):
		for guest in self.guests:
			if guest['name'] == name:
				self.guests.remove(guest)
				return 'Guest Removed Successfully'

			elif name not in guest['name']:
				return 'Sory user does not exist in GuestList'

			else:
				'Wrong Selection made'
		