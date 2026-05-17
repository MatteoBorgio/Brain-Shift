# Brain Shift — progetto di gruppo

> Questa è la prima pagina che vede chi apre il vostro repository. Deve essere chiara, pulita, utile. Niente fuffa.

## Chi siamo

- Adam Boulal — adam.boulal2@jcmaxwell.it / Adamboulal
- Matteo Borgio — matteo.borgio@jcmaxwell.it / MatteoBorgio
- (eventuale terzo membro se siete un trio)

Classe 4A Informatica — a.s. 2025-26.

## Cos'è Brain Shift

Brain Shift è un gioco che si basa sui riflessi di una persona. Ci sono due box, uno in alto e l'altro in basso. In uno dei due box compare una combinazione di una lettera e una cifra. Se la combinazione compare nel box in alto, bisogna verificare che la cifra sia pari, mentre se la combinazione compare nel box sotto, bisogna verificare che la lettera sia una vocale.

## Come giocare

Istruzioni minime ma complete per far partire il gioco da clone pulito:

```bash
git clone https://github.com/adamboulal/brain-shift.git
cd brain-shift
pip install -r requirements.txt
python main.py
```

**Requisiti:**
- Python 3.11+
- pygame 2.1+
- pytest (per i test)

## Controlli

- ← freccia sinistra: Errato
- → freccia destra: Giusto
- p tasto p: pausa

## Screenshot

![Screenshot 1](img/immagine_1.png)

![Screenshot 2](img/immagine_2.png)

## Struttura del repository

Breve spiegazione di dove sta cosa:

```
brain_shift/
├── main.py              ← entry point
├── rules.py             ← logica regole
├── scoring.py           ← sistema scoring
├── config.py            ← configurazione
├── generator.py         ← generatore di stimoli
├── models.py            ← modelli dati
├── state.py             ← gestione stato gioco
├── timer.py             ← gestione timer
├── ui.py                ← interfaccia utente
├── requirements.txt     ← dipendenze Python
├── docs/                ← documentazione
│   ├── README.md
│   ├── README-progetto.md
│   ├── architettura.md
│   ├── devlog.md
│   ├── personalizzazioni.md
│   ├── scelte.md
│   └── uso-ia.md
└── tests/               ← test pytest
    ├── conftest.py
    ├── README.md
    ├── test_rules.py
    └── test_scoring_base.py
```

## Come lanciare i test

Eseguire tutti i test:

```bash
pytest tests/
```

**Opzioni comuni:**

```bash
# Output dettagliato
pytest tests/ -v

# Mostrare print e output durante i test
pytest tests/ -s

# Lanciare un test specifico
pytest tests/test_rules.py

# Lanciare una funzione di test specifica
pytest tests/test_rules.py::test_nome_funzione
```

---

### Domande-guida per questa pagina

Non vanno lasciate nel file finale, servono solo a voi per capire cosa scrivere.

1. Se un vostro compagno di un'altra classe apre questo repo, capisce in 30 secondi cosa fa il gioco?
2. Le istruzioni di setup sono abbastanza specifiche da funzionare sul suo computer?
3. C'è almeno uno screenshot o una GIF?
4. Tutti i link ad altre pagine di `docs/` sono validi?
