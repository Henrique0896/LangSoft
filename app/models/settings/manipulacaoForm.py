class ManipulacaoForm():
    def preencher(form, video):
        form.g_i_catalogo.data = video['geral']['identificador']['catalogo']
        form.g_i_entrada.data = video['geral']['identificador']['entrada']
        form.g_titulo.data = video['geral']['titulo']
        form.g_idioma.data = video['geral']['idioma']
        form.g_descricao.data = video['geral']['descricao']
        form.g_palavras_chave.data = video['geral']['palavras_chave']
        form.g_cobertura.data = video['geral']['cobertura']
        form.g_estrutura.data = video['geral']['estrutura']
        form.g_nivel_de_agregacao.data = video['geral']['nivel_de_agregacao']
        form.g_subnivel_de_agregacao.data = video['geral']['subnivel_de_agregacao']
        form.g_outros_termos.data = video['geral']['outros_termos']
        form.g_termos.data = video['geral']['termos']

        form.c_versao.data = video['ciclo_de_vida']['versao']
        form.c_status.data = video['ciclo_de_vida']['status']
        form.c_c_entidade.data = video['ciclo_de_vida']['contribuinte']['entidade']
        form.c_c_data.data = video['ciclo_de_vida']['contribuinte']['data']
        form.c_c_papel.data = video['ciclo_de_vida']['contribuinte']['papel']

        form.m_i_catalogo.data = video['meta_metadados']['identificador']['catalogo']
        form.m_i_entrada.data = video['meta_metadados']['identificador']['entrada']
        form.m_c_entidade.data = video['meta_metadados']['contribuinte']['entidade']
        form.m_c_data.data = video['meta_metadados']['contribuinte']['data']
        form.m_c_papel.data = video['meta_metadados']['contribuinte']['papel']
        form.m_esquema_de_metadados.data = video['meta_metadados']['esquema_de_metadados']
        form.m_idioma.data = video['meta_metadados']['idioma']

        form.d_formato.data = video['dados_tecnicos']['formato']
        form.d_tamanho.data = video['dados_tecnicos']['tamanho']
        form.d_localizacao.data = video['dados_tecnicos']['localizacao']
        form.d_requisitos.data = video['dados_tecnicos']['requisitos']
        form.d_o_tipo.data = video['dados_tecnicos']['ou_composto']['tipo']
        form.d_o_nome.data = video['dados_tecnicos']['ou_composto']['nome']
        form.d_o_versao_minima.data = video['dados_tecnicos']['ou_composto']['versao_minima']
        form.d_o_versao_maxima.data = video['dados_tecnicos']['ou_composto']['versao_maxima']
        form.d_observacoes_de_instalacao.data = video['dados_tecnicos']['observacoes_de_instalacao']
        form.d_outros_requisitos_de_sistema.data = video['dados_tecnicos']['outros_requisitos_de_sistema']
        form.d_duracao.data = video['dados_tecnicos']['duracao']

        form.a_tipo_de_interatividade.data = video['aspectos_educacionais']['tipo_de_interatividade']
        form.a_tipo_de_recurso_de_aprendizado.data = video['aspectos_educacionais']['tipo_de_recurso_de_aprendizado']
        form.a_nivel_de_interatividade.data = video['aspectos_educacionais']['nivel_de_interatividade']
        form.a_densidade_semantica.data = video['aspectos_educacionais']['densidade_semantica']
        form.a_usuario_final.data = video['aspectos_educacionais']['usuario_final']
        form.a_contexto_de_aprendizagem.data = video['aspectos_educacionais']['contexto_de_aprendizagem']
        form.a_idade_recomendada.data = video['aspectos_educacionais']['idade_recomendada']
        form.a_grau_de_dificuldade.data = video['aspectos_educacionais']['grau_de_dificuldade']
        form.a_tempo_de_aprendizado.data = video['aspectos_educacionais']['tempo_de_aprendizado']
        form.a_intervalo_de_tempo_de_aprendizado.data = video['aspectos_educacionais']['intervalo_de_tempo_de_aprendizado']
        form.a_descricao.data = video['aspectos_educacionais']['descricao']
        form.a_linguagem.data = video['aspectos_educacionais']['linguagem']
        form.a_dominio_cognitivo.data = video['aspectos_educacionais']['dominio_cognitivo']
        form.a_estrategia_cognitiva.data = video['aspectos_educacionais']['estrategia_cognitiva']

        form.di_custo.data = video['direitos']['custo']
        form.di_direitos_autorais.data = video['direitos']['direitos_autorais']
        form.di_descricao.data = video['direitos']['descricao']

        form.r_tipo.data = video['relacoes']['tipo']
        form.r_recurso.data = video['relacoes']['recurso']
        form.r_i_catalogo.data = video['relacoes']['identificador']['catalogo']
        form.r_i_entrada.data = video['relacoes']['identificador']['entrada']
        form.r_descricao.data = video['relacoes']['descricao']

        form.an_entidade.data = video['anotacoes']['entidade']
        form.an_data.data = video['anotacoes']['data']
        form.an_descricao.data = video['anotacoes']['descricao']
      
        form.cl_proposito.data = video['classificacao']['proposito']
        form.cl_c_fonte.data = video['classificacao']['caminho_taxon']['fonte']
        form.cl_c_taxon.data = video['classificacao']['caminho_taxon']['taxon']
        form.cl_c_id.data = video['classificacao']['caminho_taxon']['id']
        form.cl_c_entrada.data = video['classificacao']['caminho_taxon']['entrada']
        form.cl_descricao.data = video['classificacao']['descricao']
        form.cl_palavras_chave.data = video['classificacao']['palavras_chave']

       
        return form

    def atualizarObjeto(form, video):
        video['geral']['identificador']['catalogo'] = form.g_i_catalogo.data
        video['geral']['identificador']['entrada'] = form.g_i_entrada.data
        video['geral']['titulo'] = form.g_titulo.data
        video['geral']['idioma'] = form.g_idioma.data
        video['geral']['descricao'] = form.g_descricao.data
        video['geral']['palavras_chave'] = form.g_palavras_chave.data
        video['geral']['cobertura'] = form.g_cobertura.data
        video['geral']['estrutura'] = form.g_estrutura.data
        video['geral']['nivel_de_agregacao'] = form.g_nivel_de_agregacao.data
        video['geral']['subnivel_de_agregacao'] = form.g_subnivel_de_agregacao.data
        video['geral']['outros_termos'] = form.g_outros_termos.data
        video['geral']['termos'] = form.g_termos.data

        video['ciclo_de_vida']['versao'] = form.c_versao.data 
        video['ciclo_de_vida']['status'] = form.c_status.data
        video['ciclo_de_vida']['contribuinte']['entidade'] = form.c_c_entidade.data
        video['ciclo_de_vida']['contribuinte']['data'] = form.c_c_data.data
        video['ciclo_de_vida']['contribuinte']['papel'] = form.c_c_papel.data

        video['meta_metadados']['identificador']['catalogo'] = form.m_i_catalogo.data 
        video['meta_metadados']['identificador']['entrada'] = form.m_i_entrada.data
        video['meta_metadados']['contribuinte']['entidade'] = form.m_c_entidade.data
        video['meta_metadados']['contribuinte']['data'] = form.m_c_data.data
        video['meta_metadados']['contribuinte']['papel'] = form.m_c_papel.data
        video['meta_metadados']['esquema_de_metadados'] = form.m_esquema_de_metadados.data
        video['meta_metadados']['idioma'] = form.m_idioma.data

        video['dados_tecnicos']['formato'] = form.d_formato.data
        video['dados_tecnicos']['tamanho'] = form.d_tamanho.data
        video['dados_tecnicos']['localizacao'] = form.d_localizacao.data
        video['dados_tecnicos']['requisitos'] = form.d_requisitos.data
        video['dados_tecnicos']['ou_composto']['tipo'] = form.d_o_tipo.data 
        video['dados_tecnicos']['ou_composto']['nome'] = form.d_o_nome.data 
        video['dados_tecnicos']['ou_composto']['versao_minima'] = form.d_o_versao_minima.data
        video['dados_tecnicos']['ou_composto']['versao_maxima'] = form.d_o_versao_maxima.data
        video['dados_tecnicos']['observacoes_de_instalacao'] = form.d_observacoes_de_instalacao.data 
        video['dados_tecnicos']['outros_requisitos_de_sistema'] = form.d_outros_requisitos_de_sistema.data 
        video['dados_tecnicos']['duracao'] = form.d_duracao.data

        video['aspectos_educacionais']['tipo_de_interatividade'] = form.a_tipo_de_interatividade.data
        video['aspectos_educacionais']['tipo_de_recurso_de_aprendizado'] = form.a_tipo_de_recurso_de_aprendizado.data
        video['aspectos_educacionais']['nivel_de_interatividade'] = form.a_nivel_de_interatividade.data
        video['aspectos_educacionais']['densidade_semantica'] = form.a_densidade_semantica.data
        video['aspectos_educacionais']['usuario_final'] = form.a_usuario_final.data
        video['aspectos_educacionais']['contexto_de_aprendizagem'] = form.a_contexto_de_aprendizagem.data
        video['aspectos_educacionais']['idade_recomendada'] = form.a_idade_recomendada.data
        video['aspectos_educacionais']['grau_de_dificuldade'] = form.a_grau_de_dificuldade.data
        video['aspectos_educacionais']['tempo_de_aprendizado'] = form.a_tempo_de_aprendizado.data
        video['aspectos_educacionais']['intervalo_de_tempo_de_aprendizado'] = form.a_intervalo_de_tempo_de_aprendizado.data
        video['aspectos_educacionais']['descricao'] = form.a_descricao.data
        video['aspectos_educacionais']['linguagem'] = form.a_linguagem.data
        video['aspectos_educacionais']['dominio_cognitivo'] = form.a_dominio_cognitivo.data
        video['aspectos_educacionais']['estrategia_cognitiva'] = form.a_estrategia_cognitiva.data

        video['direitos']['custo'] = form.di_custo.data
        video['direitos']['direitos_autorais'] = form.di_direitos_autorais.data
        video['direitos']['descricao'] = form.di_descricao.data

        video['relacoes']['tipo'] = form.r_tipo.data
        video['relacoes']['recurso'] = form.r_recurso.data
        video['relacoes']['identificador']['catalogo'] = form.r_i_catalogo.data
        video['relacoes']['identificador']['entrada'] = form.r_i_entrada.data
        video['relacoes']['descricao'] = form.r_descricao.data

        video['anotacoes']['entidade'] = form.an_entidade.data
        video['anotacoes']['data'] = form.an_data.data 
        video['anotacoes']['descricao'] = form.an_descricao.data

        video['classificacao']['proposito'] = form.cl_proposito.data
        video['classificacao']['caminho_taxon']['fonte'] = form.cl_c_fonte.data
        video['classificacao']['caminho_taxon']['taxon'] = form.cl_c_taxon.data
        video['classificacao']['caminho_taxon']['id'] = form.cl_c_id.data
        video['classificacao']['caminho_taxon']['entrada'] = form.cl_c_entrada.data
        video['classificacao']['descricao'] = form.cl_descricao.data
        video['classificacao']['palavras_chave'] = form.cl_palavras_chave.data

        return video