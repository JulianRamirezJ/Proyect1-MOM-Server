from chasqui import ChasquiConnector
#Owner:0rncpasade
#Suscribers:'4jqa06l7yf' - 'o27709melz'
def main():
    conn = ChasquiConnector('localhost','5000','0rncpasade')
    #conn.subscribe_topic('prueba')
    #conn.consume_message_topic('prueba', True)
    conn.publish_message_topic('prueba','Hola a todos Prueba retry')
main()

