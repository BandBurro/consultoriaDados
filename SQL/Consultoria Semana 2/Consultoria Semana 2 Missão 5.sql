CREATE DATABASE estoquedb;

USE estoquedb;

CREATE TABLE Produtos (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100) NOT NULL,
    Preco DECIMAL(10, 2) NOT NULL,
    Categoria VARCHAR(50) NOT NULL
);

CREATE TABLE Estoque (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Produto_ID INT NOT NULL,
    Quantidade INT NOT NULL,
    Data_Entrada DATE NOT NULL,
    FOREIGN KEY (Produto_ID) REFERENCES Produtos(ID)
);

INSERT INTO Produtos (Nome, Preco, Categoria) VALUES
('Notebook Gamer', 5500.00, 'Eletrônico'),
('Mouse Wireless', 150.00, 'Periférico'),
('Teclado Mecânico', 350.00, 'Periférico'),
('Monitor 24 Polegadas', 900.00, 'Eletrônico'),
('Cadeira Gamer', 1200.00, 'Móvel');

INSERT INTO Estoque (Produto_ID, Quantidade, Data_Entrada) VALUES
(1, 10, '2024-06-01'),
(2, 50, '2024-06-02'),
(3, 20, '2024-06-03'),
(4, 15, '2024-06-04'),
(5, 5,  '2024-06-05'),
(2, 30, '2024-07-01'),
(3, 10, '2024-07-01'),
(1, 5,  '2024-07-05');

-- Consulta 1
SELECT Categoria, SUM(Quantidade) AS Unidades FROM Produtos, Estoque
WHERE Produtos.ID = Estoque.Produto_ID
GROUP BY Categoria;

-- Consulta 2
SELECT AVG(Preco) FROM Produtos;

-- Consulta 3
SELECT Nome, SUM(Quantidade) AS Unidades FROM Produtos, Estoque
WHERE Produtos.ID = Estoque.Produto_ID
GROUP BY Nome
HAVING SUM(Quantidade) < 10;

-- Consulta 4
UPDATE Estoque
SET Quantidade = 10
WHERE Produto_ID = 2 AND Data_Entrada = '2024-07-01';

DELETE FROM Estoque WHERE Produto_ID = 1 AND Quantidade = '10';

INSERT INTO Estoque VALUES (1, 10, '2024-06-01');
