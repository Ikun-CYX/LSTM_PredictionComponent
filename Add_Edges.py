import json


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# 保存组件列表到 JSON 文件
def save_components_to_json(components, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(components, file, ensure_ascii=False, indent=4)


def main():
    file_path = r'D:\垂直领域\dataset\2024_8_26\data\7.新边2_删除环\demo10.json'  # 替换为你的 JSON 文件路径
    output_file_path = (r'D:\垂直领域\dataset\2024_8_26\data\8.测试\demo10.json')  # 输出的 JSON 文件路径

    json_data = read_json(file_path)

    for item in json_data:
        if "behind" not in item.keys():
            item["behind"] = "null"


    save_components_to_json(json_data, output_file_path)

    print(f"Updated components saved to {output_file_path}")

if __name__ == "__main__":
    main()