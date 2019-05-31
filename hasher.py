import pandas as pd
import hashlib

datafile = 'ANIs.txt'
df = pd.read_csv(datafile)
dataset = pd.DataFrame(index = range(0, len(df)), columns = ['ANI'])

out = open('output.txt','w+')

for i in range(0, len(dataset)):
    ani = str(df['ANI'][i])
    hex_dig = hashlib.sha256(ani.encode())
    hex_dig = hex_dig.hexdigest()
    line = str(df['ANI'][i]) + ';' + str(hex_dig)
    #print(line)
    out.write(line + '\n')

out.close()
