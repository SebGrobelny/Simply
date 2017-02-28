from random import gammavariate, seed
from SimPy.Simulation import *

class glb:
	order_list = [] #list of times that orders took
	delivery_list = [] #amount of time delivery takes

	stock = None
	order_amount = 1
	delivery_amount = 1


class Customer(Process):
	def custtime(self, alphac,betac):
		while True:

			order_time = random.gammavariate(alphac,betac) #returns gamma distribution--for time customer orders arrive

	  		if glb.stock.amount > 0 : # if stock amount > 0, fulfill order instantly
				yield get, self, glb.stock, glb.order_amount
				glb.order_list.append(0) # 0 represents an instant order

				print 'at %7.4f, get %7.4f units, now amount = %6.4f'\
					%(now(),glb.order_amount,glb.stock.amount)

			else: # otherwise, fulfill order in the calculated time
				yield hold, self, order_time

				glb.order_list.append(order_time)

				print 'at %7.4f, get %7.4f units, now amount = %6.4f'\
					%(now(),glb.order_amount,glb.stock.amount)



class Inventory(Process):
	def inventime(self, alphai,betai):
		while True:
			delivery_time = random.gammavariate(alphai,betai) # returns gamma distribution--for time to deliver new inventory
			glb.delivery_list.append(delivery_time)
			
			yield put, self, glb.stock, glb.delivery_amount
			print 'at %7.4f, add %7.4f units, now amount = %6.4f'\
	               %(now(),glb.delivery_amount,glb.stock.amount)
			yield hold, self, delivery_time


def storesim(maxsimtime, alphac, betac, alphai, betai):

	glb.stock = Level(monitored=True)

	seed(12345)

	initialize()

	# activate both the store and the customer simulations
	store = Inventory()
	activate (store, store.inventime(alphai,betai))
	
	customer = Customer()
	activate (customer, customer.custtime(alphac, betac))

	simulate (until = maxsimtime)

	# add up the total order times of all orders
	order_sum = 0
	instant_orders = 0
	for i in glb.order_list:
		if i == 0: # count the total amount of instant orders
			instant_orders = instant_orders + 1
		order_sum = order_sum + i

	mean_ordertime = order_sum / len(glb.order_list)
	inst_prop = float(instant_orders) / float(len(glb.order_list))

	return (mean_ordertime, inst_prop, 0) # TODO: need to compute last variable in tuple
