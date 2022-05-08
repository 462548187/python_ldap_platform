## Python版本
FROM python:3.10.0

# 创建工作目录
RUN mkdir -p /code

# 将当前工作目录设置为 /code
WORKDIR /code

# 添加文件到容器中
ADD . /code

# 正式安装依赖
# !!! 注意--trusted-host 的值为tool.poetry.source的域名
RUN pip install -r /code/requirements.txt

# 运行服务
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
