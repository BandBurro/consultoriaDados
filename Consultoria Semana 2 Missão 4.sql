-- Já que já fiz alguns inserts e updates, farei a exclusão
INSERT INTO Produtos (Nome, Preco, Categoria) VALUES 
('Webcam Full HD', 250.00, 'Periférico');

INSERT INTO Estoque (Produto_ID, Quantidade, Data_Entrada) VALUES 
(6, 20, '2024-07-01');

UPDATE Produtos
SET Preco = 1350.00
WHERE ID = 5;

UPDATE Estoque
SET Quantidade = 30
WHERE ID = 3;

DELETE FROM Estoque
WHERE ID = 8;
