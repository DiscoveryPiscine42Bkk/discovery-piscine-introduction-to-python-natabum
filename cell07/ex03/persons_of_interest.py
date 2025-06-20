def famous_births(figures):
    
    sorted_figures = sorted(figures.values(), key=lambda person: person['date_of_birth'])
    
    
    for person in sorted_figures:
        print(f"{person['name']}: {person['date_of_birth']}")

if __name__ == "__main__":
    
    historical_figures = {
        "einstein": {"name": "Albert Einstein", "date_of_birth": "1879-03-14"},
        "newton": {"name": "Isaac Newton", "date_of_birth": "1643-01-04"},
        "curie": {"name": "Marie Curie", "date_of_birth": "1867-11-07"},
        "galileo": {"name": "Galileo Galilei", "date_of_birth": "1564-02-15"},
        "darwin": {"name": "Charles Darwin", "date_of_birth": "1809-02-12"}
    }

    famous_births(historical_figures)