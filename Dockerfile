FROM postgres
ENV POSTGRES_PASSWORD 123456
ENV POSTGRES_DB face_recognition


ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y cmake && rm -rf /var/lib/apt/lists/*