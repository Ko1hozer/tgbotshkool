import os

# Список папок и файлов для создания
project_structure = {
    'telegram_bot': [
        'bot.py',
        'config.py',
        'requirements.txt',
        '.env',
        {'handlers': [
            '__init__.py',
            'main_menu.py',
            'schedules.py',
            'grades.py',
            'weather.py',
            'settings.py',
            'parent.py',
        ]},
        {'keyboards': [
            '__init__.py',
            'main_menu_kb.py',
            'schedules_kb.py',
            'grades_kb.py',
            'weather_kb.py',
            'settings_kb.py',
            'parent_kb.py',
            'weekdays_kb.py',
            'subjects_kb.py',
            'notifications_kb.py',
            'delete_schedule_kb.py',
        ]},
        {'utils': [
            '__init__.py',
            'db.py',
            'weather_api.py',
            'notifications.py',
            'logger.py',
        ]},
        {'data': []},
    ],
}

def create_structure(base_path, structure):
    for item in structure:
        if isinstance(item, dict):
            for folder_name, contents in item.items():
                folder_path = os.path.join(base_path, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                create_structure(folder_path, contents)
        else:
            file_path = os.path.join(base_path, item)
            if not os.path.exists(file_path):
                open(file_path, 'w').close()

def main():
    create_structure('.', project_structure['telegram_bot'])
    print("Структура проекта создана успешно.")

if __name__ == '__main__':
    main()
