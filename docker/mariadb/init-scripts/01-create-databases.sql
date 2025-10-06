CREATE DATABASE IF NOT EXISTS botilleria_db;
USE botilleria_db;

CREATE TABLE grados_alcohol (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    horario_limite_venta VARCHAR(100) NOT NULL DEFAULT '09:00-22:00'
);

CREATE TABLE categorias (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    tipo_grado INT NOT NULL,
    restriction_edad BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (tipo_grado) REFERENCES grados_alcohol(id)
);

CREATE TABLE bebidas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    codigo VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    precio INT NOT NULL CHECK (precio > 0),
    stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0),
    categoria_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

-- Datos por defecto para grados de alcohol
INSERT INTO grados_alcohol (id, nombre, description, horario_limite_venta) VALUES
(1, 'ALTA_GRADUACION', 'Bebidas con más de 30° grados de alcohol', '09:00-22:00'),
(2, 'MEDIA_GRADUACION', 'Bebidas entre 15° y 30° grados de alcohol', '09:00-22:00'),
(3, 'BAJA_GRADUACION', 'Bebidas con menos de 15° grados de alcohol', '08:00-23:00'),
(4, 'SIN_ALCOHOL', 'Bebidas sin contenido alcohólico', 'SIN_LIMITE');

-- Datos por defecto para categorías
INSERT INTO categorias (id, nombre, tipo_grado, restriction_edad) VALUES
(1, 'PISCO', 1, TRUE),
(2, 'RON', 1, TRUE),
(3, 'WHISKY', 1, TRUE),
(4, 'VODKA', 1, TRUE),
(5, 'VINO', 2, TRUE),
(6, 'CHAMPAGNE', 2, TRUE),
(7, 'CERVEZA', 3, TRUE),
(8, 'COCTEL', 3, TRUE),
(9, 'ENERGIZANTE', 4, FALSE),
(10, 'REFRESCO', 4, FALSE);

-- Datos por defecto para bebidas
INSERT INTO bebidas (codigo, nombre, marca, precio, stock, categoria_id) VALUES
-- Piscos
('PIS-001', 'Pisco Alto del Carmen 35°', 'Alto del Carmen', 12500, 50, 1),
('PIS-002', 'Pisco Control Cero', 'Control', 8500, 30, 1),
('PIS-003', 'Pisco Mistral Gran Reserva', 'Mistral', 15000, 20, 1),

-- Rones
('RON-001', 'Ron Bacardí Añejo', 'Bacardí', 8900, 40, 2),
('RON-002', 'Ron Captain Morgan', 'Captain Morgan', 11200, 25, 2),
('RON-003', 'Ron Havana Club', 'Havana Club', 13500, 15, 2),

-- Whisky
('WHI-001', 'Whisky Johnnie Walker Red', 'Johnnie Walker', 12900, 35, 3),
('WHI-002', 'Whisky Jack Daniels', 'Jack Daniels', 18500, 18, 3),
('WHI-003', 'Whisky Chivas Regal 12', 'Chivas Regal', 24500, 12, 3),

-- Vodka
('VOD-001', 'Vodka Absolut', 'Absolut', 9500, 45, 4),
('VOD-002', 'Vodka Smirnoff', 'Smirnoff', 8200, 38, 4),

-- Vinos
('VIN-001', 'Vino Tinto Reserva', 'Casillero del Diablo', 7500, 60, 5),
('VIN-002', 'Vino Blanco Sauvignon', 'Concha y Toro', 6800, 55, 5),
('VIN-003', 'Vino Rosé Santa Rita', 'Santa Rita', 7200, 40, 5),

-- Cervezas
('CER-001', 'Cerveza Corona Botella', 'Corona', 2500, 100, 7),
('CER-002', 'Cerveza Heineken Lata', 'Heineken', 1800, 120, 7),
('CER-003', 'Cerveza Kunstmann Torobayo', 'Kunstmann', 3200, 80, 7),

-- Energizantes
('ENE-001', 'Red Bull Energy Drink', 'Red Bull', 1800, 150, 9),
('ENE-002', 'Monster Energy', 'Monster', 2200, 90, 9),

-- Refrescos
('REF-001', 'Coca-Cola 2L', 'Coca-Cola', 1800, 200, 10),
('REF-002', 'Sprite 2L', 'Sprite', 1600, 180, 10);

-- 5. Verificar que todo se creó correctamente
SHOW TABLES;
