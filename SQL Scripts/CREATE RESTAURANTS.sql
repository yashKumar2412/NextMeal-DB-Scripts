CREATE TABLE IF NOT EXISTS public.restaurants (
    name character varying(255) COLLATE pg_catalog."default",
    address text COLLATE pg_catalog."default",
    city character varying(100) COLLATE pg_catalog."default",
    state character varying(100) COLLATE pg_catalog."default",
    postal_code character varying(20) COLLATE pg_catalog."default",
    latitude double precision,
    longitude double precision,
    average_rating numeric,
    review_count integer,
    is_open boolean,
    categories text[] COLLATE pg_catalog."default",
    menu text[] COLLATE pg_catalog."default",
    hours jsonb,
    attributes jsonb,
    business_id character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT restaurants_pkey PRIMARY KEY (business_id)
);