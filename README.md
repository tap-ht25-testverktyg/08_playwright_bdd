# E2E-test med Playwright och BDD

Filen `requirements.txt` innehåller alla paket som ska importeras.

För att köra, skriv `behave` i terminalen i projektets rotmapp.

Rekommenderad mappstruktur för dina projekt:

```
project_name/
├─ src/
|  └─ features/
|     ├─ pages/
|     ├─ steps/
|     └─ environment.py
|
├─ tests/
|  ├─ e2e/
|  ├─ integration/
|  ├─ performance/
|  └─ unit/
| 
├─ .gitignore
├─ behave.ini
├─ pytest.ini
├─ README.md 
└─ requirements.txt
```