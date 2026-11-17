use despesas_api;

-- drop table `devdespesas_api_api`.`carros`;

create table `despesas_api`.`despesas` (
	`oid_despesa` BIGINT not null AUTO_INCREMENT,
	`dat_vencimento_despesa` date not null ,
	`dat_despesa_pagamento` date,
	`des_despesa` VARCHAR(500) not null ,
	`tpo_despesa` VARCHAR(500) not null ,
	`vlr_despesa` decimal(12, 2) not null ,
	`vlr_despesa_pago` decimal(12, 2),
	`dat_criacao` DATETIME not null DEFAULT CURRENT_TIMESTAMP,
	`dat_alteracao` DATETIME null,
	primary key (`oid_despesa`)
)
-- engine = InnoDB
;