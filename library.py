import os

PAGESIZE = 8192
HEADERSIZE = 96


def print_list(items):
    print('\n'.join(map(str, items)))

def list_files(path = '.', extension = ''):
    if extension == '.*':
        extension = ''
    items = os.listdir(path)
    files = []
    for name in items:
        if name.lower().endswith(extension.lower()):
            files.append(name)            
    print_list(files)

def file_exists(path):
    return os.path.isfile(path)

def file_size(path):
    return os.path.getsize(path)


page_header_layout = '''

    Bytes	Content
    -----	-------
    00		HeaderVersion (tinyint)
    01		Type (tinyint)
    02		TypeFlagBits (tinyint)
    03		Level (tinyint)
    04-05	FlagBits (smallint)
    06-07	IndexID (smallint)
    08-11	PreviousPageID (int)
    12-13	PreviousFileID (smallint)
    14-15	Pminlen (smallint)
    16-19	NextPageID (int)
    20-21	NextPageFileID (smallint)
    22-23	SlotCnt (smallint)
    24-27	ObjectID (int)
    28-29	FreeCnt (smallint)
    30-31	FreeData (smallint)
    32-35	PageID (int)
    36-37	FileID (smallint)
    38-39	ReservedCnt (smallint)
    40-43	Lsn1 (int)
    44-47	Lsn2 (int)
    48-49	Lsn3 (smallint)
    50-51	XactReserved (smallint)
    52-55	XdesIDPart2 (int)
    56-57	XdesIDPart1 (smallint)
    58-59	GhostRecCnt (smallint)
    60-63	Checksum/Tornbits (int)
    64-95	?
    ======================================
    bigint	8 Bytes
    int         4 Bytes
    smallint	2 Bytes
    tinyint 	1 Byte
'''

#=============================================================================================
import sys
import inspect

def get_size(obj, seen=None):
    """Recursively finds size of objects in bytes"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if hasattr(obj, '__dict__'):
        for cls in obj.__class__.__mro__:
            if '__dict__' in cls.__dict__:
                d = cls.__dict__['__dict__']
                if inspect.isgetsetdescriptor(d) or inspect.ismemberdescriptor(d):
                    size += get_size(obj.__dict__, seen)
                break
    if isinstance(obj, dict):
        size += sum((get_size(v, seen) for v in obj.values()))
        size += sum((get_size(k, seen) for k in obj.keys()))
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum((get_size(i, seen) for i in obj))
        
    if hasattr(obj, '__slots__'): # can have __slots__ with __dict__
        size += sum(get_size(getattr(obj, s), seen) for s in obj.__slots__ if hasattr(obj, s))
        
    return size
#=============================================================================================

from datetime import datetime as dt

timestamp = lambda: dt.now().strftime("%Y-%m-%d_%H-%M-%S.%f")

#=============================================================================================

def reflect(some_object):
    property_names = vars(__builtins__)
    properties = [vars(__builtins__)[name] for name in property_names]
    return property_names, properties
