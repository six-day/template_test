from string import Template
import json
# 需要pip install pyyaml
import yaml

# dumps() 将dict转为json格式的字符串
# loads(string) 将string类型转为dict
# dump() 将python对象写入文件
# load() 从文件中读取json数据


def replace_json_file_yaml():
    context = dict_to_json_str(read_json("./template.json"))
    temp_template = Template(context)
    parameters = yaml_to_json("./parameters.yml")
    temp_str1 = temp_template.safe_substitute(parameters)
    print(temp_str1)
    write_file(temp_str1)
    print("=======================替换json结束，参数从yaml读取================")


def replace_json_file():
    temp_template = Template(dict_to_json_str(read_json("./template.json")))
    parameters = read_json("./parameters.json")
    temp_str1 = temp_template.safe_substitute(parameters)
    print(temp_str1)
    print("=======================替换json结束================")


def replace_string():
    temp_template = Template("My name is ${name} , i like ${fancy}， i don't like ${test}")
    parameters = read_json("./parameters.json")
    temp_str1 = temp_template.safe_substitute(parameters)
    print(temp_str1)
    print("=======================替换字符串结束================")


def read_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        # load()函数将fp(一个支持.read()的文件类对象，包含一个JSON文档)反序列化为一个Python对象
        data = json.load(file)
    file.close()
    return data


def yaml_to_json(yaml_path):
    with open(yaml_path, 'r', encoding="utf-8") as file:
        # 将文件的内容转换为字典形式
        datas = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    json_str = dict_to_json_str(datas)
    return json_str_to_dict(json_str)


def write_file(context):
    with open('test.json', 'w', encoding="utf-8") as file:
        # indent参数能将字典按照json样式可视化显示
        json.dump(json_str_to_dict(context), file, ensure_ascii=False, indent=4)
    file.close()


# 将string类型转为dict
def json_str_to_dict(data):
    return json.loads(data)


# 将字典的内容转换为json格式的字符串
def dict_to_json_str(data):
    return json.dumps(data, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    replace_string()
    replace_json_file()
    replace_json_file_yaml()

