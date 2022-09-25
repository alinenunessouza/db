CREATE TABLE Produto (id uuid default uuid_generate_v4(),
                      fabricacao_timestamp DATE,
                      custo_unitario DOUBLE,
                      nome char (30),
                      altura DOUBLE.
                      comprimento DOUBLE.
                      largura DOUBLE,
                      massa DOUBLE,
                      codigo_barra char (30),
                      PRIMARY KEY (id)
                      );
                     
create table Vendido(id uuid default uuid_generate_v4(),
                      
                      PRIMARY KEY (id)
                      );               
 
                      
CREATE TABLE Pedido (id uuid default uuid_generate_v4(),
                     timestamp DATE,
                     PRIMARY KEY (id),
                     FOREIGN KEY (id_comprador) references Comprador(id),
                     FOREIGN KEY (id_vendedor) references Vendedor(id)
                    );
                    
                    
                   

CREATE TABLE Comprador (id uuid default uuid_generate_v4(),
                       cartao char (16));
 
CREATE TABLE Vendedor (id uuid default uuid_generate_v4(),
                      registro);

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

-- criar uma visão para calcular o volume

-- vendedores precisam ser pessoas físicas, com CPF

-- vendedor e comprador só devem ter um endereço
