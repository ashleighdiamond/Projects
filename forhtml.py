import pandas as pd

print("Average transactions and sums per day")
filee=pd.read_csv('datafrompostgress.csv')
filee.to_html('project.html')
