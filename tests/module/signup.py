class user_reg:

    def __init__(self):
        self.user_details = []
        self.user = dict()

    def add_user(self, first_name, last_name, email, password):
        self.username = first_name + last_name
        self.email = email
        self.password = password
        # self.first_name = first_name
        # self.last_name = last_name

        self.user['username'] = self.username
        self.user['email'] = email
        self.user['Security key'] = password
        
        self.user_details.append(self.user)


trial = user_reg()
trial.add_user('edmond', 'sylar', 'edmondmusiitwa@gmail.com', 'sec98229829sec')

print (trial.user_details)
