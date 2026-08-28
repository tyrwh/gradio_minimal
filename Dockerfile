FROM public.ecr.aws/docker/library/python:3.12-slim

COPY . .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 7860
CMD ["python3", "app.py"]
