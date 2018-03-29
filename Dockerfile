FROM python:3.6-slim
LABEL maintainer "jack092123@gmail.com"

EXPOSE 8000
ENV DJANGO_PORT 8000

RUN apt-get update && apt-get install -y \
		gcc \ 
		gettext \ 
		sqlite3 \
		git \ 
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /home
RUN git clone https://github.com/jack092123/ToDoList-Django.git

WORKDIR /home/ToDoList-Django
RUN pip install -r ./requirements.txt

ENTRYPOINT ["python", "./server/manage.py", "runserver", "0.0.0.0:$DJANGO_PORT"]
