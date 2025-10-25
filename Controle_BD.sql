CREATE DATABASE alianca_corp;
USE alianca_corp; 

CREATE TABLE departamento (
departamento_id INT AUTO_INCREMENT PRIMARY KEY, 
nome_departamento VARCHAR(255) NOT NULL
);

CREATE TABLE funcionarios (
funcionario_id INT AUTO_INCREMENT PRIMARY KEY,
nome_funcionario VARCHAR(255)  NOT NULL,
cargo VARCHAR(255),
nivel VARCHAR(255),
salario decimal(10,2),
departamento_id INT,
FOREIGN KEY (departamento_id) REFERENCES departamento (departamento_id)
);

INSERT INTO departamento (nome_departamento) VALUES
('Recursos Humanos'),
('Financeiro'),
('Marketing'),
('Operação'),
('Tecnologia de Informação');

INSERT INTO funcionarios (nome_funcionario, cargo, nivel, salario, departamento_id) VALUES
('Ana Souza', 'Recursos Humanos', 'Júnior', 2500.00, 1),
('Bruno Lima', 'Recursos Humanos', 'Pleno', 3500.00, 1),
('Carla Mendes', 'Recursos Humanos', 'Sênior', 5000.00, 1),
('Julia Fernandes', 'Financeiro', 'Júnior', 2100.00, 2),
('Lucas Cardoso', 'Financeiro', 'Pleno', 3300.00, 2),
('Mariana Lima', 'Financeiro', 'Sênior', 5000.00, 2),
('Rafael Nunes', 'Marketing', 'Pleno', 3200.00, 3),
('Daniel Alves', 'Operacao', 'Júnior', 2200.00, 4),
('Eduardo Silva', 'Operacao', 'Pleno', 3200.00, 4),
('Fernanda Rocha', 'Operacao', 'Sênior', 4500.00, 4),
('Gabriel Costa', 'Tecnologia de Informação', 'Júnior', 3000.00, 5),
('Helena Martins', 'Tecnologia de Informação', 'Pleno', 4000.00, 5),
('Igor Pereira', 'Tecnologia de Informação', 'Sênior', 5500.00, 5);
