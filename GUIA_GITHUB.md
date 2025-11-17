# 🚀 Guia Rápido - Como Enviar para o GitHub

## Passo 1: Criar Repositório no GitHub

1. Acesse https://github.com e faça login
2. Clique no botão **"New"** (ou ícone +) para criar novo repositório
3. Preencha:
   - **Repository name:** `diabetes-prediction` (ou outro nome)
   - **Description:** "Análise preditiva de diabetes usando machine learning"
   - **Public** ou **Private** (escolha conforme preferir)
   - **NÃO** marque "Initialize with README" (já temos um)
4. Clique em **"Create repository"**

## Passo 2: Configurar Git Local (primeira vez apenas)

Abra o PowerShell e execute:

```powershell
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

## Passo 3: Inicializar e Enviar o Repositório

No PowerShell, navegue até a pasta do projeto e execute:

```powershell
# 1. Inicializar repositório Git
cd "C:\Users\vitho\OneDrive\Documentos\Modelagem Estatitisca\Projeto"
git init

# 2. Adicionar todos os arquivos
git add .

# 3. Fazer o primeiro commit
git commit -m "Initial commit: Análise preditiva de diabetes"

# 4. Adicionar o repositório remoto (substitua SEU-USUARIO pelo seu nome de usuário)
git remote add origin https://github.com/SEU-USUARIO/diabetes-prediction.git

# 5. Enviar para o GitHub
git branch -M main
git push -u origin main
```

## Passo 4: Verificar

Acesse o repositório no GitHub e verifique se todos os arquivos foram enviados:
- ✅ README.md
- ✅ main.ipynb
- ✅ diabetes.csv
- ✅ requirements.txt
- ✅ LICENSE
- ✅ CITATION.cff
- ✅ .gitignore

## 📝 Comandos Git Úteis

### Verificar status dos arquivos
```powershell
git status
```

### Adicionar alterações específicas
```powershell
git add nome-do-arquivo.txt
```

### Fazer commit de mudanças
```powershell
git commit -m "Descrição das mudanças"
```

### Enviar mudanças para o GitHub
```powershell
git push
```

### Ver histórico de commits
```powershell
git log --oneline
```

### Baixar mudanças do GitHub
```powershell
git pull
```

## 🔧 Solução de Problemas

### Erro: "remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/SEU-USUARIO/diabetes-prediction.git
```

### Erro: "failed to push some refs"
```powershell
git pull origin main --rebase
git push origin main
```

### Ignorar arquivos grandes (modelo .pkl)
Se o arquivo `modelo_diabetes_final.pkl` for muito grande (>100MB):
1. Adicione `*.pkl` no arquivo `.gitignore`
2. Execute: `git rm --cached modelo_diabetes_final.pkl`
3. Faça commit: `git commit -m "Remove arquivo grande"`

## 📦 Alternativa: GitHub Desktop (Interface Gráfica)

Se preferir uma interface visual:
1. Baixe o GitHub Desktop: https://desktop.github.com/
2. Abra o programa e faça login
3. Clique em "Add" → "Add Existing Repository"
4. Selecione a pasta do projeto
5. Clique em "Publish repository"

## ✅ Checklist Final

- [ ] Todos os arquivos estão no GitHub
- [ ] README.md está formatado corretamente
- [ ] requirements.txt lista todas as dependências
- [ ] LICENSE está presente
- [ ] Dataset está incluído (ou link de download no README)
- [ ] Notebook executa sem erros
- [ ] Repositório está público (se exigido pelo professor)

## 🎓 Para Entregar ao Professor

Envie o link do repositório no formato:
```
https://github.com/SEU-USUARIO/diabetes-prediction
```

Ou crie uma release:
1. No GitHub, vá em "Releases" → "Create a new release"
2. Tag version: `v1.0.0`
3. Title: "Entrega Final - Modelagem Estatística"
4. Description: Resumo do projeto
5. Clique em "Publish release"
6. Envie o link da release ao professor

---

**Dúvidas?** Consulte a documentação oficial: https://docs.github.com/pt
