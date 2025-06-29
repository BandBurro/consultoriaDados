CREATE TABLE Clientes (
    CPFCliente VARCHAR(11) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100),
    Cidade VARCHAR(50),
    Telefone VARCHAR(20)
);

ALTER TABLE Vendas
ADD COLUMN CPFCliente VARCHAR(11),
ADD CONSTRAINT FK_Vendas_Clientes FOREIGN KEY (CPFCliente) REFERENCES Clientes(CPFCliente);

INSERT INTO Clientes (CPFCliente, Nome, Email, Cidade, Telefone) VALUES
('12345678901', 'Matheus Lino', 'matheus@example.com', 'Porto Alegre', '51999999999'),
('98765432100', 'Ana Souza', 'ana@example.com', 'São Paulo', '11988888888'),
('55544433322', 'Carlos Lima', 'carlos@example.com', 'Curitiba', '41977777777'),
('11122233344', 'Fernanda Alves', 'fernanda@example.com', 'Belo Horizonte', '31966666666'),
('99988877766', 'Roberto Silva', 'roberto@example.com', 'Florianópolis', '48955555555');

UPDATE Vendas SET CPFCliente = '12345678901' WHERE IDVenda = 1;
UPDATE Vendas SET CPFCliente = '98765432100' WHERE IDVenda = 2;
UPDATE Vendas SET CPFCliente = '55544433322' WHERE IDVenda = 3;
UPDATE Vendas SET CPFCliente = '11122233344' WHERE IDVenda = 4;
UPDATE Vendas SET CPFCliente = '99988877766' WHERE IDVenda = 5;
UPDATE Vendas SET CPFCliente = '98765432100' WHERE IDVenda = 6;
UPDATE Vendas SET CPFCliente = '55544433322' WHERE IDVenda = 7;
UPDATE Vendas SET CPFCliente = '12345678901' WHERE IDVenda = 8;
UPDATE Vendas SET CPFCliente = '11122233344' WHERE IDVenda = 9;
UPDATE Vendas SET CPFCliente = '99988877766' WHERE IDVenda = 10;

SELECT IDVenda, CPFCliente FROM Vendas;

-- Consulta 1 não consegui
SELECT QntdVnd AS QuantidadeVendida, COUNT(*) AS TotalDeVendas
FROM Vendas
GROUP BY QntdVnd;