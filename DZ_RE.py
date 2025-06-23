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

  full_name = ' '.join(value[:3]).split()
  last_name = full_name[0] if len(full_name) > 0 else ''
  first_name = full_name[1] if len(full_name) > 1 else ''
  sur_name = full_name[2] if len(full_name) > 2 else ''

  organization = value[3]
  position = value[4]
  phone = (re.sub(pattern, subst, value[5])).strip()
  email = value[6]

  temp_str = list()
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