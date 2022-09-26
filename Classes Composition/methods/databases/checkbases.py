from typing import Dict, List
import os

JSON_ARC = POSTGRESQL_ARC = str
Data = [Dict, List[Dict]]


def move_to_dir_databases() -> str:
    current_dir = os.getcwd()
    path_databases = r'\methods\databases'
    go_dir_databases = current_dir + path_databases
    os.chdir(go_dir_databases)
    new_dir = r'\all_databases'
    try:
        os.mkdir(new_dir[1:])
    except FileExistsError:
        pass
    path_to_all_data_bases = go_dir_databases + new_dir
    os.chdir(path_to_all_data_bases)
    return current_dir  # return current dir to move back to the main program dir.


def database_json(archive_name: JSON_ARC) -> None:
    print('Created database .json...')
    current_dir = move_to_dir_databases()
    first_insert: Data = [{"Database": "Id(s)"}, []]
    database = archive_name
    import json
    result = json.dumps(first_insert, indent=2, ensure_ascii=False, sort_keys=False)
    with open(database, 'w+', encoding="utf-8") as js:
        js.write(result)
    os.chdir(current_dir)


def database_postgresql(archive_name: POSTGRESQL_ARC) -> None:
    pass


def arc_exists(archive_name: [JSON_ARC | POSTGRESQL_ARC | str]) -> None:
    current_dir = move_to_dir_databases()
    try:
        a = open(archive_name, 'r')
        a.close()
    except FileNotFoundError:
        print('Database not founded. Create it ')
        os.chdir(current_dir)
        criate_arc(archive_name)
    else:
        print('Database founded...')
    finally:
        os.chdir(current_dir)


def criate_arc(archive_name: [JSON_ARC | POSTGRESQL_ARC | str]) -> None:
    try:
        if archive_name.find('.json') >= 0:
            database_json(archive_name)
        elif archive_name.find('.POSTGRESQL') >= 0:
            pass
            # Not implemented: database_POSTGRESQL(archive_name)
        else:
            pass  # Open to aggregate new extension database.
    except FileExistsError:
        print('Error occurs in create archive. Try again.')
    else:
        print('...')
