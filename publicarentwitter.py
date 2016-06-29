#!/usr/bin/python
# coding: latin-1

'''
Programa para
author: el3ctron
website: http://el3ctron.github.io/
last edited: Final del mundo
'''

import sys, os
import time
import PyZenity
import tweepy

## https://apps.twitter.com/

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

'''
## modulo para autenticar
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret
'''

ACCESS_KEY = ''
ACCESS_SECRET = ''

key=CONSUMER_KEY
secret=CONSUMER_SECRET
token=ACCESS_KEY
token_secret=ACCESS_SECRET

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
client = tweepy.API(auth)

arr=[]
def twittadd():
    print ""
    print "                                                      [ORD3N4 TU T3XT0 QU3R1D0 El3CTR0N]"
    print ""
    print "              ...la vida es solo un sueño, un el3ctron es compuesto por quarks compuestos de energía que está compuesta de nada...    140 carácteres! ---->|"
    twitt = raw_input("Ingresar twitt: ")
    arr.append(twitt)
    if len(twitt) == 0:
        print "Digita algo dentro del campo"
        twittadd()
    if len(twitt) > 141:
        print "el twitt es mayor a 140 carácteres, se pega en el buffer ppal y se procede a publicar en wordpress"
        msgs=arr[0]
        buff = '''dbus-send --type=method_call --dest=org.kde.klipper     /klipper org.kde.klipper.klipper.setClipboardContents string:"'''+msgs+'''"'''
        ##         print buff
        os.system( buff )
        wordd="/opt/mis_scripts/8txt2wordpresscomotwitt "+'"'+twitt+'"'
        os.system( wordd )
    if len(twitt) < 141:
        msgs=arr[0]
        client.update_status(msgs)





# Verificación de parámetros para el programa 8txt2twitter


aviso = '''

        No hay parámetros!
        Al portapales el comando --> 8txt2twitter --help

        '''

def imprimir() :
    """Esta funcion imprime los parametros en pantalla"""
    print aviso

if len(sys.argv) == 1:
##     imprimir()
    catcat="44bufferOnKlipper 8txt2twitter --help"
##     os.system(catcat)
    twittadd()
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':
        print 'Version 0.1'
    elif option == 'help':
        print '''\


            #########################################
            El programa 8txt2twitter está encargado de subir estados a twitter
            #########################################

            El modo de uso es:

8txt2twitter [ post ]

            Las opciones son:
            --version : Imprime la versión del programa
            --help    : Muestra esta ayuda

            '''
        sys.exit()
    else:
        print 'Opción desconocida'
        sys.exit()
    sys.exit()

if len(sys.argv) > 1:
    cadena=" ".join(sys.argv[1:])
    print cadena
    if len(cadena) > 141:
        longi=len(cadena)
        longi=str(longi)
        print "el twitt tiene "+longi+" carácteres, se pega en el buffer ppal"
        msgs=cadena
        buff = '''dbus-send --type=method_call --dest=org.kde.klipper     /klipper org.kde.klipper.klipper.setClipboardContents string:"8txt2twitter '''+msgs+'''"'''
        ##         print buff
        os.system( buff )
    if len(cadena) < 141:
        msgs=cadena
        client.update_status(msgs)
print '''
                #########################################
                Estado de twitter actualizado
                #########################################
'''


sys.exit()


import twitter
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
print api.VerifyCredentials()
statuses = api.GetUserTimeline(screen_name="ultraviolentica")
print [s.text for s in statuses]
users = api.GetFriends()
users = api.GetFriends()
print [u.name for u in users]
users = api.GetRetweetsOfMe()
print [u.name for u in users]
