'''
My custom JSON encoders and decoders.
'''

from decimal import Decimal

from json_extensions import ExtendedJsonEncoder, ExtendedJsonDecoder

class MyJsonEncoder(ExtendedJsonEncoder):
    ''' Custom JSON encoder that extends the base encoder to handle additional types
    where we don't control the source code.
    '''
    def encode_complex(self, c):
        ''' Encode a complex number as a JSON object with real and imaginary parts. '''
        return {"real": c.real, "imag": c.imag}

    def encode_range(self, r):
        ''' Encode a range object as a JSON object with start, stop, and step. '''
        return {"start": r.start, "stop": r.stop, "step": r.step}

    def encode_Decimal(self, d): # pylint: disable=invalid-name
        ''' Encode a Decimal object as a JSON string. '''
        return {"value": str(d)}

class MyJsonDecoder(ExtendedJsonDecoder):
    ''' Custom JSON decoder that extends the base decoder to handle additional types
    where we don't control the source code. '''
    def decode_complex(self, obj):
        ''' Decode a JSON object into a complex number. '''
        return complex(obj["real"], obj["imag"])

    def decode_range(self, obj):
        ''' Decode a JSON object into a range object. '''
        return range(obj["start"], obj["stop"], obj["step"])

    def decode_Decimal(self, obj): # pylint: disable=invalid-name
        ''' Decode a JSON object into a Decimal object. '''
        return Decimal(obj["value"])
