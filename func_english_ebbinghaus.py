import json
import datetime
from datetime import timedelta

class EnglishEbbinghaus:
    def __init__(self, file_path, progress_file):
        self.file_path = file_path
        self.progress_file = progress_file
        self.review_intervals = [1, 2, 4, 7, 15]  # 复习间隔（天）

    def load_progress(self):
        try:
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_progress(self, progress):
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(progress, f, indent=4)

    def get_review_dates(self, start_date):
        review_dates = []
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        for interval in self.review_intervals:
            review_dates.append((start + timedelta(days=interval)).strftime("%Y-%m-%d"))
        return review_dates

    def update_progress(self, start_line, new_words):
        progress = self.load_progress()
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        progress[str(start_line)] = {
            "start_date": today,
            "review_dates": self.get_review_dates(today),
            "words": new_words
        }
        self.save_progress(progress)

    def print_review_words(self):
        progress = self.load_progress()
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        for group, data in progress.items():
            if today in data["review_dates"]:
                print(f"Review Group {group}: {data['words']}")

    # 其他方法（读取和打印单词，重置计数器等）...

    def print_review_words(self):
        progress = self.load_progress()
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"Today's date for review: {today}")
        print("Progress data loaded:", progress)  # 调试：打印加载的进度数据

        for group, data in progress.items():
            if today in data["review_dates"]:
                print(f"Review Group {group}: {data['words']}")
            else:
                print(f"No review for Group {group} today.")  # 调试：显示哪些组今天不需要复习


if __name__ == "__main__":
    file_path = 'cet6_words.txt'  # 单词文件路径
    progress_file = 'progress.json'  # 学习进度文件路径
    ebbinghaus = EnglishEbbinghaus(file_path, progress_file)

    # ebbinghaus.update_progress(start_line, new_words)  # 用于更新进度的示例

    ebbinghaus.print_review_words()  # 打印今天需要复习的单词