import os
import sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from models.users import User
from models.topics import Topic
from models.queues import Queue
from models.messages_topic import MessageTopic
from models.messages_queue import MessageQueue

user_names = ['u1','u2','u3','u4','u5']
users = []

def main():
    
    for user in user_names:
        u = User(user)
        u.save()
        users.append(u)

    queue_names = [['topic1',users[0].get_id()],['topic2',users[4].get_id()]]
    queues = []

    for queue in queue_names: 
        t = Queue(queue[0],queue[1])
        t.save()
        queues.append(t)
    users[2].desubscribe_queue(queues[0].get_name())
    print(users[4].get_all_suscribed_queues())
    print(queues[0].get_all_suscribed_users())
    print(queues[0].user_is_subscribed(users[2].get_id()))
    users[2].desubscribe_queue(queues[0].get_name())
    print(queues[0].user_is_subscribed(users[2].get_id()))
    #users[2].subscribe_queue(queues[0].get_name())
    #print(t.user_is_subscribed(users[1].get_id()))
    #print(users[1].get_all_suscribed_topics())
 
main()

