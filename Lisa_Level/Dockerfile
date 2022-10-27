FROM python

COPY ./lisa_level.py /app/
COPY ./requirements.txt /app/

WORKDIR /app/ 

RUN pip3 install -r ./requirements.txt

CMD ["python","lisa_level.py"]

