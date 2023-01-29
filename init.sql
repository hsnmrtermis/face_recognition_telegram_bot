create database face_recognition


create table public.people
(
    id        serial
            primary key,
    name      varchar not null,
    path      text    not null,
    file_name text
);

