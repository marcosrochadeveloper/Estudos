use cadastro;

select * from gafanhotos;

#EX001 (UMA LISTA COM O NOME DE TODAS AS GAFANHOTAS)
select nome from gafanhotos where sexo = 'F';

#EX002 (UMA LISTA COM OS DADOS DE TODOS AQUELES QUE NASCERAM ENTRE 01/JAN/2000 E 31/DEZ/2015)
select * from gafanhotos where nascimento >= '2000/01/01' and nascimento <= '2015/12/31';

#EX003 (UMA LISTA COM O NOME DE TODOS OS HOMENS QUE TRABALHAM COMO PROGRAMADORES)
select nome from gafanhotos where sexo = 'M' and profissao = 'Programador';

#EX004 (UMA LISTA COM TODOS OS DADOS DE TODAS AS MULHERES QUE NASCERAM NO BRASIL E QUE TÊM SEU NOME INICIANDO COM A LETRA J)
select * from gafanhotos where sexo = 'F' and nacionalidade = 'Brasil' and nome like 'J%';

#EX005 (UMA LISTA COM O NOME E NACIONALIDADE DE TODOS OS HOMENS QUE TÊM SILVA NO NOME, NÃO NASCERAM NO BRASIL E PESAM MENOS DE 100 KG)
select nome, nacionalidade from gafanhotos where sexo = 'M' and nome like '%SILVA%' and nacionalidade != 'BRASIL' and peso < 100;

#EX006 (QUAL É A MAIOR ALTURA ENTRE GAFANHOTOS HOMENS QUE MORAM NO BRASIL?)
select max(altura) from gafanhotos where sexo = 'M' and nacionalidade = 'Brasil';

#EX007 (QUAL É A MÉDIA DE PESO DOS GAFANHOTOS CADASTRADOS?)
select avg(peso) from gafanhotos;

#EX008 (QUAL É O MENOR PESO ENTRE AS GAFANHOTOS MULHERES QUE NASCERAM FORA DO BRASIL E ENTRE 01//JAN/1990 E 31/DEZ/2000?)
select min(peso) from gafanhotos where sexo = 'F' and nacionalidade != 'Brasil' and nascimento >= '1990/01/01' and nascimento <= '2000/12/31';

#EX009 (QUANTAS GAFANHOTOS MULHERES TÊM MAIS DE 1.90M DE ALTURA?)
select count(*) from gafanhotos where sexo = 'F' and altura > '1.90';

select distinct(group_concat(profissao)) from gafanhotos;