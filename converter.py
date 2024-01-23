import pandas as pd 
import os

directory = './excel'
output_dir = './csv/'

for filename in os.listdir(directory):
    name = os.path.splitext(filename)[0]
    f = os.path.splitext(filename)[1]
    if f=='.xlsx':
        file = os.path.join(directory, filename)
        df = pd.DataFrame(pd.read_excel(file))
    df.to_csv(output_dir + name + '.csv', index = None, header=True)