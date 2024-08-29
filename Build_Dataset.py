import json

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

file_path = r'D:\垂直领域\dataset\2024_8_26\data\8.测试\demo10.json'  # 替换为你的 JSON 文件路径
output_file_path = r'D:\垂直领域\dataset\2024_8_26\data\9.测试\demo10.txt'  # 输出的 JSON 文件路径
json_data = read_json(file_path)

# 保存组件列表到 JSON 文件
def save_components_to_json(components, output_file_path):
    with open(output_file_path, 'a', encoding='utf-8') as file:
        json.dump(components, file, ensure_ascii=False, indent=4)

def write_dict_to_txt(file_path, dictionary):
    with open(file_path, 'a') as file:
        # 将字典转化为 JSON 格式的字符串
        json.dump(dictionary, file, indent=4)
        file.write(",")
        file.write("\n")

def left_shift_by_one(arr):
    if not arr:  # 如果数组为空，则直接返回原数组
        return arr
    return arr[1:] + arr[:1]

def zhao_core(
        component,
        output_x
):
    if component["behind"] != "null":

        output_x = left_shift_by_one(output_x)
        output_x[-1] = component["behind"]["label"]

        component_id = component["behind"]["id"]

        for i in json_data:
            if i["id"] == component_id:
                component = i
                if component["behind"] != "null":
                    output_y = component["behind"]["label"]
                else:
                    output_y = "null"
                output = {}
                output["x"] = output_x
                output["y"] = output_y
                print(output)

                write_dict_to_txt(output_file_path, output)
                zhao_core(component, output_x)
def main():

    component = json_data[0]
    output = {
    }
    output_x = ["null", "null", "null", "null", "null", component["label"]]
    output_y = component["behind"]["label"]

    output["x"] = output_x
    output["y"] = output_y

    write_dict_to_txt(output_file_path, output)

    print(output)

    zhao_core(component, output_x)

    if component["behind"] != "null":
        output_x = left_shift_by_one(output_x)
        output_x[-1] = component["behind"]["label"]

    for item in json_data:
        if "behind" not in item.keys():
            item["behind"] = "null"

    print(f"Updated components saved to {output_file_path}")

if __name__ == "__main__":
    main()