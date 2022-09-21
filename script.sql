CREATE TABLE Produto (id CHAR (16),
                      fabricacao_timestamp DATE,
                      custo_unitario DOUBLE,
                      nome char (30),
                      altura DOUBLE.
                      comprimento DOUBLE.
                      largura DOUBLE,
                      massa DOUBLE,
                      codigo_barra char (30),
                      PRIMARY KEY (id, produto_id),
                      FOREIGN KEY (id_produto) REFERENCES
                      );

CREATE TABLE Pedido (id CHAR (16),
                      fabricacao_timestamp DATE,
                      custo_unitario DOUBLE,
                      nome char (30),
                      altura DOUBLE.
                      comprimento DOUBLE.
                      largura DOUBLE,
                      massa DOUBLE,
                      codigo_barra char (30),
                      PRIMARY KEY (id),
                      FOREIGN KEY (id_produto) REFERENCES
                      );
                      
CREATE TABLE Comprador (id CHAR (16));
 
CREATE TABLE Vendedor (id CHAR (16));

CREATE TABLE Usuario (cpf CHAR (11),
                      nome char (10),
                      sobrenome char (30),
                      email char (30),
                      telefone char (9),
                      PRIMARY KEY (cpf));

CREATE TABLE Endereco (id CHAR (16),
                      rua char (30),
                      numero INTEGER,
                      cep char (10),
                      bairro char (15),
                      complemento char (15),
                      PRIMARY KEY (id));

-- criar uma visão para calcular o volume

-- vendedores precisam ser pessoas físicas, com CPF

-- vendedor e comprador só devem ter um endereço
