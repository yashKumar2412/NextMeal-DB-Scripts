CREATE TABLE IF NOT EXISTS public.restaurant_images (
    photo_id character varying(255) COLLATE pg_catalog."default" NOT NULL,
    business_id character varying(255) COLLATE pg_catalog."default",
    caption text COLLATE pg_catalog."default",
    label character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT restaurant_images_pkey PRIMARY KEY (photo_id),
    CONSTRAINT restaurant_images_business_id_fkey FOREIGN KEY (business_id)
        REFERENCES public.restaurants (business_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);