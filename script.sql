--  Criação do banco de dados (Altere se necessário)
CREATE DATABASE IF NOT EXISTS petshop_bd;
USE petshop_bd;

--  Tabela de Usuários para o funcionamento do Login no frontend React
CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    perfil VARCHAR(20) DEFAULT 'admin'
);

--  Inserindo um usuário padrão para você conseguir testar o login
INSERT INTO Usuario (nome, email, senha, perfil) 
VALUES ('Administrador', 'admin@petflow.com', '123456', 'admin');

--  Tabela de Clientes
CREATE TABLE Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(20)
);

--  Tabela de Pets (Depende de Cliente)
CREATE TABLE Pet (
    id_pet INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especie VARCHAR(50) NOT NULL,
    raca VARCHAR(50),
    peso FLOAT,
    idade INT,
    id_cliente INT NOT NULL,
    CONSTRAINT fk_pet_cliente FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente) ON DELETE CASCADE
);

--  Tabela de Produtos
CREATE TABLE Produto (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    preco DECIMAL(10,2) NOT NULL CHECK (preco >= 0),
    estoque INT NOT NULL DEFAULT 0 CHECK (estoque >= 0)
);

--  Tabela de Serviços
CREATE TABLE Servico (
    id_servico INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(100) NOT NULL,
    duracao INT, --  Duração em minutos
    preco DECIMAL(10,2) NOT NULL CHECK (preco >= 0)
);

--  Tabela de Agendamentos (Depende de Pet e Serviço)
CREATE TABLE Agendamento (
    id_agendamento INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    hora TIME NOT NULL,
    status VARCHAR(20) DEFAULT 'Pendente',
    id_pet INT NOT NULL,
    id_servico INT,
    CONSTRAINT fk_agend_pet FOREIGN KEY (id_pet) REFERENCES Pet(id_pet) ON DELETE CASCADE,
    CONSTRAINT fk_agend_servico FOREIGN KEY (id_servico) REFERENCES Servico(id_servico)
);

--  Tabela de Vendas (Depende de Cliente)
CREATE TABLE Venda (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,
    data_venda DATE NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    id_cliente INT NOT NULL,
    CONSTRAINT fk_venda_cliente FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

--  Tabela Associativa Itens_Venda (Depende de Venda, Produto, Servico e Pet)
CREATE TABLE Itens_Venda (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_venda INT NOT NULL,
    id_produto INT,
    id_servico INT,
    id_pet INT,
    quantidade INT NOT NULL DEFAULT 1 CHECK (quantidade > 0),
    preco_unitario DECIMAL(10,2) NOT NULL CHECK (preco_unitario >= 0),
    subtotal DECIMAL(10,2) NOT NULL CHECK (subtotal >= 0),
    CONSTRAINT fk_item_venda FOREIGN KEY (id_venda) REFERENCES Venda(id_venda) ON DELETE CASCADE,
    CONSTRAINT fk_item_produto FOREIGN KEY (id_produto) REFERENCES Produto(id_produto),
    CONSTRAINT fk_item_servico FOREIGN KEY (id_servico) REFERENCES Servico(id_servico),
    CONSTRAINT fk_item_pet FOREIGN KEY (id_pet) REFERENCES Pet(id_pet)
);