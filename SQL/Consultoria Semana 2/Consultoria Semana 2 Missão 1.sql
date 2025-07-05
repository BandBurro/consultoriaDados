CREATE DATABASE produtosDB;

USE produtosDB;

CREATE TABLE Produtos (
    IDProduto INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Preco DECIMAL(10, 2) NOT NULL,
    Qntd INT NOT NULL,
    Tipo VARCHAR(50) NOT NULL,
    Localizacao VARCHAR(50) NOT NULL
);

INSERT INTO Produtos (Nome, Preco, Qntd, Tipo, Localizacao) VALUES
('Notebook Gamer', 5500.00, 10, 'Eletrônico', 'Porto Alegre'),
('Mouse Wireless', 150.00, 50, 'Periférico', 'São Paulo'),
('Teclado Mecânico', 350.00, 20, 'Periférico', 'Rio de Janeiro'),
('Monitor 24 Polegadas', 900.00, 15, 'Eletrônico', 'Curitiba'),
('Cadeira Gamer', 1200.00, 5, 'Móvel', 'Belo Horizonte'),
('Headset Bluetooth', 499.99, 30, 'Periférico', 'São Paulo'),
('SSD 1TB', 700.00, 8, 'Armazenamento', 'Florianópolis'),
('HD Externo 2TB', 550.00, 12, 'Armazenamento', 'Porto Alegre'),
('Placa de Vídeo RTX 4060', 2800.00, 4, 'Eletrônico', 'Curitiba'),
('Fonte 750W', 600.00, 6, 'Hardware', 'Belo Horizonte');

-- Consulta 1
SELECT * FROM Produtos
WHERE IDProduto = 1 OR IDProduto = 2;

-- Consulta 2
SELECT Nome, Preco, Qntd, ID FROM Produtos
WHERE Preco > 1199;

-- Consulta 3
SELECT Nome, Qntd, IDProduto
WHERE Qntd < 10;

-- Consulta 4
SELECT * FROM Produtos
WHERE Nome LIKE 'm%';

-- Consulta 5
SELECT Localizacao FROM Produtos
WHERE Localizacao LIKE '%o'