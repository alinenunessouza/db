-- Relational Algebra in DBMS

/* Populate the database:
group: Exercicio 1 


Fornecedores={
	id_forn:number, nome_forn:string, endereco:string
	1, f1, 'rua a'
	2, f2, 'rua b'
	3, f3, 'Av. Packer, 221'
}

Pecas = {
	id_peca:number, nome_peca:string, cor:string
	1, p1, vermelha
	2, p2, azul
	3, p3, verde
	4, p4, amarela
}

Catalogo = {
	id_forn:number, id_peca:number, custo:number
	1, 1, 1
	1, 2, 1.5
	2, 1, 1
	2, 2, 2
	2, 3, 2
	2, 4, 5
	3, 2, 2
	3, 3, 2
}
*/

-- a) Encontre os nomes dos fornecedores que fornecem alguma peça vermelha.
-- π nome_forn (((σ cor='vermelha' or cor='verde' Pecas)⨝Catalogo)⨝Fornecedores)

SELECT nome_forn
FROM SELECT * FROM Pecas WHERE cor = 'vermelha') as pecas
JOIN Catalogo on Catalogo.id_peca = pecas.id_peca
JOIN Fornecedores on Fornecedores.id_forn = Catalogo.id_forn;

-- b) Encontre os id-forns dos fornecedores que fornecem alguma peça vermelha ou verde.
-- π id_forn (((σ cor='vermelha' ∨ cor='verde' Pecas)⨝Catalogo))

SELECT nome_forn
FROM (SELECT * FROM Pecas WHERE cor = 'vermelha' or cor = 'verde') as pecas
JOIN Catalogo on Catalogo.id_peca = pecas.id_peca
JOIN Fornecedores on Fornecedores.id_forn = Catalogo.id_forn;

-- c) Encontre os id-forns dos fornecedores que fornecem alguma peça vermelha ou que estão no endereço Av. Packer,221.
-- π id_forn ((((σ cor='verde' Pecas)∪(σ endereco='Av. Packer,221.' Fornecedores))⨝Catalogo))

SELECT f.id_forn
FROM (SELECT * FROM Fornecedores WHERE endereco = 'Av. Packer, 221') as f
JOIN Catalogo on f.id_forn = Catalogo.id_forn
UNION
SELECT Catalogo.id_forn
FROM (select * from Pecas where cor = 'verde') as p
JOIN Catalogo on p.id_peca = Catalogo.id_peca;

-- d) Encontre os id-forns dos fornecedores que fornecem todas as peças.
-- ((π id_forn, id_peca Catalogo) ÷ π id_peca Pecas)

-- e) Encontre os id-forns dos fornecedores que fornecem todas as peças vermelhas
-- 

-- f) Encontre os id-forns dos fornecedores que fornecem todas as peças vermelhas ou verdes.

-- g) Encontre os id-forns dos fornecedores que fornecem todas as peças vermelhas ou fornecem todas as peças verdes.
-- r: 1, 2, 3
-- ((π id_forn, id_peca Catalogo)÷(π id_peca σ cor='vermelha' Pecas)) ∪ ((π id_forn, id_peca Catalogo) ÷ (π id_peca σ cor='verde' Pecas))

-- h) Encontre os pares de id-forns tais que o fornecedor com o primeiro id-forn cobre mais por alguma peça do que o fornecedor com o segundo id-forn
-- utilizar produto cartesiano
σ id_forn1 ≠ id_forn2 
π id_forn1,id_forn2 
(σ custo1>custo2 (
(ρ custo1←custo,id_forn1←id_forn (π custo,id_forn (Fornecedores ⨝ Catalogo)))
⨯
(ρ custo2←custo,id_forn2←id_forn (π custo,id_forn (Fornecedores ⨝ Catalogo)))
))

-- i) Encontre os id-peças das peças fornecidas por pelo menos dois fornecedores diferentes.

-- j) Encontre os id-peças das peças mais caras fornecidas pelo fornecedor chamado Yosemite Sham

-- k) Encontre os id-peças das peças fornecidas por todos os fornecedores por menos de 200 dólares (Se algum fornecedor não fornece a peça ou cobra mais do que 200 dólares por ela, a peça não é selecionada)

