'''
- 负责读取原始数据 (job_data.csv)
- 调用清洗函数
- 封装成最终的干净数据 (cleaned_job_data.csv)
'''
import csv
from liepin_cleaner import clean_liepin_data 


def process_data(input_filename, output_filename):
    """
    读取、清洗、并保存数据的核心流程。
    """

    print(f"信息：正在从 {input_filename} 读取原始数据...")
    try:
        with open(input_filename, 'r', encoding='utf-8-sig') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            all_dirty_rows = list(reader)
    except FileNotFoundError:
        print(f"【错误！】找不到原始数据文件：{input_filename}。请先运行爬虫脚本！")
        return
    print(f"信息：成功加载 {len(all_dirty_rows)} 条脏数据。")

    print("\n信息：开始执行清洗流程...")
    all_cleaned_data = []
    for a_single_dirty_row in all_dirty_rows:
        try:
            cleaned_row = clean_liepin_data(*a_single_dirty_row)
            all_cleaned_data.append(cleaned_row)
        except TypeError:
            print(f"【警告】数据行格式错误，已跳过: {a_single_dirty_row}")   
    print("信息：所有数据，清洗完毕！")

    print(f"\n信息：正在将清洗后的数据，写入 {output_filename}...")
    with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(all_cleaned_data)
    print("【胜利！】任务完成！")


def main():
    """
    程序主入口
    """
    raw_data_file = 'job_data.csv'
    cleaned_data_file = 'cleaned_job_data.csv'
    process_data(raw_data_file, cleaned_data_file)


if __name__ == "__main__":
    main()
