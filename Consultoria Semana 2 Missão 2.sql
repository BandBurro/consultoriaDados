-- Potencialmente redundante em PrecoUnitario e LocalVenda, normalizar posteriormente
CREATE TABLE Vendas (
    IDVenda INT PRIMARY KEY AUTO_INCREMENT,
    DataVenda DATE NOT NULL,
    IDProduto INT NOT NULL,
    QntdVnd INT NOT NULL,
    PrecoUnitario DECIMAL(10, 2) NOT NULL,
    LocalVenda VARCHAR(50) NOT NULL,
    FOREIGN KEY (IDProduto) REFERENCES Produtos(IDProduto)
);

INSERT INTO Vendas (DataVenda, IDProduto, QntdVnd, PrecoUnitario, LocalVenda) VALUES
('2024-06-01', 1, 2, 5500.00, 'Porto Alegre'),
('2024-06-02', 2, 5, 150.00, 'São Paulo'),
('2024-06-03', 3, 3, 350.00, 'Rio de Janeiro'),
('2024-06-04', 4, 1, 900.00, 'Curitiba'),
('2024-06-05', 5, 2, 1200.00, 'Belo Horizonte'),
('2024-06-06', 6, 4, 499.99, 'São Paulo'),
('2024-06-07', 7, 1, 700.00, 'Florianópolis'),
('2024-06-08', 8, 2, 550.00, 'Porto Alegre'),
('2024-06-09', 9, 1, 2800.00, 'Curitiba'),
('2024-06-10', 10, 2, 600.00, 'Belo Horizonte');

-- Consulta 1 + Alias
SELECT AVG(PrecoUnitario) AS MediaPreco FROM Vendas;

-- Consulta 2
SELECT COUNT(IDProduto) FROM Vendas;

-- Consulta 3
SELECT MIN(PrecoUnitario) FROM Vendas;

-- Consulta 4
SELECT MAX(PrecoUnitario) FROM Vendas;

-- Consulta 5
SELECT MAX(PrecoUnitario) FROM Vendas
WHERE LocalVenda = 'São Paulo';

-- Consulta 6
SELECT SUM(PrecoUnitario) FROM Vendas;