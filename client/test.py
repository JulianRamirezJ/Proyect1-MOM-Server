from chasqui import ChasquiConnector
#Owner:0rncpasade
#Suscribers:'4jqa06l7yf' - 'o27709melz'
def main():
    conn = ChasquiConnector('localhost','5000','4jqa06l7yf')
    #conn.subscribe_topic('prueba')
    print(conn.consume_message_topic('prueba', True))
    #conn.publish_message_topic('mytopic','Hola a todos Ahora si')
    
main()