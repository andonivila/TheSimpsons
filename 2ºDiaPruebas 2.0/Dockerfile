FROM python:3.7.9

COPY ./a.py .
COPY /requirements.txt . 

WORKDIR .
RUN pip3 install -r requirements.txt 

CMD [ "python" , "a.py" ]

