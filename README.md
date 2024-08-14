# 正方教务课表转 ics

本项目仅为满足个人需要+练手，代码一坨且注释也不全，别骂（

## 使用方法

### 安装

```
git clone https://github.com/your_username/your_repository.git
```

### 安装依赖

```
pip install -r requirements.txt
```

### 使用

```
python main.py -t <type> -f <first_Monday> -i <input> -o <output> -c <config>
    -t --type：指定需要转换的事件类别，可选值为 `class`（课表）或 `exam`（考试）。
    -f --first-Monday：指定该学期第一周的周一日期，格式为年-月-日。
    -i --input：指定输入文件的路径。
    -o --output：指定输出文件的路径。
    -c --config：指定配置文件的路径，默认为当前目录下的 `config.json`。
```

-   在正方教务课表页面点击查询，自行保存其响应的带有课表信息的 json。此处可以使用 getjson 工具（修改 url 即可）

-   根据提示输入需要的信息，然后 ics 文件就导出来了...

## 待完成列表

-   [x] 考试信息转 ics
-   [ ] 输入账号密码登录后自动获取课表信息的json并导出ics文件
-   [ ] 尝试把代码写得不那么 💩
