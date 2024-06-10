from dataclasses import dataclass, field
from enum import Enum
from typing import ForwardRef, List, Optional, Union

__NAMESPACE__ = "http://ns.editeur.org/onix/3.1/short"


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


class ADir(Enum):
    LTR = "ltr"
    RTL = "rtl"


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


class BDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class BdoDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class BigDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


@dataclass(slots=True)
class BlockAbstract:
    class Meta:
        name = "block"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


class BlockquoteDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


@dataclass(slots=True)
class Blocktext:
    class Meta:
        name = "blocktext"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(slots=True)
class Br:
    class Meta:
        name = "br"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
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


@dataclass(slots=True)
class Fontstyle:
    class Meta:
        name = "fontstyle"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(slots=True)
class Gloss:
    class Meta:
        name = "gloss"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


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


@dataclass(slots=True)
class Heading:
    class Meta:
        name = "heading"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


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


@dataclass(slots=True)
class InlineAbstract:
    class Meta:
        name = "inline"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


class KbdDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class LiDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


@dataclass(slots=True)
class Lists:
    class Meta:
        name = "lists"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


class MapDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class OlDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class OlType(Enum):
    VALUE_1 = "1"
    A = "A"
    A_1 = "a"
    I = "I"
    I_1 = "i"


class PDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


@dataclass(slots=True)
class Phrase:
    class Meta:
        name = "phrase"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


class PreDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class QDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class RbDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class RbcDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class RpDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class RtDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class RtcDir(Enum):
    LTR = "ltr"
    RTL = "rtl"


class RubyDir(Enum):
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


