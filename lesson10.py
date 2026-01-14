import yaml

data = {
    'user': {
        'name': 'Иван Иванов',
        'age': 30,
        'email': 'ivan@example.com'
    },
    'skills': ['Python', 'Django', 'Docker'],
    'is_active': True,
    'projects': [
        {'name': 'Проект 1', 'status': 'completed'},
        {'name': 'Проект 2', 'status': 'in_progress'}
    ]
}

with open('config.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data, file, default_flow_style=False, allow_unicode=True, sort_keys=False)

print("Файл создан успешно!")

with open('config.yaml', 'r', encoding='utf-8') as file:
    loaded_data = yaml.safe_load(file)

print(loaded_data)
print(f"Имя пользователя: {loaded_data['user']['name']}")