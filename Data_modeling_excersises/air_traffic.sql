-- from the terminal run:
-- psql < air_traffic.sql

DROP DATABASE IF EXISTS air_traffic;

CREATE DATABASE air_traffic;

\c air_traffic

CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    seat TEXT NOT NULL,
    departure TIMESTAMPTZ NOT NULL,
    arrival TIMESTAMPTZ NOT NULL,
    airline TEXT NOT NULL,
    from_city_id INT NOT NULL,
    to_city_id INT NOT NULL
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name TEXT NOT NULL
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name TEXT NOT NULL
);

-- Insert city data
INSERT INTO cities (city_name) VALUES
    ('Washington DC'), ('Seattle'), ('Tokyo'), ('London'), ('Los Angeles'), ('Las Vegas'),
    ('Mexico City'), ('Paris'), ('Casablanca'), ('Dubai'), ('Beijing'), ('New York'),
    ('Charlotte'), ('Cedar Rapids'), ('Chicago'), ('New Orleans'), ('Sao Paolo'), ('Santiago');

-- Insert country data
INSERT INTO countries (country_name) VALUES
    ('United States'), ('Japan'), ('United Kingdom'), ('France'), ('Morocco'), ('UAE'),
    ('China'), ('Brazil'), ('Chile');

ALTER TABLE tickets
    ADD CONSTRAINT fk_from_city FOREIGN KEY (from_city_id) REFERENCES cities (id),
    ADD CONSTRAINT fk_to_city FOREIGN KEY (to_city_id) REFERENCES cities (id);
