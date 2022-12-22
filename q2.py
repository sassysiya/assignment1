gross=float(input("gross income: "))
dependents=int(input("number of dependents: "))
taxable_income=gross-10000-(dependents*3000)
tax=taxable_income*0.02
print("your tax is: ",tax)
