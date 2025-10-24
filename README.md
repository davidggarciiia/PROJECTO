# CINE BICHO

![488869232_17962851365866278_7552931985760598634_n](https://github.com/user-attachments/assets/7f4a8038-8789-4159-9fbc-08586f03a8ef)

## INTRODUCTION

This project consists of creating a system to manage movie ticket purchases. It allows users to choose a movie, select the time, choose seats, and apply discounts before generating the final ticket.
The system is divided into several modules, each with a specific function: movies, seats, discounts, and tickets. Thanks to this organization, the program is easier to understand, maintain, and expand in the future.

## PROJECT STRUCTURE
```
PROJECT/
│
├── CINE/
│   ├── ASIENTOS/
│   │   └── asientos.py          # Seat management and availability
│   │
│   ├── DESCUENTOS/
│   │   └── descuento.py          # Discount application logic
│   │
│   ├── PELICULAS/
│   │   ├── pelicula.py           # Movie class
│   │   ├── peliculas_disponibles.py  # Movie catalog
│   │   └── peliculas_utils.py    # Movie utilities
│   │
│   └── TICKET/
│       ├── ticket.py             # Ticket generation
│       └── tickets.csv           # Ticket storage
│
├── main.py                       # Main entry point
├── .gitignore
└── README.md
```

## MODULES

### ASIENTOS (Seats)
Manages seat availability and reservations in the cinema rooms.

### DESCUENTOS (Discounts)
Applies different types of discounts based on customer type.

### PELICULAS (Movies)
Handles the available movie catalog and its utilities.

### TICKET
Generates and stores purchase tickets.

**DEPLOYMENT GUIDE**
- Clone the project in your device using the following command:
  
  ```python
  git clone https://github.com/davidggarciiia/PROJECTO.git`

- Execute main.py, located in PROJECTO/CINE/main.py

  ```python
  python .\PROJECTO\CINE\main.py`

