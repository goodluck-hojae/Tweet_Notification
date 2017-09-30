FROM python:3

RUN pip3 install tweepy

ADD main.py /

CMD [ "python3", "./main.py" ]