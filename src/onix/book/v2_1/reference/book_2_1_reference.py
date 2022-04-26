from dataclasses import dataclass, field
from typing import List, Optional
from onix.book.v2_1.reference.onix_book_product_code_lists import (
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
from onix.book.v2_1.reference.onix_xhtml_subset import (
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

__NAMESPACE__ = "http://www.editeur.org/onix/2.1/reference"


@dataclass(slots=True)
class AbbreviatedLength:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AddresseeIdtype:
    class Meta:
        name = "AddresseeIDType"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Affiliation:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AgentIdtype:
    class Meta:
        name = "AgentIDType"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AgentName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AgentRole:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AlternativeFormatEan13:
    class Meta:
        name = "AlternativeFormatEAN13"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AlternativeFormatIsbn:
    class Meta:
        name = "AlternativeFormatISBN"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AlternativeProductEan13:
    class Meta:
        name = "AlternativeProductEAN13"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AlternativeProductIsbn:
    class Meta:
        name = "AlternativeProductISBN"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Annotation:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AnnouncementDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AudienceCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AudienceCodeType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AudienceCodeTypeName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AudienceCodeValue:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AudienceDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AudienceRangePrecision:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AudienceRangeQualifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AudienceRangeValue:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AudienceRestrictionFlag:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AudienceRestrictionNote:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AvailabilityCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class BasicmainSubject:
    class Meta:
        name = "BASICMainSubject"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Basicversion:
    class Meta:
        name = "BASICVersion"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class BicdiscountGroupCode:
    class Meta:
        name = "BICDiscountGroupCode"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class BicmainSubject:
    class Meta:
        name = "BICMainSubject"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Bicversion:
    class Meta:
        name = "BICVersion"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Barcode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class BatchQuantity:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class BibleContents:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class BiblePurpose:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class BibleReferenceLocation:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class BibleTextFeature:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class BibleTextOrganization:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class BibleVersion:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class BiographicalNote:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class BookClubAdoption:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class BookFormDetail:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Cbo:
    class Meta:
        name = "CBO"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CityOfPublication:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ClassOfTrade:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ComplexityCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ComplexitySchemeIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ComponentNumber:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ComponentTypeName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ConferenceAcronym:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ConferenceDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ConferenceDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ConferenceName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ConferenceNumber:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ConferencePlace:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ConferenceRole:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ConferenceSponsorIdtype:
    class Meta:
        name = "ConferenceSponsorIDType"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ConferenceTheme:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ContributorDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ContributorRole:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ContributorStatement:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CopiesSold:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CopublisherName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CopyrightOwnerIdtype:
    class Meta:
        name = "CopyrightOwnerIDType"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CopyrightYear:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CorporateBodyAsSubject:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CorporateName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CountryCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CountryExcluded:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CountryOfPublication:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CoverImageFormatCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CoverImageLink:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CoverImageLinkTypeCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class CurrencyCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Doi:
    class Meta:
        name = "DOI"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Date:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DateFormat:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DefaultClassOfTrade:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DefaultCurrencyCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DefaultLanguageOfText:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DefaultLinearUnit:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DefaultPriceTypeCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DefaultWeightUnit:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DeletionCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DeletionText:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Dimensions:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DiscountCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DiscountCodeType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DiscountCodeTypeName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DiscountPercent:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DistinctiveTitle:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DownloadCaption:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DownloadCopyrightNotice:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DownloadCredit:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class DownloadTerms:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Ean13:
    class Meta:
        name = "EAN13"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Ean13OfSet:
    class Meta:
        name = "EAN13OfSet"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EditionNumber:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EditionStatement:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EditionTypeCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EditionVersionNumber:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EmailAddress:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EndDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EpubFormat:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EpubFormatDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EpubFormatVersion:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EpubSource:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EpubSourceDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EpubSourceVersion:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EpubType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EpubTypeDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EpubTypeNote:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class EpubTypeVersion:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ExpectedDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ExpectedShipDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ExtentType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ExtentUnit:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ExtentValue:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class FaxNumber:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class FirstPageNumber:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class FormerTitle:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class FreeQuantity:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class FromCompany:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class FromEannumber:
    class Meta:
        name = "FromEANNumber"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class FromEmail:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class FromPerson:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class FromSan:
    class Meta:
        name = "FromSAN"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Height:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class IdtypeName:
    class Meta:
        name = "IDTypeName"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Idvalue:
    class Meta:
        name = "IDValue"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Isbn:
    class Meta:
        name = "ISBN"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class IsbnofSet:
    class Meta:
        name = "ISBNOfSet"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Ismn:
    class Meta:
        name = "ISMN"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class IllustrationType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class IllustrationTypeDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class IllustrationsNote:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ImageResolution:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ImprintName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class InitialPrintRun:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class InterestAge:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class IntermediaryAvailabilityCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ItemNumberWithinSet:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ItemQuantity:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class KeyNames:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class LanguageCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class LanguageOfText:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class LanguageRole:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class LastDateForReturns:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class LastPageNumber:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class LettersAfterNames:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class LevelSequenceNumber:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class LocationIdtype:
    class Meta:
        name = "LocationIDType"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class LocationName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MainDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MainSubjectSchemeIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MapScale:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MarketCountry:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MarketCountryExcluded:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MarketDateRole:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MarketPublishingStatus:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MarketRestrictionDetail:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MarketTerritory:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MeasureTypeCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MeasureUnitCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Measurement:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MediaFileDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MediaFileFormatCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MediaFileLink:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MediaFileLinkTypeCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MediaFileTypeCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MessageNote:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MessageNumber:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MessageRepeat:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class MinimumOrderQuantity:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class NameCodeType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class NameCodeTypeName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class NameCodeValue:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class NamesAfterKey:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class NamesBeforeKey:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class NoContributor:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class NoEdition:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class NoSeries:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class NotificationType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Number:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class NumberOfIllustrations:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class NumberOfPages:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class NumberOfPieces:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class NumberWithinSeries:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class OnHand:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class OnOrder:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class OnSaleDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class OrderTime:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class OriginalLanguage:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class OriginalPublisher:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class OutOfPrintDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PackQuantity:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PagesArabic:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PagesRoman:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Percent:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PersonDateRole:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PersonName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PersonNameIdtype:
    class Meta:
        name = "PersonNameIDType"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PersonNameInverted:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PersonNameType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PlaceAsSubject:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PrefixToKey:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PriceAmount:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PriceEffectiveFrom:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PriceEffectiveUntil:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PricePer:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PriceQualifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PriceStatus:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PriceTypeCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PriceTypeDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PrizeCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PrizeCountry:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PrizeJury:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PrizeName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PrizeYear:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PrizesDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductAvailability:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductClassificationCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductClassificationType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductContentType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductForm:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductFormDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductFormDetail:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductFormFeatureDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductFormFeatureType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductFormFeatureValue:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductIdtype:
    class Meta:
        name = "ProductIDType"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductPackaging:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductWebsiteDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProductWebsiteLink:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ProfessionalPosition:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PromotionCampaign:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PromotionContact:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PublicationDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PublisherName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PublisherProductNo:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PublisherSeriesCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PublishingRole:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PublishingStatus:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class PublishingStatusNote:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class RecordReference:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class RecordSourceIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class RecordSourceIdentifierType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class RecordSourceName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class RecordSourceType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class RegionCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReissueDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReissueDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class RelationCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReligiousTextFeatureCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReligiousTextFeatureDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReligiousTextFeatureType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReligiousTextId:
    class Meta:
        name = "ReligiousTextID"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReplacedByEan13:
    class Meta:
        name = "ReplacedByEAN13"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReplacedByIsbn:
    class Meta:
        name = "ReplacedByISBN"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReplacesEan13:
    class Meta:
        name = "ReplacesEAN13"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReplacesIsbn:
    class Meta:
        name = "ReplacesISBN"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReprintDetail:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReturnsCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReturnsCodeType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ReviewQuote:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class RightsCountry:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class RightsRegion:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class RightsTerritory:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SalesOutletIdtype:
    class Meta:
        name = "SalesOutletIDType"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SalesOutletName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SalesRestrictionDetail:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SalesRestrictionType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SalesRightsType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SenderIdtype:
    class Meta:
        name = "SenderIDType"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SentDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SequenceNumber:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SequenceNumberWithinRole:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SeriesIdtype:
    class Meta:
        name = "SeriesIDType"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SeriesIssn:
    class Meta:
        name = "SeriesISSN"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SeriesPartName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SetItemTitle:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SetPartNumber:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SetPartTitle:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SponsorName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class StartDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class StockQuantityCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class StockQuantityCodeType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class StockQuantityCodeTypeName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class StudyBibleType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SubjectCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SubjectHeadingText:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SubjectSchemeIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SubjectSchemeName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SubjectSchemeVersion:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SubordinateEntries:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Subtitle:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SuffixToKey:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SupplierEanlocationNumber:
    class Meta:
        name = "SupplierEANLocationNumber"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SupplierIdtype:
    class Meta:
        name = "SupplierIDType"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SupplierName:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SupplierRole:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SupplierSan:
    class Meta:
        name = "SupplierSAN"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SupplyRestrictionDetail:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SupplyToCountry:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SupplyToCountryExcluded:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SupplyToRegion:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class SupplyToTerritory:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TaxAmount1:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TaxAmount2:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TaxRateCode1:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TaxRateCode2:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TaxRatePercent1:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TaxRatePercent2:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TaxableAmount1:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TaxableAmount2:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TelephoneNumber:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Territory:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TerritoryExcluded:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Text:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TextAuthor:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TextCaseFlag:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TextFormat:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TextItemIdtype:
    class Meta:
        name = "TextItemIDType"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TextItemType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TextLink:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TextLinkType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TextPublicationDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TextSourceCorporate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TextSourceTitle:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TextTypeCode:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TextWithDownload:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ThesisPresentedTo:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ThesisType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ThesisYear:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Thickness:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TitleOfSeries:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TitleOfSet:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TitlePrefix:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TitleText:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TitleType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TitleWithoutPrefix:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TitlesAfterNames:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TitlesBeforeNames:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ToCompany:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ToEannumber:
    class Meta:
        name = "ToEANNumber"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ToPerson:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class ToSan:
    class Meta:
        name = "ToSAN"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TradeAnnouncementDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TradeCategory:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class TranslationOfTitle:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Upc:
    class Meta:
        name = "UPC"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class UsschoolGrade:
    class Meta:
        name = "USSchoolGrade"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class UnnamedPersons:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class UnpricedItemType:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class WebsiteDescription:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class WebsiteLink:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class WebsiteRole:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Weight:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class Width:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class WorkIdtype:
    class Meta:
        name = "WorkIDType"
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class YearFirstPublished:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class YearOfAnnual:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

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
class AddresseeIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    addressee_idtype: Optional[AddresseeIdtype] = field(
        default=None,
        metadata={
            "name": "AddresseeIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
class AgentIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    agent_idtype: Optional[AgentIdtype] = field(
        default=None,
        metadata={
            "name": "AgentIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    audience_code_type: Optional[AudienceCodeType] = field(
        default=None,
        metadata={
            "name": "AudienceCodeType",
            "type": "Element",
            "required": True,
        }
    )
    audience_code_type_name: Optional[AudienceCodeTypeName] = field(
        default=None,
        metadata={
            "name": "AudienceCodeTypeName",
            "type": "Element",
        }
    )
    audience_code_value: Optional[AudienceCodeValue] = field(
        default=None,
        metadata={
            "name": "AudienceCodeValue",
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
class AudienceRange:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    audience_range_qualifier: Optional[AudienceRangeQualifier] = field(
        default=None,
        metadata={
            "name": "AudienceRangeQualifier",
            "type": "Element",
            "required": True,
        }
    )
    audience_range_precision: List[AudienceRangePrecision] = field(
        default_factory=list,
        metadata={
            "name": "AudienceRangePrecision",
            "type": "Element",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    audience_range_value: List[AudienceRangeValue] = field(
        default_factory=list,
        metadata={
            "name": "AudienceRangeValue",
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
class BatchBonus:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    batch_quantity: Optional[BatchQuantity] = field(
        default=None,
        metadata={
            "name": "BatchQuantity",
            "type": "Element",
            "required": True,
        }
    )
    free_quantity: Optional[FreeQuantity] = field(
        default=None,
        metadata={
            "name": "FreeQuantity",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    bible_contents: List[BibleContents] = field(
        default_factory=list,
        metadata={
            "name": "BibleContents",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    bible_version: List[BibleVersion] = field(
        default_factory=list,
        metadata={
            "name": "BibleVersion",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    study_bible_type: Optional[StudyBibleType] = field(
        default=None,
        metadata={
            "name": "StudyBibleType",
            "type": "Element",
        }
    )
    bible_purpose: List[BiblePurpose] = field(
        default_factory=list,
        metadata={
            "name": "BiblePurpose",
            "type": "Element",
        }
    )
    bible_text_organization: Optional[BibleTextOrganization] = field(
        default=None,
        metadata={
            "name": "BibleTextOrganization",
            "type": "Element",
        }
    )
    bible_reference_location: Optional[BibleReferenceLocation] = field(
        default=None,
        metadata={
            "name": "BibleReferenceLocation",
            "type": "Element",
        }
    )
    bible_text_feature: List[BibleTextFeature] = field(
        default_factory=list,
        metadata={
            "name": "BibleTextFeature",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    complexity_scheme_identifier: Optional[ComplexitySchemeIdentifier] = field(
        default=None,
        metadata={
            "name": "ComplexitySchemeIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    complexity_code: Optional[ComplexityCode] = field(
        default=None,
        metadata={
            "name": "ComplexityCode",
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
class ConferenceSponsorIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    conference_sponsor_idtype: Optional[ConferenceSponsorIdtype] = field(
        default=None,
        metadata={
            "name": "ConferenceSponsorIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
class CopyrightOwnerIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    copyright_owner_idtype: Optional[CopyrightOwnerIdtype] = field(
        default=None,
        metadata={
            "name": "CopyrightOwnerIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
class DiscountCoded:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    discount_code_type: Optional[DiscountCodeType] = field(
        default=None,
        metadata={
            "name": "DiscountCodeType",
            "type": "Element",
            "required": True,
        }
    )
    discount_code_type_name: Optional[DiscountCodeTypeName] = field(
        default=None,
        metadata={
            "name": "DiscountCodeTypeName",
            "type": "Element",
        }
    )
    discount_code: Optional[DiscountCode] = field(
        default=None,
        metadata={
            "name": "DiscountCode",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    extent_type: Optional[ExtentType] = field(
        default=None,
        metadata={
            "name": "ExtentType",
            "type": "Element",
            "required": True,
        }
    )
    extent_value: Optional[ExtentValue] = field(
        default=None,
        metadata={
            "name": "ExtentValue",
            "type": "Element",
            "required": True,
        }
    )
    extent_unit: Optional[ExtentUnit] = field(
        default=None,
        metadata={
            "name": "ExtentUnit",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    illustration_type: Optional[IllustrationType] = field(
        default=None,
        metadata={
            "name": "IllustrationType",
            "type": "Element",
            "required": True,
        }
    )
    illustration_type_description: Optional[IllustrationTypeDescription] = field(
        default=None,
        metadata={
            "name": "IllustrationTypeDescription",
            "type": "Element",
        }
    )
    number: Optional[Number] = field(
        default=None,
        metadata={
            "name": "Number",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ImprintName",
                    "type": ImprintName,
                },
                {
                    "name": "NameCodeType",
                    "type": NameCodeType,
                },
                {
                    "name": "NameCodeTypeName",
                    "type": NameCodeTypeName,
                },
                {
                    "name": "NameCodeValue",
                    "type": NameCodeValue,
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    language_role: Optional[LanguageRole] = field(
        default=None,
        metadata={
            "name": "LanguageRole",
            "type": "Element",
            "required": True,
        }
    )
    language_code: Optional[LanguageCode] = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Element",
            "required": True,
        }
    )
    country_code: Optional[CountryCode] = field(
        default=None,
        metadata={
            "name": "CountryCode",
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
class LocationIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    location_idtype: Optional[LocationIdtype] = field(
        default=None,
        metadata={
            "name": "LocationIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
class MainSubject:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    main_subject_scheme_identifier: Optional[MainSubjectSchemeIdentifier] = field(
        default=None,
        metadata={
            "name": "MainSubjectSchemeIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    subject_scheme_version: Optional[SubjectSchemeVersion] = field(
        default=None,
        metadata={
            "name": "SubjectSchemeVersion",
            "type": "Element",
        }
    )
    subject_code_or_subject_heading_text: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SubjectCode",
                    "type": SubjectCode,
                },
                {
                    "name": "SubjectHeadingText",
                    "type": SubjectHeadingText,
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
class MarketDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    market_date_role: Optional[MarketDateRole] = field(
        default=None,
        metadata={
            "name": "MarketDateRole",
            "type": "Element",
            "required": True,
        }
    )
    date_format: Optional[DateFormat] = field(
        default=None,
        metadata={
            "name": "DateFormat",
            "type": "Element",
        }
    )
    date: Optional[Date] = field(
        default=None,
        metadata={
            "name": "Date",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    measure_type_code: Optional[MeasureTypeCode] = field(
        default=None,
        metadata={
            "name": "MeasureTypeCode",
            "type": "Element",
            "required": True,
        }
    )
    measurement: Optional[Measurement] = field(
        default=None,
        metadata={
            "name": "Measurement",
            "type": "Element",
            "required": True,
        }
    )
    measure_unit_code: Optional[MeasureUnitCode] = field(
        default=None,
        metadata={
            "name": "MeasureUnitCode",
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
class MediaFile:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    media_file_type_code: Optional[MediaFileTypeCode] = field(
        default=None,
        metadata={
            "name": "MediaFileTypeCode",
            "type": "Element",
            "required": True,
        }
    )
    media_file_format_code: Optional[MediaFileFormatCode] = field(
        default=None,
        metadata={
            "name": "MediaFileFormatCode",
            "type": "Element",
        }
    )
    image_resolution: Optional[ImageResolution] = field(
        default=None,
        metadata={
            "name": "ImageResolution",
            "type": "Element",
        }
    )
    media_file_link_type_code: Optional[MediaFileLinkTypeCode] = field(
        default=None,
        metadata={
            "name": "MediaFileLinkTypeCode",
            "type": "Element",
            "required": True,
        }
    )
    media_file_link: Optional[MediaFileLink] = field(
        default=None,
        metadata={
            "name": "MediaFileLink",
            "type": "Element",
            "required": True,
        }
    )
    text_with_download: Optional[TextWithDownload] = field(
        default=None,
        metadata={
            "name": "TextWithDownload",
            "type": "Element",
        }
    )
    download_caption: Optional[DownloadCaption] = field(
        default=None,
        metadata={
            "name": "DownloadCaption",
            "type": "Element",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DownloadCredit",
                    "type": DownloadCredit,
                },
                {
                    "name": "DownloadCopyrightNotice",
                    "type": DownloadCopyrightNotice,
                },
                {
                    "name": "DownloadTerms",
                    "type": DownloadTerms,
                },
                {
                    "name": "MediaFileDate",
                    "type": MediaFileDate,
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
class OnOrderDetail:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    on_order: Optional[OnOrder] = field(
        default=None,
        metadata={
            "name": "OnOrder",
            "type": "Element",
            "required": True,
        }
    )
    expected_date: Optional[ExpectedDate] = field(
        default=None,
        metadata={
            "name": "ExpectedDate",
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
class OtherText:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    text_type_code: Optional[TextTypeCode] = field(
        default=None,
        metadata={
            "name": "TextTypeCode",
            "type": "Element",
            "required": True,
        }
    )
    text_format: Optional[TextFormat] = field(
        default=None,
        metadata={
            "name": "TextFormat",
            "type": "Element",
        }
    )
    text: Optional[Text] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
        }
    )
    text_link_type: Optional[TextLinkType] = field(
        default=None,
        metadata={
            "name": "TextLinkType",
            "type": "Element",
        }
    )
    text_link: Optional[TextLink] = field(
        default=None,
        metadata={
            "name": "TextLink",
            "type": "Element",
        }
    )
    text_author: Optional[TextAuthor] = field(
        default=None,
        metadata={
            "name": "TextAuthor",
            "type": "Element",
        }
    )
    text_source_corporate: Optional[TextSourceCorporate] = field(
        default=None,
        metadata={
            "name": "TextSourceCorporate",
            "type": "Element",
        }
    )
    text_source_title: Optional[TextSourceTitle] = field(
        default=None,
        metadata={
            "name": "TextSourceTitle",
            "type": "Element",
        }
    )
    text_publication_date: Optional[TextPublicationDate] = field(
        default=None,
        metadata={
            "name": "TextPublicationDate",
            "type": "Element",
        }
    )
    start_date: Optional[StartDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
        }
    )
    end_date: Optional[EndDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
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
    textformat_attribute: List34 = field(
        default=List34.VALUE_00,
        metadata={
            "name": "textformat",
            "type": "Attribute",
        }
    )
    textcase: List14 = field(
        default=List14.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[List74] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transliteration: Optional[List138] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    datestamp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"2\d\d\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-8])(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13-9]|1[0-2])(29|30)(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2\d\d\d(0[13578]|1[02])31(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[048](0[048]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?|2[1235679](0[48]|[13579][26]|[2468][048])0229(([01][0-9]|2[0-3])[0-5][0-9][0-5][0-9])?",
        }
    )
    sourcetype: List3 = field(
        default=List3.VALUE_00,
        metadata={
            "type": "Attribute",
        }
    )
    sourcename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(slots=True)
class PageRun:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    first_page_number: Optional[FirstPageNumber] = field(
        default=None,
        metadata={
            "name": "FirstPageNumber",
            "type": "Element",
            "required": True,
        }
    )
    last_page_number: Optional[LastPageNumber] = field(
        default=None,
        metadata={
            "name": "LastPageNumber",
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
class ParentIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    series_idtype: Optional[SeriesIdtype] = field(
        default=None,
        metadata={
            "name": "SeriesIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
class PersonDate:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    person_date_role: Optional[PersonDateRole] = field(
        default=None,
        metadata={
            "name": "PersonDateRole",
            "type": "Element",
            "required": True,
        }
    )
    date_format: Optional[DateFormat] = field(
        default=None,
        metadata={
            "name": "DateFormat",
            "type": "Element",
        }
    )
    date: Optional[Date] = field(
        default=None,
        metadata={
            "name": "Date",
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
class PersonNameIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    person_name_idtype: Optional[PersonNameIdtype] = field(
        default=None,
        metadata={
            "name": "PersonNameIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    prize_name: Optional[PrizeName] = field(
        default=None,
        metadata={
            "name": "PrizeName",
            "type": "Element",
            "required": True,
        }
    )
    prize_year: Optional[PrizeYear] = field(
        default=None,
        metadata={
            "name": "PrizeYear",
            "type": "Element",
        }
    )
    prize_country: Optional[PrizeCountry] = field(
        default=None,
        metadata={
            "name": "PrizeCountry",
            "type": "Element",
        }
    )
    prize_code: Optional[PrizeCode] = field(
        default=None,
        metadata={
            "name": "PrizeCode",
            "type": "Element",
        }
    )
    prize_jury: Optional[PrizeJury] = field(
        default=None,
        metadata={
            "name": "PrizeJury",
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
class ProductClassification:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    product_classification_type: Optional[ProductClassificationType] = field(
        default=None,
        metadata={
            "name": "ProductClassificationType",
            "type": "Element",
            "required": True,
        }
    )
    product_classification_code: Optional[ProductClassificationCode] = field(
        default=None,
        metadata={
            "name": "ProductClassificationCode",
            "type": "Element",
            "required": True,
        }
    )
    percent: Optional[Percent] = field(
        default=None,
        metadata={
            "name": "Percent",
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
class ProductFormFeature:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    product_form_feature_type: Optional[ProductFormFeatureType] = field(
        default=None,
        metadata={
            "name": "ProductFormFeatureType",
            "type": "Element",
            "required": True,
        }
    )
    product_form_feature_value: Optional[ProductFormFeatureValue] = field(
        default=None,
        metadata={
            "name": "ProductFormFeatureValue",
            "type": "Element",
        }
    )
    product_form_feature_description: Optional[ProductFormFeatureDescription] = field(
        default=None,
        metadata={
            "name": "ProductFormFeatureDescription",
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
class ProductIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    product_idtype: Optional[ProductIdtype] = field(
        default=None,
        metadata={
            "name": "ProductIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
class ProductWebsite:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    website_role: Optional[WebsiteRole] = field(
        default=None,
        metadata={
            "name": "WebsiteRole",
            "type": "Element",
        }
    )
    product_website_description: Optional[ProductWebsiteDescription] = field(
        default=None,
        metadata={
            "name": "ProductWebsiteDescription",
            "type": "Element",
        }
    )
    product_website_link: Optional[ProductWebsiteLink] = field(
        default=None,
        metadata={
            "name": "ProductWebsiteLink",
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
class ProfessionalAffiliation:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    professional_position_or_affiliation: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ProfessionalPosition",
                    "type": ProfessionalPosition,
                },
                {
                    "name": "Affiliation",
                    "type": Affiliation,
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
class ReligiousTextFeature:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    religious_text_feature_type: Optional[ReligiousTextFeatureType] = field(
        default=None,
        metadata={
            "name": "ReligiousTextFeatureType",
            "type": "Element",
            "required": True,
        }
    )
    religious_text_feature_code: Optional[ReligiousTextFeatureCode] = field(
        default=None,
        metadata={
            "name": "ReligiousTextFeatureCode",
            "type": "Element",
            "required": True,
        }
    )
    religious_text_feature_description: Optional[ReligiousTextFeatureDescription] = field(
        default=None,
        metadata={
            "name": "ReligiousTextFeatureDescription",
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
class SalesOutletIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    sales_outlet_idtype: Optional[SalesOutletIdtype] = field(
        default=None,
        metadata={
            "name": "SalesOutletIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
class SalesRights:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    sales_rights_type: Optional[SalesRightsType] = field(
        default=None,
        metadata={
            "name": "SalesRightsType",
            "type": "Element",
            "required": True,
        }
    )
    rights_country_or_rights_territory_or_rights_region: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RightsCountry",
                    "type": RightsCountry,
                },
                {
                    "name": "RightsTerritory",
                    "type": RightsTerritory,
                },
                {
                    "name": "RightsRegion",
                    "type": RightsRegion,
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
class SenderIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    sender_idtype: Optional[SenderIdtype] = field(
        default=None,
        metadata={
            "name": "SenderIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
class SeriesIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    series_idtype: Optional[SeriesIdtype] = field(
        default=None,
        metadata={
            "name": "SeriesIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
class StockQuantityCoded:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    stock_quantity_code_type: Optional[StockQuantityCodeType] = field(
        default=None,
        metadata={
            "name": "StockQuantityCodeType",
            "type": "Element",
            "required": True,
        }
    )
    stock_quantity_code_type_name: Optional[StockQuantityCodeTypeName] = field(
        default=None,
        metadata={
            "name": "StockQuantityCodeTypeName",
            "type": "Element",
        }
    )
    stock_quantity_code: Optional[StockQuantityCode] = field(
        default=None,
        metadata={
            "name": "StockQuantityCode",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    subject_scheme_identifier: Optional[SubjectSchemeIdentifier] = field(
        default=None,
        metadata={
            "name": "SubjectSchemeIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    subject_scheme_name: Optional[SubjectSchemeName] = field(
        default=None,
        metadata={
            "name": "SubjectSchemeName",
            "type": "Element",
        }
    )
    subject_scheme_version: Optional[SubjectSchemeVersion] = field(
        default=None,
        metadata={
            "name": "SubjectSchemeVersion",
            "type": "Element",
        }
    )
    subject_code_or_subject_heading_text: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SubjectCode",
                    "type": SubjectCode,
                },
                {
                    "name": "SubjectHeadingText",
                    "type": SubjectHeadingText,
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
class SupplierIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    supplier_idtype: Optional[SupplierIdtype] = field(
        default=None,
        metadata={
            "name": "SupplierIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
class TextItemIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    text_item_idtype: Optional[TextItemIdtype] = field(
        default=None,
        metadata={
            "name": "TextItemIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    title_type: Optional[TitleType] = field(
        default=None,
        metadata={
            "name": "TitleType",
            "type": "Element",
            "required": True,
        }
    )
    abbreviated_length: Optional[AbbreviatedLength] = field(
        default=None,
        metadata={
            "name": "AbbreviatedLength",
            "type": "Element",
        }
    )
    text_case_flag: Optional[TextCaseFlag] = field(
        default=None,
        metadata={
            "name": "TextCaseFlag",
            "type": "Element",
        }
    )
    title_text: Optional[TitleText] = field(
        default=None,
        metadata={
            "name": "TitleText",
            "type": "Element",
        }
    )
    title_prefix_or_title_without_prefix_or_subtitle: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TitlePrefix",
                    "type": TitlePrefix,
                },
                {
                    "name": "TitleWithoutPrefix",
                    "type": TitleWithoutPrefix,
                },
                {
                    "name": "Subtitle",
                    "type": Subtitle,
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    website_role: Optional[WebsiteRole] = field(
        default=None,
        metadata={
            "name": "WebsiteRole",
            "type": "Element",
        }
    )
    website_description: Optional[WebsiteDescription] = field(
        default=None,
        metadata={
            "name": "WebsiteDescription",
            "type": "Element",
        }
    )
    website_link: Optional[WebsiteLink] = field(
        default=None,
        metadata={
            "name": "WebsiteLink",
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
class WorkIdentifier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    work_idtype: Optional[WorkIdtype] = field(
        default=None,
        metadata={
            "name": "WorkIDType",
            "type": "Element",
            "required": True,
        }
    )
    idtype_name: Optional[IdtypeName] = field(
        default=None,
        metadata={
            "name": "IDTypeName",
            "type": "Element",
        }
    )
    idvalue: Optional[Idvalue] = field(
        default=None,
        metadata={
            "name": "IDValue",
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
class ConferenceSponsor:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    conference_sponsor_identifier: Optional[ConferenceSponsorIdentifier] = field(
        default=None,
        metadata={
            "name": "ConferenceSponsorIdentifier",
            "type": "Element",
        }
    )
    person_name_or_corporate_name: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonName",
                    "type": PersonName,
                },
                {
                    "name": "CorporateName",
                    "type": CorporateName,
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
class ContainedItem:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ISBN",
                    "type": Isbn,
                },
                {
                    "name": "EAN13",
                    "type": Ean13,
                },
                {
                    "name": "ProductIdentifier",
                    "type": ProductIdentifier,
                },
                {
                    "name": "ProductForm",
                    "type": ProductForm,
                },
                {
                    "name": "ProductFormDetail",
                    "type": ProductFormDetail,
                },
                {
                    "name": "ProductFormFeature",
                    "type": ProductFormFeature,
                },
                {
                    "name": "BookFormDetail",
                    "type": BookFormDetail,
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
                    "name": "ProductPackaging",
                    "type": ProductPackaging,
                },
                {
                    "name": "ProductFormDescription",
                    "type": ProductFormDescription,
                },
                {
                    "name": "NumberOfPieces",
                    "type": NumberOfPieces,
                },
                {
                    "name": "TradeCategory",
                    "type": TradeCategory,
                },
            ),
            "max_occurs": 10,
        }
    )
    product_content_type: List[ProductContentType] = field(
        default_factory=list,
        metadata={
            "name": "ProductContentType",
            "type": "Element",
        }
    )
    item_quantity: Optional[ItemQuantity] = field(
        default=None,
        metadata={
            "name": "ItemQuantity",
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
class CopyrightOwner:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    copyright_owner_identifier: Optional[CopyrightOwnerIdentifier] = field(
        default=None,
        metadata={
            "name": "CopyrightOwnerIdentifier",
            "type": "Element",
        }
    )
    person_name_or_corporate_name: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonName",
                    "type": PersonName,
                },
                {
                    "name": "CorporateName",
                    "type": CorporateName,
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    from_eannumber_or_from_san_or_sender_identifier: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FromEANNumber",
                    "type": FromEannumber,
                },
                {
                    "name": "FromSAN",
                    "type": FromSan,
                },
                {
                    "name": "SenderIdentifier",
                    "type": SenderIdentifier,
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
                    "name": "FromCompany",
                    "type": FromCompany,
                },
                {
                    "name": "FromPerson",
                    "type": FromPerson,
                },
                {
                    "name": "FromEmail",
                    "type": FromEmail,
                },
                {
                    "name": "ToEANNumber",
                    "type": ToEannumber,
                },
                {
                    "name": "ToSAN",
                    "type": ToSan,
                },
            ),
            "max_occurs": 8,
        }
    )
    addressee_identifier: List[AddresseeIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "AddresseeIdentifier",
            "type": "Element",
        }
    )
    to_company: Optional[ToCompany] = field(
        default=None,
        metadata={
            "name": "ToCompany",
            "type": "Element",
        }
    )
    to_person: Optional[ToPerson] = field(
        default=None,
        metadata={
            "name": "ToPerson",
            "type": "Element",
        }
    )
    message_number: Optional[MessageNumber] = field(
        default=None,
        metadata={
            "name": "MessageNumber",
            "type": "Element",
        }
    )
    message_repeat: Optional[MessageRepeat] = field(
        default=None,
        metadata={
            "name": "MessageRepeat",
            "type": "Element",
        }
    )
    sent_date: Optional[SentDate] = field(
        default=None,
        metadata={
            "name": "SentDate",
            "type": "Element",
            "required": True,
        }
    )
    message_note: Optional[MessageNote] = field(
        default=None,
        metadata={
            "name": "MessageNote",
            "type": "Element",
        }
    )
    default_language_of_text: Optional[DefaultLanguageOfText] = field(
        default=None,
        metadata={
            "name": "DefaultLanguageOfText",
            "type": "Element",
        }
    )
    default_price_type_code: Optional[DefaultPriceTypeCode] = field(
        default=None,
        metadata={
            "name": "DefaultPriceTypeCode",
            "type": "Element",
        }
    )
    default_currency_code: Optional[DefaultCurrencyCode] = field(
        default=None,
        metadata={
            "name": "DefaultCurrencyCode",
            "type": "Element",
        }
    )
    default_linear_unit: Optional[DefaultLinearUnit] = field(
        default=None,
        metadata={
            "name": "DefaultLinearUnit",
            "type": "Element",
        }
    )
    default_weight_unit: Optional[DefaultWeightUnit] = field(
        default=None,
        metadata={
            "name": "DefaultWeightUnit",
            "type": "Element",
        }
    )
    default_class_of_trade: Optional[DefaultClassOfTrade] = field(
        default=None,
        metadata={
            "name": "DefaultClassOfTrade",
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
class MarketRepresentation:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    agent_identifier_or_agent_name: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AgentIdentifier",
                    "type": AgentIdentifier,
                },
                {
                    "name": "AgentName",
                    "type": AgentName,
                },
            ),
        }
    )
    telephone_number: List[TelephoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "TelephoneNumber",
            "type": "Element",
        }
    )
    fax_number: List[FaxNumber] = field(
        default_factory=list,
        metadata={
            "name": "FaxNumber",
            "type": "Element",
        }
    )
    email_address: List[EmailAddress] = field(
        default_factory=list,
        metadata={
            "name": "EmailAddress",
            "type": "Element",
        }
    )
    website: List[Website] = field(
        default_factory=list,
        metadata={
            "name": "Website",
            "type": "Element",
        }
    )
    agent_role: Optional[AgentRole] = field(
        default=None,
        metadata={
            "name": "AgentRole",
            "type": "Element",
        }
    )
    market_country: Optional[MarketCountry] = field(
        default=None,
        metadata={
            "name": "MarketCountry",
            "type": "Element",
        }
    )
    market_territory: Optional[MarketTerritory] = field(
        default=None,
        metadata={
            "name": "MarketTerritory",
            "type": "Element",
        }
    )
    market_country_excluded: Optional[MarketCountryExcluded] = field(
        default=None,
        metadata={
            "name": "MarketCountryExcluded",
            "type": "Element",
        }
    )
    market_restriction_detail: Optional[MarketRestrictionDetail] = field(
        default=None,
        metadata={
            "name": "MarketRestrictionDetail",
            "type": "Element",
        }
    )
    market_publishing_status: Optional[MarketPublishingStatus] = field(
        default=None,
        metadata={
            "name": "MarketPublishingStatus",
            "type": "Element",
        }
    )
    market_date: List[MarketDate] = field(
        default_factory=list,
        metadata={
            "name": "MarketDate",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    person_name_type: Optional[PersonNameType] = field(
        default=None,
        metadata={
            "name": "PersonNameType",
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
                    "name": "PersonName",
                    "type": PersonName,
                },
                {
                    "name": "PersonNameInverted",
                    "type": PersonNameInverted,
                },
                {
                    "name": "TitlesBeforeNames",
                    "type": TitlesBeforeNames,
                },
                {
                    "name": "NamesBeforeKey",
                    "type": NamesBeforeKey,
                },
                {
                    "name": "PrefixToKey",
                    "type": PrefixToKey,
                },
                {
                    "name": "KeyNames",
                    "type": KeyNames,
                },
                {
                    "name": "NamesAfterKey",
                    "type": NamesAfterKey,
                },
                {
                    "name": "SuffixToKey",
                    "type": SuffixToKey,
                },
                {
                    "name": "LettersAfterNames",
                    "type": LettersAfterNames,
                },
                {
                    "name": "TitlesAfterNames",
                    "type": TitlesAfterNames,
                },
                {
                    "name": "PersonNameIdentifier",
                    "type": PersonNameIdentifier,
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
class NewSupplier:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    supplier_identifier: List[SupplierIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "SupplierIdentifier",
            "type": "Element",
        }
    )
    supplier_san_or_supplier_eanlocation_number_or_supplier_name: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplierSAN",
                    "type": SupplierSan,
                },
                {
                    "name": "SupplierEANLocationNumber",
                    "type": SupplierEanlocationNumber,
                },
                {
                    "name": "SupplierName",
                    "type": SupplierName,
                },
            ),
            "max_occurs": 5,
        }
    )
    telephone_number: List[TelephoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "TelephoneNumber",
            "type": "Element",
        }
    )
    fax_number: List[FaxNumber] = field(
        default_factory=list,
        metadata={
            "name": "FaxNumber",
            "type": "Element",
        }
    )
    email_address: List[EmailAddress] = field(
        default_factory=list,
        metadata={
            "name": "EmailAddress",
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
class NotForSale:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    rights_country: List[RightsCountry] = field(
        default_factory=list,
        metadata={
            "name": "RightsCountry",
            "type": "Element",
        }
    )
    rights_territory_or_isbn_or_ean13: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RightsTerritory",
                    "type": RightsTerritory,
                },
                {
                    "name": "ISBN",
                    "type": Isbn,
                },
                {
                    "name": "EAN13",
                    "type": Ean13,
                },
            ),
            "max_occurs": 4,
        }
    )
    product_identifier: List[ProductIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "ProductIdentifier",
            "type": "Element",
        }
    )
    publisher_name: Optional[PublisherName] = field(
        default=None,
        metadata={
            "name": "PublisherName",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    price_type_code: Optional[PriceTypeCode] = field(
        default=None,
        metadata={
            "name": "PriceTypeCode",
            "type": "Element",
        }
    )
    price_qualifier: Optional[PriceQualifier] = field(
        default=None,
        metadata={
            "name": "PriceQualifier",
            "type": "Element",
        }
    )
    price_type_description: Optional[PriceTypeDescription] = field(
        default=None,
        metadata={
            "name": "PriceTypeDescription",
            "type": "Element",
        }
    )
    price_per: Optional[PricePer] = field(
        default=None,
        metadata={
            "name": "PricePer",
            "type": "Element",
        }
    )
    minimum_order_quantity: Optional[MinimumOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumOrderQuantity",
            "type": "Element",
        }
    )
    batch_bonus: List[BatchBonus] = field(
        default_factory=list,
        metadata={
            "name": "BatchBonus",
            "type": "Element",
        }
    )
    class_of_trade: Optional[ClassOfTrade] = field(
        default=None,
        metadata={
            "name": "ClassOfTrade",
            "type": "Element",
        }
    )
    bicdiscount_group_code: Optional[BicdiscountGroupCode] = field(
        default=None,
        metadata={
            "name": "BICDiscountGroupCode",
            "type": "Element",
        }
    )
    discount_coded: List[DiscountCoded] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCoded",
            "type": "Element",
        }
    )
    discount_percent: Optional[DiscountPercent] = field(
        default=None,
        metadata={
            "name": "DiscountPercent",
            "type": "Element",
        }
    )
    price_status: Optional[PriceStatus] = field(
        default=None,
        metadata={
            "name": "PriceStatus",
            "type": "Element",
        }
    )
    price_amount: Optional[PriceAmount] = field(
        default=None,
        metadata={
            "name": "PriceAmount",
            "type": "Element",
            "required": True,
        }
    )
    currency_code: Optional[CurrencyCode] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Element",
        }
    )
    country_code: List[CountryCode] = field(
        default_factory=list,
        metadata={
            "name": "CountryCode",
            "type": "Element",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Territory",
                    "type": Territory,
                },
                {
                    "name": "CountryExcluded",
                    "type": CountryExcluded,
                },
                {
                    "name": "TerritoryExcluded",
                    "type": TerritoryExcluded,
                },
                {
                    "name": "TaxRateCode1",
                    "type": TaxRateCode1,
                },
                {
                    "name": "TaxRatePercent1",
                    "type": TaxRatePercent1,
                },
                {
                    "name": "TaxableAmount1",
                    "type": TaxableAmount1,
                },
                {
                    "name": "TaxAmount1",
                    "type": TaxAmount1,
                },
                {
                    "name": "TaxRateCode2",
                    "type": TaxRateCode2,
                },
                {
                    "name": "TaxRatePercent2",
                    "type": TaxRatePercent2,
                },
                {
                    "name": "TaxableAmount2",
                    "type": TaxableAmount2,
                },
                {
                    "name": "TaxAmount2",
                    "type": TaxAmount2,
                },
                {
                    "name": "PriceEffectiveFrom",
                    "type": PriceEffectiveFrom,
                },
                {
                    "name": "PriceEffectiveUntil",
                    "type": PriceEffectiveUntil,
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    publishing_role: Optional[PublishingRole] = field(
        default=None,
        metadata={
            "name": "PublishingRole",
            "type": "Element",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PublisherName",
                    "type": PublisherName,
                },
                {
                    "name": "NameCodeType",
                    "type": NameCodeType,
                },
                {
                    "name": "NameCodeTypeName",
                    "type": NameCodeTypeName,
                },
                {
                    "name": "NameCodeValue",
                    "type": NameCodeValue,
                },
            ),
            "max_occurs": 5,
        }
    )
    website: List[Website] = field(
        default_factory=list,
        metadata={
            "name": "Website",
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
class ReligiousText:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    bible_or_religious_text_id_or_religious_text_feature: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Bible",
                    "type": Bible,
                },
                {
                    "name": "ReligiousTextID",
                    "type": ReligiousTextId,
                },
                {
                    "name": "ReligiousTextFeature",
                    "type": ReligiousTextFeature,
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
class SalesOutlet:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    sales_outlet_identifier_or_sales_outlet_name: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesOutletIdentifier",
                    "type": SalesOutletIdentifier,
                },
                {
                    "name": "SalesOutletName",
                    "type": SalesOutletName,
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    isbnof_set: Optional[IsbnofSet] = field(
        default=None,
        metadata={
            "name": "ISBNOfSet",
            "type": "Element",
        }
    )
    ean13_of_set: Optional[Ean13OfSet] = field(
        default=None,
        metadata={
            "name": "EAN13OfSet",
            "type": "Element",
        }
    )
    product_identifier: List[ProductIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "ProductIdentifier",
            "type": "Element",
        }
    )
    title_of_set_or_title: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TitleOfSet",
                    "type": TitleOfSet,
                },
                {
                    "name": "Title",
                    "type": Title,
                },
            ),
        }
    )
    set_part_number: Optional[SetPartNumber] = field(
        default=None,
        metadata={
            "name": "SetPartNumber",
            "type": "Element",
        }
    )
    set_part_title: Optional[SetPartTitle] = field(
        default=None,
        metadata={
            "name": "SetPartTitle",
            "type": "Element",
        }
    )
    item_number_within_set: Optional[ItemNumberWithinSet] = field(
        default=None,
        metadata={
            "name": "ItemNumberWithinSet",
            "type": "Element",
        }
    )
    level_sequence_number: Optional[LevelSequenceNumber] = field(
        default=None,
        metadata={
            "name": "LevelSequenceNumber",
            "type": "Element",
        }
    )
    set_item_title: Optional[SetItemTitle] = field(
        default=None,
        metadata={
            "name": "SetItemTitle",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    location_identifier: Optional[LocationIdentifier] = field(
        default=None,
        metadata={
            "name": "LocationIdentifier",
            "type": "Element",
        }
    )
    location_name: Optional[LocationName] = field(
        default=None,
        metadata={
            "name": "LocationName",
            "type": "Element",
        }
    )
    stock_quantity_coded: Optional[StockQuantityCoded] = field(
        default=None,
        metadata={
            "name": "StockQuantityCoded",
            "type": "Element",
        }
    )
    on_hand_or_on_order_or_cbo: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OnHand",
                    "type": OnHand,
                },
                {
                    "name": "OnOrder",
                    "type": OnOrder,
                },
                {
                    "name": "CBO",
                    "type": Cbo,
                },
            ),
            "max_occurs": 4,
        }
    )
    on_order_detail: List[OnOrderDetail] = field(
        default_factory=list,
        metadata={
            "name": "OnOrderDetail",
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
class TextItem:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    text_item_type: Optional[TextItemType] = field(
        default=None,
        metadata={
            "name": "TextItemType",
            "type": "Element",
            "required": True,
        }
    )
    text_item_identifier: List[TextItemIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "TextItemIdentifier",
            "type": "Element",
        }
    )
    first_page_number_or_last_page_number_or_page_run: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FirstPageNumber",
                    "type": FirstPageNumber,
                },
                {
                    "name": "LastPageNumber",
                    "type": LastPageNumber,
                },
                {
                    "name": "PageRun",
                    "type": PageRun,
                },
            ),
        }
    )
    number_of_pages: Optional[NumberOfPages] = field(
        default=None,
        metadata={
            "name": "NumberOfPages",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    conference_role: Optional[ConferenceRole] = field(
        default=None,
        metadata={
            "name": "ConferenceRole",
            "type": "Element",
        }
    )
    conference_name: Optional[ConferenceName] = field(
        default=None,
        metadata={
            "name": "ConferenceName",
            "type": "Element",
            "required": True,
        }
    )
    conference_acronym: Optional[ConferenceAcronym] = field(
        default=None,
        metadata={
            "name": "ConferenceAcronym",
            "type": "Element",
        }
    )
    conference_number: Optional[ConferenceNumber] = field(
        default=None,
        metadata={
            "name": "ConferenceNumber",
            "type": "Element",
        }
    )
    conference_theme: Optional[ConferenceTheme] = field(
        default=None,
        metadata={
            "name": "ConferenceTheme",
            "type": "Element",
        }
    )
    conference_date: Optional[ConferenceDate] = field(
        default=None,
        metadata={
            "name": "ConferenceDate",
            "type": "Element",
        }
    )
    conference_place: Optional[ConferencePlace] = field(
        default=None,
        metadata={
            "name": "ConferencePlace",
            "type": "Element",
        }
    )
    conference_sponsor: List[ConferenceSponsor] = field(
        default_factory=list,
        metadata={
            "name": "ConferenceSponsor",
            "type": "Element",
        }
    )
    website: List[Website] = field(
        default_factory=list,
        metadata={
            "name": "Website",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    sequence_number: Optional[SequenceNumber] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ContributorRole",
                    "type": ContributorRole,
                },
                {
                    "name": "LanguageCode",
                    "type": LanguageCode,
                },
                {
                    "name": "SequenceNumberWithinRole",
                    "type": SequenceNumberWithinRole,
                },
                {
                    "name": "PersonName",
                    "type": PersonName,
                },
                {
                    "name": "PersonNameInverted",
                    "type": PersonNameInverted,
                },
                {
                    "name": "TitlesBeforeNames",
                    "type": TitlesBeforeNames,
                },
                {
                    "name": "NamesBeforeKey",
                    "type": NamesBeforeKey,
                },
                {
                    "name": "PrefixToKey",
                    "type": PrefixToKey,
                },
                {
                    "name": "KeyNames",
                    "type": KeyNames,
                },
                {
                    "name": "NamesAfterKey",
                    "type": NamesAfterKey,
                },
                {
                    "name": "SuffixToKey",
                    "type": SuffixToKey,
                },
                {
                    "name": "LettersAfterNames",
                    "type": LettersAfterNames,
                },
                {
                    "name": "TitlesAfterNames",
                    "type": TitlesAfterNames,
                },
            ),
        }
    )
    name_or_person_name_identifier: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Name",
                    "type": Name,
                },
                {
                    "name": "PersonNameIdentifier",
                    "type": PersonNameIdentifier,
                },
            ),
        }
    )
    person_date_or_professional_affiliation_or_corporate_name: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonDate",
                    "type": PersonDate,
                },
                {
                    "name": "ProfessionalAffiliation",
                    "type": ProfessionalAffiliation,
                },
                {
                    "name": "CorporateName",
                    "type": CorporateName,
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
                    "name": "BiographicalNote",
                    "type": BiographicalNote,
                },
                {
                    "name": "Website",
                    "type": Website,
                },
                {
                    "name": "ProfessionalPosition",
                    "type": ProfessionalPosition,
                },
                {
                    "name": "Affiliation",
                    "type": Affiliation,
                },
                {
                    "name": "ContributorDescription",
                    "type": ContributorDescription,
                },
                {
                    "name": "UnnamedPersons",
                    "type": UnnamedPersons,
                },
            ),
        }
    )
    country_code: List[CountryCode] = field(
        default_factory=list,
        metadata={
            "name": "CountryCode",
            "type": "Element",
        }
    )
    region_code: List[RegionCode] = field(
        default_factory=list,
        metadata={
            "name": "RegionCode",
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
class CopyrightStatement:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    copyright_year: List[CopyrightYear] = field(
        default_factory=list,
        metadata={
            "name": "CopyrightYear",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    copyright_owner: List[CopyrightOwner] = field(
        default_factory=list,
        metadata={
            "name": "CopyrightOwner",
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
class PersonAsSubject:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonName",
                    "type": PersonName,
                },
                {
                    "name": "PersonNameInverted",
                    "type": PersonNameInverted,
                },
                {
                    "name": "TitlesBeforeNames",
                    "type": TitlesBeforeNames,
                },
                {
                    "name": "NamesBeforeKey",
                    "type": NamesBeforeKey,
                },
                {
                    "name": "PrefixToKey",
                    "type": PrefixToKey,
                },
                {
                    "name": "KeyNames",
                    "type": KeyNames,
                },
                {
                    "name": "NamesAfterKey",
                    "type": NamesAfterKey,
                },
                {
                    "name": "SuffixToKey",
                    "type": SuffixToKey,
                },
                {
                    "name": "LettersAfterNames",
                    "type": LettersAfterNames,
                },
                {
                    "name": "TitlesAfterNames",
                    "type": TitlesAfterNames,
                },
                {
                    "name": "Name",
                    "type": Name,
                },
                {
                    "name": "PersonNameIdentifier",
                    "type": PersonNameIdentifier,
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    reissue_date: Optional[ReissueDate] = field(
        default=None,
        metadata={
            "name": "ReissueDate",
            "type": "Element",
            "required": True,
        }
    )
    reissue_description: Optional[ReissueDescription] = field(
        default=None,
        metadata={
            "name": "ReissueDescription",
            "type": "Element",
        }
    )
    price: List[Price] = field(
        default_factory=list,
        metadata={
            "name": "Price",
            "type": "Element",
        }
    )
    media_file: List[MediaFile] = field(
        default_factory=list,
        metadata={
            "name": "MediaFile",
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
class RelatedProduct:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    relation_code: Optional[RelationCode] = field(
        default=None,
        metadata={
            "name": "RelationCode",
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
                    "name": "ISBN",
                    "type": Isbn,
                },
                {
                    "name": "EAN13",
                    "type": Ean13,
                },
                {
                    "name": "ProductIdentifier",
                    "type": ProductIdentifier,
                },
                {
                    "name": "Website",
                    "type": Website,
                },
                {
                    "name": "ProductForm",
                    "type": ProductForm,
                },
                {
                    "name": "ProductFormDetail",
                    "type": ProductFormDetail,
                },
                {
                    "name": "ProductFormFeature",
                    "type": ProductFormFeature,
                },
                {
                    "name": "BookFormDetail",
                    "type": BookFormDetail,
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
                    "name": "ProductPackaging",
                    "type": ProductPackaging,
                },
                {
                    "name": "ProductFormDescription",
                    "type": ProductFormDescription,
                },
                {
                    "name": "NumberOfPieces",
                    "type": NumberOfPieces,
                },
                {
                    "name": "TradeCategory",
                    "type": TradeCategory,
                },
            ),
            "max_occurs": 10,
        }
    )
    product_content_type: List[ProductContentType] = field(
        default_factory=list,
        metadata={
            "name": "ProductContentType",
            "type": "Element",
        }
    )
    epub_type: Optional[EpubType] = field(
        default=None,
        metadata={
            "name": "EpubType",
            "type": "Element",
        }
    )
    epub_type_version: Optional[EpubTypeVersion] = field(
        default=None,
        metadata={
            "name": "EpubTypeVersion",
            "type": "Element",
        }
    )
    epub_type_description: Optional[EpubTypeDescription] = field(
        default=None,
        metadata={
            "name": "EpubTypeDescription",
            "type": "Element",
        }
    )
    epub_format: Optional[EpubFormat] = field(
        default=None,
        metadata={
            "name": "EpubFormat",
            "type": "Element",
        }
    )
    epub_format_version: Optional[EpubFormatVersion] = field(
        default=None,
        metadata={
            "name": "EpubFormatVersion",
            "type": "Element",
        }
    )
    epub_format_description: Optional[EpubFormatDescription] = field(
        default=None,
        metadata={
            "name": "EpubFormatDescription",
            "type": "Element",
        }
    )
    epub_type_note: Optional[EpubTypeNote] = field(
        default=None,
        metadata={
            "name": "EpubTypeNote",
            "type": "Element",
        }
    )
    publisher: List[Publisher] = field(
        default_factory=list,
        metadata={
            "name": "Publisher",
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
class SalesRestriction:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    sales_restriction_type: Optional[SalesRestrictionType] = field(
        default=None,
        metadata={
            "name": "SalesRestrictionType",
            "type": "Element",
            "required": True,
        }
    )
    sales_outlet: List[SalesOutlet] = field(
        default_factory=list,
        metadata={
            "name": "SalesOutlet",
            "type": "Element",
        }
    )
    sales_restriction_detail: Optional[SalesRestrictionDetail] = field(
        default=None,
        metadata={
            "name": "SalesRestrictionDetail",
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
class ContentItem:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    level_sequence_number: Optional[LevelSequenceNumber] = field(
        default=None,
        metadata={
            "name": "LevelSequenceNumber",
            "type": "Element",
        }
    )
    text_item: Optional[TextItem] = field(
        default=None,
        metadata={
            "name": "TextItem",
            "type": "Element",
            "required": True,
        }
    )
    website: List[Website] = field(
        default_factory=list,
        metadata={
            "name": "Website",
            "type": "Element",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ComponentTypeName",
                    "type": ComponentTypeName,
                },
                {
                    "name": "ComponentNumber",
                    "type": ComponentNumber,
                },
                {
                    "name": "DistinctiveTitle",
                    "type": DistinctiveTitle,
                },
                {
                    "name": "Title",
                    "type": Title,
                },
            ),
        }
    )
    work_identifier: List[WorkIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "WorkIdentifier",
            "type": "Element",
        }
    )
    contributor: List[Contributor] = field(
        default_factory=list,
        metadata={
            "name": "Contributor",
            "type": "Element",
        }
    )
    contributor_statement: Optional[ContributorStatement] = field(
        default=None,
        metadata={
            "name": "ContributorStatement",
            "type": "Element",
        }
    )
    subject: List[Subject] = field(
        default_factory=list,
        metadata={
            "name": "Subject",
            "type": "Element",
        }
    )
    person_as_subject: List[PersonAsSubject] = field(
        default_factory=list,
        metadata={
            "name": "PersonAsSubject",
            "type": "Element",
        }
    )
    corporate_body_as_subject: List[CorporateBodyAsSubject] = field(
        default_factory=list,
        metadata={
            "name": "CorporateBodyAsSubject",
            "type": "Element",
        }
    )
    place_as_subject: List[PlaceAsSubject] = field(
        default_factory=list,
        metadata={
            "name": "PlaceAsSubject",
            "type": "Element",
        }
    )
    other_text: List[OtherText] = field(
        default_factory=list,
        metadata={
            "name": "OtherText",
            "type": "Element",
        }
    )
    media_file: List[MediaFile] = field(
        default_factory=list,
        metadata={
            "name": "MediaFile",
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
class MainSeriesRecord:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    record_reference: Optional[RecordReference] = field(
        default=None,
        metadata={
            "name": "RecordReference",
            "type": "Element",
            "required": True,
        }
    )
    notification_type: Optional[NotificationType] = field(
        default=None,
        metadata={
            "name": "NotificationType",
            "type": "Element",
            "required": True,
        }
    )
    deletion_code: Optional[DeletionCode] = field(
        default=None,
        metadata={
            "name": "DeletionCode",
            "type": "Element",
        }
    )
    deletion_text: Optional[DeletionText] = field(
        default=None,
        metadata={
            "name": "DeletionText",
            "type": "Element",
        }
    )
    record_source_type: Optional[RecordSourceType] = field(
        default=None,
        metadata={
            "name": "RecordSourceType",
            "type": "Element",
        }
    )
    record_source_identifier_type: Optional[RecordSourceIdentifierType] = field(
        default=None,
        metadata={
            "name": "RecordSourceIdentifierType",
            "type": "Element",
        }
    )
    record_source_identifier: Optional[RecordSourceIdentifier] = field(
        default=None,
        metadata={
            "name": "RecordSourceIdentifier",
            "type": "Element",
        }
    )
    record_source_name: Optional[RecordSourceName] = field(
        default=None,
        metadata={
            "name": "RecordSourceName",
            "type": "Element",
        }
    )
    series_identifier: List[SeriesIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "SeriesIdentifier",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    contributor: List[Contributor] = field(
        default_factory=list,
        metadata={
            "name": "Contributor",
            "type": "Element",
        }
    )
    other_text: List[OtherText] = field(
        default_factory=list,
        metadata={
            "name": "OtherText",
            "type": "Element",
        }
    )
    publisher: List[Publisher] = field(
        default_factory=list,
        metadata={
            "name": "Publisher",
            "type": "Element",
        }
    )
    subordinate_entries: Optional[SubordinateEntries] = field(
        default=None,
        metadata={
            "name": "SubordinateEntries",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    series_issn: Optional[SeriesIssn] = field(
        default=None,
        metadata={
            "name": "SeriesISSN",
            "type": "Element",
        }
    )
    publisher_series_code: Optional[PublisherSeriesCode] = field(
        default=None,
        metadata={
            "name": "PublisherSeriesCode",
            "type": "Element",
        }
    )
    series_identifier: List[SeriesIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "SeriesIdentifier",
            "type": "Element",
        }
    )
    title_of_series_or_title: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TitleOfSeries",
                    "type": TitleOfSeries,
                },
                {
                    "name": "Title",
                    "type": Title,
                },
            ),
        }
    )
    contributor: List[Contributor] = field(
        default_factory=list,
        metadata={
            "name": "Contributor",
            "type": "Element",
        }
    )
    number_within_series: Optional[NumberWithinSeries] = field(
        default=None,
        metadata={
            "name": "NumberWithinSeries",
            "type": "Element",
        }
    )
    year_of_annual: Optional[YearOfAnnual] = field(
        default=None,
        metadata={
            "name": "YearOfAnnual",
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
class SubSeriesRecord:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    record_reference: Optional[RecordReference] = field(
        default=None,
        metadata={
            "name": "RecordReference",
            "type": "Element",
            "required": True,
        }
    )
    notification_type: Optional[NotificationType] = field(
        default=None,
        metadata={
            "name": "NotificationType",
            "type": "Element",
            "required": True,
        }
    )
    deletion_code: Optional[DeletionCode] = field(
        default=None,
        metadata={
            "name": "DeletionCode",
            "type": "Element",
        }
    )
    deletion_text: Optional[DeletionText] = field(
        default=None,
        metadata={
            "name": "DeletionText",
            "type": "Element",
        }
    )
    record_source_type: Optional[RecordSourceType] = field(
        default=None,
        metadata={
            "name": "RecordSourceType",
            "type": "Element",
        }
    )
    record_source_identifier_type: Optional[RecordSourceIdentifierType] = field(
        default=None,
        metadata={
            "name": "RecordSourceIdentifierType",
            "type": "Element",
        }
    )
    record_source_identifier: Optional[RecordSourceIdentifier] = field(
        default=None,
        metadata={
            "name": "RecordSourceIdentifier",
            "type": "Element",
        }
    )
    record_source_name: Optional[RecordSourceName] = field(
        default=None,
        metadata={
            "name": "RecordSourceName",
            "type": "Element",
        }
    )
    series_identifier: List[SeriesIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "SeriesIdentifier",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    parent_identifier: Optional[ParentIdentifier] = field(
        default=None,
        metadata={
            "name": "ParentIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    level_sequence_number: Optional[LevelSequenceNumber] = field(
        default=None,
        metadata={
            "name": "LevelSequenceNumber",
            "type": "Element",
            "required": True,
        }
    )
    series_part_name: Optional[SeriesPartName] = field(
        default=None,
        metadata={
            "name": "SeriesPartName",
            "type": "Element",
        }
    )
    number_within_series: Optional[NumberWithinSeries] = field(
        default=None,
        metadata={
            "name": "NumberWithinSeries",
            "type": "Element",
        }
    )
    title: List[Title] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    contributor: List[Contributor] = field(
        default_factory=list,
        metadata={
            "name": "Contributor",
            "type": "Element",
        }
    )
    other_text: List[OtherText] = field(
        default_factory=list,
        metadata={
            "name": "OtherText",
            "type": "Element",
        }
    )
    publisher: List[Publisher] = field(
        default_factory=list,
        metadata={
            "name": "Publisher",
            "type": "Element",
        }
    )
    subordinate_entries: Optional[SubordinateEntries] = field(
        default=None,
        metadata={
            "name": "SubordinateEntries",
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
class SupplyDetail:
    class Meta:
        namespace = "http://www.editeur.org/onix/2.1/reference"

    supplier_identifier: List[SupplierIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "SupplierIdentifier",
            "type": "Element",
        }
    )
    supplier_san_or_supplier_eanlocation_number_or_supplier_name: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplierSAN",
                    "type": SupplierSan,
                },
                {
                    "name": "SupplierEANLocationNumber",
                    "type": SupplierEanlocationNumber,
                },
                {
                    "name": "SupplierName",
                    "type": SupplierName,
                },
            ),
            "max_occurs": 5,
        }
    )
    telephone_number: List[TelephoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "TelephoneNumber",
            "type": "Element",
        }
    )
    fax_number: List[FaxNumber] = field(
        default_factory=list,
        metadata={
            "name": "FaxNumber",
            "type": "Element",
        }
    )
    email_address: List[EmailAddress] = field(
        default_factory=list,
        metadata={
            "name": "EmailAddress",
            "type": "Element",
        }
    )
    website: List[Website] = field(
        default_factory=list,
        metadata={
            "name": "Website",
            "type": "Element",
        }
    )
    supplier_role: Optional[SupplierRole] = field(
        default=None,
        metadata={
            "name": "SupplierRole",
            "type": "Element",
        }
    )
    supply_to_country_or_supply_to_territory_or_supply_to_region: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplyToCountry",
                    "type": SupplyToCountry,
                },
                {
                    "name": "SupplyToTerritory",
                    "type": SupplyToTerritory,
                },
                {
                    "name": "SupplyToRegion",
                    "type": SupplyToRegion,
                },
            ),
        }
    )
    supply_to_country_excluded: List[SupplyToCountryExcluded] = field(
        default_factory=list,
        metadata={
            "name": "SupplyToCountryExcluded",
            "type": "Element",
        }
    )
    supply_restriction_detail: Optional[SupplyRestrictionDetail] = field(
        default=None,
        metadata={
            "name": "SupplyRestrictionDetail",
            "type": "Element",
        }
    )
    returns_code_type: Optional[ReturnsCodeType] = field(
        default=None,
        metadata={
            "name": "ReturnsCodeType",
            "type": "Element",
        }
    )
    returns_code: Optional[ReturnsCode] = field(
        default=None,
        metadata={
            "name": "ReturnsCode",
            "type": "Element",
        }
    )
    last_date_for_returns: Optional[LastDateForReturns] = field(
        default=None,
        metadata={
            "name": "LastDateForReturns",
            "type": "Element",
        }
    )
    availability_code: Optional[AvailabilityCode] = field(
        default=None,
        metadata={
            "name": "AvailabilityCode",
            "type": "Element",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ProductAvailability",
                    "type": ProductAvailability,
                },
                {
                    "name": "IntermediaryAvailabilityCode",
                    "type": IntermediaryAvailabilityCode,
                },
                {
                    "name": "NewSupplier",
                    "type": NewSupplier,
                },
                {
                    "name": "DateFormat",
                    "type": DateFormat,
                },
                {
                    "name": "ExpectedShipDate",
                    "type": ExpectedShipDate,
                },
                {
                    "name": "OnSaleDate",
                    "type": OnSaleDate,
                },
                {
                    "name": "OrderTime",
                    "type": OrderTime,
                },
            ),
            "max_occurs": 10,
        }
    )
    stock: List[Stock] = field(
        default_factory=list,
        metadata={
            "name": "Stock",
            "type": "Element",
        }
    )
    pack_quantity: Optional[PackQuantity] = field(
        default=None,
        metadata={
            "name": "PackQuantity",
            "type": "Element",
        }
    )
    audience_restriction_flag: Optional[AudienceRestrictionFlag] = field(
        default=None,
        metadata={
            "name": "AudienceRestrictionFlag",
            "type": "Element",
        }
    )
    audience_restriction_note: Optional[AudienceRestrictionNote] = field(
        default=None,
        metadata={
            "name": "AudienceRestrictionNote",
            "type": "Element",
        }
    )
    price_amount_or_unpriced_item_type_or_price: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PriceAmount",
                    "type": PriceAmount,
                },
                {
                    "name": "UnpricedItemType",
                    "type": UnpricedItemType,
                },
                {
                    "name": "Price",
                    "type": Price,
                },
            ),
        }
    )
    reissue: Optional[Reissue] = field(
        default=None,
        metadata={
            "name": "Reissue",
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
        namespace = "http://www.editeur.org/onix/2.1/reference"

    record_reference: Optional[RecordReference] = field(
        default=None,
        metadata={
            "name": "RecordReference",
            "type": "Element",
            "required": True,
        }
    )
    notification_type: Optional[NotificationType] = field(
        default=None,
        metadata={
            "name": "NotificationType",
            "type": "Element",
            "required": True,
        }
    )
    deletion_code: Optional[DeletionCode] = field(
        default=None,
        metadata={
            "name": "DeletionCode",
            "type": "Element",
        }
    )
    deletion_text: Optional[DeletionText] = field(
        default=None,
        metadata={
            "name": "DeletionText",
            "type": "Element",
        }
    )
    record_source_type: Optional[RecordSourceType] = field(
        default=None,
        metadata={
            "name": "RecordSourceType",
            "type": "Element",
        }
    )
    record_source_identifier_type: Optional[RecordSourceIdentifierType] = field(
        default=None,
        metadata={
            "name": "RecordSourceIdentifierType",
            "type": "Element",
        }
    )
    record_source_identifier: Optional[RecordSourceIdentifier] = field(
        default=None,
        metadata={
            "name": "RecordSourceIdentifier",
            "type": "Element",
        }
    )
    record_source_name: Optional[RecordSourceName] = field(
        default=None,
        metadata={
            "name": "RecordSourceName",
            "type": "Element",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ISBN",
                    "type": Isbn,
                },
                {
                    "name": "EAN13",
                    "type": Ean13,
                },
                {
                    "name": "UPC",
                    "type": Upc,
                },
                {
                    "name": "PublisherProductNo",
                    "type": PublisherProductNo,
                },
                {
                    "name": "ISMN",
                    "type": Ismn,
                },
                {
                    "name": "DOI",
                    "type": Doi,
                },
                {
                    "name": "ProductIdentifier",
                    "type": ProductIdentifier,
                },
            ),
        }
    )
    barcode: List[Barcode] = field(
        default_factory=list,
        metadata={
            "name": "Barcode",
            "type": "Element",
        }
    )
    replaces_isbn: Optional[ReplacesIsbn] = field(
        default=None,
        metadata={
            "name": "ReplacesISBN",
            "type": "Element",
        }
    )
    replaces_ean13: Optional[ReplacesEan13] = field(
        default=None,
        metadata={
            "name": "ReplacesEAN13",
            "type": "Element",
        }
    )
    product_form: Optional[ProductForm] = field(
        default=None,
        metadata={
            "name": "ProductForm",
            "type": "Element",
        }
    )
    product_form_detail: List[ProductFormDetail] = field(
        default_factory=list,
        metadata={
            "name": "ProductFormDetail",
            "type": "Element",
        }
    )
    product_form_feature: List[ProductFormFeature] = field(
        default_factory=list,
        metadata={
            "name": "ProductFormFeature",
            "type": "Element",
        }
    )
    book_form_detail: List[BookFormDetail] = field(
        default_factory=list,
        metadata={
            "name": "BookFormDetail",
            "type": "Element",
        }
    )
    product_packaging: Optional[ProductPackaging] = field(
        default=None,
        metadata={
            "name": "ProductPackaging",
            "type": "Element",
        }
    )
    product_form_description: Optional[ProductFormDescription] = field(
        default=None,
        metadata={
            "name": "ProductFormDescription",
            "type": "Element",
        }
    )
    number_of_pieces: Optional[NumberOfPieces] = field(
        default=None,
        metadata={
            "name": "NumberOfPieces",
            "type": "Element",
        }
    )
    trade_category: Optional[TradeCategory] = field(
        default=None,
        metadata={
            "name": "TradeCategory",
            "type": "Element",
        }
    )
    product_content_type: List[ProductContentType] = field(
        default_factory=list,
        metadata={
            "name": "ProductContentType",
            "type": "Element",
        }
    )
    contained_item: List[ContainedItem] = field(
        default_factory=list,
        metadata={
            "name": "ContainedItem",
            "type": "Element",
        }
    )
    product_classification: List[ProductClassification] = field(
        default_factory=list,
        metadata={
            "name": "ProductClassification",
            "type": "Element",
        }
    )
    epub_type: Optional[EpubType] = field(
        default=None,
        metadata={
            "name": "EpubType",
            "type": "Element",
        }
    )
    epub_type_version: Optional[EpubTypeVersion] = field(
        default=None,
        metadata={
            "name": "EpubTypeVersion",
            "type": "Element",
        }
    )
    epub_type_description: Optional[EpubTypeDescription] = field(
        default=None,
        metadata={
            "name": "EpubTypeDescription",
            "type": "Element",
        }
    )
    epub_format: Optional[EpubFormat] = field(
        default=None,
        metadata={
            "name": "EpubFormat",
            "type": "Element",
        }
    )
    epub_format_version: Optional[EpubFormatVersion] = field(
        default=None,
        metadata={
            "name": "EpubFormatVersion",
            "type": "Element",
        }
    )
    epub_format_description: Optional[EpubFormatDescription] = field(
        default=None,
        metadata={
            "name": "EpubFormatDescription",
            "type": "Element",
        }
    )
    epub_source: Optional[EpubSource] = field(
        default=None,
        metadata={
            "name": "EpubSource",
            "type": "Element",
        }
    )
    epub_source_version: Optional[EpubSourceVersion] = field(
        default=None,
        metadata={
            "name": "EpubSourceVersion",
            "type": "Element",
        }
    )
    epub_source_description: Optional[EpubSourceDescription] = field(
        default=None,
        metadata={
            "name": "EpubSourceDescription",
            "type": "Element",
        }
    )
    epub_type_note: Optional[EpubTypeNote] = field(
        default=None,
        metadata={
            "name": "EpubTypeNote",
            "type": "Element",
        }
    )
    series_or_no_series: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Series",
                    "type": Series,
                },
                {
                    "name": "NoSeries",
                    "type": NoSeries,
                },
            ),
        }
    )
    set: List[Set] = field(
        default_factory=list,
        metadata={
            "name": "Set",
            "type": "Element",
        }
    )
    text_case_flag: Optional[TextCaseFlag] = field(
        default=None,
        metadata={
            "name": "TextCaseFlag",
            "type": "Element",
        }
    )
    distinctive_title: Optional[DistinctiveTitle] = field(
        default=None,
        metadata={
            "name": "DistinctiveTitle",
            "type": "Element",
        }
    )
    choice_1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TitlePrefix",
                    "type": TitlePrefix,
                },
                {
                    "name": "TitleWithoutPrefix",
                    "type": TitleWithoutPrefix,
                },
                {
                    "name": "Subtitle",
                    "type": Subtitle,
                },
                {
                    "name": "TranslationOfTitle",
                    "type": TranslationOfTitle,
                },
            ),
            "max_occurs": 6,
        }
    )
    former_title_or_title: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FormerTitle",
                    "type": FormerTitle,
                },
                {
                    "name": "Title",
                    "type": Title,
                },
            ),
        }
    )
    work_identifier: List[WorkIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "WorkIdentifier",
            "type": "Element",
        }
    )
    website: List[Website] = field(
        default_factory=list,
        metadata={
            "name": "Website",
            "type": "Element",
        }
    )
    thesis_type: Optional[ThesisType] = field(
        default=None,
        metadata={
            "name": "ThesisType",
            "type": "Element",
        }
    )
    thesis_presented_to: Optional[ThesisPresentedTo] = field(
        default=None,
        metadata={
            "name": "ThesisPresentedTo",
            "type": "Element",
        }
    )
    thesis_year: Optional[ThesisYear] = field(
        default=None,
        metadata={
            "name": "ThesisYear",
            "type": "Element",
        }
    )
    contributor_or_contributor_statement_or_no_contributor: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Contributor",
                    "type": Contributor,
                },
                {
                    "name": "ContributorStatement",
                    "type": ContributorStatement,
                },
                {
                    "name": "NoContributor",
                    "type": NoContributor,
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
                    "name": "ConferenceDescription",
                    "type": ConferenceDescription,
                },
                {
                    "name": "ConferenceRole",
                    "type": ConferenceRole,
                },
                {
                    "name": "ConferenceName",
                    "type": ConferenceName,
                },
                {
                    "name": "ConferenceNumber",
                    "type": ConferenceNumber,
                },
                {
                    "name": "ConferenceDate",
                    "type": ConferenceDate,
                },
                {
                    "name": "ConferencePlace",
                    "type": ConferencePlace,
                },
                {
                    "name": "Conference",
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
                    "name": "EditionTypeCode",
                    "type": EditionTypeCode,
                },
                {
                    "name": "EditionNumber",
                    "type": EditionNumber,
                },
                {
                    "name": "EditionVersionNumber",
                    "type": EditionVersionNumber,
                },
                {
                    "name": "EditionStatement",
                    "type": EditionStatement,
                },
                {
                    "name": "NoEdition",
                    "type": NoEdition,
                },
            ),
        }
    )
    religious_text: Optional[ReligiousText] = field(
        default=None,
        metadata={
            "name": "ReligiousText",
            "type": "Element",
        }
    )
    language_of_text: List[LanguageOfText] = field(
        default_factory=list,
        metadata={
            "name": "LanguageOfText",
            "type": "Element",
        }
    )
    original_language: Optional[OriginalLanguage] = field(
        default=None,
        metadata={
            "name": "OriginalLanguage",
            "type": "Element",
        }
    )
    language: List[Language] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
        }
    )
    number_of_pages: Optional[NumberOfPages] = field(
        default=None,
        metadata={
            "name": "NumberOfPages",
            "type": "Element",
        }
    )
    pages_roman: Optional[PagesRoman] = field(
        default=None,
        metadata={
            "name": "PagesRoman",
            "type": "Element",
        }
    )
    pages_arabic: Optional[PagesArabic] = field(
        default=None,
        metadata={
            "name": "PagesArabic",
            "type": "Element",
        }
    )
    extent: List[Extent] = field(
        default_factory=list,
        metadata={
            "name": "Extent",
            "type": "Element",
        }
    )
    number_of_illustrations: Optional[NumberOfIllustrations] = field(
        default=None,
        metadata={
            "name": "NumberOfIllustrations",
            "type": "Element",
        }
    )
    illustrations_note: Optional[IllustrationsNote] = field(
        default=None,
        metadata={
            "name": "IllustrationsNote",
            "type": "Element",
        }
    )
    illustrations: List[Illustrations] = field(
        default_factory=list,
        metadata={
            "name": "Illustrations",
            "type": "Element",
        }
    )
    map_scale: List[MapScale] = field(
        default_factory=list,
        metadata={
            "name": "MapScale",
            "type": "Element",
        }
    )
    basicmain_subject: Optional[BasicmainSubject] = field(
        default=None,
        metadata={
            "name": "BASICMainSubject",
            "type": "Element",
        }
    )
    basicversion: Optional[Basicversion] = field(
        default=None,
        metadata={
            "name": "BASICVersion",
            "type": "Element",
        }
    )
    bicmain_subject: Optional[BicmainSubject] = field(
        default=None,
        metadata={
            "name": "BICMainSubject",
            "type": "Element",
        }
    )
    bicversion: Optional[Bicversion] = field(
        default=None,
        metadata={
            "name": "BICVersion",
            "type": "Element",
        }
    )
    main_subject: List[MainSubject] = field(
        default_factory=list,
        metadata={
            "name": "MainSubject",
            "type": "Element",
        }
    )
    subject: List[Subject] = field(
        default_factory=list,
        metadata={
            "name": "Subject",
            "type": "Element",
        }
    )
    person_as_subject: List[PersonAsSubject] = field(
        default_factory=list,
        metadata={
            "name": "PersonAsSubject",
            "type": "Element",
        }
    )
    corporate_body_as_subject: List[CorporateBodyAsSubject] = field(
        default_factory=list,
        metadata={
            "name": "CorporateBodyAsSubject",
            "type": "Element",
        }
    )
    place_as_subject: List[PlaceAsSubject] = field(
        default_factory=list,
        metadata={
            "name": "PlaceAsSubject",
            "type": "Element",
        }
    )
    audience_code: List[AudienceCode] = field(
        default_factory=list,
        metadata={
            "name": "AudienceCode",
            "type": "Element",
        }
    )
    audience: List[Audience] = field(
        default_factory=list,
        metadata={
            "name": "Audience",
            "type": "Element",
        }
    )
    usschool_grade: Optional[UsschoolGrade] = field(
        default=None,
        metadata={
            "name": "USSchoolGrade",
            "type": "Element",
        }
    )
    interest_age: Optional[InterestAge] = field(
        default=None,
        metadata={
            "name": "InterestAge",
            "type": "Element",
        }
    )
    audience_range: List[AudienceRange] = field(
        default_factory=list,
        metadata={
            "name": "AudienceRange",
            "type": "Element",
        }
    )
    audience_description: Optional[AudienceDescription] = field(
        default=None,
        metadata={
            "name": "AudienceDescription",
            "type": "Element",
        }
    )
    complexity: List[Complexity] = field(
        default_factory=list,
        metadata={
            "name": "Complexity",
            "type": "Element",
        }
    )
    annotation: Optional[Annotation] = field(
        default=None,
        metadata={
            "name": "Annotation",
            "type": "Element",
        }
    )
    main_description: Optional[MainDescription] = field(
        default=None,
        metadata={
            "name": "MainDescription",
            "type": "Element",
        }
    )
    other_text: List[OtherText] = field(
        default_factory=list,
        metadata={
            "name": "OtherText",
            "type": "Element",
        }
    )
    review_quote: List[ReviewQuote] = field(
        default_factory=list,
        metadata={
            "name": "ReviewQuote",
            "type": "Element",
        }
    )
    cover_image_format_code: Optional[CoverImageFormatCode] = field(
        default=None,
        metadata={
            "name": "CoverImageFormatCode",
            "type": "Element",
        }
    )
    cover_image_link_type_code: Optional[CoverImageLinkTypeCode] = field(
        default=None,
        metadata={
            "name": "CoverImageLinkTypeCode",
            "type": "Element",
        }
    )
    cover_image_link: Optional[CoverImageLink] = field(
        default=None,
        metadata={
            "name": "CoverImageLink",
            "type": "Element",
        }
    )
    media_file: List[MediaFile] = field(
        default_factory=list,
        metadata={
            "name": "MediaFile",
            "type": "Element",
        }
    )
    product_website: List[ProductWebsite] = field(
        default_factory=list,
        metadata={
            "name": "ProductWebsite",
            "type": "Element",
        }
    )
    prizes_description_or_prize: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PrizesDescription",
                    "type": PrizesDescription,
                },
                {
                    "name": "Prize",
                    "type": Prize,
                },
            ),
        }
    )
    content_item: List[ContentItem] = field(
        default_factory=list,
        metadata={
            "name": "ContentItem",
            "type": "Element",
        }
    )
    choice_4: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ImprintName",
                    "type": ImprintName,
                },
                {
                    "name": "Imprint",
                    "type": Imprint,
                },
                {
                    "name": "PublisherName",
                    "type": PublisherName,
                },
                {
                    "name": "Publisher",
                    "type": Publisher,
                },
            ),
        }
    )
    city_of_publication: List[CityOfPublication] = field(
        default_factory=list,
        metadata={
            "name": "CityOfPublication",
            "type": "Element",
        }
    )
    country_of_publication: Optional[CountryOfPublication] = field(
        default=None,
        metadata={
            "name": "CountryOfPublication",
            "type": "Element",
        }
    )
    copublisher_name: List[CopublisherName] = field(
        default_factory=list,
        metadata={
            "name": "CopublisherName",
            "type": "Element",
        }
    )
    sponsor_name: List[SponsorName] = field(
        default_factory=list,
        metadata={
            "name": "SponsorName",
            "type": "Element",
        }
    )
    original_publisher: Optional[OriginalPublisher] = field(
        default=None,
        metadata={
            "name": "OriginalPublisher",
            "type": "Element",
        }
    )
    publishing_status: Optional[PublishingStatus] = field(
        default=None,
        metadata={
            "name": "PublishingStatus",
            "type": "Element",
        }
    )
    publishing_status_note: Optional[PublishingStatusNote] = field(
        default=None,
        metadata={
            "name": "PublishingStatusNote",
            "type": "Element",
        }
    )
    announcement_date: Optional[AnnouncementDate] = field(
        default=None,
        metadata={
            "name": "AnnouncementDate",
            "type": "Element",
        }
    )
    trade_announcement_date: Optional[TradeAnnouncementDate] = field(
        default=None,
        metadata={
            "name": "TradeAnnouncementDate",
            "type": "Element",
        }
    )
    publication_date: Optional[PublicationDate] = field(
        default=None,
        metadata={
            "name": "PublicationDate",
            "type": "Element",
        }
    )
    copyright_statement_or_copyright_year: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CopyrightStatement",
                    "type": CopyrightStatement,
                },
                {
                    "name": "CopyrightYear",
                    "type": CopyrightYear,
                },
            ),
        }
    )
    year_first_published: Optional[YearFirstPublished] = field(
        default=None,
        metadata={
            "name": "YearFirstPublished",
            "type": "Element",
        }
    )
    sales_rights: List[SalesRights] = field(
        default_factory=list,
        metadata={
            "name": "SalesRights",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    not_for_sale: List[NotForSale] = field(
        default_factory=list,
        metadata={
            "name": "NotForSale",
            "type": "Element",
        }
    )
    sales_restriction: List[SalesRestriction] = field(
        default_factory=list,
        metadata={
            "name": "SalesRestriction",
            "type": "Element",
        }
    )
    choice_5: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Height",
                    "type": Height,
                },
                {
                    "name": "Width",
                    "type": Width,
                },
                {
                    "name": "Thickness",
                    "type": Thickness,
                },
                {
                    "name": "Weight",
                    "type": Weight,
                },
                {
                    "name": "Measure",
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
                    "name": "Dimensions",
                    "type": Dimensions,
                },
                {
                    "name": "ReplacedByISBN",
                    "type": ReplacedByIsbn,
                },
                {
                    "name": "ReplacedByEAN13",
                    "type": ReplacedByEan13,
                },
                {
                    "name": "AlternativeFormatISBN",
                    "type": AlternativeFormatIsbn,
                },
                {
                    "name": "AlternativeFormatEAN13",
                    "type": AlternativeFormatEan13,
                },
                {
                    "name": "AlternativeProductISBN",
                    "type": AlternativeProductIsbn,
                },
                {
                    "name": "AlternativeProductEAN13",
                    "type": AlternativeProductEan13,
                },
            ),
            "max_occurs": 8,
        }
    )
    related_product: List[RelatedProduct] = field(
        default_factory=list,
        metadata={
            "name": "RelatedProduct",
            "type": "Element",
        }
    )
    out_of_print_date: Optional[OutOfPrintDate] = field(
        default=None,
        metadata={
            "name": "OutOfPrintDate",
            "type": "Element",
        }
    )
    supply_detail: List[SupplyDetail] = field(
        default_factory=list,
        metadata={
            "name": "SupplyDetail",
            "type": "Element",
        }
    )
    market_representation: List[MarketRepresentation] = field(
        default_factory=list,
        metadata={
            "name": "MarketRepresentation",
            "type": "Element",
        }
    )
    promotion_campaign: Optional[PromotionCampaign] = field(
        default=None,
        metadata={
            "name": "PromotionCampaign",
            "type": "Element",
        }
    )
    promotion_contact: Optional[PromotionContact] = field(
        default=None,
        metadata={
            "name": "PromotionContact",
            "type": "Element",
        }
    )
    initial_print_run: Optional[InitialPrintRun] = field(
        default=None,
        metadata={
            "name": "InitialPrintRun",
            "type": "Element",
        }
    )
    reprint_detail: List[ReprintDetail] = field(
        default_factory=list,
        metadata={
            "name": "ReprintDetail",
            "type": "Element",
        }
    )
    copies_sold: Optional[CopiesSold] = field(
        default=None,
        metadata={
            "name": "CopiesSold",
            "type": "Element",
        }
    )
    book_club_adoption: Optional[BookClubAdoption] = field(
        default=None,
        metadata={
            "name": "BookClubAdoption",
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
        name = "ONIXMessage"
        namespace = "http://www.editeur.org/onix/2.1/reference"

    header: Optional[Header] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )
    product_or_main_series_record_or_sub_series_record: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Product",
                    "type": Product,
                },
                {
                    "name": "MainSeriesRecord",
                    "type": MainSeriesRecord,
                },
                {
                    "name": "SubSeriesRecord",
                    "type": SubSeriesRecord,
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
