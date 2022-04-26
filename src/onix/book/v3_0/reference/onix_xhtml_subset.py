from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Type

__NAMESPACE__ = "http://ns.editeur.org/onix/3.0/reference"


class Scope(Enum):
    ROW = "row"
    COL = "col"
    ROWGROUP = "rowgroup"
    COLGROUP = "colgroup"


class Shape(Enum):
    RECT = "rect"
    CIRCLE = "circle"
    POLY = "poly"
    DEFAULT = "default"


class Tframe(Enum):
    VOID = "void"
    ABOVE = "above"
    BELOW = "below"
    HSIDES = "hsides"
    LHS = "lhs"
    RHS = "rhs"
    VSIDES = "vsides"
    BOX = "box"
    BORDER = "border"


class Trules(Enum):
    NONE = "none"
    GROUPS = "groups"
    ROWS = "rows"
    COLS = "cols"
    ALL = "all"


class AreaAttlistNohref(Enum):
    NOHREF = "nohref"


class BdoAttlistDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


@dataclass(slots=True)
class Br:
    class Meta:
        name = "br"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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


class CellhalignAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
    CHAR = "char"


class CellvalignValign(Enum):
    TOP = "top"
    MIDDLE = "middle"
    BOTTOM = "bottom"
    BASELINE = "baseline"


class I18NDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class ImgAttlistIsmap(Enum):
    ISMAP = "ismap"


