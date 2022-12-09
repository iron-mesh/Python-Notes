'''Привести строки, которые вышли из-под QtDesigner и не содержали латинских символов в удобочитаемый вид'''

import re, codecs

file_list = [r"D:\MAIN\Программирование\Проекты\Python_Notes\Multilanguage_Qt_App\ui_spaceship_control_panel.py"] # список путей к файлам, которые надо пофиксить
target_list =[r"D:\MAIN\Программирование\Проекты\Python_Notes\Multilanguage_Qt_App\ui_spaceship_control_panel2.py"] # список путей к файлам, где будет сохранен результат
regex = re.compile(r", u\"(.*)\",")

for i in range(0,len(file_list)):
    with open(file_list[i], "r") as file:
        data = file.read()

    extracted_strings=regex.findall(data)

    with open(target_list[i], "w", encoding="utf-8") as file:
        for es in extracted_strings:
            raw = r'{0}'.format(es)
            data=data.replace(
                raw,
                codecs.decode(es, "unicode-escape"))

        file.write(data)


