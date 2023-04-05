from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueueRequest(_message.Message):
    __slots__ = ["key", "queue_name"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    key: str
    queue_name: str
    def __init__(self, key: _Optional[str] = ..., queue_name: _Optional[str] = ...) -> None: ...

class QueueRequestMessage(_message.Message):
    __slots__ = ["key", "message", "queue_name"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    key: str
    message: str
    queue_name: str
    def __init__(self, key: _Optional[str] = ..., queue_name: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class QueueResponse(_message.Message):
    __slots__ = ["code"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: int
    def __init__(self, code: _Optional[int] = ...) -> None: ...

class QueueResponseList(_message.Message):
    __slots__ = ["code", "queues"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUEUES_FIELD_NUMBER: _ClassVar[int]
    code: int
    queues: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, code: _Optional[int] = ..., queues: _Optional[_Iterable[str]] = ...) -> None: ...

class QueueResponseMessage(_message.Message):
    __slots__ = ["code", "message"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class TopicRequest(_message.Message):
    __slots__ = ["key", "topic_name"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    key: str
    topic_name: str
    def __init__(self, key: _Optional[str] = ..., topic_name: _Optional[str] = ...) -> None: ...

class TopicRequestMessage(_message.Message):
    __slots__ = ["key", "message", "topic_name"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    key: str
    message: str
    topic_name: str
    def __init__(self, key: _Optional[str] = ..., topic_name: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class TopicResponse(_message.Message):
    __slots__ = ["code"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: int
    def __init__(self, code: _Optional[int] = ...) -> None: ...

class TopicResponseList(_message.Message):
    __slots__ = ["code", "topics"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    code: int
    topics: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, code: _Optional[int] = ..., topics: _Optional[_Iterable[str]] = ...) -> None: ...

class TopicResponseMessage(_message.Message):
    __slots__ = ["code", "message"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...
