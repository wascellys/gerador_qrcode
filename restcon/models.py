# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from datetime import datetime
#
from django.db import models
#
#
# class Acao(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     codigo = models.CharField(max_length=255, blank=True, null=True)
#     descricao = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'acao'
#
#
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class Bairro(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     nome = models.CharField(max_length=255, blank=True, null=True)
#     taxa_entrega = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     cidade = models.ForeignKey('Cidade', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bairro'
#
#
# class Caixa(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     data_abertura = models.DateTimeField(blank=True, null=True)
#     data_fechamento = models.DateTimeField(blank=True, null=True)
#     numero = models.IntegerField(blank=True, null=True)
#     valor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'caixa'
#
#     def __str__(self):
#         return str(self.numero) + ' - ' + str(self.valor)
#
# class Cargo(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     descricao = models.CharField(max_length=255, blank=True, null=True)
#     entrega = models.BooleanField()
#
#     class Meta:
#         managed = False
#         db_table = 'cargo'
#
#
# class Cartao(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     bandeira = models.CharField(max_length=255, blank=True, null=True)
#     forma_pagamento = models.ForeignKey('FormaPagamento', models.DO_NOTHING, db_column='forma_pagamento', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'cartao'
#
#
# class Categoria(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     descricao = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'categoria'
#
#
# class Cidade(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     nome = models.CharField(max_length=255, blank=True, null=True)
#     estado = models.ForeignKey('Estado', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'cidade'
#
#
# class Cliente(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     cpf = models.CharField(max_length=255, blank=True, null=True)
#     nome = models.CharField(max_length=255, blank=True, null=True)
#     telefone = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'cliente'
#
#
# class Comanda(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     aberta = models.BooleanField()
#     data_hora_abertura = models.DateTimeField(blank=True, null=True)
#     data_hora_fechamento = models.DateTimeField(blank=True, null=True)
#     descricao = models.CharField(max_length=255, blank=True, null=True)
#     numero = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'comanda'
#
#
# class Configuracao(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     copia_local = models.BooleanField(blank=True, null=True)
#     copia_remota = models.BooleanField(blank=True, null=True)
#     imprime_fichas = models.BooleanField(blank=True, null=True)
#     local_copia = models.CharField(max_length=255, blank=True, null=True)
#     imprime_cancelamento = models.BooleanField(blank=True, null=True)
#     imprime_comp_pagamento = models.BooleanField(blank=True, null=True)
#     imprime_produtos_caixa = models.BooleanField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'configuracao'
#
#
# class Conta(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     aberta = models.BooleanField(default=True)
#     data_hora_abertura = models.DateTimeField(blank=True, null=True)
#     data_hora_fechamento = models.DateTimeField(blank=True, null=True)
#     delivery = models.BooleanField(blank=True, null=True)
#     entrega = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     observacao = models.CharField(max_length=255, blank=True, null=True)
#     troco = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     caixa = models.ForeignKey(Caixa, models.DO_NOTHING, blank=True, null=True)
#     cliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
#     comanda = models.ForeignKey(Comanda, models.DO_NOTHING, blank=True, null=True)
#     endereco = models.ForeignKey('Endereco', models.DO_NOTHING, blank=True, null=True)
#     mesa = models.ForeignKey('Mesa', models.DO_NOTHING, blank=True, null=True)
#     responsavel = models.ForeignKey('Funcionario', models.DO_NOTHING, blank=True, null=True)
#     acrescimo = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     desconto = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     motivo_cancelamento = models.CharField(max_length=255, blank=True, null=True)
#     percentual_acrescimo = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     percentual_desconto = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     status_entrega = models.CharField(max_length=255, blank=True, null=True)
#     forma_pagamento = models.ForeignKey('FormaPagamento', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'conta'
#
#     def get_taxa_conta(self):
#         if TaxaConta.objects.filter(conta=self):
#             taxa = TaxaConta.objects.get(conta=self)
#             return taxa.taxa.valor
#
#     def __str__(self):
#         return str(self.mesa) + ' - ' + str(self.ativo)
#
#
# class ControleVersao(models.Model):
#     migration = models.CharField(primary_key=True, max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'controle_versao'
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class Endereco(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     cep = models.CharField(max_length=255, blank=True, null=True)
#     complemento = models.CharField(max_length=255, blank=True, null=True)
#     numero = models.CharField(max_length=255, blank=True, null=True)
#     principal = models.BooleanField()
#     referencia = models.CharField(max_length=255, blank=True, null=True)
#     rua = models.CharField(max_length=255, blank=True, null=True)
#     bairro = models.ForeignKey(Bairro, models.DO_NOTHING, blank=True, null=True)
#     cidade = models.ForeignKey(Cidade, models.DO_NOTHING, blank=True, null=True)
#     cliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
#     estado = models.ForeignKey('Estado', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'endereco'
#
#
# class Estabelecimento(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     cnpj = models.CharField(max_length=255, blank=True, null=True)
#     email = models.CharField(max_length=255, blank=True, null=True)
#     nome = models.CharField(max_length=255, blank=True, null=True)
#     telefone = models.CharField(max_length=255, blank=True, null=True)
#     endereco = models.ForeignKey(Endereco, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'estabelecimento'
#
#
# class Estado(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     nome = models.CharField(max_length=255, blank=True, null=True)
#     sigla = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'estado'
#
#
# class Estoque(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     quantidade = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     produto = models.ForeignKey('Produto', models.DO_NOTHING, blank=True, null=True)
#     setor = models.ForeignKey('Setor', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'estoque'
#
#
# class FormaPagamento(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     descricao = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'forma_pagamento'
#
#
# class Fornecedor(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     celular = models.CharField(max_length=255, blank=True, null=True)
#     cnpj = models.CharField(max_length=255, blank=True, null=True)
#     email = models.CharField(max_length=255, blank=True, null=True)
#     endereco = models.CharField(max_length=255, blank=True, null=True)
#     nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
#     razao_social = models.CharField(max_length=255, blank=True, null=True)
#     telefone = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'fornecedor'
#
#
# class Fracionamento(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     parte = models.ForeignKey('ProdutoTamanho', models.DO_NOTHING, blank=True, null=True)
#     produto = models.ForeignKey('Produto', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'fracionamento'
#
#
#     def __str__(self):
#         return str(self.produto) + ' - ' + str(self.parte)
#
#
# class Funcionario(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     cpf = models.CharField(max_length=255, blank=True, null=True)
#     login = models.CharField(max_length=255, blank=True, null=True)
#     matricula = models.CharField(max_length=255, blank=True, null=True)
#     nome = models.CharField(max_length=255, blank=True, null=True)
#     senha = models.CharField(max_length=255, blank=True, null=True)
#     super_user = models.BooleanField(blank=True, null=True)
#     cargo = models.ForeignKey(Cargo, models.DO_NOTHING, blank=True, null=True)
#     setor = models.ForeignKey('Setor', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'funcionario'
#
#     def __str__(self):
#         return str(self.nome)
#
#
# class FuncionarioAcao(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     acao = models.ForeignKey(Acao, models.DO_NOTHING, blank=True, null=True)
#     funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'funcionario_acao'
#
#
# class Impressora(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     imp_caixa = models.BooleanField(blank=True, null=True)
#     imp_conta = models.BooleanField(blank=True, null=True)
#     nome = models.CharField(max_length=255, blank=True, null=True)
#     tamanho_papel = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'impressora'
#
#
# class Licenca(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     datafim = models.DateTimeField(blank=True, null=True)
#     datainicio = models.DateTimeField(blank=True, null=True)
#     data_servidor = models.DateTimeField(blank=True, null=True)
#     token = models.CharField(max_length=255, blank=True, null=True)
#     ultima_verificacao = models.DateTimeField(blank=True, null=True)
#     estabelecimento = models.ForeignKey(Estabelecimento, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'licenca'
#
#
# class Mesa(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     data_hora_abertura = models.DateTimeField(blank=True, null=True)
#     data_hora_fechamento = models.DateTimeField(blank=True, null=True)
#     descricao = models.CharField(max_length=255, blank=True, null=True)
#     numero = models.IntegerField(blank=True, null=True)
#     mesa_origem = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
#     status = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'mesa'
#
#     def __str__(self):
#         return "Mesa" + str(self.numero)
#
#
# class MovimentoCaixa(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     data_abertura = models.DateTimeField(blank=True, null=True)
#     data_fechamento = models.DateTimeField(blank=True, null=True)
#     valor_abertura = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     valor_fechamento = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     caixa = models.ForeignKey(Caixa, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'movimento_caixa'
#
#
# class MovimentoEstoque(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     data_entrada = models.DateTimeField(blank=True, null=True)
#     data_fabricacao = models.DateTimeField(blank=True, null=True)
#     lote = models.CharField(max_length=255, blank=True, null=True)
#     observacao = models.CharField(max_length=255, blank=True, null=True)
#     preco_compra = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     quantidade = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     tipo = models.CharField(max_length=255, blank=True, null=True)
#     estoque = models.ForeignKey(Estoque, models.DO_NOTHING, blank=True, null=True)
#     fornecedor = models.ForeignKey(Fornecedor, models.DO_NOTHING, blank=True, null=True)
#     setor_destino = models.ForeignKey('Setor', models.DO_NOTHING, blank=True, null=True, related_name="setor_destino")
#     setor_origem = models.ForeignKey('Setor', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'movimento_estoque'
#
#
# class OperacaoCaixa(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     descricao = models.CharField(max_length=255, blank=True, null=True)
#     tipo = models.CharField(max_length=255, blank=True, null=True)
#     valor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     movimento_caixa = models.ForeignKey(MovimentoCaixa, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'operacao_caixa'
#
#
# class Pagamento(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     desconto = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     troco = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     valor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     cartao = models.ForeignKey(Cartao, models.DO_NOTHING, blank=True, null=True)
#     conta = models.ForeignKey(Conta, models.DO_NOTHING, blank=True, null=True)
#     forma_pagamento = models.ForeignKey(FormaPagamento, models.DO_NOTHING, blank=True, null=True)
#     movimento_caixa = models.ForeignKey(MovimentoCaixa, models.DO_NOTHING, blank=True, null=True)
#     acrescimo = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     percentual = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     percentual_acrescimo = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     valor_recebido = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'pagamento'
#
#     def __str__(self):
#         return str(self.conta) + ' - ' + str(self.valor)
#
#
# class Produto(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     codigo = models.CharField(max_length=255, blank=True, null=True)
#     composicao = models.BooleanField()
#     descricao = models.CharField(max_length=255, blank=True, null=True)
#     fracionado = models.BooleanField()
#     imprime = models.BooleanField()
#     medida = models.CharField(max_length=255, blank=True, null=True)
#     valor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     visivel = models.BooleanField()
#     categoria = models.ForeignKey(Categoria, models.DO_NOTHING, blank=True, null=True, related_name="produtos")
#     setor = models.ForeignKey('Setor', models.DO_NOTHING, blank=True, null=True, related_name="setor")
#     setor_estoque = models.ForeignKey('Setor', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'produto'
#
#     def __str__(self):
#         return str(self.descricao)
#
#
# class ProdutoComposicao(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     quantidade = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     tipo = models.CharField(max_length=255, blank=True, null=True)
#     valor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     composicao = models.ForeignKey(Produto, models.DO_NOTHING, blank=True, null=True)
#     produto = models.ForeignKey(Produto, models.DO_NOTHING, blank=True, null=True, related_name="produto")
#     tamanho = models.ForeignKey('Tamanho', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'produto_composicao'
#
#
# class ProdutoConta(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     observacao = models.CharField(max_length=255, blank=True, null=True)
#     quantidade = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     valor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     conta = models.ForeignKey(Conta, models.DO_NOTHING, blank=True, null=True, related_name="produtos_conta")
#     produto = models.ForeignKey(Produto, models.DO_NOTHING, blank=True, null=True)
#     status_pedido = models.ForeignKey('StatusPedido', models.DO_NOTHING, blank=True, null=True)
#     motivo_cancelamento = models.CharField(max_length=255, blank=True, null=True)
#     origem = models.CharField(max_length=255, blank=True, null=True)
#     verificado = models.BooleanField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'produto_conta'
#
#     def __str__(self):
#         return str(self.produto) + ' - ' + str(self.conta)
#
#
# class ProdutoContaComposicao(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     composicao = models.ForeignKey(ProdutoComposicao, models.DO_NOTHING, blank=True, null=True)
#     produto_conta = models.ForeignKey(ProdutoConta, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'produto_conta_composicao'
#
#
# class ProdutoContaFracionamento(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     fracionamento = models.ForeignKey(Fracionamento, models.DO_NOTHING, blank=True, null=True, )
#     produto_conta = models.ForeignKey(ProdutoConta, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'produto_conta_fracionamento'
#
#
#     def __str__(self):
#         return str(self.produto_conta) + ' - ' + str(self.fracionamento)
#
#
# class ProdutoTamanho(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     valor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     produto = models.ForeignKey(Produto, models.DO_NOTHING, blank=True, null=True)
#     tamanho = models.ForeignKey('Tamanho', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'produto_tamanho'
#
#     def __str__(self):
#         return str(self.produto) + ' - ' + str(self.tamanho)
#
#
# class RestconCardapio(models.Model):
#     arquivo = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#
#
# class Setor(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     nome = models.CharField(max_length=255, blank=True, null=True)
#     impressora = models.ForeignKey(Impressora, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'setor'
#
#
# class StatusPedido(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     descricao = models.CharField(max_length=255, blank=True, null=True)
#     ordem = models.IntegerField()
#     setor = models.ForeignKey(Setor, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'status_pedido'
#
#
# class Tamanho(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     descricao = models.CharField(max_length=255, blank=True, null=True)
#     sigla = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tamanho'
#
#     def __str__(self):
#         return str(self.descricao)
#
#
# class Taxa(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     balcao = models.BooleanField()
#     comanda = models.BooleanField()
#     delivery = models.BooleanField(blank=True, null=True)
#     descricao = models.CharField(max_length=255, blank=True, null=True)
#     mesa = models.BooleanField()
#     tipo = models.IntegerField(blank=True, null=True)
#     valor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'taxa'
#
#     def __str__(self):
#         return str(self.mesa) + ' - ' + str(self.valor)
#
#
# class TaxaConta(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     ativo = models.BooleanField()
#     data_alteracao = models.DateTimeField(blank=True, null=True)
#     data_criacao = models.DateTimeField(blank=True, null=True)
#     responsavelacao = models.CharField(max_length=255, blank=True, null=True)
#     valor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
#     conta = models.ForeignKey(Conta, models.DO_NOTHING, blank=True, null=True, related_name='taxa')
#     taxa = models.ForeignKey(Taxa, models.DO_NOTHING, blank=True, null=True,)
#
#     class Meta:
#         managed = False
#         db_table = 'taxa_conta'
#
#     def __str__(self):
#         return str(self.conta) + ' - ' + str(self.valor)
#
#
#
#
#
#
#
def upload_cardapio(instance, filename):
    # print instance.pk
    return 'logo/'+filename

#
class Cardapio(models.Model):
    arquivo = models.FileField(verbose_name='Cardápio', upload_to=upload_cardapio, null=True,)
#
#
#
# def fuso(data):
#     return data - datetime.timedelta(hours=3)
#
#
# def hora_atual():
#     return fuso(datetime.now())