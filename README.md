# Simulação de Ransomware em Python

Fiz este projeto como parte prática do meu curso de cibersegurança para entender na prática como um ransomware funciona em um ambiente controlado, como reverter os arquivos nos testes e o que fazer para se proteger desse tipo de ameaça.

> **Aviso:** Tudo aqui foi feito apenas para estudo e teste em ambiente isolado (`test_files/`). Não use esse tipo de código fora de cenários de teste autorizados.

---

## O que tem nessa pasta

* `ransoware.py`: O script principal da simulação. Ele gera uma chave com o `Fernet`, criptografa os arquivos que coloquei em `test_files/` e gera o arquivo `MENSAGEM_DE_RESCATE.txt`.
* `descriptografar.py`: O script que carrega a chave salva e devolve os arquivos de `test_files/` ao estado original.
* `test_files/`: Pasta de teste onde deixei um arquivo fictício (`senhas.txt` com dados de teste) para simular o alvo sem mexer em nada real.
* `MENSAGEM_DE_RESCATE.txt`: Arquivo gerado durante o teste com uma mensagem fictícia de cobrança de resgate.
* `.gitignore`: Configurado para evitar que `chave.key` e arquivos temporários do Python subam para o repositório.

---

## Como eu testei

1. Coloquei um arquivo de teste fictício dentro da pasta `test_files/`.
2. Rodei o `ransoware.py` no terminal e vi o conteúdo do arquivo virar texto criptografado, além da criação da `MENSAGEM_DE_RESCATE.txt`.
3. Em seguida, rodei o `descriptografar.py` para recuperar os arquivos e confirmar que voltavam ao normal.
4. Evitei rodar o script de criptografia duas vezes seguidas sem descriptografar antes, para não gerar outra chave por cima da anterior.

---

## Evidências do teste

* `criptografado.png`: Mostra a execução do `ransoware.py` e o conteúdo de `senhas.txt` após a criptografia.
* `descriptografado.png`: Mostra a execução do `descriptografar.py` e o `senhas.txt` restaurado ao conteúdo original.

---

## O que aprendi sobre defesa e prevenção

Ver na prática como a criptografia altera os arquivos deixa bem claro por que prevenção e recuperação rápida são essenciais:

* **Backup de verdade:** Manter cópias atualizadas e fora do alcance direto da máquina (ou isoladas) é o que evita perder dados caso ocorra um ataque.
* **Atualizações em dia:** Manter sistema e programas atualizados ajuda a fechar falhas conhecidas.
* **Antivírus, firewall e atenção:** Ter proteção ativa, desconfiar de links/arquivos suspeitos e limitar permissões desnecessárias reduz bastante a chance de o problema acontecer.