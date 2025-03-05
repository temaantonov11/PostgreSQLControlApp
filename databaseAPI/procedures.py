
create_table_sql = """
CREATE OR REPLACE FUNCTION create_table()
RETURNS VOID AS $$
BEGIN
    CREATE TABLE IF NOT EXISTS cars (
        id SERIAL PRIMARY KEY,
        brand VARCHAR(20) NOT NULL,
        model VARCHAR(20) NOT NULL,
        year INT NOT NULL,
        color VARCHAR(20) NOT NULL
    );
END;
$$ LANGUAGE plpgsql;

SELECT create_table();
"""