
import simpy

class glb:
    env = simpy.Environment()
    # Start the run process everytime an instance is created.
    # action = process(self.run())




def custtime(alphac,betac):
	cust_time = random.gammavariate(alphac,betac) #returns gamma distribution--for customer time


def inventime(alphai,betai):
	invent_time = random.gammavariate(alphai,betai) # returns gamma distribution--for inventory time


def storesim(maxsimtime, alphac, betac, alphai, betai):
	#maxsimtime gets passed in and determines how long whole simulation runs for
	while True:


		print('Start counting %d' % glb.env.now)



		yield glb.env.timeout(maxsimtime)

	
# TODO possible interrupts?#
