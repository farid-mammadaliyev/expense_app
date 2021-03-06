

from PIL import Image,ImageTk


import tkinter as tk
window=tk.Tk()
window.title(" Calculate the total cost of living")
window.geometry("750x750")



newlabel = tk.Label(text = "Enter the current numbers on the meters")
newlabel.grid(column=3,row=1)

gas = tk.Label(text = "Gas meter")
gas.grid(column=2,row=2)


elect_1 = tk.Label(text = "    Electricity meter 1")
elect_1.grid(column=2,row=3)
elect_2 = tk.Label(text =  "    Electricity meter 2")
elect_2.grid(column=2,row=4)
water = tk.Label(text = "Water meter")
water.grid(column=2,row=5)

number_months = tk.Label(text = "    Number of months")
number_months.grid(column=2,row=6)


gasEntry = tk.Entry()
gasEntry.grid(column=3,row=2)
elect_1Entry = tk.Entry()
elect_1Entry.grid(column=3,row=3)
elect_2Entry = tk.Entry()
elect_2Entry.grid(column=3,row=4)
waterEntry = tk.Entry()
waterEntry.grid(column=3,row=5)

number_monthsEntry = tk.Entry()
number_monthsEntry.grid(column=3,row=6)

import pandas as pd

# initialize list of lists
data = [['31_december_2021', 9825, 32334, 26707, 245, 1.2, 0.35, 5.73, 1.68, 0.42], 
        ['01_may_2022', 11015, 33324, 27555, 316, 1.2, 0.35, 5.73, 1.68, 0.42]]
  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['month', 'gas', 'electric_1', 'electric_2', 'water', 'gas_pr', 
                                   'elect_pr', 'water_pr', 'gas_pr_new', 'elect_pr_new'])
  
# print dataframe.
df



def getInput():


    monkey = Person(gas = int(gasEntry.get()), elect_1 = int(elect_1Entry.get()), elect_2 = int(elect_2Entry.get()),\
     water = int(waterEntry.get()), number_months = float(number_monthsEntry.get()))
    
    
    textArea = tk.Text(master=window,height=10,width=65)
    textArea.grid(column=3,row=8)

    answer = "The total cost is {cost_total} euro\nThe cost per month is {per_month} euro\nThe total cost per person is {per_person} euro\nThe cost per person per month is {per_person_month} euro\nThe total amount to be paid per person per month is {to_be_paid} euro\nThe total amount to be paid per person in total is {to_be_paid_total} euro".\
    format(cost_total=monkey.cost_total(), per_month=monkey.per_month(), \
    per_person=monkey.per_person(), per_person_month = monkey.per_person_month(), to_be_paid = monkey.to_be_paid(), to_be_paid_total = monkey.to_be_paid_total() )

    textArea.insert(tk.END,answer)
    
   

button=tk.Button(window,text="Calculate the cost",command=getInput,bg="pink")
button.grid(column=3,row=7)

internet = 54.56
cleaning_lady = 72.00
insurance = 52.40
material_usage = 30.00
maintaince_boiler = 5.52





