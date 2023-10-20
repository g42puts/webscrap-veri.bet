import json

def save_json(class_list) -> None:
    data_as_dict = [item.__dict__ for item in class_list]
    
    file_path = "scrap_sports.json"

    try:
        with open(file=file_path, mode='r', encoding='utf-8') as json_file:
            existing_data = json.load(fp=json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    # Adicione os novos dados à lista existente
    existing_data.extend(data_as_dict)

    # Escreva a lista completa de dados de volta ao arquivo JSON
    with open(file=file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(obj=existing_data, fp=json_file, indent=4)