#
FROM python:3.9

#
WORKDIR /code

#
COPY requirments.txt /code/requirments.txt

#
RUN pip3 install --no-cache-dir --upgrade -r /code/requirments.txt

#
COPY main.py /code/

#
COPY city.csv /code/

#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
