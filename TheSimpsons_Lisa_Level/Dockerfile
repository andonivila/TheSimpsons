FROM python:3.7.9

COPY ./FuncionPalabras.py /app/
COPY ./requirements.txt /app/

WORKDIR /app/

RUN pip3 install -r ./requirements.txt 

CMD [ "python","FuncionPalabras.py" ]