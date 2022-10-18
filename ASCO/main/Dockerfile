FROM python:3.7.12

COPY ./main.py /app/
COPY ./requirements.txt /app/

WORKDIR /app/
RUN mkdir /Lisa
RUN pip3 install -r requirements.txt 

CMD [ "python" , "main.py" ]

