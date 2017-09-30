FROM python:3

RUN pip3 install tweepy
RUN pip3 install telepot
RUN pip3 install googletrans


ADD main.py / 
ADD TwitterListener.py /
ADD TelegramBot.py /
ADD twitter_list
ADD twitter_name_id

CMD [ "python3", "./main.py" ]