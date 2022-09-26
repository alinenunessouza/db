-- PostgreSQL 9.6

-- Definições:
-- - vendedores precisam ser pessoas físicas, com CPF
-- - vendedor e comprador podem ter mais de um endereço
-- - pode ocorrer um cenário em que o vendedor e o comprador são o mesmo usuário

CREATE TABLE Produto (id uuid default uuid_generate_v4(),
                      fabricacao_timestamp DATE,
                      custo_unitario DECIMAL,
                      nome char (50),
                      altura DECIMAL,
                      comprimento DECIMAL,
                      largura DECIMAL,
                      massa DECIMAL,
                      codigo_barra char (30),
                      estoque INTEGER,
                      PRIMARY KEY (id)
                      );
                                           
CREATE TABLE Vendido (id uuid default uuid_generate_v4(),
					 quantidade INTEGER,
                     PRIMARY KEY (id)
                     );      
                     
CREATE TABLE Comprador (id uuid default uuid_generate_v4(),
                        cartao char (16),
                        cpf_usuario char (11),
                        FOREIGN KEY (cpf_usuario) references Usuario(cpf),
                        PRIMARY KEY (id)
                        );
 
CREATE TABLE Vendedor (id uuid default uuid_generate_v4(),
                       registro char (20),
                       cpf_usuario char (11),
                       PRIMARY KEY (id),
	                   FOREIGN KEY (cpf_usuario) references Usuario(cpf)
                      );
 
-- ao excluir um Pedido, todos os itens relacionados a esta venda devem ser excluídos da tabela de vendas
-- ao mesmo tempo, deve ser possível excluir um item de uma venda 
CREATE TABLE Pedido (id uuid default uuid_generate_v4(),
                     timestamp DATE,
                     PRIMARY KEY (id),
                     id_comprador uuid REFERENCES Comprador (id),
                     id_vendedor uuid REFERENCES Vendedor (id)
                     ON DELETE CASCADE);

CREATE TABLE Usuario (cpf CHAR (11),
                      nome char (10),
                      sobrenome char (30),
                      email char (30),
                      telefone char (9),
                      PRIMARY KEY (cpf));

CREATE TABLE Endereco (id uuid default uuid_generate_v4(),
                      rua char (30),
                      numero INTEGER,
                      cep char (10),
                      bairro char (15),
                      complemento char (15),
                      PRIMARY KEY (id));

-- criação de view para calcular o volume do produto
CREATE VIEW VolumeProduto (id, nome, volume) AS
SELECT p.id as id_produto, p.nome as nome, (p.comprimento * p.largura * p.altura) as volume 
FROM Produto p;

-- criação de uma visão para apresentar as vendas de um vendedor em um determinado mês, a quantidade de itens vendidos e o valor total das suas vendas

-- criação de visão para apresentar todos os dados de uma venda específica, o valor total desta venda, o nome do comprador e do vendedor

-- criação de visão para apresentar o estoque disponível, listando a quantidade de cada item
CREATE VIEW EstoqueAtual (id, quantidade) AS
SELECT p.id, pe.cnt
  FROM Produto p
       INNER JOIN (SELECT x, count(x) as cnt
                     FROM Pedido 
                    GROUP BY age) C ON p.id = pe.id;
-- COUNT das ocorrencias na tabela de pedidos

-- testes para validar o atendimento dos requisitos apresentados:

-- criando usuários
INSERT INTO Usuario (cpf, nome, sobrenome, email, telefone) VALUES ('72381889450', 'Chuck', 'Jones', 'chuckjones@gmail.com', '995458256');
INSERT INTO Usuario (cpf, nome, sobrenome, email, telefone) VALUES ('14748783184', 'Michael', 'Maltese', 'michaelmaltese@gmail.com', '997473721');
INSERT INTO Usuario (cpf, nome, sobrenome, email, telefone) VALUES ('22554696772', 'Geococcyx', 'Californianus', 'corredor@gmail.com', '997471220');
INSERT INTO Usuario (cpf, nome, sobrenome, email, telefone) VALUES ('79233761665', 'Canis', 'Latrans', 'azarado123@hotmail.com', '998123868');
INSERT INTO Usuario (cpf, nome, sobrenome, email, telefone) VALUES ('73381889450', 'Papa', 'Leguas', 'chuckjones@gmail.com', '995458256');

-- criando produtos
INSERT INTO Produto (fabricacao_timestamp, custo_unitario, nome, altura, comprimento, largura, massa, codigo_barra, estoque) VALUES (TO_TIMESTAMP('2022-02-09 07:00:00', 'YYYY-MM-DD HH24:MI:SS'), 49.90, 'CAMISETA EM MEIA MALHA COM ESTAMPA DO PAPA LÉGUAS', 34, 94, 20, 0.1, 606063065, 10);
INSERT INTO Produto (fabricacao_timestamp, custo_unitario, nome, altura, comprimento, largura, massa, codigo_barra, estoque) VALUES (TO_TIMESTAMP('2021-03-25 08:40:10', 'YYYY-MM-DD HH24:MI:SS'), 51.90, 'Mini Estátua Colecionável Papa-Léguas Road Runner', 8, 6, 4, 0.3, 90901872, 5);
INSERT INTO Produto (fabricacao_timestamp, custo_unitario, nome, altura, comprimento, largura, massa, codigo_barra, estoque) VALUES (TO_TIMESTAMP('2022-06-25 10:00:00', 'YYYY-MM-DD HH24:MI:SS'), 4149.00, 'Geladeira Panasonic Frost Free 483L A+++', 155, 65, 60, 73, 8980907523, 40);

-- criando endereços
INSERT INTO Endereco (rua, numero, cep, bairro, complemento) VALUES ('Av. Unisinos', 950, 93022750, 'Cristo Rei', 'Universidade');
INSERT INTO Endereco (rua, numero, cep, bairro, complemento) VALUES ('Av. Dr. Nilo Peçanha', 1600, 91330002, 'Boa Vista', 'Campus POA');
INSERT INTO Endereco (rua, numero, cep, bairro, complemento) VALUES ('R. Vinte e Quatro de Maio', 741, 93315125, 'Vila Rosa', 'Padaria');
INSERT INTO Endereco (rua, numero, cep, bairro, complemento) VALUES ('R. Guia Lopes', 4638, 93410324, 'Boa Vista', 'Loja 1');
