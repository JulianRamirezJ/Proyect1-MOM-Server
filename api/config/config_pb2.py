# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63onfig.proto\"C\n\x0cTopicRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x17\n\ntopic_name\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\r\n\x0b_topic_name\"\x1d\n\rTopicResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\"1\n\x11TopicResponseList\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\x12\x0e\n\x06topics\x18\x02 \x03(\t\"G\n\x13TopicRequestMessage\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\ntopic_name\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"5\n\x14TopicResponseMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\x12\x0f\n\x07message\x18\x02 \x01(\t\"C\n\x0cQueueRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x17\n\nqueue_name\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\r\n\x0b_queue_name\"\x1d\n\rQueueResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\"1\n\x11QueueResponseList\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\x12\x0e\n\x06queues\x18\x02 \x03(\t\"G\n\x13QueueRequestMessage\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\nqueue_name\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"5\n\x14QueueResponseMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\x12\x0f\n\x07message\x18\x02 \x01(\t2\xba\x02\n\x0cTopicService\x12)\n\x06\x43reate\x12\r.TopicRequest\x1a\x0e.TopicResponse\"\x00\x12)\n\x06\x44\x65lete\x12\r.TopicRequest\x1a\x0e.TopicResponse\"\x00\x12\x31\n\nListTopics\x12\r.TopicRequest\x1a\x12.TopicResponseList\"\x00\x12\x31\n\x0eSubscribeTopic\x12\r.TopicRequest\x1a\x0e.TopicResponse\"\x00\x12\x36\n\x0cPublishTopic\x12\x14.TopicRequestMessage\x1a\x0e.TopicResponse\"\x00\x12\x36\n\x0c\x43onsumeTopic\x12\r.TopicRequest\x1a\x15.TopicResponseMessage\"\x00\x32\xba\x02\n\x0cQueueService\x12)\n\x06\x43reate\x12\r.QueueRequest\x1a\x0e.QueueResponse\"\x00\x12)\n\x06\x44\x65lete\x12\r.QueueRequest\x1a\x0e.QueueResponse\"\x00\x12\x31\n\nListQueues\x12\r.QueueRequest\x1a\x12.QueueResponseList\"\x00\x12\x31\n\x0eSubscribeQueue\x12\r.QueueRequest\x1a\x0e.QueueResponse\"\x00\x12\x36\n\x0cPublishQueue\x12\x14.QueueRequestMessage\x1a\x0e.QueueResponse\"\x00\x12\x36\n\x0c\x43onsumeQueue\x12\r.QueueRequest\x1a\x15.QueueResponseMessage\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TOPICREQUEST._serialized_start=16
  _TOPICREQUEST._serialized_end=83
  _TOPICRESPONSE._serialized_start=85
  _TOPICRESPONSE._serialized_end=114
  _TOPICRESPONSELIST._serialized_start=116
  _TOPICRESPONSELIST._serialized_end=165
  _TOPICREQUESTMESSAGE._serialized_start=167
  _TOPICREQUESTMESSAGE._serialized_end=238
  _TOPICRESPONSEMESSAGE._serialized_start=240
  _TOPICRESPONSEMESSAGE._serialized_end=293
  _QUEUEREQUEST._serialized_start=295
  _QUEUEREQUEST._serialized_end=362
  _QUEUERESPONSE._serialized_start=364
  _QUEUERESPONSE._serialized_end=393
  _QUEUERESPONSELIST._serialized_start=395
  _QUEUERESPONSELIST._serialized_end=444
  _QUEUEREQUESTMESSAGE._serialized_start=446
  _QUEUEREQUESTMESSAGE._serialized_end=517
  _QUEUERESPONSEMESSAGE._serialized_start=519
  _QUEUERESPONSEMESSAGE._serialized_end=572
  _TOPICSERVICE._serialized_start=575
  _TOPICSERVICE._serialized_end=889
  _QUEUESERVICE._serialized_start=892
  _QUEUESERVICE._serialized_end=1206
# @@protoc_insertion_point(module_scope)