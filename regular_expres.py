from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

def read_csv():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


contacts_list = read_csv()
my_contacts_list = []
my_contacts_list.append(contacts_list[0])
my_list = []

for list in contacts_list[1:]:
    my_list = (' '.join(list[:3])).split()

    if len(my_list) == 2:
      my_list.append('')

    for i in list[3:5]:
        my_list.append(i)

    patterh_phone_1 = re.compile(
        r"(\+7|8)?\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d+)\s?\(?(доб\.\s(\d+))?\)?")
    patterh_phone_2 = re.compile(r"(\+7|8)?\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d+)\s?")

    if 'доб' in list[5]:
        resul = patterh_phone_1.sub(r"+7(\2)\3-\4-\5 доб.\7", list[5])
        if resul == list[5]:
            my_list.append('')
        else:
            my_list.append(resul)
    else:
        resul = patterh_phone_2.sub(r"+7(\2)\3-\4-\5", list[5])
        if resul == list[5]:
            my_list.append('')
        else:
            my_list.append(resul)

    my_list.append(list[-1])

    for list in my_contacts_list:
        if my_list[:2] == list[:2]:
            for i in range(len(my_list)):
                if (list[i] == '') and (my_list[i] != ''):
                    list.pop(i)
                    list.insert(i, my_list[i])
            my_list.clear()

    if my_list:
        my_contacts_list.append(my_list)


def write_csv():
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(my_contacts_list)
write_csv()