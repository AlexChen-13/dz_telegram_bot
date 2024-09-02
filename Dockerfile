FROM python:3.10-slim
ENV TOKEN='7527530122:AAH0mbSvzURxooNmhp0OgsITvRr9h5nqsbg'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]