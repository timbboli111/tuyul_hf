FROM python:3.9-slim
RUN pip install --no-cache-dir requests
COPY tuyul_hf.py .
CMD ["python", "tuyul_hf.py"]
