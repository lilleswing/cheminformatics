# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import generativesampler_pb2 as generativesampler__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class GenerativeSamplerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SmilesToEmbedding = channel.unary_unary(
                '/nvidia.cheminformatics.grpc.GenerativeSampler/SmilesToEmbedding',
                request_serializer=generativesampler__pb2.GenerativeSpec.SerializeToString,
                response_deserializer=generativesampler__pb2.EmbeddingList.FromString,
                )
        self.FindSimilars = channel.unary_unary(
                '/nvidia.cheminformatics.grpc.GenerativeSampler/FindSimilars',
                request_serializer=generativesampler__pb2.GenerativeSpec.SerializeToString,
                response_deserializer=generativesampler__pb2.SmilesList.FromString,
                )
        self.Interpolate = channel.unary_unary(
                '/nvidia.cheminformatics.grpc.GenerativeSampler/Interpolate',
                request_serializer=generativesampler__pb2.GenerativeSpec.SerializeToString,
                response_deserializer=generativesampler__pb2.SmilesList.FromString,
                )
        self.GetIteration = channel.unary_unary(
                '/nvidia.cheminformatics.grpc.GenerativeSampler/GetIteration',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=generativesampler__pb2.IterationVal.FromString,
                )


class GenerativeSamplerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SmilesToEmbedding(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindSimilars(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Interpolate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIteration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GenerativeSamplerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SmilesToEmbedding': grpc.unary_unary_rpc_method_handler(
                    servicer.SmilesToEmbedding,
                    request_deserializer=generativesampler__pb2.GenerativeSpec.FromString,
                    response_serializer=generativesampler__pb2.EmbeddingList.SerializeToString,
            ),
            'FindSimilars': grpc.unary_unary_rpc_method_handler(
                    servicer.FindSimilars,
                    request_deserializer=generativesampler__pb2.GenerativeSpec.FromString,
                    response_serializer=generativesampler__pb2.SmilesList.SerializeToString,
            ),
            'Interpolate': grpc.unary_unary_rpc_method_handler(
                    servicer.Interpolate,
                    request_deserializer=generativesampler__pb2.GenerativeSpec.FromString,
                    response_serializer=generativesampler__pb2.SmilesList.SerializeToString,
            ),
            'GetIteration': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIteration,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=generativesampler__pb2.IterationVal.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nvidia.cheminformatics.grpc.GenerativeSampler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GenerativeSampler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SmilesToEmbedding(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nvidia.cheminformatics.grpc.GenerativeSampler/SmilesToEmbedding',
            generativesampler__pb2.GenerativeSpec.SerializeToString,
            generativesampler__pb2.EmbeddingList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindSimilars(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nvidia.cheminformatics.grpc.GenerativeSampler/FindSimilars',
            generativesampler__pb2.GenerativeSpec.SerializeToString,
            generativesampler__pb2.SmilesList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Interpolate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nvidia.cheminformatics.grpc.GenerativeSampler/Interpolate',
            generativesampler__pb2.GenerativeSpec.SerializeToString,
            generativesampler__pb2.SmilesList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIteration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nvidia.cheminformatics.grpc.GenerativeSampler/GetIteration',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            generativesampler__pb2.IterationVal.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
