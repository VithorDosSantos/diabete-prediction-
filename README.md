# Análise Preditiva de Diabetes

Projeto de modelagem estatística para predição de diabetes usando técnicas de machine learning.

## 📋 Descrição do Projeto

Este projeto realiza uma análise completa de dados médicos para prever a ocorrência de diabetes em pacientes. Implementa diferentes técnicas de aprendizado de máquina, incluindo regressão linear, Naive Bayes e regressão logística, com foco em otimização e avaliação de desempenho.

**Objetivo Principal:** Desenvolver um modelo de classificação capaz de prever diabetes com base em 8 variáveis médicas.

### Principais Características:
- Análise exploratória detalhada com visualizações
- Tratamento de outliers pelo método IQR
- Implementação de múltiplos modelos (regressão linear, Naive Bayes, regressão logística)
- Otimização com GridSearchCV e validação cruzada
- Análise de trade-offs e interpretabilidade
- Modelo final com 73.38% de acurácia

## 🗂️ Estrutura do Repositório

```
.
├── main.ipynb              # Notebook principal com toda a análise
├── diabetes.csv            # Dataset (Pima Indians Diabetes)
├── requirements.txt        # Dependências do projeto
├── modelo_diabetes_final.pkl   # Modelo treinado (gerado após execução)
├── dados_tratados.csv      # Dados após tratamento (gerado após execução)
├── LICENSE                 # Licença do projeto
└── README.md              # Este arquivo
```

## 📊 Dataset

**Nome:** Diabetes Data Set  
**Fonte:** [Kaggle - Diabetes Data Set](https://www.kaggle.com/datasets/mathchi/diabetes-data-set/data)  
**Licença:** Open Database License (ODbL)  
**Tamanho:** 768 amostras, 9 variáveis (8 features + 1 target)

### Variáveis:
- `Pregnancies`: Número de gestações
- `Glucose`: Concentração de glicose no sangue (mg/dL)
- `BloodPressure`: Pressão arterial diastólica (mm Hg)
- `SkinThickness`: Espessura da pele do tríceps (mm)
- `Insulin`: Insulina sérica de 2 horas (mu U/ml)
- `BMI`: Índice de massa corporal (peso em kg/(altura em m)²)
- `DiabetesPedigreeFunction`: Função de histórico familiar
- `Age`: Idade (anos)
- `Outcome`: Variável alvo (0 = não diabético, 1 = diabético)

**Citação:**
```
Smith, J.W., Everhart, J.E., Dickson, W.C., Knowler, W.C., & Johannes, R.S. (1988).
Using the ADAP learning algorithm to forecast the onset of diabetes mellitus.
In Proceedings of the Symposium on Computer Applications and Medical Care (pp. 261--265).
IEEE Computer Society Press.
```

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes)

### Passo 1: Clone o repositório
```bash
git clone https://github.com/seu-usuario/diabetes-prediction.git
cd diabetes-prediction
```

### Passo 2: Crie um ambiente virtual (recomendado)
```bash
python -m venv venv
```

**Ativar no Windows:**
```bash
venv\Scripts\activate
```

**Ativar no Linux/Mac:**
```bash
source venv/bin/activate
```

### Passo 3: Instale as dependências
```bash
pip install -r requirements.txt
```

### Passo 4: Execute o notebook
```bash
jupyter notebook main.ipynb
```

Ou use VS Code com a extensão Jupyter instalada.

### Passo 5: Execute todas as células
No Jupyter, clique em `Cell > Run All` para executar toda a análise.

## 📈 Resultados Principais

| Modelo | Accuracy | F1-Score | AUC-ROC |
|--------|----------|----------|---------|
| Baseline | 64.29% | - | - |
| Regressão Linear Simples | - | - | - |
| Regressão Linear Múltipla | - | - | - |
| Naive Bayes | 75.97% | 0.65 | 0.82 |
| Regressão Logística | 73.38% | 0.60 | 0.82 |
| **RL Otimizada (Final)** | **73.38%** | **0.63** | **0.82** |

**Modelo Recomendado:** Regressão Logística com C=10 e max_iter=1000

### Insights Principais:
1. Glucose é a variável mais correlacionada com diabetes (r=0.493)
2. Dataset desbalanceado: 65% não diabéticos, 35% diabéticos
3. Regressão linear inadequada para este problema (classificação binária)
4. Otimização melhorou performance em ~14% sobre baseline
5. VIF identificou multicolinearidade, controlada por regularização

## 🔧 Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** - Manipulação de dados
- **NumPy** - Operações numéricas
- **Scikit-learn** - Modelos de machine learning
- **Statsmodels** - Análise estatística
- **Matplotlib/Seaborn** - Visualizações
- **SciPy** - Testes estatísticos

## 📝 Metodologia

1. **Análise Exploratória:**
   - Estatísticas descritivas
   - Matriz de correlação
   - Testes t para comparação de grupos
   - Histogramas comparativos

2. **Pré-processamento:**
   - Detecção de outliers (método IQR)
   - Tratamento com substituição pela mediana
   - Divisão: 60% treino, 20% validação, 20% teste

3. **Modelagem:**
   - Regressão Linear (simples, múltipla, polinomial)
   - Naive Bayes Gaussiano
   - Regressão Logística

4. **Avaliação:**
   - Métricas: Accuracy, Precision, Recall, F1-Score, AUC-ROC
   - Matrizes de confusão
   - Análise de resíduos e diagnósticos

5. **Otimização:**
   - Validação cruzada (5-fold)
   - GridSearchCV para tuning de hiperparâmetros
   - Análise de trade-offs

## 👥 Autores

- Vithor Dos Santos Santa Rosa
- João Felipe Da Rocha Soares

**Disciplina:** Modelagem Estatística  
**Instituição:** Cesupa  
**Data:** Novembro 2025

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

O dataset utilizado está sob a **Open Database License (ODbL)** conforme especificado pela fonte original.

## 🙏 Agradecimentos

- UCI Machine Learning Repository
- Kaggle pela disponibilização dos dados
- Comunidade open-source das bibliotecas utilizadas

## 📧 Contato

Para dúvidas ou sugestões, abra uma issue no repositório.

---

**⭐ Se este projeto foi útil, considere dar uma estrela!**
