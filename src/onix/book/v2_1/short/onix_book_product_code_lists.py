from enum import Enum

__NAMESPACE__ = "http://www.editeur.org/onix/2.1/short"


class List1(Enum):
    """
    Notification or update type code.

    :cvar VALUE_01: Early notification Use for a complete record issued
        earlier than approximately six months before publication
    :cvar VALUE_02: Advance notification (confirmed) Use for a complete
        record issued to confirm advance information approximately six
        months before publication; or for a complete record issued after
        that date and before information has been confirmed from the
        book-in-hand
    :cvar VALUE_03: Notification confirmed on publication Use for a
        complete record issued to confirm advance information at or just
        before actual publication date; or for a complete record issued
        at any later date
    :cvar VALUE_04: Update (partial) In ONIX 3.0 only, use when sending
        a ‘block update’ record. In previous ONIX releases, ONIX
        updating has generally been by complete record replacement using
        code 03, and code 04 is not used
    :cvar VALUE_05: Delete Use when sending an instruction to delete a
        record which was previously issued. Note that a Delete
        instruction should NOT be used when a product is cancelled, put
        out of print, or otherwise withdrawn from sale: this should be
        handled as a change of Publishing status, leaving the receiver
        to decide whether to retain or delete the record. A Delete
        instruction is only used when there is a particular reason to
        withdraw a record completely, eg because it was issued in error
    :cvar VALUE_08: Notice of sale Notice of sale of a product, from one
        publisher to another: sent by the publisher disposing of the
        product
    :cvar VALUE_09: Notice of acquisition Notice of acquisition of a
        product, by one publisher from another: sent by the acquiring
        publisher
    :cvar VALUE_12: Update – SupplyDetail only ONIX Books 2.1 supply
        update – &lt;SupplyDetail&gt; only (not used in ONIX 3.0)
    :cvar VALUE_13: Update – MarketRepresentation only ONIX Books 2.1
        supply update – &lt;MarketRepresentation&gt; only (not used in
        ONIX 3.0)
    :cvar VALUE_14: Update – SupplyDetail and MarketRepresentation ONIX
        Books 2.1 supply update – both &lt;SupplyDetail&gt; and
        &lt;MarketRepresentation&gt; (not used in ONIX 3.0)
    :cvar VALUE_88: Test update (Partial) ONIX 3.0 only. Record may be
        processed for test purposes, but data should be discarded.
        Sender must ensure the &lt;RecordReference&gt; matches a
        previously-sent Test record
    :cvar VALUE_89: Test record Record may be processed for test
        purposes, but data should be discarded. Sender must ensure the
        &lt;RecordReference&gt; does not match any previously-sent live
        product record
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_88 = "88"
    VALUE_89 = "89"


class List10(Enum):
    """
    Epublication type code.

    :cvar VALUE_000: Epublication ‘content package’ An epublication
        viewed as a unique package of content which may be converted
        into any of a number of different types for delivery to the
        consumer. This code is used when an ONIX &lt;Product&gt; record
        describes the content package and lists within the record the
        different forms in which it is available
    :cvar VALUE_001: HTML An epublication delivered in a basic,
        unprotected, HTML format. Do NOT use for HTML-based formats
        which include DRM protection
    :cvar VALUE_002: PDF An epublication delivered in a basic,
        unprotected, PDF format. Do NOT use for PDF-based formats which
        include DRM protection
    :cvar VALUE_003: PDF-Merchant An epublication delivered in PDF
        format, capable of being read in the standard Acrobat Reader,
        and protected by PDF-Merchant DRM features. (This format is no
        longer supported for new applications)
    :cvar VALUE_004: Adobe Ebook Reader An epublication delivered in an
        enhanced PDF format, using Adobe’s proprietary EBX DRM, capable
        of being read in the Adobe Ebook Reader software, on any
        platform which can support this software, which was formerly
        known as Glassbook
    :cvar VALUE_005: Microsoft Reader Level 1/Level 3 An epublication
        delivered in an unencrypted Microsoft .LIT format, capable of
        being read in the Microsoft Reader software at any level, on any
        platform which can support this software. (Level 3 differs from
        Level 1 only in that it embeds the name of the original
        purchaser)
    :cvar VALUE_006: Microsoft Reader Level 5 An epublication delivered
        in the Microsoft .LIT format, with full encryption, capable of
        being read in the Microsoft Reader software at Level 5, on any
        platform which can support this software
    :cvar VALUE_007: NetLibrary An epublication delivered in a
        proprietary HTML- or OEBF-based format, capable of being read
        only through subscription to the NetLibrary service
    :cvar VALUE_008: MetaText An epublication delivered in a proprietary
        format through a web browser, capable of being read only through
        subscription to the MetaText service (the educational division
        of NetLibrary)
    :cvar VALUE_009: MightyWords An epublication delivered in a
        proprietary PDF-based format, capable of being read only through
        subscription to the MightyWords service
    :cvar VALUE_010: eReader (AKA Palm Reader) An epublication delivered
        in a proprietary HTML-based format, capable of being read in
        reading software which may be used on handheld devices using the
        Palm OS or Pocket PC/Windows CE operating systems
    :cvar VALUE_011: Softbook An epublication delivered in a proprietary
        format capable of being read in reading software which is
        specific to the Softbook hardware platform. Also capable of
        being read on the Softbook’s successor, the Gemstar REB 1200
    :cvar VALUE_012: RocketBook An epublication delivered in a
        proprietary .RB format, capable of being read in reading
        software which is specific to the RocketBook hardware platform.
        Also capable of being read on the RocketBook’s successor, the
        Gemstar REB 1100
    :cvar VALUE_013: Gemstar REB 1100 An epublication delivered in a
        proprietary .RB format, capable of being read in reading
        software which is specific to the Gemstar REB 1100 hardware
        platform. Also capable of being read on the RocketBook with some
        loss of functionality
    :cvar VALUE_014: Gemstar REB 1200 An epublication delivered in a
        proprietary format, capable of being read in reading software
        which is specific to the Gemstar REB 1200 hardware platform.
        Also capable of being read on the Softbook with some loss of
        functionality
    :cvar VALUE_015: Franklin eBookman An epublication delivered in
        Franklin’s proprietary HTML-based format, capable of being read
        in reading software which is specific to the Franklin eBookman
        platform
    :cvar VALUE_016: Books24x7 An epublication delivered in a
        proprietary XML-based format and available for online access
        only through subscription to the Books24x7 service
    :cvar VALUE_017: DigitalOwl An epublication available through
        DigitalOwl proprietary packaging, distribution and DRM software,
        delivered in a variety of formats across a range of platforms
    :cvar VALUE_018: Handheldmed An epublication delivered in a
        proprietary HTML-based format, capable of being read in
        Handheldmed reader software on Palm OS, Windows, and EPOC/Psion
        handheld devices, available only through the Handheldmed service
    :cvar VALUE_019: WizeUp An epublication delivered in a proprietary
        ???-based format and available for download only through the
        WizeUp service
    :cvar VALUE_020: TK3 An epublication delivered in the proprietary
        TK3 format, capable of being read only in the TK3 reader
        software supplied by Night Kitchen Inc, on any platform which
        can support this software
    :cvar VALUE_021: Litraweb An epublication delivered in an encrypted
        .RTF format, capable of being read only in the Litraweb Visor
        software, and available only from Litraweb.com
    :cvar VALUE_022: MobiPocket An epublication delivered in a
        proprietary format, capable of being read in the MobiPocket
        software on PalmOS, WindowsCE /Pocket PC, Franklin eBookman, and
        EPOC32 handheld devices, available through the MobiPocket
        service. Includes Amazon Kindle formats up to and including
        version 7 – but prefer code 031 for version 7, and always use
        031 for KF8
    :cvar VALUE_023: Open Ebook An epublication delivered in the
        standard distribution format specified in the Open Ebook
        Publication Structure (OEBPS) format and capable of being read
        in any OEBPS-compliant reading system. Includes EPUB format up
        to and including version 2 – but prefer code 029 for EPUB 2, and
        always use 029 for EPUB 3
    :cvar VALUE_024: Town Compass DataViewer An epublication delivered
        in a proprietary format, capable of being read in Town Compass
        DataViewer reader software on a Palm OS handheld device
    :cvar VALUE_025: TXT An epublication delivered in an openly
        available .TXT format, with ASCII or UTF-8 encoding, as used for
        example in Project Gutenberg
    :cvar VALUE_026: ExeBook An epublication delivered as a self-
        executing file including its own reader software, and created
        with proprietary ExeBook Self-Publisher software
    :cvar VALUE_027: Sony BBeB An epublication in a Sony proprietary
        format for use with the Sony Reader and LIBRIé reading devices
    :cvar VALUE_028: VitalSource Bookshelf
    :cvar VALUE_029: EPUB An epublication delivered using the Open
        Publication Structure / OPS Container Format standard of the
        International Digital Publishing Forum (IDPF). [This value was
        originally defined as ‘Adobe Digital Editions’, which is not an
        epublication format but a reader which supports PDF or EPUB
        (IDPF) formats. Since PDF is already covered by code 002, it was
        agreed, and announced to the ONIX listserv in September 2009,
        that code 029 should be refined to represent EPUB format]
    :cvar VALUE_030: MyiLibrary
    :cvar VALUE_031: Kindle Amazon proprietary file format derived from
        Mobipocket format, used for Kindle devices and Kindle reader
        software
    :cvar VALUE_032: Google Edition An epublication made available by
        Google in association with a publisher; readable online on a
        browser-enabled device and offline on designated ebook readers
    :cvar VALUE_033: Vook An epublication in a proprietary format
        combining text and video content and available to be used online
        or as a downloadable application for a mobile device – see
        www.vook.com
    :cvar VALUE_034: DXReader An epublication in a proprietary format
        for use with DXReader software
    :cvar VALUE_035: EBL An epublication in a format proprietary to the
        Ebook Library service
    :cvar VALUE_036: Ebrary An epublication in a format proprietary to
        the Ebrary service
    :cvar VALUE_037: iSilo An epublication in a proprietary format for
        use with iSilo software on various hardware platforms
    :cvar VALUE_038: Plucker An epublication in a proprietary format for
        use with Plucker reader software on Palm and other handheld
        devices
    :cvar VALUE_039: VitalBook A format proprietary to the VitalSource
        service
    :cvar VALUE_040: Book ‘app’ for iOS Epublication packaged as an
        application for iOS (eg Apple iPhone, iPad etc) containing both
        executable code and content. Content can be described with
        &lt;ProductContentType&gt;
    :cvar VALUE_041: Android ‘app’ Epublication packaged as an
        application for Android (eg Android phone or tablet) containing
        both executable code and content. Content can be described with
        &lt;ProductContentType&gt;
    :cvar VALUE_042: Other ‘app’ Epublication packaged as an
        application. Technical requirements such as target operating
        system and/or device should be provided in &lt;EpubTypeNote&gt;.
        Content can be described with &lt;ProductContentType&gt;
    :cvar VALUE_043: XPS XML Paper Specification format [File extension
        .xps] for (eg) Blio
    :cvar VALUE_044: iBook Apple’s iBook format (a proprietary extension
        of EPUB), can only be read on Apple iOS devices
    :cvar VALUE_045: ePIB Proprietary format based on EPUB used by
        Barnes and Noble for fixed-format e-books, readable on NOOK
        devices and Nook reader software
    :cvar VALUE_046: SCORM Sharable Content Object Reference Model,
        standard content and packaging format for e-learning objects
    :cvar VALUE_047: EBP E-book Plus (proprietary Norwegian e-book
        format based on HTML5 documents packaged within a zipped .ebp
        file)
    :cvar VALUE_048: Page Perfect Proprietary format based on PDF used
        by Barnes and Noble for fixed-format e-books, readable on some
        NOOK devices and Nook reader software
    :cvar VALUE_098: Multiple formats Product consists of parts in
        different formats
    :cvar VALUE_099: Unspecified Unknown, or no code yet assigned for
        this format
    """
    VALUE_000 = "000"
    VALUE_001 = "001"
    VALUE_002 = "002"
    VALUE_003 = "003"
    VALUE_004 = "004"
    VALUE_005 = "005"
    VALUE_006 = "006"
    VALUE_007 = "007"
    VALUE_008 = "008"
    VALUE_009 = "009"
    VALUE_010 = "010"
    VALUE_011 = "011"
    VALUE_012 = "012"
    VALUE_013 = "013"
    VALUE_014 = "014"
    VALUE_015 = "015"
    VALUE_016 = "016"
    VALUE_017 = "017"
    VALUE_018 = "018"
    VALUE_019 = "019"
    VALUE_020 = "020"
    VALUE_021 = "021"
    VALUE_022 = "022"
    VALUE_023 = "023"
    VALUE_024 = "024"
    VALUE_025 = "025"
    VALUE_026 = "026"
    VALUE_027 = "027"
    VALUE_028 = "028"
    VALUE_029 = "029"
    VALUE_030 = "030"
    VALUE_031 = "031"
    VALUE_032 = "032"
    VALUE_033 = "033"
    VALUE_034 = "034"
    VALUE_035 = "035"
    VALUE_036 = "036"
    VALUE_037 = "037"
    VALUE_038 = "038"
    VALUE_039 = "039"
    VALUE_040 = "040"
    VALUE_041 = "041"
    VALUE_042 = "042"
    VALUE_043 = "043"
    VALUE_044 = "044"
    VALUE_045 = "045"
    VALUE_046 = "046"
    VALUE_047 = "047"
    VALUE_048 = "048"
    VALUE_098 = "098"
    VALUE_099 = "099"


class List100(Enum):
    """
    Discount code type.

    :cvar VALUE_01: BIC discount group code UK publisher’s or
        distributor’s discount group code in a format specified by BIC
        to ensure uniqueness
    :cvar VALUE_02: Proprietary discount code A publisher’s or
        supplier’s own code which identifies a trade discount category,
        as specified in &lt;DiscountCodeTypeName&gt;. The actual
        discount for each code is set by trading partner agreement
        (applies to goods supplied on standard trade discounting terms)
    :cvar VALUE_03: Boeksoort Terms code used in the Netherlands book
        trade
    :cvar VALUE_04: German terms code Terms code used in German ONIX
        applications
    :cvar VALUE_05: Proprietary commission code A publisher’s or
        supplier’s own code which identifies a commission rate category,
        as specified in &lt;DiscountCodeTypeName&gt;. The actual
        commission rate for each code is set by trading partner
        agreement (applies to goods supplied on agency terms)
    :cvar VALUE_06: BIC commission group code UK publisher’s or
        distributor’s commission group code in format specified by BIC
        to ensure uniqueness. Format is identical to BIC discount group
        code, but indicates a commission rather than a discount (applies
        to goods supplied on agency terms)
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"


class List101(Enum):
    """
    Person name identifier type.

    :cvar VALUE_01: Proprietary Note that &lt;IDTypeName&gt; is required
        with proprietary identifiers
    :cvar VALUE_02: PND Personennamendatei – person name authority file
        used by Deutsche Nationalbibliothek and in other German-speaking
        countries. See
        http://www.d-nb.de/standardisierung/normdateien/pnd.htm (German)
        or http://www.d-nb.de/eng/standardisierung/normdateien/pnd.htm
        (English). DEPRECATED in favour of the GND
    :cvar VALUE_04: LCCN Library of Congress control number assigned to
        a Library of Congress Name Authority record
    :cvar VALUE_16: ISNI International Standard Name Identifier. See
        http://www.isni.org/
    :cvar VALUE_25: GND Gemeinsame Normdatei – Joint Authority File in
        the German-speaking countries. See http://www.dnb.de/EN/gnd
        (English). Combines the PND, SWD and GKD into a single authority
        file, and should be used in preference
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_04 = "04"
    VALUE_16 = "16"
    VALUE_25 = "25"


class List102(Enum):
    """
    Sales outlet identifier type.

    :cvar VALUE_01: Proprietary Proprietary list of retail and other
        end-user sales outlet IDs. Note that &lt;IDTypeName&gt; is
        required with proprietary identifiers
    :cvar VALUE_02: BIC sales outlet ID code DEPRECATED – use code 03
    :cvar VALUE_03: ONIX retail sales outlet ID code Use with ONIX
        retail and other end-user sales outlet IDs from List 139
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"


class List11(Enum):
    """
    Epublication format code.

    :cvar VALUE_01: HTML
    :cvar VALUE_02: PDF
    :cvar VALUE_03: Microsoft Reader ‘.LIT’ file format used by
        Microsoft Reader software
    :cvar VALUE_04: RocketBook
    :cvar VALUE_05: Rich text format (RTF)
    :cvar VALUE_06: Open Ebook Publication Structure (OEBPS) format
        standard
    :cvar VALUE_07: XML
    :cvar VALUE_08: SGML
    :cvar VALUE_09: EXE ‘.EXE’ file format used when an epublication is
        delivered as a self-executing package of software and content
    :cvar VALUE_10: ASCII ‘.TXT’ file format
    :cvar VALUE_11: MobiPocket format Proprietary file format used for
        the MobiPocket reader software
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"


class List12(Enum):
    """
    Trade category code.

    :cvar VALUE_01: UK open market edition An edition from a UK
        publisher sold only in territories where exclusive rights are
        not held. Rights details should be carried in PR.21 (ONIX 2.1)
        OR P.21 (ONIX 3.0) as usual
    :cvar VALUE_02: Airport edition In UK, an edition intended primarily
        for airside sales in UK airports, though it may be available for
        sale in other territories where exclusive rights are not held.
        Rights details should be carried in PR.21 (ONIX 2.1) OR P.21
        (ONIX 3.0) as usual
    :cvar VALUE_03: Sonderausgabe In Germany, a special printing sold at
        a lower price than the regular hardback
    :cvar VALUE_04: Pocket paperback In countries where recognised as a
        distinct trade category, eg France ‘livre de poche’, Germany
        ‘Taschenbuch’, Italy ‘tascabile’, Spain ‘libro de bolsillo’
    :cvar VALUE_05: International edition (US) Edition produced solely
        for sale in designated export markets
    :cvar VALUE_06: Library audio edition Audio product sold in special
        durable packaging and with a replacement guarantee for the
        contained cassettes or CDs for a specified shelf-life
    :cvar VALUE_07: US open market edition An edition from a US
        publisher sold only in territories where exclusive rights are
        not held. Rights details should be carried in PR.21 (ONIX 2.1)
        OR P.21 (ONIX 3.0) as usual
    :cvar VALUE_08: Livre scolaire, déclaré par l’éditeur In France, a
        category of book that has a particular legal status, claimed by
        the publisher
    :cvar VALUE_09: Livre scolaire (non spécifié) In France, a category
        of book that has a particular legal status, designated
        independently of the publisher
    :cvar VALUE_10: Supplement to newspaper Edition published for sale
        only with a newspaper or periodical
    :cvar VALUE_11: Precio libre textbook In Spain, a school textbook
        for which there is no fixed or suggested retail price and which
        is supplied by the publisher on terms individually agreed with
        the bookseller
    :cvar VALUE_12: News outlet edition For editions sold only through
        newsstands/newsagents
    :cvar VALUE_13: US textbook In the US and Canada, a book that is
        published primarily for use by students in school or college
        education as a basis for study. Textbooks published for the
        elementary and secondary school markets are generally purchased
        by school districts for the use of students. Textbooks published
        for the higher education market are generally adopted for use in
        particular classes by the instructors of those classes.
        Textbooks are usually not marketed to the general public, which
        distinguishes them from trade books. Note that trade books
        adopted for course use are not considered to be textbooks
        (though a specific education edition of a trade title may be)
    :cvar VALUE_14: E-book short ‘Short’ e-book (sometimes also called a
        ‘single’), typically containing a single short story, an essay
        or piece of long-form journalism
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"


class List13(Enum):
    """
    Series identifier type code.

    :cvar VALUE_01: Proprietary For example, publisher’s own series ID.
        Note that &lt;IDTypeName&gt; is required with proprietary
        identifiers
    :cvar VALUE_02: ISSN International Standard Serial Number,
        unhyphenated, 8 digits
    :cvar VALUE_03: German National Bibliography series ID Maintained by
        the Deutsche Nationalbibliothek
    :cvar VALUE_04: German Books in Print series ID Maintained by VLB
    :cvar VALUE_05: Electre series ID Maintained by Electre Information,
        France
    :cvar VALUE_06: DOI Digital Object Identifier (variable length and
        character set)
    :cvar VALUE_15: ISBN-13 Use only where the collection (series or
        set) is available as a single product
    :cvar VALUE_22: URN Uniform Resource Name
    :cvar VALUE_29: BNF Control number French National Bibliography
        series ID. Identifiant des publications en série maintenu par la
        Bibliothèque Nationale de France
    :cvar VALUE_35: ARK Archival Resource Key, as a URL (including the
        address of the ARK resolver provided by eg a national library)
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_15 = "15"
    VALUE_22 = "22"
    VALUE_29 = "29"
    VALUE_35 = "35"


class List138(Enum):
    """
    Transliteration scheme code.

    :cvar SFS4900: Finnish standard SFS 4900 Transliteration of Cyrillic
        characters – Slavic languages
    :cvar SFS5807: Finnish standard SFS 5807 Transliteration and
        transcription of Greek characters
    :cvar SFS5755: Finnish standard SFS 5755 Transliteration of Arabic
        characters
    :cvar SFS3602: Finnish standard SFS 5824 Transliteration of Hebrew
        characters
    :cvar ISO3602: ISO 3602 Documentation – Romanization of Japanese
        (kana script)
    :cvar ISO7098: ISO 7098 Information and documentation – Romanization
        of Chinese
    """
    SFS4900 = "SFS4900"
    SFS5807 = "SFS5807"
    SFS5755 = "SFS5755"
    SFS3602 = "SFS3602"
    ISO3602 = "ISO3602"
    ISO7098 = "ISO7098"


class List14(Enum):
    """
    Text case flag.

    :cvar VALUE_00: Undefined Default
    :cvar VALUE_01: Sentence case Initial capitals on first word and
        subsequently on proper names only, eg ‘The conquest of Mexico’
    :cvar VALUE_02: Title case Initial capitals on first word and
        subsequently on all significant words (nouns, pronouns,
        adjectives, verbs, adverbs, subordinate conjunctions)
        thereafter. Unless they appear as the first word, articles,
        prepositions and coordinating conjunctions remain lower case, eg
        ‘The Conquest of Mexico’
    :cvar VALUE_03: All capitals For example, ‘THE CONQUEST OF MEXICO’
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"


class List15(Enum):
    """
    Title type code.

    :cvar VALUE_00: Undefined
    :cvar VALUE_01: Distinctive title (book); Cover title (serial);
        Title on item (serial content item or reviewed resource) The
        full text of the distinctive title of the item, without
        abbreviation or abridgement. For books, where the title alone is
        not distinctive, elements may be taken from a set or series
        title and part number etc to create a distinctive title. Where
        the item is an omnibus edition containing two or more works by
        the same author, and there is no separate combined title, a
        distinctive title may be constructed by concatenating the
        individual titles, with suitable punctuation, as in ‘Pride and
        prejudice / Sense and sensibility / Northanger Abbey’
    :cvar VALUE_02: ISSN key title of serial Serials only
    :cvar VALUE_03: Title in original language Where the subject of the
        ONIX record is a translated item
    :cvar VALUE_04: Title acronym or initialism For serials: an acronym
        or initialism of Title Type 01, eg ‘JAMA’, ‘JACM’
    :cvar VALUE_05: Abbreviated title An abbreviated form of Title Type
        01
    :cvar VALUE_06: Title in other language A translation of Title Type
        01 into another language
    :cvar VALUE_07: Thematic title of journal issue Serials only: when a
        journal issue is explicitly devoted to a specified topic
    :cvar VALUE_08: Former title Books or serials: when an item was
        previously published under another title
    :cvar VALUE_10: Distributor’s title For books: the title carried in
        a book distributor’s title file: frequently incomplete, and may
        include elements not properly part of the title
    :cvar VALUE_11: Alternative title on cover An alternative title that
        appears on the cover of a book
    :cvar VALUE_12: Alternative title on back An alternative title that
        appears on the back of a book
    :cvar VALUE_13: Expanded title An expanded form of the title, eg the
        title of a school text book with grade and type and other
        details added to make the title meaningful, where otherwise it
        would comprise only the curriculum subject. This title type is
        required for submissions to the Spanish ISBN Agency
    :cvar VALUE_14: Alternative title An alternative title that the book
        is widely known by, whether it appears on the book or not
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"


class List16(Enum):
    """
    Work identifier type code.

    :cvar VALUE_01: Proprietary Note that &lt;IDTypeName&gt; is required
        with proprietary identifiers
    :cvar VALUE_02: ISBN-10 10-character ISBN of manifestation of work,
        when this is the only work identifier available – now DEPRECATED
        in ONIX for Books, except where providing historical information
        for compatibility with legacy systems. It should only be used in
        relation to products published before 2007 – when ISBN-13
        superseded it – and should never be used as the ONLY identifier
        (it should always be accompanied by the correct GTIN-13 /
        ISBN-13 of the manifestation of the work)
    :cvar VALUE_06: DOI Digital Object Identifier (variable length and
        character set)
    :cvar VALUE_11: ISTC International Standard Text Code (16
        characters: numerals and letters A-F, unhyphenated)
    :cvar VALUE_15: ISBN-13 13-character ISBN of manifestation of work,
        when this is the only work identifier available
    :cvar VALUE_18: ISRC International Standard Recording Code
    :cvar VALUE_32: GLIMIR Global Library Manifestation Identifier,
        OCLC’s ‘manifestation cluster’ ID
    :cvar VALUE_33: OWI OCLC Work Identifier
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_06 = "06"
    VALUE_11 = "11"
    VALUE_15 = "15"
    VALUE_18 = "18"
    VALUE_32 = "32"
    VALUE_33 = "33"


class List17(Enum):
    """
    Contributor role code.

    :cvar A01: By (author) Author of a textual work
    :cvar A02: With With or as told to: ‘ghost’ author of a literary
        work
    :cvar A03: Screenplay by Writer of screenplay or script (film or
        video)
    :cvar A04: Libretto by Writer of libretto (opera): see also A31
    :cvar A05: Lyrics by Author of lyrics (song): see also A31
    :cvar A06: By (composer) Composer of music
    :cvar A07: By (artist) Visual artist when named as the primary
        creator of, eg, a book of reproductions of artworks
    :cvar A08: By (photographer) Photographer when named as the primary
        creator of, eg, a book of photographs
    :cvar A09: Created by
    :cvar A10: From an idea by
    :cvar A11: Designed by
    :cvar A12: Illustrated by Artist when named as the creator of
        artwork which illustrates a text, or the originator (sometimes
        ‘penciller’ for collaborative art) of the artwork of a graphic
        novel or comic book
    :cvar A13: Photographs by Photographer when named as the creator of
        photographs which illustrate a text
    :cvar A14: Text by Author of text which accompanies art
        reproductions or photographs, or which is part of a graphic
        novel or comic book
    :cvar A15: Preface by Author of preface
    :cvar A16: Prologue by Author of prologue
    :cvar A17: Summary by Author of summary
    :cvar A18: Supplement by Author of supplement
    :cvar A19: Afterword by Author of afterword
    :cvar A20: Notes by Author of notes or annotations: see also A29
    :cvar A21: Commentaries by Author of commentaries on the main text
    :cvar A22: Epilogue by Author of epilogue
    :cvar A23: Foreword by Author of foreword
    :cvar A24: Introduction by Author of introduction: see also A29
    :cvar A25: Footnotes by Author/compiler of footnotes
    :cvar A26: Memoir by Author of memoir accompanying main text
    :cvar A27: Experiments by Person who carried out experiments
        reported in the text
    :cvar A29: Introduction and notes by Author of introduction and
        notes: see also A20 and A24
    :cvar A30: Software written by Writer of computer programs ancillary
        to the text
    :cvar A31: Book and lyrics by Author of the textual content of a
        musical drama: see also A04 and A05
    :cvar A32: Contributions by Author of additional contributions to
        the text
    :cvar A33: Appendix by Author of appendix
    :cvar A34: Index by Compiler of index
    :cvar A35: Drawings by
    :cvar A36: Cover design or artwork by Use also for the cover artist
        of a graphic novel or comic book if named separately
    :cvar A37: Preliminary work by Responsible for preliminary work on
        which the work is based
    :cvar A38: Original author Author of the first edition (usually of a
        standard work) who is not an author of the current edition
    :cvar A39: Maps by Maps drawn or otherwise contributed by
    :cvar A40: Inked or colored by Use for secondary creators when
        separate persons are named as having respectively drawn and
        inked/colored/finished artwork, eg for a graphic novel or comic
        book. Use with A12 for ‘drawn by’. Use A40 for 'finished by',
        but prefer more specific codes A46 to A48 instead of A40 unless
        the more specific secondary roles are inappropriate, unclear or
        unavailable
    :cvar A41: Pop-ups by Designer of pop-ups in a pop-up book, who may
        be different from the illustrator
    :cvar A42: Continued by Use where a standard work is being continued
        by somebody other than the original author
    :cvar A43: Interviewer
    :cvar A44: Interviewee
    :cvar A45: Comic script by Writer of dialogue, captions in a comic
        book (following an outline by the primary writer)
    :cvar A46: Inker Renders final comic book line art based on work of
        the illustrator or penciller. Preferred to code A40
    :cvar A47: Colorist Provides comic book color art and effects.
        Preferred to code A40
    :cvar A48: Letterer Creates comic book text balloons and other text
        elements (where this is a distinct role from script writer
        and/or illustrator)
    :cvar A99: Other primary creator Other type of primary creator not
        specified above
    :cvar B01: Edited by
    :cvar B02: Revised by
    :cvar B03: Retold by
    :cvar B04: Abridged by
    :cvar B05: Adapted by
    :cvar B06: Translated by
    :cvar B07: As told by
    :cvar B08: Translated with commentary by This code applies where a
        translator has provided a commentary on issues relating to the
        translation. If the translator has also provided a commentary on
        the work itself, codes B06 and A21 should be used
    :cvar B09: Series edited by Name of a series editor when the product
        belongs to a series
    :cvar B10: Edited and translated by
    :cvar B11: Editor-in-chief
    :cvar B12: Guest editor
    :cvar B13: Volume editor
    :cvar B14: Editorial board member
    :cvar B15: Editorial coordination by
    :cvar B16: Managing editor
    :cvar B17: Founded by Usually the founder editor of a serial
        publication: Begruendet von
    :cvar B18: Prepared for publication by
    :cvar B19: Associate editor
    :cvar B20: Consultant editor Use also for ‘advisory editor’, ‘series
        advisor’, ‘editorial consultant’ etc
    :cvar B21: General editor
    :cvar B22: Dramatized by
    :cvar B23: General rapporteur In Europe, an expert editor who takes
        responsibility for the legal content of a collaborative law
        volume
    :cvar B24: Literary editor An editor who is responsible for
        establishing the text used in an edition of a literary work,
        where this is recognised as a distinctive role (in Spain,
        ‘editor literario’)
    :cvar B25: Arranged by (music)
    :cvar B26: Technical editor Responsible for the technical accuracy
        and language, may also be involved in coordinating and preparing
        technical material for publication
    :cvar B27: Thesis advisor or supervisor
    :cvar B28: Thesis examiner
    :cvar B29: Scientific editor Responsible overall for the scientific
        content of the publication
    :cvar B99: Other adaptation by Other type of adaptation or editing
        not specified above
    :cvar C01: Compiled by For puzzles, directories, statistics, etc
    :cvar C02: Selected by For textual material (eg for an anthology)
    :cvar C03: Non-text material selected by Eg for a collection of
        photographs etc
    :cvar C04: Curated by Eg for an exhibition
    :cvar C99: Other compilation by Other type of compilation not
        specified above
    :cvar D01: Producer
    :cvar D02: Director
    :cvar D03: Conductor Conductor of a musical performance
    :cvar D99: Other direction by Other type of direction not specified
        above
    :cvar E01: Actor
    :cvar E02: Dancer
    :cvar E03: Narrator
    :cvar E04: Commentator
    :cvar E05: Vocal soloist Singer etc
    :cvar E06: Instrumental soloist
    :cvar E07: Read by Reader of recorded text, as in an audiobook
    :cvar E08: Performed by (orchestra, band, ensemble) Name of a
        musical group in a performing role
    :cvar E09: Speaker Of a speech, lecture etc
    :cvar E10: Presenter Introduces and links other contributors and
        material, eg within a documentary
    :cvar E99: Performed by Other type of performer not specified above:
        use for a recorded performance which does not fit a category
        above, eg a performance by a stand-up comedian
    :cvar F01: Filmed/photographed by Cinematographer, etc
    :cvar F02: Editor (film or video)
    :cvar F99: Other recording by Other type of recording not specified
        above
    :cvar Z01: Assisted by May be associated with any contributor role,
        and placement should therefore be controlled by contributor
        sequence numbering
    :cvar Z02: Honored/dedicated to
    :cvar Z98: (Various roles) For use ONLY with ‘et al’ or ‘Various’
        within &lt;UnnamedPersons&gt;, where the roles of the multiple
        contributors vary
    :cvar Z99: Other Other creative responsibility not falling within A
        to F above
    """
    A01 = "A01"
    A02 = "A02"
    A03 = "A03"
    A04 = "A04"
    A05 = "A05"
    A06 = "A06"
    A07 = "A07"
    A08 = "A08"
    A09 = "A09"
    A10 = "A10"
    A11 = "A11"
    A12 = "A12"
    A13 = "A13"
    A14 = "A14"
    A15 = "A15"
    A16 = "A16"
    A17 = "A17"
    A18 = "A18"
    A19 = "A19"
    A20 = "A20"
    A21 = "A21"
    A22 = "A22"
    A23 = "A23"
    A24 = "A24"
    A25 = "A25"
    A26 = "A26"
    A27 = "A27"
    A29 = "A29"
    A30 = "A30"
    A31 = "A31"
    A32 = "A32"
    A33 = "A33"
    A34 = "A34"
    A35 = "A35"
    A36 = "A36"
    A37 = "A37"
    A38 = "A38"
    A39 = "A39"
    A40 = "A40"
    A41 = "A41"
    A42 = "A42"
    A43 = "A43"
    A44 = "A44"
    A45 = "A45"
    A46 = "A46"
    A47 = "A47"
    A48 = "A48"
    A99 = "A99"
    B01 = "B01"
    B02 = "B02"
    B03 = "B03"
    B04 = "B04"
    B05 = "B05"
    B06 = "B06"
    B07 = "B07"
    B08 = "B08"
    B09 = "B09"
    B10 = "B10"
    B11 = "B11"
    B12 = "B12"
    B13 = "B13"
    B14 = "B14"
    B15 = "B15"
    B16 = "B16"
    B17 = "B17"
    B18 = "B18"
    B19 = "B19"
    B20 = "B20"
    B21 = "B21"
    B22 = "B22"
    B23 = "B23"
    B24 = "B24"
    B25 = "B25"
    B26 = "B26"
    B27 = "B27"
    B28 = "B28"
    B29 = "B29"
    B99 = "B99"
    C01 = "C01"
    C02 = "C02"
    C03 = "C03"
    C04 = "C04"
    C99 = "C99"
    D01 = "D01"
    D02 = "D02"
    D03 = "D03"
    D99 = "D99"
    E01 = "E01"
    E02 = "E02"
    E03 = "E03"
    E04 = "E04"
    E05 = "E05"
    E06 = "E06"
    E07 = "E07"
    E08 = "E08"
    E09 = "E09"
    E10 = "E10"
    E99 = "E99"
    F01 = "F01"
    F02 = "F02"
    F99 = "F99"
    Z01 = "Z01"
    Z02 = "Z02"
    Z98 = "Z98"
    Z99 = "Z99"


class List18(Enum):
    """
    Person / organization name type.

    :cvar VALUE_00: Unspecified
    :cvar VALUE_01: Pseudonym May be used to give a well-known
        pseudonym, where the primary name is a ‘real’ name
    :cvar VALUE_02: Authority-controlled name
    :cvar VALUE_03: Earlier name Use only within &lt;AlternativeName&gt;
    :cvar VALUE_04: ‘Real’ name May be used to identify a well-known
        real name, where the primary name is a pseudonym
    :cvar VALUE_05: Transliterated form of primary name Use only within
        &lt;AlternativeName&gt;, when the primary name type is
        unspecified
    :cvar VALUE_06: Later name Use only within &lt;AlternativeName&gt;
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"


class List19(Enum):
    """
    Unnamed person(s)

    :cvar VALUE_01: Unknown
    :cvar VALUE_02: Anonymous
    :cvar VALUE_03: et al And others: additional contributors not listed
    :cvar VALUE_04: Various authors When the product is a pack of books
        by different authors
    :cvar VALUE_05: Synthesized voice – male Use with Contributor role
        code E07 ‘read by’, for audio books for the blind
    :cvar VALUE_06: Synthesized voice – female Use with Contributor role
        code E07 ‘read by’, for audio books for the blind
    :cvar VALUE_07: Synthesized voice – unspecified Use with Contributor
        role code E07 ‘read by’, for audio books for the blind
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"


class List2(Enum):
    """
    Product composition.

    :cvar VALUE_00: Single-item retail product
    :cvar VALUE_10: Multiple-item retail product Multiple-item product
        retailed as a whole
    :cvar VALUE_11: Multiple-item collection, retailed as separate parts
        Used when an ONIX record is required for a collection-as-a-
        whole, even though it is not currently retailed as such
    :cvar VALUE_20: Trade-only product Product not for retail, and not
        carrying retail items, eg empty dumpbin, empty counterpack,
        promotional material
    :cvar VALUE_30: Multiple-item trade pack Carrying multiple copies
        for retailing as separate items, eg shrink-wrapped trade pack,
        filled dumpbin, filled counterpack
    :cvar VALUE_31: Multiple-item pack Carrying multiple copies,
        primarily for retailing as separate items. The pack may be split
        and retailed as separate items OR retailed as a single item. Use
        instead of Multiple item trade pack (code 30) only if the data
        provider specifically wishes to make explicit that the pack may
        optionally be retailed as a whole
    """
    VALUE_00 = "00"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_20 = "20"
    VALUE_30 = "30"
    VALUE_31 = "31"


class List20(Enum):
    """
    Event role.

    :cvar VALUE_01: Publication linked to conference For example an
        academic, professional or political conference
    :cvar VALUE_02: Complete proceedings of conference
    :cvar VALUE_03: Selected papers from conference
    :cvar VALUE_11: Publication linked to sporting event For example a
        competitive match, fixture series or championship
    :cvar VALUE_12: Programme or guide for sporting event
    :cvar VALUE_21: Publication linked to artistic event For example a
        theatrical or musical event or performance, a season of events
        or performances, or an exhibition of art
    :cvar VALUE_22: Programme or guide for artistic event
    :cvar VALUE_31: Publication linked to exposition For example a
        commercial exposition
    :cvar VALUE_32: Programme or guide for exposition
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_31 = "31"
    VALUE_32 = "32"


class List21(Enum):
    """
    Edition type code.

    :cvar ABR: Abridged edition Content has been shortened: use for
        abridged, shortened, concise, condensed
    :cvar ACT: Acting edition Version of a play or script intended for
        use of those directly involved in a production, usually
        including full stage directions in addition to the text of the
        script
    :cvar ADP: Adapted edition Content has been adapted to serve a
        different purpose or audience, or from one medium to another:
        use for dramatization, novelization etc. Use
        &lt;EditionStatement&gt; to describe the exact nature of the
        adaptation
    :cvar ALT: Alternate Do not use. This code is now DEPRECATED, but is
        retained in the list for reasons of backwards compatibility
    :cvar ANN: Annotated edition Content is augmented by the addition of
        notes
    :cvar BLL: Bilingual edition Both languages should be specified in
        the &lt;Language&gt; group. Use MLL for an edition in more than
        two languages
    :cvar BLP: Bilingual ‘facing page’ edition Use only where the two
        languages are presented in parallel on facing pages, or in
        parallel columns of text on a single page (otherwise use BLL).
        Both languages should be specified in the &lt;Language&gt; group
    :cvar BRL: Braille edition Braille edition
    :cvar CMB: Combined volume An edition in which two or more works
        also published separately are combined in a single volume; AKA
        ‘omnibus’ edition
    :cvar CRI: Critical edition Content includes critical commentary on
        the text
    :cvar CSP: Coursepack Content was compiled for a specified
        educational course
    :cvar DGO: Digital original A digital product that, at the time of
        publication, has or had no print counterpart and that is or was
        not expected to have a print counterpart for a reasonable time
        (recommended at least 30 days following publication)
    :cvar ENH: Enhanced edition Use for e-publications that have been
        enhanced with additional text, speech, other audio, video,
        interactive or other content
    :cvar ENL: Enlarged edition Content has been enlarged or expanded
        from that of a previous edition
    :cvar EXP: Expurgated edition ‘Offensive’ content has been removed
    :cvar FAC: Facsimile edition Exact reproduction of the content and
        format of a previous edition
    :cvar FST: Festschrift A collection of writings published in honor
        of a person, an institution or a society
    :cvar ILL: Illustrated edition Content includes extensive
        illustrations which are not part of other editions
    :cvar INT: International edition A product aimed specifically at
        markets other than the country of original publication, usually
        titled as an ‘International edition’ and with specification
        and/or content changes
    :cvar LTE: Large type / large print edition Large print edition,
        print sizes 14 to 19pt – see also ULP
    :cvar MCP: Microprint edition A printed edition in a type size too
        small to be read without a magnifying glass
    :cvar MDT: Media tie-in An edition published to coincide with the
        release of a film, TV program, or electronic game based on the
        same work. Use &lt;EditionStatement&gt; to describe the exact
        nature of the tie-in
    :cvar MLL: Multilingual edition All languages should be specified in
        the ‘Language’ group. Use BLL for a bilingual edition
    :cvar NED: New edition Where no other information is given, or no
        other coded type is applicable
    :cvar NUM: Edition with numbered copies A limited edition in which
        each copy is individually numbered. Use &lt;EditionStatement&gt;
        to give details of the number of copies printed
    :cvar PRB: Prebound edition In the US, a book that was previously
        bound, normally as a paperback, and has been rebound with a
        library-quality hardcover binding by a supplier other than the
        original publisher. See also the &lt;Publisher&gt; and
        &lt;RelatedProduct&gt; composites for other aspects of the
        treatment of prebound editions in ONIX
    :cvar REV: Revised edition Content has been revised from that of a
        previous edition
    :cvar SCH: School edition An edition intended specifically for use
        in schools
    :cvar SIG: Signed edition Individually autographed by the author(s)
    :cvar SMP: Simplified language edition An edition that uses
        simplified language (Finnish ‘Selkokirja’)
    :cvar SPE: Special edition Use for anniversary, collectors’, de
        luxe, gift, limited (but prefer codes NUM or UNN as
        appropriate), autographed (but prefer code SIG as appropriate)
        edition. Use &lt;EditionStatement&gt; to describe the exact
        nature of the special edition
    :cvar STU: Student edition Where a text is available in both student
        and teacher’s editions
    :cvar TCH: Teacher’s edition Where a text is available in both
        student and teacher’s editions; use also for instructor’s or
        leader’s editions, and for editions intended exclusively for
        educators where no specific student edition is available
    :cvar UBR: Unabridged edition Where a title has also been published
        in an abridged edition; also for audiobooks, regardless of
        whether an abridged audio version also exists
    :cvar ULP: Ultra large print edition For print sizes 20pt and above,
        and with typefaces designed for the visually impaired – see also
        LTE
    :cvar UNN: Edition with unnumbered copies A limited edition in which
        each copy is not individually numbered – but where the actual
        number of copies is strictly limited. Use
        &lt;EditionStatement&gt; to give details of the number of copies
        printed
    :cvar UXP: Unexpurgated edition Content previously considered
        ‘offensive’ has been restored
    :cvar VAR: Variorum edition Content includes notes by various
        commentators, and/or includes and compares several variant texts
        of the same work
    """
    ABR = "ABR"
    ACT = "ACT"
    ADP = "ADP"
    ALT = "ALT"
    ANN = "ANN"
    BLL = "BLL"
    BLP = "BLP"
    BRL = "BRL"
    CMB = "CMB"
    CRI = "CRI"
    CSP = "CSP"
    DGO = "DGO"
    ENH = "ENH"
    ENL = "ENL"
    EXP = "EXP"
    FAC = "FAC"
    FST = "FST"
    ILL = "ILL"
    INT = "INT"
    LTE = "LTE"
    MCP = "MCP"
    MDT = "MDT"
    MLL = "MLL"
    NED = "NED"
    NUM = "NUM"
    PRB = "PRB"
    REV = "REV"
    SCH = "SCH"
    SIG = "SIG"
    SMP = "SMP"
    SPE = "SPE"
    STU = "STU"
    TCH = "TCH"
    UBR = "UBR"
    ULP = "ULP"
    UNN = "UNN"
    UXP = "UXP"
    VAR = "VAR"


class List22(Enum):
    """
    Language role code.

    :cvar VALUE_01: Language of text
    :cvar VALUE_02: Original language of a translated text Where the
        text in the original language is NOT part of the current product
    :cvar VALUE_03: Language of abstracts Where different from language
        of text: used mainly for serials
    :cvar VALUE_04: Rights language Language to which specified rights
        apply
    :cvar VALUE_05: Rights-excluded language Language to which specified
        rights do not apply
    :cvar VALUE_06: Original language in a multilingual edition Where
        the text in the original language is part of a bilingual or
        multilingual product
    :cvar VALUE_07: Translated language in a multilingual edition Where
        the text in a translated language is part of a bilingual or
        multilingual product
    :cvar VALUE_08: Language of audio track For example, on a DVD. Use
        for the only available audio track, or for an alternate language
        audio track when the original language audio is also present
        (code 11), or is missing (code 10)
    :cvar VALUE_09: Language of subtitles For example, on a DVD
    :cvar VALUE_10: Language of original audio track Where the audio in
        the original language is NOT part of the current product
    :cvar VALUE_11: Original language audio track in a multilingual
        product Where the audio in the original language is part of a
        multilingual product with multiple audio tracks
    :cvar VALUE_12: Language of notes Use for the language of footnotes,
        endnotes, annotations or commentary, where it is different from
        the language of the main text
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"


class List23(Enum):
    """
    Extent type code.

    :cvar VALUE_00: Main content page count The highest-numbered page in
        a single numbered sequence of main content, usually the highest
        Arabic-numbered page in a book; or, for books without page
        numbers or (rarely) with multiple numbered sequences of main
        content, the total number of pages that carry the main content
        of the book. Note that this may include numbered but otherwise
        blank pages (eg pages inserted to ensure chapters start on a
        recto page) and may exclude unnumbered (but contentful) pages
        such as those in inserts/plate sections. It should exclude pages
        of back matter (eg any index) even when their numbering sequence
        continues from the main content. Either this or the Content Page
        count is the preferred page count for most books for the general
        reader. For books with substantial front and/or back matter,
        include also Front matter (03) and Back matter (04) page counts,
        or Total numbered pages (05). For books with inserts (plate
        sections), also include Total unnumbered insert page count
        whenever possible
    :cvar VALUE_02: Number of words Number of words of natural language
        text
    :cvar VALUE_03: Front matter page count The total number of numbered
        (usually Roman-numbered) pages that precede the main content of
        a book. This usually consists of various title and imprint
        pages, table of contents, an introduction, preface, foreword,
        etc
    :cvar VALUE_04: Back matter page count The total number of numbered
        (often Roman-numbered) pages that follow the main content of a
        book. This usually consists of an afterword, appendices,
        endnotes, index, etc. It excludes extracts or ‘teaser’ material
        from other works, and blank (or advertising) pages that are
        present only for convenience of printing and binding
    :cvar VALUE_05: Total numbered pages The sum of all Roman- and
        Arabic-numbered pages. Note that this may include numbered but
        otherwise blank pages (eg pages inserted to ensure chapters
        start on a recto page) and may exclude unnumbered (but
        contentful) pages such as those in inserts/plate sections. It is
        the sum of the main content (00), front matter (03) and back
        matter (04) page counts
    :cvar VALUE_06: Production page count The total number of pages in a
        book, including unnumbered pages, front matter, back matter,
        etc. This includes any extracts or ‘teaser’ material from other
        works, and blank pages at the back that carry no content and are
        present only for convenience of printing and binding
    :cvar VALUE_07: Absolute page count The total number of pages of the
        book counting the cover as page 1. This page count type should
        be used only for digital publications delivered with fixed
        pagination
    :cvar VALUE_08: Number of pages in print counterpart The total
        number of pages (equivalent to the Content page count) in the
        print counterpart of a digital product delivered without fixed
        pagination
    :cvar VALUE_09: Duration Total duration in time, expressed in the
        specified extent unit. This is the ‘running time’ equivalent of
        codes 05 or 11
    :cvar VALUE_10: Notional number of pages in digital product An
        estimate of the number of ‘pages’ in a digital product delivered
        without fixed pagination, and with no print counterpart, given
        as an indication of the size of the work. Equivalent to code 08,
        but for exclusively digital products
    :cvar VALUE_11: Content page count The sum of all Roman- and Arabic-
        numbered and contentful unnumbered pages. Sum of page counts
        with codes 00, 03, 04 and 12, and also the sum of 05 and 12
    :cvar VALUE_12: Total unnumbered insert page count The total number
        of unnumbered pages with content inserted within the main
        content of a book – for example inserts/plate sections that are
        not numbered
    :cvar VALUE_13: Duration of introductory matter Duration in time,
        expressed in the specified extent units, of introductory matter.
        This is the ‘running time’ equivalent of code 03, and comprises
        any significant amount of running time represented by
        announcements, titles, introduction or other material prefacing
        the main content
    :cvar VALUE_14: Duration of main content Duration in time, expressed
        in the specified extent units, of the main content. This is the
        ‘running time’ equivalent of code 00, and excludes time
        represented by announcements, titles, introduction or other
        prefatory material or ‘back matter’
    :cvar VALUE_15: Duration of back matter Duration in time, expressed
        in the specified extent units, of any content that follows the
        main content of a book. This usually consists of an afterword,
        appendices, endnotes etc. It excludes extracts or ‘teaser’
        material from other works. This is the ‘running time’ equivalent
        of code 04
    :cvar VALUE_16: Production duration Duration in time, expressed in
        the specified extent units, of the complete content of a book.
        This is the ‘running time’ equivalent of code 06, and includes
        time represented by announcements, titles, introductory and
        other prefatory material, plus ‘back matter’ such as any
        afterword, appendices, and any extracts or ‘teaser’ material
        from other works
    :cvar VALUE_22: Filesize The size of a digital file, expressed in
        the specified extent unit
    """
    VALUE_00 = "00"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_22 = "22"


class List24(Enum):
    """
    Extent unit code.

    :cvar VALUE_02: Words Words of natural language text
    :cvar VALUE_03: Pages
    :cvar VALUE_04: Hours (integer and decimals)
    :cvar VALUE_05: Minutes (integer and decimals)
    :cvar VALUE_06: Seconds (integer only)
    :cvar VALUE_11: Tracks Of an audiobook on CD (or a similarly divided
        selection of audio files). Conventionally, each track is 3–6
        minutes of running time, and track counts are misleading and
        inappropriate if the average track duration is significantly
        more or less than this. Note that track breaks are not
        necessarily aligned with structural breaks in the text (eg
        chapter breaks)
    :cvar VALUE_14: Hours HHH Fill with leading zeroes if any elements
        are missing
    :cvar VALUE_15: Hours and minutes HHHMM Fill with leading zeroes if
        any elements are missing
    :cvar VALUE_16: Hours minutes seconds HHHMMSS Fill with leading
        zeroes if any elements are missing
    :cvar VALUE_17: Bytes
    :cvar VALUE_18: Kbytes
    :cvar VALUE_19: Mbytes
    """
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_11 = "11"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"


class List25(Enum):
    """
    Illustration and other content type code.

    :cvar VALUE_00: Unspecified, see description See description in the
        &lt;IllustrationTypeDescription&gt; element
    :cvar VALUE_01: Illustrations, black and white
    :cvar VALUE_02: Illustrations, color
    :cvar VALUE_03: Halftones, black and white Including black and white
        photographs
    :cvar VALUE_04: Halftones, color Including color photographs
    :cvar VALUE_05: Line drawings, black and white
    :cvar VALUE_06: Line drawings, color
    :cvar VALUE_07: Tables, black and white
    :cvar VALUE_08: Tables, color
    :cvar VALUE_09: Illustrations, unspecified
    :cvar VALUE_10: Halftones, unspecified Including photographs
    :cvar VALUE_11: Tables, unspecified
    :cvar VALUE_12: Line drawings, unspecified
    :cvar VALUE_13: Halftones, duotone
    :cvar VALUE_14: Maps
    :cvar VALUE_15: Frontispiece
    :cvar VALUE_16: Diagrams
    :cvar VALUE_17: Figures
    :cvar VALUE_18: Charts
    :cvar VALUE_19: Recorded music items Recorded music extracts or
        examples, or complete recorded work(s), accompanying textual or
        other content
    :cvar VALUE_20: Printed music items Printed music extracts or
        examples, or complete music score(s), accompanying textual or
        other content
    :cvar VALUE_21: Graphs To be used in the mathematical sense of a
        diagram that represents numerical values plotted against an
        origin and axes, cf codes 16 and 18
    :cvar VALUE_22: Plates, unspecified ‘Plates’ means illustrations
        that are on separate pages bound into the body of a book
    :cvar VALUE_23: Plates, black and white ‘Plates’ means illustrations
        that are on separate pages bound into the body of a book
    :cvar VALUE_24: Plates, color ‘Plates’ means illustrations that are
        on separate pages bound into the body of a book
    :cvar VALUE_25: Index
    :cvar VALUE_26: Bibliography
    :cvar VALUE_27: Inset maps Larger-scale inset maps of places or
        features of interest included in a map product
    :cvar VALUE_28: GPS grids GPS grids included in a map product
    :cvar VALUE_29: Glossary
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"


class List26(Enum):
    """
    Main subject scheme identifier code.

    :cvar VALUE_01: Dewey Dewey Decimal Classification
    :cvar VALUE_02: Abridged Dewey
    :cvar VALUE_03: LC classification US Library of Congress
        classification
    :cvar VALUE_04: LC subject heading US Library of Congress subject
        heading
    :cvar VALUE_05: NLM classification US National Library of Medicine
        medical classification
    :cvar VALUE_06: MeSH heading US National Library of Medicine Medical
        subject heading
    :cvar VALUE_07: NAL subject heading US National Agricultural Library
        subject heading
    :cvar VALUE_08: AAT Getty Art and Architecture Thesaurus heading
    :cvar VALUE_09: UDC Universal Decimal Classification
    :cvar VALUE_10: BISAC Subject Heading BISAC Subject Headings are
        used in the North American market to categorize books based on
        topical content. They serve as a guideline for shelving books in
        physical stores and browsing books in online stores. See
        https://www.bisg.org/complete-bisac-subject-
        headings-2013-edition
    :cvar VALUE_11: BISAC region code A geographical qualifier used with
        a BISAC subject category
    :cvar VALUE_12: BIC subject category For all BIC subject codes and
        qualifiers, see http://www.bic.org.uk/7/BIC-Standard-Subject-
        Categories/
    :cvar VALUE_13: BIC geographical qualifier
    :cvar VALUE_14: BIC language qualifier (language as subject)
    :cvar VALUE_15: BIC time period qualifier
    :cvar VALUE_16: BIC educational purpose qualifier
    :cvar VALUE_17: BIC reading level and special interest qualifier
    :cvar VALUE_18: DDC-Sachgruppen der Deutschen Nationalbibliografie
        Used for German National Bibliography since 2004 (100 subjects).
        Is different from value 30. See
        http://www.d-nb.de/service/pdf/ddc_wv_aktuell.pdf (in German) or
        http://www.d-nb.de/eng/service/pdf/ddc_wv_aktuell_eng.pdf
        (English)
    :cvar VALUE_19: LC fiction genre heading
    :cvar VALUE_20: Keywords For indexing and search purposes, not
        normally intended for display. Where multiple keywords or
        keyword phrases are sent, this should be in a single instance of
        the &lt;SubjectHeadingText&gt; element, and it is recommended
        that they should be separated by semi-colons (this is consistent
        with Library of Congress preferred practice)
    :cvar VALUE_21: BIC children’s book marketing category See
        http://www.bic.org.uk/8/Children’s-Books-Marketing-
        Classifications/
    :cvar VALUE_22: BISAC Merchandising Theme BISAC Merchandising Themes
        are used in addition to BISAC Subject Headings to denote an
        audience to which a work may be of particular appeal, a time of
        year or event for which a work may be especially appropriate, or
        to further describe fictional works that have been subject-coded
        by genre
    :cvar VALUE_23: Publisher’s own category code
    :cvar VALUE_24: Proprietary subject scheme As specified in
        &lt;SubjectSchemeName&gt;
    :cvar VALUE_25: Tabla de materias ISBN Latin America
    :cvar VALUE_26: Warengruppen-Systematik des deutschen Buchhandels
        See http://info.vlb.de/files/wgsneuversion2_0.pdf (in German)
    :cvar VALUE_27: SWD Schlagwortnormdatei – Subject Headings Authority
        File in the German-speaking countries. See
        http://www.d-nb.de/standardisierung/normdateien/swd.htm (in
        German) and
        http://www.d-nb.de/eng/standardisierung/normdateien/swd.htm
        (English). DEPRECATED in favour of the GND
    :cvar VALUE_28: Thèmes Electre Subject classification used by
        Electre (France)
    :cvar VALUE_29: CLIL France. A four-digit number, see
        http://www.clil.org/information/documentation.html (in French).
        The first digit identifies the version of the scheme
    :cvar VALUE_30: DNB-Sachgruppen Deutsche Bibliothek subject groups.
        Used for German National Bibliography until 2003 (65 subjects).
        Is different from value 18. See
        http://www.d-nb.de/service/pdf/ddc_wv_alt_neu.pdf
    :cvar VALUE_31: NUGI Nederlandse Uniforme Genre-Indeling (former
        Dutch book trade classification)
    :cvar VALUE_32: NUR Nederlandstalige Uniforme Rubrieksindeling
        (Dutch book trade classification, from 2002),see
        http://www.boek.nl/nur (in Dutch)
    :cvar VALUE_33: ECPA Christian Book Category ECPA Christian Product
        Category Book Codes, consisting of up to three x 3-letter
        blocks, for Super Category, Primary Category and Sub-Category.
        See http://www.ecpa.org/ECPA/cbacategories.xls
    :cvar VALUE_34: SISO Schema Indeling Systematische Catalogus
        Openbare Bibliotheken (Dutch library classification)
    :cvar VALUE_35: Korean Decimal Classification (KDC) A modified Dewey
        Decimal Classification used in the Republic of Korea
    :cvar VALUE_36: DDC Deutsch 22 German Translation of Dewey Decimal
        Classification 22. Also known as DDC 22 ger. See http://www.ddc-
        deutsch.de/produkte/uebersichten/
    :cvar VALUE_37: Bokgrupper Norwegian book trade product categories
        (Bokgrupper) administered by the Norwegian Publishers
        Association (http://www.forleggerforeningen.no/)
    :cvar VALUE_38: Varegrupper Norwegian bookselling subject categories
        (Bokhandelens varegrupper) administered by the Norwegian
        Booksellers Association (http://bokhandlerforeningen.no/)
    :cvar VALUE_39: Læreplaner Norwegian school curriculum version.
        Deprecated
    :cvar VALUE_40: Nippon Decimal Classification Japanese subject
        classification scheme
    :cvar VALUE_41: BSQ BookSelling Qualifier: Russian book trade
        classification
    :cvar VALUE_42: ANELE Materias Spain: subject coding scheme of the
        Asociación Nacional de Editores de Libros y Material de
        Enseñanza
    :cvar VALUE_43: Utdanningsprogram Codes for Norwegian
        ‘utdanningsprogram’ used in secondary education. See:
        http://www.udir.no/. (Formerly labelled ‘Skolefag’)
    :cvar VALUE_44: Programområde Codes for Norwegian ‘programområde’
        used in secondary education. See http://www.udir.no/. (Formerly
        labelled ‘Videregående’ or ‘Programfag’)
    :cvar VALUE_45: Undervisningsmateriell Norwegian list of categories
        for books and other material used in education
    :cvar VALUE_46: Norsk DDK Norwegian version of Dewey Decimal
        Classification
    :cvar VALUE_47: Varugrupper Swedish bookselling subject categories
    :cvar VALUE_48: SAB Swedish classification scheme
    :cvar VALUE_49: Läromedelstyp Swedish bookselling educational
        subject type
    :cvar VALUE_50: Förhandsbeskrivning Swedish publishers preliminary
        subject classification
    :cvar VALUE_51: Spanish ISBN UDC subset Controlled subset of UDC
        codes used by the Spanish ISBN Agency
    :cvar VALUE_52: ECI subject categories Subject categories defined by
        El Corte Inglés and used widely in the Spanish book trade
    :cvar VALUE_53: Soggetto CCE Classificazione commerciale editoriale
        (Italian book trade subject category based on BIC). CCE
        documentation available at http://www.ie-online.it/CCE2_2.0.pdf
    :cvar VALUE_54: Qualificatore geografico CCE
    :cvar VALUE_55: Qualificatore di lingua CCE
    :cvar VALUE_56: Qualificatore di periodo storico CCE
    :cvar VALUE_57: Qualificatore di livello scolastico CCE
    :cvar VALUE_58: Qualificatore di età di lettura CCE
    :cvar VALUE_59: VdS Bildungsmedien Fächer Subject code list of the
        German association of educational media publishers
    :cvar VALUE_60: Fagkoder Norwegian primary and secondary school
        subject categories (fagkoder), see http://www.udir.no/
    :cvar VALUE_61: JEL classification Journal of Economic Literature
        classification scheme
    :cvar VALUE_62: CSH National Library of Canada subject heading
        (English)
    :cvar VALUE_63: RVM Répertoire de vedettes-matière (Bibliothèque de
        l’Université Laval) (French)
    :cvar VALUE_64: YSA Yleinen suomalainen asiasanasto: Finnish General
        Thesaurus. See http://onki.fi/fi/browser/ (in Finnish)
    :cvar VALUE_65: Allärs Allmän tesaurus på svenska: Swedish
        translation of the Finnish General Thesaurus. See
        http://onki.fi/fi/browser/ (in Finnish)
    :cvar VALUE_66: YKL Yleisten kirjastojen luokitusjärjestelmä:
        Finnish Public Libraries Classification System. See
        http://ykl.kirjastot.fi/ (in Finnish)
    :cvar VALUE_67: MUSA Musiikin asiasanasto: Finnish Music Thesaurus.
        See http://onki.fi/fi/browser/ (in Finnish)
    :cvar VALUE_68: CILLA Specialtesaurus för musik: Swedish translation
        of the Finnish Music Thesaurus. See http://onki.fi/fi/browser/
        (in Finnish)
    :cvar VALUE_69: Kaunokki Fiktiivisen aineiston asiasanasto: Finnish
        thesaurus for fiction. See http://kaunokki.kirjastot.fi/ (in
        Finnish)
    :cvar VALUE_70: Bella Specialtesaurus för fiktivt material: Swedish
        translation of the Finnish thesaurus for fiction. See
        http://kaunokki.kirjastot.fi/sv-FI/ (in Finnish)
    :cvar VALUE_71: YSO Yleinen suomalainen ontologia: Finnish General
        Upper Ontology. See http://onki.fi/fi/browser/ (In Finnish)
    :cvar VALUE_72: Paikkatieto ontologia Finnish Place Ontology. See
        http://onki.fi/fi/browser/ (in Finnish)
    :cvar VALUE_73: Suomalainen kirja-alan luokitus Finnish book trade
        categorisation
    :cvar VALUE_74: Sears Sears List of Subject Headings
    :cvar VALUE_75: BIC E4L BIC E4Libraries Category Headings, see
        http://www.bic.org.uk/51/E4libraries-Subject-Category-Headings/
    :cvar VALUE_76: CSR Code Sujet Rayon: subject categories used by
        bookstores in France
    :cvar VALUE_77: Suomalainen oppiaineluokitus Finnish school subject
        categories
    :cvar VALUE_78: Japanese book trade C-Code See http://www.asahi-
        net.or.jp/~ax2s-kmtn/ref/ccode.html (in Japanese)
    :cvar VALUE_79: Japanese book trade Genre Code
    :cvar VALUE_80: Fiktiivisen aineiston lisäluokitus Finnish fiction
        genre classification. See http://ykl.kirjastot.fi/fi-
        FI/lisaluokat/ (in Finnish)
    :cvar VALUE_85: Postal code Location defined by postal code. Format
        is two-letter country code (from List 91), space, postal code.
        Note some postal codes themselves contain spaces, eg ‘GB N7 9DP’
        or ‘US 10125’
    :cvar VALUE_86: GeoNames ID ID number for geographical place, as
        defined at http://www.geonames.org (eg 2825297 is Stuttgart,
        Germany, see http://www.geonames.org/2825297)
    :cvar VALUE_87: NewBooks Subject Classification Used for
        classification of academic and specialist publication in German-
        speaking countries. See http://www.newbooks-
        services.com/de/top/unternehmensportrait/klassifikation-und-
        mapping.html (German) and http://www.newbooks-
        services.com/en/top/about-newbooks/classification-mapping.html
        (English)
    :cvar VALUE_91: GND Gemeinsame Normdatei – Joint Authority File in
        the German-speaking countries. See http://www.dnb.de/EN/gnd
        (English). Combines the PND, SWD and GKD into a single authority
        file, and should be used in preference to the older codes
    :cvar VALUE_92: BIC UKSLC UK Standard Library Categories, the
        successor to BIC’s E4L classification scheme
    :cvar VALUE_93: Thema subject category
    :cvar VALUE_94: Thema geographical qualifier
    :cvar VALUE_95: Thema language qualifier
    :cvar VALUE_96: Thema time period qualifier
    :cvar VALUE_97: Thema educational purpose qualifier
    :cvar VALUE_98: Thema interest age / special interest qualifier
    :cvar VALUE_99: Thema style qualifier
    :cvar A2: Ämnesord Swedish subject categories maintained by
        Bokrondellen
    :cvar A3: Statystyka Książek Papierowych, Mówionych I
        Elektronicznych Polish Statistical Book and E-book
        Classification
    :cvar A4: CCSS Common Core State Standards curriculum alignment, for
        links to US educational standards. &lt;SubjectCode&gt; uses the
        full dot notation. See http://www.corestandards.org/developers-
        and-publishers
    :cvar A5: Rameau French library subject headings
    :cvar A6: Nomenclature discipline scolaire French educational
        subject classification scolomfr-voc-015, used for example on
        WizWiz.fr. See http://www.lom-
        fr.fr/scolomfr/vocabulaires/consultation-des-vocabulaires.html
    :cvar A7: ISIC International Standard Industry Classification, a
        classification of economic activities. Use for books that are
        about a particular industry or economic activity.
        &lt;SubjectCode&gt; should be a single letter denoting an ISIC
        section OR a 2-, 3- or 4-digit number denoting an ISIC division,
        group or class. See
        http://unstats.un.org/unsd/cr/registry/isic-4.asp
    :cvar A8: LC Children’s Subject Headings Library of Congress
        Children’s Subject Headings: LCSHAC supplementary headings for
        Children’s books
    :cvar A9: Ny Läromedel Swedish bookselling educational subject
    :cvar B0: EuroVoc EuroVoc multilingual thesaurus.
        &lt;SubjectCode&gt; should be a EuroVoc concept dc:identifier
        (for example, 2777, ‘Refrigerated products’). See
        http://eurovoc.europa.eu
    :cvar B1: BISG Educational Taxonomy Controlled vocabulary for
        educational objectives. See https://www.bisg.org/educational-
        taxonomy
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_36 = "36"
    VALUE_37 = "37"
    VALUE_38 = "38"
    VALUE_39 = "39"
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_45 = "45"
    VALUE_46 = "46"
    VALUE_47 = "47"
    VALUE_48 = "48"
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_54 = "54"
    VALUE_55 = "55"
    VALUE_56 = "56"
    VALUE_57 = "57"
    VALUE_58 = "58"
    VALUE_59 = "59"
    VALUE_60 = "60"
    VALUE_61 = "61"
    VALUE_62 = "62"
    VALUE_63 = "63"
    VALUE_64 = "64"
    VALUE_65 = "65"
    VALUE_66 = "66"
    VALUE_67 = "67"
    VALUE_68 = "68"
    VALUE_69 = "69"
    VALUE_70 = "70"
    VALUE_71 = "71"
    VALUE_72 = "72"
    VALUE_73 = "73"
    VALUE_74 = "74"
    VALUE_75 = "75"
    VALUE_76 = "76"
    VALUE_77 = "77"
    VALUE_78 = "78"
    VALUE_79 = "79"
    VALUE_80 = "80"
    VALUE_85 = "85"
    VALUE_86 = "86"
    VALUE_87 = "87"
    VALUE_91 = "91"
    VALUE_92 = "92"
    VALUE_93 = "93"
    VALUE_94 = "94"
    VALUE_95 = "95"
    VALUE_96 = "96"
    VALUE_97 = "97"
    VALUE_98 = "98"
    VALUE_99 = "99"
    A2 = "A2"
    A3 = "A3"
    A4 = "A4"
    A5 = "A5"
    A6 = "A6"
    A7 = "A7"
    A8 = "A8"
    A9 = "A9"
    B0 = "B0"
    B1 = "B1"


class List27(Enum):
    """
    Subject scheme identifier code.

    :cvar VALUE_01: Dewey Dewey Decimal Classification
    :cvar VALUE_02: Abridged Dewey
    :cvar VALUE_03: LC classification US Library of Congress
        classification
    :cvar VALUE_04: LC subject heading US Library of Congress subject
        heading
    :cvar VALUE_05: NLM classification US National Library of Medicine
        medical classification
    :cvar VALUE_06: MeSH heading US National Library of Medicine Medical
        subject heading
    :cvar VALUE_07: NAL subject heading US National Agricultural Library
        subject heading
    :cvar VALUE_08: AAT Getty Art and Architecture Thesaurus heading
    :cvar VALUE_09: UDC Universal Decimal Classification
    :cvar VALUE_10: BISAC Subject Heading BISAC Subject Headings are
        used in the North American market to categorize books based on
        topical content. They serve as a guideline for shelving books in
        physical stores and browsing books in online stores. See
        https://www.bisg.org/complete-bisac-subject-
        headings-2014-edition
    :cvar VALUE_11: BISAC region code A geographical qualifier used with
        a BISAC subject category
    :cvar VALUE_12: BIC subject category For all BIC subject codes and
        qualifiers, see http://www.bic.org.uk/7/BIC-Standard-Subject-
        Categories/
    :cvar VALUE_13: BIC geographical qualifier
    :cvar VALUE_14: BIC language qualifier (language as subject)
    :cvar VALUE_15: BIC time period qualifier
    :cvar VALUE_16: BIC educational purpose qualifier
    :cvar VALUE_17: BIC reading level and special interest qualifier
    :cvar VALUE_18: DDC-Sachgruppen der Deutschen Nationalbibliografie
        Used for German National Bibliography since 2004 (100 subjects).
        Is different from value 30. See
        http://www.d-nb.de/service/pdf/ddc_wv_aktuell.pdf (in German) or
        http://www.d-nb.de/eng/service/pdf/ddc_wv_aktuell_eng.pdf
        (English)
    :cvar VALUE_19: LC fiction genre heading
    :cvar VALUE_20: Keywords For indexing and search purposes, not
        normally intended for display. Where multiple keywords or
        keyword phrases are sent, this should be in a single instance of
        the &lt;SubjectHeadingText&gt; element, and it is recommended
        that they should be separated by semi-colons (this is consistent
        with Library of Congress preferred practice)
    :cvar VALUE_21: BIC children’s book marketing category See
        http://www.bic.org.uk/8/Children’s-Books-Marketing-
        Classifications/
    :cvar VALUE_22: BISAC Merchandising Theme BISAC Merchandising Themes
        are used in addition to BISAC Subject Headings to denote an
        audience to which a work may be of particular appeal, a time of
        year or event for which a work may be especially appropriate, or
        to further describe fictional works that have been subject-coded
        by genre
    :cvar VALUE_23: Publisher’s own category code
    :cvar VALUE_24: Proprietary subject scheme As specified in
        &lt;SubjectSchemeName&gt;
    :cvar VALUE_25: Tabla de materias ISBN Latin America
    :cvar VALUE_26: Warengruppen-Systematik des deutschen Buchhandels
        See http://info.vlb.de/files/wgsneuversion2_0.pdf (in German)
    :cvar VALUE_27: SWD Schlagwortnormdatei – Subject Headings Authority
        File in the German-speaking countries. See
        http://www.d-nb.de/standardisierung/normdateien/swd.htm (in
        German) and
        http://www.d-nb.de/eng/standardisierung/normdateien/swd.htm
        (English). DEPRECATED in favour of the GND
    :cvar VALUE_28: Thèmes Electre Subject classification used by
        Electre (France)
    :cvar VALUE_29: CLIL France. A four-digit number, see
        http://www.clil.org/information/documentation.html (in French).
        The first digit identifies the version of the scheme
    :cvar VALUE_30: DNB-Sachgruppen Deutsche Bibliothek subject groups.
        Used for German National Bibliography until 2003 (65 subjects).
        Is different from value 18. See
        http://www.d-nb.de/service/pdf/ddc_wv_alt_neu.pdf (in German)
    :cvar VALUE_31: NUGI Nederlandse Uniforme Genre-Indeling (former
        Dutch book trade classification)
    :cvar VALUE_32: NUR Nederlandstalige Uniforme Rubrieksindeling
        (Dutch book trade classification, from 2002, see
        http://www.boek.nl/nur (in Dutch)
    :cvar VALUE_33: ECPA Christian Book Category ECPA Christian Product
        Category Book Codes, consisting of up to three x 3-letter
        blocks, for Super Category, Primary Category and Sub-Category.
        See http://www.ecpa.org/ECPA/cbacategories.xls
    :cvar VALUE_34: SISO Schema Indeling Systematische Catalogus
        Openbare Bibliotheken (Dutch library classification)
    :cvar VALUE_35: Korean Decimal Classification (KDC) A modified Dewey
        Decimal Classification used in the Republic of Korea
    :cvar VALUE_36: DDC Deutsch 22 German Translation of Dewey Decimal
        Classification 22. Also known as DDC 22 ger. See http://www.ddc-
        deutsch.de/produkte/uebersichten/
    :cvar VALUE_37: Bokgrupper Norwegian book trade product categories
        (Bokgrupper) administered by the Norwegian Publishers
        Association (http://www.forleggerforeningen.no/)
    :cvar VALUE_38: Varegrupper Norwegian bookselling subject categories
        (Bokhandelens varegrupper) administered by the Norwegian
        Booksellers Association (http://bokhandlerforeningen.no/)
    :cvar VALUE_39: Læreplaner Norwegian school curriculum version.
        Deprecated
    :cvar VALUE_40: Nippon Decimal Classification Japanese subject
        classification scheme
    :cvar VALUE_41: BSQ BookSelling Qualifier: Russian book trade
        classification
    :cvar VALUE_42: ANELE Materias Spain: subject coding scheme of the
        Asociación Nacional de Editores de Libros y Material de
        Enseñanza
    :cvar VALUE_43: Utdanningsprogram Codes for Norwegian
        ‘utdanningsprogram’ used in secondary education. See:
        http://www.udir.no/. (Formerly labelled ‘Skolefag’)
    :cvar VALUE_44: Programområde Codes for Norwegian ‘programområde’
        used in secondary education. See http://www.udir.no/. (Formerly
        labelled ‘Videregående’ or ‘Programfag’)
    :cvar VALUE_45: Undervisningsmateriell Norwegian list of categories
        for books and other material used in education
    :cvar VALUE_46: Norsk DDK Norwegian version of Dewey Decimal
        Classification
    :cvar VALUE_47: Varugrupper Swedish bookselling subject categories
    :cvar VALUE_48: SAB Swedish classification scheme
    :cvar VALUE_49: Läromedelstyp Swedish bookselling educational
        subject type
    :cvar VALUE_50: Förhandsbeskrivning Swedish publishers preliminary
        subject classification
    :cvar VALUE_51: Spanish ISBN UDC subset Controlled subset of UDC
        codes used by the Spanish ISBN Agency
    :cvar VALUE_52: ECI subject categories Subject categories defined by
        El Corte Inglés and used widely in the Spanish book trade
    :cvar VALUE_53: Soggetto CCE Classificazione commerciale editoriale
        (Italian book trade subject category based on BIC). CCE
        documentation available at http://www.ie-online.it/CCE2_2.0.pdf
    :cvar VALUE_54: Qualificatore geografico CCE CCE Geographical
        qualifier
    :cvar VALUE_55: Qualificatore di lingua CCE CCE Language qualifier
    :cvar VALUE_56: Qualificatore di periodo storico CCE CCE Time Period
        qualifier
    :cvar VALUE_57: Qualificatore di livello scolastico CCE CCE
        Educational Purpose qualifier
    :cvar VALUE_58: Qualificatore di età di lettura CCE CCE Reading
        Level Qualifier
    :cvar VALUE_59: VdS Bildungsmedien Fächer Subject code list of the
        German association of educational media publishers. See
        http://www.bildungsmedien.de/service/onixlisten/unterrichtsfach_onix_codelist27_value59_0408.pdf
    :cvar VALUE_60: Fagkoder Norwegian primary and secondary school
        subject categories (fagkoder), see http://www.udir.no/
    :cvar VALUE_61: JEL classification Journal of Economic Literature
        classification scheme
    :cvar VALUE_62: CSH National Library of Canada subject heading
        (English)
    :cvar VALUE_63: RVM Répertoire de vedettes-matière Bibliothèque de
        l’Université Laval) (French)
    :cvar VALUE_64: YSA Yleinen suomalainen asiasanasto: Finnish General
        Thesaurus. See http://onki.fi/fi/browser/ (in Finnish)
    :cvar VALUE_65: Allärs Allmän tesaurus på svenska: Swedish
        translation of the Finnish General Thesaurus. See
        http://onki.fi/fi/browser/ (in Finnish)
    :cvar VALUE_66: YKL Yleisten kirjastojen luokitusjärjestelmä:
        Finnish Public Libraries Classification System. See
        http://ykl.kirjastot.fi/ (in Finnish)
    :cvar VALUE_67: MUSA Musiikin asiasanasto: Finnish Music Thesaurus.
        See http://onki.fi/fi/browser/ (in Finnish)
    :cvar VALUE_68: CILLA Specialtesaurus för musik: Swedish translation
        of the Finnish Music Thesaurus. See http://onki.fi/fi/browser/
        (in Finnish)
    :cvar VALUE_69: Kaunokki Fiktiivisen aineiston asiasanasto: Finnish
        thesaurus for fiction. See http://kaunokki.kirjastot.fi/ (in
        Finnish)
    :cvar VALUE_70: Bella Specialtesaurus för fiktivt material: Swedish
        translation of the Finnish thesaurus for fiction. See
        http://kaunokki.kirjastot.fi/sv-FI/ (in Finnish)
    :cvar VALUE_71: YSO Yleinen suomalainen ontologia: Finnish General
        Upper Ontology. See http://onki.fi/fi/browser/ (In Finnish)
    :cvar VALUE_72: Paikkatieto ontologia Finnish Place Ontology. See
        http://onki.fi/fi/browser/ (in Finnish)
    :cvar VALUE_73: Suomalainen kirja-alan luokitus Finnish book trade
        categorisation
    :cvar VALUE_74: Sears Sears List of Subject Headings
    :cvar VALUE_75: BIC E4L BIC E4Libraries Category Headings, see
        http://www.bic.org.uk/51/E4libraries-Subject-Category-Headings/
    :cvar VALUE_76: CSR Code Sujet Rayon: subject categories used by
        bookstores in France
    :cvar VALUE_77: Suomalainen oppiaineluokitus Finnish school subject
        categories
    :cvar VALUE_78: Japanese book trade C-Code See http://www.asahi-
        net.or.jp/~ax2s-kmtn/ref/ccode.html (in Japanese)
    :cvar VALUE_79: Japanese book trade Genre Code
    :cvar VALUE_80: Fiktiivisen aineiston lisäluokitus Finnish fiction
        genre classification. See http://ykl.kirjastot.fi/fi-
        FI/lisaluokat/ (in Finnish)
    :cvar VALUE_81: Arabic Subject heading scheme
    :cvar VALUE_82: Arabized BIC subject category Arabized version of
        BIC subject category scheme developed by ElKotob.com
    :cvar VALUE_83: Arabized LC subject headings Arabized version of
        Library of Congress scheme
    :cvar VALUE_84: Bibliotheca Alexandrina Subject Headings
        Classification scheme used by Library of Alexandria
    :cvar VALUE_85: Postal code Location defined by postal code. Format
        is two-letter country code (from List 91), space, postal code.
        Note some postal codes themselves contain spaces, eg ‘GB N7 9DP’
        or ‘US 10125’
    :cvar VALUE_86: GeoNames ID ID number for geographical place, as
        defined at http://www.geonames.org (eg 2825297 is Stuttgart,
        Germany, see http://www.geonames.org/2825297)
    :cvar VALUE_87: NewBooks Subject Classification Used for
        classification of academic and specialist publication in German-
        speaking countries. See http://www.newbooks-
        services.com/de/top/unternehmensportrait/klassifikation-und-
        mapping.html (German) and http://www.newbooks-
        services.com/en/top/about-newbooks/classification-mapping.html
        (English)
    :cvar VALUE_88: Chinese Library Classification Subject
        classification maintained by the Editorial Board of Chinese
        Library Classification. See http://cct.nlc.gov.cn for access to
        details of the scheme
    :cvar VALUE_89: NTCPDSAC Classification Subject classification for
        Books, Audiovisual products and E-publications formulated by
        China National Technical Committee 505
    :cvar VALUE_90: Season and Event Indicator German code scheme
        indicating association with seasons, holidays, events (eg
        Autumn, Back to School, Easter)
    :cvar VALUE_91: GND Gemeinsame Normdatei – Joint Authority File in
        the German-speaking countries. See http://www.dnb.de/EN/gnd
        (English). Combines the PND, SWD and GKD into a single authority
        file, and should be used in preference to the older codes
    :cvar VALUE_92: BIC UKSLC UK Standard Library Categories, the
        successor to BIC’s E4L classification scheme
    :cvar VALUE_93: Thema subject category
    :cvar VALUE_94: Thema geographical qualifier
    :cvar VALUE_95: Thema language qualifier
    :cvar VALUE_96: Thema time period qualifier
    :cvar VALUE_97: Thema educational purpose qualifier
    :cvar VALUE_98: Thema interest age / special interest qualifier
    :cvar VALUE_99: Thema style qualifier
    :cvar A2: Ämnesord Swedish subject categories maintained by
        Bokrondellen
    :cvar A3: Statystyka Książek Papierowych, Mówionych I
        Elektronicznych Polish Statistical Book and E-book
        Classification
    :cvar A4: CCSS Common Core State Standards curriculum alignment, for
        links to US educational standards. &lt;SubjectCode&gt; uses the
        full dot notation. See http://www.corestandards.org/developers-
        and-publishers
    :cvar A5: Rameau French library subject headings
    :cvar A6: Nomenclature discipline scolaire French educational
        subject classification scolomfr-voc-015, used for example on
        WizWiz.fr. See http://www.lom-
        fr.fr/scolomfr/vocabulaires/consultation-des-vocabulaires.html
    :cvar A7: ISIC International Standard Industry Classification, a
        classification of economic activities. Use for books that are
        about a particular industry or economic activity.
        &lt;SubjectCode&gt; should be a single letter denoting an ISIC
        section OR a 2-, 3- or 4-digit number denoting an ISIC division,
        group or class. See
        http://unstats.un.org/unsd/cr/registry/isic-4.asp
    :cvar A8: LC Children’s Subject Headings Library of Congress
        Children’s Subject Headings: LCSHAC supplementary headings for
        Children’s books
    :cvar A9: Ny Läromedel Swedish bookselling educational subject
    :cvar B0: EuroVoc EuroVoc multilingual thesaurus.
        &lt;SubjectCode&gt; should be a EuroVoc concept dc:identifier
        (for example, 2777, ‘refrigerated products’). See
        http://eurovoc.europa.eu
    :cvar B1: BISG Educational Taxonomy Controlled vocabulary for
        educational objectives. See https://www.bisg.org/educational-
        taxonomy
    :cvar B2: Keywords (not for display) For indexing and search
        purposes, MUST not be displayed. Where multiple keywords or
        keyword phrases are sent, this should be in a single instance of
        the &lt;SubjectHeadingText&gt; element, and it is recommended
        that they should be separated by semi-colons. Use of code B2
        should be very rare: use B2 in preference to code 20 only where
        it is important to show the keyword list is specifically NOT for
        display to purchasers (eg some keywords for a medical textbook
        may appear offensive if displayed out of context)
    :cvar B3: Nomenclature Diplôme French higher and vocational
        educational subject classification scolomfr-voc-29 subject
        category for degree and diploma study. See http://www.lom-
        fr.fr/scolomfr/vocabulaires/consultation-des-vocabulaires.html
    :cvar B4: Key character names For fiction only, one or more key
        names, provided – like keywords – for indexing and search
        purposes. Where multiple character names are sent, this should
        be in a single instance of &lt;SubjectHeadingText&gt;, and it is
        recommended they should be separated by semi-colons
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_36 = "36"
    VALUE_37 = "37"
    VALUE_38 = "38"
    VALUE_39 = "39"
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_45 = "45"
    VALUE_46 = "46"
    VALUE_47 = "47"
    VALUE_48 = "48"
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_54 = "54"
    VALUE_55 = "55"
    VALUE_56 = "56"
    VALUE_57 = "57"
    VALUE_58 = "58"
    VALUE_59 = "59"
    VALUE_60 = "60"
    VALUE_61 = "61"
    VALUE_62 = "62"
    VALUE_63 = "63"
    VALUE_64 = "64"
    VALUE_65 = "65"
    VALUE_66 = "66"
    VALUE_67 = "67"
    VALUE_68 = "68"
    VALUE_69 = "69"
    VALUE_70 = "70"
    VALUE_71 = "71"
    VALUE_72 = "72"
    VALUE_73 = "73"
    VALUE_74 = "74"
    VALUE_75 = "75"
    VALUE_76 = "76"
    VALUE_77 = "77"
    VALUE_78 = "78"
    VALUE_79 = "79"
    VALUE_80 = "80"
    VALUE_81 = "81"
    VALUE_82 = "82"
    VALUE_83 = "83"
    VALUE_84 = "84"
    VALUE_85 = "85"
    VALUE_86 = "86"
    VALUE_87 = "87"
    VALUE_88 = "88"
    VALUE_89 = "89"
    VALUE_90 = "90"
    VALUE_91 = "91"
    VALUE_92 = "92"
    VALUE_93 = "93"
    VALUE_94 = "94"
    VALUE_95 = "95"
    VALUE_96 = "96"
    VALUE_97 = "97"
    VALUE_98 = "98"
    VALUE_99 = "99"
    A2 = "A2"
    A3 = "A3"
    A4 = "A4"
    A5 = "A5"
    A6 = "A6"
    A7 = "A7"
    A8 = "A8"
    A9 = "A9"
    B0 = "B0"
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    B4 = "B4"


class List28(Enum):
    """
    Audience code.

    :cvar VALUE_01: General/trade For a non-specialist adult audience
    :cvar VALUE_02: Children/juvenile For a juvenile audience, not
        specifically for any educational purpose
    :cvar VALUE_03: Young adult For a teenage audience, not specifically
        for any educational purpose
    :cvar VALUE_04: Primary and secondary/elementary and high school
        Kindergarten, pre-school, primary/elementary or secondary/high
        school education
    :cvar VALUE_05: College/higher education For universities and
        colleges of further and higher education
    :cvar VALUE_06: Professional and scholarly For an expert adult
        audience, including professional development and academic
        research
    :cvar VALUE_07: ELT/ESL Intended for use in teaching English as a
        second language
    :cvar VALUE_08: Adult education For centres providing academic,
        vocational or recreational courses for adults
    :cvar VALUE_09: Second language teaching Intended for use in
        teaching second languages, for example teaching German to
        Spanish speakers. Prefer code 07 for products specific to
        teaching English
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"


class List29(Enum):
    """
    Audience code type.

    :cvar VALUE_01: ONIX audience codes Using a code from List 28
    :cvar VALUE_02: Proprietary As specified in
        &lt;AudienceCodeTypeName&gt;
    :cvar VALUE_03: MPAA rating Motion Picture Association of America
        rating applied to movies
    :cvar VALUE_04: BBFC rating British Board of Film Classification
        rating applied to movies
    :cvar VALUE_05: FSK rating German FSK (Freiwillige Selbstkontrolle
        der Filmwirtschaft) rating applied to movies
    :cvar VALUE_06: BTLF audience code French Canadian audience code
        list, used by BTLF for Memento
    :cvar VALUE_07: Electre audience code Audience code used by Electre
        (France)
    :cvar VALUE_08: ANELE Tipo Spain: educational audience and material
        type code of the Asociación Nacional de Editores de Libros y
        Material de Enseñanza
    :cvar VALUE_09: AVI Code list used to specify reading levels for
        children’s books, used in Flanders, and formerly in the
        Netherlands – see also code 18
    :cvar VALUE_10: USK rating German USK (Unterhaltungssoftware
        Selbstkontrolle) rating applied to video or computer games
    :cvar VALUE_11: AWS Audience code used in Flanders
    :cvar VALUE_12: Schulform Type of school: codelist maintained by VdS
        Bildungsmedien eV, the German association of educational media
        publishers. See
        http://www.bildungsmedien.de/service/onixlisten/schulform_onix_codelist29_value12_0408.pdf
    :cvar VALUE_13: Bundesland School region: codelist maintained by VdS
        Bildungsmedien eV, the German association of educational media
        publishers, indicating where products are licensed to be used in
        schools. See
        http://www.bildungsmedien.de/service/onixlisten/bundesland_onix_codelist29_value13_0408.pdf
    :cvar VALUE_14: Ausbildungsberuf Occupation: codelist for vocational
        training materials, maintained by VdS Bildungsmedien eV, the
        German association of educational media publishers. See
        http://www.bildungsmedien.de/service/onixlisten/ausbildungsberufe_onix_codelist29_value14_0408.pdf
    :cvar VALUE_15: Suomalainen kouluasteluokitus Finnish school or
        college level
    :cvar VALUE_16: CBG age guidance UK Publishers Association,
        Children’s Book Group, coded indication of intended reader age,
        carried on book covers
    :cvar VALUE_17: Nielsen Book audience code Audience code used in
        Nielsen Book Services
    :cvar VALUE_18: AVI (revised) Code list used to specify reading
        levels for children’s books, used in the Netherlands – see also
        code 09
    :cvar VALUE_19: Lexile measure Lexile measure (the Lexile measure in
        &lt;AudienceCodeValue&gt; may optionally be prefixed by the
        Lexile code). Examples might be ‘880L’, ‘AD0L’ or ‘HL600L’.
        Deprecated – use &lt;Complexity&gt; instead
    :cvar VALUE_20: Fry Readability score Fry readability metric based
        on number of sentences and syllables per 100 words. Expressed as
        a number from 1 to 15 in &lt;AudienceCodeValue&gt;. Deprecated –
        use &lt;Complexity&gt; instead
    :cvar VALUE_21: Japanese Children’s audience code Children’s
        audience code (対象読者), two-digit encoding of intended target
        readership from 0–2 years up to High School level
    :cvar VALUE_22: ONIX Adult audience rating Publisher’s rating
        indicating suitability for an particular adult audience, using a
        code from List 203
    :cvar VALUE_23: Common European Framework for Language Learning
        Codes A1 to C2 indicating standardised level of language
        learning or teaching material, from beginner to advanced, used
        in EU
    :cvar VALUE_24: Korean Publication Ethics Commission rating Rating
        used in Korea to control selling of books and e-books to minors.
        Current values are 0 (suitable for all) and 19 (only for sale to
        ages 19+). See http://www.kpec.or.kr/english/
    :cvar VALUE_25: IoE Book Band UK Institute of Education Book Bands
        for Guided Reading scheme (see
        http://www.ioe.ac.uk/research/4664.html).
        &lt;AudienceCodeValue&gt; is a color, eg ‘Pink A’ or ‘Copper’.
        Deprecated – use &lt;Complexity&gt; instead
    :cvar VALUE_26: FSK Lehr-/Infoprogramm Used for German videos/DVDs
        with educational or informative content; value for
        &lt;AudienceCodeValue&gt; must be either ‘Infoprogramm gemäß §
        14 JuSchG’ or ‘Lehrprogramm gemäß § 14 JuSchG’
    :cvar VALUE_27: Intended audience language Where this is different
        from the language of the text of the book recorded in
        &lt;Language&gt;. &lt;AudienceCodeValue&gt; should be a value
        from List 74
    :cvar VALUE_28: PEGI rating Pan European Game Information rating
        used primarily for video games
    :cvar VALUE_29: Gymnasieprogram Code indicating the intended
        curriculum (eg Naturvetenskapsprogrammet, Estetica programmet)
        in Swedish higher secondary education
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"


class List3(Enum):
    """
    Record source type code.

    :cvar VALUE_00: Unspecified
    :cvar VALUE_01: Publisher
    :cvar VALUE_02: Publisher’s distributor Use to designate a
        distributor providing warehousing and fulfillment for a
        publisher or for a publisher’s sales agent, as distinct from a
        wholesaler
    :cvar VALUE_03: Wholesaler
    :cvar VALUE_04: Bibliographic agency Bibliographic data aggregator
    :cvar VALUE_05: Library bookseller Bookseller selling to libraries
        (including academic libraries)
    :cvar VALUE_06: Publisher’s sales agent Use for a publisher’s sales
        agent responsible for marketing the publisher’s products within
        a territory, as opposed to a publisher’s distributor who
        fulfills orders but does not market
    :cvar VALUE_07: Publisher’s conversion service provider Downstream
        provider of e-publication format conversion service (who might
        also be a distributor or retailer of the converted
        e-publication), supplying metadata on behalf of the publisher.
        The assigned ISBN is taken from the publisher’s ISBN prefix
    :cvar VALUE_08: Conversion service provider Downstream provider of
        e-publication format conversion service (who might also be a
        distributor or retailer of the converted e-publication),
        supplying metadata on behalf of the publisher. The assigned ISBN
        is taken from the service provider’s prefix (whether or not the
        service provider dedicates that prefix to a particular
        publisher)
    :cvar VALUE_09: ISBN Registration Agency
    :cvar VALUE_10: ISTC Registration Agency
    :cvar VALUE_11: Retail bookseller Bookseller selling primarily to
        consumers
    :cvar VALUE_12: Education bookseller Bookseller selling primarily to
        educational institutions
    :cvar VALUE_13: Library Library service providing enhanced metadata
        to publishers or other parties
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"


class List30(Enum):
    """
    Audience range qualifier.

    :cvar VALUE_11: US school grade range Values for
        &lt;AudienceRangeValue&gt; are specified in List 77
    :cvar VALUE_12: UK school grade Values are defined by BIC for
        England and Wales, Scotland and N Ireland
    :cvar VALUE_15: Reading speed, words per minute Values in
        &lt;AudienceRangeValue&gt; must be integers
    :cvar VALUE_16: Interest age, months For use up to 36 months only:
        values in &lt;AudienceRangeValue&gt; must be integers
    :cvar VALUE_17: Interest age, years Values in
        &lt;AudienceRangeValue&gt; must be integers
    :cvar VALUE_18: Reading age, years Values in
        &lt;AudienceRangeValue&gt; must be integers
    :cvar VALUE_19: Spanish school grade Spain: combined grade and
        region code, maintained by the Ministerio de Educación
    :cvar VALUE_20: Skoletrinn Norwegian educational level for primary
        and secondary education
    :cvar VALUE_21: Nivå Swedish educational qualifier (code)
    :cvar VALUE_22: Italian school grade
    :cvar VALUE_23: Schulform DEPRECATED – assigned in error: see List
        29
    :cvar VALUE_24: Bundesland DEPRECATED – assigned in error: see List
        29
    :cvar VALUE_25: Ausbildungsberuf DEPRECATED – assigned in error: see
        List 29
    :cvar VALUE_26: Canadian school grade range Values for
        &lt;AudienceRangeValue&gt; are specified in List 77
    :cvar VALUE_27: Finnish school grade range
    :cvar VALUE_28: Finnish Upper secondary school course Lukion kurssi
    :cvar VALUE_29: Chinese School Grade range Values are P, K, 1–17
        (including college-level audiences), see List 227
    :cvar VALUE_30: Nomenclature niveaux French educational level
        classification scolomfr-voc-022, used for example on WizWiz.fr.
        See http://www.lom-fr.fr/scolomfr/vocabulaires/consultation-des-
        vocabulaires.html
    """
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_30 = "30"


class List31(Enum):
    """
    Audience range precision.

    :cvar VALUE_01: Exact
    :cvar VALUE_03: From
    :cvar VALUE_04: To
    """
    VALUE_01 = "01"
    VALUE_03 = "03"
    VALUE_04 = "04"


class List32(Enum):
    """
    Complexity scheme identifier code.

    :cvar VALUE_01: Lexile code For example AD or HL. DEPRECATED in ONIX
        3 – use code 06 instead
    :cvar VALUE_02: Lexile number For example 880L. DEPRECATED in ONIX 3
        – use code 06 instead
    :cvar VALUE_03: Fry Readability score Fry readability metric based
        on number of sentences and syllables per 100 words. Expressed as
        a number from 1 to 15 in &lt;ComplexityCode&gt;
    :cvar VALUE_04: IoE Book Band UK Institute of Education Book Bands
        for Guided Reading scheme (see
        http://www.ioe.ac.uk/research/4664.html). &lt;ComplexityCode&gt;
        is a color, eg ‘Pink A’ or ‘Copper’
    :cvar VALUE_05: Fountas &amp; Pinnell Text Level Gradient
        &lt;ComplexityCode&gt; is a code from ‘A’ to Z+’. See
        http://www.fountasandpinnellleveledbooks.com/aboutLeveledTexts.aspx
    :cvar VALUE_06: Lexile measure The Lexile measure in
        &lt;ComplexityCode&gt; combines the Lexile number (for example
        620L or 880L) and optionally the Lexile code (for example AD or
        HL). Examples might be ‘880L’, ‘AD0L’ or ‘HL600L’. See
        https://lexile.com/about-lexile/lexile-overview/
    :cvar VALUE_07: ATOS for Books Advantage-TASA Open Standard book
        readability score, used for example within the Renaissance
        Learning Accelerated Reader scheme. &lt;ComplexityCode&gt; is a
        real number between 0 and 17. See
        http://www.renaissance.com/products/accelerated-reader/atos-
        analyzer
    :cvar VALUE_08: Flesch-Kincaid Grade Level Flesch-Kincaid Grade
        Level Formula, a standard readability measure based on the
        weighted number of syllables per word and words per sentence.
        &lt;ComplexityCode&gt; is a real number between about -1 and 20
    :cvar VALUE_09: Guided Reading Level Use this code for books
        levelled by the publisher or a third party using the Fountas and
        Pinnell Guided Reading methodology
    :cvar VALUE_10: Reading Recovery Level Used for books aimed at K-2
        literacy intervention. &lt;ComplexityCode&gt; is an integer
        between 1 and 20
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"


class List33(Enum):
    """
    Other text type code.

    :cvar VALUE_01: Main description
    :cvar VALUE_02: Short description/annotation Limited to a maximum of
        350 characters
    :cvar VALUE_03: Long description
    :cvar VALUE_04: Table of contents Used for a table of contents sent
        as a single text field, which may or may not carry structure
        expressed through HTML etc. Alternatively, a fully structured
        table of contents may be sent by using the &lt;ContentItem&gt;
        composite
    :cvar VALUE_05: Review quote, restricted length A review quote that
        is restricted to a maximum length agreed between the sender and
        receiver of an ONIX file
    :cvar VALUE_06: Quote from review of previous edition A review quote
        taken from a review of a previous edition of the work
    :cvar VALUE_07: Review text Full text of a review of the product
    :cvar VALUE_08: Review quote A quote from a review of the product
    :cvar VALUE_09: Promotional ‘headline’ A promotional phrase which is
        intended to headline a description of the product
    :cvar VALUE_10: Previous review quote A quote from a review of a
        previous work by the same author(s) or in the same series
    :cvar VALUE_11: Author comments May be part of Reading Group Guide
        material: for other commentary, see code 42
    :cvar VALUE_12: Description for reader
    :cvar VALUE_13: Biographical note A note referring to all
        contributors to a product – NOT linked to a single contributor
    :cvar VALUE_14: Description for Reading Group Guide For linking to a
        complete Reading Group Guide, see code 41
    :cvar VALUE_15: Discussion question for Reading Group Guide Each
        instance must carry a single question: for linking to a complete
        Reading Group Guide, see code 41
    :cvar VALUE_16: Competing titles Free text listing of other titles
        with which the product is in competition: although this text
        might not appear in ‘public’ ONIX records, it could be required
        where ONIX Is used as a communication format within a group of
        publishing and distribution companies
    :cvar VALUE_17: Flap copy
    :cvar VALUE_18: Back cover copy
    :cvar VALUE_19: Feature Text describing a feature of a product to
        which the publisher wishes to draw attention for promotional
        purposes. Each separate feature should be described by a
        separate repeat, so that formatting can be applied at the
        discretion of the receiver of the ONIX record
    :cvar VALUE_20: New feature As code 19, but used for a feature which
        is new in a new edition of the product
    :cvar VALUE_21: Publisher’s notice A statement included by a
        publisher in fulfillment of its contractual obligations, such as
        a disclaimer, sponsor statement, or legal notice of any sort.
        Note that the inclusion of such a notice cannot and does not
        imply that a user of the ONIX record is obliged to reproduce it
    :cvar VALUE_22: Index
    :cvar VALUE_23: Excerpt from book
    :cvar VALUE_24: First chapter
    :cvar VALUE_25: Description for sales people
    :cvar VALUE_26: Description for press or other media
    :cvar VALUE_27: Description for subsidiary rights department
    :cvar VALUE_28: Description for teachers/educators
    :cvar VALUE_30: Unpublished endorsement A quote usually provided by
        a celebrity to promote a new book, not from a review
    :cvar VALUE_31: Description for bookstore
    :cvar VALUE_32: Description for library
    :cvar VALUE_33: Introduction or preface
    :cvar VALUE_34: Full text
    :cvar VALUE_35: Promotional text Promotional text not covered
        elsewhere
    :cvar VALUE_40: Author interview / QandA
    :cvar VALUE_41: Reading Group Guide Complete guide: see also codes
        14 and 15
    :cvar VALUE_42: Commentary / discussion Other than author comments:
        see code 11
    :cvar VALUE_43: Short description for series or set (of which the
        product is a part.) Limited to a maximum of 350 characters
    :cvar VALUE_44: Long description for series or set (of which the
        product is a part)
    :cvar VALUE_45: Contributor event schedule Link to a schedule in
        iCalendar format
    :cvar VALUE_46: License Link to a license covering permitted usage
        of the product content
    :cvar VALUE_47: Open access statement Short summary statement of
        open access status and any related conditions (eg ‘Open access –
        no commercial use’), primarily for marketing purposes. Should
        always be accompanied by a link to the complete license (see
        code 46)
    :cvar VALUE_48: Digital exclusivity statement Short summary
        statement that the product is available only in digital formats
        (eg ‘Digital exclusive’). If a non-digital version is planned,
        an &lt;EndDate&gt; should be used to specify the date when
        exclusivity will end. If a non-digital version is available, the
        statement should not be included
    :cvar VALUE_49: Official recommendation For example a recommendation
        or approval provided by a ministry of education or other
        official body. Use &lt;Text&gt; to provide details and
        &lt;TextSourceCorporate&gt; to name the approver
    :cvar VALUE_98: Master brand name A master brand name or title,
        where the use of the brand spans multiple sets, series and
        product forms, and possibly multiple imprints and publishers.
        Used only for branded media properties carrying, for example, a
        children’s character brand. (This functionality is provided as a
        workaround in ONIX 2.1 only. ONIX 3.0 has specific provision for
        master brands as title elements
    :cvar VALUE_99: Country of final manufacture A single ISO 3166-1
        country code from List 91 designating the country of final
        manufacture of the product. (This functionality is provided as a
        workaround in ONIX 2.1. ONIX 3.0 has specific provision for
        country of manufacture as a separate element)
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_45 = "45"
    VALUE_46 = "46"
    VALUE_47 = "47"
    VALUE_48 = "48"
    VALUE_49 = "49"
    VALUE_98 = "98"
    VALUE_99 = "99"


class List34(Enum):
    """
    Text format code.

    :cvar VALUE_00: ASCII text DEPRECATED: use code 06 or 07 as
        appropriate
    :cvar VALUE_01: SGML
    :cvar VALUE_02: HTML Other than XHTML
    :cvar VALUE_03: XML Other than XHTML
    :cvar VALUE_04: PDF DEPRECATED: was formerly assigned both to PDF
        and to XHTML
    :cvar VALUE_05: XHTML
    :cvar VALUE_06: Default text format Default: text containing no tags
        of any kind, except for the tags &amp;amp; and &amp;lt; that XML
        insists must be used to represent ampersand and less-than
        characters in text, and in the encoding declared at the head of
        the message or in the XML default (UTF-8 or UTF-16) if there is
        no explicit declaration
    :cvar VALUE_07: Basic ASCII text Plain text containing no tags of
        any kind, except for the tags &amp;amp; and &amp;lt; that XML
        insists must be used to represent ampersand and less-than
        characters in text, and with the character set limited to the
        ASCII range, i.e. valid UTF-8 characters whose character number
        lies between 32 (space) and 126 (tilde)
    :cvar VALUE_08: PDF Replaces 04 for the &lt;TextFormat&gt; element,
        but cannot of course be used as a textformat attribute
    :cvar VALUE_09: Microsoft rich text format (RTF)
    :cvar VALUE_10: Microsoft Word binary format (DOC)
    :cvar VALUE_11: ECMA 376 WordprocessingML Office Open XML file
        format / OOXML / DOCX
    :cvar VALUE_12: ISO 26300 ODF ISO Open Document Format
    :cvar VALUE_13: Corel Wordperfect binary format (DOC)
    :cvar VALUE_14: EPUB The Open Publication Structure / OPS Container
        Format standard of the International Digital Publishing Forum
        (IDPF) [File extension .epub]
    :cvar VALUE_15: XPS XML Paper Specification
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"


class List35(Enum):
    """
    Text link type code.

    :cvar VALUE_01: URL
    :cvar VALUE_02: DOI
    :cvar VALUE_03: PURL
    :cvar VALUE_04: URN
    :cvar VALUE_05: FTP address
    :cvar VALUE_06: filename
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"


class List36(Enum):
    """
    Front cover image file format code.

    :cvar VALUE_02: GIF
    :cvar VALUE_03: JPEG
    :cvar VALUE_05: TIF
    """
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_05 = "05"


class List37(Enum):
    """
    Front cover image file link type code.

    :cvar VALUE_01: URL
    :cvar VALUE_02: DOI
    :cvar VALUE_03: PURL
    :cvar VALUE_04: URN
    :cvar VALUE_05: FTP address
    :cvar VALUE_06: filename
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"


class List38(Enum):
    """
    Image/audio/video file type code.

    :cvar VALUE_01: Whole product Link to a location where the whole
        product may be found – used for epublications
    :cvar VALUE_02: Application: software demo
    :cvar VALUE_03: Image: whole cover Includes cover, back cover, spine
        and – where appropriate – any flaps. Quality unspecified: if
        sending both a standard quality and a high quality image, use 03
        for standard quality and 05 for high quality
    :cvar VALUE_04: Image: front cover Quality unspecified: if sending
        both a standard quality and a high quality image, use 04 for
        standard quality and 06 for high quality
    :cvar VALUE_05: Image: whole cover, high quality Should have a
        minimum resolution of 300 dpi when rendered at the intended size
        for display or print
    :cvar VALUE_06: Image: front cover, high quality Should have a
        minimum resolution of 300 dpi when rendered at the intended size
        for display or print
    :cvar VALUE_07: Image: front cover thumbnail
    :cvar VALUE_08: Image: contributor(s)
    :cvar VALUE_10: Image: for series Use for an image, other than a
        logo, that is part of the ‘branding’ of a series
    :cvar VALUE_11: Image: series logo
    :cvar VALUE_12: Image: product logo Use only for a logo which is
        specific to an individual product
    :cvar VALUE_16: Image: Master brand logo
    :cvar VALUE_17: Image: publisher logo
    :cvar VALUE_18: Image: imprint logo
    :cvar VALUE_22: Image: table of contents
    :cvar VALUE_23: Image: sample content Use for inside page image for
        book, or screenshot for software or game (revised definition
        from Issue 8)
    :cvar VALUE_24: Image: back cover Quality unspecified: if sending
        both a standard quality and a high quality image, use 24 for
        standard quality and 25 for high quality
    :cvar VALUE_25: Image: back cover, high quality Should have a
        minimum resolution of 300 dpi when rendered at the intended size
        for display or print
    :cvar VALUE_26: Image: back cover thumbnail
    :cvar VALUE_27: Image: other cover material
    :cvar VALUE_28: Image: promotional material
    :cvar VALUE_29: Video segment: unspecified
    :cvar VALUE_30: Audio segment: unspecified
    :cvar VALUE_31: Video: author presentation / commentary
    :cvar VALUE_32: Video: author interview
    :cvar VALUE_33: Video: author reading
    :cvar VALUE_34: Video: cover material
    :cvar VALUE_35: Video: sample content
    :cvar VALUE_36: Video: promotional material
    :cvar VALUE_37: Video: review
    :cvar VALUE_38: Video: other commentary / discussion
    :cvar VALUE_41: Audio: author presentation / commentary
    :cvar VALUE_42: Audio: author interview
    :cvar VALUE_43: Audio: author reading
    :cvar VALUE_44: Audio: sample content
    :cvar VALUE_45: Audio: promotional material
    :cvar VALUE_46: Audio: review
    :cvar VALUE_47: Audio: other commentary / discussion
    :cvar VALUE_51: Application: sample content Use for ‘look inside’
        facility or ‘widget’
    :cvar VALUE_52: Application: promotional material
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_36 = "36"
    VALUE_37 = "37"
    VALUE_38 = "38"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_45 = "45"
    VALUE_46 = "46"
    VALUE_47 = "47"
    VALUE_51 = "51"
    VALUE_52 = "52"


class List39(Enum):
    """
    Image/audio/video file format code.

    :cvar VALUE_02: GIF
    :cvar VALUE_03: JPEG
    :cvar VALUE_04: PDF
    :cvar VALUE_05: TIF
    :cvar VALUE_06: RealAudio 28.8
    :cvar VALUE_07: MP3 MPEG-1/2 Audio Layer III file (.mp3)
    :cvar VALUE_08: MPEG-4 MPEG-4 container format (.mp4, .m4a)
    :cvar VALUE_09: PNG Portable Network Graphics bitmapped image format
        (.png)
    :cvar VALUE_10: WMA Windows Media Audio format (.wma)
    :cvar VALUE_11: AAC Advanced Audio Codec format (.aac)
    :cvar VALUE_12: WAV Waveform audio file (.wav)
    :cvar VALUE_13: AIFF Audio Interchange File Format (.aiff)
    :cvar VALUE_14: WMV Windows Media Video format (.wmv)
    :cvar VALUE_15: OGG Ogg container format (.ogg)
    :cvar VALUE_16: AVI Audio Video Interleaved container format (.avi)
    :cvar VALUE_17: MOV Quicktime container format (.mov)
    :cvar VALUE_18: Flash Flash container format (includes .flv, .swf,
        .f4v etc)
    :cvar VALUE_19: 3GP 3GP container format (.3gp, 3g2)
    :cvar VALUE_20: WebM WebM container format (includes .webm and .mkv)
    """
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"


class List40(Enum):
    """
    Image/audio/video file link type.

    :cvar VALUE_01: URL
    :cvar VALUE_02: DOI
    :cvar VALUE_03: PURL
    :cvar VALUE_04: URN
    :cvar VALUE_05: FTP address
    :cvar VALUE_06: filename
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"


class List41(Enum):
    """
    Prize or award achievement code.

    :cvar VALUE_01: Winner
    :cvar VALUE_02: Runner-up Named as being in second place
    :cvar VALUE_03: Commended Cited as being worthy of special attention
        at the final stage of the judging process, but not named
        specifically as winner or runner-up. Possible terminology used
        by a particular prize includes ‘specially commended’ or
        ‘honored’
    :cvar VALUE_04: Short-listed Title named by the judging process to
        be one of the final list of candidates, such as a ‘short-list’
        from which the winner is selected, or a title named as
        ‘finalist’
    :cvar VALUE_05: Long-listed Title named by the judging process to be
        one of the preliminary list of candidates, such as a ‘long-list’
        from which first a shorter list or set of finalists is selected,
        and then the winner is announced
    :cvar VALUE_06: Joint winner Or co-winner
    :cvar VALUE_07: Nominated Selected by judging panel or an official
        nominating process for final consideration for a prize, award or
        honour for which no ‘short-list’ or ‘long list’ exists
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"


class List42(Enum):
    """
    Text item type code.

    :cvar VALUE_01: Textual work A complete work which is published as a
        content item in a product which carries two or more such works,
        eg when two or three novels are published in a single omnibus
        volume
    :cvar VALUE_02: Front matter Text components such as Preface,
        Introduction etc which appear as preliminaries to the main body
        of text content in a product
    :cvar VALUE_03: Body matter Text components such as Part, Chapter,
        Section etc which appear as part of the main body of text
        content in a product
    :cvar VALUE_04: Back matter Text components such as Index which
        appear after the main body of text in a product
    :cvar VALUE_10: Serial item, miscellaneous or unspecified For
        journals
    :cvar VALUE_11: Research article For journals
    :cvar VALUE_12: Review article For journals
    :cvar VALUE_13: Letter For journals
    :cvar VALUE_14: Short communication For journals
    :cvar VALUE_15: Erratum For journals
    :cvar VALUE_16: Abstract For journals
    :cvar VALUE_17: Book review (or review of other publication) For
        journals
    :cvar VALUE_18: Editorial For journals
    :cvar VALUE_19: Product review For journals
    :cvar VALUE_20: Index
    :cvar VALUE_21: Obituary For journals
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"


class List43(Enum):
    """
    Text item identifier type code.

    :cvar VALUE_01: Proprietary For example, a publisher’s own
        identifier. Note that &lt;IDTypeName&gt; is required with
        proprietary identifiers
    :cvar VALUE_03: GTIN-13 Formerly known as the EAN-13 (unhyphenated)
    :cvar VALUE_06: DOI
    :cvar VALUE_09: PII Publisher item identifier
    :cvar VALUE_10: SICI For serial items only
    :cvar VALUE_11: ISTC
    :cvar VALUE_15: ISBN-13 (Unhyphenated)
    """
    VALUE_01 = "01"
    VALUE_03 = "03"
    VALUE_06 = "06"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_15 = "15"


class List44(Enum):
    """
    Name code type.

    :cvar VALUE_01: Proprietary Note that &lt;IDTypeName&gt; is required
        with proprietary identifiers
    :cvar VALUE_02: Proprietary DEPRECATED – use 01
    :cvar VALUE_03: DNB publisher identifier Deutsche Nationalbibliothek
        publisher identifier
    :cvar VALUE_04: Börsenverein Verkehrsnummer
    :cvar VALUE_05: German ISBN Agency publisher identifier
    :cvar VALUE_06: GLN GS1 global location number (formerly EAN
        location number)
    :cvar VALUE_07: SAN Book trade Standard Address Number – US, UK etc
    :cvar VALUE_08: MARC organization code MARC code list for
        organizations – see
        http://www.loc.gov/marc/organizations/orgshome.html
    :cvar VALUE_10: Centraal Boekhuis Relatie ID Trading party
        identifier used in the Netherlands
    :cvar VALUE_13: Fondscode Boekenbank Flemish publisher code
    :cvar VALUE_15: Y-tunnus Business Identity Code (Finland). See
        http://www.ytj.fi/ (in Finnish)
    :cvar VALUE_16: ISNI International Standard Name Identifier. See
        http://www.isni.org/
    :cvar VALUE_17: PND Personennamendatei – person name authority file
        used by Deutsche Nationalbibliothek and in other German-speaking
        countries. See
        http://www.d-nb.de/standardisierung/normdateien/pnd.htm (German)
        or http://www.d-nb.de/eng/standardisierung/normdateien/pnd.htm
        (English). DEPRECATED in favour of the GND
    :cvar VALUE_18: LCCN A control number assigned to a Library of
        Congress Name Authority record
    :cvar VALUE_19: Japanese Publisher identifier Publisher identifier
        administered by Japanese ISBN Agency
    :cvar VALUE_20: GKD Gemeinsame Körperschaftsdatei – Corporate Body
        Authority File in the German-speaking countries. See
        http://www.d-nb.de/standardisierung/normdateien/gkd.htm (German)
        or http://www.d-nb.de/eng/standardisierung/normdateien/gkd.htm
        (English). DEPRECATED in favour of the GND
    :cvar VALUE_21: ORCID Open Researcher and Contributor ID. See
        http://www.orcid.org/
    :cvar VALUE_22: GAPP Publisher Identifier Publisher identifier
        maintained by the Chinese ISBN Agency (GAPP)
    :cvar VALUE_23: VAT Identity Number Identifier for a business
        organization for VAT purposes, eg within the EU’s VIES system.
        See http://ec.europa.eu/taxation_customs/vies/faqvies.do for EU
        VAT ID formats, which vary from country to country. Generally
        these consist of a two-letter country code followed by the 8–12
        digits of the national VAT ID. Some countries include one or two
        letters within their VAT ID. See
        http://en.wikipedia.org/wiki/VAT_identification_number for non-
        EU countries that maintain similar identifiers. Spaces, dashes
        etc should be omitted
    :cvar VALUE_24: JP Distribution Identifier 4-digit business
        organization identifier controlled by the Japanese Publication
        Wholesalers Association
    :cvar VALUE_25: GND Gemeinsame Normdatei – Joint Authority File in
        the German-speaking countries. See http://www.dnb.de/EN/gnd
        (English). Combines the PND, SWD and GKD into a single authority
        file, and should be used in preference
    :cvar VALUE_26: DUNS Dunn and Bradstreet Universal Numbering System,
        see http://www.dnb.co.uk/dandb-duns-number
    :cvar VALUE_27: Ringgold ID Ringgold organizational identifier, see
        http://www.ringgold.com/pages/identify.html
    :cvar VALUE_28: Identifiant Editeur Electre French Electre publisher
        identifier
    :cvar VALUE_29: EIDR Party DOI DOI used in EIDR party registry, for
        example ‘10.5237/C9F6-F41F’ (Sam Raimi). See http://eidr.org
    :cvar VALUE_30: Identifiant Marque Electre French Electre imprint
        Identifier
    :cvar VALUE_31: VIAF ID Virtual Internet Authority File.
        &lt;IDValue&gt; should be a number. The URI form of the
        identifier can be created by prefixing the number with
        ‘https://viaf.org/viaf/’. See https://viaf.org
    :cvar VALUE_32: FundRef DOI DOI used in CrossRef’s Open Funder
        Registry list of academic research funding bodies, for example
        ‘10.13039/100004440’ (Wellcome Trust). See
        http://www.crossref.org/fundingdata/registry.html
    :cvar VALUE_33: BNE CN Control number assigned to a Name Authority
        record by the Biblioteca Nacional de España
    :cvar VALUE_34: BNF Control Number Numéro de la notice de personne
        BNF
    :cvar VALUE_35: ARK Archival Resource Key, as a URL (including the
        address of the ARK resolver provided by eg a national library)
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_10 = "10"
    VALUE_13 = "13"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_35 = "35"


class List45(Enum):
    """
    Publishing role code.

    :cvar VALUE_01: Publisher
    :cvar VALUE_02: Co-publisher Use where two or more publishers co-
        publish the exact same product, either under a single ISBN (in
        which case both publishers are co-publishers), or under
        different ISBNs (in which case the publisher of THIS ISBN is the
        publisher and the publishers of OTHER ISBNs are co-publishers.
        Note this is different from publication of ‘co-editions’
    :cvar VALUE_03: Sponsor
    :cvar VALUE_04: Publisher of original-language version Of a
        translated work
    :cvar VALUE_05: Host/distributor of electronic content
    :cvar VALUE_06: Published for/on behalf of
    :cvar VALUE_07: Published in association with Use also for
        ‘Published in cooperation with’
    :cvar VALUE_08: Published on behalf of DEPRECATED: use code 06
    :cvar VALUE_09: New or acquiring publisher When ownership of a
        product or title is transferred from one publisher to another
    :cvar VALUE_10: Publishing group The group to which a publisher
        (publishing role 01) belongs: use only if a publisher has been
        identified with role code 01
    :cvar VALUE_11: Publisher of facsimile original The publisher of the
        edition of which a product is a facsimile
    :cvar VALUE_12: Repackager of prebound edition The repackager of a
        prebound edition that has been assigned its own identifier. (In
        the US, a ‘prebound edition’ is a book that was previously
        bound, normally as a paperback, and has been rebound with a
        library-quality hardcover binding by a supplier other than the
        original publisher.) Required when the &lt;EditionType&gt; is
        coded PRB. The original publisher should be named as the
        ‘publisher’
    :cvar VALUE_13: Former publisher When ownership of a product or
        title is transferred from one publisher to another (complement
        of code 09)
    :cvar VALUE_14: Publication funder Body funding publication fees, if
        different from the body funding the underlying research. For use
        with open access publications
    :cvar VALUE_15: Research funder Body funding the research on which
        publication is based, if different from the body funding the
        publication. For use with open access publications
    :cvar VALUE_16: Funding body Body funding research and publication.
        For use with open access publications
    :cvar VALUE_17: Printer Organisation responsible for printing a
        printed product. Supplied primarily to meet legal deposit
        requirements, and may apply only to the first impression. The
        organisation may also be responsible for binding, when a
        separate binder is not specified
    :cvar VALUE_18: Binder Organisation responsible for binding a
        printed product (where distinct from the printer). Supplied
        primarily to meet legal deposit requirements, and may apply only
        to the first impression
    :cvar VALUE_19: Manufacturer Organisation primarily responsible for
        physical manufacture of a product, when neither Printer nor
        Binder is directly appropriate (for example, with disc or tape
        products, or digital products on a physical carrier)
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"


class List46(Enum):
    """
    Sales rights type code.

    :cvar VALUE_00: Sales rights unknown or unstated for any reason May
        only be used with the ONIX 3 &lt;ROWSalesRightsType&gt; element
    :cvar VALUE_01: For sale with exclusive rights in the specified
        countries or territories
    :cvar VALUE_02: For sale with non-exclusive rights in the specified
        countries or territories
    :cvar VALUE_03: Not for sale in the specified countries or
        territories (reason unspecified)
    :cvar VALUE_04: Not for sale in the specified countries (but
        publisher holds exclusive rights in those countries or
        territories)
    :cvar VALUE_05: Not for sale in the specified countries (publisher
        holds non-exclusive rights in those countries or territories)
    :cvar VALUE_06: Not for sale in the specified countries (because
        publisher does not hold rights in those countries or
        territories)
    :cvar VALUE_07: For sale with exclusive rights in the specified
        countries or territories (sales restriction applies) Only for
        use with ONIX 3. Deprecated
    :cvar VALUE_08: For sale with non-exclusive rights in the specified
        countries or territories (sales restriction applies) Only for
        use with ONIX 3. Deprecated
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"


class List47(Enum):
    """
    Rights region.

    :cvar VALUE_000: World
    :cvar VALUE_001: World except territories specified elsewhere in
        rights statements
    :cvar VALUE_002: UK airports
    :cvar VALUE_003: UK ‘open market’ Use when an open market edition is
        published under its own ISBN
    """
    VALUE_000 = "000"
    VALUE_001 = "001"
    VALUE_002 = "002"
    VALUE_003 = "003"


class List48(Enum):
    """
    Measure type code.

    :cvar VALUE_01: Height For a book, the overall spine height when
        standing on a shelf. For a folded map, the height when folded.
        In general, the height of a product in the form in which it is
        presented or packaged for retail sale
    :cvar VALUE_02: Width For a book, the overall horizontal dimension
        of the cover when standing upright. For a folded map, the width
        when folded. In general, the width of a product in the form in
        which it is presented or packaged for retail sale
    :cvar VALUE_03: Thickness For a book, the overall thickness of the
        spine. For a folded map, the thickness when folded. In general,
        the thickness or depth of a product in the form in which it is
        presented or packaged for retail sale
    :cvar VALUE_04: Page trim height Not recommended for general use
    :cvar VALUE_05: Page trim width Not recommended for general use
    :cvar VALUE_08: Unit weight
    :cvar VALUE_09: Diameter (sphere) Of a globe, for example
    :cvar VALUE_10: Unfolded/unrolled sheet height The height of a
        folded or rolled sheet map, poster etc when unfolded
    :cvar VALUE_11: Unfolded/unrolled sheet width The width of a folded
        or rolled sheet map, poster etc when unfolded
    :cvar VALUE_12: Diameter (tube or cylinder) The diameter of the
        cross-section of a tube or cylinder, usually carrying a rolled
        sheet product. Use 01 ‘Height’ for the height or length of the
        tube
    :cvar VALUE_13: Rolled sheet package side measure The length of a
        side of the cross-section of a long triangular or square
        package, usually carrying a rolled sheet product. Use 01
        ‘Height’ for the height or length of the package
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"


class List49(Enum):
    """
    Region code.

    :cvar AU_CT: Australian Capital Territory
    :cvar AU_NS: New South Wales
    :cvar AU_NT: Northern Territory
    :cvar AU_QL: Queensland
    :cvar AU_SA: South Australia
    :cvar AU_TS: Tasmania
    :cvar AU_VI: Victoria
    :cvar AU_WA: Western Australia
    :cvar CA_AB: Alberta
    :cvar CA_BC: British Columbia
    :cvar CA_MB: Manitoba
    :cvar CA_NB: New Brunswick
    :cvar CA_NL: Newfoundland and Labrador
    :cvar CA_NS: Nova Scotia
    :cvar CA_NT: Northwest Territories
    :cvar CA_NU: Nunavut
    :cvar CA_ON: Ontario
    :cvar CA_PE: Prince Edward Island
    :cvar CA_QC: Quebec
    :cvar CA_SK: Saskatchewan
    :cvar CA_YT: Yukon Territory
    :cvar CN_11: Beijing Municipality
    :cvar CN_12: Tianjin Municipality
    :cvar CN_13: Hebei Province
    :cvar CN_14: Shanxi Province
    :cvar CN_15: Inner Mongolia Autonomous Region
    :cvar CN_21: Liaoning Province
    :cvar CN_22: Jilin Province
    :cvar CN_23: Heilongjiang Province
    :cvar CN_31: Shanghai Municipality
    :cvar CN_32: Jiangsu Province
    :cvar CN_33: Zhejiang Province
    :cvar CN_34: Anhui Province
    :cvar CN_35: Fujian Province
    :cvar CN_36: Jiangxi Province
    :cvar CN_37: Shandong Province
    :cvar CN_41: Henan Province
    :cvar CN_42: Hubei Province
    :cvar CN_43: Hunan Province
    :cvar CN_44: Guangdong Province
    :cvar CN_45: Guangxi Zhuang Autonomous Region
    :cvar CN_46: Hainan Province
    :cvar CN_50: Chongqing Municipality
    :cvar CN_51: Sichuan Province
    :cvar CN_52: Guizhou Province
    :cvar CN_53: Yunnan Province
    :cvar CN_54: Tibet Autonomous Region
    :cvar CN_61: Shaanxi Province
    :cvar CN_62: Gansu Province
    :cvar CN_63: Qinghai Province
    :cvar CN_64: Ningxia Hui Autonomous Region
    :cvar CN_65: Xinjiang Uyghur Autonomous Region
    :cvar CN_71: Taiwan Province Prefer code TW (Taiwan, Province of
        China) from List 91
    :cvar CN_91: Hong Kong Special Administrative Region Prefer code HK
        (Hong Kong) from List 91
    :cvar CN_92: Macau Special Administrative Region Prefer code MO
        (Macao) from List 91
    :cvar ES_CN: Canary Islands
    :cvar FR_H: Corsica
    :cvar GB_AIR: UK airside Airside outlets at UK international
        airports only
    :cvar GB_APS: UK airports All UK airports, including both airside
        and other outlets
    :cvar GB_CHA: Channel Islands DEPRECATED, replaced by country codes
        GG – Guernsey, and JE – Jersey
    :cvar GB_ENG: England
    :cvar GB_EWS: England, Wales, Scotland UK excluding Northern Ireland
    :cvar GB_IOM: Isle of Man DEPRECATED, replaced by country code IM –
        Isle of Man
    :cvar GB_NIR: Northern Ireland
    :cvar GB_SCT: Scotland
    :cvar GB_WLS: Wales
    :cvar IE_AIR: Ireland airside Airside outlets at Irish international
        airports only
    :cvar IT_AG: Agrigento
    :cvar IT_AL: Alessandria
    :cvar IT_AN: Ancona
    :cvar IT_AO: Aosta
    :cvar IT_AR: Arezzo
    :cvar IT_AP: Ascoli Piceno
    :cvar IT_AT: Asti
    :cvar IT_AV: Avellino
    :cvar IT_BA: Bari
    :cvar IT_BT: Barletta-Andria-Trani
    :cvar IT_BL: Belluno
    :cvar IT_BN: Benevento
    :cvar IT_BG: Bergamo
    :cvar IT_BI: Biella
    :cvar IT_BO: Bologna
    :cvar IT_BZ: Bolzano
    :cvar IT_BS: Brescia
    :cvar IT_BR: Brindisi
    :cvar IT_CA: Cagliari
    :cvar IT_CL: Caltanissetta
    :cvar IT_CB: Campobasso
    :cvar IT_CI: Carbonia-Iglesias
    :cvar IT_CE: Caserta
    :cvar IT_CT: Catania
    :cvar IT_CZ: Catanzaro
    :cvar IT_CH: Chieti
    :cvar IT_CO: Como
    :cvar IT_CS: Cosenza
    :cvar IT_CR: Cremona
    :cvar IT_KR: Crotone
    :cvar IT_CN: Cuneo
    :cvar IT_EN: Enna
    :cvar IT_FM: Fermo
    :cvar IT_FE: Ferrara
    :cvar IT_FI: Firenze
    :cvar IT_FG: Foggia
    :cvar IT_FC: Forlì-Cesena
    :cvar IT_FR: Frosinone
    :cvar IT_GE: Genova
    :cvar IT_GO: Gorizia
    :cvar IT_GR: Grosseto
    :cvar IT_IM: Imperia
    :cvar IT_IS: Isernia
    :cvar IT_SP: La Spezia
    :cvar IT_AQ: L’Aquila
    :cvar IT_LT: Latina
    :cvar IT_LE: Lecce
    :cvar IT_LC: Lecco
    :cvar IT_LI: Livorno
    :cvar IT_LO: Lodi
    :cvar IT_LU: Lucca
    :cvar IT_MC: Macerata
    :cvar IT_MN: Mantova
    :cvar IT_MS: Massa-Carrara
    :cvar IT_MT: Matera
    :cvar IT_VS: Medio Campidano
    :cvar IT_ME: Messina
    :cvar IT_MI: Milano
    :cvar IT_MO: Modena
    :cvar IT_MB: Monza e Brianza
    :cvar IT_NA: Napoli
    :cvar IT_NO: Novara
    :cvar IT_NU: Nuoro
    :cvar IT_OG: Ogliastra
    :cvar IT_OT: Olbia-Tempio
    :cvar IT_OR: Oristano
    :cvar IT_PD: Padova
    :cvar IT_PA: Palermo
    :cvar IT_PR: Parma
    :cvar IT_PV: Pavia
    :cvar IT_PG: Perugia
    :cvar IT_PU: Pesaro e Urbino
    :cvar IT_PE: Pescara
    :cvar IT_PC: Piacenza
    :cvar IT_PI: Pisa
    :cvar IT_PT: Pistoia
    :cvar IT_PN: Pordenone
    :cvar IT_PZ: Potenza
    :cvar IT_PO: Prato
    :cvar IT_RG: Ragusa
    :cvar IT_RA: Ravenna
    :cvar IT_RC: Reggio Calabria
    :cvar IT_RE: Reggio Emilia
    :cvar IT_RI: Rieti
    :cvar IT_RN: Rimini
    :cvar IT_RM: Roma
    :cvar IT_RO: Rovigo
    :cvar IT_SA: Salerno
    :cvar IT_SS: Sassari
    :cvar IT_SV: Savona
    :cvar IT_SI: Siena
    :cvar IT_SR: Siracusa
    :cvar IT_SO: Sondrio
    :cvar IT_TA: Taranto
    :cvar IT_TE: Teramo
    :cvar IT_TR: Terni
    :cvar IT_TO: Torino
    :cvar IT_TP: Trapani
    :cvar IT_TN: Trento
    :cvar IT_TV: Treviso
    :cvar IT_TS: Trieste
    :cvar IT_UD: Udine
    :cvar IT_VA: Varese
    :cvar IT_VE: Venezia
    :cvar IT_VB: Verbano-Cusio-Ossola
    :cvar IT_VC: Vercelli
    :cvar IT_VR: Verona
    :cvar IT_VV: Vibo Valentia
    :cvar IT_VI: Vicenza
    :cvar IT_VT: Viterbo
    :cvar RS_KM: Kosovo-Metohija
    :cvar RS_VO: Vojvodina
    :cvar RU_AD: Republic of Adygeya
    :cvar RU_AL: Republic of Altay
    :cvar RU_BA: Republic of Bashkortostan
    :cvar RU_BU: Republic of Buryatiya
    :cvar RU_CE: Chechenskaya Republic
    :cvar RU_CU: Chuvashskaya Republic
    :cvar RU_DA: Republic of Dagestan
    :cvar RU_IN: Republic of Ingushetiya
    :cvar RU_KB: Kabardino-Balkarskaya Republic
    :cvar RU_KL: Republic of Kalmykiya
    :cvar RU_KC: Karachayevo-Cherkesskaya Republic
    :cvar RU_KR: Republic of Kareliya
    :cvar RU_KK: Republic of Khakasiya
    :cvar RU_KO: Republic of Komi
    :cvar RU_ME: Republic of Mariy El
    :cvar RU_MO: Republic of Mordoviya
    :cvar RU_SA: Republic of Sakha (Yakutiya)
    :cvar RU_SE: Republic of Severnaya Osetiya-Alaniya
    :cvar RU_TA: Republic of Tatarstan
    :cvar RU_TY: Republic of Tyva (Tuva)
    :cvar RU_UD: Udmurtskaya Republic
    :cvar RU_ALT: Altayskiy Administrative Territory
    :cvar RU_KAM: Kamchatskiy Administrative Territory
    :cvar RU_KHA: Khabarovskiy Administrative Territory
    :cvar RU_KDA: Krasnodarskiy Administrative Territory
    :cvar RU_KYA: Krasnoyarskiy Administrative Territory
    :cvar RU_PER: Permskiy Administrative Territory
    :cvar RU_PRI: Primorskiy Administrative Territory
    :cvar RU_STA: Stavropol’skiy Administrative Territory
    :cvar RU_ZAB: Zabaykal’skiy Administrative Territory
    :cvar RU_AMU: Amurskaya Administrative Region
    :cvar RU_ARK: Arkhangel’skaya Administrative Region
    :cvar RU_AST: Astrakhanskaya Administrative Region
    :cvar RU_BEL: Belgorodskaya Administrative Region
    :cvar RU_BRY: Bryanskaya Administrative Region
    :cvar RU_CHE: Chelyabinskaya Administrative Region
    :cvar RU_IRK: Irkutskaya Administrative Region
    :cvar RU_IVA: Ivanovskaya Administrative Region
    :cvar RU_KGD: Kaliningradskaya Administrative Region
    :cvar RU_KLU: Kaluzhskaya Administrative Region
    :cvar RU_KEM: Kemerovskaya Administrative Region
    :cvar RU_KIR: Kirovskaya Administrative Region
    :cvar RU_KOS: Kostromskaya Administrative Region
    :cvar RU_KGN: Kurganskaya Administrative Region
    :cvar RU_KRS: Kurskaya Administrative Region
    :cvar RU_LEN: Leningradskaya Administrative Region
    :cvar RU_LIP: Lipetskaya Administrative Region
    :cvar RU_MAG: Magadanskaya Administrative Region
    :cvar RU_MOS: Moskovskaya Administrative Region
    :cvar RU_MUR: Murmanskaya Administrative Region
    :cvar RU_NIZ: Nizhegorodskaya Administrative Region
    :cvar RU_NGR: Novgorodskaya Administrative Region
    :cvar RU_NVS: Novosibirskaya Administrative Region
    :cvar RU_OMS: Omskaya Administrative Region
    :cvar RU_ORE: Orenburgskaya Administrative Region
    :cvar RU_ORL: Orlovskaya Administrative Region
    :cvar RU_PNZ: Penzenskaya Administrative Region
    :cvar RU_PSK: Pskovskaya Administrative Region
    :cvar RU_ROS: Rostovskaya Administrative Region
    :cvar RU_RYA: Ryazanskaya Administrative Region
    :cvar RU_SAK: Sakhalinskaya Administrative Region
    :cvar RU_SAM: Samarskaya Administrative Region
    :cvar RU_SAR: Saratovskaya Administrative Region
    :cvar RU_SMO: Smolenskaya Administrative Region
    :cvar RU_SVE: Sverdlovskaya Administrative Region
    :cvar RU_TAM: Tambovskaya Administrative Region
    :cvar RU_TOM: Tomskaya Administrative Region
    :cvar RU_TUL: Tul’skaya Administrative Region
    :cvar RU_TVE: Tverskaya Administrative Region
    :cvar RU_TYU: Tyumenskaya Administrative Region
    :cvar RU_ULY: Ul’yanovskaya Administrative Region
    :cvar RU_VLA: Vladimirskaya Administrative Region
    :cvar RU_VGG: Volgogradskaya Administrative Region
    :cvar RU_VLG: Vologodskaya Administrative Region
    :cvar RU_VOR: Voronezhskaya Administrative Region
    :cvar RU_YAR: Yaroslavskaya Administrative Region
    :cvar RU_MOW: Moskva City
    :cvar RU_SPE: Sankt-Peterburg City
    :cvar RU_YEV: Yevreyskaya Autonomous Administrative Region
    :cvar RU_CHU: Chukotskiy Autonomous District
    :cvar RU_KHM: Khanty-Mansiyskiy Autonomous District
    :cvar RU_NEN: Nenetskiy Autonomous District
    :cvar RU_YAN: Yamalo-Nenetskiy Autonomous District
    :cvar US_AK: Alaska
    :cvar US_AL: Alabama
    :cvar US_AR: Arkansas
    :cvar US_AZ: Arizona
    :cvar US_CA: California
    :cvar US_CO: Colorado
    :cvar US_CT: Connecticut
    :cvar US_DC: District of Columbia
    :cvar US_DE: Delaware
    :cvar US_FL: Florida
    :cvar US_GA: Georgia
    :cvar US_HI: Hawaii
    :cvar US_IA: Iowa
    :cvar US_ID: Idaho
    :cvar US_IL: Illinois
    :cvar US_IN: Indiana
    :cvar US_KS: Kansas
    :cvar US_KY: Kentucky
    :cvar US_LA: Louisiana
    :cvar US_MA: Massachusetts
    :cvar US_MD: Maryland
    :cvar US_ME: Maine
    :cvar US_MI: Michigan
    :cvar US_MN: Minnesota
    :cvar US_MO: Missouri
    :cvar US_MS: Mississippi
    :cvar US_MT: Montana
    :cvar US_NC: North Carolina
    :cvar US_ND: North Dakota
    :cvar US_NE: Nebraska
    :cvar US_NH: New Hampshire
    :cvar US_NJ: New Jersey
    :cvar US_NM: New Mexico
    :cvar US_NV: Nevada
    :cvar US_NY: New York
    :cvar US_OH: Ohio
    :cvar US_OK: Oklahoma
    :cvar US_OR: Oregon
    :cvar US_PA: Pennsylvania
    :cvar US_RI: Rhode Island
    :cvar US_SC: South Carolina
    :cvar US_SD: South Dakota
    :cvar US_TN: Tennessee
    :cvar US_TX: Texas
    :cvar US_UT: Utah
    :cvar US_VA: Virginia
    :cvar US_VT: Vermont
    :cvar US_WA: Washington
    :cvar US_WI: Wisconsin
    :cvar US_WV: West Virginia
    :cvar US_WY: Wyoming
    :cvar ECZ: Eurozone Countries geographically within continental
        Europe which use the Euro as their sole currency. At the time of
        writing, this is a synonym for ‘AT BE CY EE FI FR DE ES GR IE IT
        LT LU LV MT NL PT SI SK’ (the official Eurozone 19), plus ‘AD MC
        SM VA ME’ and Kosovo (other Euro-using countries in continental
        Europe). Note some other territories using the Euro, but outside
        continental Europe are excluded from this list, and may need to
        be specified separately. ONLY valid in ONIX 3, and ONLY within
        P.26 – and this use is itself DEPRECATED. Use of an explicit
        list of countries instead of ECZ is strongly encouraged
    :cvar ROW: Rest of world World except as otherwise specified. NOT
        USED in ONIX 3
    :cvar WORLD: World In ONIX 3, may ONLY be used in
        &lt;RegionsIncluded&gt;
    """
    AU_CT = "AU-CT"
    AU_NS = "AU-NS"
    AU_NT = "AU-NT"
    AU_QL = "AU-QL"
    AU_SA = "AU-SA"
    AU_TS = "AU-TS"
    AU_VI = "AU-VI"
    AU_WA = "AU-WA"
    CA_AB = "CA-AB"
    CA_BC = "CA-BC"
    CA_MB = "CA-MB"
    CA_NB = "CA-NB"
    CA_NL = "CA-NL"
    CA_NS = "CA-NS"
    CA_NT = "CA-NT"
    CA_NU = "CA-NU"
    CA_ON = "CA-ON"
    CA_PE = "CA-PE"
    CA_QC = "CA-QC"
    CA_SK = "CA-SK"
    CA_YT = "CA-YT"
    CN_11 = "CN-11"
    CN_12 = "CN-12"
    CN_13 = "CN-13"
    CN_14 = "CN-14"
    CN_15 = "CN-15"
    CN_21 = "CN-21"
    CN_22 = "CN-22"
    CN_23 = "CN-23"
    CN_31 = "CN-31"
    CN_32 = "CN-32"
    CN_33 = "CN-33"
    CN_34 = "CN-34"
    CN_35 = "CN-35"
    CN_36 = "CN-36"
    CN_37 = "CN-37"
    CN_41 = "CN-41"
    CN_42 = "CN-42"
    CN_43 = "CN-43"
    CN_44 = "CN-44"
    CN_45 = "CN-45"
    CN_46 = "CN-46"
    CN_50 = "CN-50"
    CN_51 = "CN-51"
    CN_52 = "CN-52"
    CN_53 = "CN-53"
    CN_54 = "CN-54"
    CN_61 = "CN-61"
    CN_62 = "CN-62"
    CN_63 = "CN-63"
    CN_64 = "CN-64"
    CN_65 = "CN-65"
    CN_71 = "CN-71"
    CN_91 = "CN-91"
    CN_92 = "CN-92"
    ES_CN = "ES-CN"
    FR_H = "FR-H"
    GB_AIR = "GB-AIR"
    GB_APS = "GB-APS"
    GB_CHA = "GB-CHA"
    GB_ENG = "GB-ENG"
    GB_EWS = "GB-EWS"
    GB_IOM = "GB-IOM"
    GB_NIR = "GB-NIR"
    GB_SCT = "GB-SCT"
    GB_WLS = "GB-WLS"
    IE_AIR = "IE-AIR"
    IT_AG = "IT-AG"
    IT_AL = "IT-AL"
    IT_AN = "IT-AN"
    IT_AO = "IT-AO"
    IT_AR = "IT-AR"
    IT_AP = "IT-AP"
    IT_AT = "IT-AT"
    IT_AV = "IT-AV"
    IT_BA = "IT-BA"
    IT_BT = "IT-BT"
    IT_BL = "IT-BL"
    IT_BN = "IT-BN"
    IT_BG = "IT-BG"
    IT_BI = "IT-BI"
    IT_BO = "IT-BO"
    IT_BZ = "IT-BZ"
    IT_BS = "IT-BS"
    IT_BR = "IT-BR"
    IT_CA = "IT-CA"
    IT_CL = "IT-CL"
    IT_CB = "IT-CB"
    IT_CI = "IT-CI"
    IT_CE = "IT-CE"
    IT_CT = "IT-CT"
    IT_CZ = "IT-CZ"
    IT_CH = "IT-CH"
    IT_CO = "IT-CO"
    IT_CS = "IT-CS"
    IT_CR = "IT-CR"
    IT_KR = "IT-KR"
    IT_CN = "IT-CN"
    IT_EN = "IT-EN"
    IT_FM = "IT-FM"
    IT_FE = "IT-FE"
    IT_FI = "IT-FI"
    IT_FG = "IT-FG"
    IT_FC = "IT-FC"
    IT_FR = "IT-FR"
    IT_GE = "IT-GE"
    IT_GO = "IT-GO"
    IT_GR = "IT-GR"
    IT_IM = "IT-IM"
    IT_IS = "IT-IS"
    IT_SP = "IT-SP"
    IT_AQ = "IT-AQ"
    IT_LT = "IT-LT"
    IT_LE = "IT-LE"
    IT_LC = "IT-LC"
    IT_LI = "IT-LI"
    IT_LO = "IT-LO"
    IT_LU = "IT-LU"
    IT_MC = "IT-MC"
    IT_MN = "IT-MN"
    IT_MS = "IT-MS"
    IT_MT = "IT-MT"
    IT_VS = "IT-VS"
    IT_ME = "IT-ME"
    IT_MI = "IT-MI"
    IT_MO = "IT-MO"
    IT_MB = "IT-MB"
    IT_NA = "IT-NA"
    IT_NO = "IT-NO"
    IT_NU = "IT-NU"
    IT_OG = "IT-OG"
    IT_OT = "IT-OT"
    IT_OR = "IT-OR"
    IT_PD = "IT-PD"
    IT_PA = "IT-PA"
    IT_PR = "IT-PR"
    IT_PV = "IT-PV"
    IT_PG = "IT-PG"
    IT_PU = "IT-PU"
    IT_PE = "IT-PE"
    IT_PC = "IT-PC"
    IT_PI = "IT-PI"
    IT_PT = "IT-PT"
    IT_PN = "IT-PN"
    IT_PZ = "IT-PZ"
    IT_PO = "IT-PO"
    IT_RG = "IT-RG"
    IT_RA = "IT-RA"
    IT_RC = "IT-RC"
    IT_RE = "IT-RE"
    IT_RI = "IT-RI"
    IT_RN = "IT-RN"
    IT_RM = "IT-RM"
    IT_RO = "IT-RO"
    IT_SA = "IT-SA"
    IT_SS = "IT-SS"
    IT_SV = "IT-SV"
    IT_SI = "IT-SI"
    IT_SR = "IT-SR"
    IT_SO = "IT-SO"
    IT_TA = "IT-TA"
    IT_TE = "IT-TE"
    IT_TR = "IT-TR"
    IT_TO = "IT-TO"
    IT_TP = "IT-TP"
    IT_TN = "IT-TN"
    IT_TV = "IT-TV"
    IT_TS = "IT-TS"
    IT_UD = "IT-UD"
    IT_VA = "IT-VA"
    IT_VE = "IT-VE"
    IT_VB = "IT-VB"
    IT_VC = "IT-VC"
    IT_VR = "IT-VR"
    IT_VV = "IT-VV"
    IT_VI = "IT-VI"
    IT_VT = "IT-VT"
    RS_KM = "RS-KM"
    RS_VO = "RS-VO"
    RU_AD = "RU-AD"
    RU_AL = "RU-AL"
    RU_BA = "RU-BA"
    RU_BU = "RU-BU"
    RU_CE = "RU-CE"
    RU_CU = "RU-CU"
    RU_DA = "RU-DA"
    RU_IN = "RU-IN"
    RU_KB = "RU-KB"
    RU_KL = "RU-KL"
    RU_KC = "RU-KC"
    RU_KR = "RU-KR"
    RU_KK = "RU-KK"
    RU_KO = "RU-KO"
    RU_ME = "RU-ME"
    RU_MO = "RU-MO"
    RU_SA = "RU-SA"
    RU_SE = "RU-SE"
    RU_TA = "RU-TA"
    RU_TY = "RU-TY"
    RU_UD = "RU-UD"
    RU_ALT = "RU-ALT"
    RU_KAM = "RU-KAM"
    RU_KHA = "RU-KHA"
    RU_KDA = "RU-KDA"
    RU_KYA = "RU-KYA"
    RU_PER = "RU-PER"
    RU_PRI = "RU-PRI"
    RU_STA = "RU-STA"
    RU_ZAB = "RU-ZAB"
    RU_AMU = "RU-AMU"
    RU_ARK = "RU-ARK"
    RU_AST = "RU-AST"
    RU_BEL = "RU-BEL"
    RU_BRY = "RU-BRY"
    RU_CHE = "RU-CHE"
    RU_IRK = "RU-IRK"
    RU_IVA = "RU-IVA"
    RU_KGD = "RU-KGD"
    RU_KLU = "RU-KLU"
    RU_KEM = "RU-KEM"
    RU_KIR = "RU-KIR"
    RU_KOS = "RU-KOS"
    RU_KGN = "RU-KGN"
    RU_KRS = "RU-KRS"
    RU_LEN = "RU-LEN"
    RU_LIP = "RU-LIP"
    RU_MAG = "RU-MAG"
    RU_MOS = "RU-MOS"
    RU_MUR = "RU-MUR"
    RU_NIZ = "RU-NIZ"
    RU_NGR = "RU-NGR"
    RU_NVS = "RU-NVS"
    RU_OMS = "RU-OMS"
    RU_ORE = "RU-ORE"
    RU_ORL = "RU-ORL"
    RU_PNZ = "RU-PNZ"
    RU_PSK = "RU-PSK"
    RU_ROS = "RU-ROS"
    RU_RYA = "RU-RYA"
    RU_SAK = "RU-SAK"
    RU_SAM = "RU-SAM"
    RU_SAR = "RU-SAR"
    RU_SMO = "RU-SMO"
    RU_SVE = "RU-SVE"
    RU_TAM = "RU-TAM"
    RU_TOM = "RU-TOM"
    RU_TUL = "RU-TUL"
    RU_TVE = "RU-TVE"
    RU_TYU = "RU-TYU"
    RU_ULY = "RU-ULY"
    RU_VLA = "RU-VLA"
    RU_VGG = "RU-VGG"
    RU_VLG = "RU-VLG"
    RU_VOR = "RU-VOR"
    RU_YAR = "RU-YAR"
    RU_MOW = "RU-MOW"
    RU_SPE = "RU-SPE"
    RU_YEV = "RU-YEV"
    RU_CHU = "RU-CHU"
    RU_KHM = "RU-KHM"
    RU_NEN = "RU-NEN"
    RU_YAN = "RU-YAN"
    US_AK = "US-AK"
    US_AL = "US-AL"
    US_AR = "US-AR"
    US_AZ = "US-AZ"
    US_CA = "US-CA"
    US_CO = "US-CO"
    US_CT = "US-CT"
    US_DC = "US-DC"
    US_DE = "US-DE"
    US_FL = "US-FL"
    US_GA = "US-GA"
    US_HI = "US-HI"
    US_IA = "US-IA"
    US_ID = "US-ID"
    US_IL = "US-IL"
    US_IN = "US-IN"
    US_KS = "US-KS"
    US_KY = "US-KY"
    US_LA = "US-LA"
    US_MA = "US-MA"
    US_MD = "US-MD"
    US_ME = "US-ME"
    US_MI = "US-MI"
    US_MN = "US-MN"
    US_MO = "US-MO"
    US_MS = "US-MS"
    US_MT = "US-MT"
    US_NC = "US-NC"
    US_ND = "US-ND"
    US_NE = "US-NE"
    US_NH = "US-NH"
    US_NJ = "US-NJ"
    US_NM = "US-NM"
    US_NV = "US-NV"
    US_NY = "US-NY"
    US_OH = "US-OH"
    US_OK = "US-OK"
    US_OR = "US-OR"
    US_PA = "US-PA"
    US_RI = "US-RI"
    US_SC = "US-SC"
    US_SD = "US-SD"
    US_TN = "US-TN"
    US_TX = "US-TX"
    US_UT = "US-UT"
    US_VA = "US-VA"
    US_VT = "US-VT"
    US_WA = "US-WA"
    US_WI = "US-WI"
    US_WV = "US-WV"
    US_WY = "US-WY"
    ECZ = "ECZ"
    ROW = "ROW"
    WORLD = "WORLD"


class List5(Enum):
    """
    Product identifier type code.

    :cvar VALUE_01: Proprietary For example, a publisher’s or
        wholesaler’s product number. Note that &lt;IDTypeName&gt; is
        required with proprietary identifiers
    :cvar VALUE_02: ISBN-10 International Standard Book Number,
        pre-2007, unhyphenated (10 characters) – now DEPRECATED in ONIX
        for Books, except where providing historical information for
        compatibility with legacy systems. It should only be used in
        relation to products published before 2007 – when ISBN-13
        superseded it – and should never be used as the ONLY identifier
        (it should always be accompanied by the correct GTIN-13 /
        ISBN-13)
    :cvar VALUE_03: GTIN-13 GS1 Global Trade Item Number, formerly known
        as EAN article number (13 digits)
    :cvar VALUE_04: UPC UPC product number (12 digits)
    :cvar VALUE_05: ISMN-10 International Standard Music Number (M plus
        nine digits). Pre-2008 – now DEPRECATED in ONIX for Books,
        except where providing historical information for compatibility
        with legacy systems. It should only be used in relation to
        products published before 2008 – when ISMN-13 superseded it –
        and should never be used as the ONLY identifier (it should
        always be accompanied by the correct ISMN-13)
    :cvar VALUE_06: DOI Digital Object Identifier (variable length and
        character set)
    :cvar VALUE_13: LCCN Library of Congress Control Number (12
        characters, alphanumeric)
    :cvar VALUE_14: GTIN-14 GS1 Global Trade Item Number (14 digits)
    :cvar VALUE_15: ISBN-13 International Standard Book Number, from
        2007, unhyphenated (13 digits starting 978 or 9791–9799)
    :cvar VALUE_17: Legal deposit number The number assigned to a
        publication as part of a national legal deposit process
    :cvar VALUE_22: URN Uniform Resource Name: note that in trade
        applications an ISBN must be sent as a GTIN-13 and, where
        required, as an ISBN-13 – it should not be sent as a URN
    :cvar VALUE_23: OCLC number A unique number assigned to a
        bibliographic item by OCLC
    :cvar VALUE_24: Co-publisher’s ISBN-13 An ISBN-13 assigned by a co-
        publisher. The ‘main’ ISBN sent with ID type code 03 and/or 15
        should always be the ISBN that is used for ordering from the
        supplier identified in Supply Detail. However, ISBN rules allow
        a co-published title to carry more than one ISBN. The co-
        publisher should be identified in an instance of the
        &lt;Publisher&gt; composite, with the applicable
        &lt;PublishingRole&gt; code
    :cvar VALUE_25: ISMN-13 International Standard Music Number, from
        2008 (13-digit number starting 9790)
    :cvar VALUE_26: ISBN-A Actionable ISBN, in fact a special DOI
        incorporating the ISBN-13 within the DOI syntax. Begins
        ‘10.978.’ or ‘10.979.’ and includes a / character between the
        registrant element (publisher prefix) and publication element of
        the ISBN, eg 10.978.000/1234567. Note the ISBN-A should always
        be accompanied by the ISBN itself, using codes 03 and/or 15
    :cvar VALUE_27: JP e-code E-publication identifier controlled by
        JPOIID’s Committee for Research and Management of Electronic
        Publishing Codes
    :cvar VALUE_28: OLCC number Unique number assigned by the Chinese
        Online Library Cataloging Center (see http://olcc.nlc.gov.cn)
    :cvar VALUE_29: JP Magazine ID Japanese magazine identifier, similar
        in scope to ISSN but identifying a specific issue of a serial
        publication. Five digits to identify the periodical, plus a
        hyphen and two digits to identify the issue
    :cvar VALUE_30: UPC12+5 Used only with comic books and other
        products which use the UPC extension to identify individual
        issues or products. Do not use where the UPC12 itself identifies
        the specific product, irrespective of any 5-digit extension –
        use code 04 instead
    :cvar VALUE_31: BNF Control number Numéro de la notice
        bibliographique BNF
    :cvar VALUE_35: ARK Archival Resource Key, as a URL (including the
        address of the ARK resolver provided by eg a national library)
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_17 = "17"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_35 = "35"


class List50(Enum):
    """
    Measure unit code.

    :cvar CM: Centimeters Millimeters are the preferred metric unit of
        length
    :cvar GR: Grams
    :cvar IN: Inches (US)
    :cvar KG: Kilograms Grams are the preferred metric unit of weight
    :cvar LB: Pounds (US)
    :cvar MM: Millimeters
    :cvar OZ: Ounces (US)
    :cvar PX: Pixels
    """
    CM = "cm"
    GR = "gr"
    IN = "in"
    KG = "kg"
    LB = "lb"
    MM = "mm"
    OZ = "oz"
    PX = "px"


class List51(Enum):
    """
    Product relation code.

    :cvar VALUE_00: Unspecified &lt;Product&gt; is related to
        &lt;RelatedProduct&gt; in a way that cannot be specified by
        another code value
    :cvar VALUE_01: Includes &lt;Product&gt; includes
        &lt;RelatedProduct&gt;
    :cvar VALUE_02: Is part of &lt;Product&gt; is part of
        &lt;RelatedProduct&gt;: use for ‘also available as part of’
    :cvar VALUE_03: Replaces &lt;Product&gt; replaces, or is new edition
        of, &lt;RelatedProduct&gt;
    :cvar VALUE_05: Replaced by &lt;Product&gt; is replaced by, or has
        new edition, &lt;RelatedProduct&gt; (reciprocal of code 03)
    :cvar VALUE_06: Alternative format &lt;Product&gt; is available in
        an alternative format as &lt;RelatedProduct&gt; – indicates an
        alternative format of the same content which is or may be
        available
    :cvar VALUE_07: Has ancillary product &lt;Product&gt; has an
        ancillary or supplementary product &lt;RelatedProduct&gt;
    :cvar VALUE_08: Is ancillary to &lt;Product&gt; is ancillary or
        supplementary to &lt;RelatedProduct&gt;
    :cvar VALUE_09: Is remaindered as &lt;Product&gt; is remaindered as
        &lt;RelatedProduct&gt;, when a remainder merchant assigns its
        own identifier to the product
    :cvar VALUE_10: Is remainder of &lt;Product&gt; was originally sold
        as &lt;RelatedProduct&gt;, indicating the publisher’s original
        identifier for a title which is offered as a remainder under a
        different identifier (reciprocal of code 09)
    :cvar VALUE_11: Is other-language version of &lt;Product&gt; is an
        other-language version of &lt;RelatedProduct&gt;
    :cvar VALUE_12: Publisher’s suggested alternative &lt;Product&gt;
        has a publisher’s suggested alternative &lt;RelatedProduct&gt;,
        which does not, however, carry the same content (cf 05 and 06)
    :cvar VALUE_13: Epublication based on (print product)
        &lt;Product&gt; is an epublication based on printed product
        &lt;RelatedProduct&gt;
    :cvar VALUE_14: Epublication is distributed as &lt;Product&gt; is an
        epublication ‘rendered’ as &lt;RelatedProduct&gt;: use in ONIX
        2.1 only when the &lt;Product&gt; record describes a package of
        electronic content which is available in multiple ‘renderings’
        (coded 000 in &lt;EpubTypeCode&gt;): NOT USED in ONIX 3.0
    :cvar VALUE_15: Epublication is a rendering of &lt;Product&gt; is a
        ‘rendering’ of an epublication &lt;RelatedProduct&gt;: use in
        ONIX 2.1 only when the &lt;Product&gt; record describes a
        specific rendering of an epublication content package, to
        identify the package: NOT USED in ONIX 3.0
    :cvar VALUE_16: POD replacement for &lt;Product&gt; is a POD
        replacement for &lt;RelatedProduct&gt;. &lt;RelatedProduct&gt;
        is an out-of-print product replaced by a print-on-demand version
        under a new ISBN
    :cvar VALUE_17: Replaced by POD &lt;Product&gt; is replaced by POD
        &lt;RelatedProduct&gt;. &lt;RelatedProduct&gt; is a print-on-
        demand replacement, under a new ISBN, for an out-of-print
        &lt;Product&gt; (reciprocal of code 16)
    :cvar VALUE_18: Is special edition of &lt;Product&gt; is a special
        edition of &lt;RelatedProduct&gt;. Used for a special edition
        (German: Sonderausgabe) with different cover, binding, premium
        content etc – more than ‘alternative format’ – which may be
        available in limited quantity and for a limited time
    :cvar VALUE_19: Has special edition &lt;Product&gt; has a special
        edition &lt;RelatedProduct&gt; (reciprocal of code 18)
    :cvar VALUE_20: Is prebound edition of &lt;Product&gt; is a prebound
        edition of &lt;RelatedProduct&gt; (in the US, a prebound edition
        is ‘a book that was previously bound and has been rebound with a
        library quality hardcover binding. In almost all commercial
        cases, the book in question began as a paperback.’)
    :cvar VALUE_21: Is original of prebound edition &lt;Product&gt; is
        the regular edition of which &lt;RelatedProduct&gt; is a
        prebound edition
    :cvar VALUE_22: Product by same author &lt;Product&gt; and
        &lt;RelatedProduct&gt; have a common author
    :cvar VALUE_23: Similar product &lt;RelatedProduct&gt; is another
        product that is suggested as similar to &lt;Product&gt; (‘if you
        liked &lt;Product&gt;, you may also like
        &lt;RelatedProduct&gt;’, or vice versa)
    :cvar VALUE_24: Is facsimile of &lt;Product&gt; is a facsimile
        edition of &lt;RelatedProduct&gt;
    :cvar VALUE_25: Is original of facsimile &lt;Product&gt; is the
        original edition from which a facsimile edition
        &lt;RelatedProduct&gt; is taken (reciprocal of code 25)
    :cvar VALUE_26: Is license for &lt;Product&gt; is a license for a
        digital &lt;RelatedProduct&gt;, traded or supplied separately
    :cvar VALUE_27: Electronic version available as
        &lt;RelatedProduct&gt; is an electronic version of print
        &lt;Product&gt; (reciprocal of code 13)
    :cvar VALUE_28: Enhanced version available as &lt;RelatedProduct&gt;
        is an ‘enhanced’ version of &lt;Product&gt;, with additional
        content. Typically used to link an enhanced e-book to its
        original ‘unenhanced’ equivalent, but not specifically limited
        to linking e-books – for example, may be used to link
        illustrated and non-illustrated print books. &lt;Product&gt; and
        &lt;RelatedProduct&gt; should share the same &lt;ProductForm&gt;
    :cvar VALUE_29: Basic version available as &lt;RelatedProduct&gt; is
        a basic version of &lt;Product&gt; (reciprocal of code 28).
        &lt;Product&gt; and &lt;RelatedProduct&gt; should share the same
        &lt;ProductForm&gt;
    :cvar VALUE_30: Product in same collection &lt;RelatedProduct&gt;
        and &lt;Product&gt; are part of the same collection (eg two
        products in same series or set)
    :cvar VALUE_31: Has alternative in a different market sector
        &lt;RelatedProduct&gt; is an alternative product in another
        sector (of the same geographical market). Indicates an
        alternative that carries the same content, but available to a
        different set of customers, as one or both products are
        retailer-, channel- or market sector-specific
    :cvar VALUE_32: Has equivalent intended for a different market
        &lt;RelatedProduct&gt; is an equivalent product, often intended
        for another (geographical) market. Indicates an alternative that
        carries essentially the same content, though slightly adapted
        for local circumstances (as opposed to a translation – use code
        11)
    :cvar VALUE_33: Has alternative intended for different market
        &lt;RelatedProduct&gt; is an alternative product, often intended
        for another (geographical) market. Indicates the content of the
        alternative is identical in all respects
    :cvar VALUE_34: Cites &lt;Product&gt; cites &lt;RelatedProduct&gt;
    :cvar VALUE_35: Is cited by &lt;Product&gt; is the object of a
        citation in &lt;RelatedProduct&gt;
    :cvar VALUE_36: Sales expectation Use to give the ISBN of another
        book that had sales (both in terms of copy numbers and customer
        profile) comparable to that the publisher or distributor
        estimates for the product. Use in ONIX 2.1 ONLY
    :cvar VALUE_37: Is signed version of &lt;Product&gt; is a signed
        copy of &lt;RelatedProduct&gt;. Use where signed copies are
        given a distinct product identifier and can be ordered
        separately, but are otherwise identical
    :cvar VALUE_38: Has signed version &lt;Product&gt; is an unsigned
        copy of &lt;RelatedProduct&gt;. Use where signed copies are
        given a distinct product identifier and can be ordered
        separately, but are otherwise identical
    :cvar VALUE_39: Has related student material &lt;Product&gt; is
        intended for teacher use, and the related product is for student
        use
    :cvar VALUE_40: Has related teacher material &lt;Product&gt; is
        intended for student use, and the related product is for teacher
        use
    :cvar VALUE_41: Some content shared with &lt;Product&gt; includes
        some content shared with &lt;RelatedProduct&gt;. Note the shared
        content does not form the whole of either product. Compare with
        the includes / is part of relationship pair, where the shared
        content forms the whole of one of the products, and with the
        alternative format relationship, where the shared content forms
        the whole of both products
    :cvar VALUE_42: Is later edition of first edition &lt;Product&gt; is
        a later edition of &lt;RelatedProduct&gt;, where the related
        product is the first edition
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_36 = "36"
    VALUE_37 = "37"
    VALUE_38 = "38"
    VALUE_39 = "39"
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_42 = "42"


class List52(Enum):
    """
    Supply-to region code.

    :cvar VALUE_004: UK ‘open market’ When the same ISBN is used for
        open market and UK editions
    """
    VALUE_004 = "004"


class List53(Enum):
    """
    Returns conditions code type.

    :cvar VALUE_00: Proprietary As specified in
        &lt;ReturnsCodeTypeName&gt; (ONIX 3.0 only)
    :cvar VALUE_01: French book trade returns conditions code Maintained
        by CLIL (Commission Interprofessionnel du Livre). Returns
        conditions values in &lt;ReturnsCode&gt; should be taken from
        the CLIL list
    :cvar VALUE_02: BISAC Returnable Indicator code Maintained by BISAC:
        Returns conditions values in &lt;ReturnsCode&gt; should be taken
        from List 66
    :cvar VALUE_03: UK book trade returns conditions code NOT CURRENTLY
        USED – BIC has decided that it will not maintain a code list for
        this purpose, since returns conditions are usually at least
        partly based on the trading relationship
    :cvar VALUE_04: ONIX Returns conditions code Returns conditions
        values in &lt;ReturnsCode&gt; should be taken from List 204
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"


class List54(Enum):
    """
    Availability status code.

    :cvar AB: Cancelled Publication abandoned after having been
        announced
    :cvar AD: Available direct from publisher only Apply direct to
        publisher, item not available to trade
    :cvar CS: Availability uncertain Check with customer service
    :cvar EX: No longer stocked by us Wholesaler or vendor only
    :cvar IP: Available In-print and in stock
    :cvar MD: Manufactured on demand May be accompanied by an estimated
        average time to supply
    :cvar NP: Not yet published MUST be accompanied by an expected
        availability date
    :cvar NY: Newly catalogued, not yet in stock Wholesaler or vendor
        only: MUST be accompanied by expected availability date
    :cvar OF: Other format available This format is out of print, but
        another format is available: should be accompanied by an
        identifier for the alternative product
    :cvar OI: Out of stock indefinitely No current plan to reprint
    :cvar OP: Out of print Discontinued, deleted from catalogue
    :cvar OR: Replaced by new edition This edition is out of print, but
        a new edition has been or will soon be published: should be
        accompanied by an identifier for the new edition
    :cvar PP: Publication postponed indefinitely Publication has been
        announced, and subsequently postponed with no new date
    :cvar RF: Refer to another supplier Supply of this item has been
        transferred to another publisher or distributor: should be
        accompanied by an identifier for the new supplier
    :cvar RM: Remaindered
    :cvar RP: Reprinting MUST be accompanied by an expected availability
        date
    :cvar RU: Reprinting, undated Use instead of RP as a last resort,
        only if it is really impossible to give an expected availability
        date
    :cvar TO: Special order This item is not stocked but has to be
        specially ordered from a supplier (eg import item not stocked
        locally): may be accompanied by an estimated average time to
        supply
    :cvar TP: Temporarily out of stock because publisher cannot supply
        Wholesaler or vendor only
    :cvar TU: Temporarily unavailable MUST be accompanied by an expected
        availability date
    :cvar UR: Unavailable, awaiting reissue The item is out of stock but
        will be reissued under the same ISBN: MUST be accompanied by an
        expected availability date and by the reissue date in the
        &lt;Reissue&gt; composite. See notes on the &lt;Reissue&gt;
        composite for details on treatment of availability status during
        reissue
    :cvar WR: Will be remaindered as of (date) MUST be accompanied by
        the remainder date
    :cvar WS: Withdrawn from sale Typically, withdrawn indefinitely for
        legal reasons
    """
    AB = "AB"
    AD = "AD"
    CS = "CS"
    EX = "EX"
    IP = "IP"
    MD = "MD"
    NP = "NP"
    NY = "NY"
    OF = "OF"
    OI = "OI"
    OP = "OP"
    OR = "OR"
    PP = "PP"
    RF = "RF"
    RM = "RM"
    RP = "RP"
    RU = "RU"
    TO = "TO"
    TP = "TP"
    TU = "TU"
    UR = "UR"
    WR = "WR"
    WS = "WS"


class List55(Enum):
    """
    Date format.

    :cvar VALUE_00: YYYYMMDD Year month day (default)
    :cvar VALUE_01: YYYYMM Year and month
    :cvar VALUE_02: YYYYWW Year and week number
    :cvar VALUE_03: YYYYQ Year and quarter (Q = 1, 2, 3, 4, with 1 = Jan
        to Mar)
    :cvar VALUE_04: YYYYS Year and season (S = 1, 2, 3, 4, with 1 =
        ‘Spring’)
    :cvar VALUE_05: YYYY Year
    :cvar VALUE_06: YYYYMMDDYYYYMMDD Spread of exact dates
    :cvar VALUE_07: YYYYMMYYYYMM Spread of months
    :cvar VALUE_08: YYYYWWYYYYWW Spread of week numbers
    :cvar VALUE_09: YYYYQYYYYQ Spread of quarters
    :cvar VALUE_10: YYYYSYYYYS Spread of seasons
    :cvar VALUE_11: YYYYYYYY Spread of years
    :cvar VALUE_12: Text string For complex, approximate or uncertain
        dates
    :cvar VALUE_13: YYYYMMDDThhmm Exact time. Use ONLY when exact times
        with hour/minute precision are relevant. By default, time is
        local. Alternatively, the time may be suffixed with an optional
        ‘Z’ for UTC times, or with ‘+’ or ‘-’ and an hhmm timezone
        offset from UTC. Times without a timezone are ‘rolling’ local
        times, times qualified with a timezone (using Z, + or -) specify
        a particular instant in time
    :cvar VALUE_14: YYYYMMDDThhmmss Exact time. Use ONLY when exact
        times with second precision are relevant. By default, time is
        local. Alternatively, the time may be suffixed with an optional
        ‘Z’ for UTC times, or with ‘+’ or ‘-’ and an hhmm timezone
        offset from UTC. Times without a timezone are ‘rolling’ local
        times, times qualified with a timezone (using Z, + or -) specify
        a particular instant in time
    :cvar VALUE_20: YYYYMMDD (H) Year month day (Hijri calendar)
    :cvar VALUE_21: YYYYMM (H) Year and month (Hijri calendar)
    :cvar VALUE_25: YYYY (H) Year (Hijri calendar)
    :cvar VALUE_32: Text string (H) For complex, approximate or
        uncertain dates (Hijri calendar), text would usually be in
        Arabic script
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_25 = "25"
    VALUE_32 = "32"


class List56(Enum):
    """
    Audience restriction flag.

    :cvar R: Restrictions apply, see note
    :cvar X: Indiziert Indexed for the German market – in Deutschland
        indiziert
    """
    R = "R"
    X = "X"


class List57(Enum):
    """
    Unpriced item type code.

    :cvar VALUE_01: Free of charge
    :cvar VALUE_02: Price to be announced
    :cvar VALUE_03: Not sold separately Not sold separately at retail
    :cvar VALUE_04: Contact supplier May be used for books that do not
        carry a recommended retail price; when goods can only be ordered
        ‘in person’ from a sales representative; when an ONIX file is
        ‘broadcast’ rather than sent one-to-one to a single trading
        partner; or for digital products offered on subscription or with
        pricing which is too complex to specify in ONIX
    :cvar VALUE_05: Not sold as set When a collection that is not sold
        as a set nevertheless has its own ONIX record
    :cvar VALUE_06: Revenue share Unpriced, but available via a pre-
        determined revenue share agreement
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"


class List58(Enum):
    """
    Price type code.

    :cvar VALUE_01: RRP excluding tax RRP excluding any sales tax or
        value-added tax
    :cvar VALUE_02: RRP including tax RRP including sales or value-added
        tax if applicable
    :cvar VALUE_03: Fixed retail price excluding tax In countries where
        retail price maintenance applies by law to certain products: not
        used in USA
    :cvar VALUE_04: Fixed retail price including tax In countries where
        retail price maintenance applies by law to certain products: not
        used in USA
    :cvar VALUE_05: Supplier’s net price excluding tax Unit price
        charged by supplier to reseller excluding any sales tax or
        value-added tax: goods for retail sale
    :cvar VALUE_06: Supplier’s net price excluding tax: rental goods
        Unit price charged by supplier to reseller / rental outlet,
        excluding any sales tax or value-added tax: goods for rental
        (used for video and DVD)
    :cvar VALUE_07: Supplier’s net price including tax Unit price
        charged by supplier to reseller including any sales tax or
        value-added tax if applicable: goods for retail sale
    :cvar VALUE_08: Supplier’s alternative net price excluding tax Unit
        price charged by supplier to a specified class of reseller
        excluding any sales tax or value-added tax: goods for retail
        sale (this value is for use only in countries, eg Finland, where
        trade practice requires two different net prices to be listed
        for different classes of resellers, and where national
        guidelines specify how the code should be used)
    :cvar VALUE_09: Supplier’s alternative net price including tax Unit
        price charged by supplier to a specified class of reseller
        including any sales tax or value-added tax: goods for retail
        sale (this value is for use only in countries, eg Finland, where
        trade practice requires two different net prices to be listed
        for different classes of resellers, and where national
        guidelines specify how the code should be used)
    :cvar VALUE_11: Special sale RRP excluding tax Special sale RRP
        excluding any sales tax or value-added tax. Note ‘special sales’
        are sales where terms and conditions are different from normal
        trade sales, when for example products that are normally sold on
        a sale-or-return basis are sold on firm-sale terms, where a
        particular product is tailored for a specific retail outlet
        (often termed a ‘premium’ product), or where other specific
        conditions or qualiifications apply. Further details of the
        modified terms and conditions should be given in
        &lt;PriceTypeDescription&gt;
    :cvar VALUE_12: Special sale RRP including tax Special sale RRP
        including sales or value-added tax if applicable
    :cvar VALUE_13: Special sale fixed retail price excluding tax In
        countries where retail price maintenance applies by law to
        certain products: not used in USA
    :cvar VALUE_14: Special sale fixed retail price including tax In
        countries where retail price maintenance applies by law to
        certain products: not used in USA
    :cvar VALUE_15: Supplier’s net price for special sale excluding tax
        Unit price charged by supplier to reseller for special sale
        excluding any sales tax or value-added tax
    :cvar VALUE_17: Supplier’s net price for special sale including tax
        Unit price charged by supplier to reseller for special sale
        including any sales tax or value-added tax
    :cvar VALUE_21: Pre-publication RRP excluding tax Pre-publication
        RRP excluding any sales tax or value-added tax. Use where RRP
        for pre-orders is different from post-publication RRP
    :cvar VALUE_22: Pre-publication RRP including tax Pre-publication
        RRP including sales or value-added tax if applicable. Use where
        RRP for pre-orders is different from post-publication RRP
    :cvar VALUE_23: Pre-publication fixed retail price excluding tax In
        countries where retail price maintenance applies by law to
        certain products: not used in USA
    :cvar VALUE_24: Pre-publication fixed retail price including tax In
        countries where retail price maintenance applies by law to
        certain products: not used in USA
    :cvar VALUE_25: Supplier’s pre-publication net price excluding tax
        Unit price charged by supplier to reseller pre-publication
        excluding any sales tax or value-added tax
    :cvar VALUE_27: Supplier’s pre-publication net price including tax
        Unit price charged by supplier to reseller pre-publication
        including any sales tax or value-added tax
    :cvar VALUE_31: Freight-pass-through RRP excluding tax In the US,
        books are sometimes supplied on ‘freight-pass-through’ terms,
        where a price that is different from the RRP is used as the
        basis for calculating the supplier’s charge to a reseller. To
        make it clear when such terms are being invoked, code 31 is used
        instead of code 01 to indicate the RRP. Code 32 is used for the
        ‘billing price’
    :cvar VALUE_32: Freight-pass-through billing price excluding tax
        When freight-pass-through terms apply, the price on which the
        supplier’s charge to a reseller is calculated, ie the price to
        which trade discount terms are applied. See also code 31
    :cvar VALUE_33: Importer’s Fixed retail price excluding tax In
        countries where retail price maintenance applies by law to
        certain products, but the price is set by the importer or local
        sales agent, not the foreign publisher. In France, ‘prix
        catalogue éditeur étranger’
    :cvar VALUE_34: Importer’s Fixed retail price including tax In
        countries where retail price maintenance applies by law to
        certain products, but the price is set by the importer or local
        sales agent, not the foreign publisher. In France, ‘prix
        catalogue éditeur étranger’
    :cvar VALUE_41: Publishers retail price excluding tax For a product
        supplied on agency terms, the retail price set by the publisher,
        excluding any sales tax or value-added tax
    :cvar VALUE_42: Publishers retail price including tax For a product
        supplied on agency terms, the retail price set by the publisher,
        including sales or value-added tax if applicable
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_17 = "17"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_27 = "27"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_41 = "41"
    VALUE_42 = "42"


class List59(Enum):
    """
    Price type qualifier.

    :cvar VALUE_00: Unqualified price Price applies to all customers
        that do not fall within any other group with a specified group-
        specific qualified price
    :cvar VALUE_01: Member/subscriber price Price applies to a
        designated group membership
    :cvar VALUE_02: Export price Price applies to sales outside the
        territory in which the supplier is located
    :cvar VALUE_03: Reduced price applicable when the item is purchased
        as part of a set (or series, or collection) Use in cases where
        there is no combined price, but a lower price is offered for
        each part if the whole set / series / collection is purchased
        (either at one time, as part of a continuing commitment, or in a
        single purchase)
    :cvar VALUE_04: Voucher price In the Netherlands (or any other
        market where similar arrangements exist): a reduced fixed price
        available for a limited time on presentation of a voucher or
        coupon published in a specified medium, eg a newspaper. Should
        be accompanied by Price Type code 13 and additional detail in
        &lt;PriceTypeDescription&gt;, and by validity dates in
        &lt;PriceEffectiveFrom&gt; and &lt;PriceEffectiveUntil&gt; (ONIX
        2.1) or in the &lt;PriceDate&gt; composite (ONIX 3.0)
    :cvar VALUE_05: Consumer price Price for individual consumer sale
        only
    :cvar VALUE_06: Corporate / Library / Education price Price for sale
        to libraries or other corporate or institutional customers
    :cvar VALUE_07: Reservation order price Price valid for a specified
        period prior to publication. Orders placed prior to the end of
        the period are guaranteed to be delivered to the retailer before
        the nominal publication date. The price may or may not be
        different from the ‘normal’ price, which carries no such
        delivery guarantee. Must be accompanied by a
        &lt;PriceEffectiveUntil&gt; date (or equivalent
        &lt;PriceDate&gt; composite in ONIX 3), and should also be
        accompanied by a ‘normal’ price
    :cvar VALUE_08: Promotional offer price Temporary ‘Special offer’
        price. Must be accompanied by &lt;PriceEffectiveFrom&gt; and
        &lt;PriceEffectiveUntil&gt; dates (or equivalent
        &lt;PriceDate&gt; composites in ONIX 3), and may also be
        accompanied by a ‘normal’ price
    :cvar VALUE_09: Linked price Price requires purchase with, or proof
        of ownership of another product. Further details of purchase or
        ownership requirements must be given in
        &lt;PriceTypeDescription&gt;
    :cvar VALUE_10: Library price Price for sale only to libraries
        (including public, school and academic libraries)
    :cvar VALUE_11: Education price Price for sale only to educational
        institutions (including school and academic libraries),
        educational buying consortia, government and local government
        bodies purchasing for use in education
    :cvar VALUE_12: Corporate price Price for sale to corporate
        customers only
    :cvar VALUE_13: Subscription service price Price for sale to
        organisations or services offering consumers subscription access
        to a library of books
    :cvar VALUE_14: School library price Price for primary and secondary
        education
    :cvar VALUE_15: Academic library price Price for higher education
        and scholarly institutions
    :cvar VALUE_16: Public library price
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"


class List6(Enum):
    """
    Barcode indicator.

    :cvar VALUE_00: Not barcoded
    :cvar VALUE_01: Barcoded, scheme unspecified
    :cvar VALUE_02: EAN13 Position unspecified
    :cvar VALUE_03: EAN13+5 (US dollar price encoded) Position
        unspecified
    :cvar VALUE_04: UPC12 Type and position unspecified. DEPRECATED: if
        possible, use more specific values below
    :cvar VALUE_05: UPC12+5 Type and position unspecified. DEPRECATED:
        if possible, use more specific values below
    :cvar VALUE_06: UPC12 (item-specific) AKA item/price: position
        unspecified
    :cvar VALUE_07: UPC12+5 (item-specific) AKA item/price: position
        unspecified
    :cvar VALUE_08: UPC12 (price-point) AKA price/item: position
        unspecified
    :cvar VALUE_09: UPC12+5 (price-point) AKA price/item: position
        unspecified
    :cvar VALUE_10: EAN13 on cover 4 ‘Cover 4’ is defined as the back
        cover of a book
    :cvar VALUE_11: EAN13+5 on cover 4 (US dollar price encoded) ‘Cover
        4’ is defined as the back cover of a book
    :cvar VALUE_12: UPC12 (item-specific) on cover 4 AKA item/price;
        ‘cover 4’ is defined as the back cover of a book
    :cvar VALUE_13: UPC12+5 (item-specific) on cover 4 AKA item/price;
        ‘cover 4’ is defined as the back cover of a book
    :cvar VALUE_14: UPC12 (price-point) on cover 4 AKA price/item;
        ‘cover 4’ is defined as the back cover of a book
    :cvar VALUE_15: UPC12+5 (price-point) on cover 4 AKA price/item;
        ‘cover 4’ is defined as the back cover of a book
    :cvar VALUE_16: EAN13 on cover 3 ‘Cover 3’ is defined as the inside
        back cover of a book
    :cvar VALUE_17: EAN13+5 on cover 3 (US dollar price encoded) ‘Cover
        3’ is defined as the inside back cover of a book
    :cvar VALUE_18: UPC12 (item-specific) on cover 3 AKA item/price;
        ‘cover 3’ is defined as the inside back cover of a book
    :cvar VALUE_19: UPC12+5 (item-specific) on cover 3 AKA item/price;
        ‘cover 3’ is defined as the inside back cover of a book
    :cvar VALUE_20: UPC12 (price-point) on cover 3 AKA price/item;
        ‘cover 3’ is defined as the inside back cover of a book
    :cvar VALUE_21: UPC12+5 (price-point) on cover 3 AKA price/item;
        ‘cover 3’ is defined as the inside back cover of a book
    :cvar VALUE_22: EAN13 on cover 2 ‘Cover 2’ is defined as the inside
        front cover of a book
    :cvar VALUE_23: EAN13+5 on cover 2 (US dollar price encoded) ‘Cover
        2’ is defined as the inside front cover of a book
    :cvar VALUE_24: UPC12 (item-specific) on cover 2 AKA item/price;
        ‘cover 2’ is defined as the inside front cover of a book
    :cvar VALUE_25: UPC12+5 (item-specific) on cover 2 AKA item/price;
        ‘cover 2’ is defined as the inside front cover of a book
    :cvar VALUE_26: UPC12 (price-point) on cover 2 AKA price/item;
        ‘cover 2’ is defined as the inside front cover of a book
    :cvar VALUE_27: UPC12+5 (price-point) on cover 2 AKA price/item;
        ‘cover 2’ is defined as the inside front cover of a book
    :cvar VALUE_28: EAN13 on box To be used only on boxed products
    :cvar VALUE_29: EAN13+5 on box (US dollar price encoded) To be used
        only on boxed products
    :cvar VALUE_30: UPC12 (item-specific) on box AKA item/price; to be
        used only on boxed products
    :cvar VALUE_31: UPC12+5 (item-specific) on box AKA item/price; to be
        used only on boxed products
    :cvar VALUE_32: UPC12 (price-point) on box AKA price/item; to be
        used only on boxed products
    :cvar VALUE_33: UPC12+5 (price-point) on box AKA price/item; to be
        used only on boxed products
    :cvar VALUE_34: EAN13 on tag To be used only on products fitted with
        hanging tags
    :cvar VALUE_35: EAN13+5 on tag (US dollar price encoded) To be used
        only on products fitted with hanging tags
    :cvar VALUE_36: UPC12 (item-specific) on tag AKA item/price; to be
        used only on products fitted with hanging tags
    :cvar VALUE_37: UPC12+5 (item-specific) on tag AKA item/price; to be
        used only on products fitted with hanging tags
    :cvar VALUE_38: UPC12 (price-point) on tag AKA price/item; to be
        used only on products fitted with hanging tags
    :cvar VALUE_39: UPC12+5 (price-point) on tag AKA price/item; to be
        used only on products fitted with hanging tags
    :cvar VALUE_40: EAN13 on bottom Not be used on books unless they are
        contained within outer packaging
    :cvar VALUE_41: EAN13+5 on bottom (US dollar price encoded) Not be
        used on books unless they are contained within outer packaging
    :cvar VALUE_42: UPC12 (item-specific) on bottom AKA item/price; not
        be used on books unless they are contained within outer
        packaging
    :cvar VALUE_43: UPC12+5 (item-specific) on bottom AKA item/price;
        not be used on books unless they are contained within outer
        packaging
    :cvar VALUE_44: UPC12 (price-point) on bottom AKA price/item; not be
        used on books unless they are contained within outer packaging
    :cvar VALUE_45: UPC12+5 (price-point) on bottom AKA price/item; not
        be used on books unless they are contained within outer
        packaging
    :cvar VALUE_46: EAN13 on back Not be used on books unless they are
        contained within outer packaging
    :cvar VALUE_47: EAN13+5 on back (US dollar price encoded) Not be
        used on books unless they are contained within outer packaging
    :cvar VALUE_48: UPC12 (item-specific) on back AKA item/price; not be
        used on books unless they are contained within outer packaging
    :cvar VALUE_49: UPC12+5 (item-specific) on back AKA item/price; not
        be used on books unless they are contained within outer
        packaging
    :cvar VALUE_50: UPC12 (price-point) on back AKA price/item; not be
        used on books unless they are contained within outer packaging
    :cvar VALUE_51: UPC12+5 (price-point) on back AKA price/item; not be
        used on books unless they are contained within outer packaging
    :cvar VALUE_52: EAN13 on outer sleeve/back To be used only on
        products packaged in outer sleeves
    :cvar VALUE_53: EAN13+5 on outer sleeve/back (US dollar price
        encoded) To be used only on products packaged in outer sleeves
    :cvar VALUE_54: UPC12 (item-specific) on outer sleeve/back AKA
        item/price; to be used only on products packaged in outer
        sleeves
    :cvar VALUE_55: UPC12+5 (item-specific) on outer sleeve/back AKA
        item/price; to be used only on products packaged in outer
        sleeves
    :cvar VALUE_56: UPC12 (price-point) on outer sleeve/back AKA
        price/item; to be used only on products packaged in outer
        sleeves
    :cvar VALUE_57: UPC12+5 (price-point) on outer sleeve/back AKA
        price/item; to be used only on products packaged in outer
        sleeves
    :cvar VALUE_58: EAN13+5 (no price encoded) Position unspecified
    :cvar VALUE_59: EAN13+5 on cover 4 (no price encoded) ‘Cover 4’ is
        defined as the back cover of a book
    :cvar VALUE_60: EAN13+5 on cover 3 (no price encoded) ‘Cover 3’ is
        defined as the inside back cover of a book
    :cvar VALUE_61: EAN13+5 on cover 2 (no price encoded) ‘Cover 2’ is
        defined as the inside front cover of a book
    :cvar VALUE_62: EAN13+5 on box (no price encoded) To be used only on
        boxed products
    :cvar VALUE_63: EAN13+5 on tag (no price encoded) To be used only on
        products fitted with hanging tags
    :cvar VALUE_64: EAN13+5 on bottom (no price encoded) Not be used on
        books unless they are contained within outer packaging
    :cvar VALUE_65: EAN13+5 on back (no price encoded) Not be used on
        books unless they are contained within outer packaging
    :cvar VALUE_66: EAN13+5 on outer sleeve/back (no price encoded) To
        be used only on products packaged in outer sleeves
    :cvar VALUE_67: EAN13+5 (CAN dollar price encoded) Position
        unspecified
    :cvar VALUE_68: EAN13+5 on cover 4 (CAN dollar price encoded) ‘Cover
        4’ is defined as the back cover of a book
    :cvar VALUE_69: EAN13+5 on cover 3 (CAN dollar price encoded) ‘Cover
        3’ is defined as the inside back cover of a book
    :cvar VALUE_70: EAN13+5 on cover 2 (CAN dollar price encoded) ‘Cover
        2’ is defined as the inside front cover of a book
    :cvar VALUE_71: EAN13+5 on box (CAN dollar price encoded) To be used
        only on boxed products
    :cvar VALUE_72: EAN13+5 on tag (CAN dollar price encoded) To be used
        only on products fitted with hanging tags
    :cvar VALUE_73: EAN13+5 on bottom (CAN dollar price encoded) Not be
        used on books unless they are contained within outer packaging
    :cvar VALUE_74: EAN13+5 on back (CAN dollar price encoded) Not be
        used on books unless they are contained within outer packaging
    :cvar VALUE_75: EAN13+5 on outer sleeve/back (CAN dollar price
        encoded) To be used only on products packaged in outer sleeves
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_36 = "36"
    VALUE_37 = "37"
    VALUE_38 = "38"
    VALUE_39 = "39"
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_45 = "45"
    VALUE_46 = "46"
    VALUE_47 = "47"
    VALUE_48 = "48"
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_54 = "54"
    VALUE_55 = "55"
    VALUE_56 = "56"
    VALUE_57 = "57"
    VALUE_58 = "58"
    VALUE_59 = "59"
    VALUE_60 = "60"
    VALUE_61 = "61"
    VALUE_62 = "62"
    VALUE_63 = "63"
    VALUE_64 = "64"
    VALUE_65 = "65"
    VALUE_66 = "66"
    VALUE_67 = "67"
    VALUE_68 = "68"
    VALUE_69 = "69"
    VALUE_70 = "70"
    VALUE_71 = "71"
    VALUE_72 = "72"
    VALUE_73 = "73"
    VALUE_74 = "74"
    VALUE_75 = "75"


class List60(Enum):
    """
    Unit of pricing code.

    :cvar VALUE_00: Per copy of whole product Default
    :cvar VALUE_01: Per page for printed loose-leaf content only
    """
    VALUE_00 = "00"
    VALUE_01 = "01"


class List61(Enum):
    """
    Price status code.

    :cvar VALUE_00: Unspecified Default
    :cvar VALUE_01: Provisional
    :cvar VALUE_02: Firm
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"


class List62(Enum):
    """
    Tax rate, coded.

    :cvar H: Higher rate Specifies that tax is applied at a higher rate
        than standard
    :cvar P: Tax paid at source (Italy) Under Italian tax rules, VAT on
        books may be paid at source by the publisher, and subsequent
        transactions through the supply chain are tax-exempt
    :cvar R: Lower rate Specifies that tax is applied at a lower rate
        than standard
    :cvar S: Standard rate
    :cvar Z: Zero-rated
    """
    H = "H"
    P = "P"
    R = "R"
    S = "S"
    Z = "Z"


class List64(Enum):
    """
    Publishing status.

    :cvar VALUE_00: Unspecified Status is not specified (as distinct
        from unknown): the default if the &lt;PublishingStatus&gt;
        element is not sent. Also to be used in applications where the
        element is considered mandatory, but the sender of the ONIX
        message chooses not to pass on status information
    :cvar VALUE_01: Cancelled The product was announced, and
        subsequently abandoned; the &lt;PublicationDate&gt; element in
        ONIX 2.1 or its equivalent in &lt;PublishingDate&gt; in ONIX 3.0
        must not be sent
    :cvar VALUE_02: Forthcoming Not yet published, must be accompanied
        by the expected date in &lt;PublicationDate&gt; in ONIX 2.1, or
        its equivalent in the &lt;PublishingDate&gt; composite in ONIX
        3.0
    :cvar VALUE_03: Postponed indefinitely The product was announced,
        and subsequently postponed with no expected publication date;
        the &lt;Publication Date&gt; element in ONIX 2.1, or its
        equivalent as a &lt;PublishingDate&gt; composite in ONIX 3.0,
        must not be sent
    :cvar VALUE_04: Active The product was published, and is still
        active in the sense that the publisher will accept orders for
        it, though it may or may not be immediately available, for which
        see &lt;SupplyDetail&gt;
    :cvar VALUE_05: No longer our product Ownership of the product has
        been transferred to another publisher (with details of acquiring
        publisher if possible in PR.19 (ONIX 2.1) OR P.19 (ONIX 3.0))
    :cvar VALUE_06: Out of stock indefinitely The product was active,
        but is now inactive in the sense that (a) the publisher cannot
        fulfill orders for it, though stock may still be available
        elsewhere in the supply chain, and (b) there are no current
        plans to bring it back into stock. Use this code for ‘reprint
        under consideration’. Code 06 does not specifically imply that
        returns are or are not still accepted
    :cvar VALUE_07: Out of print The product was active, but is now
        permanently inactive in the sense that (a) the publisher will
        not accept orders for it, though stock may still be available
        elsewhere in the supply chain, and (b) the product will not be
        made available again under the same ISBN. Code 07 normally
        implies that the publisher will not accept returns beyond a
        specified date
    :cvar VALUE_08: Inactive The product was active, but is now
        permanently or indefinitely inactive in the sense that the
        publisher will not accept orders for it, though stock may still
        be available elsewhere in the supply chain. Code 08 covers both
        of codes 06 and 07, and may be used where the distinction
        between those values is either unnecessary or meaningless
    :cvar VALUE_09: Unknown The sender of the ONIX record does not know
        the current publishing status
    :cvar VALUE_10: Remaindered The product is no longer available from
        the current publisher, under the current ISBN, at the current
        price. It may be available to be traded through another channel.
        A Publishing Status code 10 ‘Remaindered’ usually but not always
        means that the publisher has decided to sell off excess
        inventory of the book. Copies of books that are remaindered are
        often made available in the supply chain at a reduced price.
        However, such remainders are often sold under a product
        identifier that differs from the ISBN on the full-priced copy of
        the book. A Publishing Status code 10 ‘Remaindered’ on a given
        product record may or may not be followed by a Publishing Status
        code 06 ‘Out of Stock Indefinitely’ or 07 ‘Out of Print’: the
        practise varies from one publisher to another. Some publishers
        may revert to a Publishing Status code 04 ‘Active’ if a desired
        inventory level on the product in question has subsequently been
        reached. No change in rights should ever be inferred from this
        (or any other) Publishing Status code value
    :cvar VALUE_11: Withdrawn from sale Withdrawn, typically for legal
        reasons or to avoid giving offence
    :cvar VALUE_12: Recalled Recalled for reasons of consumer safety.
        Deprecated, use code 15 instead
    :cvar VALUE_13: Active, but not sold separately The product is
        published and active but, as a publishing decision, it is not
        sold separately – only in an assembly or as part of a pack.
        Depending on product composition and pricing, it may be saleable
        separately at retail
    :cvar VALUE_15: Recalled Recalled for reasons of consumer safety
    :cvar VALUE_16: Temporarily withdrawn from sale Withdrawn
        temporarily, typically for quality or technical reasons. In ONIX
        3.0, must be accompanied by expected availability date coded
        ‘22’ within the &lt;PublishingDate&gt; composite, except in
        exceptional circumstances where no date is known
    :cvar VALUE_17: Permanently withdrawn from sale Withdrawn
        permanently from sale in all markets. Effectively synonymous
        with ‘Out of print’ (code 07), but specific to downloadable and
        online digital products (where no ‘stock’ would remain in the
        supply chain)
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"


class List65(Enum):
    """
    Product availability.

    :cvar VALUE_01: Cancelled Cancelled: product was announced, and
        subsequently abandoned
    :cvar VALUE_10: Not yet available Not yet available (requires
        expected date, either as &lt;ExpectedShipDate&gt; (ONIX 2.1) or
        as &lt;SupplyDate&gt; with &lt;SupplyDateRole&gt; coded ‘08’
        (ONIX 3.0), except in exceptional circumstances where no date is
        known)
    :cvar VALUE_11: Awaiting stock Not yet available, but will be a
        stock item when available (requires expected date, either as
        &lt;ExpectedShipDate&gt; (ONIX 2.1) or as &lt;SupplyDate&gt;
        with &lt;SupplyDateRole&gt; coded ‘08’ (ONIX 3.0), except in
        exceptional circumstances where no date is known). Used
        particularly for imports which have been published in the
        country of origin but have not yet arrived in the importing
        country
    :cvar VALUE_12: Not yet available, will be POD Not yet available, to
        be published as print-on-demand only (requires expected date,
        either as &lt;ExpectedShipDate&gt; (ONIX 2.1) or as
        &lt;SupplyDate&gt; with &lt;SupplyDateRole&gt; coded ‘08’ (ONIX
        3.0), except in exceptional circumstances where no date is
        known). May apply either to a POD successor to an existing
        conventional edition, when the successor will be published under
        a different ISBN (normally because different trade terms apply);
        or to a title that is being published as a POD original
    :cvar VALUE_20: Available Available from us (form of availability
        unspecified)
    :cvar VALUE_21: In stock Available from us as a stock item
    :cvar VALUE_22: To order Available from us as a non-stock item, by
        special order
    :cvar VALUE_23: POD Available from us by print-on-demand
    :cvar VALUE_30: Temporarily unavailable Temporarily unavailable:
        temporarily unavailable from us (reason unspecified) (requires
        expected date, either as &lt;ExpectedShipDate&gt; (ONIX 2.1) or
        as &lt;SupplyDate&gt; with &lt;SupplyDateRole&gt; coded ‘08’
        (ONIX 3.0), except in exceptional circumstances where no date is
        known)
    :cvar VALUE_31: Out of stock Stock item, temporarily out of stock
        (requires expected date, either as &lt;ExpectedShipDate&gt;
        (ONIX 2.1) or as &lt;SupplyDate&gt; with &lt;SupplyDateRole&gt;
        coded ‘08’ (ONIX 3.0), except in exceptional circumstances where
        no date is known)
    :cvar VALUE_32: Reprinting Temporarily unavailable, reprinting
        (requires expected date, either as &lt;ExpectedShipDate&gt;
        (ONIX 2.1) or as &lt;SupplyDate&gt; with &lt;SupplyDateRole&gt;
        coded ‘08’ (ONIX 3.0), except in exceptional circumstances where
        no date is known)
    :cvar VALUE_33: Awaiting reissue Temporarily unavailable, awaiting
        reissue (requires expected date, either as
        &lt;ExpectedShipDate&gt; (ONIX 2.1) or as &lt;SupplyDate&gt;
        with &lt;SupplyDateRole&gt; coded ‘08’ (ONIX 3.0), except in
        exceptional circumstances where no date is known)
    :cvar VALUE_34: Temporarily withdrawn from sale May be for quality
        or technical reasons. Requires expected availability date,
        either as &lt;ExpectedShipDate&gt; (ONIX 2.1) or as
        &lt;SupplyDate&gt; with &lt;SupplyDateRole&gt; coded ‘08’ (ONIX
        3.0), except in exceptional circumstances where no date is known
    :cvar VALUE_40: Not available (reason unspecified) Not available
        from us (for any reason)
    :cvar VALUE_41: Not available, replaced by new product This product
        is unavailable, but a successor product or edition is or will be
        available from us (identify successor in &lt;RelatedProduct&gt;)
    :cvar VALUE_42: Not available, other format available This product
        is unavailable, but the same content is or will be available
        from us in an alternative format (identify other format product
        in &lt;RelatedProduct&gt;)
    :cvar VALUE_43: No longer supplied by us Identify new supplier in
        &lt;NewSupplier&gt; if possible
    :cvar VALUE_44: Apply direct Not available to trade, apply direct to
        publisher
    :cvar VALUE_45: Not sold separately Must be bought as part of a set
        or trade pack (identify set or pack in &lt;RelatedProduct&gt;)
    :cvar VALUE_46: Withdrawn from sale May be for legal reasons or to
        avoid giving offence
    :cvar VALUE_47: Remaindered Remaindered
    :cvar VALUE_48: Not available, replaced by POD Out of print, but a
        print-on-demand edition is or will be available under a
        different ISBN. Use only when the POD successor has a different
        ISBN, normally because different trade terms apply
    :cvar VALUE_49: Recalled Recalled for reasons of consumer safety
    :cvar VALUE_50: Not sold as set When a collection that is not sold
        as a set nevertheless has its own ONIX record
    :cvar VALUE_51: Not available, publisher indicates OP This product
        is unavailable, no successor product or alternative format is
        available or planned. Use this code only when the publisher has
        indicated the product is out of print
    :cvar VALUE_52: Not available, publisher no longer sells product in
        this market This product is unavailable in this market, no
        successor product or alternative format is available or planned.
        Use this code when a publisher has indicated the product is
        permanently unavailable (in this market) while remaining
        available elsewhere
    :cvar VALUE_97: No recent update received Sender has not received
        any recent update for this product from the publisher/supplier
        (for use when the sender is a data aggregator): the definition
        of ‘recent’ must be specified by the aggregator, or by agreement
        between parties to an exchange
    :cvar VALUE_98: No longer receiving updates Sender is no longer
        receiving any updates from the publisher/supplier of this
        product (for use when the sender is a data aggregator)
    :cvar VALUE_99: Contact supplier Availability not known to sender
    """
    VALUE_01 = "01"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_45 = "45"
    VALUE_46 = "46"
    VALUE_47 = "47"
    VALUE_48 = "48"
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_97 = "97"
    VALUE_98 = "98"
    VALUE_99 = "99"


class List7(Enum):
    """
    Product form code.

    :cvar VALUE_00: Undefined
    :cvar AA: Audio Audio recording – detail unspecified
    :cvar AB: Audio cassette Audio cassette (analogue)
    :cvar AC: CD-Audio Audio compact disc, in any recording format: use
        for ‘red book’ (conventional audio CD) and SACD, and use coding
        in Product Form Detail to specify the format, if required
    :cvar AD: DAT Digital audio tape cassette
    :cvar AE: Audio disc Audio disc (excluding CD-Audio)
    :cvar AF: Audio tape Audio tape (analogue open reel tape)
    :cvar AG: MiniDisc Sony MiniDisc format
    :cvar AH: CD-Extra Audio compact disc with part CD-ROM content, also
        termed CD-Plus or Enhanced-CD: use for ‘blue book’ and
        ‘yellow/red book’ two-session discs
    :cvar AI: DVD Audio
    :cvar AJ: Downloadable audio file Audio recording downloadable
        online
    :cvar AK: Pre-recorded digital audio player For example, Playaway
        audiobook and player: use coding in Product Form Detail to
        specify the recording format, if required
    :cvar AL: Pre-recorded SD card For example, Audiofy audiobook chip
    :cvar AZ: Other audio format Other audio format not specified by AB
        to AL
    :cvar BA: Book Book – detail unspecified
    :cvar BB: Hardback Hardback or cased book
    :cvar BC: Paperback / softback Paperback or other softback book
    :cvar BD: Loose-leaf Loose-leaf book
    :cvar BE: Spiral bound Spiral, comb or coil bound book
    :cvar BF: Pamphlet Pamphlet or brochure, stapled; German ‘geheftet’.
        Includes low-extent wire-stitched books bound without a distinct
        spine (eg many comic books)
    :cvar BG: Leather / fine binding
    :cvar BH: Board book Child’s book with all pages printed on board
    :cvar BI: Rag book Child’s book with all pages printed on textile
    :cvar BJ: Bath book Child’s book printed on waterproof material
    :cvar BK: Novelty book A book whose novelty consists wholly or
        partly in a format which cannot be described by any other
        available code – a ‘conventional’ format code is always to be
        preferred; one or more Product Form Detail codes, eg from the
        B2nn group, should be used whenever possible to provide
        additional description
    :cvar BL: Slide bound Slide bound book
    :cvar BM: Big book Extra-large format for teaching etc; this format
        and terminology may be specifically UK; required as a top-level
        differentiator
    :cvar BN: Part-work (fascículo) A part-work issued with its own ISBN
        and intended to be collected and bound into a complete book
    :cvar BO: Fold-out book or chart Concertina-folded book or chart,
        designed to fold to pocket or regular page size: use for German
        ‘Leporello’
    :cvar BP: Foam book A children’s book whose cover and pages are made
        of foam
    :cvar BZ: Other book format Other book format or binding not
        specified by BB to BP
    :cvar CA: Sheet map Sheet map – detail unspecified
    :cvar CB: Sheet map, folded
    :cvar CC: Sheet map, flat
    :cvar CD: Sheet map, rolled See Code List 80 for ‘rolled in tube’
    :cvar CE: Globe Globe or planisphere
    :cvar CZ: Other cartographic Other cartographic format not specified
        by CB to CE
    :cvar DA: Digital Digital or multimedia (detail unspecified)
    :cvar DB: CD-ROM
    :cvar DC: CD-I CD interactive, use for ‘green book’ discs
    :cvar DD: DVD DEPRECATED – use VI for DVD video, AI for DVD audio,
        DI for DVD-ROM
    :cvar DE: Game cartridge
    :cvar DF: Diskette AKA ‘floppy disc’
    :cvar DG: Electronic book text Electronic book text in proprietary
        or open standard format
    :cvar DH: Online resource An electronic database or other resource
        or service accessible through online networks
    :cvar DI: DVD-ROM
    :cvar DJ: Secure Digital (SD) Memory Card
    :cvar DK: Compact Flash Memory Card
    :cvar DL: Memory Stick Memory Card
    :cvar DM: USB Flash Drive
    :cvar DN: Double-sided CD/DVD Double-sided disc, one side CD-
        Audio/CD-ROM, other side DVD-Audio/DVD-Video/DVD-ROM (at least
        one side must be -ROM)
    :cvar DO: Digital product license key Digital product license
        delivered through the retail supply chain as a physical ‘key’,
        typically a card or booklet containing a code enabling the
        purchaser to download or activate the associated product
    :cvar DZ: Other digital Other digital or multimedia not specified by
        DB to DN
    :cvar FA: Film or transparency Film or transparency – detail
        unspecified
    :cvar FB: Film Continuous film or filmstrip: DEPRECATED – use FE or
        FF
    :cvar FC: Slides Photographic transparencies mounted for projection
    :cvar FD: OHP transparencies Transparencies for overhead projector
    :cvar FE: Filmstrip
    :cvar FF: Film Continuous movie film as opposed to filmstrip
    :cvar FZ: Other film or transparency format Other film or
        transparency format not specified by FB to FF
    :cvar MA: Microform Microform – detail unspecified
    :cvar MB: Microfiche
    :cvar MC: Microfilm Roll microfilm
    :cvar MZ: Other microform Other microform not specified by MB or MC
    :cvar PA: Miscellaneous print Miscellaneous printed material –
        detail unspecified
    :cvar PB: Address book May use product form detail codes P201 to
        P204 to specify binding
    :cvar PC: Calendar
    :cvar PD: Cards Cards, flash cards (eg for teaching reading)
    :cvar PE: Copymasters Copymasters, photocopiable sheets
    :cvar PF: Diary May use product form detail codes P201 to P204 to
        specify binding
    :cvar PG: Frieze Narrow strip-shaped printed sheet used mostly for
        education or children’s products (eg depicting alphabet, number
        line, procession of illustrated characters etc). Usually
        intended for horizontal display
    :cvar PH: Kit Parts for post-purchase assembly
    :cvar PI: Sheet music
    :cvar PJ: Postcard book or pack
    :cvar PK: Poster Poster for retail sale – see also XF
    :cvar PL: Record book Record book (eg ‘birthday book’, ‘baby book’):
        may use product form detail codes P201 to P204 to specify
        binding
    :cvar PM: Wallet or folder Wallet or folder (containing loose sheets
        etc): it is preferable to code the contents and treat ‘wallet’
        as packaging (List 80), but if this is not possible the product
        as a whole may be coded as a ‘wallet’
    :cvar PN: Pictures or photographs
    :cvar PO: Wallchart
    :cvar PP: Stickers
    :cvar PQ: Plate (lámina) A book-sized (as opposed to poster-sized)
        sheet, usually in color or high quality print
    :cvar PR: Notebook / blank book A book with all pages blank for the
        buyer’s own use: may use product form detail codes P201 to P204
        to specify binding
    :cvar PS: Organizer May use product form detail codes P201 to P204
        to specify binding
    :cvar PT: Bookmark
    :cvar PZ: Other printed item Other printed item not specified by PB
        to PT
    :cvar VA: Video Video – detail unspecified
    :cvar VB: Video, VHS, PAL DEPRECATED – use new VJ
    :cvar VC: Video, VHS, NTSC DEPRECATED – use new VJ
    :cvar VD: Video, Betamax, PAL DEPRECATED – use new VK
    :cvar VE: Video, Betamax, NTSC DEPRECATED – use new VK
    :cvar VF: Videodisc eg Laserdisc
    :cvar VG: Video, VHS, SECAM DEPRECATED – use new VJ
    :cvar VH: Video, Betamax, SECAM DEPRECATED – use new VK
    :cvar VI: DVD video DVD video: specify TV standard in List 78
    :cvar VJ: VHS video VHS videotape: specify TV standard in List 78
    :cvar VK: Betamax video Betamax videotape: specify TV standard in
        List 78
    :cvar VL: VCD VideoCD
    :cvar VM: SVCD Super VideoCD
    :cvar VN: HD DVD High definition DVD disc, Toshiba HD DVD format
    :cvar VO: Blu-ray High definition DVD disc, Sony Blu-ray format
    :cvar VP: UMD Video Sony Universal Media disc
    :cvar VZ: Other video format Other video format not specified by VB
        to VP
    :cvar WW: Mixed media product A product consisting of two or more
        items in different media or different product forms, eg book and
        CD-ROM, book and toy, hardback book and e-book, etc
    :cvar WX: Multiple copy pack A product containing multiple copies of
        one or more items packaged together for retail sale, consisting
        of either (a) several copies of a single item (eg 6 copies of a
        graded reader), or (b) several copies of each of several items
        (eg 3 copies each of 3 different graded readers), or (c) several
        copies of one or more single items plus a single copy of one or
        more related items (eg 30 copies of a pupil’s textbook plus 1 of
        teacher’s text). NOT TO BE CONFUSED WITH: multi-volume sets, or
        sets containing a single copy of a number of different items
        (boxed, slip-cased or otherwise); items with several components
        of different physical forms (see WW); or packs intended for
        trade distribution only, where the contents are retailed
        separately (see XC, XE, XL)
    :cvar XA: Trade-only material Trade-only material (unspecified)
    :cvar XB: Dumpbin – empty
    :cvar XC: Dumpbin – filled Dumpbin with contents
    :cvar XD: Counterpack – empty
    :cvar XE: Counterpack – filled Counterpack with contents
    :cvar XF: Poster, promotional Promotional poster for display, not
        for sale – see also PK
    :cvar XG: Shelf strip
    :cvar XH: Window piece Promotional piece for shop window display
    :cvar XI: Streamer
    :cvar XJ: Spinner
    :cvar XK: Large book display Large scale facsimile of book for
        promotional display
    :cvar XL: Shrink-wrapped pack A quantity pack with its own product
        code, for trade supply only: the retail items it contains are
        intended for sale individually – see also WX. For products or
        product bundles supplied shrink-wrapped for retail sale, use the
        Product Form code of the contents plus code 21 from List 80
    :cvar XM: Boxed pack A quantity pack with its own product code, for
        trade supply only: the retail items it contains are intended for
        sale individually – see also WX. For products or product bundles
        supplied boxed for retail sale, use the Product Form code of the
        contents plus code 09 from List 80
    :cvar XZ: Other point of sale Other point of sale material not
        specified by XB to XL
    :cvar ZA: General merchandise General merchandise – unspecified
    :cvar ZB: Doll
    :cvar ZC: Soft toy Soft or plush toy
    :cvar ZD: Toy
    :cvar ZE: Game Board game, or other game (except computer game: see
        DE)
    :cvar ZF: T-shirt
    :cvar ZG: E-book reader Dedicated e-book reading device, typically
        with mono screen
    :cvar ZH: Tablet computer General purpose tablet computer, typically
        with color screen
    :cvar ZI: Audiobook player Dedicated audiobook player device,
        typically including book-related features like bookmarking
    :cvar ZJ: Jigsaw
    :cvar ZY: Other apparel Other apparel items not specified by ZB to
        ZJ, including promotional or branded scarves, caps, aprons etc
    :cvar ZZ: Other merchandise Other merchandise not specified by ZB to
        ZY
    """
    VALUE_00 = "00"
    AA = "AA"
    AB = "AB"
    AC = "AC"
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AH = "AH"
    AI = "AI"
    AJ = "AJ"
    AK = "AK"
    AL = "AL"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BC = "BC"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BK = "BK"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BP = "BP"
    BZ = "BZ"
    CA = "CA"
    CB = "CB"
    CC = "CC"
    CD = "CD"
    CE = "CE"
    CZ = "CZ"
    DA = "DA"
    DB = "DB"
    DC = "DC"
    DD = "DD"
    DE = "DE"
    DF = "DF"
    DG = "DG"
    DH = "DH"
    DI = "DI"
    DJ = "DJ"
    DK = "DK"
    DL = "DL"
    DM = "DM"
    DN = "DN"
    DO = "DO"
    DZ = "DZ"
    FA = "FA"
    FB = "FB"
    FC = "FC"
    FD = "FD"
    FE = "FE"
    FF = "FF"
    FZ = "FZ"
    MA = "MA"
    MB = "MB"
    MC = "MC"
    MZ = "MZ"
    PA = "PA"
    PB = "PB"
    PC = "PC"
    PD = "PD"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PI = "PI"
    PJ = "PJ"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PO = "PO"
    PP = "PP"
    PQ = "PQ"
    PR = "PR"
    PS = "PS"
    PT = "PT"
    PZ = "PZ"
    VA = "VA"
    VB = "VB"
    VC = "VC"
    VD = "VD"
    VE = "VE"
    VF = "VF"
    VG = "VG"
    VH = "VH"
    VI = "VI"
    VJ = "VJ"
    VK = "VK"
    VL = "VL"
    VM = "VM"
    VN = "VN"
    VO = "VO"
    VP = "VP"
    VZ = "VZ"
    WW = "WW"
    WX = "WX"
    XA = "XA"
    XB = "XB"
    XC = "XC"
    XD = "XD"
    XE = "XE"
    XF = "XF"
    XG = "XG"
    XH = "XH"
    XI = "XI"
    XJ = "XJ"
    XK = "XK"
    XL = "XL"
    XM = "XM"
    XZ = "XZ"
    ZA = "ZA"
    ZB = "ZB"
    ZC = "ZC"
    ZD = "ZD"
    ZE = "ZE"
    ZF = "ZF"
    ZG = "ZG"
    ZH = "ZH"
    ZI = "ZI"
    ZJ = "ZJ"
    ZY = "ZY"
    ZZ = "ZZ"


class List70(Enum):
    """
    Stock quantity code type.

    :cvar VALUE_01: Proprietary As specified in
        &lt;StockQuantityCodeTypeName&gt;
    :cvar VALUE_02: APA stock quantity code Code scheme defined by the
        Australian Publishers Association
    """
    VALUE_01 = "01"
    VALUE_02 = "02"


class List71(Enum):
    """
    Sales restriction type code.

    :cvar VALUE_00: Unspecified – see text Restriction must be described
        in &lt;SalesRestrictionDetail&gt; (ONIX 2.1) or
        &lt;SalesRestrictionNote&gt; (ONIX 3.0)
    :cvar VALUE_01: Retailer exclusive / own brand For sale only through
        designated retailer. Retailer must be identified or named in an
        instance of the &lt;SalesOutlet&gt; composite. Use only when it
        is not possible to assign the more explicit code 04 or 05
    :cvar VALUE_02: Office supplies edition For editions sold only
        though office supplies wholesalers. Retailer(s) and/or
        distributor(s) may be identified or named in an instance of the
        &lt;SalesOutlet&gt; composite
    :cvar VALUE_03: Internal publisher use only: do not list For an ISBN
        that is assigned for a publisher’s internal purposes
    :cvar VALUE_04: Retailer exclusive For sale only through designated
        retailer, though not under retailer’s own brand/imprint.
        Retailer must be identified or named in an instance of the
        &lt;SalesOutlet&gt; composite
    :cvar VALUE_05: Retailer own brand For sale only through designated
        retailer under retailer’s own brand/imprint. Retailer must be
        identified or named in an instance of the &lt;SalesOutlet&gt;
        composite
    :cvar VALUE_06: Library edition For sale to libraries only; not for
        sale through retail trade
    :cvar VALUE_07: Schools only edition For sale directly to schools
        only; not for sale through retail trade
    :cvar VALUE_08: Indiziert Indexed for the German market – in
        Deutschland indiziert
    :cvar VALUE_09: Not for sale to libraries Expected to apply in
        particular to digital products for consumer sale where the
        publisher does not permit the product to be supplied to
        libraries who provide an ebook loan service
    :cvar VALUE_10: News outlet edition For editions sold only through
        newsstands/newsagents
    :cvar VALUE_11: Retailer exception Not for sale through designated
        retailer. Retailer must be identified or named in an instance of
        the &lt;SalesOutlet&gt; composite
    :cvar VALUE_12: Not for sale to subscription services Not for sale
        to organisations or services offering consumers subscription
        access to a library of books
    :cvar VALUE_13: Subscription services only Restricted to
        organisations or services offering consumers subscription access
        to a library of books
    :cvar VALUE_14: Not for retail online Exclusive to bricks-and-mortar
        retail outlets
    :cvar VALUE_15: Online retail only Exclusive to online retail
        outlets
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"


class List72(Enum):
    """
    Thesis type code.

    :cvar VALUE_01: Habilitationsschrift Professorial dissertation
        (thesis for postdoctoral lecturing qualification)
    :cvar VALUE_02: Dissertationsschrift Doctoral thesis
    :cvar VALUE_03: Staatsexamensarbeit State examination thesis
    :cvar VALUE_04: Magisterarbeit Magisters degree thesis
    :cvar VALUE_05: Diplomarbeit Diploma degree thesis
    :cvar VALUE_06: Bachelorarbeit Bachelors degree thesis
    :cvar VALUE_07: Masterarbeit Masters degree thesis
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"


class List73(Enum):
    """
    Website role.

    :cvar VALUE_00: Unspecified, see website description
    :cvar VALUE_01: Publisher’s corporate website See also codes 17 and
        18
    :cvar VALUE_02: Publisher’s website for a specified work A
        publisher’s informative and/or promotional webpage relating to a
        specified work (book, journal, online resource or other
        publication type)
    :cvar VALUE_03: Online hosting service home page A webpage giving
        access to an online content hosting service as a whole
    :cvar VALUE_04: Journal home page A webpage giving general
        information about a serial, in print or electronic format or
        both
    :cvar VALUE_05: Online resource ‘available content’ page A webpage
        giving direct access to the content that is available online for
        a specified resource version. Generally used for content
        available online under subscription terms
    :cvar VALUE_06: Contributor’s own website A webpage maintained by an
        author or other contributor about her/his publications and
        personal background
    :cvar VALUE_07: Publisher’s website relating to specified
        contributor A publisher’s webpage devoted to a specific author
        or other contributor
    :cvar VALUE_08: Other publisher’s website relating to specified
        contributor A webpage devoted to a specific author or other
        contributor, and maintained by a publisher other than the
        publisher of the item described in the ONIX record
    :cvar VALUE_09: Third-party website relating to specified
        contributor A webpage devoted to a specific author or other
        contributor, and maintained by a third party (eg a fan site)
    :cvar VALUE_10: Contributor’s own website for specified work A
        webpage maintained by an author or other contributor and
        specific to an individual work
    :cvar VALUE_11: Other publisher’s website relating to specified work
        A webpage devoted to an individual work, and maintained by a
        publisher other than the publisher of the item described in the
        ONIX record
    :cvar VALUE_12: Third-party website relating to specified work A
        webpage devoted to an individual work, and maintained by a third
        party (eg a fan site)
    :cvar VALUE_13: Contributor’s own website for group or series of
        works A webpage maintained by an author or other contributor and
        specific to a group or series of works
    :cvar VALUE_14: Publisher’s website relating to group or series of
        works A publisher’s webpage devoted to a group or series of
        works
    :cvar VALUE_15: Other publisher’s website relating to group or
        series of works A webpage devoted to a group or series of works,
        and maintained by a publisher other than the publisher of the
        item described in the ONIX record
    :cvar VALUE_16: Third-party website relating to group or series of
        works (eg a fan site) A webpage devoted to a group or series of
        works, and maintained by a third party (eg a fan site)
    :cvar VALUE_17: Publisher’s B2B website Use instead of code 01 to
        specify a publisher’s website for trade users
    :cvar VALUE_18: Publisher’s B2C website Use instead of code 01 to
        specify a publisher’s website for end customers (consumers)
    :cvar VALUE_23: Author blog For example, a Blogger or Tumblr URL, a
        Wordpress website or other blog URL
    :cvar VALUE_24: Web page for author presentation / commentary
    :cvar VALUE_25: Web page for author interview
    :cvar VALUE_26: Web page for author reading
    :cvar VALUE_27: Web page for cover material
    :cvar VALUE_28: Web page for sample content
    :cvar VALUE_29: Web page for full content Use this value in the
        &lt;Website&gt; composite in &lt;SupplyDetail&gt; when sending a
        link to a webpage at which a digital product is available for
        download and/or online access
    :cvar VALUE_30: Web page for other commentary / discussion
    :cvar VALUE_31: Transfer-URL URL needed by the German National
        Library for direct access, harvesting and storage of an
        electronic resource
    :cvar VALUE_32: DOI Website Link Link needed by German Books in
        Print (VLB) for DOI registration and ONIX DOI conversion
    :cvar VALUE_33: Supplier’s corporate website A corporate website
        operated by a distributor or other supplier (not the publisher)
    :cvar VALUE_34: Supplier’s B2B website A website operated by a
        distributor or other supplier (not the publisher) and aimed at
        trade customers
    :cvar VALUE_35: Supplier’s B2C website A website operated by a
        distributor or other supplier (not the publisher) and aimed at
        consumers
    :cvar VALUE_36: Supplier’s website for a specified work A
        distributor or supplier’s webpage describing a specified work
    :cvar VALUE_37: Supplier’s B2B website for a specified work A
        distributor or supplier’s webpage describing a specified work,
        and aimed at trade customers
    :cvar VALUE_38: Supplier’s B2C website for a specified work A
        distributor or supplier’s webpage describing a specified work,
        and aimed at consumers
    :cvar VALUE_39: Supplier’s website for a group or series of works A
        distributor or supplier’s webpage describing a group or series
        of works
    :cvar VALUE_40: URL of full metadata description For example an ONIX
        or MARC record for the product, available online
    :cvar VALUE_41: Social networking URL for specific work or product
        For example, a Facebook, Google+ or Twitter URL for the product
        or work
    :cvar VALUE_42: Author’s social networking URL For example, a
        Facebook, Google+ or Twitter page
    :cvar VALUE_43: Publisher’s social networking URL For example, a
        Facebook, Google+ or Twitter page
    :cvar VALUE_44: Social networking URL for specific article, chapter
        or content item For example, a Facebook, Google+ or Twitter
        page. Use only in the context of a specific content item (eg
        within &lt;ContentItem&gt;)
    :cvar VALUE_45: Publisher’s or third party website for permissions
        requests For example, a service offering click-through licensing
        of extracts
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_36 = "36"
    VALUE_37 = "37"
    VALUE_38 = "38"
    VALUE_39 = "39"
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_45 = "45"


class List74(Enum):
    """
    Language code – ISO 639-2/B.

    :cvar AAR: Afar
    :cvar ABK: Abkhaz
    :cvar ACE: Achinese
    :cvar ACH: Acoli
    :cvar ADA: Adangme
    :cvar ADY: Adygei
    :cvar AFA: Afro-Asiatic languages Collective name
    :cvar AFH: Afrihili Artificial language
    :cvar AFR: Afrikaans
    :cvar AIN: Ainu
    :cvar AKA: Akan Macrolanguage
    :cvar AKK: Akkadian
    :cvar ALB: Albanian Macrolanguage
    :cvar ALE: Aleut
    :cvar ALG: Algonquian languages Collective name
    :cvar ALT: Southern Altai
    :cvar AMH: Amharic
    :cvar ANG: English, Old (ca. 450-1100)
    :cvar ANP: Angika
    :cvar APA: Apache languages Collective name
    :cvar ARA: Arabic Macrolanguage
    :cvar ARC: Official Aramaic; Imperial Aramaic (700-300 BCE)
    :cvar ARG: Aragonese
    :cvar ARM: Armenian
    :cvar ARN: Mapudungun; Mapuche
    :cvar ARP: Arapaho
    :cvar ART: Artificial languages Collective name
    :cvar ARW: Arawak
    :cvar ASM: Assamese
    :cvar AST: Asturian; Bable; Leonese; Asturleonese
    :cvar ATH: Athapascan languages Collective name
    :cvar AUS: Australian languages Collective name
    :cvar AVA: Avaric
    :cvar AVE: Avestan
    :cvar AWA: Awadhi
    :cvar AYM: Aymara Macrolanguage
    :cvar AZE: Azerbaijani Macrolanguage
    :cvar BAD: Banda languages Collective name
    :cvar BAI: Bamileke languages Collective name
    :cvar BAK: Bashkir
    :cvar BAL: Baluchi Macrolanguage
    :cvar BAM: Bambara
    :cvar BAN: Balinese
    :cvar BAQ: Basque
    :cvar BAS: Basa
    :cvar BAT: Baltic languages Collective name
    :cvar BEJ: Beja; Bedawiyet
    :cvar BEL: Belarusian
    :cvar BEM: Bemba
    :cvar BEN: Bengali
    :cvar BER: Berber languages Collective name
    :cvar BHO: Bhojpuri
    :cvar BIH: Bihari languages Collective name
    :cvar BIK: Bikol Macrolanguage
    :cvar BIN: Bini; Edo
    :cvar BIS: Bislama
    :cvar BLA: Siksika
    :cvar BNT: Bantu languages Collective name
    :cvar BOS: Bosnian
    :cvar BRA: Braj
    :cvar BRE: Breton
    :cvar BTK: Batak languages Collective name
    :cvar BUA: Buriat Macrolanguage
    :cvar BUG: Buginese
    :cvar BUL: Bulgarian
    :cvar BUR: Burmese
    :cvar BYN: Blin; Bilin
    :cvar CAD: Caddo
    :cvar CAI: Central American Indian languages Collective name
    :cvar CAR: Galibi Carib
    :cvar CAT: Catalan
    :cvar CAU: Caucasian languages Collective name
    :cvar CEB: Cebuano
    :cvar CEL: Celtic languages Collective name
    :cvar CHA: Chamorro
    :cvar CHB: Chibcha
    :cvar CHE: Chechen
    :cvar CHG: Chagatai
    :cvar CHI: Chinese Macrolanguage
    :cvar CHK: Chuukese (Truk)
    :cvar CHM: Mari Macrolanguage
    :cvar CHN: Chinook jargon
    :cvar CHO: Choctaw
    :cvar CHP: Chipewyan; Dene Suline
    :cvar CHR: Cherokee
    :cvar CHU: Church Slavic; Old Slavonic; Church Slavonic; Old
        Bulgarian; Old Church Slavonic
    :cvar CHV: Chuvash
    :cvar CHY: Cheyenne
    :cvar CMC: Chamic languages Collective name
    :cvar CMN: Mandarin ONIX local code, equivalent to cmn in ISO 639-3
    :cvar COP: Coptic
    :cvar COR: Cornish
    :cvar COS: Corsican
    :cvar CPE: Creoles and pidgins, English-based Collective name
    :cvar CPF: Creoles and pidgins, French-based Collective name
    :cvar CPP: Creoles and pidgins, Portuguese-based Collective name
    :cvar CRE: Cree Macrolanguage
    :cvar CRH: Crimean Turkish; Crimean Tatar
    :cvar CRP: Creoles and pidgins Collective name
    :cvar CSB: Kashubian
    :cvar CUS: Cushitic languages Collective name
    :cvar CZE: Czech
    :cvar DAK: Dakota
    :cvar DAN: Danish
    :cvar DAR: Dargwa
    :cvar DAY: Land Dayak languages Collective name
    :cvar DEL: Delaware Macrolanguage
    :cvar DEN: Slave (Athapascan) Macrolanguage
    :cvar DGR: Dogrib
    :cvar DIN: Dinka Macrolanguage
    :cvar DIV: Divehi; Dhivehi; Maldivian
    :cvar DOI: Dogri Macrolanguage
    :cvar DRA: Dravidian languages Collective name
    :cvar DSB: Lower Sorbian
    :cvar DUA: Duala
    :cvar DUM: Dutch, Middle (ca. 1050-1350)
    :cvar DUT: Dutch; Flemish
    :cvar DYU: Dyula
    :cvar DZO: Dzongkha
    :cvar EFI: Efik
    :cvar EGY: Egyptian (Ancient)
    :cvar EKA: Ekajuk
    :cvar ELX: Elamite
    :cvar ENG: English
    :cvar ENM: English, Middle (1100-1500)
    :cvar EPO: Esperanto Artificial language
    :cvar EST: Estonian Macrolanguage
    :cvar EWE: Ewe
    :cvar EWO: Ewondo
    :cvar FAN: Fang
    :cvar FAO: Faroese
    :cvar FAT: Fanti
    :cvar FIJ: Fijian
    :cvar FIL: Filipino; Pilipino
    :cvar FIN: Finnish
    :cvar FIT: Meänkieli / Tornedalen Finnish ONIX local code,
        equivalent to fit in ISO 639-3
    :cvar FIU: Finno-Ugrian languages Collective name
    :cvar FKV: Kvensk ONIX local code, equivalent to fkv in ISO 639-3
    :cvar FON: Fon
    :cvar FRE: French
    :cvar FRM: French, Middle (ca. 1400-1600)
    :cvar FRO: French, Old (ca. 842-1400)
    :cvar FRR: Northern Frisian
    :cvar FRS: Eastern Frisian
    :cvar FRY: Western Frisian
    :cvar FUL: Fulah
    :cvar FUR: Friulian
    :cvar GAA: Gã
    :cvar GAY: Gayo
    :cvar GBA: Gbaya Macrolanguage
    :cvar GEM: Germanic languages Collective name
    :cvar GEO: Georgian
    :cvar GER: German
    :cvar GEZ: Ethiopic (Ge’ez)
    :cvar GIL: Gilbertese
    :cvar GLA: Scottish Gaelic
    :cvar GLE: Irish
    :cvar GLG: Galician
    :cvar GLV: Manx
    :cvar GMH: German, Middle High (ca. 1050-1500)
    :cvar GOH: German, Old High (ca. 750-1050)
    :cvar GON: Gondi Macrolanguage
    :cvar GOR: Gorontalo
    :cvar GOT: Gothic
    :cvar GRB: Grebo Macrolanguage
    :cvar GRC: Greek, Ancient (to 1453)
    :cvar GRE: Greek, Modern (1453-)
    :cvar GRN: Guarani Macrolanguage
    :cvar GSW: Swiss German; Alemannic
    :cvar GUJ: Gujarati
    :cvar GWI: Gwich’in
    :cvar HAI: Haida Macrolanguage
    :cvar HAT: Haitian French Creole
    :cvar HAU: Hausa
    :cvar HAW: Hawaiian
    :cvar HEB: Hebrew
    :cvar HER: Herero
    :cvar HIL: Hiligaynon
    :cvar HIM: Himachali languages; Western Pahari languages Collective
        name
    :cvar HIN: Hindi
    :cvar HIT: Hittite
    :cvar HMN: Hmong; Mong Macrolanguage
    :cvar HMO: Hiri Motu
    :cvar HRV: Croatian
    :cvar HSB: Upper Sorbian
    :cvar HUN: Hungarian
    :cvar HUP: Hupa
    :cvar IBA: Iban
    :cvar IBO: Igbo
    :cvar ICE: Icelandic
    :cvar IDO: Ido Artificial language
    :cvar III: Sichuan Yi; Nuosu
    :cvar IJO: Ijo languages Collective name
    :cvar IKU: Inuktitut Macrolanguage
    :cvar ILE: Interlingue; Occidental Artificial language
    :cvar ILO: Iloko
    :cvar INA: Interlingua (International Auxiliary Language
        Association) Artificial language
    :cvar INC: Indic languages Collective name
    :cvar IND: Indonesian
    :cvar INE: Indo-European languages Collective name
    :cvar INH: Ingush
    :cvar IPK: Inupiaq Macrolanguage
    :cvar IRA: Iranian languages Collective name
    :cvar IRO: Iroquoian languages Collective name
    :cvar ITA: Italian
    :cvar JAV: Javanese
    :cvar JBO: Lojban
    :cvar JPN: Japanese
    :cvar JPR: Judeo-Persian
    :cvar JRB: Judeo-Arabic Macrolanguage
    :cvar KAA: Kara-Kalpak
    :cvar KAB: Kabyle
    :cvar KAC: Kachin; Jingpho
    :cvar KAL: Kalâtdlisut; Greenlandic
    :cvar KAM: Kamba
    :cvar KAN: Kannada
    :cvar KAR: Karen languages Collective name
    :cvar KAS: Kashmiri
    :cvar KAU: Kanuri Macrolanguage
    :cvar KAW: Kawi
    :cvar KAZ: Kazakh
    :cvar KBD: Kabardian (Circassian)
    :cvar KDR: Karaim ONIX local code, equivalent to kdr in ISO 639-3
    :cvar KHA: Khasi
    :cvar KHI: Khoisan languages Collective name
    :cvar KHM: Central Khmer
    :cvar KHO: Khotanese; Sakan
    :cvar KIK: Kikuyu; Gikuyu
    :cvar KIN: Kinyarwanda
    :cvar KIR: Kirghiz; Kyrgyz
    :cvar KMB: Kimbundu
    :cvar KOK: Konkani Macrolanguage
    :cvar KOM: Komi Macrolanguage
    :cvar KON: Kongo Macrolanguage
    :cvar KOR: Korean
    :cvar KOS: Kusaiean (Caroline Islands)
    :cvar KPE: Kpelle Macrolanguage
    :cvar KRC: Karachay-Balkar
    :cvar KRL: Karelian
    :cvar KRO: Kru languages Collective name
    :cvar KRU: Kurukh
    :cvar KUA: Kuanyama
    :cvar KUM: Kumyk
    :cvar KUR: Kurdish Macrolanguage
    :cvar KUT: Kutenai
    :cvar LAD: Ladino
    :cvar LAH: Lahnda Macrolanguage
    :cvar LAM: Lamba
    :cvar LAO: Lao
    :cvar LAT: Latin
    :cvar LAV: Latvian Macrolanguage
    :cvar LEZ: Lezgian
    :cvar LIM: Limburgish
    :cvar LIN: Lingala
    :cvar LIT: Lithuanian
    :cvar LOL: Mongo-Nkundu
    :cvar LOZ: Lozi
    :cvar LTZ: Luxembourgish; Letzeburgesch
    :cvar LUA: Luba-Lulua
    :cvar LUB: Luba-Katanga
    :cvar LUG: Ganda
    :cvar LUI: Luiseño
    :cvar LUN: Lunda
    :cvar LUO: Luo (Kenya and Tanzania)
    :cvar LUS: Lushai
    :cvar MAC: Macedonian
    :cvar MAD: Madurese
    :cvar MAG: Magahi
    :cvar MAH: Marshallese
    :cvar MAI: Maithili
    :cvar MAK: Makasar
    :cvar MAL: Malayalam
    :cvar MAN: Mandingo Macrolanguage
    :cvar MAO: Maori
    :cvar MAP: Austronesian languages Collective name
    :cvar MAR: Marathi
    :cvar MAS: Masai
    :cvar MAY: Malay Macrolanguage
    :cvar MDF: Moksha
    :cvar MDR: Mandar
    :cvar MEN: Mende
    :cvar MGA: Irish, Middle (ca. 1100-1550)
    :cvar MIC: Mi’kmaq; Micmac
    :cvar MIN: Minangkabau
    :cvar MIS: Uncoded languages Use where no suitable code is available
    :cvar MKH: Mon-Khmer languages Collective name
    :cvar MLG: Malagasy Macrolanguage
    :cvar MLT: Maltese
    :cvar MNC: Manchu
    :cvar MNI: Manipuri
    :cvar MNO: Manobo languages Collective name
    :cvar MOH: Mohawk
    :cvar MOL: Moldavian; Moldovan DEPRECATED – use rum
    :cvar MON: Mongolian Macrolanguage
    :cvar MOS: Mooré; Mossi
    :cvar MUL: Multiple languages
    :cvar MUN: Munda languages Collective name
    :cvar MUS: Creek
    :cvar MWL: Mirandese
    :cvar MWR: Marwari Macrolanguage
    :cvar MYN: Mayan languages Collective name
    :cvar MYV: Erzya
    :cvar NAH: Nahuatl languages Collective name
    :cvar NAI: North American Indian languages Collective name
    :cvar NAP: Neapolitan
    :cvar NAU: Nauruan
    :cvar NAV: Navajo
    :cvar NBL: Ndebele, South
    :cvar NDE: Ndebele, North
    :cvar NDO: Ndonga
    :cvar NDS: Low German; Low Saxon
    :cvar NEP: Nepali Macrolanguage
    :cvar NEW: Newari; Nepal Bhasa
    :cvar NIA: Nias
    :cvar NIC: Niger-Kordofanian languages Collective name
    :cvar NIU: Niuean
    :cvar NNO: Norwegian Nynorsk
    :cvar NOB: Norwegian Bokmål
    :cvar NOG: Nogai
    :cvar NON: Old Norse
    :cvar NOR: Norwegian Macrolanguage
    :cvar NQO: N’Ko
    :cvar NSO: Pedi; Sepedi; Northern Sotho
    :cvar NUB: Nubian languages Collective name
    :cvar NWC: Classical Newari; Old Newari; Classical Nepal Bhasa
    :cvar NYA: Chichewa; Chewa; Nyanja
    :cvar NYM: Nyamwezi
    :cvar NYN: Nyankole
    :cvar NYO: Nyoro
    :cvar NZI: Nzima
    :cvar OCI: Occitan (post 1500)
    :cvar ODT: Old Dutch / Old Low Franconian (ca. 400–1050) ONIX local
        code, equivalent to odt in ISO 639-3
    :cvar OJI: Ojibwa Macrolanguage
    :cvar OMQ: Oto-Manguean languages ONIX local code, equivalent to omq
        in ISO 639-5. Collective name
    :cvar ORI: Oriya Macrolanguage
    :cvar ORM: Oromo Macrolanguage
    :cvar OSA: Osage
    :cvar OSS: Ossetian; Ossetic
    :cvar OTA: Turkish, Ottoman
    :cvar OTO: Otomian languages Collective name
    :cvar PAA: Papuan languages Collective name
    :cvar PAG: Pangasinan
    :cvar PAL: Pahlavi
    :cvar PAM: Pampanga; Kapampangan
    :cvar PAN: Panjabi
    :cvar PAP: Papiamento
    :cvar PAU: Palauan
    :cvar PEO: Old Persian (ca. 600-400 B.C.)
    :cvar PER: Persian Macrolanguage
    :cvar PHI: Philippine languages Collective name
    :cvar PHN: Phoenician
    :cvar PLI: Pali
    :cvar POL: Polish
    :cvar PON: Ponapeian
    :cvar POR: Portuguese
    :cvar PRA: Prakrit languages Collective name
    :cvar PRO: Provençal, Old (to 1500); Occitan, Old (to 1500)
    :cvar PUS: Pushto; Pashto Macrolanguage
    :cvar QAR: Aranés ONIX local code, distinct dialect of Occitan (not
        distinguished from oci by ISO 639-3)
    :cvar QAV: Valencian ONIX local code, distinct dialect of Catalan
        (not distinguished from cat by ISO 639-3)
    :cvar QUE: Quechua Macrolanguage
    :cvar RAJ: Rajasthani Macrolanguage
    :cvar RAP: Rapanui
    :cvar RAR: Rarotongan; Cook Islands Maori
    :cvar ROA: Romance languages Collective name
    :cvar ROH: Romansh
    :cvar ROM: Romany Macrolanguage
    :cvar RUM: Romanian
    :cvar RUN: Rundi
    :cvar RUP: Aromanian; Arumanian; Macedo-Romanian
    :cvar RUS: Russian
    :cvar SAD: Sandawe
    :cvar SAG: Sango
    :cvar SAH: Yakut
    :cvar SAI: South American Indian languages Collective name
    :cvar SAL: Salishan languages Collective name
    :cvar SAM: Samaritan Aramaic
    :cvar SAN: Sanskrit
    :cvar SAS: Sasak
    :cvar SAT: Santali
    :cvar SCC: Serbian DEPRECATED – use srp
    :cvar SCN: Sicilian
    :cvar SCO: Scots (lallans)
    :cvar SCR: Croatian DEPRECATED – use hrv
    :cvar SEL: Selkup
    :cvar SEM: Semitic languages Collective name
    :cvar SGA: Irish, Old (to 1100)
    :cvar SGN: Sign languages Collective name
    :cvar SHN: Shan
    :cvar SID: Sidamo
    :cvar SIN: Sinhala; Sinhalese
    :cvar SIO: Siouan languages Collective name
    :cvar SIT: Sino-Tibetan languages Collective name
    :cvar SLA: Slavic languages Collective name
    :cvar SLO: Slovak
    :cvar SLV: Slovenian
    :cvar SMA: Southern Sami
    :cvar SME: Northern Sami
    :cvar SMI: Sami languages Collective name
    :cvar SMJ: Lule Sami
    :cvar SMN: Inari Sami
    :cvar SMO: Samoan
    :cvar SMS: Skolt Sami
    :cvar SNA: Shona
    :cvar SND: Sindhi
    :cvar SNK: Soninke
    :cvar SOG: Sogdian
    :cvar SOM: Somali
    :cvar SON: Songhai languages Collective name
    :cvar SOT: Sotho; Sesotho
    :cvar SPA: Spanish
    :cvar SRD: Sardinian Macrolanguage
    :cvar SRN: Sranan Tongo
    :cvar SRP: Serbian
    :cvar SRR: Serer
    :cvar SSA: Nilo-Saharan languages Collective name
    :cvar SSW: Swazi; Swati
    :cvar SUK: Sukuma
    :cvar SUN: Sundanese
    :cvar SUS: Susu
    :cvar SUX: Sumerian
    :cvar SWA: Swahili Macrolanguage
    :cvar SWE: Swedish
    :cvar SYC: Classical Syriac
    :cvar SYR: Syriac Macrolanguage
    :cvar TAH: Tahitian
    :cvar TAI: Tai languages Collective name
    :cvar TAM: Tamil
    :cvar TAT: Tatar
    :cvar TEL: Telugu
    :cvar TEM: Temne; Time
    :cvar TER: Terena
    :cvar TET: Tetum
    :cvar TGK: Tajik
    :cvar TGL: Tagalog
    :cvar THA: Thai
    :cvar TIB: Tibetan
    :cvar TIG: Tigré
    :cvar TIR: Tigrinya
    :cvar TIV: Tiv
    :cvar TKL: Tokelauan
    :cvar TLH: Klingon; tlhIngan-Hol Artificial language
    :cvar TLI: Tlingit
    :cvar TMH: Tamashek Macrolanguage
    :cvar TOG: Tonga (Nyasa)
    :cvar TON: Tongan
    :cvar TPI: Tok Pisin
    :cvar TSI: Tsimshian
    :cvar TSN: Tswana AKA Setswana
    :cvar TSO: Tsonga
    :cvar TUK: Turkmen
    :cvar TUM: Tumbuka
    :cvar TUP: Tupi languages Collective name
    :cvar TUR: Turkish
    :cvar TUT: Altaic languages
    :cvar TVL: Tuvaluan
    :cvar TWI: Twi
    :cvar TYV: Tuvinian
    :cvar TZO: Tzotzil ONIX local code, equivalent to tzo in ISO 639-3
    :cvar UDM: Udmurt
    :cvar UGA: Ugaritic
    :cvar UIG: Uighur; Uyghur
    :cvar UKR: Ukrainian
    :cvar UMB: Umbundu
    :cvar UND: Undetermined language
    :cvar URD: Urdu
    :cvar UZB: Uzbek Macrolanguage
    :cvar VAI: Vai
    :cvar VEN: Venda
    :cvar VIE: Vietnamese
    :cvar VOL: Volapük Artificial language
    :cvar VOT: Votic
    :cvar WAK: Wakashan languages Collective name
    :cvar WAL: Wolaitta; Wolaytta
    :cvar WAR: Waray
    :cvar WAS: Washo
    :cvar WEL: Welsh
    :cvar WEN: Sorbian languages Collective name
    :cvar WLN: Walloon
    :cvar WOL: Wolof
    :cvar XAL: Kalmyk
    :cvar XHO: Xhosa
    :cvar YAO: Yao
    :cvar YAP: Yapese
    :cvar YID: Yiddish Macrolanguage
    :cvar YOR: Yoruba
    :cvar YUE: Cantonese ONIX local code, equivalent to yue in ISO 639-3
    :cvar YPK: Yupik languages Collective name
    :cvar ZAP: Zapotec Macrolanguage
    :cvar ZBL: Blissymbols; Blissymbolics; Bliss Artificial language
    :cvar ZEN: Zenaga
    :cvar ZGH: Standard Moroccan Tamazight
    :cvar ZHA: Zhuang; Chuang Macrolanguage
    :cvar ZND: Zande languages Collective name
    :cvar ZUL: Zulu
    :cvar ZUN: Zuni
    :cvar ZXX: No linguistic content
    :cvar ZZA: Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki
        Macrolanguage
    """
    AAR = "aar"
    ABK = "abk"
    ACE = "ace"
    ACH = "ach"
    ADA = "ada"
    ADY = "ady"
    AFA = "afa"
    AFH = "afh"
    AFR = "afr"
    AIN = "ain"
    AKA = "aka"
    AKK = "akk"
    ALB = "alb"
    ALE = "ale"
    ALG = "alg"
    ALT = "alt"
    AMH = "amh"
    ANG = "ang"
    ANP = "anp"
    APA = "apa"
    ARA = "ara"
    ARC = "arc"
    ARG = "arg"
    ARM = "arm"
    ARN = "arn"
    ARP = "arp"
    ART = "art"
    ARW = "arw"
    ASM = "asm"
    AST = "ast"
    ATH = "ath"
    AUS = "aus"
    AVA = "ava"
    AVE = "ave"
    AWA = "awa"
    AYM = "aym"
    AZE = "aze"
    BAD = "bad"
    BAI = "bai"
    BAK = "bak"
    BAL = "bal"
    BAM = "bam"
    BAN = "ban"
    BAQ = "baq"
    BAS = "bas"
    BAT = "bat"
    BEJ = "bej"
    BEL = "bel"
    BEM = "bem"
    BEN = "ben"
    BER = "ber"
    BHO = "bho"
    BIH = "bih"
    BIK = "bik"
    BIN = "bin"
    BIS = "bis"
    BLA = "bla"
    BNT = "bnt"
    BOS = "bos"
    BRA = "bra"
    BRE = "bre"
    BTK = "btk"
    BUA = "bua"
    BUG = "bug"
    BUL = "bul"
    BUR = "bur"
    BYN = "byn"
    CAD = "cad"
    CAI = "cai"
    CAR = "car"
    CAT = "cat"
    CAU = "cau"
    CEB = "ceb"
    CEL = "cel"
    CHA = "cha"
    CHB = "chb"
    CHE = "che"
    CHG = "chg"
    CHI = "chi"
    CHK = "chk"
    CHM = "chm"
    CHN = "chn"
    CHO = "cho"
    CHP = "chp"
    CHR = "chr"
    CHU = "chu"
    CHV = "chv"
    CHY = "chy"
    CMC = "cmc"
    CMN = "cmn"
    COP = "cop"
    COR = "cor"
    COS = "cos"
    CPE = "cpe"
    CPF = "cpf"
    CPP = "cpp"
    CRE = "cre"
    CRH = "crh"
    CRP = "crp"
    CSB = "csb"
    CUS = "cus"
    CZE = "cze"
    DAK = "dak"
    DAN = "dan"
    DAR = "dar"
    DAY = "day"
    DEL = "del"
    DEN = "den"
    DGR = "dgr"
    DIN = "din"
    DIV = "div"
    DOI = "doi"
    DRA = "dra"
    DSB = "dsb"
    DUA = "dua"
    DUM = "dum"
    DUT = "dut"
    DYU = "dyu"
    DZO = "dzo"
    EFI = "efi"
    EGY = "egy"
    EKA = "eka"
    ELX = "elx"
    ENG = "eng"
    ENM = "enm"
    EPO = "epo"
    EST = "est"
    EWE = "ewe"
    EWO = "ewo"
    FAN = "fan"
    FAO = "fao"
    FAT = "fat"
    FIJ = "fij"
    FIL = "fil"
    FIN = "fin"
    FIT = "fit"
    FIU = "fiu"
    FKV = "fkv"
    FON = "fon"
    FRE = "fre"
    FRM = "frm"
    FRO = "fro"
    FRR = "frr"
    FRS = "frs"
    FRY = "fry"
    FUL = "ful"
    FUR = "fur"
    GAA = "gaa"
    GAY = "gay"
    GBA = "gba"
    GEM = "gem"
    GEO = "geo"
    GER = "ger"
    GEZ = "gez"
    GIL = "gil"
    GLA = "gla"
    GLE = "gle"
    GLG = "glg"
    GLV = "glv"
    GMH = "gmh"
    GOH = "goh"
    GON = "gon"
    GOR = "gor"
    GOT = "got"
    GRB = "grb"
    GRC = "grc"
    GRE = "gre"
    GRN = "grn"
    GSW = "gsw"
    GUJ = "guj"
    GWI = "gwi"
    HAI = "hai"
    HAT = "hat"
    HAU = "hau"
    HAW = "haw"
    HEB = "heb"
    HER = "her"
    HIL = "hil"
    HIM = "him"
    HIN = "hin"
    HIT = "hit"
    HMN = "hmn"
    HMO = "hmo"
    HRV = "hrv"
    HSB = "hsb"
    HUN = "hun"
    HUP = "hup"
    IBA = "iba"
    IBO = "ibo"
    ICE = "ice"
    IDO = "ido"
    III = "iii"
    IJO = "ijo"
    IKU = "iku"
    ILE = "ile"
    ILO = "ilo"
    INA = "ina"
    INC = "inc"
    IND = "ind"
    INE = "ine"
    INH = "inh"
    IPK = "ipk"
    IRA = "ira"
    IRO = "iro"
    ITA = "ita"
    JAV = "jav"
    JBO = "jbo"
    JPN = "jpn"
    JPR = "jpr"
    JRB = "jrb"
    KAA = "kaa"
    KAB = "kab"
    KAC = "kac"
    KAL = "kal"
    KAM = "kam"
    KAN = "kan"
    KAR = "kar"
    KAS = "kas"
    KAU = "kau"
    KAW = "kaw"
    KAZ = "kaz"
    KBD = "kbd"
    KDR = "kdr"
    KHA = "kha"
    KHI = "khi"
    KHM = "khm"
    KHO = "kho"
    KIK = "kik"
    KIN = "kin"
    KIR = "kir"
    KMB = "kmb"
    KOK = "kok"
    KOM = "kom"
    KON = "kon"
    KOR = "kor"
    KOS = "kos"
    KPE = "kpe"
    KRC = "krc"
    KRL = "krl"
    KRO = "kro"
    KRU = "kru"
    KUA = "kua"
    KUM = "kum"
    KUR = "kur"
    KUT = "kut"
    LAD = "lad"
    LAH = "lah"
    LAM = "lam"
    LAO = "lao"
    LAT = "lat"
    LAV = "lav"
    LEZ = "lez"
    LIM = "lim"
    LIN = "lin"
    LIT = "lit"
    LOL = "lol"
    LOZ = "loz"
    LTZ = "ltz"
    LUA = "lua"
    LUB = "lub"
    LUG = "lug"
    LUI = "lui"
    LUN = "lun"
    LUO = "luo"
    LUS = "lus"
    MAC = "mac"
    MAD = "mad"
    MAG = "mag"
    MAH = "mah"
    MAI = "mai"
    MAK = "mak"
    MAL = "mal"
    MAN = "man"
    MAO = "mao"
    MAP = "map"
    MAR = "mar"
    MAS = "mas"
    MAY = "may"
    MDF = "mdf"
    MDR = "mdr"
    MEN = "men"
    MGA = "mga"
    MIC = "mic"
    MIN = "min"
    MIS = "mis"
    MKH = "mkh"
    MLG = "mlg"
    MLT = "mlt"
    MNC = "mnc"
    MNI = "mni"
    MNO = "mno"
    MOH = "moh"
    MOL = "mol"
    MON = "mon"
    MOS = "mos"
    MUL = "mul"
    MUN = "mun"
    MUS = "mus"
    MWL = "mwl"
    MWR = "mwr"
    MYN = "myn"
    MYV = "myv"
    NAH = "nah"
    NAI = "nai"
    NAP = "nap"
    NAU = "nau"
    NAV = "nav"
    NBL = "nbl"
    NDE = "nde"
    NDO = "ndo"
    NDS = "nds"
    NEP = "nep"
    NEW = "new"
    NIA = "nia"
    NIC = "nic"
    NIU = "niu"
    NNO = "nno"
    NOB = "nob"
    NOG = "nog"
    NON = "non"
    NOR = "nor"
    NQO = "nqo"
    NSO = "nso"
    NUB = "nub"
    NWC = "nwc"
    NYA = "nya"
    NYM = "nym"
    NYN = "nyn"
    NYO = "nyo"
    NZI = "nzi"
    OCI = "oci"
    ODT = "odt"
    OJI = "oji"
    OMQ = "omq"
    ORI = "ori"
    ORM = "orm"
    OSA = "osa"
    OSS = "oss"
    OTA = "ota"
    OTO = "oto"
    PAA = "paa"
    PAG = "pag"
    PAL = "pal"
    PAM = "pam"
    PAN = "pan"
    PAP = "pap"
    PAU = "pau"
    PEO = "peo"
    PER = "per"
    PHI = "phi"
    PHN = "phn"
    PLI = "pli"
    POL = "pol"
    PON = "pon"
    POR = "por"
    PRA = "pra"
    PRO = "pro"
    PUS = "pus"
    QAR = "qar"
    QAV = "qav"
    QUE = "que"
    RAJ = "raj"
    RAP = "rap"
    RAR = "rar"
    ROA = "roa"
    ROH = "roh"
    ROM = "rom"
    RUM = "rum"
    RUN = "run"
    RUP = "rup"
    RUS = "rus"
    SAD = "sad"
    SAG = "sag"
    SAH = "sah"
    SAI = "sai"
    SAL = "sal"
    SAM = "sam"
    SAN = "san"
    SAS = "sas"
    SAT = "sat"
    SCC = "scc"
    SCN = "scn"
    SCO = "sco"
    SCR = "scr"
    SEL = "sel"
    SEM = "sem"
    SGA = "sga"
    SGN = "sgn"
    SHN = "shn"
    SID = "sid"
    SIN = "sin"
    SIO = "sio"
    SIT = "sit"
    SLA = "sla"
    SLO = "slo"
    SLV = "slv"
    SMA = "sma"
    SME = "sme"
    SMI = "smi"
    SMJ = "smj"
    SMN = "smn"
    SMO = "smo"
    SMS = "sms"
    SNA = "sna"
    SND = "snd"
    SNK = "snk"
    SOG = "sog"
    SOM = "som"
    SON = "son"
    SOT = "sot"
    SPA = "spa"
    SRD = "srd"
    SRN = "srn"
    SRP = "srp"
    SRR = "srr"
    SSA = "ssa"
    SSW = "ssw"
    SUK = "suk"
    SUN = "sun"
    SUS = "sus"
    SUX = "sux"
    SWA = "swa"
    SWE = "swe"
    SYC = "syc"
    SYR = "syr"
    TAH = "tah"
    TAI = "tai"
    TAM = "tam"
    TAT = "tat"
    TEL = "tel"
    TEM = "tem"
    TER = "ter"
    TET = "tet"
    TGK = "tgk"
    TGL = "tgl"
    THA = "tha"
    TIB = "tib"
    TIG = "tig"
    TIR = "tir"
    TIV = "tiv"
    TKL = "tkl"
    TLH = "tlh"
    TLI = "tli"
    TMH = "tmh"
    TOG = "tog"
    TON = "ton"
    TPI = "tpi"
    TSI = "tsi"
    TSN = "tsn"
    TSO = "tso"
    TUK = "tuk"
    TUM = "tum"
    TUP = "tup"
    TUR = "tur"
    TUT = "tut"
    TVL = "tvl"
    TWI = "twi"
    TYV = "tyv"
    TZO = "tzo"
    UDM = "udm"
    UGA = "uga"
    UIG = "uig"
    UKR = "ukr"
    UMB = "umb"
    UND = "und"
    URD = "urd"
    UZB = "uzb"
    VAI = "vai"
    VEN = "ven"
    VIE = "vie"
    VOL = "vol"
    VOT = "vot"
    WAK = "wak"
    WAL = "wal"
    WAR = "war"
    WAS = "was"
    WEL = "wel"
    WEN = "wen"
    WLN = "wln"
    WOL = "wol"
    XAL = "xal"
    XHO = "xho"
    YAO = "yao"
    YAP = "yap"
    YID = "yid"
    YOR = "yor"
    YUE = "yue"
    YPK = "ypk"
    ZAP = "zap"
    ZBL = "zbl"
    ZEN = "zen"
    ZGH = "zgh"
    ZHA = "zha"
    ZND = "znd"
    ZUL = "zul"
    ZUN = "zun"
    ZXX = "zxx"
    ZZA = "zza"


class List75(Enum):
    """
    Person date role.

    :cvar VALUE_007: Date of birth
    :cvar VALUE_008: Date of death
    """
    VALUE_007 = "007"
    VALUE_008 = "008"


class List78(Enum):
    """
    Product form detail.

    :cvar A101: CD standard audio format CD ‘red book’ format
    :cvar A102: SACD super audio format
    :cvar A103: MP3 format MPEG-1/2 Audio Layer III file
    :cvar A104: WAV format Waveform audio file
    :cvar A105: Real Audio format
    :cvar A106: WMA Windows Media Audio format
    :cvar A107: AAC Advanced Audio Coding format
    :cvar A108: Ogg/Vorbis Vorbis audio format in the Ogg container
    :cvar A109: Audible Audio format proprietary to Audible.com
    :cvar A110: FLAC Free lossless audio codec
    :cvar A111: AIFF Audio Interchangeable File Format
    :cvar A112: ALAC Apple Lossless Audio Codec
    :cvar A201: DAISY 2: full audio with title only (no navigation)
        Deprecated, as does not meet DAISY 2 standard. Use conventional
        audiobook codes instead
    :cvar A202: DAISY 2: full audio with navigation (no text)
    :cvar A203: DAISY 2: full audio with navigation and partial text
    :cvar A204: DAISY 2: full audio with navigation and full text
    :cvar A205: DAISY 2: full text with navigation and partial audio
        Reading systems may provide full audio via text-to-speech
    :cvar A206: DAISY 2: full text with navigation and no audio Reading
        systems may provide full audio via text-to-speech
    :cvar A207: DAISY 3: full audio with title only (no navigation)
        Deprecated, as does not meet DAISY 3 standard. Use conventional
        audiobook codes instead
    :cvar A208: DAISY 3: full audio with navigation (no text)
    :cvar A209: DAISY 3: full audio with navigation and partial text
    :cvar A210: DAISY 3: full audio with navigation and full text
    :cvar A211: DAISY 3: full text with navigation and some audio
        Reading systems may provide full audio via text-to-speech
    :cvar A212: DAISY 3: full text with navigation (no audio) Reading
        systems may provide full audio via text-to-speech
    :cvar A301: Standalone audio
    :cvar A302: Readalong audio Audio intended exclusively for use
        alongside a printed copy of the book. Most often a children’s
        product. Normally contains instructions such as ‘turn the page
        now’ and other references to the printed item, and is usually
        sold packaged together with a printed copy
    :cvar A303: Playalong audio Audio intended for musical
        accompaniment, eg ‘Music minus one’, etc, often used for music
        learning. Includes singalong backing audio for musical learning
        or for Karaoke-style entertainment
    :cvar A304: Speakalong audio Audio intended for language learning,
        which includes speech plus gaps intended to be filled by the
        listener
    :cvar A305: Synchronised audio Audio synchronised to text within an
        e-publication, for example an EPUB3 with audio overlay.
        Synchronisation at least at paragraph level, and covering the
        full content
    :cvar A410: Mono Includes 'stereo' where channels are identical
    :cvar A420: Stereo
    :cvar A421: Stereo 2.1 Stereo plus low-frequency channel
    :cvar A441: Surround 4.1 Five-channel audio (including low-frequency
        channel)
    :cvar A451: Surround 5.1 Six-channel audio (including low-frequency
        channel)
    :cvar B101: Mass market (rack) paperback In North America, a
        category of paperback characterized partly by page size
        (typically from 6¾ up to 7⅛ x 4¼ inches) and partly by target
        market and terms of trade. Use with Product Form code BC
    :cvar B102: Trade paperback (US) In North America, a category of
        paperback characterized partly by page size and partly by target
        market and terms of trade. AKA ‘quality paperback’, and
        including textbooks. Most paperback books sold in North America
        except ‘mass-market’ (B101) and ‘tall rack’ (B107) are correctly
        described with this code. Use with Product Form code BC
    :cvar B103: Digest format paperback In North America, a category of
        paperback characterized by page size and generally used for
        children’s books; use with Product Form code BC. Note: was
        wrongly shown as B102 (duplicate entry) in Issue 3
    :cvar B104: A-format paperback In UK, a category of paperback
        characterized by page size (normally 178 x 111 mm approx); use
        with Product Form code BC
    :cvar B105: B-format paperback In UK, a category of paperback
        characterized by page size (normally 198 x 129 mm approx); use
        with Product Form code BC
    :cvar B106: Trade paperback (UK) In UK, a category of paperback
        characterized partly by size (usually in traditional hardback
        dimensions), and often used for paperback originals; use with
        Product Form code BC (replaces ‘C-format’ from former List 8)
    :cvar B107: Tall rack paperback (US) In North America, a category of
        paperback characterised partly by page size (typically 7½ x 4¼
        inches) and partly by target market and terms of trade; use with
        Product Form code BC
    :cvar B108: A5 size Tankobon 210 x 148mm
    :cvar B109: JIS B5 size Tankobon Japanese B-series size, 257 x 182
        mm
    :cvar B110: JIS B6 size Tankobon Japanese B-series size, 182 x 128
        mm
    :cvar B111: A6 size Bunko 148 x 105 mm
    :cvar B112: B40-dori Shinsho Japanese format, 182 x 103 mm or 173 x
        105 mm
    :cvar B113: Pocket (Sweden, Norway, France) A Swedish, Norwegian,
        French paperback format, of no particular fixed size. Use with
        Product Form Code BC
    :cvar B114: Storpocket (Sweden) A Swedish paperback format, use with
        Product Form Code BC
    :cvar B115: Kartonnage (Sweden) A Swedish hardback format, use with
        Product Form Code BB
    :cvar B116: Flexband (Sweden) A Swedish softback format, use with
        Product Form Code BC
    :cvar B117: Mook / Bookazine A softback book in the format of a
        magazine, usually sold like a book. Use with Product Form code
        BC
    :cvar B118: Dwarsligger Also called ‘Flipback’. A softback book in a
        specially compact proprietary format with pages printed in
        landscape on very thin paper and bound along the long (top) edge
        – see www.dwarsligger.com
    :cvar B119: 46 size Japanese format: 188 x 127 mm
    :cvar B120: 46-Henkei size Japanese format
    :cvar B121: A4 297 x 210 mm
    :cvar B122: A4-Henkei size Japanese format
    :cvar B123: A5-Henkei size Japanese format
    :cvar B124: B5-Henkei size Japanese format
    :cvar B125: B6-Henkei size Japanese format
    :cvar B126: AB size 257 x 210 mm
    :cvar B127: JIS B7 size Japanese B-series size, 128 x 91 mm
    :cvar B128: Kiku size Japanese format, 218 x 152 mm or 227 x 152 mm
    :cvar B129: Kiku-Henkei size Japanese format
    :cvar B130: JIS B4 size Japanese B-series size, 364 x 257 mm
    :cvar B131: Paperback (DE) German paperback format, greater than 205
        mm high, with flaps. Use with Product form code BC
    :cvar B201: Coloring / join-the-dot book
    :cvar B202: Lift-the-flap book
    :cvar B203: Fuzzy book DEPRECATED because of ambiguity – use B210,
        B214 or B215 as appropriate
    :cvar B204: Miniature book Note: was wrongly shown as B203
        (duplicate entry) in Issue 3
    :cvar B205: Moving picture / flicker book
    :cvar B206: Pop-up book
    :cvar B207: Scented / ‘smelly’ book
    :cvar B208: Sound story / ‘noisy’ book
    :cvar B209: Sticker book
    :cvar B210: Touch-and-feel book A book whose pages have a variety of
        textured inserts designed to stimulate tactile exploration: see
        also B214 and B215
    :cvar B211: Toy / die-cut book DEPRECATED – use B212 or B213 as
        appropriate
    :cvar B212: Die-cut book A book which is cut into a distinctive non-
        rectilinear shape and/or in which holes or shapes have been cut
        internally. (‘Die-cut’ is used here as a convenient shorthand,
        and does not imply strict limitation to a particular production
        process)
    :cvar B213: Book-as-toy A book which is also a toy, or which
        incorporates a toy as an integral part. (Do not, however, use
        B213 for a multiple-item product which includes a book and a toy
        as separate items)
    :cvar B214: Soft-to-touch book A book whose cover has a soft
        textured finish, typically over board
    :cvar B215: Fuzzy-felt book A book with detachable felt pieces and
        textured pages on which they can be arranged
    :cvar B221: Picture book Children’s picture book: use with
        applicable Product Form code
    :cvar B222: ‘Carousel’ book (aka ‘Star’ book). Tax treatment of
        products may differ from that of products with similar codes
        such as Book as toy or Pop-up book)
    :cvar B301: Loose leaf – sheets and binder Use with Product Form
        code BD
    :cvar B302: Loose leaf – binder only Use with Product Form code BD
    :cvar B303: Loose leaf – sheets only Use with Product Form code BD
    :cvar B304: Sewn AKA stitched; for ‘saddle-sewn’, see code B310
    :cvar B305: Unsewn / adhesive bound Including ‘perfect bound’,
        ‘glued’
    :cvar B306: Library binding Strengthened cloth-over-boards binding
        intended for libraries: use with Product form code BB
    :cvar B307: Reinforced binding Strengthened binding, not
        specifically intended for libraries
    :cvar B308: Half bound Must be accompanied by a code specifiying a
        material, eg ‘half-bound real leather’
    :cvar B309: Quarter bound Must be accompanied by a code specifiying
        a material, eg ‘quarter bound real leather’
    :cvar B310: Saddle-sewn AKA ‘saddle-stitched’ or ‘wire-stitched’
    :cvar B311: Comb bound Round or oval plastic forms in a clamp-like
        configuration: use with Product Form code BE
    :cvar B312: Wire-O Twin loop metal wire spine: use with Product Form
        code BE
    :cvar B313: Concealed wire Cased over Coiled or Wire-O binding: use
        with Product Form code BE and Product Form Detail code B312 or
        B315
    :cvar B314: Coiled wire bound Spiral wire bound. Use with product
        form code BE. The default if a spiral binding type is not
        stated. Cf. Comb and Wire-O binding
    :cvar B315: Trade binding Hardcover binding intended for general
        consumers rather than libraries, use with Product form code BB.
        The default if a hardcover binding detail is not stated. cf.
        Library binding
    :cvar B400: Self-cover Covers do not use a distinctive stock, but
        are the same as the body pages
    :cvar B401: Cloth over boards AKA fabric, linen over boards
    :cvar B402: Paper over boards
    :cvar B403: Leather, real
    :cvar B404: Leather, imitation
    :cvar B405: Leather, bonded
    :cvar B406: Vellum
    :cvar B407: Plastic DEPRECATED – use new B412 or B413 as appropriate
    :cvar B408: Vinyl DEPRECATED – use new B412 or B414 as appropriate
    :cvar B409: Cloth Cloth, not necessarily over boards – cf B401
    :cvar B410: Imitation cloth Spanish ‘simil-tela’
    :cvar B411: Velvet
    :cvar B412: Flexible plastic/vinyl cover AKA ‘flexibound’: use with
        Product Form code BC
    :cvar B413: Plastic-covered
    :cvar B414: Vinyl-covered
    :cvar B415: Laminated cover Book, laminating material unspecified:
        use L101 for ‘whole product laminated’, eg a laminated sheet map
        or wallchart
    :cvar B416: Card cover With card cover (like a typical paperback).
        As distinct from a self-cover or more elaborate binding
    :cvar B501: With dust jacket Type unspecified
    :cvar B502: With printed dust jacket Used to distinguish from B503
    :cvar B503: With translucent dust cover With translucent paper or
        plastic protective cover
    :cvar B504: With flaps For paperback with flaps
    :cvar B505: With thumb index
    :cvar B506: With ribbon marker(s) If the number of markers is
        significant, it can be stated as free text in
        &lt;ProductFormDescription&gt;
    :cvar B507: With zip fastener
    :cvar B508: With button snap fastener
    :cvar B509: With leather edge lining AKA yapp edge?
    :cvar B510: Rough front With edge trimming such that the front edge
        is ragged, not neatly and squarely trimmed: AKA deckle edge,
        feather edge, uncut edge, rough cut
    :cvar B511: With foldout With one or more gatefold or foldout
        sections bound in
    :cvar B512: Wide margin Pages include extra-wide margin specifically
        intended for hand-written annotations
    :cvar B513: With fastening strap Book with attached loop for fixing
        to baby stroller, cot, chair etc
    :cvar B514: With perforated pages With one or more pages perforated
        and intended to be torn out for use
    :cvar B601: Turn-around book A book in which half the content is
        printed upside-down, to be read the other way round. Also known
        as a ‘flip-book’, ‘back-to-back’, (fr.) ‘tête-bêche’ (usually an
        omnibus of two works)
    :cvar B602: Unflipped manga format Manga with pages and panels in
        the sequence of the original Japanese, but with Western text
    :cvar B610: Syllabification Text shows syllable breaks
    :cvar B701: UK Uncontracted Braille Single letters only. Was
        formerly identified as UK Braille Grade 1
    :cvar B702: UK Contracted Braille With some letter combinations. Was
        formerly identified as UK Braille Grade 2
    :cvar B703: US Braille DEPRECATED- use B704/B705 as appropriate
        instead
    :cvar B704: US Uncontracted Braille
    :cvar B705: US Contracted Braille
    :cvar B706: Unified English Braille
    :cvar B707: Moon Moon embossed alphabet, used by some print-impaired
        readers who have difficulties with Braille
    :cvar D101: Real Video format Includes RealVideo packaged within a
        .rm RealMedia container
    :cvar D102: Quicktime format
    :cvar D103: AVI format
    :cvar D104: Windows Media Video format
    :cvar D105: MPEG-4
    :cvar D201: MS-DOS Use with an applicable Product Form code D*; note
        that more detail of operating system requirements can be given
        in a Product Form Feature composite
    :cvar D202: Windows Use with an applicable Product Form code D*; see
        note on D201
    :cvar D203: Macintosh Use with an applicable Product Form code D*;
        see note on D201
    :cvar D204: UNIX / LINUX Use with an applicable Product Form code
        D*; see note on D201
    :cvar D205: Other operating system(s) Use with an applicable Product
        Form code D*; see note on D201
    :cvar D206: Palm OS Use with an applicable Product Form code D*; see
        note on D201
    :cvar D207: Windows Mobile Use with an applicable Product Form code
        D*; see note on D201
    :cvar D301: Microsoft XBox Use with Product Form code DE or DB as
        applicable
    :cvar D302: Nintendo Gameboy Color Use with Product Form code DE or
        DB as applicable
    :cvar D303: Nintendo Gameboy Advanced Use with Product Form code DE
        or DB as applicable
    :cvar D304: Nintendo Gameboy Use with Product Form code DE or DB as
        applicable
    :cvar D305: Nintendo Gamecube Use with Product Form code DE or DB as
        applicable
    :cvar D306: Nintendo 64 Use with Product Form code DE or DB as
        applicable
    :cvar D307: Sega Dreamcast Use with Product Form code DE or DB as
        applicable
    :cvar D308: Sega Genesis/Megadrive Use with Product Form code DE or
        DB as applicable
    :cvar D309: Sega Saturn Use with Product Form code DE or DB as
        applicable
    :cvar D310: Sony PlayStation 1 Use with Product Form code DE or DB
        as applicable
    :cvar D311: Sony PlayStation 2 Use with Product Form code DE or DB
        as applicable
    :cvar D312: Nintendo Dual Screen
    :cvar D313: Sony PlayStation 3
    :cvar D314: Xbox 360
    :cvar D315: Nintendo Wii
    :cvar D316: Sony PlayStation Portable (PSP)
    :cvar E200: Reflowable Use where a particular e-publication type
        (specified in &lt;EpubType&gt;) has both reflowable and fixed-
        format variants
    :cvar E201: Fixed format Use where a particular e-publication type
        (specified in &lt;EpubType&gt;) has both reflowable and fixed-
        format variants
    :cvar E202: Readable offline All e-publication resources are
        included within the e-publication package
    :cvar E203: Requires network connection E-publication requires a
        network connection to access some resources (eg an enhanced
        e-book where video clips are not stored within the e-publication
        ‘package’ itself, but are delivered via an internet connection)
    :cvar E204: Content removed Resources (eg images) present in other
        editions have been removed from this product, eg due to rights
        issues
    :cvar E210: Landscape Use for fixed-format e-books optimised for
        landscape display. Also include an indication of the optimal
        screen aspect ratio
    :cvar E211: Portrait Use for fixed-format e-books optimised for
        portrait display. Also include an indication of the optimal
        screen aspect ratio
    :cvar E221: 5:4 Use for fixed-format e-books optimised for displays
        with a 5:4 aspect ratio (eg 1280x1024 pixels etc, assuming
        square pixels). Note that aspect ratio codes are NOT specific to
        actual screen dimensions or pixel counts, but to the ratios
        between two dimensions or two pixel counts
    :cvar E222: 4:3 Use for fixed-format e-books optimised for displays
        with a 4:3 aspect ratio (eg 800x600, 1024x768, 2048x1536 pixels
        etc)
    :cvar E223: 3:2 Use for fixed-format e-books optimised for displays
        with a 3:2 aspect ratio (eg 960x640, 3072x2048 pixels etc)
    :cvar E224: 16:10 Use for fixed-format e-books optimised for
        displays with a 16:10 aspect ratio (eg 1440x900, 2560x1600
        pixels etc)
    :cvar E225: 16:9 Use for fixed-format e-books optimised for displays
        with a 16:9 aspect ratio (eg 1024x576, 1920x1080, 2048x1152
        pixels etc)
    :cvar L101: Laminated Whole product laminated (eg laminated map,
        fold-out chart, wallchart, etc): use B415 for book with
        laminated cover
    :cvar P101: Desk calendar Use with Product Form code PC
    :cvar P102: Mini calendar Use with Product Form code PC
    :cvar P103: Engagement calendar Use with Product Form code PC
    :cvar P104: Day by day calendar Use with Product Form code PC
    :cvar P105: Poster calendar Use with Product Form code PC
    :cvar P106: Wall calendar Use with Product Form code PC
    :cvar P107: Perpetual calendar Use with Product Form code PC
    :cvar P108: Advent calendar Use with Product Form code PC
    :cvar P109: Bookmark calendar Use with Product Form code PC
    :cvar P110: Student calendar Use with Product Form code PC
    :cvar P111: Project calendar Use with Product Form code PC
    :cvar P112: Almanac calendar Use with Product Form code PC
    :cvar P113: Other calendar A calendar that is not one of the types
        specified elsewhere: use with Product Form code PC
    :cvar P114: Other calendar or organiser product A product that is
        associated with or ancillary to a calendar or organiser, eg a
        deskstand for a calendar, or an insert for an organiser: use
        with Product Form code PC or PS
    :cvar P120: Picture story cards Kamishibai / Cantastoria cards
    :cvar P201: Hardback (stationery) Stationery item in hardback book
        format
    :cvar P202: Paperback / softback (stationery) Stationery item in
        paperback/softback book format
    :cvar P203: Spiral bound (stationery) Stationery item in spiral-
        bound book format
    :cvar P204: Leather / fine binding (stationery) Stationery item in
        leather-bound book format, or other fine binding
    :cvar P301: With hanging strips For map, poster, wallchart etc
    :cvar V201: PAL TV standard for video or DVD
    :cvar V202: NTSC TV standard for video or DVD
    :cvar V203: SECAM TV standard for video or DVD
    :cvar V220: Home use Licensed for use in domestic contexts only
    :cvar V221: Classroom use Licensed for use in education
    """
    A101 = "A101"
    A102 = "A102"
    A103 = "A103"
    A104 = "A104"
    A105 = "A105"
    A106 = "A106"
    A107 = "A107"
    A108 = "A108"
    A109 = "A109"
    A110 = "A110"
    A111 = "A111"
    A112 = "A112"
    A201 = "A201"
    A202 = "A202"
    A203 = "A203"
    A204 = "A204"
    A205 = "A205"
    A206 = "A206"
    A207 = "A207"
    A208 = "A208"
    A209 = "A209"
    A210 = "A210"
    A211 = "A211"
    A212 = "A212"
    A301 = "A301"
    A302 = "A302"
    A303 = "A303"
    A304 = "A304"
    A305 = "A305"
    A410 = "A410"
    A420 = "A420"
    A421 = "A421"
    A441 = "A441"
    A451 = "A451"
    B101 = "B101"
    B102 = "B102"
    B103 = "B103"
    B104 = "B104"
    B105 = "B105"
    B106 = "B106"
    B107 = "B107"
    B108 = "B108"
    B109 = "B109"
    B110 = "B110"
    B111 = "B111"
    B112 = "B112"
    B113 = "B113"
    B114 = "B114"
    B115 = "B115"
    B116 = "B116"
    B117 = "B117"
    B118 = "B118"
    B119 = "B119"
    B120 = "B120"
    B121 = "B121"
    B122 = "B122"
    B123 = "B123"
    B124 = "B124"
    B125 = "B125"
    B126 = "B126"
    B127 = "B127"
    B128 = "B128"
    B129 = "B129"
    B130 = "B130"
    B131 = "B131"
    B201 = "B201"
    B202 = "B202"
    B203 = "B203"
    B204 = "B204"
    B205 = "B205"
    B206 = "B206"
    B207 = "B207"
    B208 = "B208"
    B209 = "B209"
    B210 = "B210"
    B211 = "B211"
    B212 = "B212"
    B213 = "B213"
    B214 = "B214"
    B215 = "B215"
    B221 = "B221"
    B222 = "B222"
    B301 = "B301"
    B302 = "B302"
    B303 = "B303"
    B304 = "B304"
    B305 = "B305"
    B306 = "B306"
    B307 = "B307"
    B308 = "B308"
    B309 = "B309"
    B310 = "B310"
    B311 = "B311"
    B312 = "B312"
    B313 = "B313"
    B314 = "B314"
    B315 = "B315"
    B400 = "B400"
    B401 = "B401"
    B402 = "B402"
    B403 = "B403"
    B404 = "B404"
    B405 = "B405"
    B406 = "B406"
    B407 = "B407"
    B408 = "B408"
    B409 = "B409"
    B410 = "B410"
    B411 = "B411"
    B412 = "B412"
    B413 = "B413"
    B414 = "B414"
    B415 = "B415"
    B416 = "B416"
    B501 = "B501"
    B502 = "B502"
    B503 = "B503"
    B504 = "B504"
    B505 = "B505"
    B506 = "B506"
    B507 = "B507"
    B508 = "B508"
    B509 = "B509"
    B510 = "B510"
    B511 = "B511"
    B512 = "B512"
    B513 = "B513"
    B514 = "B514"
    B601 = "B601"
    B602 = "B602"
    B610 = "B610"
    B701 = "B701"
    B702 = "B702"
    B703 = "B703"
    B704 = "B704"
    B705 = "B705"
    B706 = "B706"
    B707 = "B707"
    D101 = "D101"
    D102 = "D102"
    D103 = "D103"
    D104 = "D104"
    D105 = "D105"
    D201 = "D201"
    D202 = "D202"
    D203 = "D203"
    D204 = "D204"
    D205 = "D205"
    D206 = "D206"
    D207 = "D207"
    D301 = "D301"
    D302 = "D302"
    D303 = "D303"
    D304 = "D304"
    D305 = "D305"
    D306 = "D306"
    D307 = "D307"
    D308 = "D308"
    D309 = "D309"
    D310 = "D310"
    D311 = "D311"
    D312 = "D312"
    D313 = "D313"
    D314 = "D314"
    D315 = "D315"
    D316 = "D316"
    E200 = "E200"
    E201 = "E201"
    E202 = "E202"
    E203 = "E203"
    E204 = "E204"
    E210 = "E210"
    E211 = "E211"
    E221 = "E221"
    E222 = "E222"
    E223 = "E223"
    E224 = "E224"
    E225 = "E225"
    L101 = "L101"
    P101 = "P101"
    P102 = "P102"
    P103 = "P103"
    P104 = "P104"
    P105 = "P105"
    P106 = "P106"
    P107 = "P107"
    P108 = "P108"
    P109 = "P109"
    P110 = "P110"
    P111 = "P111"
    P112 = "P112"
    P113 = "P113"
    P114 = "P114"
    P120 = "P120"
    P201 = "P201"
    P202 = "P202"
    P203 = "P203"
    P204 = "P204"
    P301 = "P301"
    V201 = "V201"
    V202 = "V202"
    V203 = "V203"
    V220 = "V220"
    V221 = "V221"


class List79(Enum):
    """
    Product form feature type.

    :cvar VALUE_01: Color of cover For Product Form Feature values see
        code list 98
    :cvar VALUE_02: Color of page edge For Product Form Feature values
        see code list 98
    :cvar VALUE_03: Text font The principal font used for body text,
        when this is a significant aspect of product description, eg for
        some Bibles, and for large print product. The accompanying
        Product Form Feature Description is text specifying font size
        and, if desired, typeface
    :cvar VALUE_04: Special cover material For Product Form Feature
        values see code list 99
    :cvar VALUE_05: DVD region For Product Form Feature values see code
        list 76
    :cvar VALUE_06: Operating system requirements A computer or handheld
        device operating system required to use a digital product, with
        version detail if applicable. The accompanying Product Form
        Feature Value is a code from List 176. Version detail, when
        applicable, is carried in Product Form Feature Description
    :cvar VALUE_07: Other system requirements Other system requirements
        for a digital product, described by free text in Product Form
        Feature Description
    :cvar VALUE_08: ‘Point and listen’ device compatibility Indicates
        compatibility with proprietary ‘point and listen’ devices such
        as Ting Pen (http://www.ting.eu) or the iSmart Touch and Read
        Pen. These devices scan invisible codes specially printed on the
        page to identify the book and position of the word, and the word
        is then read aloud by the device. The name of the compatible
        device (or range of devices) should be given in
        &lt;ProductFormFeatureDescription&gt;
    :cvar VALUE_09: E-publication accessibility detail For
        &lt;ProductFormFeatureValue&gt; codes, see Codelist 196
    :cvar VALUE_10: E-publication format version For versioned e-book
        file formats (or in some cases, devices).
        &lt;ProductFormFeatureValue&gt; should contain the version
        number as a period-separated list of numbers (eg ‘7’, ‘1.5’ or
        ‘3.10.7’). Use only with ONIX 3.0 – in ONIX 2.1, use
        &lt;EpubTypeVersion&gt; instead. For the most common file
        formats, code 15 and List 220 is strongly preferred
    :cvar VALUE_11: CPSIA choking hazard warning DEPRECATED – use code
        12 and List 143
    :cvar VALUE_12: CPSIA choking hazard warning Choking hazard warning
        required by US Consumer Product Safety Improvement Act (CPSIA)
        of 2008. Required, when applicable, for products sold in the US.
        The Product Form Feature Value is a code from List 143. Further
        explanation may be given in Product Form Feature Description
    :cvar VALUE_13: EU Toy Safety Hazard warning Product carries hazard
        warning required by EU Toy Safety Directive. The Product Form
        Feature Value is a code from List 184, and (for some codes) the
        exact wording of the warning may be given in Product Form
        Feature Description
    :cvar VALUE_14: IATA Dangerous Goods warning Product Form Feature
        Description must give further details of the warning
    :cvar VALUE_15: E-publication format version code For common
        versioned e-book formats (or in some cases, devices) – for
        example EPUB 2.0.1 or EPUB 3.0. &lt;ProductFormFeatureValue&gt;
        is a code from list 220. Use in ONIX 3.0 only
    :cvar VALUE_16: E-publication format validator version For common
        versioned e-book formats, the name and version of the validator
        used to check conformance. &lt;ProductFormFeatureDescription&gt;
        is the common name of the validator used (eg EpubCheck,
        Flightdeck), and &lt;ProductFormFeatureValue&gt; is the version
        number of the validator (eg 4.0.0a). Use with code 15 (or
        possibly code 10), or with &lt;EpubTypeVersion&gt;, to specify
        the version the e-publication conforms with
    :cvar VALUE_30: Not FSC or PEFC certified Product does not carry FSC
        or PEFC logo. The Product Form Feature Value and Description
        elements are not used. The product may, however, still carry a
        claimed Pre- and Post-Consumer Waste (PCW) content (type code
        37) in a separate repeat of the Product Form Feature composite
    :cvar VALUE_31: FSC certified – pure Product carries FSC logo (Pure,
        100%). &lt;ProductFormFeatureValue&gt; is the Certification
        number (ie either a Chain Of Custody (COC) number or a Trademark
        License number) printed on the book. Format: Chain of Custody
        number is two to five letters-COC-six digits (the digits should
        include leading zeros if necessary), eg ‘AB-COC-001234’ or
        ‘ABCDE-COC-123456’; Trademark License number is C followed by
        six digits, eg ‘C005678’ (this would normally be prefixed by
        ‘FSC®’ when displayed). By definition, a product certified Pure
        does not contain Pre- or Post-Consumer-Waste (PCW), so type code
        31 can only occur on its own. Certification numbers may be
        checked at http://info.fsc.org/
    :cvar VALUE_32: FSC certified – mixed sources Product carries FSC
        logo (Mixed sources, Mix). &lt;ProductFormFeatureValue&gt; is
        the Certification number (ie either a Chain Of Custody (COC)
        number or a Trademark License number) printed on the book.
        Format: Chain of Custody number is two to five letters-COC-six
        digits (the digits should include leading zeros if necessary),
        eg ‘AB-COC-001234’ or ‘ABCDE-COC-123456’; Trademark License
        number is C followed by six digits, eg ‘C005678’ (this would
        normally be prefixed by ‘FSC®’ when displayed). May be
        accompanied by a Pre- and Post-Consumer-Waste (PCW) percentage
        value, to be reported in another instance of
        &lt;ProductFormFeature&gt; with type code 36. Certification
        numbers may be checked at http://info.fsc.org/
    :cvar VALUE_33: FSC certified – recycled Product carries FSC logo
        (Recycled). &lt;ProductFormFeatureValue&gt; is the Certification
        number (ie either a Chain Of Custody (COC) number or a Trademark
        License number) printed on the book. Format: Chain of Custody
        number is two to five letters-COC-six digits (the digits should
        include leading zeroes if necessary), eg ‘AB-COC-001234’ or
        ‘ABCDE-COC-123456’; Trademark License number is C followed by
        six digits, eg ‘C005678’ (this would normally be prefixed by
        ‘FSC®’ when displayed). Should be accompanied by a Pre- and
        Post-Consumer-Waste (PCW) percentage value, to be reported in
        another instance of &lt;ProductFormFeature&gt; with type code
        36. Certification numbers may be checked at http://info.fsc.org/
    :cvar VALUE_34: PEFC certified Product carries PEFC logo
        (certified). &lt;ProductFormFeatureValue&gt; is the Chain Of
        Custody (COC) number printed on the book. May be accompanied by
        a Post-Consumer Waste (PCW) percentage value, to be reported in
        another instance of &lt;ProductFormFeature&gt; with type code 36
    :cvar VALUE_35: PEFC recycled Product carries PEFC logo (recycled).
        &lt;ProductFormFeatureValue&gt; is the Chain Of Custody (COC)
        number printed on the book. Should be accompanied by a Post-
        Consumer-Waste (PCW) percentage value, to be reported in another
        instance of &lt;ProductFormFeature&gt; with type code 36
    :cvar VALUE_36: FSC or PEFC certified Pre- and Post-Consumer Waste
        (PCW) percentage The percentage of recycled Pre- and Post-
        Consumer-Waste (PCW) used in a product where the composition is
        certified by FSC or PEFC. &lt;ProductFormFeatureValue&gt; is an
        integer. May occur together with type code 32, 33, 34 or 35
    :cvar VALUE_37: Claimed Pre- and Post-Consumer Waste (PCW)
        percentage The percentage of recycled Pre- and Post-Consumer
        Waste (PCW) claimed to be used in a product where the
        composition is not certified by FSC or PEFC. &lt;Product
        FormFeatureValue&gt; is an integer.
        &lt;ProductFormFeatureDescription&gt; may carry free text
        supporting the claim. Must be accompanied by type code 30
    :cvar VALUE_40: Paper produced by ‘green’ technology Product made
        from paper produced using environmentally-conscious technology.
        &lt;ProductFormFeatureDescription&gt; may carry free text with a
        more detailed statement
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_36 = "36"
    VALUE_37 = "37"
    VALUE_40 = "40"


class List8(Enum):
    """
    Book form detail.

    :cvar VALUE_01: A-format paperback DEPRECATED
    :cvar VALUE_02: B-format paperback ‘B’ format paperback: UK 198 x
        129 mm – DEPRECATED
    :cvar VALUE_03: C-format paperback ‘C’ format paperback: UK 216 x
        135 mm – DEPRECATED
    :cvar VALUE_04: Paper over boards DEPRECATED
    :cvar VALUE_05: Cloth DEPRECATED
    :cvar VALUE_06: With dust jacket DEPRECATED
    :cvar VALUE_07: Reinforced binding DEPRECATED
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"


class List80(Enum):
    """
    Product packaging type.

    :cvar VALUE_00: No outer packaging No packaging, or all smaller
        items enclosed inside largest item
    :cvar VALUE_01: Slip-sleeve Thin card or soft plastic sleeve, much
        less rigid than a slip case
    :cvar VALUE_02: Clamshell Packaging consisting of formed plastic
        sealed around each side of the product. Not to be confused with
        single-sided Blister pack
    :cvar VALUE_03: Keep case Typical DVD-style packaging, sometimes
        known as an ‘Amaray’ case
    :cvar VALUE_05: Jewel case Typical CD-style packaging
    :cvar VALUE_06: Digipak Common CD-style packaging, a card folder
        with one or more panels incorporating a tray, hub or pocket to
        hold the disc(s)
    :cvar VALUE_09: In box Individual item, items or set in card box
        with separate or hinged lid: not to be confused with the
        commonly-used ‘boxed set’
    :cvar VALUE_10: Slip-cased Slip-case for single item only: German
        ‘Schuber’
    :cvar VALUE_11: Slip-cased set Slip-case for multi-volume set:
        German ‘Kassette’; also commonly referred to as ‘boxed set’
    :cvar VALUE_12: Tube Rolled in tube or cylinder: eg sheet map or
        poster
    :cvar VALUE_13: Binder Use for miscellaneous items such as slides,
        microfiche, when presented in a binder
    :cvar VALUE_14: In wallet or folder Use for miscellaneous items such
        as slides, microfiche, when presented in a wallet or folder
    :cvar VALUE_15: Long triangular package Long package with triangular
        cross-section used for rolled sheet maps, posters etc
    :cvar VALUE_16: Long square package Long package with square cross-
        section used for rolled sheet maps, posters, etc
    :cvar VALUE_17: Softbox (for DVD)
    :cvar VALUE_18: Pouch In pouch, eg teaching materials in a plastic
        bag or pouch
    :cvar VALUE_19: Rigid plastic case In duroplastic or other rigid
        plastic case, eg for a class set
    :cvar VALUE_20: Cardboard case In cardboard case, eg for a class set
    :cvar VALUE_21: Shrink-wrapped Use for products or product bundles
        supplied for retail sale in shrink-wrapped packaging. For
        shrink-wrapped packs of multiple products for trade supply only,
        see code XL in List 7
    :cvar VALUE_22: Blister pack A pack comprising a pre-formed plastic
        blister and a printed card with a heat-seal coating
    :cvar VALUE_23: Carry case A case with carrying handle, typically
        for a set of educational books and/or learning materials
    :cvar VALUE_24: In tin Individual item, items or set in metal box or
        can with separate or hinged lid
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"


class List81(Enum):
    """
    Product content type.

    :cvar VALUE_10: Text (eye-readable) Readable text of the main work:
        this value is required, together with applicable
        &lt;ProductForm&gt; and &lt;ProductFormDetail&gt; values, to
        designate an e-book or other digital product whose primary
        content is eye-readable text
    :cvar VALUE_15: Extensive links between internal content
        E-publication is enhanced with a significant number of
        actionable cross-references, hyperlinked notes and annotations,
        or with other links between largely textual elements (eg
        quiz/test questions, ‘choose your own ending’ etc)
    :cvar VALUE_14: Extensive links to external content E-publication is
        enhanced with a significant number of actionable (clickable) web
        links
    :cvar VALUE_16: Additional eye-readable text not part of main work
        E-publication is enhanced with additional textual content such
        as interview, feature article, essay, bibliography, quiz/test,
        other background material or text that is not included in a
        primary or ‘unenhanced’ version
    :cvar VALUE_17: Promotional text for other book product eg Teaser
        chapter
    :cvar VALUE_11: Musical notation
    :cvar VALUE_07: Still images / graphics Use only when no more
        detailed specification is provided
    :cvar VALUE_18: Photographs Whether in a plate section / insert, or
        not
    :cvar VALUE_19: Figures, diagrams, charts, graphs Including other
        ‘mechanical’ (ie non-photographic) illustrations
    :cvar VALUE_20: Additional images / graphics not part of main work
        E-publication is enhanced with additional images or graphical
        content such as supplementary photographs that are not included
        in a primary or ‘unenhanced’ version
    :cvar VALUE_12: Maps and/or other cartographic content
    :cvar VALUE_01: Audiobook Audio recording of a reading of a book or
        other text
    :cvar VALUE_02: Performance – spoken word Audio recording of a drama
        or other spoken word performance
    :cvar VALUE_13: Other speech content eg an interview, not a
        ‘reading’ or ‘performance’)
    :cvar VALUE_03: Music recording Audio recording of a music
        performance, including musical drama and opera
    :cvar VALUE_04: Other audio Audio recording of other sound, eg
        birdsong
    :cvar VALUE_21: Partial performance – spoken word Audio recording of
        a reading, performance or dramatization of part of the work
    :cvar VALUE_22: Additional audio content not part of main work
        Product is enhanced with audio recording of full or partial
        reading, performance, dramatization, interview, background
        documentary or other audio content not included in the primary
        or ‘unenhanced’ version
    :cvar VALUE_23: Promotional audio for other book product eg Reading
        of teaser chapter
    :cvar VALUE_06: Video Includes Film, video, animation etc. Use only
        when no more detailed specification is provided. Formerly
        ‘Moving images’
    :cvar VALUE_26: Video recording of a reading
    :cvar VALUE_27: Performance – visual Video recording of a drama or
        other performance, including musical performance
    :cvar VALUE_24: Animated / interactive illustrations eg animated
        diagrams, charts, graphs or other illustrations
    :cvar VALUE_25: Narrative animation eg cartoon, animatic or CGI
        animation
    :cvar VALUE_28: Other video Other video content eg interview, not a
        reading or performance
    :cvar VALUE_29: Partial performance – video Video recording of a
        reading, performance or dramatization of part of the work
    :cvar VALUE_30: Additional video content not part of main work
        E-publication is enhanced with video recording of full or
        partial reading, performance, dramatization, interview,
        background documentary or other content not included in the
        primary or ‘unenhanced’ version
    :cvar VALUE_31: Promotional video for other book product eg Book
        trailer
    :cvar VALUE_05: Game / Puzzle No multi-user functionality. Formerly
        just ‘Game’
    :cvar VALUE_32: Contest Includes some degree of multi-user
        functionality
    :cvar VALUE_08: Software Largely ‘content free’
    :cvar VALUE_09: Data Data files
    :cvar VALUE_33: Data set plus software
    :cvar VALUE_34: Blank pages Intended to be filled in by the reader
    :cvar VALUE_35: Advertising content Use only where type of
        advertising content is not stated
    :cvar VALUE_37: Advertising – first party ‘Back ads’ – promotional
        pages for other books (that do not include sample content, cf
        codes 17, 23)
    :cvar VALUE_36: Advertising – coupons Eg to obtain discounts on
        other products
    :cvar VALUE_38: Advertising – third party display
    :cvar VALUE_39: Advertising – third party textual
    """
    VALUE_10 = "10"
    VALUE_15 = "15"
    VALUE_14 = "14"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_11 = "11"
    VALUE_07 = "07"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_12 = "12"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_13 = "13"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_06 = "06"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_05 = "05"
    VALUE_32 = "32"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_33 = "33"
    VALUE_34 = "34"
    VALUE_35 = "35"
    VALUE_37 = "37"
    VALUE_36 = "36"
    VALUE_38 = "38"
    VALUE_39 = "39"


class List82(Enum):
    """
    Bible contents.

    :cvar AP: Apocrypha (Catholic canon) The seven portions of the
        Apocrypha added to the Catholic canon at the Council of Trent in
        1546: Tobit; Judith; Wisdom of Solomon; Sirach (Ecclesiasticus);
        Baruch, including the Letter of Jeremiah; I and II Maccabees;
        Extra portions of Esther and Daniel (Additions to Esther; the
        Prayer of Azariah; Song of the Three Jews; Susannah; Bel and the
        Dragon). These are not generally included in the Protestant
        canon
    :cvar AQ: Apocrypha (canon unspecified) A collection of Apocryphal
        texts, canon not specified
    :cvar AX: Additional Apocryphal texts: Greek Orthodox canon I
        Esdras; Prayer of Manasseh; Psalm 151; III Maccabees
    :cvar AY: Additional Apocryphal texts: Slavonic Orthodox canon I and
        II Esdras; Prayer of Manasseh; Psalm 151; III and IV Maccabees
    :cvar AZ: Additional Apocryphal texts Additional Apocryphal texts
        included in some Bible versions: I and II Esdras; Prayer of
        Manasseh
    :cvar GA: General canon with Apocrypha (Catholic canon) The 66 books
        included in the Protestant, Catholic and Orthodox canons,
        together with the seven portions of the Apocrypha included in
        the Catholic canon. (Equivalent to OT plus NT plus AP)
    :cvar GC: General canon with Apocryphal texts (canon unspecified)
        The 66 books included in the Protestant, Catholic and Orthodox
        canons, together with Apocryphal texts, canon not specified.
        (Equivalent to OT plus NT plus AQ)
    :cvar GE: General canon The 66 books included in the Protestant,
        Catholic and Orthodox canons, 39 from the Old Testament and 27
        from the New Testament. The sequence of books may differ in
        different canons. (Equivalent to OT plus NT)
    :cvar GS: Gospels The books of Matthew, Mark, Luke and John
    :cvar OT: Old Testament Those 39 books which were included in the
        Jewish canon by the rabbinical academy established at Jamma in
        90 CE. Also known as the Jewish or Hebrew scriptures
    :cvar NT: New Testament The 27 books included in the Christian canon
        through the Easter Letter of Athanasius, Bishop of Alexandria
        and also by a general council of the Christian church held near
        the end of the 4th century CE
    :cvar NP: New Testament with Psalms and Proverbs Includes the 27
        books of the New Testament plus Psalms and Proverbs from the Old
        Testament. Equivalent to NT plus PP)
    :cvar PE: Paul’s Epistles The books containing the letters of Paul
        to the various early Christian churches
    :cvar PP: Psalms and Proverbs The book of Psalms and the book of
        Proverbs combined
    :cvar PS: Psalms The book of Psalms
    :cvar PT: Pentateuch The first five books of the Bible: Genesis,
        Exodus, Numbers, Leviticus, Deuteronomy. Also applied to the
        Torah
    :cvar ZZ: Other portions Selected books of either the OT or NT not
        otherwise noted
    """
    AP = "AP"
    AQ = "AQ"
    AX = "AX"
    AY = "AY"
    AZ = "AZ"
    GA = "GA"
    GC = "GC"
    GE = "GE"
    GS = "GS"
    OT = "OT"
    NT = "NT"
    NP = "NP"
    PE = "PE"
    PP = "PP"
    PS = "PS"
    PT = "PT"
    ZZ = "ZZ"


class List83(Enum):
    """
    Bible version.

    :cvar ALV: Alberto Vaccari Alberto Vaccari – Pontificio Istituto
        Biblico
    :cvar AMP: Amplified A translation based on the American Standard
        Version and showing multiple options for the translation of
        ancient text. Published in full in 1965. Sponsored by the
        Lockman Foundation
    :cvar ANM: Antonio Martini Most popular Catholic Bible translation
        in Italian prior to the CEI translation in 1971
    :cvar ASV: American Standard A 1901 translation using verbal
        equivalence techniques with the purpose of Americanizing the REV
    :cvar CEB: Common English Bible 2011 contemporary English
        translation of the Bible sponsored by the US-based Christian
        Resources Development Corporation. The translation includes Old
        Testament, Apocrypha and New Testament, and is aimed to be
        accessible to most English readers (minimum 7th grade reading
        age)
    :cvar CEI: Conferenza Episcopale Italiana Italian Episcopal
        Conference 1971 translation suitable for Italian Catholic
        liturgy. (Includes minor 1974 revision)
    :cvar CEN: Conferenza Episcopale Italiana 2008 New translation of
        the C.E.I. first published in 2008 – the version most widely
        used by the Italian Catholic Church
    :cvar CEV: Contemporary English A translation completed in 1995 and
        sponsored by the American Bible Society under the leadership of
        Barclay Newman
    :cvar CNC: Concordata 1968 Interfaith version promoted by the
        Italian Bible Society. Has a Catholic ‘imprimateur’, but its
        ecumenical approach has Jewish, Protestant and Christian
        Orthodox approval
    :cvar DDI: Diodati Version based on original documents, edited by
        Giovanni Diodati in 1607, revised by Diodati in 1641 and again
        in 1894. It is the reference version for many Italian
        Protestants
    :cvar DDN: Nuova Diodati Revision of the Diodati Bible dating to the
        1990s, aiming at highest fidelity to original ancient Greek (New
        Testament) and Hebrew (Old Testament) texts
    :cvar DOU: Douay-Rheims An early (1580-1609) English translation
        from the Latin Vulgate designed for Catholics and performed by
        George Martin
    :cvar EIN: Einheitsübersetzung A German translation of the Bible for
        use in Roman Catholic churches
    :cvar ESV: English Standard An update of the Revised Standard
        Version that makes ‘modest’ use of gender-free terminology
    :cvar FBB: Biblia (1776) Finnish Bible translation
    :cvar FRA: Raamattu (1933/1938) Finnish Bible translation
    :cvar FRK: Raamattu kansalle Finnish Bible translation
    :cvar FRM: Raamattu (1992) Finnish Bible translation
    :cvar GDW: God’s Word A 1995 translation by the World Bible
        Publishing Company using the English language in a manner to
        communicate to the late 20th century American
    :cvar GEN: Geneva An early (1560) English version of the Bible
        translated by William Whittingham with strong Protestant
        leanings
    :cvar GNB: Good News A translation sponsored by the American Bible
        Society. The New Testament was first published (as ‘Today’s
        English Version’ TEV) in 1966. The Old Testament was completed
        in 1976, and the whole was published as the ‘Good News Bible’
    :cvar GPR: Galbiati, Penna, Rossano – UTET Version edited by E.
        Galbiati, A. Penna and P. Rossano, and published by UTET. This
        version, based on original texts, is rich in notes and has been
        used as the basis for CEI translation
    :cvar GRK: Original Greek New Testament text in an original Greek
        version
    :cvar GRM: Garofano, Rinaldi – Marietti Richly annotated 1963
        Version edited by S. Garofano and S. Rinaldi, and published by
        Marietti
    :cvar HBR: Original Hebrew Old Testament text in an original Hebrew
        version
    :cvar HCS: Holman Christian Standard Published by Broadman and
        Holman this translation rejects all forms of gender-neutral
        wording and is written with strong influences from the Southern
        Baptist perspective of biblical scholarship
    :cvar ICB: International Children’s A translation completed in 1986
        targeting readability at the US third grade level
    :cvar ILC: Traduzione Interconfessionale in Lingua Corrente
        Interconfessional translation resulting from 1985 effort by
        Catholic and Protestant scholars, aimed at delivering an easy-
        to-understand message
    :cvar JER: Jerusalem A translation designed for English speaking
        Catholics based on the original languages. It is based on French
        as well as ancient texts and was first published in 1966
    :cvar KJV: King James A translation commissioned by King James I of
        England and first published in 1611
    :cvar KJT: 21st Century King James A verbal translation led by
        William Prindele. Published in 1994, it was designed to
        modernize the language of the King James Version based on
        Webster’s New International Dictionary, 2nd edition, unabridged
    :cvar LVB: Living Bible A paraphrase translation led by Kenneth N
        Taylor and first published in 1972
    :cvar LZZ: Luzzi 1924 translation by Giovanni Luzzi, Professor at
        the Waldensian Faculty of Theology in Rome, who revised the 17th
        Century Diodati version
    :cvar MSG: Message Bible A paraphrase translation of the New
        Testament by Eugene Peterson first published in 1993
    :cvar NAB: New American A translation aimed at Catholic readers
        first published in its entirety in 1970. A revised New Testament
        was issued in 1986 as the 2nd Edition. The 3rd Edtion was
        published in 1991 with a revision to Psalms. The 4th Edition
        (also known as the New American Bible Revised Edition) was
        published in 2011, incorporating revisions to the Old Testament
    :cvar NAS: New American Standard A translation commissioned by the
        Lockman Foundation. The New Testament was published in 1960
        followed by the entire Bible in 1971
    :cvar NAU: New American Standard, Updated A 1995 translation using
        more modern language than the NASB
    :cvar NBA: Bibelen 1895 Norwegian Bible translation
    :cvar NBB: Bibelen 1930 Norwegian Bible translation
    :cvar NBC: Bibelen 1938 Norwegian Bible translation
    :cvar NBD: Bibelen 1978-85 Norwegian Bible translation
    :cvar NBE: Bibelen 1978 Norwegian Bible translation
    :cvar NBF: Bibelen 1985 Norwegian Bible translation
    :cvar NBG: Bibelen 1988 Norwegian Bible translation
    :cvar NBH: Bibelen 1978-85/rev. 2005 Norwegian Bible translation
    :cvar NBI: Bibelen 2011 Norwegian Bible translation
    :cvar NCV: New Century A translation inspired by the International
        Children’s version. First published by World Publishing in 1991
    :cvar NEB: New English A translation first issued in 1961 (New
        Testament) and 1970 (complete Bible) as a result of a proposal
        at the 1946 General Assembly of the Church of Scotland
    :cvar NGO: Bibelen Guds ord Norwegian Bible translation
    :cvar NIV: New International A translation underwritten by Biblica
        (formerly the International Bible Society, and previously the
        New York Bible Society). The New Testament was published in 1973
        followed by the entire Bible in 1978. The NIV text was revised
        in 1984 and again in 2011
    :cvar NIR: New International Reader’s A 1996 translation designed
        for people with limited literacy in English and based on the NIV
    :cvar NJB: New Jerusalem A revision of the Jerusalem Bible. First
        published in 1986
    :cvar NKJ: New King James A version issued by Thomas Nelson
        Publishers in 1982-83 designed to update the language of the
        King James Version while maintaining the phrasing and rhythm and
        using the same sources as its predecessor
    :cvar NNK: Bibelen, nynorsk Norwegian ‘nynorsk’ Bible translation
    :cvar NLV: New Living A translation sponsored by Tyndale House and
        first released in 1996. It is considered a revision and updating
        of the Living Bible
    :cvar NRS: New Revised Standard A revision of the Revised Standard
        based on ancient texts but updating language to American usage
        of the 1980s
    :cvar NTV: Nueva Traduccion Vivienta A Spanish translation from the
        original Greek and Hebrew, sponsored by Tyndale House
    :cvar NVB: Novissima Versione della Bibbia Nuovissima version – a
        Catholic-oriented translation in modern Italian, edited by a
        group including Carlo Martini, Gianfranco Ravasi and Ugo Vanni
        and first published (in 48 volumes, 1967-1980) by Edizioni San
        Paolo
    :cvar NVD: Nueva Biblia al Dia A Spanish translation from the
        original Greek and Hebrew, sponsored by the International Bible
        Society/Sociedad Bíblica Internacional
    :cvar NVI: Nueva Version Internacional A Spanish translation
        underwritten by the International Bible Society
    :cvar PHP: New Testament in Modern English (Phillips) An idiomatic
        translation by J B Phillips, first completed in 1966
    :cvar REB: Revised English A 1989 revision of the NEB. A significant
        effort was made to reduce the British flavor present in the NEB
    :cvar REV: Revised Version The first major revision of the King
        James Version, the Revised Version incorporates insights from
        early manuscripts discovered between 1611 and 1870, and corrects
        readings in the KJV which nineteenth-century scholarship deemed
        mistaken. The New Testament was published in 1881, the Old
        Testament in 1885, and the Apocrypha in 1895
    :cvar RSV: Revised Standard A translation authorized by the National
        Council of Churches of Christ in the USA. The New Testament was
        published in 1946 followed by a complete Protestant canon in
        1951
    :cvar RVL: Reina Valera A Spanish translation based on the original
        texts
    :cvar SBB: Bibel 2000 Swedish Bible translation
    :cvar SMK: Bibelen, samisk Norwegian ‘samisk’ Bible translation
    :cvar TEV: Today’s English A translation of the New Testament
        sponsored by the American Bible Society and first published in
        1966. It was incorporated into the ‘Good News Bible’ (GNB) in
        1976
    :cvar TNI: Today’s New International An updating of the New
        International Version. The New Testament was published in 2002,
        and the entire Bible in 2005. Superseded by the 2011 NIV update
    :cvar ZZZ: Other Other translations not otherwise noted
    """
    ALV = "ALV"
    AMP = "AMP"
    ANM = "ANM"
    ASV = "ASV"
    CEB = "CEB"
    CEI = "CEI"
    CEN = "CEN"
    CEV = "CEV"
    CNC = "CNC"
    DDI = "DDI"
    DDN = "DDN"
    DOU = "DOU"
    EIN = "EIN"
    ESV = "ESV"
    FBB = "FBB"
    FRA = "FRA"
    FRK = "FRK"
    FRM = "FRM"
    GDW = "GDW"
    GEN = "GEN"
    GNB = "GNB"
    GPR = "GPR"
    GRK = "GRK"
    GRM = "GRM"
    HBR = "HBR"
    HCS = "HCS"
    ICB = "ICB"
    ILC = "ILC"
    JER = "JER"
    KJV = "KJV"
    KJT = "KJT"
    LVB = "LVB"
    LZZ = "LZZ"
    MSG = "MSG"
    NAB = "NAB"
    NAS = "NAS"
    NAU = "NAU"
    NBA = "NBA"
    NBB = "NBB"
    NBC = "NBC"
    NBD = "NBD"
    NBE = "NBE"
    NBF = "NBF"
    NBG = "NBG"
    NBH = "NBH"
    NBI = "NBI"
    NCV = "NCV"
    NEB = "NEB"
    NGO = "NGO"
    NIV = "NIV"
    NIR = "NIR"
    NJB = "NJB"
    NKJ = "NKJ"
    NNK = "NNK"
    NLV = "NLV"
    NRS = "NRS"
    NTV = "NTV"
    NVB = "NVB"
    NVD = "NVD"
    NVI = "NVI"
    PHP = "PHP"
    REB = "REB"
    REV = "REV"
    RSV = "RSV"
    RVL = "RVL"
    SBB = "SBB"
    SMK = "SMK"
    TEV = "TEV"
    TNI = "TNI"
    ZZZ = "ZZZ"


class List84(Enum):
    """
    Study Bible type.

    :cvar CAM: Cambridge Annotated Contains the work of Howard Clark Kee
        including a summary of the development of the canon,
        introductions to the books, notes and cross references.
        Originally published in 1993, NRSV
    :cvar LIF: Life Application A project of Tyndale House Publishers
        and Zondervan intended to help readers apply the Bible to daily
        living. Living Bible, King James, New International, NASB
    :cvar MAC: Macarthur A King James version study Bible with notes by
        James Macarthur first published in 1997
    :cvar OXF: Oxford Annotated A study Bible originally published in
        the 1960s and based on the RSV / NRSV
    :cvar NNT: Studiebibel, Det Nye testamentet Norwegian study Bible,
        New Testament
    :cvar NOX: New Oxford Annotated Published in 1991 and based on the
        New Revised Standard version
    :cvar NSB: Norsk studiebibel Norwegian study Bible
    :cvar RYR: Ryrie Based on the work of Charles C. Ryrie. King James,
        NI, NASB
    :cvar SCO: Scofield A study Bible based on the early 20th century
        work of C.I. Scofield. Based on the King James version
    :cvar SPR: Spirit Filled A transdenominational study Bible for
        persons from the Pentecostal/Charismatic traditions
    """
    CAM = "CAM"
    LIF = "LIF"
    MAC = "MAC"
    OXF = "OXF"
    NNT = "NNT"
    NOX = "NOX"
    NSB = "NSB"
    RYR = "RYR"
    SCO = "SCO"
    SPR = "SPR"


class List85(Enum):
    """
    Bible purpose.

    :cvar AW: Award A Bible (or selected Biblical text) designed for
        presentation from a religious organization
    :cvar BB: Baby A Bible (or selected Biblical text) designed to be a
        gift to commemorate a child’s birth
    :cvar BR: Bride A special gift Bible (or selected Biblical text)
        designed for the bride on her wedding day. Usually white
    :cvar CF: Confirmation A Bible (or selected Biblical text) designed
        to be used in the confirmation reading or as a gift to a
        confirmand
    :cvar CH: Children’s A text Bible (or selected Biblical text)
        designed in presentation and readability for a child
    :cvar CM: Compact A small Bible (or selected Biblical text) with a
        trim height of five inches or less
    :cvar CR: Cross-reference A Bible (or selected Biblical text) which
        includes text conveying cross-references to related scripture
        passages
    :cvar DR: Daily readings A Bible (or selected Biblical text) laid
        out to provide readings for each day of the year
    :cvar DV: Devotional A Bible (or selected Biblical text) containing
        devotional content together with the scripture
    :cvar FM: Family A Bible (or selected Biblical text) containing
        family record pages and/or additional study material for family
        devotion
    :cvar GT: General/Text A standard Bible (or selected Biblical text)
        of any version with no distinguishing characteristics beyond the
        canonical text
    :cvar GF: Gift A Bible (or selected Biblical text) designed for gift
        or presentation, often including a presentation page
    :cvar LP: Lectern/Pulpit A large Bible (or selected Biblical text)
        with large print designed for use in reading scriptures in
        public worship from either the pulpit or lectern
    :cvar MN: Men’s A Bible (or selected Biblical text) especially
        designed with helps and study guides oriented to the adult male
    :cvar PS: Primary school A Bible (or selected Biblical text)
        designed for use in primary school
    :cvar PW: Pew Usually inexpensive but sturdy, a Bible (or selected
        Biblical text) designed for use in church pews
    :cvar SC: Scholarly A Bible (or selected Biblical text) including
        texts in Greek and/or Hebrew and designed for scholarly study
    :cvar SL: Slimline
    :cvar ST: Student A Bible (or selected Biblical text) with study
        articles and helps especially for use in the classroom
    :cvar SU: Study A Bible (or selected Biblical text) with many extra
        features, e.g. book introductions, dictionary, concordance,
        references, maps, etc., to help readers better understand the
        scripture
    :cvar WG: Wedding gift A special gift Bible (or selected Biblical
        text) designed as a gift to the couple on their wedding day
    :cvar WM: Women’s A devotional or study Bible (or selected Biblical
        text) with helps targeted at the adult woman
    :cvar YT: Youth A Bible (or selected Biblical text) containing
        special study and devotional helps designed specifically for the
        needs of teenagers
    """
    AW = "AW"
    BB = "BB"
    BR = "BR"
    CF = "CF"
    CH = "CH"
    CM = "CM"
    CR = "CR"
    DR = "DR"
    DV = "DV"
    FM = "FM"
    GT = "GT"
    GF = "GF"
    LP = "LP"
    MN = "MN"
    PS = "PS"
    PW = "PW"
    SC = "SC"
    SL = "SL"
    ST = "ST"
    SU = "SU"
    WG = "WG"
    WM = "WM"
    YT = "YT"


class List86(Enum):
    """
    Bible text organization.

    :cvar CHR: Chronological A Bible with the text organized in the
        order in which events are believed to have happened
    :cvar CHA: Chain reference A Bible which explores keywords or themes
        by referring text to preceding or following text
    :cvar INT: Interlinear A Bible or other text in which different
        versions are printed one line above the other, so that the
        variations can easily be detected
    :cvar PAR: Parallel A Bible with two or more versions printed side
        by side
    :cvar STN: Standard A Bible in which the text is presented in the
        traditional order
    """
    CHR = "CHR"
    CHA = "CHA"
    INT = "INT"
    PAR = "PAR"
    STN = "STN"


class List87(Enum):
    """
    Bible reference location.

    :cvar CCL: Center column References are printed in a narrow column
        in the center of the page between two columns of text
    :cvar PGE: Page end References are printed at the foot of the page
    :cvar SID: Side column References are printed in a column to the
        side of the scripture
    :cvar VER: Verse end References are printed at the end of the
        applicable verse
    :cvar UNK: Unknown The person creating the ONIX record does not know
        where the references are located
    :cvar ZZZ: Other Other locations not otherwise identified
    """
    CCL = "CCL"
    PGE = "PGE"
    SID = "SID"
    VER = "VER"
    UNK = "UNK"
    ZZZ = "ZZZ"


class List89(Enum):
    """
    Religious text feature type.

    :cvar VALUE_01: Church season or activity A church season or
        activity for which a religious text is intended. Religious text
        feature code must be taken from List 90
    """
    VALUE_01 = "01"


class List9(Enum):
    """
    Product classification type code.

    :cvar VALUE_01: WCO Harmonized System World Customs Organization
        Harmonized Commodity Coding and Description System. Use 6 or 8
        digits, without punctuation
    :cvar VALUE_02: UNSPSC UN Standard Product and Service
        Classification
    :cvar VALUE_03: HMRC UK Revenue and Customs classifications, based
        on the Harmonized System
    :cvar VALUE_04: Warenverzeichnis für die Außenhandelsstatistik
        German export trade classification, based on the Harmonised
        System
    :cvar VALUE_05: TARIC EU TARIC codes, an extended version of the
        Harmonized System
    :cvar VALUE_06: Fondsgroep Centraal Boekhuis free classification
        field for publishers
    :cvar VALUE_07: Sender’s product category A product category (not a
        subject classification) assigned by the sender
    :cvar VALUE_08: GAPP Product Class Product classification maintained
        by the Chinese General Administration of Press and Publication
        (http://www.gapp.gov.cn)
    :cvar VALUE_09: CPA Statistical Classification of Products by
        Activity in the European Economic Community, see
        http://ec.europa.eu/eurostat/ramon/nomenclatures/index.cfm?TargetUrl=LST_NOM_DTL&amp;StrNom=CPA_2008.
        Up to six digits, with one or two periods. For example, printed
        children’s books are ‘58.11.13’, but the periods are normally
        ommited in ONIX
    :cvar VALUE_10: NCM Mercosur/Mercosul Common Nomenclature, based on
        the Harmonised System
    :cvar VALUE_11: CPV Common Procurement Vocabulary, uses to describe
        requirements for tender for public tendering and procurement
        within the EU. Code is a nine digit number (including the check
        digit). See http://eur-lex.europa.eu/legal-
        content/EN/TXT/?uri=URISERV:l22008
    :cvar VALUE_50: Electre genre Typologie de marché géré par Electre
        (Market segment code maintained by Electre)
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_50 = "50"


class List90(Enum):
    """
    Religious text feature code.

    :cvar VALUE_01: Academic year Use with code 01 in
        &lt;ReligiousTextFeatureType&gt;
    :cvar VALUE_02: Catechistic year Use with code 01 in
        &lt;ReligiousTextFeatureType&gt;
    :cvar VALUE_03: Liturgical year Use with code 01 in
        &lt;ReligiousTextFeatureType&gt;
    :cvar VALUE_04: Advent and Christmas Use with code 01 in
        &lt;ReligiousTextFeatureType&gt;
    :cvar VALUE_05: Blessings Use with code 01 in
        &lt;ReligiousTextFeatureType&gt;
    :cvar VALUE_06: Scholastic cycles Use with code 01 in
        &lt;ReligiousTextFeatureType&gt;
    :cvar VALUE_07: Confirmation and Holy Communion Use with code 01 in
        &lt;ReligiousTextFeatureType&gt;
    :cvar VALUE_08: Summer activites For example, summer camps and other
        youth recreational activities: use with code 01 in
        &lt;ReligiousTextFeatureType&gt;
    :cvar VALUE_09: Easter Use with code 01 in
        &lt;ReligiousTextFeatureType&gt;
    :cvar VALUE_10: Lent Use with code 01 in
        &lt;ReligiousTextFeatureType&gt;
    :cvar VALUE_11: Marian themes Use with code 01 in
        &lt;ReligiousTextFeatureType&gt;
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"


class List91(Enum):
    """
    Country code – ISO 3166-1.

    :cvar AD: Andorra
    :cvar AE: United Arab Emirates
    :cvar AF: Afghanistan
    :cvar AG: Antigua and Barbuda
    :cvar AI: Anguilla
    :cvar AL: Albania
    :cvar AM: Armenia
    :cvar AN: Netherlands Antilles Deprecated – use BQ, CW or SX as
        appropriate
    :cvar AO: Angola
    :cvar AQ: Antarctica
    :cvar AR: Argentina
    :cvar AS: American Samoa
    :cvar AT: Austria
    :cvar AU: Australia
    :cvar AW: Aruba
    :cvar AX: Åland Islands
    :cvar AZ: Azerbaijan
    :cvar BA: Bosnia and Herzegovina
    :cvar BB: Barbados
    :cvar BD: Bangladesh
    :cvar BE: Belgium
    :cvar BF: Burkina Faso
    :cvar BG: Bulgaria
    :cvar BH: Bahrain
    :cvar BI: Burundi
    :cvar BJ: Benin
    :cvar BL: Saint Barthélemy
    :cvar BM: Bermuda
    :cvar BN: Brunei Darussalam
    :cvar BO: Bolivia, Plurinational State of
    :cvar BQ: Bonaire, Sint Eustatius and Saba
    :cvar BR: Brazil
    :cvar BS: Bahamas
    :cvar BT: Bhutan
    :cvar BV: Bouvet Island
    :cvar BW: Botswana
    :cvar BY: Belarus
    :cvar BZ: Belize
    :cvar CA: Canada
    :cvar CC: Cocos (Keeling) Islands
    :cvar CD: Congo, Democratic Republic of the
    :cvar CF: Central African Republic
    :cvar CG: Congo
    :cvar CH: Switzerland
    :cvar CI: Cote d’Ivoire
    :cvar CK: Cook Islands
    :cvar CL: Chile
    :cvar CM: Cameroon
    :cvar CN: China
    :cvar CO: Colombia
    :cvar CR: Costa Rica
    :cvar CS: Serbia and Montenegro DEPRECATED, replaced by ME –
        Montenegro and RS – Serbia
    :cvar CU: Cuba
    :cvar CV: Cabo Verde
    :cvar CW: Curaçao
    :cvar CX: Christmas Island
    :cvar CY: Cyprus
    :cvar CZ: Czech Republic
    :cvar DE: Germany
    :cvar DJ: Djibouti
    :cvar DK: Denmark
    :cvar DM: Dominica
    :cvar DO: Dominican Republic
    :cvar DZ: Algeria
    :cvar EC: Ecuador
    :cvar EE: Estonia
    :cvar EG: Egypt
    :cvar EH: Western Sahara
    :cvar ER: Eritrea
    :cvar ES: Spain
    :cvar ET: Ethiopia
    :cvar FI: Finland
    :cvar FJ: Fiji
    :cvar FK: Falkland Islands (Malvinas)
    :cvar FM: Micronesia, Federated States of
    :cvar FO: Faroe Islands
    :cvar FR: France
    :cvar GA: Gabon
    :cvar GB: United Kingdom
    :cvar GD: Grenada
    :cvar GE: Georgia
    :cvar GF: French Guiana
    :cvar GG: Guernsey
    :cvar GH: Ghana
    :cvar GI: Gibraltar
    :cvar GL: Greenland
    :cvar GM: Gambia
    :cvar GN: Guinea
    :cvar GP: Guadeloupe
    :cvar GQ: Equatorial Guinea
    :cvar GR: Greece
    :cvar GS: South Georgia and the South Sandwich Islands
    :cvar GT: Guatemala
    :cvar GU: Guam
    :cvar GW: Guinea-Bissau
    :cvar GY: Guyana
    :cvar HK: Hong Kong
    :cvar HM: Heard Island and McDonald Islands
    :cvar HN: Honduras
    :cvar HR: Croatia
    :cvar HT: Haiti
    :cvar HU: Hungary
    :cvar ID: Indonesia
    :cvar IE: Ireland
    :cvar IL: Israel
    :cvar IM: Isle of Man
    :cvar IN: India
    :cvar IO: British Indian Ocean Territory
    :cvar IQ: Iraq
    :cvar IR: Iran, Islamic Republic of
    :cvar IS: Iceland
    :cvar IT: Italy
    :cvar JE: Jersey
    :cvar JM: Jamaica
    :cvar JO: Jordan
    :cvar JP: Japan
    :cvar KE: Kenya
    :cvar KG: Kyrgyzstan
    :cvar KH: Cambodia
    :cvar KI: Kiribati
    :cvar KM: Comoros
    :cvar KN: Saint Kitts and Nevis
    :cvar KP: Korea, Democratic People’s Republic of
    :cvar KR: Korea, Republic of
    :cvar KW: Kuwait
    :cvar KY: Cayman Islands
    :cvar KZ: Kazakhstan
    :cvar LA: Lao People’s Democratic Republic
    :cvar LB: Lebanon
    :cvar LC: Saint Lucia
    :cvar LI: Liechtenstein
    :cvar LK: Sri Lanka
    :cvar LR: Liberia
    :cvar LS: Lesotho
    :cvar LT: Lithuania
    :cvar LU: Luxembourg
    :cvar LV: Latvia
    :cvar LY: Libya
    :cvar MA: Morocco
    :cvar MC: Monaco
    :cvar MD: Moldova, Repubic of
    :cvar ME: Montenegro
    :cvar MF: Saint Martin (French part)
    :cvar MG: Madagascar
    :cvar MH: Marshall Islands
    :cvar MK: Macedonia, the former Yugoslav Republic of
    :cvar ML: Mali
    :cvar MM: Myanmar
    :cvar MN: Mongolia
    :cvar MO: Macao
    :cvar MP: Northern Mariana Islands
    :cvar MQ: Martinique
    :cvar MR: Mauritania
    :cvar MS: Montserrat
    :cvar MT: Malta
    :cvar MU: Mauritius
    :cvar MV: Maldives
    :cvar MW: Malawi
    :cvar MX: Mexico
    :cvar MY: Malaysia
    :cvar MZ: Mozambique
    :cvar NA: Namibia
    :cvar NC: New Caledonia
    :cvar NE: Niger
    :cvar NF: Norfolk Island
    :cvar NG: Nigeria
    :cvar NI: Nicaragua
    :cvar NL: Netherlands
    :cvar NO: Norway
    :cvar NP: Nepal
    :cvar NR: Nauru
    :cvar NU: Niue
    :cvar NZ: New Zealand
    :cvar OM: Oman
    :cvar PA: Panama
    :cvar PE: Peru
    :cvar PF: French Polynesia
    :cvar PG: Papua New Guinea
    :cvar PH: Philippines
    :cvar PK: Pakistan
    :cvar PL: Poland
    :cvar PM: Saint Pierre and Miquelon
    :cvar PN: Pitcairn
    :cvar PR: Puerto Rico
    :cvar PS: Palestine, State of
    :cvar PT: Portugal
    :cvar PW: Palau
    :cvar PY: Paraguay
    :cvar QA: Qatar
    :cvar RE: Réunion
    :cvar RO: Romania
    :cvar RS: Serbia
    :cvar RU: Russian Federation
    :cvar RW: Rwanda
    :cvar SA: Saudi Arabia
    :cvar SB: Solomon Islands
    :cvar SC: Seychelles
    :cvar SD: Sudan
    :cvar SE: Sweden
    :cvar SG: Singapore
    :cvar SH: Saint Helena, Ascension and Tristan da Cunha
    :cvar SI: Slovenia
    :cvar SJ: Svalbard and Jan Mayen
    :cvar SK: Slovakia
    :cvar SL: Sierra Leone
    :cvar SM: San Marino
    :cvar SN: Senegal
    :cvar SO: Somalia
    :cvar SR: Suriname
    :cvar SS: South Sudan
    :cvar ST: Sao Tome and Principe
    :cvar SV: El Salvador
    :cvar SX: Sint Maarten (Dutch part)
    :cvar SY: Syrian Arab Republic
    :cvar SZ: Swaziland
    :cvar TC: Turks and Caicos Islands
    :cvar TD: Chad
    :cvar TF: French Southern Territories
    :cvar TG: Togo
    :cvar TH: Thailand
    :cvar TJ: Tajikistan
    :cvar TK: Tokelau
    :cvar TL: Timor-Leste
    :cvar TM: Turkmenistan
    :cvar TN: Tunisia
    :cvar TO: Tonga
    :cvar TR: Turkey
    :cvar TT: Trinidad and Tobago
    :cvar TV: Tuvalu
    :cvar TW: Taiwan, Province of China
    :cvar TZ: Tanzania, United Republic of
    :cvar UA: Ukraine
    :cvar UG: Uganda
    :cvar UM: United States Minor Outlying Islands
    :cvar US: United States
    :cvar UY: Uruguay
    :cvar UZ: Uzbekistan
    :cvar VA: Holy See (Vatican City State)
    :cvar VC: Saint Vincent and the Grenadines
    :cvar VE: Venezuela, Bolivarian Republic of
    :cvar VG: Virgin Islands, British
    :cvar VI: Virgin Islands, US
    :cvar VN: Viet Nam
    :cvar VU: Vanuatu
    :cvar WF: Wallis and Futuna
    :cvar WS: Samoa
    :cvar YE: Yemen
    :cvar YT: Mayotte
    :cvar YU: Yugoslavia DEPRECATED, replaced by ME – Montenegro and RS
        – Serbia
    :cvar ZA: South Africa
    :cvar ZM: Zambia
    :cvar ZW: Zimbabwe
    """
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AN = "AN"
    AO = "AO"
    AQ = "AQ"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AX = "AX"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BQ = "BQ"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BV = "BV"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CS = "CS"
    CU = "CU"
    CV = "CV"
    CW = "CW"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    EH = "EH"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FM = "FM"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GF = "GF"
    GG = "GG"
    GH = "GH"
    GI = "GI"
    GL = "GL"
    GM = "GM"
    GN = "GN"
    GP = "GP"
    GQ = "GQ"
    GR = "GR"
    GS = "GS"
    GT = "GT"
    GU = "GU"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HM = "HM"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IQ = "IQ"
    IR = "IR"
    IS = "IS"
    IT = "IT"
    JE = "JE"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    ME = "ME"
    MF = "MF"
    MG = "MG"
    MH = "MH"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MQ = "MQ"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OM = "OM"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PR = "PR"
    PS = "PS"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SJ = "SJ"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SV = "SV"
    SX = "SX"
    SY = "SY"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TF = "TF"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    UM = "UM"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VI = "VI"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    YE = "YE"
    YT = "YT"
    YU = "YU"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"


class List92(Enum):
    """
    Supplier identifier type.

    :cvar VALUE_01: Proprietary Note that &lt;IDTypeName&gt; is required
        with proprietary identifiers
    :cvar VALUE_02: Proprietary DEPRECATED – use 01
    :cvar VALUE_04: Börsenverein Verkehrsnummer
    :cvar VALUE_05: German ISBN Agency publisher identifier
    :cvar VALUE_06: GLN GS1 global location number (formerly EAN
        location number)
    :cvar VALUE_07: SAN Book trade Standard Address Number – US, UK etc
    :cvar VALUE_12: Distributeurscode Boekenbank Flemish supplier code
    :cvar VALUE_13: Fondscode Boekenbank Flemish publisher code
    :cvar VALUE_23: VAT Identity Number Identifier for a business
        organization for VAT purposes, eg within the EU’s VIES system.
        See http://ec.europa.eu/taxation_customs/vies/faqvies.do for EU
        VAT ID formats, which vary from country to country. Generally
        these consist of a two-letter country code followed by the 8–12
        digits of the national VAT ID. Some countries include one or two
        letters within their VAT ID. See
        http://en.wikipedia.org/wiki/VAT_identification_number for non-
        EU countries that maintain similar identifiers. Spaces, dashes
        etc should be omitted
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_23 = "23"


class List93(Enum):
    """
    Supplier role.

    :cvar VALUE_00: Unspecified Default
    :cvar VALUE_01: Publisher to retailers Publisher as supplier to
        retail trade outlets
    :cvar VALUE_02: Publisher’s exclusive distributor to retailers
    :cvar VALUE_03: Publisher’s non-exclusive distributor to retailers
    :cvar VALUE_04: Wholesaler Wholesaler supplying retail trade outlets
    :cvar VALUE_05: Sales agent DEPRECATED – use
        &lt;MarketRepresentation&gt; (ONIX 2.1) or
        &lt;MarketPublishingDetail&gt; (ONIX 3.0) to specify a sales
        agent
    :cvar VALUE_06: Publisher’s distributor to retailers In a specified
        supply territory. Use only where exclusive/non-exclusive status
        is not known. Prefer 02 or 03 as appropriate, where possible
    :cvar VALUE_07: POD supplier Where a POD product is supplied to
        retailers and/or consumers direct from a POD source
    :cvar VALUE_08: Retailer
    :cvar VALUE_09: Publisher to end-customers Publisher as supplier
        direct to consumers and/or institutional customers
    :cvar VALUE_10: Exclusive distributor to end-customers Intermediary
        as exclusive distributor direct to consumers and/or
        institutional customers
    :cvar VALUE_11: Non-exclusive distributor to end-customers
        Intermediary as non-exclusive distributor direct to consumers
        and/or institutional customers
    :cvar VALUE_12: Distributor to end-customers Use only where
        exclusive/non-exclusive status is not known. Prefer 10 or 11 as
        appropriate, where possible
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"


class List94(Enum):
    """
    Default linear unit.

    :cvar CM: Centimeters Millimeters are the preferred metric unit of
        length
    :cvar IN: Inches (US)
    :cvar MM: Millimeters
    """
    CM = "cm"
    IN = "in"
    MM = "mm"


class List95(Enum):
    """
    Default unit of weight.

    :cvar LB: Pounds (US)
    :cvar GR: Grams
    :cvar OZ: Ounces (US)
    """
    LB = "lb"
    GR = "gr"
    OZ = "oz"


class List96(Enum):
    """
    Currency code – ISO 4217.

    :cvar AED: UAE Dirham United Arab Emirates
    :cvar AFA: Afghani Afghanistan. DEPRECATED, replaced by AFN
    :cvar AFN: Afghani Afghanistan (prices normally quoted as integers)
    :cvar ALL: Lek Albania (prices normally quoted as integers)
    :cvar AMD: Armenian Dram Armenia (prices normally quoted as
        integers)
    :cvar ANG: Netherlands Antillian Guilder Curaçao, Sint Maarten
    :cvar AOA: Kwanza Angola
    :cvar ARS: Argentine Peso Argentina
    :cvar ATS: Schilling Austria. Now replaced by the Euro (EUR): use
        only for historical prices that pre-date the introduction of the
        Euro
    :cvar AUD: Australian Dollar Australia, Christmas Island, Cocos
        (Keeling) Islands, Heard Island and McDonald Islands, Kiribati,
        Nauru, Norfolk Island, Tuvalu
    :cvar AWG: Aruban Florin Aruba
    :cvar AZN: Azerbaijanian Manat Azerbaijan
    :cvar BAM: Convertible Marks Bosnia and Herzegovina
    :cvar BBD: Barbados Dollar Barbados
    :cvar BDT: Taka Bangladesh
    :cvar BEF: Belgian Franc Belgium. Now replaced by the Euro (EUR):
        use only for historical prices that pre-date the introduction of
        the Euro
    :cvar BGL: Bulgarian Lev DEPRECATED, replaced by BGN
    :cvar BGN: Bulgarian Lev Bulgaria
    :cvar BHD: Bahraini Dinar Bahrain (prices normally quoted with 3
        decimal places)
    :cvar BIF: Burundi Franc Burundi (prices normally quoted as
        integers)
    :cvar BMD: Bermudian Dollar Bermuda
    :cvar BND: Brunei Dollar Brunei Darussalam
    :cvar BOB: Boliviano Bolivia
    :cvar BRL: Brazilian Real Brazil
    :cvar BSD: Bahamian Dollar Bahamas
    :cvar BTN: Ngultrun Bhutan
    :cvar BWP: Pula Botswana
    :cvar BYR: Belarussian Ruble Belarus (prices normally quoted as
        integers). Now replaced by new Belarussian Ruble (BYN): use only
        for historical prices that pre-date the introduction of the new
        Belarussian Ruble
    :cvar BYN: Belarussian Ruble Belarus
    :cvar BZD: Belize Dollar Belize
    :cvar CAD: Canadian Dollar Canada
    :cvar CDF: Franc Congolais Congo (Democratic Republic of the)
    :cvar CHF: Swiss Franc Switzerland, Liechtenstein
    :cvar CLP: Chilean Peso Chile (prices normally quoted as integers)
    :cvar CNY: Yuan Renminbi China
    :cvar COP: Colombian Peso Colombia (prices normally quoted as
        integers)
    :cvar CRC: Costa Rican Colon Costa Rica (prices normally quoted as
        integers)
    :cvar CSD: Serbian Dinar Deprecated, replaced by RSD
    :cvar CUC: Cuban Convertible Peso Cuba (alternative currency)
    :cvar CUP: Cuban Peso Cuba
    :cvar CVE: Cabo Verde Escudo Cabo Verde (prices normally quoted as
        integers)
    :cvar CYP: Cyprus Pound Cyprus. Now replaced by the Euro (EUR): use
        only for historical prices that pre-date the introduction of the
        Euro
    :cvar CZK: Czech Koruna Czech Republic
    :cvar DEM: Mark Germany. Now replaced by the Euro (EUR): use only
        for historical prices that pre-date the introduction of the Euro
    :cvar DJF: Djibouti Franc Djibouti (prices normally quoted as
        integers)
    :cvar DKK: Danish Krone Denmark, Faroe Islands, Greenland
    :cvar DOP: Dominican Peso Dominican Republic
    :cvar DZD: Algerian Dinar Algeria
    :cvar EEK: Kroon Estonia.Now replaced by the Euro (EUR): use only
        for historical prices that pre-date the introduction of the Euro
    :cvar EGP: Egyptian Pound Egypt
    :cvar ERN: Nakfa Eritrea
    :cvar ESP: Peseta Spain. Now replaced by the Euro (EUR): use only
        for historical prices that pre-date the introduction of the Euro
        (prices normally quoted as integers)
    :cvar ETB: Ethiopian Birr Ethiopia
    :cvar EUR: Euro Eurozone: Andorra, Austria, Belgium, Cyprus,
        Estonia, Finland, France, Fr Guiana, Fr S Territories, Germany,
        Greece, Guadeloupe, Holy See (Vatican City), Ireland, Italy,
        Latvia, Lithuania, Luxembourg, Martinique, Malta, Mayotte,
        Monaco, Montenegro, Netherlands, Portugal, Réunion, St
        Barthelemy, St Martin, St Pierre and Miquelon, San Marino,
        Slovakia, Slovenia, Spain
    :cvar FIM: Markka Finland. Now replaced by the Euro (EUR): use only
        for historical prices that pre-date the introduction of the Euro
    :cvar FJD: Fiji Dollar Fiji
    :cvar FKP: Falkland Islands Pound Falkland Islands (Malvinas)
    :cvar FRF: Franc France. Now replaced by the Euro (EUR): use only
        for historical prices that pre-date the introduction of the Euro
    :cvar GBP: Pound Sterling United Kingdom, Isle of Man, Channel
        Islands, South Georgia, South Sandwich Islands
    :cvar GEL: Lari Georgia
    :cvar GHC: Ghana Cedi Deprecated, replaced by GHS
    :cvar GHS: Ghana Cedi Ghana
    :cvar GIP: Gibraltar Pound Gibraltar
    :cvar GMD: Dalasi Gambia
    :cvar GNF: Guinea Franc Guinea (prices normally quoted as integers)
    :cvar GRD: Drachma Greece. Now replaced by the Euro (EUR): use only
        for historical prices that pre-date the introduction of the Euro
    :cvar GTQ: Quetzal Guatemala
    :cvar GWP: Guinea-Bissau Peso Now replaced by the CFA Franc BCEAO
        XOF use only for historical prices that pre-date use of the CFA
        Franc
    :cvar GYD: Guyana Dollar Guyana (prices normally quoted as integers)
    :cvar HKD: Hong Kong Dollar Hong Kong
    :cvar HNL: Lempira Honduras
    :cvar HRK: Kuna Croatia
    :cvar HTG: Gourde Haiti
    :cvar HUF: Forint Hungary (prices normally quoted as integers)
    :cvar IDR: Rupiah Indonesia (prices normally quoted as integers)
    :cvar IEP: Punt Ireland. Now replaced by the Euro (EUR): use only
        for historical prices that pre-date the introduction of the Euro
    :cvar ILS: New Israeli Sheqel Israel
    :cvar INR: Indian Rupee India, Bhutan (prices normally quoted as
        integers)
    :cvar IQD: Iraqi Dinar Iraq (prices normally quoted as integers)
    :cvar IRR: Iranian Rial Iran (Islamic Republic of) (prices normally
        quoted as integers)
    :cvar ISK: Iceland Krona Iceland (prices normally quoted as
        integers)
    :cvar ITL: Lira italy. Now replaced by the Euro (EUR): use only for
        historical prices that pre-date the introduction of the Euro
        (prices normally quoted as integers)
    :cvar JMD: Jamaican Dollar Jamaica
    :cvar JOD: Jordanian Dinar Jordan (prices normally quoted with 3
        decimal places)
    :cvar JPY: Yen Japan (prices normally quoted as integers)
    :cvar KES: Kenyan Shilling Kenya
    :cvar KGS: Som Kyrgyzstan
    :cvar KHR: Riel Cambodia
    :cvar KMF: Comoro Franc Comoros (prices normally quoted as integers)
    :cvar KPW: North Korean Won Korea (Democratic People’s Republic of)
        (prices normally quoted as integers)
    :cvar KRW: Won Korea (Republic of) (prices normally quoted as
        integers)
    :cvar KWD: Kuwaiti Dinar Kuwait (prices normally quoted with 3
        decimal places)
    :cvar KYD: Cayman Islands Dollar Cayman Islands
    :cvar KZT: Tenge Kazakstan
    :cvar LAK: Kip Lao People’s Democratic Republic (prices normally
        quoted as integers)
    :cvar LBP: Lebanese Pound Lebanon (prices normally quoted as
        integers)
    :cvar LKR: Sri Lanka Rupee Sri Lanka
    :cvar LRD: Liberian Dollar Liberia
    :cvar LSL: Loti Lesotho
    :cvar LTL: Litus Lithuania. Now replaced by the Euro (EUR): use only
        for historical prices that pre-date the introduction of the Euro
    :cvar LUF: Luxembourg Franc Luxembourg. Now replaced by the Euro
        (EUR): use only for historical prices that pre-date the
        introduction of the Euro (prices normally quoted as integers)
    :cvar LVL: Latvian Lats Latvia. Now replaced by the Euro (EUR): use
        only for historical prices that pre-date the introduction of the
        Euro
    :cvar LYD: Libyan Dinar Libyan Arab Jamahiriya (prices normally
        quoted with 3 decimal places)
    :cvar MAD: Moroccan Dirham Morocco, Western Sahara
    :cvar MDL: Moldovan Leu Moldova, Republic of
    :cvar MGA: Malagasy Ariary Madagascar (prices normally quoted with 0
        or 1 decimal place – 1 iraimbilanja = Ar0.2)
    :cvar MGF: Malagasy Franc Now replaced by the Ariary (MGA) (prices
        normally quoted as integers)
    :cvar MKD: Denar Macedonia (former Yugoslav Republic of)
    :cvar MMK: Kyat Myanmar (prices normally quoted as integers)
    :cvar MNT: Tugrik Mongolia (prices normally quoted as integers)
    :cvar MOP: Pataca Macau
    :cvar MRO: Ouguiya Mauritania (0 or 1 – 1 khoums = UM0.2)
    :cvar MTL: Maltese Lira Malta. Now replaced by the Euro (EUR): use
        only for historical prices that pre-date the introduction of the
        Euro
    :cvar MUR: Mauritius Rupee Mauritius (prices normally quoted as
        integers)
    :cvar MVR: Rufiyaa Maldives
    :cvar MWK: Malawi Kwacha Malawi
    :cvar MXN: Mexican Peso Mexico
    :cvar MYR: Malaysian Ringgit Malaysia
    :cvar MZN: Mozambique Metical Mozambique
    :cvar NAD: Namibia Dollar Namibia
    :cvar NGN: Naira Nigeria
    :cvar NIO: Cordoba Oro Nicaragua
    :cvar NLG: Guilder Netherlands. Now replaced by the Euro (EUR): use
        only for historical prices that pre-date the introduction of the
        Euro
    :cvar NOK: Norwegian Krone Norway, Bouvet Island, Svalbard and Jan
        Mayen
    :cvar NPR: Nepalese Rupee Nepal
    :cvar NZD: New Zealand Dollar New Zealand, Cook Islands, Niue,
        Pitcairn, Tokelau
    :cvar OMR: Rial Omani Oman (prices normally quoted with 3 decimal
        places)
    :cvar PAB: Balboa Panama
    :cvar PEN: Sol Peru (formerly Nuevo Sol)
    :cvar PGK: Kina Papua New Guinea
    :cvar PHP: Philippine Peso Philippines
    :cvar PKR: Pakistan Rupee Pakistan (prices normally quoted as
        integers)
    :cvar PLN: Zloty Poland
    :cvar PTE: Escudo Portugal. Now replaced by the Euro (EUR): use only
        for historical prices that pre-date the introduction of the Euro
    :cvar PYG: Guarani Paraguay (prices normally quoted as integers)
    :cvar QAR: Qatari Rial Qatar
    :cvar ROL: Romanian Old Leu Deprecated, replaced by RON
    :cvar RON: Romanian Leu Romania
    :cvar RSD: Serbian Dinar Serbia (prices normally quoted as integers)
    :cvar RUB: Russian Ruble Russian Federation
    :cvar RUR: Russian Ruble DEPRECATED, replaced by RUB
    :cvar RWF: Rwanda Franc Rwanda (prices normally quoted as integers)
    :cvar SAR: Saudi Riyal Saudi Arabia
    :cvar SBD: Solomon Islands Dollar Solomon Islands
    :cvar SCR: Seychelles Rupee Seychelles
    :cvar SDD: Sudanese Dinar Now replaced by the Sudanese Pound (SDG)
    :cvar SDG: Sudanese Pound Sudan
    :cvar SEK: Swedish Krona Sweden
    :cvar SGD: Singapore Dollar Singapore
    :cvar SHP: Saint Helena Pound Saint Helena
    :cvar SIT: Tolar Slovenia. Now replaced by the Euro (EUR): use only
        for historical prices that pre-date the introduction of the Euro
    :cvar SKK: Slovak Koruna Slovakia. Now replaced by the Euro (EUR):
        use only for historical prices that pre-date the introduction of
        the Euro
    :cvar SLL: Leone Sierra Leone (prices normally quoted as integers)
    :cvar SOS: Somali Shilling Somalia (prices normally quoted as
        integers)
    :cvar SRD: Surinam Dollar Suriname
    :cvar SRG: Suriname Guilder DEPRECATED, replaced by SRD
    :cvar STD: Dobra São Tome and Principe (prices normally quoted as
        integers)
    :cvar SVC: El Salvador Colon El Salvador
    :cvar SYP: Syrian Pound Syrian Arab Republic (prices normally quoted
        as integers)
    :cvar SZL: Lilangeni Swaziland
    :cvar THB: Baht Thailand
    :cvar TJS: Somoni Tajikistan
    :cvar TMM: Turkmenistan Manat Deprecated, replaced by TMT (prices
        normally quoted as integers)
    :cvar TMT: Turkmenistan New Manat Turkmenistan
    :cvar TND: Tunisian Dinar Tunisia (prices normally quoted with 3
        decimal places)
    :cvar TOP: Pa’anga Tonga
    :cvar TPE: Timor Escudo Deprecated. Timor-Leste now uses the US
        Dollar
    :cvar TRL: Turkish Lira (old) Deprecated, replaced by TRY (prices
        normally quoted as integers)
    :cvar TRY: Turkish Lira Turkey, from 1 January 2005
    :cvar TTD: Trinidad and Tobago Dollar Trinidad and Tobago
    :cvar TWD: New Taiwan Dollar Taiwan (Province of China)
    :cvar TZS: Tanzanian Shilling Tanzania (United Republic of) (prices
        normally quoted as integers)
    :cvar UAH: Hryvnia Ukraine
    :cvar UGX: Uganda Shilling Uganda (prices normally quoted as
        integers)
    :cvar USD: US Dollar United States, American Samoa, Bonaire, Sint
        Eustatius and Saba, British Indian Ocean Territory, Ecuador, El
        Salvador, Guam, Haiti, Marshall Is, Micronesia (Federated States
        of), Northern Mariana Is, Palau, Panama, Puerto Rico, Timor-
        Leste, Turks and Caicos Is, US Minor Outlying Is, Virgin Is
        (British), Virgin Is (US)
    :cvar UYU: Peso Uruguayo Uruguay
    :cvar UZS: Uzbekistan Sum Uzbekistan (prices normally quoted as
        integers)
    :cvar VEB: Bolivar Deprecated, replaced by VEF
    :cvar VEF: Bolívar Venezuela (formerly Bolívar fuerte)
    :cvar VND: Dong Viet Nam (prices normally quoted as integers)
    :cvar VUV: Vatu Vanuatu (prices normally quoted as integers)
    :cvar WST: Tala Samoa
    :cvar XAF: CFA Franc BEAC Cameroon, Central African Republic, Chad,
        Congo, Equatorial Guinea, Gabon (prices normally quoted as
        integers)
    :cvar XCD: East Caribbean Dollar Anguilla, Antigua and Barbuda,
        Dominica, Grenada, Montserrat, Saint Kitts and Nevis, Saint
        Lucia, Saint Vincent and the Grenadines
    :cvar XOF: CFA Franc BCEAO Benin, Burkina Faso, Côte D’Ivoire,
        Guinea-Bissau, Mali, Niger, Senegal, Togo (prices normally
        quoted as integers)
    :cvar XPF: CFP Franc French Polynesia, New Caledonia, Wallis and
        Futuna (prices normally quoted as integers)
    :cvar YER: Yemeni Rial Yemen (prices normally quoted as integers)
    :cvar YUM: Yugoslavian Dinar DEPRECATED, replaced by CSD
    :cvar ZAR: Rand South Africa, Namibia, Lesotho
    :cvar ZMK: Kwacha Zambia. Deprecated, replaced with ZMW (prices
        normally quoted as integers)
    :cvar ZMW: Zambian Kwacha Zambia
    :cvar ZWD: Zimbabwe Dollar Deprecated, replaced with ZWL (prices
        normally quoted as integers)
    :cvar ZWL: Zimbabwe Dollar Zimbabwe
    """
    AED = "AED"
    AFA = "AFA"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    ATS = "ATS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BEF = "BEF"
    BGL = "BGL"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYR = "BYR"
    BYN = "BYN"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHF = "CHF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    CRC = "CRC"
    CSD = "CSD"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CYP = "CYP"
    CZK = "CZK"
    DEM = "DEM"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EEK = "EEK"
    EGP = "EGP"
    ERN = "ERN"
    ESP = "ESP"
    ETB = "ETB"
    EUR = "EUR"
    FIM = "FIM"
    FJD = "FJD"
    FKP = "FKP"
    FRF = "FRF"
    GBP = "GBP"
    GEL = "GEL"
    GHC = "GHC"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GRD = "GRD"
    GTQ = "GTQ"
    GWP = "GWP"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    IEP = "IEP"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    ITL = "ITL"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LTL = "LTL"
    LUF = "LUF"
    LVL = "LVL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MGF = "MGF"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRO = "MRO"
    MTL = "MTL"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NLG = "NLG"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PTE = "PTE"
    PYG = "PYG"
    QAR = "QAR"
    ROL = "ROL"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RUR = "RUR"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDD = "SDD"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SIT = "SIT"
    SKK = "SKK"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    SRG = "SRG"
    STD = "STD"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMM = "TMM"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TPE = "TPE"
    TRL = "TRL"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    UYU = "UYU"
    UZS = "UZS"
    VEB = "VEB"
    VEF = "VEF"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XCD = "XCD"
    XOF = "XOF"
    XPF = "XPF"
    YER = "YER"
    YUM = "YUM"
    ZAR = "ZAR"
    ZMK = "ZMK"
    ZMW = "ZMW"
    ZWD = "ZWD"
    ZWL = "ZWL"


class List97(Enum):
    """
    Bible text feature.

    :cvar RL: Red letter Words spoken by Christ are printed in red
    """
    RL = "RL"