@dataclass(slots=True)
class Area:
    class Meta:
        name = "area"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    shape: Shape = field(
        default=Shape.RECT,
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
    nohref: Optional[AreaAttlistNohref] = field(
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
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
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
    align: Optional[CellhalignAlign] = field(
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
    valign: Optional[CellvalignValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Dl:
    class Meta:
        name = "dl"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

    dt_or_dd: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "dt",
                    "type": Type["Dt"],
                },
                {
                    "name": "dd",
                    "type": Type["Dd"],
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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Hr:
    class Meta:
        name = "hr"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Img:
    class Meta:
        name = "img"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
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
    ismap: Optional[ImgAttlistIsmap] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Ol:
    class Meta:
        name = "ol"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Rp:
    class Meta:
        name = "rp"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
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
        }
    )


@dataclass(slots=True)
class Ul:
    class Meta:
        name = "ul"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Colgroup:
    class Meta:
        name = "colgroup"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
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
    align: Optional[CellhalignAlign] = field(
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
    valign: Optional[CellvalignValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class RubyContent:
    class Meta:
        name = "ruby.content"

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
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "b",
                    "type": Type["B"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "i",
                    "type": Type["I"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "q",
                    "type": Type["Q"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "acronym",
                    "type": Type["Acronym"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "abbr",
                    "type": Type["Abbr"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "cite",
                    "type": Type["Cite"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "var",
                    "type": Type["Var"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "kbd",
                    "type": Type["Kbd"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "samp",
                    "type": Type["Samp"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
            ),
        }
    )


@dataclass(slots=True)
class Rb(RubyContent):
    class Meta:
        name = "rb"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Rt(RubyContent):
    class Meta:
        name = "rt"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rbspan: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Rbc:
    class Meta:
        name = "rbc"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

    rb: List[Rb] = field(
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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Rtc:
    class Meta:
        name = "rtc"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

    rt: List[Rt] = field(
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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Ruby:
    class Meta:
        name = "ruby"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

    rb: Optional[Rb] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "rt",
                    "type": Rt,
                },
                {
                    "name": "rp",
                    "type": Rp,
                },
                {
                    "name": "rbc",
                    "type": Rbc,
                },
                {
                    "name": "rtc",
                    "type": Rtc,
                },
            ),
            "max_occurs": 7,
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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Q:
    class Meta:
        name = "q"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
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
                    "name": "ruby",
                    "type": Ruby,
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                },
                {
                    "name": "q",
                    "type": Type["Q"],
                },
                {
                    "name": "acronym",
                    "type": Type["Acronym"],
                },
                {
                    "name": "abbr",
                    "type": Type["Abbr"],
                },
                {
                    "name": "var",
                    "type": Type["Var"],
                },
                {
                    "name": "kbd",
                    "type": Type["Kbd"],
                },
                {
                    "name": "samp",
                    "type": Type["Samp"],
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                },
                {
                    "name": "b",
                    "type": Type["B"],
                },
                {
                    "name": "i",
                    "type": Type["I"],
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                },
                {
                    "name": "img",
                    "type": Img,
                },
                {
                    "name": "br",
                    "type": Br,
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                },
            ),
        }
    )


@dataclass(slots=True)
class PreContent:
    class Meta:
        name = "pre.content"

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
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "i",
                    "type": Type["I"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "b",
                    "type": Type["B"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "acronym",
                    "type": Type["Acronym"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "abbr",
                    "type": Type["Abbr"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "cite",
                    "type": Type["Cite"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "var",
                    "type": Type["Var"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "kbd",
                    "type": Type["Kbd"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "samp",
                    "type": Type["Samp"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
            ),
        }
    )


@dataclass(slots=True)
class Pre(PreContent):
    class Meta:
        name = "pre"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Block:
    table: List["Table"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    p: List["P"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    div: List["Div"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    blockquote: List["Blockquote"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    pre: List[Pre] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    hr: List[Hr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    address: List["Address"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    dl: List[Dl] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    ol: List[Ol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    ul: List[Ul] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    h6: List["H6"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    h5: List["H5"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    h4: List["H4"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    h3: List["H3"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    h2: List["H2"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )
    h1: List["H1"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ns.editeur.org/onix/3.0/reference",
        }
    )


@dataclass(slots=True)
class Blockquote(Block):
    class Meta:
        name = "blockquote"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
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
class Flow:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "table",
                    "type": Type["Table"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "p",
                    "type": Type["P"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "div",
                    "type": Type["Div"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "pre",
                    "type": Pre,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "address",
                    "type": Type["Address"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "dl",
                    "type": Dl,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "ol",
                    "type": Ol,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "ul",
                    "type": Ul,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "h6",
                    "type": Type["H6"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "h5",
                    "type": Type["H5"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "h4",
                    "type": Type["H4"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "h3",
                    "type": Type["H3"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "h2",
                    "type": Type["H2"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "h1",
                    "type": Type["H1"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "a",
                    "type": Type["A"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "acronym",
                    "type": Type["Acronym"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "abbr",
                    "type": Type["Abbr"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "cite",
                    "type": Type["Cite"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "var",
                    "type": Type["Var"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "kbd",
                    "type": Type["Kbd"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "samp",
                    "type": Type["Samp"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "b",
                    "type": Type["B"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "i",
                    "type": Type["I"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "map",
                    "type": Type["Map"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
            ),
        }
    )


@dataclass(slots=True)
class Dd(Flow):
    class Meta:
        name = "dd"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Div(Flow):
    class Meta:
        name = "div"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Li(Flow):
    class Meta:
        name = "li"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Td(Flow):
    class Meta:
        name = "td"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
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
    scope: Optional[Scope] = field(
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
    align: Optional[CellhalignAlign] = field(
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
    valign: Optional[CellvalignValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Th(Flow):
    class Meta:
        name = "th"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
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
    scope: Optional[Scope] = field(
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
    align: Optional[CellhalignAlign] = field(
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
    valign: Optional[CellvalignValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Tr:
    class Meta:
        name = "tr"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[CellhalignAlign] = field(
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
    valign: Optional[CellvalignValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Tbody:
    class Meta:
        name = "tbody"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[CellhalignAlign] = field(
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
    valign: Optional[CellvalignValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Tfoot:
    class Meta:
        name = "tfoot"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[CellhalignAlign] = field(
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
    valign: Optional[CellvalignValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Thead:
    class Meta:
        name = "thead"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[CellhalignAlign] = field(
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
    valign: Optional[CellvalignValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Table:
    class Meta:
        name = "table"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

    caption: Optional["Caption"] = field(
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
    dir: Optional[I18NDir] = field(
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
    frame: Optional[Tframe] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rules: Optional[Trules] = field(
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
class Map:
    class Meta:
        name = "map"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "table",
                    "type": Table,
                },
                {
                    "name": "p",
                    "type": Type["P"],
                },
                {
                    "name": "div",
                    "type": Div,
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
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
                    "name": "address",
                    "type": Type["Address"],
                },
                {
                    "name": "dl",
                    "type": Dl,
                },
                {
                    "name": "ol",
                    "type": Ol,
                },
                {
                    "name": "ul",
                    "type": Ul,
                },
                {
                    "name": "h6",
                    "type": Type["H6"],
                },
                {
                    "name": "h5",
                    "type": Type["H5"],
                },
                {
                    "name": "h4",
                    "type": Type["H4"],
                },
                {
                    "name": "h3",
                    "type": Type["H3"],
                },
                {
                    "name": "h2",
                    "type": Type["H2"],
                },
                {
                    "name": "h1",
                    "type": Type["H1"],
                },
                {
                    "name": "area",
                    "type": Area,
                },
            ),
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dir: Optional[I18NDir] = field(
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
class AContent:
    class Meta:
        name = "a.content"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "map",
                    "type": Map,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "b",
                    "type": Type["B"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "i",
                    "type": Type["I"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "acronym",
                    "type": Type["Acronym"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "abbr",
                    "type": Type["Abbr"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "cite",
                    "type": Type["Cite"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "var",
                    "type": Type["Var"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "kbd",
                    "type": Type["Kbd"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "samp",
                    "type": Type["Samp"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
            ),
        }
    )


@dataclass(slots=True)
class A(AContent):
    class Meta:
        name = "a"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
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
    shape: Shape = field(
        default=Shape.RECT,
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


@dataclass(slots=True)
class Inline:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "ruby",
                    "type": Ruby,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "sup",
                    "type": Type["Sup"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "sub",
                    "type": Type["Sub"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "acronym",
                    "type": Type["Acronym"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "abbr",
                    "type": Type["Abbr"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "cite",
                    "type": Type["Cite"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "var",
                    "type": Type["Var"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "kbd",
                    "type": Type["Kbd"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "samp",
                    "type": Type["Samp"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "code",
                    "type": Type["Code"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "dfn",
                    "type": Type["Dfn"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "strong",
                    "type": Type["Strong"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "em",
                    "type": Type["Em"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "small",
                    "type": Type["Small"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "big",
                    "type": Type["Big"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "b",
                    "type": Type["B"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "i",
                    "type": Type["I"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "tt",
                    "type": Type["Tt"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "map",
                    "type": Map,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "bdo",
                    "type": Type["Bdo"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
                {
                    "name": "span",
                    "type": Type["Span"],
                    "namespace": "http://ns.editeur.org/onix/3.0/reference",
                },
            ),
        }
    )


@dataclass(slots=True)
class Abbr(Inline):
    class Meta:
        name = "abbr"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Acronym(Inline):
    class Meta:
        name = "acronym"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Address(Inline):
    class Meta:
        name = "address"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B(Inline):
    class Meta:
        name = "b"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Bdo(Inline):
    class Meta:
        name = "bdo"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[BdoAttlistDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(slots=True)
class Big(Inline):
    class Meta:
        name = "big"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Caption(Inline):
    class Meta:
        name = "caption"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Cite(Inline):
    class Meta:
        name = "cite"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Code(Inline):
    class Meta:
        name = "code"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Dfn(Inline):
    class Meta:
        name = "dfn"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Dt(Inline):
    class Meta:
        name = "dt"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Em(Inline):
    class Meta:
        name = "em"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class H1(Inline):
    class Meta:
        name = "h1"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class H2(Inline):
    class Meta:
        name = "h2"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class H3(Inline):
    class Meta:
        name = "h3"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class H4(Inline):
    class Meta:
        name = "h4"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class H5(Inline):
    class Meta:
        name = "h5"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class H6(Inline):
    class Meta:
        name = "h6"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class I(Inline):
    class Meta:
        name = "i"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Kbd(Inline):
    class Meta:
        name = "kbd"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class P(Inline):
    class Meta:
        name = "p"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Samp(Inline):
    class Meta:
        name = "samp"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Small(Inline):
    class Meta:
        name = "small"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Span(Inline):
    class Meta:
        name = "span"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Strong(Inline):
    class Meta:
        name = "strong"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Sub(Inline):
    class Meta:
        name = "sub"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Sup(Inline):
    class Meta:
        name = "sup"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Tt(Inline):
    class Meta:
        name = "tt"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Var(Inline):
    class Meta:
        name = "var"
        namespace = "http://ns.editeur.org/onix/3.0/reference"

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
    dir: Optional[I18NDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
