
FROM python:3.12 AS train


WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


COPY . .


RUN jupyter mbl_assessment.ipynb


FROM python:3.12 AS inference

WORKDIR /app


COPY --from=mbl_assessment.ipynb /app/model.pickle /app/model.pickle

COPY . .


COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000


CMD ["fastapi", "dev", "main.py"]
