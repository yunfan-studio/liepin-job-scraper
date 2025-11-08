'''这是一个专门爬虫猎聘的脚本'''
# ----------------模块一 导入工具包----------------------
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
# 导入智能等待所需的工具
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ----------------模块二 定义核心爬虫函数------------------------
def scrape_liepin(url):
    """
    启动Selenium浏览器，访问猎聘网并抓取职位列表的HTML。
    
    参数:
    url (str): 要抓取的目标网址。
    
    返回:
    str: 包含职位列表的完整页面HTML源代码。
    """
    print("信息：正在启动机器人浏览器...")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    all_data = [] # 将all_data的初始化移入函数

    try:
        print(f"信息：正在访问目标网址: {url}")
        driver.get(url)
        
        # --- “智能等待” ---
        # 最长等待10秒，直到“看到”第一个class为'job-card-pc-container'出现！
        print("信息：启动智能等待，等待关键目标出现...")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'job-card-pc-container')))
        print("信息：关键目标已加载！")

        html_content = driver.page_source
        print("信息：已获取最终HTML源代码。")

        # ----------------模块三 解析 定位原始数据---------------------
        print("\n信息：HTML解析完毕，开始提取数据...")
        soup = BeautifulSoup(html_content, 'html.parser')
        jobs_card = soup.find_all('div', {'class': 'job-card-pc-container'})
        print(f"【侦察报告】发现 {len(jobs_card)} 个职位卡片！")
        
        if not jobs_card:
            print("警告：未找到任何职位卡片，程序提前结束。")
            return [] 

        for index, job_card in enumerate(jobs_card, 1):
            # 将所有变量的默认值设置在循环内部，确保每次都是新的
            position, salary, company_name, area, experience, education = "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"
            print(f"--- 正在解析第 {index} 号目标 ---")
                       
            detail = job_card.find('div', {'class': 'job-detail-box'})
            if detail:
                header_box = detail.find('div', {'class': 'job-detail-header-box'})
                if header_box:
                    salary_tag = header_box.find('span', {'class': 'job-salary'})
                    if salary_tag:
                        salary = salary_tag.get_text(strip=True) 

                    title_box = header_box.find('div', {'class': 'job-title-box'})     
                    if title_box:
                        ellipsis = title_box.find('div', {'class': 'ellipsis-1'})
                        if ellipsis:
                            position = ellipsis.get_text(strip=True)  
                        ellipsis_1 = title_box.find('span', {'class': 'ellipsis-1'})
                        if ellipsis_1:
                            area = ellipsis_1.get_text(strip=True) 

                job_labels_box = detail.find('div', {'class': 'job-labels-box'})
                if job_labels_box: 
                    labels = job_labels_box.find_all('span', {'class': 'labels-tag'})
                    if len(labels) > 0:  
                        experience = labels[0].get_text(strip=True)    
                    if len(labels) > 1:    
                        education = labels[1].get_text(strip=True)

                job_detail_company_box = detail.find('div', {'class': 'job-detail-company-box'})
                if job_detail_company_box:
                    company_tag = job_detail_company_box.find('span', {'class': 'company-name'})
                    if company_tag:
                        company_name = company_tag.get_text(strip=True)
            
            all_data.append([position, salary, company_name, area, experience, education])
        
        return all_data

    finally:
        driver.quit()
        print("\n信息：机器人浏览器已关闭。")


# ----------------模块四 封装-------------------------
def save_to_csv(data, filename='job_data.csv'):
    """
    将提取的数据保存到CSV文件中。
    
    参数:
    data (list of lists): 包含职位信息的列表。
    filename (str): 要保存的CSV文件名。
    """
    if not data:
        print("警告：没有数据可以保存。")
        return

    with open(filename, 'w', newline='', encoding='utf--sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['职业', '薪资', '公司', '地区', '经验', '学历'])
        writer.writerows(data)
    print(f"\n任务完成！数据已成功写入到文件 {filename}")


# ----------------标准程序入口---------------------
def main():
    """
    程序主入口函数
    """
    target_url = 'https://www.liepin.com/zhaopin/?key=python'
    # 第一步：执行爬取和解析
    scraped_data = scrape_liepin(target_url)
    # 第二步：保存结果
    save_to_csv(scraped_data)


if __name__ == "__main__":
    main()