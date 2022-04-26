from dataclasses import dataclass, field
from typing import List, Optional
from onix.book.v2_1.short.onix_book_product_code_lists import (
    List1,
    List10,
    List100,
    List101,
    List102,
    List11,
    List12,
    List13,
    List138,
    List14,
    List15,
    List16,
    List17,
    List18,
    List19,
    List2,
    List20,
    List21,
    List22,
    List23,
    List24,
    List25,
    List26,
    List27,
    List28,
    List29,
    List3,
    List30,
    List31,
    List32,
    List33,
    List34,
    List35,
    List36,
    List37,
    List38,
    List39,
    List40,
    List41,
    List42,
    List43,
    List44,
    List45,
    List46,
    List47,
    List48,
    List49,
    List5,
    List50,
    List51,
    List52,
    List53,
    List54,
    List55,
    List56,
    List57,
    List58,
    List59,
    List6,
    List60,
    List61,
    List62,
    List64,
    List65,
    List7,
    List70,
    List71,
    List72,
    List73,
    List74,
    List75,
    List78,
    List79,
    List8,
    List80,
    List81,
    List82,
    List83,
    List84,
    List85,
    List86,
    List87,
    List89,
    List9,
    List90,
    List91,
    List92,
    List93,
    List94,
    List95,
    List96,
    List97,
)
from onix.book.v2_1.short.onix_xhtml_subset import (
    A,
    Abbr,
    Acronym,
    Address,
    B,
    Bdo,
    Big,
    Blockquote,
    Br,
    Cite,
    Code,
    Dfn,
    Div,
    Dl,
    Em,
    H1,
    H2,
    H3,
    H4,
    H5,
    H6,
    Hr,
    I,
    Img,
    Kbd,
    Map,
    Object,
    Ol,
    P,
    Pre,
    Q,
    Samp,
    Small,
    Span,
    Strong,
    Sub,
    Sup,
    Table,
    Tt,
    Ul,
    Var,
)

__NAMESPACE__ = "http://www.editeur.org/onix/2.1/short"


@dataclass(slots=True)
class A001:
    class Meta:
        name = "a001"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="RecordReference",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="a001",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class A002:
    class Meta:
        name = "a002"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List1] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="NotificationType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="a002",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class A194:
    class Meta:
        name = "a194"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List3] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="RecordSourceType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="a194",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class A195:
    class Meta:
        name = "a195"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List44] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="RecordSourceIdentifierType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="a195",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class A196:
    class Meta:
        name = "a196"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="RecordSourceIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="a196",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class A197:
    class Meta:
        name = "a197"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="RecordSourceName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="a197",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class A198:
    class Meta:
        name = "a198"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List2] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="DeletionCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="a198",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class A199:
    class Meta:
        name = "a199"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="DeletionText",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="a199",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class A245:
    class Meta:
        name = "a245"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SubordinateEntries",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="a245",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B003:
    class Meta:
        name = "b003"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PublicationDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b003",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B004:
    class Meta:
        name = "b004"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ISBN",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b004",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B005:
    class Meta:
        name = "b005"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EAN13",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b005",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B006:
    class Meta:
        name = "b006"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="UPC",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b006",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B007:
    class Meta:
        name = "b007"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PublisherProductNo",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b007",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B008:
    class Meta:
        name = "b008"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ISMN",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b008",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B009:
    class Meta:
        name = "b009"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="DOI",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b009",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B010:
    class Meta:
        name = "b010"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ReplacesISBN",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b010",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B011:
    class Meta:
        name = "b011"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ReplacesEAN13",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b011",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B012:
    class Meta:
        name = "b012"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List7] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ProductForm",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b012",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B013:
    class Meta:
        name = "b013"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List8] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="BookFormDetail",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b013",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B014:
    class Meta:
        name = "b014"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ProductFormDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b014",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B015:
    class Meta:
        name = "b015"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ItemQuantity",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b015",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B016:
    class Meta:
        name = "b016"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SeriesISSN",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b016",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B017:
    class Meta:
        name = "b017"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PublisherSeriesCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b017",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B018:
    class Meta:
        name = "b018"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TitleOfSeries",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b018",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B019:
    class Meta:
        name = "b019"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="NumberWithinSeries",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b019",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B020:
    class Meta:
        name = "b020"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="YearOfAnnual",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b020",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B021:
    class Meta:
        name = "b021"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ISBNOfSet",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b021",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B022:
    class Meta:
        name = "b022"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EAN13OfSet",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b022",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B023:
    class Meta:
        name = "b023"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TitleOfSet",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b023",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B024:
    class Meta:
        name = "b024"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SetPartNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b024",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B025:
    class Meta:
        name = "b025"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SetPartTitle",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b025",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B026:
    class Meta:
        name = "b026"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ItemNumberWithinSet",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b026",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B027:
    class Meta:
        name = "b027"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List14] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="TextCaseFlag",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b027",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B028:
    class Meta:
        name = "b028"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="DistinctiveTitle",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b028",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B029:
    class Meta:
        name = "b029"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="Subtitle",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b029",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B030:
    class Meta:
        name = "b030"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TitlePrefix",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b030",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B031:
    class Meta:
        name = "b031"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TitleWithoutPrefix",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b031",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B032:
    class Meta:
        name = "b032"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TranslationOfTitle",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b032",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B033:
    class Meta:
        name = "b033"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="FormerTitle",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b033",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B034:
    class Meta:
        name = "b034"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SequenceNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b034",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B035:
    class Meta:
        name = "b035"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List17] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ContributorRole",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b035",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B036:
    class Meta:
        name = "b036"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PersonName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b036",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B037:
    class Meta:
        name = "b037"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PersonNameInverted",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b037",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B038:
    class Meta:
        name = "b038"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TitlesBeforeNames",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b038",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B039:
    class Meta:
        name = "b039"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="NamesBeforeKey",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b039",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B040:
    class Meta:
        name = "b040"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="KeyNames",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b040",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B041:
    class Meta:
        name = "b041"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="NamesAfterKey",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b041",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B042:
    class Meta:
        name = "b042"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="LettersAfterNames",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b042",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B043:
    class Meta:
        name = "b043"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TitlesAfterNames",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b043",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B044:
    class Meta:
        name = "b044"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="BiographicalNote",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b044",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
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
                    "type": A,
                },
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


