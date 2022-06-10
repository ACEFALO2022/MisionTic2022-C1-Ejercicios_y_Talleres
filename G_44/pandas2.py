import pandas as pd
s = pd.Series({'Matematicas':3.5,'Historia':4.3,'Economia':3.1,'Programacion':4.1,'Ingles':3.4}, dtype='string')
print(s)

print('----accesar posiciones lista----')
print(s[1:4])  #accesar a las posiciones
print()
print(s['Historia'])
print()
print(s[['Historia','Ingles']])


