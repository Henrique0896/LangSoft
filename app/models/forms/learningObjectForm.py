from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class campoPesquisa(FlaskForm): 
    pesquisa = StringField("pesquisa", validators=[DataRequired()])

class filtroDeDados(FlaskForm): 
    pesquisa = StringField("pesquisa", validators=[DataRequired()])
    campo = SelectField(u'Campo', choices=[('geral','Geral'), ('ciclo_de_vida','Ciclo de Vida'),
    ('meta_metadados','Meta Metadados'), ('dados_tecnicos','Dados Técnicos'),
    ('aspectos_educacionais','Aspectos Educacionais'), ('direitos','Direitos'),
    ('relacoes','Relações'), ('anotacoes','Anotações'), ('classificacao','Classificação')])

class updateGeral(FlaskForm): 
    g_i_catalogo = StringField("g_i_catalogo")
    g_i_entrada = StringField("g_i_entrada")
    g_titulo = StringField("g_titulo", validators=[DataRequired()])
    g_idioma = StringField("g_idioma")
    g_descricao = StringField("g_descricao")
    g_palavras_chave = StringField("g_palavras_chave")
    g_cobertura = StringField("g_cobertura")
    g_estrutura = StringField("g_estrutura")
    g_nivel_de_agregacao = StringField("g_nivel_de_agregacao")
    g_subnivel_de_agregacao = StringField("g_subnivel_de_agregacao")
    g_outros_termos = StringField("g_outros_termos")
    g_termos = StringField("g_termos")

    c_versao = StringField("c_versao")
    c_status = StringField("c_status")
    c_c_entidade = StringField("c_c_entidade")
    c_c_data = StringField("c_c_data")
    c_c_papel = StringField("c_c_papel")

    m_i_catalogo = StringField("m_i_catalogo")
    m_i_entrada = StringField("m_i_entrada")
    m_c_entidade = StringField("m_c_entidade")
    m_c_data = StringField("m_c_data")
    m_c_papel = StringField("m_c_papel")
    m_esquema_de_metadados = StringField("m_esquema_de_metadados")
    m_idioma = StringField("m_idioma")

    d_formato = StringField("d_formato")
    d_tamanho = StringField("d_tamanho")
    d_localizacao = StringField("d_localizacao")
    d_requisitos = StringField("d_requisitos")
    d_o_tipo = StringField("d_o_tipo")
    d_o_nome = StringField("d_o_nome")
    d_o_versao_minima = StringField("d_o_versao_minima")
    d_o_versao_maxima = StringField("d_o_versao_maxima")
    d_observacoes_de_instalacao = StringField("d_observacoes_de_instalacao")
    d_outros_requisitos_de_sistema = StringField("d_outros_requisitos_de_sistema")
    d_duracao = StringField("d_duracao")

    a_tipo_de_interatividade = StringField("a_tipo_de_interatividade")
    a_tipo_de_recurso_de_aprendizado = StringField("a_tipo_de_recurso_de_aprendizado")
    a_nivel_de_interatividade = StringField("a_nivel_de_interatividade")
    a_densidade_semantica = StringField("a_densidade_semantica")
    a_usuario_final = StringField("a_usuario_final")
    a_contexto_de_aprendizagem = StringField("a_contexto_de_aprendizagem")
    a_idade_recomendada = StringField("a_idade_recomendada")
    a_grau_de_dificuldade = StringField("a_grau_de_dificuldade")
    a_tempo_de_aprendizado = StringField("a_tempo_de_aprendizado")
    a_intervalo_de_tempo_de_aprendizado = StringField("a_intervalo_de_tempo_de_aprendizado")
    a_descricao = StringField("a_descricao")
    a_linguagem = StringField("a_linguagem")
    a_dominio_cognitivo = StringField("a_dominio_cognitivo")
    a_estrategia_cognitiva = StringField("a_estrategia_cognitiva")

    di_custo = StringField("di_custo")
    di_direitos_autorais = StringField("di_direitos_autorais")
    di_descricao = StringField("di_descricao")

    r_tipo = StringField("r_tipo")
    r_recurso = StringField("r_recurso")
    r_i_catalogo = StringField("r_i_catalogo")
    r_i_entrada = StringField("r_i_entrada")
    r_descricao = StringField("r_descricao")

    an_entidade = StringField("an_entidade")
    an_data = StringField("an_data")
    an_descricao = StringField("an_descricao")

    cl_proposito = StringField("cl_proposito")
    cl_c_fonte = StringField("cl_c_fonte")
    cl_c_taxon = StringField("cl_c_taxon")
    cl_c_id = StringField("cl_c_id")
    cl_c_entrada = StringField("cl_c_entrada")
    cl_descricao = StringField("cl_descricao")
    cl_palavras_chave = StringField("cl_palavras_chave")