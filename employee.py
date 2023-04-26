class Employee():
	def __init__(self, first, last, pay, status=False):
		self.first_name = first                          
		self.last_name = last
		self.payment = pay
		self.authorized = status
	def set_email(self):
		return (f"{self.first_name}{self.last_name}@gmail.com").lower()

