from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv


def get_data_from_file(file_name='phonebook_raw.csv'):
    with open(file_name, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    contacts = []
    for contact_fields in contacts_list[1:]:
        contacts.append({contacts_list[0][0]: contact_fields[0], contacts_list[0][1]: contact_fields[1],
                         contacts_list[0][2]: contact_fields[2], contacts_list[0][3]: contact_fields[3],
                         contacts_list[0][4]: contact_fields[4], contacts_list[0][5]: contact_fields[5],
                         contacts_list[0][6]: contact_fields[6]})
    return contacts


def correct_names(contacts_data: list):
    for data in contacts_data:
        lastname = data['lastname'].split(' ')
        firstname = data['firstname'].split(' ')
        if len(lastname) == 2 or len(firstname) == 2:
            if len(lastname) == 2:
                data['lastname'], data['firstname'] = lastname[0], lastname[1]
            else:
                data['firstname'], data['surname'] = firstname[0], firstname[1]
        elif len(lastname) == 3:
            data['lastname'], data['firstname'], data['surname'] = lastname[0], lastname[1], lastname[2]
    contacts_to_remove = []
    for id, data in enumerate(contacts_data):
        for idx, contact_info in enumerate(contacts_data[id+1:]):
            if data['lastname'] == contact_info['lastname'] and data['firstname'] == contact_info['firstname']:
                contacts_to_remove.append(idx+id+1)
                for original_contact in data:
                    if data[original_contact] == '' and contact_info[original_contact] != '':
                        data[original_contact] = contact_info[original_contact]

                contacts_data.pop(idx+id+1)
    return contacts_data

def correct_phones(data: list):
    pattern_phone = r'(\+7|8)?\s*\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d*)?\)?'
    for contact in data:
        fixed_phone = re.sub(pattern_phone, r'+7(\2)\3-\4-\5\6\7\8', contact['phone'])
        contact['phone'] = fixed_phone
    return data


if __name__ == '__main__':
    updated_data = get_data_from_file()
    filtered_data = correct_names(updated_data)
    data_with_phone_correction = correct_phones(filtered_data)
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerow(data_with_phone_correction[0].keys())
        for data in data_with_phone_correction:
            datawriter.writerow(data.values())