@dataclass(slots=True)
class B045:
    class Meta:
        name = "b045"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ProfessionalPosition",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b045",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B046:
    class Meta:
        name = "b046"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="Affiliation",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b046",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B047:
    class Meta:
        name = "b047"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="CorporateName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b047",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B048:
    class Meta:
        name = "b048"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ContributorDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b048",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B049:
    class Meta:
        name = "b049"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ContributorStatement",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b049",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B050:
    class Meta:
        name = "b050"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ConferenceDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b050",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B051:
    class Meta:
        name = "b051"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List20] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ConferenceRole",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b051",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B052:
    class Meta:
        name = "b052"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ConferenceName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b052",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B053:
    class Meta:
        name = "b053"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ConferenceNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b053",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B054:
    class Meta:
        name = "b054"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ConferenceDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b054",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B055:
    class Meta:
        name = "b055"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ConferencePlace",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b055",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B056:
    class Meta:
        name = "b056"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List21] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="EditionTypeCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b056",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B057:
    class Meta:
        name = "b057"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EditionNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b057",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B058:
    class Meta:
        name = "b058"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EditionStatement",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b058",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B059:
    class Meta:
        name = "b059"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List74] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="LanguageOfText",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b059",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B060:
    class Meta:
        name = "b060"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List74] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="OriginalLanguage",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b060",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B061:
    class Meta:
        name = "b061"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="NumberOfPages",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b061",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B062:
    class Meta:
        name = "b062"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="IllustrationsNote",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b062",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B063:
    class Meta:
        name = "b063"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="MapScale",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b063",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B064:
    class Meta:
        name = "b064"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="BASICMainSubject",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b064",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B065:
    class Meta:
        name = "b065"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="BICMainSubject",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b065",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B066:
    class Meta:
        name = "b066"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="BICVersion",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b066",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B067:
    class Meta:
        name = "b067"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List27] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="SubjectSchemeIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b067",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B068:
    class Meta:
        name = "b068"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SubjectSchemeVersion",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b068",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B069:
    class Meta:
        name = "b069"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SubjectCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b069",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B070:
    class Meta:
        name = "b070"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SubjectHeadingText",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b070",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B071:
    class Meta:
        name = "b071"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="CorporateBodyAsSubject",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b071",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B072:
    class Meta:
        name = "b072"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PlaceAsSubject",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b072",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B073:
    class Meta:
        name = "b073"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List28] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="AudienceCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b073",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B074:
    class Meta:
        name = "b074"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List30] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="AudienceRangeQualifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b074",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B075:
    class Meta:
        name = "b075"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List31] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="AudienceRangePrecision",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b075",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B076:
    class Meta:
        name = "b076"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AudienceRangeValue",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b076",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B077:
    class Meta:
        name = "b077"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List32] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ComplexitySchemeIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b077",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B078:
    class Meta:
        name = "b078"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ComplexityCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b078",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B079:
    class Meta:
        name = "b079"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ImprintName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b079",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B081:
    class Meta:
        name = "b081"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PublisherName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b081",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B083:
    class Meta:
        name = "b083"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List91] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="CountryOfPublication",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b083",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B084:
    class Meta:
        name = "b084"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="CopublisherName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b084",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B085:
    class Meta:
        name = "b085"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SponsorName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b085",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B086:
    class Meta:
        name = "b086"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AnnouncementDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b086",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B087:
    class Meta:
        name = "b087"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="CopyrightYear",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b087",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B088:
    class Meta:
        name = "b088"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="YearFirstPublished",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b088",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B089:
    class Meta:
        name = "b089"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List46] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="SalesRightsType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b089",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B090:
    class Meta:
        name = "b090"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: List[List91] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    refname: str = field(
        init=False,
        default="RightsCountry",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b090",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B091:
    class Meta:
        name = "b091"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List47] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="RightsRegion",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b091",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B125:
    class Meta:
        name = "b125"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="NumberOfIllustrations",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b125",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B171:
    class Meta:
        name = "b171"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SubjectSchemeName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b171",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B189:
    class Meta:
        name = "b189"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="USSchoolGrade",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b189",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B190:
    class Meta:
        name = "b190"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="InterestAge",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b190",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B191:
    class Meta:
        name = "b191"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List26] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="MainSubjectSchemeIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b191",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B200:
    class Meta:
        name = "b200"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="BASICVersion",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b200",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B201:
    class Meta:
        name = "b201"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List16] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="WorkIDType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b201",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B202:
    class Meta:
        name = "b202"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List15] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="TitleType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b202",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B203:
    class Meta:
        name = "b203"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TitleText",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b203",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B204:
    class Meta:
        name = "b204"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List29] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="AudienceCodeType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b204",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B205:
    class Meta:
        name = "b205"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AudienceCodeTypeName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b205",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B206:
    class Meta:
        name = "b206"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AudienceCodeValue",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b206",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B207:
    class Meta:
        name = "b207"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AudienceDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b207",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B209:
    class Meta:
        name = "b209"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="CityOfPublication",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b209",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B210:
    class Meta:
        name = "b210"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="NumberOfPieces",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b210",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B211:
    class Meta:
        name = "b211"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List10] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="EpubType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b211",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B212:
    class Meta:
        name = "b212"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EpubTypeVersion",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b212",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B213:
    class Meta:
        name = "b213"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EpubTypeDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b213",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B214:
    class Meta:
        name = "b214"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List11] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="EpubFormat",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b214",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B215:
    class Meta:
        name = "b215"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EpubFormatVersion",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b215",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B216:
    class Meta:
        name = "b216"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EpubFormatDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b216",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B217:
    class Meta:
        name = "b217"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EditionVersionNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b217",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B218:
    class Meta:
        name = "b218"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List23] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ExtentType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b218",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B219:
    class Meta:
        name = "b219"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ExtentValue",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b219",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B220:
    class Meta:
        name = "b220"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List24] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ExtentUnit",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b220",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B221:
    class Meta:
        name = "b221"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List5] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ProductIDType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b221",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B225:
    class Meta:
        name = "b225"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List80] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ProductPackaging",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b225",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B233:
    class Meta:
        name = "b233"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="IDTypeName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b233",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B240:
    class Meta:
        name = "b240"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="OriginalPublisher",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b240",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B241:
    class Meta:
        name = "b241"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List44] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="NameCodeType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b241",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B242:
    class Meta:
        name = "b242"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="NameCodeTypeName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b242",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B243:
    class Meta:
        name = "b243"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="NameCodeValue",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b243",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B244:
    class Meta:
        name = "b244"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="IDValue",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b244",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B246:
    class Meta:
        name = "b246"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List6] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="Barcode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b246",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B247:
    class Meta:
        name = "b247"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PrefixToKey",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b247",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B248:
    class Meta:
        name = "b248"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SuffixToKey",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b248",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B249:
    class Meta:
        name = "b249"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List19] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="UnnamedPersons",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b249",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B250:
    class Meta:
        name = "b250"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List18] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="PersonNameType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b250",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B251:
    class Meta:
        name = "b251"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List91] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="CountryCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b251",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B252:
    class Meta:
        name = "b252"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List74] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="LanguageCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b252",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B253:
    class Meta:
        name = "b253"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List22] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="LanguageRole",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b253",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B254:
    class Meta:
        name = "b254"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PagesRoman",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b254",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B255:
    class Meta:
        name = "b255"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PagesArabic",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b255",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B256:
    class Meta:
        name = "b256"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List25] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="IllustrationType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b256",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B257:
    class Meta:
        name = "b257"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="Number",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b257",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B273:
    class Meta:
        name = "b273"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List13] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="SeriesIDType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b273",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B274:
    class Meta:
        name = "b274"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List9] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ProductClassificationType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b274",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B275:
    class Meta:
        name = "b275"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ProductClassificationCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b275",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B276:
    class Meta:
        name = "b276"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AbbreviatedLength",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b276",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B277:
    class Meta:
        name = "b277"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EpubTypeNote",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b277",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B278:
    class Meta:
        name = "b278"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List11] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="EpubSource",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b278",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B279:
    class Meta:
        name = "b279"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EpubSourceVersion",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b279",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B280:
    class Meta:
        name = "b280"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EpubSourceDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b280",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B281:
    class Meta:
        name = "b281"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SetItemTitle",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b281",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B282:
    class Meta:
        name = "b282"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SeriesPartName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b282",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B284:
    class Meta:
        name = "b284"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="LevelSequenceNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b284",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B285:
    class Meta:
        name = "b285"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List43] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="TextItemIDType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b285",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B286:
    class Meta:
        name = "b286"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="FirstPageNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b286",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B287:
    class Meta:
        name = "b287"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="LastPageNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b287",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B288:
    class Meta:
        name = "b288"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ComponentTypeName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b288",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B289:
    class Meta:
        name = "b289"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ComponentNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b289",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B290:
    class Meta:
        name = "b290"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List42] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="TextItemType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b290",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B291:
    class Meta:
        name = "b291"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List45] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="PublishingRole",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b291",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B294:
    class Meta:
        name = "b294"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="WebsiteDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b294",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
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
                    "type": A,
                },
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


