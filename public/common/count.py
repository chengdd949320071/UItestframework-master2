import os

k_file_extension = '.py'


def get_file_list():
    file_list = [os.path.join(root, file) for root, dirs, files in os.walk(file_path) for file in files if
                 file.endswith(k_file_extension)]
    return file_list


def count_code_lines(file_list):
    count_of_code_lines = 0
    count_of_blank_lines = 0
    count_of_annotation_lines = 0
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as fp:
            content_list = fp.readlines()
            for content in content_list:
                content = content.strip()
                if content == '':
                    count_of_blank_lines += 1
                elif content.startswith('#'):
                    count_of_annotation_lines += 1
                else:
                    count_of_code_lines += 1
    print(f'代码总行数：{count_of_code_lines}，代码空行：{count_of_blank_lines}，代码注释：{count_of_annotation_lines}')


if __name__ == '__main__':
    file_path = r'C:\Users\Administrator\PycharmProjects\UItestframework-master'
    count_code_lines(get_file_list())
