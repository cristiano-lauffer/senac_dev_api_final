use despesas_api;


INSERT INTO despesas_api.despesas(
	dat_vencimento_despesa,
	dat_despesa_pagamento,
	des_despesa,
	tpo_despesa,
	vlr_despesa,
	vlr_despesa_pago
)VALUES(
	'2026-10-23',
	NULL,
	'Condomínio para o mês de 2026/09',
	'CONDOMÍNIO',
	500.23,
	NULL
);

INSERT INTO despesas_api.despesas(
	dat_vencimento_despesa,
	dat_despesa_pagamento,
	des_despesa,
	tpo_despesa,
	vlr_despesa,
	vlr_despesa_pago
)VALUES(
	'2026-10-11',
	NULL,
	'CEEE para o mês de 2026/09',
	'LUZ',
	201.54,
	NULL
);

INSERT INTO despesas_api.despesas(
	dat_vencimento_despesa,
	dat_despesa_pagamento,
	des_despesa,
	tpo_despesa,
	vlr_despesa,
	vlr_despesa_pago
)VALUES(
	'2026-10-08',
	'2026-10-07',
	'Cartão NuBank para o mês de 2026/09',
	'NUBANK',
	1301.29,
	1301.29
);

INSERT INTO despesas_api.despesas(
	dat_vencimento_despesa,
	dat_despesa_pagamento,
	des_despesa,
	tpo_despesa,
	vlr_despesa,
	vlr_despesa_pago
)VALUES(
	'2026-10-08',
	'2026-10-23',
	'Cartão Bradesco para o mês de 2026/09',
	'BRADESCO',
	301.31,
	201.29
);