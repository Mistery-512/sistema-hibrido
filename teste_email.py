import smtplib

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login("email do remetente", "codigo google")
        
        # Codifique a mensagem corretamente em UTF-8
        assunto = "Teste"
        corpo = "Este é um e-mail de teste com caracteres especiais: é, ç, à."
        mensagem = f"Subject: {assunto}\n\n{corpo}".encode("utf-8")
        
        smtp.sendmail(
            "email do remetente", 
            "email do destinatario", 
            mensagem
        )
        print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail isolado: {e}")