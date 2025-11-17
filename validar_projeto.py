"""
Script de Validação - Verifica se o projeto está pronto para entrega
Execute antes de enviar ao professor!

Uso: python validar_projeto.py
"""

import os
import sys

def verificar_arquivo(nome_arquivo, obrigatorio=True):
    """Verifica se um arquivo existe"""
    existe = os.path.exists(nome_arquivo)
    status = "✅" if existe else ("❌" if obrigatorio else "⚠️")
    tipo = "OBRIGATÓRIO" if obrigatorio else "OPCIONAL"
    print(f"{status} {nome_arquivo:30} [{tipo}]")
    return existe

def verificar_conteudo_arquivo(nome_arquivo, texto_esperado):
    """Verifica se um arquivo contém determinado texto"""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            return texto_esperado.lower() in conteudo.lower()
    except:
        return False

def main():
    print("=" * 60)
    print("🔍 VALIDAÇÃO DO PROJETO - ANÁLISE DE DIABETES")
    print("=" * 60)
    print()
    
    todos_ok = True
    
    # 1. Verificar arquivos obrigatórios
    print("📁 ARQUIVOS OBRIGATÓRIOS:")
    print("-" * 60)
    arquivos_obrigatorios = [
        'README.md',
        'main.ipynb',
        'diabetes.csv',
        'requirements.txt',
        'LICENSE'
    ]
    
    for arquivo in arquivos_obrigatorios:
        if not verificar_arquivo(arquivo, obrigatorio=True):
            todos_ok = False
    
    print()
    
    # 2. Verificar arquivos recomendados
    print("📄 ARQUIVOS RECOMENDADOS:")
    print("-" * 60)
    arquivos_recomendados = [
        'CITATION.cff',
        '.gitignore',
        'GUIA_GITHUB.md',
        'CHECKLIST_ENTREGA.md'
    ]
    
    for arquivo in arquivos_recomendados:
        verificar_arquivo(arquivo, obrigatorio=False)
    
    print()
    
    # 3. Verificar arquivos gerados (podem não existir ainda)
    print("🔧 ARQUIVOS GERADOS (após executar notebook):")
    print("-" * 60)
    verificar_arquivo('modelo_diabetes_final.pkl', obrigatorio=False)
    verificar_arquivo('dados_tratados.csv', obrigatorio=False)
    
    print()
    
    # 4. Verificar conteúdo do README
    print("📋 CONTEÚDO DO README:")
    print("-" * 60)
    
    checks_readme = [
        ('Descrição do projeto', 'descrição'),
        ('Instruções de instalação', 'instalação'),
        ('Instruções de execução', 'execução'),
        ('Estrutura do repositório', 'estrutura'),
        ('Citação da fonte', 'citação' or 'smith'),
        ('Licença mencionada', 'licença' or 'license')
    ]
    
    for nome_check, texto in checks_readme:
        tem_conteudo = verificar_conteudo_arquivo('README.md', texto)
        status = "✅" if tem_conteudo else "❌"
        print(f"{status} {nome_check}")
        if not tem_conteudo:
            todos_ok = False
    
    print()
    
    # 5. Verificar LICENSE
    print("⚖️ LICENÇA:")
    print("-" * 60)
    
    if os.path.exists('LICENSE'):
        tem_dataset_license = verificar_conteudo_arquivo('LICENSE', 'dataset')
        tem_odbl = verificar_conteudo_arquivo('LICENSE', 'odbl')
        tem_citacao = verificar_conteudo_arquivo('LICENSE', 'smith')
        
        if tem_dataset_license and tem_odbl and tem_citacao:
            print("✅ Licença do dataset (ODbL) está documentada")
            print("✅ Citação da fonte está presente")
        else:
            print("⚠️ Licença pode estar incompleta")
            if not tem_dataset_license:
                print("   - Falta menção ao dataset")
            if not tem_odbl:
                print("   - Falta menção à licença ODbL")
            if not tem_citacao:
                print("   - Falta citação completa")
    else:
        print("❌ Arquivo LICENSE não encontrado")
        todos_ok = False
    
    print()
    
    # 6. Verificar requirements.txt
    print("📦 DEPENDÊNCIAS:")
    print("-" * 60)
    
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r') as f:
            libs = f.read()
            libs_necessarias = ['pandas', 'numpy', 'scikit-learn', 'matplotlib', 
                              'seaborn', 'scipy', 'statsmodels', 'jupyter']
            
            faltando = []
            for lib in libs_necessarias:
                if lib not in libs.lower():
                    faltando.append(lib)
            
            if not faltando:
                print(f"✅ Todas as {len(libs_necessarias)} bibliotecas essenciais estão listadas")
            else:
                print(f"⚠️ Bibliotecas faltando: {', '.join(faltando)}")
    else:
        print("❌ requirements.txt não encontrado")
        todos_ok = False
    
    print()
    
    # 7. Verificar tamanho do dataset
    print("📊 DATASET:")
    print("-" * 60)
    
    if os.path.exists('diabetes.csv'):
        tamanho_mb = os.path.getsize('diabetes.csv') / (1024 * 1024)
        print(f"✅ diabetes.csv encontrado ({tamanho_mb:.2f} MB)")
        
        if tamanho_mb > 100:
            print("⚠️ Arquivo muito grande para GitHub (>100MB)")
            print("   Considere usar Git LFS ou link de download")
    else:
        print("❌ diabetes.csv não encontrado")
        todos_ok = False
    
    print()
    
    # 8. Verificar Git
    print("🔧 GIT:")
    print("-" * 60)
    
    if os.path.exists('.git'):
        print("✅ Repositório Git inicializado")
    else:
        print("⚠️ Git ainda não inicializado")
        print("   Execute: git init")
    
    print()
    
    # Resultado final
    print("=" * 60)
    if todos_ok:
        print("✅ PROJETO PRONTO PARA ENTREGA!")
        print()
        print("Próximos passos:")
        print("1. Execute o notebook para garantir que funciona")
        print("2. Siga o arquivo GUIA_GITHUB.md para enviar ao GitHub")
        print("3. Envie o link do repositório ao professor")
    else:
        print("⚠️ PROJETO PRECISA DE AJUSTES")
        print()
        print("Revise os itens marcados com ❌ acima")
        print("Consulte o arquivo CHECKLIST_ENTREGA.md para mais detalhes")
    print("=" * 60)

if __name__ == "__main__":
    main()
