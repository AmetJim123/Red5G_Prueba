toc.dat                                                                                             0000600 0004000 0002000 00000006716 14340254072 0014452 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP                       
    z            prueba_tecnica_backend    15.0    15.0     	           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false         
           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                    0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                    1262    16671    prueba_tecnica_backend    DATABASE     x   CREATE DATABASE prueba_tecnica_backend WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
 &   DROP DATABASE prueba_tecnica_backend;
             
   ametjimgra    false         ?            1259    16673    medico    TABLE     ?   CREATE TABLE public.medico (
    id integer NOT NULL,
    nombre character varying(150),
    apellido character varying(150),
    email character varying(150),
    password character varying(150),
    token character varying(255)
);
    DROP TABLE public.medico;
       public         heap    postgres    false         ?            1259    16672    medico_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.medico_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.medico_id_seq;
       public          postgres    false    215                    0    0    medico_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.medico_id_seq OWNED BY public.medico.id;
          public          postgres    false    214         ?            1259    16686 	   pacientes    TABLE     A  CREATE TABLE public.pacientes (
    nombre character varying(150),
    id bigint,
    edad bigint,
    genero character varying(150),
    temperatura_corporal character varying(150),
    malestar character varying(150),
    fecha_ingreso date,
    eps character varying(150),
    tipo_documento character varying(150)
);
    DROP TABLE public.pacientes;
       public         heap    postgres    false         s           2604    16676 	   medico id    DEFAULT     f   ALTER TABLE ONLY public.medico ALTER COLUMN id SET DEFAULT nextval('public.medico_id_seq'::regclass);
 8   ALTER TABLE public.medico ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214    215                   0    16673    medico 
   TABLE DATA           N   COPY public.medico (id, nombre, apellido, email, password, token) FROM stdin;
    public          postgres    false    215       3589.dat           0    16686 	   pacientes 
   TABLE DATA           ?   COPY public.pacientes (nombre, id, edad, genero, temperatura_corporal, malestar, fecha_ingreso, eps, tipo_documento) FROM stdin;
    public          postgres    false    216       3590.dat            0    0    medico_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.medico_id_seq', 2, true);
          public          postgres    false    214         u           2606    16680    medico medico_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.medico
    ADD CONSTRAINT medico_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.medico DROP CONSTRAINT medico_pkey;
       public            postgres    false    215                                                          3589.dat                                                                                            0000600 0004000 0002000 00000000455 14340254072 0014267 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	Amet	Jimenez	jimenezamet@gmail.com	Amet12345	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6bnVsbH0.I_70zL6MrQbzTzqQ39x0ph_RN-q0ZEEOmjD3Z06ckmA
2	Carlos	Perez	carlosPE@gmail.com	asdjasdlakdj	eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6bnVsbH0.poC7CYF-aWvyp63cfMiGWJekUZIl7zJiZGUB-eHQfeY
\.


                                                                                                                                                                                                                   3590.dat                                                                                            0000600 0004000 0002000 00000000142 14340254072 0014250 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        Karen tana	1232342323	10	femenino	45 grados C	Insolacion	2022-12-21	alcafe	tarjeta identidad
\.


                                                                                                                                                                                                                                                                                                                                                                                                                              restore.sql                                                                                         0000600 0004000 0002000 00000007207 14340254072 0015373 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 15.0
-- Dumped by pg_dump version 15.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE prueba_tecnica_backend;
--
-- Name: prueba_tecnica_backend; Type: DATABASE; Schema: -; Owner: ametjimgra
--

CREATE DATABASE prueba_tecnica_backend WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';


ALTER DATABASE prueba_tecnica_backend OWNER TO ametjimgra;

\connect prueba_tecnica_backend

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: medico; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.medico (
    id integer NOT NULL,
    nombre character varying(150),
    apellido character varying(150),
    email character varying(150),
    password character varying(150),
    token character varying(255)
);


ALTER TABLE public.medico OWNER TO postgres;

--
-- Name: medico_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.medico_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medico_id_seq OWNER TO postgres;

--
-- Name: medico_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.medico_id_seq OWNED BY public.medico.id;


--
-- Name: pacientes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pacientes (
    nombre character varying(150),
    id bigint,
    edad bigint,
    genero character varying(150),
    temperatura_corporal character varying(150),
    malestar character varying(150),
    fecha_ingreso date,
    eps character varying(150),
    tipo_documento character varying(150)
);


ALTER TABLE public.pacientes OWNER TO postgres;

--
-- Name: medico id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medico ALTER COLUMN id SET DEFAULT nextval('public.medico_id_seq'::regclass);


--
-- Data for Name: medico; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.medico (id, nombre, apellido, email, password, token) FROM stdin;
\.
COPY public.medico (id, nombre, apellido, email, password, token) FROM '$$PATH$$/3589.dat';

--
-- Data for Name: pacientes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pacientes (nombre, id, edad, genero, temperatura_corporal, malestar, fecha_ingreso, eps, tipo_documento) FROM stdin;
\.
COPY public.pacientes (nombre, id, edad, genero, temperatura_corporal, malestar, fecha_ingreso, eps, tipo_documento) FROM '$$PATH$$/3590.dat';

--
-- Name: medico_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.medico_id_seq', 2, true);


--
-- Name: medico medico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medico
    ADD CONSTRAINT medico_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         