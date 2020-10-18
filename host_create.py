# ***
# AUTOMATIZANDO CRIAÇÃO DE HOSTS
# by KessiDiones
#
# 
# ***

'''
INSTALANDO O PIP3 E A API DO ZABBIX
$ sudo apt install python3-pip
$ sudo pip3 install zabbix-api-erigones
'''

from zabbix_api import ZabbixAPI

URL = 'ip/zabbix'
USERNAME = 'user'
PASSWORD = 'password'
try:
    zapi = ZabbixAPI(URL, timeout=15)
    zapi.login(USERNAME,PASSWORD)
    # print(zapi.api_version()) Imprime a versão da API do Zabbix
    print(f'Conectado na API do Zabbix versão {zapi.api_version()}')
except Exception as err:
    print(f'Falha ao conectar na API do Zabbix, erro: {err}')

'''
Possible values are:
1 - agent;
2 - SNMP;
3 - IPMI;
4 - JMX.
'''

# Grupo A
gid_A = ['10','20','30']
gids_A = [{"groupid": groupid} for groupid in gid_A]

# Grupo B
gid_B = ['40','50','60']
gids_B = [{"groupid": groupid} for groupid in gid_B]

''' Uso dicionário para pré definir alguns dados do host'''
info_interfaces = {
    "1": {"type": "agent", "id": "1", "port": 10050},
    "2": {"type": "SNMP", "id": "2", "port": 161}
}


def create_host(name, ip, groups, community):
    try:
        create_host = zapi.host.create({
            "groups": groups,
            "host": name,
            "interfaces": {
                "type": info_interfaces['2']['id'],
                "main": 1,
                "useip": 1,
                "ip": ip,
                "dns": "",
                "details": {
                        "version": 2,
                        "bulk": 1,
                        "community": community
                },
                "port": info_interfaces['2']['id']
            }

        })
        print(f'Host cadastrado com sucesso: {create_host}')
    except Exception as err:
        print(f'Falha ao cadastrar o host: erro {err}')
        
        
# Chamando a função para criação de um host
create_host("HostA", "192.168.10.1", gid_A, "public")
create_host("HostB", "192.168.10.1", gid_B, "public")
