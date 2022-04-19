"""
calculating ENBIS for tultech.
Loss provided the breach happens => 20M


"""
#calculations are done assuming unit dollars here.
print("\n\n")
IC = 20*10**6
Recurring_cost = 10**6
 
r = 0.88
print("Since SOC clients have no record for the breach. We can assume \n the breakeven risk of reduction to be a high value.\n\n")
print(f"assume r = {r} \n")
#assuming time horizon of 20years
T = 20

annual_breakeven_probability = Recurring_cost / (r* IC)
print(f"The annual break even probability assuming the break even risk reduction to be 0.88 is {annual_breakeven_probability}\n\n")

print("\n This leads to the ENBIS amortized over 20 years to be")
sum = 0
for i in range(0,21):
    sum += 20*1
ENBIS = annual_breakeven_probability*r*sum - Recurring_cost
print(f"\n\t{ENBIS}")
if(ENBIS > 0):
    print("I suggest we should move forward with the SOC Investment")    
else:
    print(" Thus I suggest we should move not forward with the SOC Investment and look for other solutions.")   

