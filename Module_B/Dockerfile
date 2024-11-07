FROM python:3.9

WORKDIR /Module_B

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/bin/bash", "-c", "uvicorn api.main:app --host 0.0.0.0 --port 8000 & streamlit run ui/app.py"]