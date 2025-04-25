//Questão 1
// LETRA A
MATCH (n)
RETURN n;

//LETRA B
MATCH (g:Game)
WHERE g.ano > 2012
RETURN g;

// LETRA C
MATCH (g:Game)
WHERE g.genero = 'Terror'
RETURN g;

//LETRA D
MATCH (j:Jurado)-[r:JOGOU]->(g:Game)
WHERE r.nota >= 7
RETURN g, r.nota, j.nome;


//Questão 2

CREATE(:Game {titulo:'Mortal Kombat 1', genero:'Luta', ano:2023});
CREATE(:Game {titulo:'Overwatched', genero:'Shooter', ano:2016});
CREATE(:Game {titulo:'Forza Horizon', genero:'Corrida', ano:2012});
CREATE(:Game {titulo:'Resident Evil 4 Remake', genero:'Terror', ano:2023});


CREATE(:Jurado {nome:'Carrillo'});
CREATE(:Jurado {nome:'Garro'});
CREATE(:Jurado {nome:'Hugo'});

MATCH (j:Jurado {nome:'Carrillo'}), (g:Game {titulo:'Mortal Kombat 1'})
CREATE (j)-[:JOGOU {nota:8, horas:120}]->(g);

MATCH (j:Jurado {nome:'Carrillo'}), (g:Game {titulo:'Resident Evil 4 Remake'})
CREATE (j)-[:JOGOU {nota:9, horas:45}]->(g);


MATCH (j:Jurado {nome:'Garro'}), (g:Game {titulo:'Overwatched'})
CREATE (j)-[:JOGOU {nota:7, horas:300}]->(g);

MATCH (j:Jurado {nome:'Garro'}), (g:Game {titulo:'Forza Horizon'})
CREATE (j)-[:JOGOU {nota:8, horas:150}]->(g);


MATCH (j:Jurado {nome:'Hugo'}), (g:Game {titulo:'Mortal Kombat 1'})
CREATE (j)-[:JOGOU {nota:6, horas:50}]->(g);

MATCH (j:Jurado {nome:'Hugo'}), (g:Game {titulo:'Overwatched'})
CREATE (j)-[:JOGOU {nota:9, horas:600}]->(g);


MATCH (j:Jurado {nome:'Gabriel'}), (g:Game {titulo:'Overwatched'})
CREATE (j)-[:JOGOU {nota:10, horas:10000}]->(g);

MATCH (j:Jurado {nome:'Davi'}), (g:Game {titulo:'Mortal Kombat 1'})
CREATE (j)-[:JOGOU {nota:9, horas:680}]->(g);

MATCH (j:Jurado {nome:'Davi'}), (g:Game {titulo:'Forza Horizon'})
CREATE (j)-[:JOGOU {nota:10, horas:477}]->(g);

MATCH (j:Jurado {nome:'Davi'}), (g:Game {titulo:'Warzone'})
CREATE (j)-[:JOGOU {nota:8, horas:1344}]->(g);


MATCH (j:Jurado {nome:'Ewel'}), (g:Game {titulo:'Resident Evil 4 Remake'})
CREATE (j)-[:JOGOU {nota:7, horas:20}]->(g);

MATCH (j:Jurado {nome:'Ewel'}), (g:Game {titulo:'Overwatched'})
CREATE (j)-[:JOGOU {nota:8, horas:400}]->(g);