import json

# 读取文件
with open(r'D:\垂直领域\dataset\2024_8_26\data\merged.json', 'r') as f:
    first_data = json.load(f)

with open(r'D:\垂直领域\dataset\2024_8_26\data\definition.json', 'r') as f:
    second_data = json.load(f)

# 替换组件字符串为序号
for item in first_data:
    item['x'] = [second_data[comp] for comp in item['x']]
    item['y'] = second_data[item['y']]

# 保存到新的 JSON 文件
with open(r'D:\垂直领域\dataset\2024_8_26\data\converted_file.json', 'w') as f:
    json.dump(first_data, f, indent=4)
