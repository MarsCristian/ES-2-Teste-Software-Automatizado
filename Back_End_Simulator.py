import csv
import re

class self:
    def validar_nome(self, nome):
        if re.search(r'\d', nome):  # Verifica se o nome contém números
            self.vnome = False
            return False
        if len(nome) < 2 or len(nome) > 25:  # Verifica se o nome tem tamanho válido (entre 2 e 25 caracteres)
            self.vnome = False
            return False
        

        self.vnome = True
        return True

    def validar_senha(self, senha):
        if len(senha) < 4 or len(senha) > 25:  # Verifica se a senha tem tamanho válido (entre 4 e 25 caracteres)
            self.vsenha = False
            return False
        
        self.vsenha = True
        return True

    def validar_numero(self, numero):
        if re.match(r'^\d{2}-\d{5}-\d{4}$', numero) or re.match(r'^\d{11}$', numero) or re.match(r'^\(\d{2}\)\d{9}$', numero):
            # Verifica se o número está nos formatos válidos xx-xxxxx-xxxx, xxxxxxxxxxx ou (xx)xxxxxxxxx
            self.vnumero = True
            return True

        self.vnumero = False
        return False

    def validar_email(self, email):
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            # Verifica se o email está no formato válido
            self.vemail = True
            return True
        
        self.vemail = False
        return False

    def validar_endereco(self, endereco):
        if len(endereco) > 60:  # Verifica se o endereço tem no máximo 60 caracteres
            self.vendereco = False
            return False
        

        self.vendereco = True
        return True
    
    def validar_request(self,request):
        if self.validar_nome(request['nome']) and self.validar_email(request['email']) \
        and self.validar_numero(request['numero']) and self.validar_endereco(request['endereco']) \
        and self.validar_senha(request['senha']):
            response = "Dados Válidos, enviando ao Banco de Dados..."
            print(response)
            salvar_no_banco_de_dados(request)
            return 'sucesso'

        else:
            print("Há dados invalidos!:")
            response = ''
            if not self.vnome:
                response += 'nome, '
            if not self.vemail:
                response += 'email, '
            if not self.vnumero:
                response += 'numero, '
            if not self.vsenha:
                response += 'senha, '
            if not self.vendereco:
                response += 'endereco, '
            print(response)
            return response

        

def salvar_no_banco_de_dados(dados):
    with open('dados.csv', 'a', newline='') as arquivo_csv:
        writer = csv.DictWriter(arquivo_csv, fieldnames=['Nome', 'Email', 'Número', 'Endereço', 'Senha'])
        
        # Verifica se o arquivo CSV já existe ou é um novo arquivo
        if arquivo_csv.tell() == 0:
            writer.writeheader()
        
        writer.writerow(dados)


    