class Person:
    def __init__(self, gas, elect_1, elect_2, water, number_months ):
        self.gas = gas
        self.elect_1 = elect_1
        self.elect_2 = elect_2
        self.water = water
        self.number_months  = number_months 

    def cost_total(self):

        other_costs = (internet + cleaning_lady + insurance + material_usage + maintaince_boiler) * self.number_months 

        total_cost_old = (((df[df['month'] == '01_may_2022'].gas[1] - df[df['month'] == '31_december_2021'].gas[0]) * df.gas_pr) + (((df[df['month'] == '01_may_2022'].electric_1[1] +  
        df[df['month'] == '01_may_2022'].electric_2[1]) - (df[df['month'] == '31_december_2021'].electric_1[0] +  df[df['month'] == '31_december_2021'].electric_2[0])) * df.elect_pr) + 
        ((df[df['month'] == '01_may_2022'].water[1] - df[df['month'] == '31_december_2021'].water[0]) * df.water_pr))
     
        total_cost_new = (((self.gas - df[df['month'] == '01_may_2022'].gas[1]) *  df.gas_pr_new) + (((self.elect_1 + self.elect_2) - (df[df['month'] == '01_may_2022'].electric_1[1] +   
        df[df['month'] == '01_may_2022'].electric_2[1])) * df.elect_pr_new) + ((self.water - df[df['month'] == '01_may_2022'].water[1]) * df.water_pr))
    
        cost = total_cost_old[0] + total_cost_new[0]

        cost_total = round((other_costs + cost), 2)

        return cost_total



    def per_month(self):

        other_costs = (internet + cleaning_lady + insurance + material_usage + maintaince_boiler) * self.number_months 

        total_cost_old = (((df[df['month'] == '01_may_2022'].gas[1] - df[df['month'] == '31_december_2021'].gas[0]) * df.gas_pr) + (((df[df['month'] == '01_may_2022'].electric_1[1] +  
        df[df['month'] == '01_may_2022'].electric_2[1]) - (df[df['month'] == '31_december_2021'].electric_1[0] +  df[df['month'] == '31_december_2021'].electric_2[0])) * df.elect_pr) + 
        ((df[df['month'] == '01_may_2022'].water[1] - df[df['month'] == '31_december_2021'].water[0]) * df.water_pr))
     
        total_cost_new = (((self.gas - df[df['month'] == '01_may_2022'].gas[1]) *  df.gas_pr_new) + (((self.elect_1 + self.elect_2) - (df[df['month'] == '01_may_2022'].electric_1[1] +   
        df[df['month'] == '01_may_2022'].electric_2[1])) * df.elect_pr_new) + ((self.water - df[df['month'] == '01_may_2022'].water[1]) * df.water_pr))
    
        cost = total_cost_old[0] + total_cost_new[0]

        cost_total = other_costs + cost

        per_month = round((cost_total/self.number_months), 2)
        
        return per_month



    def per_person(self):

        other_costs = (internet + cleaning_lady + insurance + material_usage + maintaince_boiler) * self.number_months 

        total_cost_old = (((df[df['month'] == '01_may_2022'].gas[1] - df[df['month'] == '31_december_2021'].gas[0]) * df.gas_pr) + (((df[df['month'] == '01_may_2022'].electric_1[1] +  
        df[df['month'] == '01_may_2022'].electric_2[1]) - (df[df['month'] == '31_december_2021'].electric_1[0] +  df[df['month'] == '31_december_2021'].electric_2[0])) * df.elect_pr) + 
        ((df[df['month'] == '01_may_2022'].water[1] - df[df['month'] == '31_december_2021'].water[0]) * df.water_pr))
     
        total_cost_new = (((self.gas - df[df['month'] == '01_may_2022'].gas[1]) *  df.gas_pr_new) + (((self.elect_1 + self.elect_2) - (df[df['month'] == '01_may_2022'].electric_1[1] +   
        df[df['month'] == '01_may_2022'].electric_2[1])) * df.elect_pr_new) + ((self.water - df[df['month'] == '01_may_2022'].water[1]) * df.water_pr))
    
        cost = total_cost_old[0] + total_cost_new[0]

        cost_total = other_costs + cost

        per_person= round((cost_total/5), 2)
        
        return per_person


    def per_person_month(self):

        other_costs = (internet + cleaning_lady + insurance + material_usage + maintaince_boiler) * self.number_months 

        total_cost_old = (((df[df['month'] == '01_may_2022'].gas[1] - df[df['month'] == '31_december_2021'].gas[0]) * df.gas_pr) + (((df[df['month'] == '01_may_2022'].electric_1[1] +  
        df[df['month'] == '01_may_2022'].electric_2[1]) - (df[df['month'] == '31_december_2021'].electric_1[0] +  df[df['month'] == '31_december_2021'].electric_2[0])) * df.elect_pr) + 
        ((df[df['month'] == '01_may_2022'].water[1] - df[df['month'] == '31_december_2021'].water[0]) * df.water_pr))
     
        total_cost_new = (((self.gas - df[df['month'] == '01_may_2022'].gas[1]) *  df.gas_pr_new) + (((self.elect_1 + self.elect_2) - (df[df['month'] == '01_may_2022'].electric_1[1] +   
        df[df['month'] == '01_may_2022'].electric_2[1])) * df.elect_pr_new) + ((self.water - df[df['month'] == '01_may_2022'].water[1]) * df.water_pr))
    
        cost = total_cost_old[0] + total_cost_new[0]

        cost_total = other_costs + cost

        per_person_month= round((cost_total/5/self.number_months), 2)
        
        return per_person_month


    def to_be_paid(self):

        other_costs = (internet + cleaning_lady + insurance + material_usage + maintaince_boiler) * self.number_months 

        total_cost_old = (((df[df['month'] == '01_may_2022'].gas[1] - df[df['month'] == '31_december_2021'].gas[0]) * df.gas_pr) + (((df[df['month'] == '01_may_2022'].electric_1[1] +  
        df[df['month'] == '01_may_2022'].electric_2[1]) - (df[df['month'] == '31_december_2021'].electric_1[0] +  df[df['month'] == '31_december_2021'].electric_2[0])) * df.elect_pr) + 
        ((df[df['month'] == '01_may_2022'].water[1] - df[df['month'] == '31_december_2021'].water[0]) * df.water_pr))
     
        total_cost_new = (((self.gas - df[df['month'] == '01_may_2022'].gas[1]) *  df.gas_pr_new) + (((self.elect_1 + self.elect_2) - (df[df['month'] == '01_may_2022'].electric_1[1] +   
        df[df['month'] == '01_may_2022'].electric_2[1])) * df.elect_pr_new) + ((self.water - df[df['month'] == '01_may_2022'].water[1]) * df.water_pr))
    
        cost = total_cost_old[0] + total_cost_new[0]

        cost_total = other_costs + cost

        to_be_paid = round((cost_total/5/self.number_months) - 110, 2)
        
        return to_be_paid

    def to_be_paid_total(self):

        other_costs = (internet + cleaning_lady + insurance + material_usage + maintaince_boiler) * self.number_months 

        total_cost_old = (((df[df['month'] == '01_may_2022'].gas[1] - df[df['month'] == '31_december_2021'].gas[0]) * df.gas_pr) + (((df[df['month'] == '01_may_2022'].electric_1[1] +  
        df[df['month'] == '01_may_2022'].electric_2[1]) - (df[df['month'] == '31_december_2021'].electric_1[0] +  df[df['month'] == '31_december_2021'].electric_2[0])) * df.elect_pr) + 
        ((df[df['month'] == '01_may_2022'].water[1] - df[df['month'] == '31_december_2021'].water[0]) * df.water_pr))
     
        total_cost_new = (((self.gas - df[df['month'] == '01_may_2022'].gas[1]) *  df.gas_pr_new) + (((self.elect_1 + self.elect_2) - (df[df['month'] == '01_may_2022'].electric_1[1] +   
        df[df['month'] == '01_may_2022'].electric_2[1])) * df.elect_pr_new) + ((self.water - df[df['month'] == '01_may_2022'].water[1]) * df.water_pr))
    
        cost = total_cost_old[0] + total_cost_new[0]

        cost_total = other_costs + cost

        to_be_paid_total = round(((cost_total/5/self.number_months) - 110) * self.number_months, 2)
        
        return to_be_paid_total 




image=Image.open('app_photo.jpg')
image.thumbnail((600,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=3,row=0)


window.mainloop()




