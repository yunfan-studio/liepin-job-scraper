猎聘网Python职位数据爬虫与清洗项目 (Liepin Job Scraper)
这是一个使用Python开发的自动化数据项目，旨在从猎聘网 (liepin.com) 抓取与特定关键词（如“Python”）相关的职位信息，对原始数据进行结构化清洗，并最终将干净的数据存储为CSV文件。

  项目目标 (Project Goal)
自动化数据采集: 自动访问目标网站，获取职位列表的动态加载内容。
精准数据解析: 从复杂的HTML结构中，准确提取出每一项关键的职位信息（如职位名称、薪资、公司、地点、经验要求、学历要求）。
结构化数据清洗: 对提取的原始“脏”数据，进行标准化、规范化的清洗，使其成为可直接用于分析的“干净”数据。
模块化代码架构: 整个项目被设计为三个独立的模块（爬虫、清洗、主控），实现了高度的解耦和可维护性。
🛠️ 技术栈 (Technology Stack)
Python 3: 项目核心开发语言。
Selenium: 用于驱动浏览器，模拟真人访问，并获取JavaScript动态渲染后的最终网页源代码。
BeautifulSoup4: 强大的HTML/XML解析库，用于从HTML中精准地定位和提取数据。
webdriver-manager: 自动管理浏览器驱动，实现“开箱即用”，无需手动配置ChromeDriver。
  如何运行 (How to Run)

  
1. 准备环境

确保您的电脑已安装 Python 3。
克隆或下载本项目到您的本地。


2. 安装依赖

打开您的终端（或CMD），进入项目所在的文件夹，运行以下命令，安装本项目所需的所有库：
pip install -r requirements.txt


3. 执行项目

项目执行分为两步，严格按照顺序操作：

第一步：运行爬虫脚本，获取原始数据
在终端中运行（请确保文件名与您的文件名一致）：
python liepin_scraper.py

运行结束后，项目文件夹内会生成一个名为 job_data.csv 的文件，里面包含了所有未经处理的原始数据。

第二步：运行主控脚本，清洗并生成最终数据
接着运行：
python liepin_main.py

运行结束后，文件夹内会生成一个名为 cleaned_job_data.csv 的文件，这就是我们最终的、干净的数据成品！

📂 文件结构 (File Structure)
.
├── liepin_scraper.py             # 模块一：负责执行爬虫，抓取原始数据并保存为 job_data.csv
├── liepin_cleaner.py             # 模块二：包含核心的数据清洗函数
├── liepin_main.py                # 模块三：主控脚本，负责读取原始数据，用清洗函数，并保存最终结果
├── requirements.txt       # 项目依赖库清单
└── README.md              # 就是本文件，项目说明书
