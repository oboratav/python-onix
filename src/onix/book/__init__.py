# nothing here
import lxml
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler

from . import v2_1, v3_0, v3_1

namespace_map = {
    "http://www.editeur.org/onix/2.1/short": v2_1.short.Onixmessage,
    "http://www.editeur.org/onix/2.1/reference": v2_1.reference.Onixmessage,
    "http://ns.editeur.org/onix/3.0/reference": v3_0.reference.Onixmessage,
    "http://ns.editeur.org/onix/3.0/short": v3_0.short.Onixmessage,
    "http://ns.editeur.org/onix/3.1/reference": v3_1.reference.Onixmessage,
    "http://ns.editeur.org/onix/3.1/short": v3_1.short.Onixmessage,
}


def parse_onix_message(message):
    parser = XmlParser(handler=LxmlEventHandler)
    msg = lxml.etree.parse(message)
    ns = msg.getroot().nsmap.get(None)
    return parser.parse(msg, namespace_map.get(ns))
