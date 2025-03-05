
create_table_sql = """
CREATE OR REPLACE FUNCTION create_table()
RETURNS VOID AS $$
BEGIN
    CREATE TABLE IF NOT EXISTS cars (
        id INT PRIMARY KEY,
        brand VARCHAR(20) NOT NULL,
        model VARCHAR(20) NOT NULL,
        year INT NOT NULL,
        color VARCHAR(20) NOT NULL
    );
END;
$$ LANGUAGE plpgsql;

SELECT create_table();
"""

insert_sql = """
CREATE OR REPLACE FUNCTION insert_car(
    id INT,
    brand VARCHAR(20),
    model VARCHAR(20),
    year INT,
    color VARCHAR(20))
RETURNS VOID AS $$
BEGIN
    INSERT INTO cars (id, brand, model, year, color)
    VALUES (id, brand, model, year, color);
END;
$$ LANGUAGE plpgsql;
"""