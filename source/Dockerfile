FROM python:3.9-buster
WORKDIR /app 
COPY . .

ARG ACCESS_ID
ENV ACCESS_ID=$ACCESS_ID
ARG ACCESS_KEY
ENV ACCESS_KEY=$ACCESS_KEY

ENV CUSTOM_HOUR=1000
RUN pip install boto3

CMD ["python3", "detect-old-accesskeys.py"]