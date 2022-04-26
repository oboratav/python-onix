from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Type

__NAMESPACE__ = "http://www.editeur.org/onix/2.1/reference"


class ADir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class AShape(Enum):
    RECT = "rect"
    CIRCLE = "circle"
    POLY = "poly"
    DEFAULT = "default"


class AbbrDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class AcronymDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class AddressDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class AreaDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class AreaNohref(Enum):
    NOHREF = "nohref"


class AreaShape(Enum):
    RECT = "rect"
    CIRCLE = "circle"
    POLY = "poly"
    DEFAULT = "default"


class BDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class BdoDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class BigDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class BlockquoteDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


@dataclass(slots=True)
class Br:
    class Meta:
        name = "br"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class CaptionDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class CiteDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class CodeDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class ColAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class ColDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class ColValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class ColgroupAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class ColgroupDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class ColgroupValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class DdDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class DfnDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class DivDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class DlDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class DtDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class EmDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class H1Dir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class H2Dir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class H3Dir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class H4Dir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class H5Dir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class H6Dir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class HrDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class IDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class ImgDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class ImgIsmap(Enum):
    ISMAP = "ismap"


class KbdDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class LiDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class MapDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class ObjectDeclare(Enum):
    DECLARE = "declare"


class ObjectDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class OlDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class PDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class ParamValuetype(Enum):
    DATA = "data"
    REF = "ref"
    OBJECT = "object"


class PreDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class QDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class SampDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class SmallDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class SpanDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class StrongDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class SubDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class SupDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class TableDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class TableFrame(Enum):
    VOID = "void"
    ABOVE = "above"
    BELOW = "below"
    HSIDES = "hsides"
    LHS = "lhs"
    RHS = "rhs"
    VSIDES = "vsides"
    BOX = "box"
    BORDER = "border"


class TableRules(Enum):
    NONE = "none"
    GROUPS = "groups"
    ROWS = "rows"
    COLS = "cols"
    ALL = "all"


class TbodyAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class TbodyDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class TbodyValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class TdAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class TdDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class TdScope(Enum):
    ROW = "row"
    COL = "col"
    ROWGROUP = "rowgroup"
    COLGROUP = "colgroup"


class TdValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class TfootAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class TfootDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class TfootValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class ThAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class ThDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class ThScope(Enum):
    ROW = "row"
    COL = "col"
    ROWGROUP = "rowgroup"
    COLGROUP = "colgroup"


class ThValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class TheadAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class TheadDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class TheadValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class TrAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class TrDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class TrValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class TtDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class UlDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class VarDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


