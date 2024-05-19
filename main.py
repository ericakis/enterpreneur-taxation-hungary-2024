import calendar
import csv
def month_name(num):
    return calendar.month_name[num]

# it is a list
net_income = [102345,987654,45632,0,0,1000000,650000,650000,650000,650000,650000,650000]
cost_percentage = 0.4
taxable_income = []
personal_income_tax_payable = []
accumulated_taxable_income = 0
personal_income_tax_free_taxable_income_treshold = 1600800

for i in net_income:
    taxable_income.append(i*(1-cost_percentage))

month = 1

over_treshold=False

for i in taxable_income:
    if over_treshold:
        personal_income_tax_payable.append([month_name(month),i*0.15])
    else:
        accumulated_taxable_income=accumulated_taxable_income+i
        if accumulated_taxable_income > personal_income_tax_free_taxable_income_treshold:
            diff = accumulated_taxable_income-personal_income_tax_free_taxable_income_treshold
            personal_income_tax_payable.append([month_name(month),diff*0.15])
            over_treshold=True
        else:
            personal_income_tax_payable.append([month_name(month),0])
    month=month+1

annual_PIT_total=0
for i in personal_income_tax_payable:
    annual_PIT_total=annual_PIT_total+i[1]

print(personal_income_tax_payable)
column_names = ['Month','PIT payable']

with open('2024_PIT_payable.csv', 'w', newline='') as f:
    csv_writer= csv.writer(f)
    csv_writer.writerow(column_names)
    csv_writer.writerows(personal_income_tax_payable)
    csv_writer.writerow(['Total',annual_PIT_total])