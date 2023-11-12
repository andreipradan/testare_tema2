
## Automatizare in python folosind frameworkul playwright

### Cerinte initiale
Se va realiza un exemplu de automatizare in orice limbaj.

Se va explica codul si ce face automatizarea.

Se va incarca si un fisier txt cu descrierea a ce face automatizarea.

*Automatizarea va fi diferita de automatizarea de la proiect; sa nici nu aiba legatura cu proiectul.


### Descrierea proiectului

#### Motivatie
Am ales sa folosesc biblioteca [playwright](https://playwright.dev/) fiindca am tot auzit ca e foarte populara ([9.6k stars pe github](https://github.com/microsoft/playwright-python)) si in sfarsit s-a ivit ocazia de a o folosi.

Documentatie playwright specifica pentru limbajul python se pot gasi [aici](https://playwright.dev/python/docs/intro).

### Scenarii de automatizare

- Am scris cele trei scenarii pentru login [gasite aici](https://practicetestautomation.com/practice-test-login/) in python/playwright

- In plus fata de a implementa scenariile respective - si a nu "hardcoda" credentialele pentru login - am decis sa folosesc playwright pentru extragerea credentialelor afisate in pagina respectiva de test

- Detaliile fiecarui test case se pot gasi ca docstring in interiorul fiecarui test

- check url usiCredentialele se extrag folosind o fixtura de pytest la inceputul fisierului


## Ghid de folosire a proiectului

#### Preconditii
- python instalat
  - versiune folosita: 3.12 (se poate downloada si instala [de aici](https://www.python.org/downloads/))

1. Creati un virtual environment pentru a nu polua setupul si dependintele globale specifice python:
   ```bash
    python -m venv venv_testare_tema_2
   ```
2. Activati virtualenv-ul creat:
   ```bash
   source venv_testare_tema_2/bin/activate 
   ```
3. Instalati toate bibliotecile/dependintele din requirements.txt
    ```bash
   pip install -r requirements.txt
   ```
4. Instalati browserele necesare playwright
    ```bash
   playwright install
   ```
5. Rulati scriptul automatizat
    ```bash
   pytest
   ```
   
#### OPTIONAL
- Daca se doreste vizualizarea in timp real a actiunilor automate facute de playwright se poate rula in modul "headed"
    ```bash
       pytest --headed
    ```
- Testele au fost implementate in asa mod - izolat - incat
  - daca se doreste rularea in paralel a tuturor testelor se poate face prin:
      ```bash
    pytest -n auto
    ```
    Note:
    - necesita biblioteca `pytest-xdist` (inclusa in requirements.tzt - instalata deja la pasul 3)
    - auto o sa descopere el numarul de procese maxim ce pot fi folosite
    - se poate folosi un integer daca se vrea configurat manual: e.g. `-n 2`
- Daca se doreste oprirea executiei la un anumit punct din automatizare se poate adauga in [test_login_feature](test_login_feature.py) oriunde expresia
    ```python
    breakpoint()
    ```
    - in momentul acesta se poate
      - afisa linia la care e executia tastand `l` (L mic + enter)
      - merge la linia urmatoare tastand `n` (N mic + enter)
    - mai multe detalii despre breakpoint [aici](https://docs.python.org/3/library/pdb.html)
