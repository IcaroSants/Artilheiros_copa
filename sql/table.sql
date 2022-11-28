CREATE database copa;

CREATE SEQUENCE IDJogador;
CREATE TABLE artilheiros_copa(
    id_jogador INT DEFAULT nextval('IDJogador'::regclass) PRIMARY KEY,
    nome VARCHAR(50),
    J int,
    G int,
    PEN int, 
    AG int, 
    MPG int, 
    GTIT int, 
    GSUP int,
    GPTS int,
    GVIT int,
    GRVV int,
    PGE int,
    data_rodada DATE
);

