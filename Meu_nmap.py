import nmap
import time
import threading
from colorama import Fore, Style, init
init(autoreset=True)
print(Fore.GREEN + r"""
          _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \                /::\____\                /::\____\        
       /::::\    \              /::::\    \              /::::\    \              /::::|   |               /::::|   |        
      /::::::\    \            /::::::\    \            /::::::\    \            /:::::|   |              /:::::|   |        
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \          /::::::|   |             /::::::|   |        
    /:::/__\:::\    \        /:::/  \:::\    \        /:::/__\:::\    \        /:::/|::|   |            /:::/|::|   |        
    \:::\   \:::\    \      /:::/    \:::\    \      /::::\   \:::\    \      /:::/ |::|   |           /:::/ |::|   |        
  ___\:::\   \:::\    \    /:::/    / \:::\    \    /::::::\   \:::\    \    /:::/  |::|   | _____    /:::/  |::|   | _____  
 /\   \:::\   \:::\    \  /:::/    /   \:::\    \  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \  /:::/   |::|   |/\    \ 
/::\   \:::\   \:::\____\/:::/____/     \:::\____\/:::/  \:::\   \:::\____\/:: /    |::|   /::\____\/:: /    |::|   /::\____\
\:::\   \:::\   \::/    /\:::\    \      \::/    /\::/    \:::\  /:::/    /\::/    /|::|  /:::/    /\::/    /|::|  /:::/    /
 \:::\   \:::\   \/____/  \:::\    \      \/____/  \/____/ \:::\/:::/    /  \/____/ |::| /:::/    /  \/____/ |::| /:::/    / 
  \:::\   \:::\    \       \:::\    \                       \::::::/    /           |::|/:::/    /           |::|/:::/    /  
   \:::\   \:::\____\       \:::\    \                       \::::/    /            |::::::/    /            |::::::/    /   
    \:::\  /:::/    /        \:::\    \                      /:::/    /             |:::::/    /             |:::::/    /    
     \:::\/:::/    /          \:::\    \                    /:::/    /              |::::/    /              |::::/    /     
      \::::::/    /            \:::\    \                  /:::/    /               /:::/    /               /:::/    /      
       \::::/    /              \:::\____\                /:::/    /               /:::/    /               /:::/    /       
        \::/    /                \::/    /                \::/    /                \::/    /                \::/    /        
         \/____/                  \/____/                  \/____/                  \/____/                  \/____/         
""")


scanner = nmap.PortScanner()


def mostrar_ajuda_nmap():
    print("""
Comandos Nmap úteis:
────────────────────
-sS.............→ Scan TCP SYN (rápido e silencioso)
-sT.............→ Scan TCP Connect (completo)
-sU.............→ Scan UDP
-sV.............→ Detectar versão dos serviços
-O..............→ Detectar sistema operacional
-Pn ............→ Ignorar ping (escanear hosts mesmo offline)
-T0 a T5........→ Ajuste de velocidade (T0 = stealth, T5 = rápido)
-p..............→ Especificar portas (ex: -p 22,80,443 ou -p 1-65535)
--top-ports <N> → Scaneia as N portas mais comuns
-F..............→ Scan rápido (top 100 portas)
-A..............→ Ativa detecção de SO, versão, script scanning e traceroute
--exclude-ports → Excluir portas
────────────────────────────────────
PARA MAIS COMANDOS ACESSE O LINK : https://nmap.org/book/port-scanning-options.html
────────────────────────────────────
Exemplo de uso completo:
nmap -sS -p 22,80 -T4 -A 192.168.0.1
────────────────────────────────────
""")
def mostrar_tempo():
        tempo = 0
        while escaneando: 
            mins, segs, = divmod(tempo, 60)
            tempo_formatado = f"{mins:02}:{segs:02}"
            print(f"\rTempo decorrido : {tempo_formatado}", end="")
            time.sleep(1)
            tempo += 1

while True:
    print("==== Caixa de Ferramentas:", Fore.CYAN + "Módulo Nmap","====")
    
    print(Fore.YELLOW + "[1] Mostrar ajuda (comandos do Nmap)")
    print(Fore.YELLOW + "[2] Realizar escaneamento personalizado")
    print(Fore.YELLOW + "[0] Sair")
    opcao = input("insira uma opção : ")
   
    
    if opcao == "1":
        mostrar_ajuda_nmap()
    elif opcao == "2":
        parametros = input("Digite os parâmetros do Nmap (ex: -sS -p 1-1000 -T4): ")
        ip = input("Digite o IP ou o dominio a ser escaneado: ")

        print(f"Escaneando {ip} com os seguintes parametros [{parametros}]")

        escaneando = True
        t = threading.Thread(target= mostrar_tempo) 
        t.start()
        scanner.scan(hosts= ip, arguments=parametros)

        escaneando = False
        t.join()
        print(Fore.GREEN + "\nEscaneamento finalizado!\n")

        print(Fore.GREEN + "\nHosts vivos encontrados:")
        for host in scanner.all_hosts():
            print(f"\nHost: {host}")
            print(f"Estado: {scanner[host].state()}")

            for proto in scanner[host].all_protocols():
                print(f"\nProtocolo: {proto}")
                portas = scanner[host][proto].keys()
                for porta in sorted(portas):
                    info = scanner[host][proto][porta]
                    estado = info['state']
                    service = info.get('name', '')
                    product = info.get('product', '')
                    version = info.get('version', '')
                    extrainfo = info.get('extrainfo', '')

                    print(f"Porta {porta}: {estado} | Serviço: {service} {product} {version} {extrainfo}")

            # Mostrar sistemas operacionais se disponíveis
            if 'osmatch' in scanner[host]:
                print("\nPossíveis sistemas operacionais detectados:")
                for os in scanner[host]['osmatch']:
                    print(f"- {os['name']} ({os['accuracy']}% de precisão)")

        input(Fore.YELLOW + "\nPressione Enter para voltar ao menu...")

        input(Fore.YELLOW + "\nPressione Enter para voltar ao menu...")
    elif opcao == "0":
        print(Fore.RED + "Saindo...")
        break
    else:
        print(Fore.RED + "opção invalida. ")