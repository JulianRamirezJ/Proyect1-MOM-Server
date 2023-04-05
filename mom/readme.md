### Libraries grpc
python3 -m pip install --upgrade pip
python -m pip install grpcio
python -m pip install grpcio-tools

### Generate code
python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. config.proto