# RoutineAnalyzer with Python
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Version](https://img.shields.io/badge/version-1.0-blue)
![Language](https://img.shields.io/badge/language-Python-3776AB)
![Library](https://img.shields.io/badge/library-Pandas-150458)

A simple and functional routine analysis system built in Python.  
It processes weekly activity logs from CSV files, calculates daily/weekly statistics, and generates percentage-based distribution reports directly in the terminal.

---

## 🌐 Language Index
- <img src="https://twemoji.maxcdn.com/2/svg/1f1fa-1f1f8.svg" width="20" /> **English Version** → (you are here)
- <img src="https://twemoji.maxcdn.com/2/svg/1f1e7-1f1f7.svg" width="20" /> [**Versão em Português**](#routineanalyzer-com-python)

---

## 📚 Index
- [Description](#description)
- [Features](#features)
- [Architecture/Design](#architecturedesign)
- [Motivation / Why This Project?](#motivation--why-this-project)
- [Installation](#installation)
  - [Requirements](#requirements)
  - [Running the project](#running-the-project)
- [Contributing](#contributing)

---

## Description

The **RoutineAnalyzer** is a Python console application designed to transform raw activity logs into statistical insights.  
It analyzes a CSV file where activities are organized by weekdays and provides a clear report showing how your time is distributed.

This project was created as an exercise to strengthen knowledge in data manipulation with **Pandas**, focusing on data cleaning and statistical aggregation.

---

## Features
- Process weekly activities from a CSV source
- Automatic data cleaning (removes extra whitespaces)
- Calculate frequency and percentage of each activity per day
- Generate a consolidated weekly percentage report
- Light, fast, and organized terminal output
- Direct and useful logic without bloated dashboards

---

## Architecture/Design

### **RoutineAnalyzer Week days structure.csv**
The data source containing activities organized by weekdays (Monday to Sunday).

### **routine_analyzer.py**
The core engine of the system, responsible for:
1. **Loading:** Reading the CSV file via Pandas.
2. **Cleaning:** String normalization to avoid duplication due to typing errors.
3. **Calculation:** Processing columns to generate daily counts and percentages.
4. **Aggregation:** Consolidating all daily data into a weekly closing report.

---

### **Flow Overview**

CSV File (Input Data)
↓
routine_analyzer.py (Pandas Cleaning & Logic)
↓
Terminal Output (Daily & Weekly Reports)

---

## Motivation / Why This Project?

- Practice data cleaning and normalization (handling manual input issues).
- Consolidate Pandas fundamentals (DataFrames, value_counts, and mapping).
- Build a useful tool for personal productivity analysis.
- Understand data aggregation (transitioning from granular daily data to weekly totals).

---

## Installation

### Requirements
- Windows, Linux, or macOS  
- Python 3.x installed  
- Pandas library (`pip install pandas`)  

---

### Running the project

First, you will need a spreadsheet following a weekly structure with schedules, as shown in the example below.

<img width="1548" height="680" alt="image" src="https://github.com/user-attachments/assets/7cba263a-b60b-418a-8d1a-0fd1873ecb5f" />

The user can add or remove time slots as they wish. The only requirement for the project to function correctly is the weekday structure.

Then, you must download it as a CSV file, place it in the repository folder, and set the filename in the "df_name" variable.

The program will display all daily relationships and the weekly summary as follows:

### Daily (Monday)

TOTAL ACTIVITIES PER DAY

MONDAY

Sleep = 8 hours (33.33%)

Work = 8 hours (33.33%)

Study = 2 hours (8.33%)

Gym = 2 hours (8.33%)

Lunch = 1 hours (4.17%)

Breakfast = 1 hours (4.17%)

Dinner = 1 hours (4.17%)

Leisure = 1 hours (4.17%)

### Weekly

WEEKLY ACTIVITY REPORT

'Sleep' represents 33.33% of total week activities.

'Work' represents 25.60% of total week activities.

'Study' represents 4.76% of total week activities.

'Gym' represents 4.76% of total week activities.

'Lunch' represents 4.17% of total week activities.

'Breakfast' represents 4.17% of total week activities.

'Dinner' represents 4.17% of total week activities.

'Leisure' represents 17.86% of total week activities.

'Church' represents 1.19% of total week activities.

```bash
git clone [https://github.com/YOUR_USERNAME/RoutineAnalyzer](https://github.com/YOUR_USERNAME/RoutineAnalyzer)
cd RoutineAnalyzer
python routine_analyzer.py
```

# RoutineAnalyzer com Python
![Status](https://img.shields.io/badge/status-ativo-brightgreen)
![Versão](https://img.shields.io/badge/versão-1.0-blue)
![Linguagem](https://img.shields.io/badge/linguagem-Python-3776AB)
![Biblioteca](https://img.shields.io/badge/biblioteca-Pandas-150458)

Um sistema de análise de rotina simples e funcional feito em Python.  
Ele processa registros de atividades semanais via arquivos CSV, calcula estatísticas diárias/semanais e gera relatórios de distribuição percentual diretamente no terminal.

---

## 🌐 Índice de Idiomas
- <img src="https://twemoji.maxcdn.com/2/svg/1f1fa-1f1f8.svg" width="20" /> [**English Version**](#routineanalyzer-with-python)
- <img src="https://twemoji.maxcdn.com/2/svg/1f1e7-1f1f7.svg" width="20" /> **Versão em Português** → (você está aqui)

---

## 📚 Índice
- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Arquitetura/Design](#arquiteturadesign)
- [Motivação / Por que este projeto?](#motivação--por-que-este-projeto)
- [Instalação](#instalação)
  - [Requisitos](#requisitos)
  - [Rodando o projeto](#rodando-o-projeto)
- [Contribuição](#contribuição)

---

## Descrição

O **RoutineAnalyzer** é um aplicativo de console em Python desenvolvido para transformar registros brutos de atividades em insights estatísticos.  
Ele analisa um arquivo CSV onde as atividades são organizadas por dias da semana e fornece um relatório claro de como seu tempo está distribuído.

Este projeto foi criado como exercício para fortalecer conhecimentos em manipulação de dados com **Pandas**, focando em limpeza de dados e agregação estatística.

---

## Funcionalidades
- Processar atividades semanais a partir de uma fonte CSV
- Limpeza automática de dados (remove espaços em branco extras)
- Calcular frequência e porcentagem de cada atividade por dia
- Gerar um relatório consolidado de porcentagem semanal
- Saída em terminal leve, rápida e organizada
- Lógica direta e útil, sem dashboards inflados

---

## Arquitetura/Design

### **RoutineAnalyzer Week days structure.csv**
A fonte de dados contendo as atividades organizadas por dias da semana (Segunda a Domingo).

### **routine_analyzer.py**
O motor principal do sistema, responsável por:
1. **Carga:** Leitura do arquivo CSV via Pandas.
2. **Limpeza:** Normalização das strings para evitar duplicidade por erro de digitação.
3. **Cálculo:** Processamento das colunas para gerar contagens e porcentagens diárias.
4. **Agregação:** Consolidação de todos os dados diários em um fechamento semanal.

---

### **Fluxo Geral**

Arquivo CSV (Dados de Entrada)
↓
routine_analyzer.py (Limpeza Pandas & Lógica)
↓
Saída no Terminal (Relatórios Diários e Semanais)

---

## Motivação / Por que este projeto?

- Praticar limpeza e normalização de dados (lidando com problemas de input manual).
- Consolidar fundamentos de Pandas (DataFrames, value_counts e mapping).
- Construir uma ferramenta útil para análise de produtividade pessoal.
- Entender a agregação de dados (transição de dados granulares diários para totais semanais).

---

## Instalação

### Requisitos
- Windows, Linux ou macOS  
- Python 3.x instalado  
- Biblioteca Pandas (`pip install pandas`)  

---

### Rodando o projeto

Primeiro será necessário ter uma planilha seguindo uma estrutura semanal com horários, como no exemplo a baixo.


<img width="1546" height="679" alt="image" src="https://github.com/user-attachments/assets/64ff34e3-2e93-4194-ada9-30b7b4908d08" />

O usuário pode adicionar ou remover horários da forma que quiser. O necessário para o bom funcionamento do projeto é a estrutura de
dias na semana.

Depois deve baixar como arquivo csv, colocar na pasta do repositório e o nome do arquivo na variável "df_name".

O programa exibirá todas as relações diárias e a semanal, ficando da seguinte forma:

### Diária(segunda-feira)

TOTAL DE ATIVIDADES NO DIA

SEGUNDA

Dormir = 8 horas (33.33%)

Trabalho = 8 horas (33.33%)

Estudar = 2 horas (8.33%)

Academia = 2 horas (8.33%)

Almoço = 1 horas (4.17%)

Café Da Manhã = 1 horas (4.17%)

Jantar = 1 horas (4.17%)

Lazer = 1 horas (4.17%)

### Semanal

RELATÓRIO SEMANAL DAS ATIVIDADES

'Dormir' representa 33.33% das atividades da semana.

'Trabalho' representa 23.81% das atividades da semana.

'Estudar' representa 6.55% das atividades da semana.

'Academia' representa 4.76% das atividades da semana.

'Almoço' representa 4.17% das atividades da semana.

'Café Da Manhã' representa 4.17% das atividades da semana.

'Jantar' representa 4.17% das atividades da semana.

'Lazer' representa 17.86% das atividades da semana.

'Igreja' representa 1.19% das atividades da semana.

```bash
git clone [https://github.com/SEU_USUARIO/RoutineAnalyzer](https://github.com/SEU_USUARIO/RoutineAnalyzer)
cd RoutineAnalyzer
python routine_analyzer.py
```

### Contribuição
Faça um fork do repositório

Crie uma nova branch

Adicione suas melhorias

Abra um pull request
