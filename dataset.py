import json
import numpy as np
# 读取JSON文件

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# 提取x和y的值并将它们添加到一个数组中
def extract_xy(data):
    X = []
    y = []
    for item in data:
        X.append(item['x'])
        y.append(item['y'])

    return X,  y

def split_and_convert_X(input_array):
    # 获取原数组的形状
    num_rows, num_cols = input_array.shape

    # 创建一个新的数组来存储转换后的数据
    # 新数组的形状是 (num_rows, num_cols, 10)
    output_array = np.zeros((num_rows, num_cols, 10), dtype=int)

    # 遍历每个元素，将其拆分并转换为整数
    for i in range(num_rows):
        for j in range(num_cols):
            # 拆分每个字符串为单个字符，并转换为整数
            output_array[i, j] = [int(char) for char in input_array[i, j]]

    return output_array

def split_and_convert_y(input_array):
    # 获取原数组的形状
    num_rows = input_array.shape[0]

    # 创建一个新的数组来存储转换后的数据
    # 新数组的形状是 (num_rows, num_cols, 10)
    output_array = np.zeros((num_rows, 10), dtype=int)

    # 遍历每个元素，将其拆分并转换为整数
    for i in range(num_rows):
            # 拆分每个字符串为单个字符，并转换为整数
        output_array[i] = [int(char) for char in input_array[i]]

    return output_array


def Use_Dataset(file_path):
    data = read_json_file(file_path)

    # 提取x和y的值
    X, y = extract_xy(data)

    numpy_X = np.array(X)
    numpy_y = np.array(y)

    output_array_X = split_and_convert_X(numpy_X)
    output_array_y = split_and_convert_y(numpy_y)

    return output_array_X, output_array_y