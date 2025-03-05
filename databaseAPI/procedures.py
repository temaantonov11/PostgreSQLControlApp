
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

search_by_brand = """
CREATE OR REPLACE FUNCTION search(search_brand VARCHAR(20))
RETURNS TABLE (
    id INT,
    brand VARCHAR(20),
    model VARCHAR(20),
    year INT,
    color VARCHAR(20)) AS $$
BEGIN
    RETURN QUERY
    SELECT cars.id, cars.brand, cars.model, cars.year, cars.color
    FROM cars
    WHERE cars.brand = search_brand;
END;
$$ LANGUAGE plpgsql;
"""

clear_table_sql = """
CREATE OR REPLACE FUNCTION clear_table()
RETURNS void AS $$
BEGIN
    TRUNCATE TABLE cars;
END;
$$ LANGUAGE plpgsql;
"""

update_sql = """
CREATE OR REPLACE FUNCTION update_tuple(
    car_id INT,
    new_brand VARCHAR(20),
    new_model VARCHAR(20),
    new_year INT,
    new_color VARCHAR(20))
RETURNS void AS $$
BEGIN
    UPDATE cars
    SET 
        brand = new_brand,
        model = new_model,
        year = new_year,
        color = new_color
    WHERE id = car_id;
END;
$$ LANGUAGE plpgsql;
"""

delete_sql = """
CREATE OR REPLACE FUNCTION delete_sql(del_brand VARCHAR(20))
RETURNS VOID AS $$
BEGIN
    DELETE FROM cars WHERE brand = del_brand;
END;
$$ LANGUAGE plpgsql;
"""

selectall_sql = """
CREATE OR REPLACE FUNCTION select_sql()
RETURNS TABLE (
    id INT,
    brand VARCHAR(20),
    model VARCHAR(20),
    year INT,
    color VARCHAR(20)) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM cars;
END;
$$ LANGUAGE plpgsql;
"""