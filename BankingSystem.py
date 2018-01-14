from datetime import datetime



class Banking:


	def __init__(self, pin, balance, transaction_time):
		self.pin = pin
		self.balance = balance
		self.transaction_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	def deposit(self):
		print(self.pin ,":",self.balance,":", self.transaction_time)

	def withdraw(self,amount):
		amount=int("Enter the amount to withdraw\n")
		balance=-amount


	def checkBalance(self,balance):
		print("Your balance is: ", balance)


trans=Banking(1332, 3400, transaction_time)

print(Banking.deposit(trans))