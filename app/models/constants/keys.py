# Neste dict vão ser salvas todas as keys de acordo com cada campo do formato LOM para poderem
# ser recuperadas e possibilitar filtragem no banco. AS keys serão chamadas em controllers.default

keys = {
    "geral": {
        0: "geral.identificador.catalogo",
        1: "geral.identificador.entrada",
        2: "geral.titulo",
        3: "geral.idioma",
        4: "geral.descricao",
        5: "geral.palavras_chave",
        6: "geral.cobertura",
        7: "geral.estrutura",
        8: "geral.nivel_de_agregacao",
        9: "geral.subnivel_de_agregacao",
        10: "geral.outros_termos",
        11: "geral.termos"
    },
    "ciclo_de_vida": {
        0: "ciclo_de_vida.versao",
        1: "ciclo_de_vida.status",
        2: "ciclo_de_vida.contribuinte.entidade",
        3: "ciclo_de_vida.contribuinte.data",
        4: "ciclo_de_vida.contribuinte.papel"
    },
    "meta_metadados": {
        0: "meta_metadados.identificador.catalogo",
        1: "meta_metadados.identificador.entrada",
        2: "meta_metadados.contribuinte.entidade",
        3: "meta_metadados.contribuinte.data",
        4: "meta_metadados.contribuinte.papel",
        5: "meta_metadados.esquema_de_metadados",
        6: "meta_metadados.idioma"
    },
    "dados_tecnicos": {
        0: "dados_tecnicos.formato",
        1: "dados_tecnicos.tamanho",
        2: "dados_tecnicos.localizacao",
        3: "dados_tecnicos.requisitos",
        4: "dados_tecnicos.ou_composto.tipo",
        5: "dados_tecnicos.ou_composto.nome",
        6: "dados_tecnicos.ou_composto.versao_minima",
        7: "dados_tecnicos.ou_composto.versao_maxima",
        8: "dados_tecnicos.observacoes_de_instalacao",
        5: "dados_tecnicos.outros_requisitos_de_sistema",
        6: "dados_tecnicos.duracao"
    },
    "aspectos_educacionais": {
        0: "aspectos_educacionais.tipo_de_iteratividade",
        1: "aspectos_educacionais.tipo_de_recurso_de_aprendizado",
        2: "aspectos_educacionais.nivel_de_interatividade",
        3: "aspectos_educacionais.densidade_semantica",
        4: "aspectos_educacionais.usuario_final",
        5: "aspectos_educacionais.contexto_de_aprendizagem",
        6: "aspectos_educacionais.idade_recomendada",
        7: "aspectos_educacionais.grau_de_dificuldade",
        8: "aspectos_educacionais.tempo_de_aprendizado",
        9: "aspectos_educacionais.intervalo_de_tempo_de_aprendizado",
        10: "aspectos_educacionais.descricao",
        11: "aspectos_educacionais.linguagem",
        12: "aspectos_educacionais.dominio_cognitivo",
        13: "aspectos_educacionais.estrategia_cognitiva"
    },
    "direitos": {
        0: "direitos.custo",
        1: "direitos.direitos_autorais",
        2: "direitos.descricao"
    },
    "relacoes": {
        0: "relacoes.tipo",
        1: "relacoes.recurso",
        2: "relacoes.identificador.catalogo",
        3: "relacoes.identificador.entrada",
        4: "relacoes.descricao"
    },
    "classificacao": {
        0: "classificacao.proposito",
        1: "classificacao.caminho_taxon.fonte",
        2: "classificacao.caminho_taxon.taxon",
        3: "classificacao.caminho_taxon.id",
        4: "classificacao.caminho_taxon.entrada",
        5: "classificacao.descricao",
        6: "classificacao.palavra_chave"
    },
    "anotacoes": {
        0: "anotacoes.entidade",
        1: "anotacoes.data",
        2: "anotacoes.descricao",
    },
    "conteudo": {
        0: "conteudo.imagem_padrao",
    }
}
