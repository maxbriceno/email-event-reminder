import click
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Percorso fisso al file HTML del template
TEMPLATE_PATH = "mailto_event_reminder.html"
email_domain = "emotion-team.com"

destinatari = [
    # f"giacomo.fiorucci@{email_domain}",
    # f"kevin.bodan@{email_domain}",
    # f"c.calcagni@{email_domain}",
    # f"christopher.caponi@{email_domain}",
    # f"filippo.mariani@{email_domain}",
    # f"giulio.cassano@{email_domain}",
    # f"francesco.bellesini@{email_domain}",
    # f"e.mancinelli@{email_domain}",
    f"massimo.briceno@{email_domain}",
]

SMTP_SERVER = "smtps.aruba.it"
SMTP_PORT = 465

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# CLI con Click
@click.command()
@click.option('--data', '-de', prompt="Inserisci la data dell'evento", help="Data dell'evento (es. '30 gennaio 2025')")
@click.option('--ora', '-o', prompt="Inserisci l'ora dell'evento", help="Ora dell'evento (es. '10:00')")
@click.option('--number', '-n', type=int,  prompt="Inserisci il numero dello Sprint", help="# Sprint (es. '48')")
def cli(data, ora, number):
    send_email(destinatari, data, ora, number)

def send_email(destinatari, data, ora, number):
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as file:
        template = file.read().strip()

    mailto_conferma = f"mailto:massimo.briceno@emotion-team.com?subject=Conferma%20Partecipazione%20#%20{number}%20-%20{data}%20ora%20{ora}&body=Confermo%20la%20mia%20partecipazione%20alla%20riunione%20del%20{data}%20ora%20{ora}"
    mailto_rifiuto = f"mailto:massimo.briceno@emotion-team.com?subject=Rifiuto%20Partecipazione%20#%20{number}%20-%20{data}%20ora%20{ora}&body=Non%20posso%20partecipare%20alla%20riunione%20del%20{data}%20ora%20{ora}"

    try:
        email_body = template.replace("[data_riunione]", data)
        email_body = email_body.replace("[ora_riunione]", ora)
        email_body = email_body.replace("[mailto_conferma]", mailto_conferma)
        email_body = email_body.replace("[mailto_rifiuto]", mailto_rifiuto)
    except KeyError as e:
        print(f"Errore nella formattazione: {e}")
        raise

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Invito Sprint Review # {number} - {data} ore {ora}"
    msg["From"] = EMAIL
    msg["To"] = ", ".join(destinatari)

    part = MIMEText(email_body, "html")
    msg.attach(part)

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, destinatari, msg.as_string())
        click.echo("Email inviata con successo!")
    except Exception as e:
        click.echo(f"Errore durante l'invio dell'email: {e}")


if __name__ == "__main__":
    cli()
