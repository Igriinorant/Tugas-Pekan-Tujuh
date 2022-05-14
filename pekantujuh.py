import pandas as pd

pizza = {'Nama' : ['Agri', 'Ergianto', 'Prasetya','resa','uni','natulistiya','grii','igrii','ilasovik','rosifah'], 'Tinggi Badan':[160,170,180,155,158,164,159,165,154,156], 'Berat Badan' : [50,60,70,55,74,59,56,64,57,45]}

pizza_df = pd.DataFrame(pizza)
pizza_df

print(pizza_df)