@dataclass(slots=True)
class B295:
    class Meta:
        name = "b295"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="WebsiteLink",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b295",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B305:
    class Meta:
        name = "b305"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List75] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="PersonDateRole",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b305",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B306:
    class Meta:
        name = "b306"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="Date",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b306",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B324:
    class Meta:
        name = "b324"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="StartDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b324",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B325:
    class Meta:
        name = "b325"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EndDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b325",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B333:
    class Meta:
        name = "b333"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List78] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ProductFormDetail",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b333",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B334:
    class Meta:
        name = "b334"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List79] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ProductFormFeatureType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b334",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B335:
    class Meta:
        name = "b335"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ProductFormFeatureValue",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b335",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B336:
    class Meta:
        name = "b336"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ProductFormFeatureDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b336",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B337:
    class Meta:
        name = "b337"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="Percent",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b337",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B340:
    class Meta:
        name = "b340"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SequenceNumberWithinRole",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b340",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B341:
    class Meta:
        name = "b341"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ConferenceAcronym",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b341",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B342:
    class Meta:
        name = "b342"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ConferenceTheme",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b342",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B352:
    class Meta:
        name = "b352"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List82] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="BibleContents",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b352",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B353:
    class Meta:
        name = "b353"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List83] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="BibleVersion",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b353",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B354:
    class Meta:
        name = "b354"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List85] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="BiblePurpose",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b354",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B355:
    class Meta:
        name = "b355"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List86] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="BibleTextOrganization",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b355",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B356:
    class Meta:
        name = "b356"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List87] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="BibleReferenceLocation",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b356",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B357:
    class Meta:
        name = "b357"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List97] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="BibleTextFeature",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b357",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B358:
    class Meta:
        name = "b358"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List89] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ReligiousTextFeatureType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b358",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B359:
    class Meta:
        name = "b359"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List90] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ReligiousTextFeatureCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b359",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B360:
    class Meta:
        name = "b360"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ReligiousTextFeatureDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b360",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B361:
    class Meta:
        name = "b361"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="IllustrationTypeDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b361",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B362:
    class Meta:
        name = "b362"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TradeAnnouncementDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b362",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B367:
    class Meta:
        name = "b367"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List73] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="WebsiteRole",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b367",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B368:
    class Meta:
        name = "b368"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List72] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ThesisType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b368",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B369:
    class Meta:
        name = "b369"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ThesisPresentedTo",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b369",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B370:
    class Meta:
        name = "b370"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ThesisYear",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b370",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B374:
    class Meta:
        name = "b374"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TextSourceCorporate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b374",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B376:
    class Meta:
        name = "b376"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ReligiousTextID",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b376",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B381:
    class Meta:
        name = "b381"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List71] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="SalesRestrictionType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b381",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B382:
    class Meta:
        name = "b382"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SalesOutletName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b382",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B383:
    class Meta:
        name = "b383"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SalesRestrictionDetail",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b383",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B384:
    class Meta:
        name = "b384"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List12] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="TradeCategory",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b384",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B385:
    class Meta:
        name = "b385"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List81] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ProductContentType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b385",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B388:
    class Meta:
        name = "b388"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: List[List49] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    refname: str = field(
        init=False,
        default="RightsTerritory",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b388",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B389:
    class Meta:
        name = "b389"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List84] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="StudyBibleType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b389",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B390:
    class Meta:
        name = "b390"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List101] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="PersonNameIDType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b390",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B391:
    class Meta:
        name = "b391"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List44] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ConferenceSponsorIDType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b391",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B392:
    class Meta:
        name = "b392"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List44] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="CopyrightOwnerIDType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b392",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B393:
    class Meta:
        name = "b393"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List102] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="SalesOutletIDType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b393",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B394:
    class Meta:
        name = "b394"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List64] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="PublishingStatus",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b394",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B395:
    class Meta:
        name = "b395"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PublishingStatusNote",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b395",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class B398:
    class Meta:
        name = "b398"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="RegionCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="b398",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class C093:
    class Meta:
        name = "c093"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List48] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="MeasureTypeCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="c093",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class C094:
    class Meta:
        name = "c094"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="Measurement",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="c094",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class C095:
    class Meta:
        name = "c095"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List50] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="MeasureUnitCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="c095",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class C096:
    class Meta:
        name = "c096"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="Height",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="c096",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class C097:
    class Meta:
        name = "c097"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="Width",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="c097",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class C098:
    class Meta:
        name = "c098"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="Thickness",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="c098",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class C099:
    class Meta:
        name = "c099"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="Weight",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="c099",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class C258:
    class Meta:
        name = "c258"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="Dimensions",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="c258",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class D100:
    class Meta:
        name = "d100"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="Annotation",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="d100",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
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
                    "type": A,
                },
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


@dataclass(slots=True)
class D101:
    class Meta:
        name = "d101"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="MainDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="d101",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
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
                    "type": A,
                },
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


@dataclass(slots=True)
class D102:
    class Meta:
        name = "d102"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List33] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="TextTypeCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="d102",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class D103:
    class Meta:
        name = "d103"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List34] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="TextFormat",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="d103",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class D104:
    class Meta:
        name = "d104"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="Text",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="d104",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
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
                    "type": A,
                },
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


@dataclass(slots=True)
class D105:
    class Meta:
        name = "d105"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List35] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="TextLinkType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="d105",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class D106:
    class Meta:
        name = "d106"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TextLink",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="d106",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class D107:
    class Meta:
        name = "d107"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TextAuthor",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="d107",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class D108:
    class Meta:
        name = "d108"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TextSourceTitle",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="d108",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class D109:
    class Meta:
        name = "d109"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TextPublicationDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="d109",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class E110:
    class Meta:
        name = "e110"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="ReviewQuote",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="e110",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
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
                    "type": A,
                },
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


@dataclass(slots=True)
class F111:
    class Meta:
        name = "f111"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List36] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="CoverImageFormatCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f111",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class F112:
    class Meta:
        name = "f112"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List37] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="CoverImageLinkTypeCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f112",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class F113:
    class Meta:
        name = "f113"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="CoverImageLink",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f113",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class F114:
    class Meta:
        name = "f114"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List38] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="MediaFileTypeCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f114",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class F115:
    class Meta:
        name = "f115"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List39] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="MediaFileFormatCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f115",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class F116:
    class Meta:
        name = "f116"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List40] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="MediaFileLinkTypeCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f116",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class F117:
    class Meta:
        name = "f117"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="MediaFileLink",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f117",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class F118:
    class Meta:
        name = "f118"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="TextWithDownload",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f118",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
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
                    "type": A,
                },
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


@dataclass(slots=True)
class F119:
    class Meta:
        name = "f119"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="DownloadCaption",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f119",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
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
                    "type": A,
                },
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


@dataclass(slots=True)
class F120:
    class Meta:
        name = "f120"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="DownloadCredit",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f120",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
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
                    "type": A,
                },
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


@dataclass(slots=True)
class F121:
    class Meta:
        name = "f121"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="DownloadCopyrightNotice",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f121",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
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
                    "type": A,
                },
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


@dataclass(slots=True)
class F122:
    class Meta:
        name = "f122"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="DownloadTerms",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f122",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
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
                    "type": A,
                },
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


@dataclass(slots=True)
class F123:
    class Meta:
        name = "f123"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ProductWebsiteLink",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f123",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class F170:
    class Meta:
        name = "f170"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="ProductWebsiteDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f170",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
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
                    "type": A,
                },
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


@dataclass(slots=True)
class F259:
    class Meta:
        name = "f259"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ImageResolution",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f259",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class F373:
    class Meta:
        name = "f373"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="MediaFileDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="f373",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class G124:
    class Meta:
        name = "g124"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PrizesDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="g124",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class G126:
    class Meta:
        name = "g126"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PrizeName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="g126",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class G127:
    class Meta:
        name = "g127"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PrizeYear",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="g127",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class G128:
    class Meta:
        name = "g128"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List91] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="PrizeCountry",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="g128",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class G129:
    class Meta:
        name = "g129"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List41] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="PrizeCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="g129",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class G343:
    class Meta:
        name = "g343"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="PrizeJury",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="g343",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
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
                    "type": A,
                },
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


