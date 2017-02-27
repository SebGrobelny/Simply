from random import gammavariate, seed
import simpy

# class glb:
#     env = simpy.Environment()
#     # Start the run process everytime an instance is created.
#     # action = process(self.run())



class Customer():
	def custtime(alphac,betac):
		while True:
			order_list = [] #list of times that orders took
			order_time = random.gammavariate(alphac,betac) #returns gamma distribution--for time customer orders arrive
			order_list.append(order_time)
			order_amount = 1.0 # amount requested
			yield get, stock, order_amount
			print 'at %7.4f, add %7.4f units, now amount = %6.4f'\
	               %(now(),order_amount,stock.amount)
	        yield hold, order_time



class Inventory():
	def inventime(alphai,betai):
		while True:
			delivery_list = [] #amount of time delivery takes
			delivery_time = random.gammavariate(alphai,betai) # returns gamma distribution--for time to deliver new inventory
			delivery_list.append(delivery_time)
			delivery_amount = 1.0 # amount of items delivered
			yield put, stock, deliver_amount
			print 'at %7.4f, add %7.4f units, now amount = %6.4f'\
	               %(now(),delivery_amount,stock.amount)
			yield hold, delivery_time


def storesim(maxsimtime, alphac, betac, alphai, betai):
	#maxsimtime gets passed in and determines how long whole simulation runs for
	stock = Level(monitored=true)

	seed(99999)

	initialize()

	store = Inventory()
	activate (store, store.inventime(alphai,betai))
	customer = Customer()
	activate (customer, customer.custtime(alphac, betac))

	simulate (until = maxsimtime)


	
# TODO possible interrupts?#
