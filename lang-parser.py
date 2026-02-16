import re

class RuLangParser:
    def __init__(self):
        self.html_output = ""

    def parse_line(self, line):
        if "СОЗДАТЬ СТРАНИЦУ" in line:
            title_match = re.search(r'ЗАГОЛОВОК "(.*?)"', line)
            description_match = re.search(r'ОПИСАНИЕ "(.*?)"', line)
            title = title_match.group(1) if title_match else ""
            description = description_match.group(1) if description_match else ""
            self.html_output += f"<html><head><title>{title}</title></head><body><h1>{title}</h1><p>{description}</p>"
        elif "СОЗДАТЬ ФОРМУ" in line:
            self.html_output += '<form method="post">'
        elif "ПОЛЕ ВВОДА" in line:
            label_match = re.search(r'МЕТКА: "(.*?)"', line)
            label = label_match.group(1) if label_match else ""
            self.html_output += f'<label>{label}</label><input type="text" required>'
        elif "КНОПКА" in line:
            button_match = re.search(r'КНОПКА "(.*?)"', line)
            button_text = button_match.group(1) if button_match else ""
            self.html_output += f'<button type="submit">{button_text}</button>'
        elif "СОЗДАТЬ ТАБЛИЦУ" in line:
            self.html_output += '<table>'
        elif "СТОЛБЕЦ" in line:
            header_match = re.search(r'ЗАГОЛОВОК: "(.*?)"', line)
            header = header_match.group(1) if header_match else ""
            self.html_output += f'<th>{header}</th>'
        elif "СОЗДАТЬ ВЫПАДАЮЩИЙ СПИСОК" in line:
            self.html_output += '<select>'
        elif "ОПЦИЯ" in line:
            option_match = re.search(r'С ТЕКСТОМ "(.*?)"', line)
            option_text = option_match.group(1) if option_match else ""
            self.html_output += f'<option>{option_text}</option>'
        elif "СОЗДАТЬ СЛАЙДЕР" in line:
            min_match = re.search(r'МИНИМУМ: (\d+)', line)
            max_match = re.search(r'МАКСИМУМ: (\d+)', line)
            step_match = re.search(r'ШАГ: (\d+)', line)
            min_val = min_match.group(1) if min_match else "0"
            max_val = max_match.group(1) if max_match else "100"
            step_val = step_match.group(1) if step_match else "1"
            self.html_output += f'<input type="range" min="{min_val}" max="{max_val}" step="{step_val}">'
        elif "КОНЕЦ ФОРМЫ" in line:
            self.html_output += '</form>'
        elif "КОНЕЦ ТАБЛИЦЫ" in line:
            self.html_output += '</table>'
        elif "КОНЕЦ СТРАНИЦЫ" in line:
            self.html_output += '</body></html>'

    def parse(self, code):
        lines = code.split('\n')
        for line in lines:
            self.parse_line(line)
        return self.html_output

# Example usage:
# Uncomment to use:
# parser = RuLangParser()
#
# with open('РуЯзык.руяз', 'r', encoding='utf-8') as file:
#     ru_lang_code = file.read()
#
# html_code = parser.parse(ru_lang_code)
# with open('output.html', 'w', encoding='utf-8') as file:
#     file.write(html_code)
