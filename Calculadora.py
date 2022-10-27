import re

file_regras = open("Rules.txt", 'r')

list_rules = []
for line in file_regras:
    line = line.replace("\n", "")
    list_rules.append(line)
    
new_list_rules = []
for line in list_rules:
    line = str(line)
    number = float(re.findall(r'-?\d+\.?\d*', line).__getitem__(0))
    print(number)
    if "T" in line:
        new_value = f"{number * 1000}G"
    elif "M" in line:
        new_value = f"{number / 1000}G"
    elif "k" in line:
        new_value = f"{number / 1000000}G"
    elif "G" in line:
        new_value = line
    else:
        new_value = f"{number}Desconhecido"
    print(new_value)
    new_list_rules.append(new_value)
    
print(list_rules)
print(new_list_rules)