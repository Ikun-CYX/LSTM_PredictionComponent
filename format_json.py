import json
import sys

def format_json(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            data = json.load(infile)
        
        with open(output_file, 'w') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)
        
        print(f"JSON 文件已成功格式化并保存到 {output_file}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python format_json.py <输入文件> <输出文件>")
    else:
        format_json(sys.argv[1], sys.argv[2])