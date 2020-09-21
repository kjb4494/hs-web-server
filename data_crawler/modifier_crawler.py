from bs4 import BeautifulSoup
import requests
import enum
import sys
import json


class Modifiers(enum.Enum):
    Military = 0
    Navy = 1
    Flagships = 2
    Diplomacy = 3
    Economy = 4
    Technology = 5
    Court = 6
    Government = 7
    Estates = 8
    HolyRomanEmpire = 9
    Culture = 10
    Stability = 11
    Subject = 12
    Espionage = 13
    Religion = 14
    Colonisation = 15
    Trade = 16


def get_modifier_list_from_eu4_wiki(with_default_value=False):
    try:
        req = requests.get('https://eu4.paradoxwikis.com/Modifier_list')
    except requests.ConnectionError:
        print('wiki connect fail... please check your network.')
        sys.exit()

    if req.status_code != 200:
        print('wiki connect fail... status is not 200.')
        sys.exit()

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    modifier_tables = soup.find_all(
        'table',
        {'class': ['wikitable', 'sortable', 'jquery-tablesorter']}
    )[:len(Modifiers)]

    modifier_list = []

    for idx, modifier_table in enumerate(modifier_tables):
        trs = modifier_table.find_all('tr')
        tr_th, tr_tds = trs[0], trs[1:]
        modifier_names = [th.text.strip().lower().replace(' ', '_') for th in tr_th.find_all('th')]
        for tr_td in tr_tds:
            tds = tr_td.find_all('td')
            modifier_values = [td.text.strip().replace('<', '&lt;').replace('>', '&gt;') for td in tds]
            modifier = {
                'm_type': Modifiers(idx).name
            }
            for i in range(len(modifier_names)):
                modifier[modifier_names[i]] = modifier_values[i]
            if with_default_value:
                try:
                    modifier['default_value'] = float(modifier['example'].split()[-1])
                except:
                    modifier['default_value'] = 1.0
            modifier_list.append(modifier)

    return modifier_list


def get_dump_data(model, fields_list):
    data_list = []
    for fields in fields_list:
        data_list.append({
            'model': model,
            'fields': fields
        })
    return data_list


def generate_json_file(dump_data, output_name='dumpdata.json'):
    with open(output_name, 'w') as fout:
        json.dump(dump_data, fout)


def main_code():
    try:
        modifier_list = get_modifier_list_from_eu4_wiki(with_default_value=True)
        dump_data = get_dump_data('testapp.modifier', modifier_list)
        output_name = '../modifier_data.json'
        generate_json_file(dump_data=dump_data, output_name=output_name)
        print(output_name, '파일을 생성했습니다.')
    except Exception as err:
        print("데이터 파일 생성에 실패했습니다.", err)


if __name__ == '__main__':
    main_code()
