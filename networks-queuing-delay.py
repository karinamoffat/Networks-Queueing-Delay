import numpy as np
import matplotlib.pyplot as plt

#define all variables
service = 0.75
arrivals = [0.2, 0.4, 0.6, 0.65, 0.7, 0.72, 0.74, 0.745]
averageQueueLength = None
timeSlots = int(1e6)
averageQueueDelay = None

#function to simulate single server queue
def simulateSingleServer(arrivalRate):
    #queue starts empty
    queueLength = 0
    arrival = 0
    departure = 0

    #at each time slot
    for j in range (timeSlots):

        #generate a random value
        num = np.random.random()

        #if value is less than arrival rate it is an arrival and adds to queue
        if num < arrivalRate:
            arrival += 1
        #if value is less than service time, it is a departure and leaves queue
        if num < service:
            departure += 1
        
        #add new additions to the queue to the current queue length
        queueLength = (arrival - departure) + queueLength
    
    #little law: L = lambda/W, W is expected queue delay
    #how can we find expected queue delay
    averageQueueLength = arrivalRate / service
    averageQueueDelay = averageQueueLength / 1000000

    return averageQueueLength, averageQueueDelay

results = [simulateSingleServer(arrivalRate) for arrivalRate in arrivals]

averageQueueLength = [result[0] for result in results]
averageQueueDelay = [result[1] for result in results]

plt.figure(figsize=(10, 5))
plt.plot(arrivals, averageQueueDelay, marker='o', label='Simulation')
plt.title('Average Queueing Delay vs Arrival Rate')
plt.xlabel('Arrival Rate (λ)')
plt.ylabel('Average Queueing Delay')
plt.grid(True)
plt.legend()
plt.show()
