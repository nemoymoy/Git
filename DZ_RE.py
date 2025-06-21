from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
temp_list = list()
temp_list.append(['lastname',
  'firstname',
  'surname',
  'organization',
  'position',
  'phone',
  'email'])

pattern = r"(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)"
subst = r"+7(\4)\8-\11-\14 \17\18\20"

for value in contacts_list:
  temp_str = list()
  if len(value[0].split()) == 3:
    last_name = value[0].split()[0]
    first_name = value[0].split()[1]
    sur_name = value[0].split()[2]
  elif len(value[0].split()) == 2:
    last_name = value[0].split()[0]
    first_name = value[0].split()[1]
  elif len(value[0].split()) == 1:
    last_name = value[0]

  if len(value[1].split()) == 2:
    first_name = value[1].split()[0]
    sur_name = value[1].split()[1]
  elif len(value[1].split()) == 1:
    first_name = value[1]

  if len(value[2].split()) == 1:
    sur_name = value[2]

  organization = value[3]
  position = value[4]
  phone = (re.sub(pattern, subst, value[5])).strip()
  email = value[6]

  temp_str.append(last_name)
  temp_str.append(first_name)
  temp_str.append(sur_name)
  temp_str.append(organization)
  temp_str.append(position)
  temp_str.append(phone)
  temp_str.append(email)

  # print(temp_str)

  flag = 0
  for num, str in enumerate(temp_list):
    # print(str[0], str[1])
    if last_name == str[0] and first_name == str[1]:
      flag = 1
      if str[2] == '':
        temp_list[num][2] = sur_name
      if str[3] == '':
        temp_list[num][3] = organization
      if str[4] == '':
        temp_list[num][4] = position
      if str[5] == '':
        temp_list[num][5] = phone
      if str[6] == '':
        temp_list[num][6] = email


  if flag == 0:
    temp_list.append(temp_str)

pprint(temp_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-16") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(temp_list)