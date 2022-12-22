# simulates bank account

class BankAccount:
	# Constructor - allows us to specify the owner, initial balance, account type, and interest rate
	def __init__(self, owner, balance, is_savings, rate):
		self.owner = owner 				# Name of account owner
		self.balance = balance 			# Current account balance		
		self.is_savings = is_savings	# False for checking, True for savings
		self.interest_rate = rate 		# As a percentage (e.g., 1 for 1%)

		acct_type = 'savings' if self.is_savings else 'checking'
		print(f'Created a new {acct_type} account for {self.owner} with balance ${self.balance:.2f}, interest rate {self.interest_rate}%.')

	# Deposits the specified amount into the account
	def deposit(self, amount):
		if amount <= 0:
			print('Deposit amount must be positive.  No changes to account made.')
		else:
			self.balance += amount
			print(f"Deposited ${amount:.2f} into {self.owner}'s account, new balance is ${self.balance:.2f}.")

	# Withdraws the specified amount from the account
	def withdraw(self, amount):
		if amount <= 0:
			print('Withdraw amount must be positive.  No changes to account made.')
		elif amount > self.balance:
			print('Withdraw amount exceeds available balance.  No changes to account made.')
		else:
			self.balance -= amount
			print(f"Withdrew ${amount:.2f} from {self.owner}'s account, new balance is ${self.balance:.2f}.")

	# Modifies the interest rate of the account by the specified amount, as a percentage
	def adjust_interest_rate(self, amount):
		self.interest_rate += amount
		print(f"Changed interest rate on {self.owner}'s account by {amount}%, new interest rate is {self.interest_rate}%.")

	# Makes one annual interest payment to the account, based on the current balance and interest_rate
	def pay_interest(self):
		interest = self.interest_rate / 100 * self.balance;
		self.balance += interest
		print(f"Made interest payment of ${interest:.2f} to {self.owner}'s account, new balance is ${self.balance:.2f}.")