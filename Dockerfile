# DOCKER FOR FIBONACCI PROGRAM

FROM python:3.11.1

ADD Fibonacci_test.py .

RUN pip install numpy

ENTRYPOINT ["python", "./Fibonacci_test.py"]
