
'''
- 包含一个专门用于清洗从猎聘网抓取的职位数据的函数。
'''

import re


def clean_liepin_data(position, salary, company_name, area, experience, education):
    """
    【专业说明书！】
    一个专门处理猎聘网原始数据的清洗函数。
    接收六个字符串作为输入，返回清洗后的六个字符串元组。

    清洗规则:
    - 职位: 去除括号内容
    - 薪资: 处理'面议'和'·'的情况
    - 公司: 去除括号和斜杠后的内容
    - 地区: 只保留'-'之前的部分
    - 经验: 提取核心数字或关键词
    - 学历: 去除'统招'字样
    """ 


    # ------规则一 清洗职位-----------
    cleaned_position = re.sub(r"\(.*?\)|（.*?）", "", position)
    
    if '面议' in salary: 

        cleaned_salary = '面议'
    elif '·' in salary:
    
        cleaned_salary = re.sub(r'·(.*?)薪', "", salary)
    else:
       
        cleaned_salary = salary
    cleaned_company_name = re.sub(r"\(.*?\)|（.*?）|/.*", "", company_name)

    cleaned_area = re.sub(r"-.*", "", area)

    
    cleaned_experience = re.search(r"(\d+)|经验不限|实习|(\d+)-(\d+)", experience)
    if cleaned_experience:
        cleaned_experience = cleaned_experience.group(0)
    else:
        cleaned_experience = experience

    cleaned_education = re.sub(r"统招", "", education)
    
    
    return cleaned_position, cleaned_salary, cleaned_company_name, cleaned_area, cleaned_experience, cleaned_education.strip()
    
