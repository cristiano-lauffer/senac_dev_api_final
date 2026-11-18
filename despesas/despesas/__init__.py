from django.db.backends.mysql.base import DatabaseWrapper
from django.db.backends.mysql.features import DatabaseFeatures

# Ignora a checagem de versão do banco
DatabaseWrapper.check_database_version_supported = lambda self: None

# Evita o erro de retorno de dados no INSERT (PUT/POST)
DatabaseFeatures.can_return_columns_from_insert = False