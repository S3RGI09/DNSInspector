import dns.resolver
import socket

print("-DNS Inspector- | By S3RGI09")

def get_dns_info(domain):
    dns_info = {}

    try:
        answers = dns.resolver.resolve(domain, 'A')
        dns_info['A'] = [str(answer) for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        dns_info['A'] = []

    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        dns_info['AAAA'] = [str(answer) for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        dns_info['AAAA'] = []

    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        dns_info['CNAME'] = [str(answer) for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        dns_info['CNAME'] = []

    try:
        answers = dns.resolver.resolve(domain, 'MX')
        dns_info['MX'] = [(str(answer.preference), str(answer.exchange)) for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        dns_info['MX'] = []

    try:
        answers = dns.resolver.resolve(domain, 'NS')
        dns_info['NS'] = [str(answer) for answer in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        dns_info['NS'] = []

    return dns_info

def main():
    domain = input("Introduce el dominio para recopilar información de DNS (ejemplo.com): ")
    
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Dirección IP de {domain}: {ip_address}")
    except socket.gaierror:
        print(f"No se pudo resolver el dominio: {domain}")
        return

    dns_info = get_dns_info(domain)

    print("\nInformación de DNS recopilada:")
    for record_type, records in dns_info.items():
        if records:
            print(f"{record_type} registros: {records}")
        else:
            print(f"{record_type} registros: No se encontraron.")

if __name__ == "__main__":
    main()
