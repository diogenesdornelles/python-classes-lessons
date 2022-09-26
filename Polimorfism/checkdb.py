from typing import Dict, List

JSON_ARC = CSV_ARC = str
Data = [Dict, List[Dict]]


def database_json(archive_name: JSON_ARC) -> None:
    print('Created database .json...')
    first_insert: Data = [{"Database": "users"}, []]
    database = archive_name
    import json
    result = json.dumps(first_insert, indent=2, ensure_ascii=False, sort_keys=False)
    with open(database, 'w+', encoding="utf-8") as js:
        js.write(result)


def database_csv(archive_name: CSV_ARC) -> None:
    with open(archive_name, 'w') as arc:
        arc.write('')


def arc_exists(archive_name: [JSON_ARC | CSV_ARC | str]) -> None:
    try:
        a = open(archive_name, 'r')
        a.close()
    except FileNotFoundError:
        print('Database not founded. Create it ')
        criate_arc(archive_name)
    else:
        print('Database founded...')


def criate_arc(archive_name: [JSON_ARC | CSV_ARC | str]) -> None:
    try:
        if archive_name.find('.json') >= 0:
            database_json(archive_name)
        elif archive_name.find('.csv') >= 0:
            database_csv(archive_name)
        else:
            pass  # Open to aggregate new extension database.
    except FileExistsError:
        print('Error occurs in create archive. Try again.')
    else:
        print('...')
