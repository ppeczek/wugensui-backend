FROM python:3

RUN apt-get update
RUN apt-get install -y libicu-dev screen

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE "wugensui.settings.local"
ENV PORT 8000
EXPOSE 8000

ENTRYPOINT [ "./run.sh" ]
