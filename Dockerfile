FROM python:alpine
RUN mkdir /app
RUN pip3 install flask requests
COPY main.py /app
WORKDIR /app
ENV HOST="0.0.0.0"
EXPOSE 5000

CMD ["python3" "main.py"]
