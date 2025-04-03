-- CREATE TABLE `cidades` (
--   `id` integer PRIMARY KEY AUTO_INCREMENT,
--   `nome` varchar(80),
--   `uf` char(2),
--   `ativo` bool
-- );

-- CREATE TABLE `agencias` (
--   `id` integer PRIMARY KEY AUTO_INCREMENT,
--   `nome` varchar(80),
--   `id_cidade` int,
--   `ativo` bool
-- );

-- CREATE TABLE `clientes` (
--   `id` integer PRIMARY KEY AUTO_INCREMENT,
--   `nome` varchar(150),
--   `endereco` varchar(150),
--   `ativo` bool
-- );

-- CREATE TABLE `tiposContas` (
--   `id` integer PRIMARY KEY AUTO_INCREMENT,
--   `descricao` varchar(150),
--   `taxaJuros` float,
--   `ativo` bool
-- );

-- CREATE TABLE `contasClientes` (
--   `id` integer PRIMARY KEY AUTO_INCREMENT,
--   `id_agencia` int,
--   `id_tipoConta` int,
--   `id_cliente` int,
--   `saldo` float,
--   `dataUltimoAcesso` date,
--   `ativo` bool
-- );

-- CREATE TABLE `naturezasMovimentacao` (
--   `id` integer PRIMARY KEY AUTO_INCREMENT,
--   `descricao` varchar(150),
--   `valor` int,
--   `ativo` bool
-- );

-- CREATE TABLE `movimentacoesContas` (
--   `id` integer PRIMARY KEY AUTO_INCREMENT,
--   `id_contaCliente` int,
--   `id_natureza` int,
--   `valor` float
-- );

-- ALTER TABLE `agencias` ADD FOREIGN KEY (`id_cidade`) REFERENCES `cidades` (`id`);

-- ALTER TABLE `contasClientes` ADD FOREIGN KEY (`id_agencia`) REFERENCES `agencias` (`id`);

-- ALTER TABLE `contasClientes` ADD FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id`);

-- ALTER TABLE `contasClientes` ADD FOREIGN KEY (`id_tipoConta`) REFERENCES `tiposContas` (`id`);

-- ALTER TABLE `movimentacoesContas` ADD FOREIGN KEY (`id_contaCliente`) REFERENCES `contasClientes` (`id`);

-- ALTER TABLE `movimentacoesContas` ADD FOREIGN KEY (`id_natureza`) REFERENCES `naturezasMovimentacao` (`id`);



--------------------------------------------------------------------------------------------------------------

-- INICIO SCRIPT SQLLITE3

CREATE TABLE cidades (
    id    INTEGER   PRIMARY KEY AUTOINCREMENT,
    nome  TEXT (80),
    uf    TEXT (2),
    ativo INTEGER
);

CREATE TABLE agencias (
  id integer PRIMARY KEY AUTOINCREMENT,
  nome varchar(80),
  id_cidade int,
  ativo INTEGER
);

CREATE TABLE clientes (
  id integer PRIMARY KEY AUTOINCREMENT,
  nome varchar(150),
  endereco varchar(150),
  ativo bool
);



CREATE TABLE tiposContas (
  id integer PRIMARY KEY AUTOINCREMENT,
  descricao varchar(150),
  taxaJuros float,
  ativo INTEGER
);

CREATE TABLE contasClientes (
  id integer PRIMARY KEY AUTOINCREMENT,
  id_agencia int,
  id_tipoConta int,
  id_cliente int,
  saldo float,
  dataUltimoAcesso date,
  ativo INTEGER
);

CREATE TABLE naturezasMovimentacao (
  id integer PRIMARY KEY AUTOINCREMENT,
  descricao varchar(150),
  valor int,
  ativo INTEGER
);

CREATE TABLE movimentacoesContas (
  id integer PRIMARY KEY AUTOINCREMENT,
  id_contaCliente int,
  id_natureza int,
  valor float
);
