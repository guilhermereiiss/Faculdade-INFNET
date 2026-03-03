
-- TP5 - PyMusic Scraper (Schema dedicado)

-- Criar schema dedicado
CREATE SCHEMA IF NOT EXISTS tp5;

-- Tabela principal: álbuns (equivalente aos books do PyBooks)
CREATE TABLE tp5.albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist VARCHAR(200) NOT NULL,       
    release_year INTEGER,
    genre VARCHAR(100),
    description TEXT,
    wikipedia_url TEXT UNIQUE,          
    added_at TIMESTAMP DEFAULT NOW(),
    scraped_success BOOLEAN DEFAULT FALSE
);

-- Tabela de metadados das páginas raspadas
CREATE TABLE tp5.scraped_pages (
    id SERIAL PRIMARY KEY,
    url TEXT NOT NULL UNIQUE,
    page_title VARCHAR(255),
    scraped_at TIMESTAMP DEFAULT NOW(),
    status_code INTEGER,
    success BOOLEAN DEFAULT FALSE,
    error_message TEXT
);

-- Tabela de erros detalhados (exigência do professor)
CREATE TABLE tp5.scraping_errors (
    id SERIAL PRIMARY KEY,
    page_id INTEGER REFERENCES tp5.scraped_pages(id) ON DELETE CASCADE,
    error_type VARCHAR(100),
    error_detail TEXT,
    occurred_at TIMESTAMP DEFAULT NOW()
);

-- Tabela de artistas (para futuro relacionamento)
CREATE TABLE tp5.artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) UNIQUE NOT NULL,
    country VARCHAR(100),
    active_years VARCHAR(50)
);

-- Relacionamento muitos-para-muitos: álbum ↔ artista(s)
CREATE TABLE tp5.album_artists (
    album_id INTEGER REFERENCES tp5.albums(id) ON DELETE CASCADE,
    artist_id INTEGER REFERENCES tp5.artists(id) ON DELETE CASCADE,
    PRIMARY KEY (album_id, artist_id)
);

-- Índices para performance
CREATE INDEX IF NOT EXISTS idx_albums_title ON tp5.albums(title);
CREATE INDEX IF NOT EXISTS idx_scraped_url ON tp5.scraped_pages(url);