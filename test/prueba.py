import os
import sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from models.users import UserModel
from models.topics import TopicModel
from models.queues import QueueModel
from models.messages_topic import MessageTopicModel
from models.messages_queue import MessageQueueModel

user_names = ['u1','u2','u3','u4','u5']
users = []

def main():
    #users = UserModel.get_all_users()

    # onlyQueues = QueueModel.get_all_queues()
    # for queue in onlyQueues:
    #     newQueue = QueueModel(queue[1],queue[2],queue[0])
    #     print(newQueue.id)
    #     subscribers = newQueue.get_all_suscribed_users()
    #     for subscriber in subscribers:
    #         print(subscriber[0])
    #     messages = MessageQueueModel.get_all_messages_from_queue(newQueue.name)
    #     print(messages)
    #     for message in messages:
    #         print(not message[2])

    # queue = QueueModel.get_by_name('queue2')
    # print(queue.id)

    topics_bd = TopicModel.get_all_topics()
    for topic in topics_bd:
        print(topic)
        newTopic = TopicModel(topic[1],topic[2],topic[0])
        topics_queue_bd = newTopic.get_all_suscribed_users()
        for topic_queue in topics_queue_bd:
            print(topic_queue,'topic_queue')
            messages_topic_bd = MessageTopicModel.get_all_messages_from_topic_queue_not_read(topic_queue[0])
            for message in messages_topic_bd:
                print(message)
    # for user in user_names:
    #     u = User(user)
    #     u.save()
    #     users.append(u)

    # queue_names = [['topic1',users[0].get_id()],['topic2',users[4].get_id()]]
    # queues = []

    # for queue in queue_names: 
    #     t = Queue(queue[0],queue[1])
    #     t.save()
    #     queues.append(t)
    # users[2].desubscribe_queue(queues[0].get_name())
    # print(users[4].get_all_suscribed_queues())
    # print(queues[0].get_all_suscribed_users())
    # print(queues[0].user_is_subscribed(users[2].get_id()))
    # users[2].desubscribe_queue(queues[0].get_name())
    # print(queues[0].user_is_subscribed(users[2].get_id()))
    # #users[2].subscribe_queue(queues[0].get_name())
    # #print(t.user_is_subscribed(users[1].get_id()))
    # #print(users[1].get_all_suscribed_topics())
 
main()

