import os
import json
import pandas as pd
from collections import Counter


def count_labels_in_json(directory_path):
    # 创建一个空的Counter对象来统计标签
    label_counter = Counter()

    # 遍历指定文件夹中的所有文件
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)

            # 读取JSON文件并统计label出现次数
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for item in data:
                    if 'label' in item:
                        label_counter[item['label']] += 1

    return label_counter


def export_to_excel(label_counts, output_file):
    # 将统计结果转换为DataFrame
    df = pd.DataFrame(list(label_counts.items()), columns=['Label', 'Count'])

    # 将DataFrame导出到Excel文件
    df.to_excel(output_file, index=False)
    print(f"统计结果已成功导出到 {output_file}")


if __name__ == "__main__":
    # 输入JSON文件所在的文件夹路径
    directory_path = r'D:\垂直领域\dataset\2024_8_26\组件统计'  # 替换为你的JSON文件夹路径
    # 输出Excel文件路径
    output_file = 'label_counts.xlsx'

    # 统计标签并导出到Excel
    label_counts = count_labels_in_json(directory_path)
    export_to_excel(label_counts, output_file)