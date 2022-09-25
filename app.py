from BBC import *
from data_client import *

my_pfm = PFM(customerId=customer_data['customerId'])
my_IP = InitPayment(my_pfm)


print(my_pfm.showAllMySituation())

my_IP.toRealocateAccounts()
print(my_pfm.showAllMySituation())
print(my_IP.log)


my_IP.toApplication()
print(my_pfm.showAllMySituation())
print(my_IP.log)


    