@dataclass(slots=True)
class H130:
    class Meta:
        name = "h130"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ReplacedByISBN",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="h130",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class H131:
    class Meta:
        name = "h131"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ReplacedByEAN13",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="h131",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class H132:
    class Meta:
        name = "h132"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AlternativeFormatISBN",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="h132",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class H133:
    class Meta:
        name = "h133"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AlternativeFormatEAN13",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="h133",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class H134:
    class Meta:
        name = "h134"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="OutOfPrintDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="h134",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class H163:
    class Meta:
        name = "h163"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AlternativeProductISBN",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="h163",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class H164:
    class Meta:
        name = "h164"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AlternativeProductEAN13",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="h164",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class H208:
    class Meta:
        name = "h208"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List51] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="RelationCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="h208",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J135:
    class Meta:
        name = "j135"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SupplierEANLocationNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j135",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J136:
    class Meta:
        name = "j136"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SupplierSAN",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j136",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J137:
    class Meta:
        name = "j137"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SupplierName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j137",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J138:
    class Meta:
        name = "j138"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: List[List91] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    refname: str = field(
        init=False,
        default="SupplyToCountry",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j138",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J139:
    class Meta:
        name = "j139"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List52] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="SupplyToRegion",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j139",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J140:
    class Meta:
        name = "j140"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: List[List91] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    refname: str = field(
        init=False,
        default="SupplyToCountryExcluded",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j140",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J141:
    class Meta:
        name = "j141"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List54] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="AvailabilityCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j141",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J142:
    class Meta:
        name = "j142"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ExpectedShipDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j142",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J143:
    class Meta:
        name = "j143"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="OnSaleDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j143",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J144:
    class Meta:
        name = "j144"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="OrderTime",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j144",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J145:
    class Meta:
        name = "j145"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PackQuantity",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j145",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J146:
    class Meta:
        name = "j146"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List56] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="AudienceRestrictionFlag",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j146",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J147:
    class Meta:
        name = "j147"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AudienceRestrictionNote",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j147",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J148:
    class Meta:
        name = "j148"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List58] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="PriceTypeCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j148",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J149:
    class Meta:
        name = "j149"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ClassOfTrade",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j149",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J150:
    class Meta:
        name = "j150"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="BICDiscountGroupCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j150",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J151:
    class Meta:
        name = "j151"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PriceAmount",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j151",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J152:
    class Meta:
        name = "j152"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List96] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="CurrencyCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j152",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J153:
    class Meta:
        name = "j153"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List62] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="TaxRateCode1",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j153",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J154:
    class Meta:
        name = "j154"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TaxRatePercent1",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j154",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J155:
    class Meta:
        name = "j155"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TaxableAmount1",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j155",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J156:
    class Meta:
        name = "j156"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TaxAmount1",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j156",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J157:
    class Meta:
        name = "j157"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List62] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="TaxRateCode2",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j157",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J158:
    class Meta:
        name = "j158"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TaxRatePercent2",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j158",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J159:
    class Meta:
        name = "j159"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TaxableAmount2",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j159",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J160:
    class Meta:
        name = "j160"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TaxAmount2",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j160",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J161:
    class Meta:
        name = "j161"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PriceEffectiveFrom",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j161",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J162:
    class Meta:
        name = "j162"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PriceEffectiveUntil",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j162",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J192:
    class Meta:
        name = "j192"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List57] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="UnpricedItemType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j192",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J239:
    class Meta:
        name = "j239"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List60] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="PricePer",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j239",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J260:
    class Meta:
        name = "j260"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List55] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="DateFormat",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j260",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J261:
    class Meta:
        name = "j261"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List59] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="PriceQualifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j261",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J262:
    class Meta:
        name = "j262"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PriceTypeDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j262",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J263:
    class Meta:
        name = "j263"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="MinimumOrderQuantity",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j263",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J264:
    class Meta:
        name = "j264"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="BatchQuantity",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j264",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J265:
    class Meta:
        name = "j265"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="FreeQuantity",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j265",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J266:
    class Meta:
        name = "j266"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List61] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="PriceStatus",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j266",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J267:
    class Meta:
        name = "j267"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="DiscountPercent",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j267",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J268:
    class Meta:
        name = "j268"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List53] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ReturnsCodeType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j268",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J269:
    class Meta:
        name = "j269"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ReturnsCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j269",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J270:
    class Meta:
        name = "j270"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="TelephoneNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j270",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J271:
    class Meta:
        name = "j271"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="FaxNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j271",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J272:
    class Meta:
        name = "j272"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="EmailAddress",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j272",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J292:
    class Meta:
        name = "j292"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List93] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="SupplierRole",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j292",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J293:
    class Meta:
        name = "j293"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List70] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="StockQuantityCodeType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j293",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J296:
    class Meta:
        name = "j296"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="StockQuantityCodeTypeName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j296",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J297:
    class Meta:
        name = "j297"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="StockQuantityCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j297",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J302:
    class Meta:
        name = "j302"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ExpectedDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j302",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J303:
    class Meta:
        name = "j303"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: List[List49] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    refname: str = field(
        init=False,
        default="Territory",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j303",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J304:
    class Meta:
        name = "j304"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: List[List91] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    refname: str = field(
        init=False,
        default="CountryExcluded",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j304",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J308:
    class Meta:
        name = "j308"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: List[List49] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    refname: str = field(
        init=False,
        default="TerritoryExcluded",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j308",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J345:
    class Meta:
        name = "j345"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List92] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="SupplierIDType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j345",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J348:
    class Meta:
        name = "j348"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="IntermediaryAvailabilityCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j348",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J349:
    class Meta:
        name = "j349"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="LocationName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j349",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J350:
    class Meta:
        name = "j350"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="OnHand",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j350",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J351:
    class Meta:
        name = "j351"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="OnOrder",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j351",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J363:
    class Meta:
        name = "j363"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List100] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="DiscountCodeType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j363",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J364:
    class Meta:
        name = "j364"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="DiscountCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j364",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J365:
    class Meta:
        name = "j365"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ReissueDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j365",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J366:
    class Meta:
        name = "j366"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ReissueDescription",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j366",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J375:
    class Meta:
        name = "j375"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="CBO",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j375",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J377:
    class Meta:
        name = "j377"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List92] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="LocationIDType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j377",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J378:
    class Meta:
        name = "j378"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="DiscountCodeTypeName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j378",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J387:
    class Meta:
        name = "j387"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="LastDateForReturns",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j387",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J396:
    class Meta:
        name = "j396"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List65] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ProductAvailability",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j396",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J397:
    class Meta:
        name = "j397"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: List[List49] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    refname: str = field(
        init=False,
        default="SupplyToTerritory",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j397",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J399:
    class Meta:
        name = "j399"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SupplyRestrictionDetail",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j399",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J400:
    class Meta:
        name = "j400"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AgentIDType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j400",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J401:
    class Meta:
        name = "j401"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AgentName",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j401",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J402:
    class Meta:
        name = "j402"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="AgentRole",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j402",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J403:
    class Meta:
        name = "j403"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="MarketCountry",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j403",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J404:
    class Meta:
        name = "j404"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="MarketTerritory",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j404",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J405:
    class Meta:
        name = "j405"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="MarketCountryExcluded",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j405",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J406:
    class Meta:
        name = "j406"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="MarketRestrictionDetail",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j406",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J407:
    class Meta:
        name = "j407"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="MarketPublishingStatus",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j407",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class J408:
    class Meta:
        name = "j408"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="MarketDateRole",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="j408",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class K165:
    class Meta:
        name = "k165"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PromotionCampaign",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="k165",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class K166:
    class Meta:
        name = "k166"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="PromotionContact",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="k166",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class K167:
    class Meta:
        name = "k167"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="InitialPrintRun",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="k167",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class K168:
    class Meta:
        name = "k168"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="CopiesSold",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="k168",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class K169:
    class Meta:
        name = "k169"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="BookClubAdoption",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="k169",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class K309:
    class Meta:
        name = "k309"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ReprintDetail",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="k309",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M172:
    class Meta:
        name = "m172"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="FromEANNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m172",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M173:
    class Meta:
        name = "m173"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="FromSAN",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m173",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M174:
    class Meta:
        name = "m174"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="FromCompany",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m174",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M175:
    class Meta:
        name = "m175"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="FromPerson",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m175",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M176:
    class Meta:
        name = "m176"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ToEANNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m176",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M177:
    class Meta:
        name = "m177"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ToSAN",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m177",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M178:
    class Meta:
        name = "m178"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ToCompany",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m178",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M179:
    class Meta:
        name = "m179"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="ToPerson",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m179",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M180:
    class Meta:
        name = "m180"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="MessageNumber",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m180",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M181:
    class Meta:
        name = "m181"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="MessageRepeat",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m181",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M182:
    class Meta:
        name = "m182"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="SentDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m182",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M183:
    class Meta:
        name = "m183"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="MessageNote",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m183",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M184:
    class Meta:
        name = "m184"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List74] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="DefaultLanguageOfText",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m184",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M185:
    class Meta:
        name = "m185"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List58] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="DefaultPriceTypeCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m185",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M186:
    class Meta:
        name = "m186"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List96] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="DefaultCurrencyCode",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m186",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M187:
    class Meta:
        name = "m187"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List94] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="DefaultLinearUnit",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m187",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M188:
    class Meta:
        name = "m188"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List95] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="DefaultWeightUnit",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m188",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M193:
    class Meta:
        name = "m193"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="DefaultClassOfTrade",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m193",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M283:
    class Meta:
        name = "m283"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    refname: str = field(
        init=False,
        default="FromEmail",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m283",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M379:
    class Meta:
        name = "m379"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List44] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="SenderIDType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m379",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class M380:
    class Meta:
        name = "m380"
        namespace = "http://www.editeur.org/onix/2.1/short"

    value: Optional[List44] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="AddresseeIDType",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="m380",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class N338:
    class Meta:
        name = "n338"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="NoSeries",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="n338",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class N339:
    class Meta:
        name = "n339"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="NoContributor",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="n339",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class N386:
    class Meta:
        name = "n386"
        namespace = "http://www.editeur.org/onix/2.1/short"

    refname: str = field(
        init=False,
        default="NoEdition",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="n386",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Addresseeidentifier:
    class Meta:
        name = "addresseeidentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    m380: Optional[M380] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="AddresseeIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="addresseeidentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Agentidentifier:
    class Meta:
        name = "agentidentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    j400: Optional[J400] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="AgentIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="agentidentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Audience:
    class Meta:
        name = "audience"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b204: Optional[B204] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b205: Optional[B205] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b206: Optional[B206] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="Audience",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="audience",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Audiencerange:
    class Meta:
        name = "audiencerange"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b074: Optional[B074] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b075: List[B075] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    b076: List[B076] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    refname: str = field(
        init=False,
        default="AudienceRange",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="audiencerange",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Batchbonus:
    class Meta:
        name = "batchbonus"
        namespace = "http://www.editeur.org/onix/2.1/short"

    j264: Optional[J264] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    j265: Optional[J265] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="BatchBonus",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="batchbonus",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Bible:
    class Meta:
        name = "bible"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b352: List[B352] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    b353: List[B353] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    b389: Optional[B389] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b354: List[B354] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b355: Optional[B355] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b356: Optional[B356] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b357: List[B357] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="Bible",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="bible",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Complexity:
    class Meta:
        name = "complexity"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b077: Optional[B077] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b078: Optional[B078] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="Complexity",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="complexity",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Conferencesponsoridentifier:
    class Meta:
        name = "conferencesponsoridentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b391: Optional[B391] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ConferenceSponsorIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="conferencesponsoridentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Copyrightowneridentifier:
    class Meta:
        name = "copyrightowneridentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b392: Optional[B392] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="CopyrightOwnerIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="copyrightowneridentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Discountcoded:
    class Meta:
        name = "discountcoded"
        namespace = "http://www.editeur.org/onix/2.1/short"

    j363: Optional[J363] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    j378: Optional[J378] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j364: Optional[J364] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="DiscountCoded",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="discountcoded",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Extent:
    class Meta:
        name = "extent"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b218: Optional[B218] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b219: Optional[B219] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b220: Optional[B220] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="Extent",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="extent",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Illustrations:
    class Meta:
        name = "illustrations"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b256: Optional[B256] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b361: Optional[B361] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b257: Optional[B257] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="Illustrations",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="illustrations",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Imprint:
    class Meta:
        name = "imprint"
        namespace = "http://www.editeur.org/onix/2.1/short"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b079",
                    "type": B079,
                },
                {
                    "name": "b241",
                    "type": B241,
                },
                {
                    "name": "b242",
                    "type": B242,
                },
                {
                    "name": "b243",
                    "type": B243,
                },
            ),
            "max_occurs": 5,
        }
    )
    refname: str = field(
        init=False,
        default="Imprint",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="imprint",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Language:
    class Meta:
        name = "language"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b253: Optional[B253] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b252: Optional[B252] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b251: Optional[B251] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="Language",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="language",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Locationidentifier:
    class Meta:
        name = "locationidentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    j377: Optional[J377] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="LocationIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="locationidentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Mainsubject:
    class Meta:
        name = "mainsubject"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b191: Optional[B191] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b068: Optional[B068] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b069_or_b070: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b069",
                    "type": B069,
                },
                {
                    "name": "b070",
                    "type": B070,
                },
            ),
            "max_occurs": 2,
        }
    )
    refname: str = field(
        init=False,
        default="MainSubject",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="mainsubject",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Marketdate:
    class Meta:
        name = "marketdate"
        namespace = "http://www.editeur.org/onix/2.1/short"

    j408: Optional[J408] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    j260: Optional[J260] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b306: Optional[B306] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="MarketDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="marketdate",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Measure:
    class Meta:
        name = "measure"
        namespace = "http://www.editeur.org/onix/2.1/short"

    c093: Optional[C093] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    c094: Optional[C094] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    c095: Optional[C095] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="Measure",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="measure",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Mediafile:
    class Meta:
        name = "mediafile"
        namespace = "http://www.editeur.org/onix/2.1/short"

    f114: Optional[F114] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    f115: Optional[F115] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    f259: Optional[F259] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    f116: Optional[F116] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    f117: Optional[F117] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    f118: Optional[F118] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    f119: Optional[F119] = field(
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
                    "name": "f120",
                    "type": F120,
                },
                {
                    "name": "f121",
                    "type": F121,
                },
                {
                    "name": "f122",
                    "type": F122,
                },
                {
                    "name": "f373",
                    "type": F373,
                },
            ),
            "max_occurs": 7,
        }
    )
    refname: str = field(
        init=False,
        default="MediaFile",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="mediafile",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Onorderdetail:
    class Meta:
        name = "onorderdetail"
        namespace = "http://www.editeur.org/onix/2.1/short"

    j351: Optional[J351] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    j302: Optional[J302] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="OnOrderDetail",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="onorderdetail",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Othertext:
    class Meta:
        name = "othertext"
        namespace = "http://www.editeur.org/onix/2.1/short"

    d102: Optional[D102] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    d103: Optional[D103] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    d104: Optional[D104] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    d105: Optional[D105] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    d106: Optional[D106] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    d107: Optional[D107] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b374: Optional[B374] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    d108: Optional[D108] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    d109: Optional[D109] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b324: Optional[B324] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b325: Optional[B325] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="OtherText",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="othertext",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Pagerun:
    class Meta:
        name = "pagerun"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b286: Optional[B286] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b287: Optional[B287] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="PageRun",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="pagerun",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Parentidentifier:
    class Meta:
        name = "parentidentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b273: Optional[B273] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ParentIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="parentidentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Persondate:
    class Meta:
        name = "persondate"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b305: Optional[B305] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    j260: Optional[J260] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b306: Optional[B306] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="PersonDate",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="persondate",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Personnameidentifier:
    class Meta:
        name = "personnameidentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b390: Optional[B390] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="PersonNameIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="personnameidentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Prize:
    class Meta:
        name = "prize"
        namespace = "http://www.editeur.org/onix/2.1/short"

    g126: Optional[G126] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    g127: Optional[G127] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    g128: Optional[G128] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    g129: Optional[G129] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    g343: Optional[G343] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="Prize",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="prize",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Productclassification:
    class Meta:
        name = "productclassification"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b274: Optional[B274] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b275: Optional[B275] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b337: Optional[B337] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="ProductClassification",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="productclassification",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Productformfeature:
    class Meta:
        name = "productformfeature"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b334: Optional[B334] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b335: Optional[B335] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b336: Optional[B336] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="ProductFormFeature",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="productformfeature",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Productidentifier:
    class Meta:
        name = "productidentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b221: Optional[B221] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ProductIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="productidentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Productwebsite:
    class Meta:
        name = "productwebsite"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b367: Optional[B367] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    f170: Optional[F170] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    f123: Optional[F123] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="ProductWebsite",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="productwebsite",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Professionalaffiliation:
    class Meta:
        name = "professionalaffiliation"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b045_or_b046: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b045",
                    "type": B045,
                },
                {
                    "name": "b046",
                    "type": B046,
                },
            ),
            "max_occurs": 2,
        }
    )
    refname: str = field(
        init=False,
        default="ProfessionalAffiliation",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="professionalaffiliation",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Religioustextfeature:
    class Meta:
        name = "religioustextfeature"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b358: Optional[B358] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b359: Optional[B359] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b360: Optional[B360] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="ReligiousTextFeature",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="religioustextfeature",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Salesoutletidentifier:
    class Meta:
        name = "salesoutletidentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b393: Optional[B393] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="SalesOutletIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="salesoutletidentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Salesrights:
    class Meta:
        name = "salesrights"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b089: Optional[B089] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b090_or_b388_or_b091: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b090",
                    "type": B090,
                },
                {
                    "name": "b388",
                    "type": B388,
                },
                {
                    "name": "b091",
                    "type": B091,
                },
            ),
        }
    )
    refname: str = field(
        init=False,
        default="SalesRights",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="salesrights",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Senderidentifier:
    class Meta:
        name = "senderidentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    m379: Optional[M379] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="SenderIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="senderidentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Seriesidentifier:
    class Meta:
        name = "seriesidentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b273: Optional[B273] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="SeriesIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="seriesidentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Stockquantitycoded:
    class Meta:
        name = "stockquantitycoded"
        namespace = "http://www.editeur.org/onix/2.1/short"

    j293: Optional[J293] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    j296: Optional[J296] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j297: Optional[J297] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="StockQuantityCoded",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="stockquantitycoded",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Subject:
    class Meta:
        name = "subject"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b067: Optional[B067] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b171: Optional[B171] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b068: Optional[B068] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b069_or_b070: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b069",
                    "type": B069,
                },
                {
                    "name": "b070",
                    "type": B070,
                },
            ),
            "max_occurs": 2,
        }
    )
    refname: str = field(
        init=False,
        default="Subject",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="subject",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Supplieridentifier:
    class Meta:
        name = "supplieridentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    j345: Optional[J345] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="SupplierIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="supplieridentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Textitemidentifier:
    class Meta:
        name = "textitemidentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b285: Optional[B285] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="TextItemIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="textitemidentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Title:
    class Meta:
        name = "title"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b202: Optional[B202] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b276: Optional[B276] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b027: Optional[B027] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b203: Optional[B203] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b030_or_b031_or_b029: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b030",
                    "type": B030,
                },
                {
                    "name": "b031",
                    "type": B031,
                },
                {
                    "name": "b029",
                    "type": B029,
                },
            ),
            "max_occurs": 5,
        }
    )
    refname: str = field(
        init=False,
        default="Title",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="title",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Website:
    class Meta:
        name = "website"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b367: Optional[B367] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b294: Optional[B294] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b295: Optional[B295] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="Website",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="website",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Workidentifier:
    class Meta:
        name = "workidentifier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b201: Optional[B201] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b233: Optional[B233] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b244: Optional[B244] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    refname: str = field(
        init=False,
        default="WorkIdentifier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="workidentifier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Conferencesponsor:
    class Meta:
        name = "conferencesponsor"
        namespace = "http://www.editeur.org/onix/2.1/short"

    conferencesponsoridentifier: Optional[Conferencesponsoridentifier] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b036_or_b047: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b036",
                    "type": B036,
                },
                {
                    "name": "b047",
                    "type": B047,
                },
            ),
            "max_occurs": 2,
        }
    )
    refname: str = field(
        init=False,
        default="ConferenceSponsor",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="conferencesponsor",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Containeditem:
    class Meta:
        name = "containeditem"
        namespace = "http://www.editeur.org/onix/2.1/short"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b004",
                    "type": B004,
                },
                {
                    "name": "b005",
                    "type": B005,
                },
                {
                    "name": "productidentifier",
                    "type": Productidentifier,
                },
                {
                    "name": "b012",
                    "type": B012,
                },
                {
                    "name": "b333",
                    "type": B333,
                },
                {
                    "name": "productformfeature",
                    "type": Productformfeature,
                },
                {
                    "name": "b013",
                    "type": B013,
                },
            ),
        }
    )
    choice_1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b225",
                    "type": B225,
                },
                {
                    "name": "b014",
                    "type": B014,
                },
                {
                    "name": "b210",
                    "type": B210,
                },
                {
                    "name": "b384",
                    "type": B384,
                },
            ),
            "max_occurs": 10,
        }
    )
    b385: List[B385] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b015: Optional[B015] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="ContainedItem",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="containeditem",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Copyrightowner:
    class Meta:
        name = "copyrightowner"
        namespace = "http://www.editeur.org/onix/2.1/short"

    copyrightowneridentifier: Optional[Copyrightowneridentifier] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b036_or_b047: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b036",
                    "type": B036,
                },
                {
                    "name": "b047",
                    "type": B047,
                },
            ),
            "max_occurs": 2,
        }
    )
    refname: str = field(
        init=False,
        default="CopyrightOwner",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="copyrightowner",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Header:
    class Meta:
        name = "header"
        namespace = "http://www.editeur.org/onix/2.1/short"

    m172_or_m173_or_senderidentifier: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "m172",
                    "type": M172,
                },
                {
                    "name": "m173",
                    "type": M173,
                },
                {
                    "name": "senderidentifier",
                    "type": Senderidentifier,
                },
            ),
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "m174",
                    "type": M174,
                },
                {
                    "name": "m175",
                    "type": M175,
                },
                {
                    "name": "m283",
                    "type": M283,
                },
                {
                    "name": "m176",
                    "type": M176,
                },
                {
                    "name": "m177",
                    "type": M177,
                },
            ),
            "max_occurs": 8,
        }
    )
    addresseeidentifier: List[Addresseeidentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    m178: Optional[M178] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    m179: Optional[M179] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    m180: Optional[M180] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    m181: Optional[M181] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    m182: Optional[M182] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    m183: Optional[M183] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    m184: Optional[M184] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    m185: Optional[M185] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    m186: Optional[M186] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    m187: Optional[M187] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    m188: Optional[M188] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    m193: Optional[M193] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="Header",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="header",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Marketrepresentation:
    class Meta:
        name = "marketrepresentation"
        namespace = "http://www.editeur.org/onix/2.1/short"

    agentidentifier_or_j401: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "agentidentifier",
                    "type": Agentidentifier,
                },
                {
                    "name": "j401",
                    "type": J401,
                },
            ),
        }
    )
    j270: List[J270] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j271: List[J271] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j272: List[J272] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    website: List[Website] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j402: Optional[J402] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j403: Optional[J403] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j404: Optional[J404] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j405: Optional[J405] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j406: Optional[J406] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j407: Optional[J407] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    marketdate: List[Marketdate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="MarketRepresentation",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="marketrepresentation",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Name:
    class Meta:
        name = "name"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b250: Optional[B250] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b036",
                    "type": B036,
                },
                {
                    "name": "b037",
                    "type": B037,
                },
                {
                    "name": "b038",
                    "type": B038,
                },
                {
                    "name": "b039",
                    "type": B039,
                },
                {
                    "name": "b247",
                    "type": B247,
                },
                {
                    "name": "b040",
                    "type": B040,
                },
                {
                    "name": "b041",
                    "type": B041,
                },
                {
                    "name": "b248",
                    "type": B248,
                },
                {
                    "name": "b042",
                    "type": B042,
                },
                {
                    "name": "b043",
                    "type": B043,
                },
                {
                    "name": "personnameidentifier",
                    "type": Personnameidentifier,
                },
            ),
        }
    )
    refname: str = field(
        init=False,
        default="Name",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="name",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Newsupplier:
    class Meta:
        name = "newsupplier"
        namespace = "http://www.editeur.org/onix/2.1/short"

    supplieridentifier: List[Supplieridentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j136_or_j135_or_j137: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "j136",
                    "type": J136,
                },
                {
                    "name": "j135",
                    "type": J135,
                },
                {
                    "name": "j137",
                    "type": J137,
                },
            ),
            "max_occurs": 5,
        }
    )
    j270: List[J270] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j271: List[J271] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j272: List[J272] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="NewSupplier",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="newsupplier",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Notforsale:
    class Meta:
        name = "notforsale"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b090: List[B090] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b388_or_b004_or_b005: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b388",
                    "type": B388,
                },
                {
                    "name": "b004",
                    "type": B004,
                },
                {
                    "name": "b005",
                    "type": B005,
                },
            ),
            "max_occurs": 4,
        }
    )
    productidentifier: List[Productidentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b081: Optional[B081] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="NotForSale",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="notforsale",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Price:
    class Meta:
        name = "price"
        namespace = "http://www.editeur.org/onix/2.1/short"

    j148: Optional[J148] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j261: Optional[J261] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j262: Optional[J262] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j239: Optional[J239] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j263: Optional[J263] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    batchbonus: List[Batchbonus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j149: Optional[J149] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j150: Optional[J150] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    discountcoded: List[Discountcoded] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j267: Optional[J267] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j266: Optional[J266] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j151: Optional[J151] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    j152: Optional[J152] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b251: List[B251] = field(
        default_factory=list,
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
                    "name": "j303",
                    "type": J303,
                },
                {
                    "name": "j304",
                    "type": J304,
                },
                {
                    "name": "j308",
                    "type": J308,
                },
                {
                    "name": "j153",
                    "type": J153,
                },
                {
                    "name": "j154",
                    "type": J154,
                },
                {
                    "name": "j155",
                    "type": J155,
                },
                {
                    "name": "j156",
                    "type": J156,
                },
                {
                    "name": "j157",
                    "type": J157,
                },
                {
                    "name": "j158",
                    "type": J158,
                },
                {
                    "name": "j159",
                    "type": J159,
                },
                {
                    "name": "j160",
                    "type": J160,
                },
                {
                    "name": "j161",
                    "type": J161,
                },
                {
                    "name": "j162",
                    "type": J162,
                },
            ),
            "max_occurs": 14,
        }
    )
    refname: str = field(
        init=False,
        default="Price",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="price",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Publisher:
    class Meta:
        name = "publisher"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b291: Optional[B291] = field(
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
                    "name": "b081",
                    "type": B081,
                },
                {
                    "name": "b241",
                    "type": B241,
                },
                {
                    "name": "b242",
                    "type": B242,
                },
                {
                    "name": "b243",
                    "type": B243,
                },
            ),
            "max_occurs": 5,
        }
    )
    website: List[Website] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="Publisher",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="publisher",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Religioustext:
    class Meta:
        name = "religioustext"
        namespace = "http://www.editeur.org/onix/2.1/short"

    bible_or_b376_or_religioustextfeature: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "bible",
                    "type": Bible,
                },
                {
                    "name": "b376",
                    "type": B376,
                },
                {
                    "name": "religioustextfeature",
                    "type": Religioustextfeature,
                },
            ),
        }
    )
    refname: str = field(
        init=False,
        default="ReligiousText",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="religioustext",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Salesoutlet:
    class Meta:
        name = "salesoutlet"
        namespace = "http://www.editeur.org/onix/2.1/short"

    salesoutletidentifier_or_b382: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "salesoutletidentifier",
                    "type": Salesoutletidentifier,
                },
                {
                    "name": "b382",
                    "type": B382,
                },
            ),
            "max_occurs": 2,
        }
    )
    refname: str = field(
        init=False,
        default="SalesOutlet",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="salesoutlet",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Set:
    class Meta:
        name = "set"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b021: Optional[B021] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b022: Optional[B022] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    productidentifier: List[Productidentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b023_or_title: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b023",
                    "type": B023,
                },
                {
                    "name": "title",
                    "type": Title,
                },
            ),
        }
    )
    b024: Optional[B024] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b025: Optional[B025] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b026: Optional[B026] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b284: Optional[B284] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b281: Optional[B281] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="Set",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="set",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Stock:
    class Meta:
        name = "stock"
        namespace = "http://www.editeur.org/onix/2.1/short"

    locationidentifier: Optional[Locationidentifier] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j349: Optional[J349] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    stockquantitycoded: Optional[Stockquantitycoded] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j350_or_j351_or_j375: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "j350",
                    "type": J350,
                },
                {
                    "name": "j351",
                    "type": J351,
                },
                {
                    "name": "j375",
                    "type": J375,
                },
            ),
            "max_occurs": 4,
        }
    )
    onorderdetail: List[Onorderdetail] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="Stock",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="stock",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Textitem:
    class Meta:
        name = "textitem"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b290: Optional[B290] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    textitemidentifier: List[Textitemidentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b286_or_b287_or_pagerun: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b286",
                    "type": B286,
                },
                {
                    "name": "b287",
                    "type": B287,
                },
                {
                    "name": "pagerun",
                    "type": Pagerun,
                },
            ),
        }
    )
    b061: Optional[B061] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="TextItem",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="textitem",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Conference:
    class Meta:
        name = "conference"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b051: Optional[B051] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b052: Optional[B052] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b341: Optional[B341] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b053: Optional[B053] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b342: Optional[B342] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b054: Optional[B054] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b055: Optional[B055] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    conferencesponsor: List[Conferencesponsor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    website: List[Website] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="Conference",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="conference",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Contributor:
    class Meta:
        name = "contributor"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b034: Optional[B034] = field(
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
                    "name": "b035",
                    "type": B035,
                },
                {
                    "name": "b252",
                    "type": B252,
                },
                {
                    "name": "b340",
                    "type": B340,
                },
                {
                    "name": "b036",
                    "type": B036,
                },
                {
                    "name": "b037",
                    "type": B037,
                },
                {
                    "name": "b038",
                    "type": B038,
                },
                {
                    "name": "b039",
                    "type": B039,
                },
                {
                    "name": "b247",
                    "type": B247,
                },
                {
                    "name": "b040",
                    "type": B040,
                },
                {
                    "name": "b041",
                    "type": B041,
                },
                {
                    "name": "b248",
                    "type": B248,
                },
                {
                    "name": "b042",
                    "type": B042,
                },
                {
                    "name": "b043",
                    "type": B043,
                },
            ),
        }
    )
    name_or_personnameidentifier: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "personnameidentifier",
                    "type": Personnameidentifier,
                },
            ),
        }
    )
    persondate_or_professionalaffiliation_or_b047: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "persondate",
                    "type": Persondate,
                },
                {
                    "name": "professionalaffiliation",
                    "type": Professionalaffiliation,
                },
                {
                    "name": "b047",
                    "type": B047,
                },
            ),
        }
    )
    choice_1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b044",
                    "type": B044,
                },
                {
                    "name": "website",
                    "type": Website,
                },
                {
                    "name": "b045",
                    "type": B045,
                },
                {
                    "name": "b046",
                    "type": B046,
                },
                {
                    "name": "b048",
                    "type": B048,
                },
                {
                    "name": "b249",
                    "type": B249,
                },
            ),
        }
    )
    b251: List[B251] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b398: List[B398] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="Contributor",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="contributor",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Copyrightstatement:
    class Meta:
        name = "copyrightstatement"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b087: List[B087] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    copyrightowner: List[Copyrightowner] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    refname: str = field(
        init=False,
        default="CopyrightStatement",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="copyrightstatement",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Personassubject:
    class Meta:
        name = "personassubject"
        namespace = "http://www.editeur.org/onix/2.1/short"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b036",
                    "type": B036,
                },
                {
                    "name": "b037",
                    "type": B037,
                },
                {
                    "name": "b038",
                    "type": B038,
                },
                {
                    "name": "b039",
                    "type": B039,
                },
                {
                    "name": "b247",
                    "type": B247,
                },
                {
                    "name": "b040",
                    "type": B040,
                },
                {
                    "name": "b041",
                    "type": B041,
                },
                {
                    "name": "b248",
                    "type": B248,
                },
                {
                    "name": "b042",
                    "type": B042,
                },
                {
                    "name": "b043",
                    "type": B043,
                },
                {
                    "name": "name",
                    "type": Name,
                },
                {
                    "name": "personnameidentifier",
                    "type": Personnameidentifier,
                },
            ),
        }
    )
    refname: str = field(
        init=False,
        default="PersonAsSubject",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="personassubject",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Reissue:
    class Meta:
        name = "reissue"
        namespace = "http://www.editeur.org/onix/2.1/short"

    j365: Optional[J365] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    j366: Optional[J366] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    price: List[Price] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mediafile: List[Mediafile] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="Reissue",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="reissue",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Relatedproduct:
    class Meta:
        name = "relatedproduct"
        namespace = "http://www.editeur.org/onix/2.1/short"

    h208: Optional[H208] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b004",
                    "type": B004,
                },
                {
                    "name": "b005",
                    "type": B005,
                },
                {
                    "name": "productidentifier",
                    "type": Productidentifier,
                },
                {
                    "name": "website",
                    "type": Website,
                },
                {
                    "name": "b012",
                    "type": B012,
                },
                {
                    "name": "b333",
                    "type": B333,
                },
                {
                    "name": "productformfeature",
                    "type": Productformfeature,
                },
                {
                    "name": "b013",
                    "type": B013,
                },
            ),
        }
    )
    choice_1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b225",
                    "type": B225,
                },
                {
                    "name": "b014",
                    "type": B014,
                },
                {
                    "name": "b210",
                    "type": B210,
                },
                {
                    "name": "b384",
                    "type": B384,
                },
            ),
            "max_occurs": 10,
        }
    )
    b385: List[B385] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b211: Optional[B211] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b212: Optional[B212] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b213: Optional[B213] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b214: Optional[B214] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b215: Optional[B215] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b216: Optional[B216] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b277: Optional[B277] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    publisher: List[Publisher] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="RelatedProduct",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="relatedproduct",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Salesrestriction:
    class Meta:
        name = "salesrestriction"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b381: Optional[B381] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    salesoutlet: List[Salesoutlet] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b383: Optional[B383] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="SalesRestriction",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="salesrestriction",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Contentitem:
    class Meta:
        name = "contentitem"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b284: Optional[B284] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    textitem: Optional[Textitem] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    website: List[Website] = field(
        default_factory=list,
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
                    "name": "b288",
                    "type": B288,
                },
                {
                    "name": "b289",
                    "type": B289,
                },
                {
                    "name": "b028",
                    "type": B028,
                },
                {
                    "name": "title",
                    "type": Title,
                },
            ),
        }
    )
    workidentifier: List[Workidentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    contributor: List[Contributor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b049: Optional[B049] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    subject: List[Subject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    personassubject: List[Personassubject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b071: List[B071] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b072: List[B072] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    othertext: List[Othertext] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mediafile: List[Mediafile] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="ContentItem",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="contentitem",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Mainseriesrecord:
    class Meta:
        name = "mainseriesrecord"
        namespace = "http://www.editeur.org/onix/2.1/short"

    a001: Optional[A001] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    a002: Optional[A002] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    a198: Optional[A198] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a199: Optional[A199] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a194: Optional[A194] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a195: Optional[A195] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a196: Optional[A196] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a197: Optional[A197] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    seriesidentifier: List[Seriesidentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    contributor: List[Contributor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    othertext: List[Othertext] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    publisher: List[Publisher] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    a245: Optional[A245] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="MainSeriesRecord",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="mainseriesrecord",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Series:
    class Meta:
        name = "series"
        namespace = "http://www.editeur.org/onix/2.1/short"

    b016: Optional[B016] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b017: Optional[B017] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    seriesidentifier: List[Seriesidentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b018_or_title: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b018",
                    "type": B018,
                },
                {
                    "name": "title",
                    "type": Title,
                },
            ),
        }
    )
    contributor: List[Contributor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b019: Optional[B019] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b020: Optional[B020] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="Series",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="series",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Subseriesrecord:
    class Meta:
        name = "subseriesrecord"
        namespace = "http://www.editeur.org/onix/2.1/short"

    a001: Optional[A001] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    a002: Optional[A002] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    a198: Optional[A198] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a199: Optional[A199] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a194: Optional[A194] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a195: Optional[A195] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a196: Optional[A196] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a197: Optional[A197] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    seriesidentifier: List[Seriesidentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    parentidentifier: Optional[Parentidentifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b284: Optional[B284] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    b282: Optional[B282] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b019: Optional[B019] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    contributor: List[Contributor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    othertext: List[Othertext] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    publisher: List[Publisher] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    a245: Optional[A245] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="SubSeriesRecord",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="subseriesrecord",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Supplydetail:
    class Meta:
        name = "supplydetail"
        namespace = "http://www.editeur.org/onix/2.1/short"

    supplieridentifier: List[Supplieridentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j136_or_j135_or_j137: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "j136",
                    "type": J136,
                },
                {
                    "name": "j135",
                    "type": J135,
                },
                {
                    "name": "j137",
                    "type": J137,
                },
            ),
            "max_occurs": 5,
        }
    )
    j270: List[J270] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j271: List[J271] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j272: List[J272] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    website: List[Website] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j292: Optional[J292] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j138_or_j397_or_j139: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "j138",
                    "type": J138,
                },
                {
                    "name": "j397",
                    "type": J397,
                },
                {
                    "name": "j139",
                    "type": J139,
                },
            ),
        }
    )
    j140: List[J140] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j399: Optional[J399] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j268: Optional[J268] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j269: Optional[J269] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j387: Optional[J387] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j141: Optional[J141] = field(
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
                    "name": "j396",
                    "type": J396,
                },
                {
                    "name": "j348",
                    "type": J348,
                },
                {
                    "name": "newsupplier",
                    "type": Newsupplier,
                },
                {
                    "name": "j260",
                    "type": J260,
                },
                {
                    "name": "j142",
                    "type": J142,
                },
                {
                    "name": "j143",
                    "type": J143,
                },
                {
                    "name": "j144",
                    "type": J144,
                },
            ),
            "max_occurs": 10,
        }
    )
    stock: List[Stock] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    j145: Optional[J145] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j146: Optional[J146] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j147: Optional[J147] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    j151_or_j192_or_price: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "j151",
                    "type": J151,
                },
                {
                    "name": "j192",
                    "type": J192,
                },
                {
                    "name": "price",
                    "type": Price,
                },
            ),
        }
    )
    reissue: Optional[Reissue] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="SupplyDetail",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="supplydetail",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Product:
    class Meta:
        name = "product"
        namespace = "http://www.editeur.org/onix/2.1/short"

    a001: Optional[A001] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    a002: Optional[A002] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    a198: Optional[A198] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a199: Optional[A199] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a194: Optional[A194] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a195: Optional[A195] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a196: Optional[A196] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    a197: Optional[A197] = field(
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
                    "name": "b004",
                    "type": B004,
                },
                {
                    "name": "b005",
                    "type": B005,
                },
                {
                    "name": "b006",
                    "type": B006,
                },
                {
                    "name": "b007",
                    "type": B007,
                },
                {
                    "name": "b008",
                    "type": B008,
                },
                {
                    "name": "b009",
                    "type": B009,
                },
                {
                    "name": "productidentifier",
                    "type": Productidentifier,
                },
            ),
        }
    )
    b246: List[B246] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b010: Optional[B010] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b011: Optional[B011] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b012: Optional[B012] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b333: List[B333] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    productformfeature: List[Productformfeature] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b013: List[B013] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b225: Optional[B225] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b014: Optional[B014] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b210: Optional[B210] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b384: Optional[B384] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b385: List[B385] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    containeditem: List[Containeditem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    productclassification: List[Productclassification] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b211: Optional[B211] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b212: Optional[B212] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b213: Optional[B213] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b214: Optional[B214] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b215: Optional[B215] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b216: Optional[B216] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b278: Optional[B278] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b279: Optional[B279] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b280: Optional[B280] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b277: Optional[B277] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    series_or_n338: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "series",
                    "type": Series,
                },
                {
                    "name": "n338",
                    "type": N338,
                },
            ),
        }
    )
    set: List[Set] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b027: Optional[B027] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b028: Optional[B028] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    choice_1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b030",
                    "type": B030,
                },
                {
                    "name": "b031",
                    "type": B031,
                },
                {
                    "name": "b029",
                    "type": B029,
                },
                {
                    "name": "b032",
                    "type": B032,
                },
            ),
            "max_occurs": 6,
        }
    )
    b033_or_title: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b033",
                    "type": B033,
                },
                {
                    "name": "title",
                    "type": Title,
                },
            ),
        }
    )
    workidentifier: List[Workidentifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    website: List[Website] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b368: Optional[B368] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b369: Optional[B369] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b370: Optional[B370] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    contributor_or_b049_or_n339: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "contributor",
                    "type": Contributor,
                },
                {
                    "name": "b049",
                    "type": B049,
                },
                {
                    "name": "n339",
                    "type": N339,
                },
            ),
        }
    )
    choice_2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b050",
                    "type": B050,
                },
                {
                    "name": "b051",
                    "type": B051,
                },
                {
                    "name": "b052",
                    "type": B052,
                },
                {
                    "name": "b053",
                    "type": B053,
                },
                {
                    "name": "b054",
                    "type": B054,
                },
                {
                    "name": "b055",
                    "type": B055,
                },
                {
                    "name": "conference",
                    "type": Conference,
                },
            ),
        }
    )
    choice_3: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b056",
                    "type": B056,
                },
                {
                    "name": "b057",
                    "type": B057,
                },
                {
                    "name": "b217",
                    "type": B217,
                },
                {
                    "name": "b058",
                    "type": B058,
                },
                {
                    "name": "n386",
                    "type": N386,
                },
            ),
        }
    )
    religioustext: Optional[Religioustext] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b059: List[B059] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b060: Optional[B060] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    language: List[Language] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b061: Optional[B061] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b254: Optional[B254] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b255: Optional[B255] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    extent: List[Extent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b125: Optional[B125] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b062: Optional[B062] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    illustrations: List[Illustrations] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b063: List[B063] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b064: Optional[B064] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b200: Optional[B200] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b065: Optional[B065] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b066: Optional[B066] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mainsubject: List[Mainsubject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    subject: List[Subject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    personassubject: List[Personassubject] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b071: List[B071] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b072: List[B072] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b073: List[B073] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    audience: List[Audience] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b189: Optional[B189] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b190: Optional[B190] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    audiencerange: List[Audiencerange] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b207: Optional[B207] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    complexity: List[Complexity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    d100: Optional[D100] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    d101: Optional[D101] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    othertext: List[Othertext] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    e110: List[E110] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    f111: Optional[F111] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    f112: Optional[F112] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    f113: Optional[F113] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mediafile: List[Mediafile] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    productwebsite: List[Productwebsite] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    g124_or_prize: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g124",
                    "type": G124,
                },
                {
                    "name": "prize",
                    "type": Prize,
                },
            ),
        }
    )
    contentitem: List[Contentitem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    choice_4: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b079",
                    "type": B079,
                },
                {
                    "name": "imprint",
                    "type": Imprint,
                },
                {
                    "name": "b081",
                    "type": B081,
                },
                {
                    "name": "publisher",
                    "type": Publisher,
                },
            ),
        }
    )
    b209: List[B209] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b083: Optional[B083] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b084: List[B084] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b085: List[B085] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    b240: Optional[B240] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b394: Optional[B394] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b395: Optional[B395] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b086: Optional[B086] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b362: Optional[B362] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    b003: Optional[B003] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    copyrightstatement_or_b087: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "copyrightstatement",
                    "type": Copyrightstatement,
                },
                {
                    "name": "b087",
                    "type": B087,
                },
            ),
        }
    )
    b088: Optional[B088] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    salesrights: List[Salesrights] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 3,
        }
    )
    notforsale: List[Notforsale] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    salesrestriction: List[Salesrestriction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    choice_5: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c096",
                    "type": C096,
                },
                {
                    "name": "c097",
                    "type": C097,
                },
                {
                    "name": "c098",
                    "type": C098,
                },
                {
                    "name": "c099",
                    "type": C099,
                },
                {
                    "name": "measure",
                    "type": Measure,
                },
            ),
        }
    )
    choice_6: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c258",
                    "type": C258,
                },
                {
                    "name": "h130",
                    "type": H130,
                },
                {
                    "name": "h131",
                    "type": H131,
                },
                {
                    "name": "h132",
                    "type": H132,
                },
                {
                    "name": "h133",
                    "type": H133,
                },
                {
                    "name": "h163",
                    "type": H163,
                },
                {
                    "name": "h164",
                    "type": H164,
                },
            ),
            "max_occurs": 8,
        }
    )
    relatedproduct: List[Relatedproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    h134: Optional[H134] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    supplydetail: List[Supplydetail] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    marketrepresentation: List[Marketrepresentation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    k165: Optional[K165] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    k166: Optional[K166] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    k167: Optional[K167] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    k309: List[K309] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    k168: Optional[K168] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    k169: Optional[K169] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    refname: str = field(
        init=False,
        default="Product",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="product",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language_attribute: Optional[List74] = field(
        default=None,
        metadata={
            "name": "language",
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class Onixmessage:
    class Meta:
        name = "ONIXmessage"
        namespace = "http://www.editeur.org/onix/2.1/short"

    header: Optional[Header] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    product_or_mainseriesrecord_or_subseriesrecord: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "product",
                    "type": Product,
                },
                {
                    "name": "mainseriesrecord",
                    "type": Mainseriesrecord,
                },
                {
                    "name": "subseriesrecord",
                    "type": Subseriesrecord,
                },
            ),
        }
    )
    refname: str = field(
        init=False,
        default="ONIXMessage",
        metadata={
            "type": "Attribute",
        }
    )
    shortname: str = field(
        init=False,
        default="ONIXmessage",
        metadata={
            "type": "Attribute",
        }
    )
    release: str = field(
        init=False,
        default="2.1",
        metadata={
            "type": "Attribute",
        }
    )
    textformat: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
