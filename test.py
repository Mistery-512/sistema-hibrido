import smtplib

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login("email do remetente", "codigo google")
        smtp.sendmail(
            "emeil do remetente",
            "email do destinatario",
            "Subject: Teste\n\nEste é um e-mail de teste."
        )
        print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail isolado: {e}")
