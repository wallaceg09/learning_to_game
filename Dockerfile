FROM tensorflow/tensorflow:2.7.0-gpu

WORKDIR app
COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y python-opengl ffmpeg xvfb python-opengl
RUN cat requirements.txt | grep -v "tensor\|keras" > requirements_mod.txt && \
    pip install -r requirements_mod.txt

COPY . .

CMD ["python3", "/app/main.py"]
