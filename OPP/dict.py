from module import Person, User, GuestList
users = []

user_name = input('Enter name:: ')
user_color = input('Enter color:: ')
user_country = input('Enter country:: ')
user_age = input('Enter Age:: ')
user_number = input('Enter Number:: ')

users.append({
	'name':user_name,
	'color':user_color,
	'country':user_country,
	'age':user_age,
	'number':user_number
})    #User(user_name, user_color, user_country, user_age, user_number)

# print (one.view_user())
print (users)

