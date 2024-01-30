from __future__ import unicode_literals
import json
with open('search.json', "r", encoding="utf-8") as json_file:
    data = json.load(json_file)
organ_ver1 = []
title_1 =[]
date_1 = []
id_1 = []
number_1 = []

for doc in data:
    title = doc.get("document").get('titleWithoutEditions')
    organ = (doc.get("document").get('organ'))
    date = (doc.get("document").get('date'))
    id = (doc.get("document").get('id'))
    number = (doc.get("document").get('number'))
    organ_ver1.append(organ)
    title_1.append(title)
    date_1.append(date)
    id_1.append(id)
    number_1.append(number)

dep_m = ['Департамент экономической политики и развития г. Москвы_Департамент экономической политики и развития г. Москвы']

organ_ver2 = []
for x in organ_ver1:
    if dep_m == organ_ver1[0]:
        organ_ver2.append(x)
verifed_1 = set(organ_ver2[0][0].split("_"))
verifed_2 = list(verifed_1)

title_2 = []
for z in title_1:
    if 'Приказ' in z:
        title_2.append(z)

date = []
for c in date_1:
    if '22.01.2024' not in c:
        date.append(c)

id = []
for u in id_1:
    if 'Б=MLAW_Д=41519' not in u:
        id.append(u)

number = []
for i in number_1:
    if i is not None:
        number.append(i)


import pandas as pd



data = { "Date": [date[0], date[1], date[2]],
    "Title": [title_2[0], title_2[1], title_2[2]],
    "Organ": [verifed_2[0], verifed_2[0], verifed_2[0]],
    "Id": [id[0], id[1], id[2]],
    "Number": [number[0], number[1], number[2]]
}
df = pd.DataFrame(data)

df.to_csv('checkpoint.csv', sep='\t', encoding='utf-8')

