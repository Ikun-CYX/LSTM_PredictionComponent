import json
import copy

# 读取 JSON 文件
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# 分类边和组件
def classify_elements(json_data):
    edges = []  # 存放包含 "shape" 键的字典
    components = []  # 存放包含 "data" 键的字典

    for element in json_data:
        if 'source' in element:
            edges.append(element)
        elif 'data' in element:
            components.append(element)

    return edges, components


# 根据ID在组件列表中查找组件
def find_component_by_id(components, component_id):
    for component in components:
        if component.get("id") == component_id:
            return component
    return None


# 更新组件的 behind 键
def update_component_behind(components, edges):
    for edge in edges:
        source_id = edge.get("source").get("cell")
        target_id = edge.get("target").get("cell")

        # 找到 target 组件
        target_component = find_component_by_id(components, target_id)

        # 找到 source 组件
        source_component = find_component_by_id(components, source_id)

        if target_component and source_component:
            label = {}

            label["label"] = target_component.get("label")
            label["id"] = target_component.get("id")

            # 依次检查并更新 behind, behind1, behind2, ...
            # if "behind" in source_component:
            #     i = 1
            #     while f"behind{i}" in source_component:
            #         i += 1
            #     source_component[f"behind{i}"] = label
            # else:
            #     source_component["behind"] = label

            if "behind" not in source_component:
                # 如果没有 "behind" 键，直接添加
                source_component["behind"] = label
            else:
                # 如果已经存在 "behind" 键，创建新的组件字典
                new_component = copy.deepcopy(source_component)
                new_component["id"] = source_id + "_copy"  # 为新的组件生成一个唯一的ID
                new_component["behind"] = label
                components.append(new_component)


# 保存组件列表到 JSON 文件
def save_components_to_json(components, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(components, file, ensure_ascii=False, indent=4)

def delete_component(components):
    for component in components:
        del component["position"]
        del component["size"]
        del component["shape"]
        del component["ports"]

        if "visible" in component:
            del component["visible"]
        if "view" in component:
            del component["view"]
        if "basicComponentData" in component:
            del component["basicComponentData"]
            component["label"] = "Start"

    return components

# 主程序
def main():
    file_path = r'D:\垂直领域\dataset\2024_8_26\4.边_节点\demo10.json'  # 替换为你的 JSON 文件路径
    output_file_path = (r'D:\垂直领域\dataset\2024_8_26\6.新边2\demo10.json')  # 输出的 JSON 文件路径

    json_data = read_json(file_path)
    edges, components = classify_elements(json_data)

    update_component_behind(components, edges)

    components = delete_component(components)

    # 将更新后的组件保存到 JSON 文件
    save_components_to_json(components, output_file_path)

    print(f"Updated components saved to {output_file_path}")

if __name__ == "__main__":
    main()