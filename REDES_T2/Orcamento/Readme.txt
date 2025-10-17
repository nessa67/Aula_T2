-- Verificar se o banco de dados já existe e criar se não existir
CREATE DATABASE IF NOT EXISTS rack_management;

-- Usar o banco de dados rack_management
USE rack_management;

-- Verificar se a tabela equipment já existe e criar se não existir
CREATE TABLE IF NOT EXISTS equipment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    model VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    unit VARCHAR(50) NOT NULL,
    value DECIMAL(10, 2) NOT NULL,
    research_link VARCHAR(255) NULL
);


-------------------------------------------
COMANDOS EM TERMINAL:

pip install Flask mysql-connector-python

python app.py
--------------------------
