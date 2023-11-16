from datetime import datetime


class English:
    # ...其他方法...

    def __init__(self):

        self.file_path = 'cet6_words.txt'
        self.counter_file = 'counter.txt'
        self.total_lines = self.get_total_lines()

    def get_total_lines(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return sum(1 for _ in file)

    def read_and_print_lines(self):
        # 获取当前日期
        now = datetime.now()
        current_date = now.strftime("%m-%d")  # 格式化为"月-日"

        # 初始化返回的字符串，首行为当前日期，下一行为空行
        lines_to_return = f"{current_date} 每日单词\n\n"

        try:
            with open(self.counter_file, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                start_line, exec_count = map(int, content.split(',')) if ',' in content else (0, 0)
        except FileNotFoundError:
            start_line, exec_count = 0, 0

        end_line = start_line + 20
        current_line = 0

        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if start_line <= current_line < end_line:
                    lines_to_return += line.strip() + "\n"
                current_line += 1

        exec_count += 1
        if exec_count >= 3:
            exec_count = 0
            start_line = end_line

            # 当达到文件末尾时，重新开始
            if start_line >= self.total_lines:
                start_line = 0

        with open(self.counter_file, 'w', encoding='utf-8') as f:
            f.write(f'{start_line},{exec_count}')

        return lines_to_return.strip()


if __name__ == "__main__":
    english = English()
    result = english.read_and_print_lines()
    print(result)
