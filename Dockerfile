FROM python:3.6.8-stretch

USER root

COPY . . 

RUN apt update && apt install -y gdebi-core libnss3 libgconf-2-4
ADD google-chrome-stable_current_amd64.deb .
RUN gdebi -n google-chrome-stable_current_amd64.deb

WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD chromedriver .
#RUN chmod +x chromedriver

RUN mv chromedriver /bin/chromedriver
RUN root:root /bin/chromedriver
RUN chmod a+x /bin/chromedriver


# ADD app.py .
ADD app.py .

# CMD python3 test.py
CMD python3 app.py
# CMD python3 app.py & python3 test.py

