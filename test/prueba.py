import os
import sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from models.users import User
from models.topics import Topic
from models.queues import Queue

def main():
    #usuario = User('myid')
    #topic = Topic(name="New Topic", user_id='myid')
    #queue = Queue(name="New Queue", user_id='myid')
    #topic.save()
    #queue.save()
    top = Topic.get_by_id(1)
    print(top.name)
    top.delete()

main()