@dataclass(slots=True)
class Area:
    class Meta:
        name = "area"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[AreaDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    shape: AreaShape = field(
        default=AreaShape.RECT,
        metadata={
            "type": "Attribute",
        }
    )
    coords: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nohref: Optional[AreaNohref] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(slots=True)
class Col:
    class Meta:
        name = "col"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[ColDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    span: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[ColAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[ColValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Hr:
    class Meta:
        name = "hr"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[HrDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Img:
    class Meta:
        name = "img"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[ImgDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    longdesc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    usemap: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ismap: Optional[ImgIsmap] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Ol:
    class Meta:
        name = "ol"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    li: List["Li"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[OlDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Param:
    class Meta:
        name = "param"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valuetype: ParamValuetype = field(
        default=ParamValuetype.DATA,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Acronym:
    class Meta:
        name = "acronym"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[AcronymDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                },
                {
                    "name": "q",
                    "type": Type["Q"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                },
                {
                    "name": "samp",
                    "type": Type["Samp"],
                },
                {
                    "name": "kbd",
                    "type": Type["Kbd"],
                },
                {
                    "name": "var",
                    "type": Type["Var"],
                },
                {
                    "name": "cite",
                    "type": Type["Cite"],
                },
                {
                    "name": "abbr",
                    "type": Type["Abbr"],
                },
                {
                    "name": "acronym",
                    "type": Type["Acronym"],
                },
            ),
        }
    )


@dataclass(slots=True)
class Colgroup:
    class Meta:
        name = "colgroup"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    col: List[Col] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[ColgroupDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    span: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[ColgroupAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[ColgroupValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Abbr:
    class Meta:
        name = "abbr"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[AbbrDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                },
                {
                    "name": "q",
                    "type": Type["Q"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                },
                {
                    "name": "samp",
                    "type": Type["Samp"],
                },
                {
                    "name": "kbd",
                    "type": Type["Kbd"],
                },
                {
                    "name": "var",
                    "type": Type["Var"],
                },
                {
                    "name": "cite",
                    "type": Type["Cite"],
                },
                {
                    "name": "abbr",
                    "type": Type["Abbr"],
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Cite:
    class Meta:
        name = "cite"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[CiteDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                },
                {
                    "name": "q",
                    "type": Type["Q"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                },
                {
                    "name": "samp",
                    "type": Type["Samp"],
                },
                {
                    "name": "kbd",
                    "type": Type["Kbd"],
                },
                {
                    "name": "var",
                    "type": Type["Var"],
                },
                {
                    "name": "cite",
                    "type": Type["Cite"],
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Var:
    class Meta:
        name = "var"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[VarDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                },
                {
                    "name": "q",
                    "type": Type["Q"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                },
                {
                    "name": "samp",
                    "type": Type["Samp"],
                },
                {
                    "name": "kbd",
                    "type": Type["Kbd"],
                },
                {
                    "name": "var",
                    "type": Type["Var"],
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Kbd:
    class Meta:
        name = "kbd"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[KbdDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                },
                {
                    "name": "q",
                    "type": Type["Q"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                },
                {
                    "name": "samp",
                    "type": Type["Samp"],
                },
                {
                    "name": "kbd",
                    "type": Type["Kbd"],
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Samp:
    class Meta:
        name = "samp"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[SampDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                },
                {
                    "name": "q",
                    "type": Type["Q"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                },
                {
                    "name": "samp",
                    "type": Type["Samp"],
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Sup:
    class Meta:
        name = "sup"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[SupDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                },
                {
                    "name": "q",
                    "type": Type["Q"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Sub:
    class Meta:
        name = "sub"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[SubDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                },
                {
                    "name": "q",
                    "type": Type["Q"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Q:
    class Meta:
        name = "q"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[QDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                },
                {
                    "name": "q",
                    "type": Type["Q"],
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Code:
    class Meta:
        name = "code"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[CodeDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Dfn:
    class Meta:
        name = "dfn"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[DfnDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Strong:
    class Meta:
        name = "strong"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[StrongDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Em:
    class Meta:
        name = "em"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[EmDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Small:
    class Meta:
        name = "small"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[SmallDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Big:
    class Meta:
        name = "big"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[BigDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class B:
    class Meta:
        name = "b"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[BDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class I:
    class Meta:
        name = "i"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[IDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Tt:
    class Meta:
        name = "tt"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[TtDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Address:
    class Meta:
        name = "address"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[AddressDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Caption:
    class Meta:
        name = "caption"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[CaptionDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Dt:
    class Meta:
        name = "dt"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[DtDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class H1:
    class Meta:
        name = "h1"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[H1Dir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class H2:
    class Meta:
        name = "h2"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[H2Dir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class H3:
    class Meta:
        name = "h3"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[H3Dir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class H4:
    class Meta:
        name = "h4"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[H4Dir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class H5:
    class Meta:
        name = "h5"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[H5Dir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class H6:
    class Meta:
        name = "h6"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[H6Dir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Pre:
    class Meta:
        name = "pre"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[PreDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Td:
    class Meta:
        name = "td"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[TdDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    abbr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    axis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    headers: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: Optional[TdScope] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[TdAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[TdValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "p",
                    "type": Type["P"],
                },
                {
                    "name": "h1",
                    "type": H1,
                },
                {
                    "name": "h2",
                    "type": H2,
                },
                {
                    "name": "h3",
                    "type": H3,
                },
                {
                    "name": "h4",
                    "type": H4,
                },
                {
                    "name": "h5",
                    "type": H5,
                },
                {
                    "name": "h6",
                    "type": H6,
                },
                {
                    "name": "div",
                    "type": Type["Div"],
                },
                {
                    "name": "ul",
                    "type": Type["Ul"],
                },
                {
                    "name": "ol",
                    "type": Ol,
                },
                {
                    "name": "dl",
                    "type": Type["Dl"],
                },
                {
                    "name": "pre",
                    "type": Pre,
                },
                {
                    "name": "hr",
                    "type": Hr,
                },
                {
                    "name": "blockquote",
                    "type": Type["Blockquote"],
                },
                {
                    "name": "address",
                    "type": Address,
                },
                {
                    "name": "table",
                    "type": Type["Table"],
                },
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Th:
    class Meta:
        name = "th"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[ThDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    abbr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    axis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    headers: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    scope: Optional[ThScope] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[ThAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[ThValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "p",
                    "type": Type["P"],
                },
                {
                    "name": "h1",
                    "type": H1,
                },
                {
                    "name": "h2",
                    "type": H2,
                },
                {
                    "name": "h3",
                    "type": H3,
                },
                {
                    "name": "h4",
                    "type": H4,
                },
                {
                    "name": "h5",
                    "type": H5,
                },
                {
                    "name": "h6",
                    "type": H6,
                },
                {
                    "name": "div",
                    "type": Type["Div"],
                },
                {
                    "name": "ul",
                    "type": Type["Ul"],
                },
                {
                    "name": "ol",
                    "type": Ol,
                },
                {
                    "name": "dl",
                    "type": Type["Dl"],
                },
                {
                    "name": "pre",
                    "type": Pre,
                },
                {
                    "name": "hr",
                    "type": Hr,
                },
                {
                    "name": "blockquote",
                    "type": Type["Blockquote"],
                },
                {
                    "name": "address",
                    "type": Address,
                },
                {
                    "name": "table",
                    "type": Type["Table"],
                },
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Tr:
    class Meta:
        name = "tr"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    th_or_td: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "th",
                    "type": Th,
                },
                {
                    "name": "td",
                    "type": Td,
                },
            ),
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[TrDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[TrAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[TrValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Tbody:
    class Meta:
        name = "tbody"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    tr: List[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[TbodyDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[TbodyAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[TbodyValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Tfoot:
    class Meta:
        name = "tfoot"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    tr: List[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[TfootDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[TfootAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[TfootValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Thead:
    class Meta:
        name = "thead"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    tr: List[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[TheadDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[TheadAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[TheadValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Table:
    class Meta:
        name = "table"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    caption: Optional[Caption] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    col_or_colgroup: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "col",
                    "type": Col,
                },
                {
                    "name": "colgroup",
                    "type": Colgroup,
                },
            ),
        }
    )
    thead: Optional[Thead] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tfoot: Optional[Tfoot] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tbody_or_tr: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "tbody",
                    "type": Tbody,
                },
                {
                    "name": "tr",
                    "type": Tr,
                },
            ),
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[TableDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    border: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    frame: Optional[TableFrame] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rules: Optional[TableRules] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cellspacing: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cellpadding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Blockquote:
    class Meta:
        name = "blockquote"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "p",
                    "type": Type["P"],
                },
                {
                    "name": "h1",
                    "type": H1,
                },
                {
                    "name": "h2",
                    "type": H2,
                },
                {
                    "name": "h3",
                    "type": H3,
                },
                {
                    "name": "h4",
                    "type": H4,
                },
                {
                    "name": "h5",
                    "type": H5,
                },
                {
                    "name": "h6",
                    "type": H6,
                },
                {
                    "name": "div",
                    "type": Type["Div"],
                },
                {
                    "name": "ul",
                    "type": Type["Ul"],
                },
                {
                    "name": "ol",
                    "type": Ol,
                },
                {
                    "name": "dl",
                    "type": Type["Dl"],
                },
                {
                    "name": "pre",
                    "type": Pre,
                },
                {
                    "name": "hr",
                    "type": Hr,
                },
                {
                    "name": "blockquote",
                    "type": Type["Blockquote"],
                },
                {
                    "name": "address",
                    "type": Address,
                },
                {
                    "name": "table",
                    "type": Table,
                },
            ),
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[BlockquoteDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Dd:
    class Meta:
        name = "dd"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[DdDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "p",
                    "type": Type["P"],
                },
                {
                    "name": "h1",
                    "type": H1,
                },
                {
                    "name": "h2",
                    "type": H2,
                },
                {
                    "name": "h3",
                    "type": H3,
                },
                {
                    "name": "h4",
                    "type": H4,
                },
                {
                    "name": "h5",
                    "type": H5,
                },
                {
                    "name": "h6",
                    "type": H6,
                },
                {
                    "name": "div",
                    "type": Type["Div"],
                },
                {
                    "name": "ul",
                    "type": Type["Ul"],
                },
                {
                    "name": "ol",
                    "type": Ol,
                },
                {
                    "name": "dl",
                    "type": Type["Dl"],
                },
                {
                    "name": "pre",
                    "type": Pre,
                },
                {
                    "name": "hr",
                    "type": Hr,
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                },
                {
                    "name": "address",
                    "type": Address,
                },
                {
                    "name": "table",
                    "type": Table,
                },
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Dl:
    class Meta:
        name = "dl"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    dt_or_dd: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "dt",
                    "type": Dt,
                },
                {
                    "name": "dd",
                    "type": Dd,
                },
            ),
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[DlDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Li:
    class Meta:
        name = "li"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[LiDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "p",
                    "type": Type["P"],
                },
                {
                    "name": "h1",
                    "type": H1,
                },
                {
                    "name": "h2",
                    "type": H2,
                },
                {
                    "name": "h3",
                    "type": H3,
                },
                {
                    "name": "h4",
                    "type": H4,
                },
                {
                    "name": "h5",
                    "type": H5,
                },
                {
                    "name": "h6",
                    "type": H6,
                },
                {
                    "name": "div",
                    "type": Type["Div"],
                },
                {
                    "name": "ul",
                    "type": Type["Ul"],
                },
                {
                    "name": "ol",
                    "type": Ol,
                },
                {
                    "name": "dl",
                    "type": Dl,
                },
                {
                    "name": "pre",
                    "type": Pre,
                },
                {
                    "name": "hr",
                    "type": Hr,
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                },
                {
                    "name": "address",
                    "type": Address,
                },
                {
                    "name": "table",
                    "type": Table,
                },
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Ul:
    class Meta:
        name = "ul"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    li: List[Li] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[UlDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Div:
    class Meta:
        name = "div"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[DivDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "p",
                    "type": Type["P"],
                },
                {
                    "name": "h1",
                    "type": H1,
                },
                {
                    "name": "h2",
                    "type": H2,
                },
                {
                    "name": "h3",
                    "type": H3,
                },
                {
                    "name": "h4",
                    "type": H4,
                },
                {
                    "name": "h5",
                    "type": H5,
                },
                {
                    "name": "h6",
                    "type": H6,
                },
                {
                    "name": "div",
                    "type": Type["Div"],
                },
                {
                    "name": "ul",
                    "type": Ul,
                },
                {
                    "name": "ol",
                    "type": Ol,
                },
                {
                    "name": "dl",
                    "type": Dl,
                },
                {
                    "name": "pre",
                    "type": Pre,
                },
                {
                    "name": "hr",
                    "type": Hr,
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                },
                {
                    "name": "address",
                    "type": Address,
                },
                {
                    "name": "table",
                    "type": Table,
                },
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Map:
    class Meta:
        name = "map"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "p",
                    "type": Type["P"],
                },
                {
                    "name": "h1",
                    "type": H1,
                },
                {
                    "name": "h2",
                    "type": H2,
                },
                {
                    "name": "h3",
                    "type": H3,
                },
                {
                    "name": "h4",
                    "type": H4,
                },
                {
                    "name": "h5",
                    "type": H5,
                },
                {
                    "name": "h6",
                    "type": H6,
                },
                {
                    "name": "div",
                    "type": Div,
                },
                {
                    "name": "ul",
                    "type": Ul,
                },
                {
                    "name": "ol",
                    "type": Ol,
                },
                {
                    "name": "dl",
                    "type": Dl,
                },
                {
                    "name": "pre",
                    "type": Pre,
                },
                {
                    "name": "hr",
                    "type": Hr,
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                },
                {
                    "name": "address",
                    "type": Address,
                },
                {
                    "name": "table",
                    "type": Table,
                },
            ),
        }
    )
    area: List[Area] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[MapDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class P:
    class Meta:
        name = "p"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[PDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Map,
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Object:
    class Meta:
        name = "object"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[ObjectDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    declare: Optional[ObjectDeclare] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    classid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    codebase: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    data: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    codetype: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    archive: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    standby: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    usemap: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    tabindex: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "param",
                    "type": Param,
                },
                {
                    "name": "p",
                    "type": P,
                },
                {
                    "name": "h1",
                    "type": H1,
                },
                {
                    "name": "h2",
                    "type": H2,
                },
                {
                    "name": "h3",
                    "type": H3,
                },
                {
                    "name": "h4",
                    "type": H4,
                },
                {
                    "name": "h5",
                    "type": H5,
                },
                {
                    "name": "h6",
                    "type": H6,
                },
                {
                    "name": "div",
                    "type": Div,
                },
                {
                    "name": "ul",
                    "type": Ul,
                },
                {
                    "name": "ol",
                    "type": Ol,
                },
                {
                    "name": "dl",
                    "type": Dl,
                },
                {
                    "name": "pre",
                    "type": Pre,
                },
                {
                    "name": "hr",
                    "type": Hr,
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                },
                {
                    "name": "address",
                    "type": Address,
                },
                {
                    "name": "table",
                    "type": Table,
                },
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Type["Object"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Map,
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Bdo:
    class Meta:
        name = "bdo"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[BdoDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "object",
                    "type": Object,
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Map,
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class Span:
    class Meta:
        name = "span"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[SpanDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": Type["A"],
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                },
                {
                    "name": "object",
                    "type": Object,
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Map,
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )


@dataclass(slots=True)
class A:
    class Meta:
        name = "a"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[ADir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rev: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    accesskey: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    shape: AShape = field(
        default=AShape.RECT,
        metadata={
            "type": "Attribute",
        }
    )
    coords: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    tabindex: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    onfocus: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    onblur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "span",
                    "type": Span,
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                },
                {
                    "name": "object",
                    "type": Object,
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "map",
                    "type": Map,
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "big",
                    "type": Big,
                },
                {
                    "name": "small",
                    "type": Small,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                },
                {
                    "name": "code",
                    "type": Code,
                },
                {
                    "name": "q",
                    "type": Q,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "samp",
                    "type": Samp,
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                },
                {
                    "name": "var",
                    "type": Var,
                },
                {
                    "name": "cite",
                    "type": Cite,
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                },
            ),
        }
    )
