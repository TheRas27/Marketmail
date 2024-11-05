#Biblioteca abaixo:

chave_api_sendgrid = "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"

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

conta_sendgrid = SendGridAPIClient(chave_api_sendgrid)

email = Mail(from_email="rodrigoaraujo2700@gmail.com", 
             to_emails=["rafaelluckner3@gmail.com"], 
             subject="Email enviado no sendgrid via python", 
             html_content="<p>Bom dia!</p><p>Segue novo gráfico formuládo</p>")

resposta = conta_sendgrid.send(email)
print(resposta.status_code)