@dataclass(slots=True)
class Special:
    class Meta:
        name = "special"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


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
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[AreaDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    shape: Shape = field(
        default=Shape.RECT,
        metadata={
            "type": "Attribute",
        },
    )
    coords: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nohref: Optional[AreaNohref] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class Col:
    class Meta:
        name = "col"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[ColDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    span: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[ColAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: Optional[ColValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Hr:
    class Meta:
        name = "hr"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[HrDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Img:
    class Meta:
        name = "img"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[ImgDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    longdesc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    usemap: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ismap: Optional[ImgIsmap] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Rp:
    class Meta:
        name = "rp"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[RpDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
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
                    "type": ForwardRef("A"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "sup",
                    "type": ForwardRef("Sup"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "q",
                    "type": ForwardRef("Q"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "acronym",
                    "type": ForwardRef("Acronym"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "abbr",
                    "type": ForwardRef("Abbr"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "cite",
                    "type": ForwardRef("Cite"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "var",
                    "type": ForwardRef("Var"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "kbd",
                    "type": ForwardRef("Kbd"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "samp",
                    "type": ForwardRef("Samp"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "code",
                    "type": ForwardRef("Code"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "dfn",
                    "type": ForwardRef("Dfn"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "strong",
                    "type": ForwardRef("Strong"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "em",
                    "type": ForwardRef("Em"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "small",
                    "type": ForwardRef("Small"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "big",
                    "type": ForwardRef("Big"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "b",
                    "type": ForwardRef("B"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "i",
                    "type": ForwardRef("I"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "tt",
                    "type": ForwardRef("Tt"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "map",
                    "type": ForwardRef("Map"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "bdo",
                    "type": ForwardRef("Bdo"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "span",
                    "type": ForwardRef("Span"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
            ),
        },
    )


@dataclass(slots=True)
class Colgroup:
    class Meta:
        name = "colgroup"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    col: List[Col] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[ColgroupDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    span: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[ColgroupAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: Optional[ColgroupValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Abbr(Inline):
    class Meta:
        name = "abbr"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[AbbrDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Acronym(Inline):
    class Meta:
        name = "acronym"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[AcronymDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Address(Inline):
    class Meta:
        name = "address"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[AddressDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class B(Inline):
    class Meta:
        name = "b"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[BDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Bdo(Inline):
    class Meta:
        name = "bdo"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[BdoDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class Big(Inline):
    class Meta:
        name = "big"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[BigDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Caption(Inline):
    class Meta:
        name = "caption"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[CaptionDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Cite(Inline):
    class Meta:
        name = "cite"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[CiteDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Code(Inline):
    class Meta:
        name = "code"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[CodeDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Dfn(Inline):
    class Meta:
        name = "dfn"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[DfnDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Dt(Inline):
    class Meta:
        name = "dt"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[DtDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Em(Inline):
    class Meta:
        name = "em"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[EmDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class H1(Inline):
    class Meta:
        name = "h1"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[H1Dir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class H2(Inline):
    class Meta:
        name = "h2"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[H2Dir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class H3(Inline):
    class Meta:
        name = "h3"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[H3Dir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class H4(Inline):
    class Meta:
        name = "h4"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[H4Dir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class H5(Inline):
    class Meta:
        name = "h5"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[H5Dir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class H6(Inline):
    class Meta:
        name = "h6"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[H6Dir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class I(Inline):
    class Meta:
        name = "i"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[IDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Kbd(Inline):
    class Meta:
        name = "kbd"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[KbdDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class P(Inline):
    class Meta:
        name = "p"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[PDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Q(Inline):
    class Meta:
        name = "q"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[QDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Samp(Inline):
    class Meta:
        name = "samp"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[SampDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Small(Inline):
    class Meta:
        name = "small"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[SmallDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Span(Inline):
    class Meta:
        name = "span"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[SpanDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Strong(Inline):
    class Meta:
        name = "strong"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[StrongDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Sub(Inline):
    class Meta:
        name = "sub"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[SubDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Sup(Inline):
    class Meta:
        name = "sup"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[SupDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Tt(Inline):
    class Meta:
        name = "tt"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[TtDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Var(Inline):
    class Meta:
        name = "var"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[VarDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Block:
    choice: List[
        Union[
            "Table",
            P,
            "Div",
            "Blockquote",
            "Pre",
            Hr,
            Address,
            "Dl",
            "Ol",
            "Ul",
            H6,
            H5,
            H4,
            H3,
            H2,
            H1,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "table",
                    "type": ForwardRef("Table"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "div",
                    "type": ForwardRef("Div"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "blockquote",
                    "type": ForwardRef("Blockquote"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "pre",
                    "type": ForwardRef("Pre"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "address",
                    "type": Address,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "dl",
                    "type": ForwardRef("Dl"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "h6",
                    "type": H6,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "h5",
                    "type": H5,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "h4",
                    "type": H4,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "h3",
                    "type": H3,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "h2",
                    "type": H2,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "h1",
                    "type": H1,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
            ),
        },
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
                    "type": ForwardRef("Map"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
            ),
        },
    )


@dataclass(slots=True)
class A(AContent):
    class Meta:
        name = "a"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[ADir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hreflang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rev: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    accesskey: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    shape: Shape = field(
        default=Shape.RECT,
        metadata={
            "type": "Attribute",
        },
    )
    coords: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tabindex: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    onfocus: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    onblur: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Blockquote(Block):
    class Meta:
        name = "blockquote"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[BlockquoteDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
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
                    "type": ForwardRef("Table"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "p",
                    "type": P,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "div",
                    "type": ForwardRef("Div"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "pre",
                    "type": ForwardRef("Pre"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "hr",
                    "type": Hr,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "address",
                    "type": Address,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "dl",
                    "type": ForwardRef("Dl"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "ol",
                    "type": ForwardRef("Ol"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "ul",
                    "type": ForwardRef("Ul"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "h6",
                    "type": H6,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "h5",
                    "type": H5,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "h4",
                    "type": H4,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "h3",
                    "type": H3,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "h2",
                    "type": H2,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "h1",
                    "type": H1,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "a",
                    "type": ForwardRef("A"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "map",
                    "type": ForwardRef("Map"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
            ),
        },
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
                    "type": A,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "map",
                    "type": ForwardRef("Map"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "ruby",
                    "type": ForwardRef("Ruby"),
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
            ),
        },
    )


@dataclass(slots=True)
class Dd(Flow):
    class Meta:
        name = "dd"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[DdDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Div(Flow):
    class Meta:
        name = "div"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[DivDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Li(Flow):
    class Meta:
        name = "li"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[LiDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Pre(PreContent):
    class Meta:
        name = "pre"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[PreDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Td(Flow):
    class Meta:
        name = "td"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[TdDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    abbr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    axis: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    headers: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    scope: Optional[Scope] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[TdAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: Optional[TdValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Th(Flow):
    class Meta:
        name = "th"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[ThDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    abbr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    axis: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    headers: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    scope: Optional[Scope] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rowspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    colspan: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[ThAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: Optional[ThValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Dl:
    class Meta:
        name = "dl"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    dt_or_dd: List[Union[Dt, Dd]] = field(
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
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[DlDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Ol:
    class Meta:
        name = "ol"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    li: List[Li] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[OlDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[OlType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    start: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Tr:
    class Meta:
        name = "tr"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    th_or_td: List[Union[Th, Td]] = field(
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
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[TrDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[TrAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: Optional[TrValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Ul:
    class Meta:
        name = "ul"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    li: List[Li] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[UlDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Tbody:
    class Meta:
        name = "tbody"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    tr: List[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[TbodyDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[TbodyAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: Optional[TbodyValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Tfoot:
    class Meta:
        name = "tfoot"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    tr: List[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[TfootDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[TfootAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: Optional[TfootValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Thead:
    class Meta:
        name = "thead"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    tr: List[Tr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[TheadDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: Optional[TheadAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: Optional[TheadValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Table:
    class Meta:
        name = "table"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    caption: Optional[Caption] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    col_or_colgroup: List[Union[Col, Colgroup]] = field(
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
        },
    )
    thead: Optional[Thead] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tfoot: Optional[Tfoot] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tbody_or_tr: List[Union[Tbody, Tr]] = field(
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
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[TableDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    border: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    frame: Optional[Tframe] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rules: Optional[Trules] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cellspacing: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cellpadding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Map:
    class Meta:
        name = "map"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    choice: List[
        Union[
            Table,
            P,
            Div,
            Blockquote,
            Pre,
            Hr,
            Address,
            Dl,
            Ol,
            Ul,
            H6,
            H5,
            H4,
            H3,
            H2,
            H1,
            Area,
        ]
    ] = field(
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
                    "type": P,
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
                    "type": Address,
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
                    "type": H6,
                },
                {
                    "name": "h5",
                    "type": H5,
                },
                {
                    "name": "h4",
                    "type": H4,
                },
                {
                    "name": "h3",
                    "type": H3,
                },
                {
                    "name": "h2",
                    "type": H2,
                },
                {
                    "name": "h1",
                    "type": H1,
                },
                {
                    "name": "area",
                    "type": Area,
                },
            ),
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[MapDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
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
                    "type": A,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "map",
                    "type": Map,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "img",
                    "type": Img,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "br",
                    "type": Br,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "bdo",
                    "type": Bdo,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "span",
                    "type": Span,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "small",
                    "type": Small,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "big",
                    "type": Big,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "i",
                    "type": I,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "tt",
                    "type": Tt,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "sup",
                    "type": Sup,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "sub",
                    "type": Sub,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "q",
                    "type": Q,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "acronym",
                    "type": Acronym,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "abbr",
                    "type": Abbr,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "cite",
                    "type": Cite,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "var",
                    "type": Var,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "kbd",
                    "type": Kbd,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "samp",
                    "type": Samp,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "code",
                    "type": Code,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "dfn",
                    "type": Dfn,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "strong",
                    "type": Strong,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
                {
                    "name": "em",
                    "type": Em,
                    "namespace": "http://ns.editeur.org/onix/3.1/short",
                },
            ),
        },
    )


@dataclass(slots=True)
class Rb(RubyContent):
    class Meta:
        name = "rb"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[RbDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Rt(RubyContent):
    class Meta:
        name = "rt"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[RtDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rbspan: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Rbc:
    class Meta:
        name = "rbc"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    rb: List[Rb] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[RbcDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Rtc:
    class Meta:
        name = "rtc"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    rt: List[Rt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[RtcDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Ruby:
    class Meta:
        name = "ruby"
        namespace = "http://ns.editeur.org/onix/3.1/short"

    rb_or_rbc: Optional[Union[Rb, Rbc]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "rb",
                    "type": Rb,
                },
                {
                    "name": "rbc",
                    "type": Rbc,
                },
            ),
        },
    )
    rt: List[Rt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    rp: List[Rp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    rtc: List[Rtc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequence": 2,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dir: Optional[RubyDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
