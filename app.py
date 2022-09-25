from BBC import *
from data_client import *

# Esse aqui pode ser a Valentina
pfm_da_valentina = PFM(customerId=customer_data['customerId'], customer_data=customer_data, initialInvestment=0)
ip_da_valentina = InitPayment(pfm_da_valentina)
credit_engine_da_valentina = CreditEngine(pfm_da_valentina)

'''
Valentina:
'''
# # Remanejamento entre contas
ip_da_valentina.toRealocateAccounts()
print(pfm_da_valentina.showAllMySituation())
print(ip_da_valentina.log)

# # Aplicar saldo positivo em investimentos de alta liquidez e baixo risco
# ip_da_valentina.toApplication()
# print(pfm_da_valentina.showAllMySituation())
# print(ip_da_valentina.log)







'''
Alexo:
'''

# Esse aqui pode ser o Alexo
# pfm_do_alexo = PFM(customerId=other_customer_data['customerId'], customer_data=other_customer_data, initialInvestment=1000)
# ip_do_alexo = InitPayment(pfm_do_alexo)






# print('Alexo: ', pfm_do_alexo.showAllMySituation())
# ip_do_alexo.toWithdrawInvestmentToPayBank()
# print('Alexo: ', pfm_do_alexo.showAllMySituation())

# print('Valentina: ', pfm_da_valentina.showAllMySituation())
# ip_da_valentina.toCredit(creditEngine=credit_engine_da_valentina, n=48)
# print('Valentina: ', pfm_da_valentina.showAllMySituation())
# print(ip_da_valentina.log)


    
