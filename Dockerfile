#
FROM python:3.9

#
WORKDIR /code

#
COPY app/requirments.txt /code/requirments.txt

#
RUN pip3 install --no-cache-dir --upgrade -r /code/requirments.txt

#
COPY app/main.py /code/

#
COPY app/city.csv /code/

#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
