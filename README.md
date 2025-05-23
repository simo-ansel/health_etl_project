# Health ETL Project

Progetto ETL per estrazione, trasformazione e caricamento di un dataset sanitario simulato in un database PostgreSQL, completamente containerizzato con Docker e Docker Compose.

---

## Contenuti

- [Descrizione](#descrizione)  
- [Prerequisiti](#prerequisiti)  
- [Setup e Installazione](#setup-e-installazione)  
- [Avvio del progetto](#avvio-del-progetto)  
- [Esecuzione manuale ETL](#esecuzione-manuale-etl)  
- [Verifica dati nel DB](#verifica-dati-nel-db)  
- [Pulizia](#pulizia)  
- [Contatti e Supporto](#contatti-e-supporto)

---

## Descrizione

Questo progetto implementa un processo ETL per caricare dati sanitari simulati in un database PostgreSQL. 
Il progetto è strutturato per essere facilmente avviato e riproducibile tramite Docker, per semplicità di setup e distribuzione.

---

## Prerequisiti

- Docker (versione recente, minimo 20.x)
- Docker Compose (minimo 1.29.x)

---

## Setup e Installazione

1. Clona il repository:

    ```bash
    git clone https://github.com/tuo-username/health_etl_project.git
    cd health_etl_project
    ```
    
2. (Opzionale) Aggiorna requirements.txt se vuoi modificare o aggiungere pacchetti Python.

3. Costruisci le immagini Docker senza cache per assicurarti di avere tutto aggiornato:

    ```bash
    sudo docker-compose build --no-cache
    ```

## Avvio del progetto

Avvia i container PostgreSQL e ETL:

```bash
sudo docker-compose up
```
    
Il processo ETL partirà automaticamente:
- Esegue l’estrazione
- Applica la trasformazione
- Effettua il caricamento nel DB
- Il container ETL terminerà con exit code 0.

## Debug o interventi manuali

Se vuoi mantenere il container ETL attivo per debug o interventi manuali, usa:

```bash
sudo docker-compose run --rm etl bash
```

## Esecuzione manuale ETL
All’interno del container ETL puoi eseguire manualmente lo script principale:

``` bash
python main.py
```

Questo lancerà il processo ETL e caricherà i dati nel database.

## Verifica dati nel DB

Per connetterti al database PostgreSQL ed eseguire query:

1. Accedi al container del DB:

    ``` bash
    sudo docker exec -it health_etl_project_db_1 psql -U postgres -d healthcare
    ```
    
2. Esempio di query per vedere le prime righe:

    ``` bash
    SELECT * FROM healthcare_data LIMIT 10;
    ```
    
## Pulizia

Per fermare e rimuovere i container e le risorse create:

``` bash
sudo docker-compose down -v
```

Questo rimuove anche i volumi (inclusi i dati PostgreSQL).

Se vuoi anche rimuovere tutte le immagini Docker non più utilizzate e liberare spazio:

``` bash
sudo docker image prune -a
```

ATTENZIONE: questo comando eliminerà tutte le immagini non utilizzate da container attivi. Usalo solo se sei sicuro di non averne bisogno.

## Grazie per aver usato il progetto Health ETL!

