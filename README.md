# 🚀 Astro Portfolio – Data Pipeline Astroneer

## 📌 Contexte
Ce projet a pour objectif de construire un **pipeline de données complet** autour du jeu *Astroneer*.  
Les données proviennent du **wiki Astroneer** (tables et pages web), sont intégrées dans une base **Oracle APEX en ligne**, puis exploitées dans **Power BI** pour créer des dashboards interactifs.

Ce projet fait office de **portfolio** et démontre mes compétences en :
- Web scraping (Python)
- ETL (Talend Open Studio)
- Base de données Oracle
- Visualisation de données (Power BI)

---

## 🛠️ Workflow technique

```mermaid
flowchart LR
    A[Wiki Astroneer] --> B[Python Scraping]
    B --> C[CSV Export]
    C --> D[Talend ETL]
    D --> E[Oracle APEX DB]
    E --> D
    E --> F[Power BI Dashboard]
````

astro-portfolio/
│
├── python/        # Scripts de scraping et transformation
├── talend/        # Jobs ETL pour charger les données
├── sql/           # Scripts Oracle (tables, vues)
├── powerbi/       # Dashboards Power BI (.pbix, exports)
└── docs/          # Schémas, captures, documentation
