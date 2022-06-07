import pandas as pd

# initialize list of lists
data = [['31_december_2021', 9825, 32334, 26707, 245, 1.2, 0.35, 5.73, 1.68, 0.42], 
        ['01_may_2022', 11015, 33324, 27555, 316, 1.2, 0.35, 5.73, 1.68, 0.42]]
  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['month', 'gas', 'electric_1', 'electric_2', 'water', 'gas_pr', 
                                   'elect_pr', 'water_pr', 'gas_pr_new', 'elect_pr_new'])
  
# print dataframe.
df



def total_cost (gas, electric_1, electric_2, water):
    
    total_cost_old = ((df[df['month'] == '01_may_2022'].gas[1] - df[df['month'] == '31_december_2021'].gas[0]) * df.gas_pr) + (((df[df['month'] == '01_may_2022'].electric_1[1] +  df[df['month'] == '01_may_2022'].electric_2[1]) -
    
    (df[df['month'] == '31_december_2021'].electric_1[0] +  df[df['month'] == '31_december_2021'].electric_2[0])) * df.elect_pr) + ((df[df['month'] == '01_may_2022'].water[1] - df[df['month'] == '31_december_2021'].water[0]) * df.water_pr)
    

    total_cost_new = ((gas - df[df['month'] == '01_may_2022'].gas[1]) *  df.gas_pr_new) + (((electric_1 + electric_2) - (df[df['month'] == '01_may_2022'].electric_1[1] +  df[df['month'] == '01_may_2022'].electric_2[1])) * df.elect_pr_new) + ((water - df[df['month'] == '01_may_2022'].water[1]) * df.water_pr)
    
    
    all_total_cost = total_cost_old[0] + total_cost_new[0]
    
    
    return round(all_total_cost, 2)

print('Enter the numbers of the meters')
gas = int(input('Gas meter: '))
electric_1 = int(input('Electric meter 1: '))
electric_2 = int(input('Electric meter 2: '))
water = int(input('Water: '))
number_months = int(input('Number of months: '))

internet = 54.56
cleaning_lady = 72.00
insurance = 52.40
material_usage = 30.00
maintaince_boiler = 5.52

other_costs = (internet + cleaning_lady + insurance + material_usage + maintaince_boiler) * number_months

print(f'Total cost until now is {total_cost (gas, electric_1, electric_2, water) + other_costs} euro')
print(f'Total cost per month is {round(((total_cost (gas, electric_1, electric_2, water) + other_costs) /number_months), 2)} euro')
print(f'Total cost per person is {round(((total_cost (gas, electric_1, electric_2, water) + other_costs)/5), 2)} euro')
print(f'Total cost per person per month is {round((((total_cost (gas, electric_1, electric_2, water) + other_costs)/5)/number_months), 2)} euro')

print(f'Total amount to be paid per person per month is {round(round((((total_cost (gas, electric_1, electric_2, water) + other_costs)/5)/number_months), 2) - 110)} euro')
print(f'Total amount to be paid per person in total is {round(round((((total_cost (gas, electric_1, electric_2, water) + other_costs)/5)/number_months), 2) - 110) * number_months} euro')


