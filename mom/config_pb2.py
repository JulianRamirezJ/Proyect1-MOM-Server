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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63onfig.proto\"/\n\x0cTopicRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\ntopic_name\x18\x02 \x01(\t\"\x1d\n\rTopicResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\"1\n\x11TopicResponseList\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\x12\x0e\n\x06topics\x18\x02 \x03(\t\"G\n\x13TopicRequestMessage\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\ntopic_name\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"5\n\x14TopicResponseMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\x12\x0f\n\x07message\x18\x02 \x01(\t\"/\n\x0cQueueRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\nqueue_name\x18\x02 \x01(\t\"\x1d\n\rQueueResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\"1\n\x11QueueResponseList\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\x12\x0e\n\x06queues\x18\x02 \x03(\t\"G\n\x13QueueRequestMessage\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\nqueue_name\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"5\n\x14QueueResponseMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x11\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2\xb3\x02\n\x0cTopicService\x12)\n\x06\x63reate\x12\r.TopicRequest\x1a\x0e.TopicResponse\"\x00\x12)\n\x06\x64\x65lete\x12\r.TopicRequest\x1a\x0e.TopicResponse\"\x00\x12*\n\nlistTopics\x12\x06.Empty\x1a\x12.TopicResponseList\"\x00\x12\x31\n\x0esubscribeTopic\x12\r.TopicRequest\x1a\x0e.TopicResponse\"\x00\x12\x36\n\x0cpublishTopic\x12\x14.TopicRequestMessage\x1a\x0e.TopicResponse\"\x00\x12\x36\n\x0c\x63onsumeTopic\x12\r.TopicRequest\x1a\x15.TopicResponseMessage\"\x00\x32\xb3\x02\n\x0cQueueService\x12)\n\x06\x63reate\x12\r.QueueRequest\x1a\x0e.QueueResponse\"\x00\x12)\n\x06\x64\x65lete\x12\r.QueueRequest\x1a\x0e.QueueResponse\"\x00\x12*\n\nlistQueues\x12\x06.Empty\x1a\x12.QueueResponseList\"\x00\x12\x31\n\x0esubscribeQueue\x12\r.QueueRequest\x1a\x0e.QueueResponse\"\x00\x12\x36\n\x0cpublishQueue\x12\x14.QueueRequestMessage\x1a\x0e.QueueResponse\"\x00\x12\x36\n\x0c\x63onsumeQueue\x12\r.QueueRequest\x1a\x15.QueueResponseMessage\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TOPICREQUEST._serialized_start=16
  _TOPICREQUEST._serialized_end=63
  _TOPICRESPONSE._serialized_start=65
  _TOPICRESPONSE._serialized_end=94
  _TOPICRESPONSELIST._serialized_start=96
  _TOPICRESPONSELIST._serialized_end=145
  _TOPICREQUESTMESSAGE._serialized_start=147
  _TOPICREQUESTMESSAGE._serialized_end=218
  _TOPICRESPONSEMESSAGE._serialized_start=220
  _TOPICRESPONSEMESSAGE._serialized_end=273
  _QUEUEREQUEST._serialized_start=275
  _QUEUEREQUEST._serialized_end=322
  _QUEUERESPONSE._serialized_start=324
  _QUEUERESPONSE._serialized_end=353
  _QUEUERESPONSELIST._serialized_start=355
  _QUEUERESPONSELIST._serialized_end=404
  _QUEUEREQUESTMESSAGE._serialized_start=406
  _QUEUEREQUESTMESSAGE._serialized_end=477
  _QUEUERESPONSEMESSAGE._serialized_start=479
  _QUEUERESPONSEMESSAGE._serialized_end=532
  _EMPTY._serialized_start=534
  _EMPTY._serialized_end=541
  _TOPICSERVICE._serialized_start=544
  _TOPICSERVICE._serialized_end=851
  _QUEUESERVICE._serialized_start=854
  _QUEUESERVICE._serialized_end=1161
# @@protoc_insertion_point(module_scope)
