from enum import Enum

__NAMESPACE__ = "http://ns.editeur.org/onix/3.1/short"


class List1(Enum):
    """
    Notification or update type.

    :cvar VALUE_01: Early notification Use for a complete record issued
        earlier than approximately six months before publication
    :cvar VALUE_02: Advance notification (confirmed) Use for a complete
        record issued to confirm advance information approximately six
        months before publication; or for a complete record issued after
        that date and before information has been confirmed from the
        book-in-hand
    :cvar VALUE_03: Notification confirmed on publication Use for a
        complete record issued to confirm advance information at or just
        before actual publication date, usually from the book-in-hand,
        or for a complete record issued at any later date
    :cvar VALUE_04: Update (partial) In ONIX 3.0 or later only, use when
        sending a ‘block update’ record. A block update implies using
        the supplied block(s) to update the existing record for the
        product, replacing only the blocks included in the block update,
        and leaving other blocks unchanged – for example, replacing old
        information from Blocks 4 and 6 with the newly-received data
        while retaining information from Blocks 1–3, 5 and 7–8
        untouched. In previous ONIX releases, and for ONIX 3.0 or later
        using other notification types, updating is by replacing the
        complete record with the newly-received data
    :cvar VALUE_05: Delete Use when sending an instruction to delete a
        record which was previously issued. Note that a Delete
        instruction should NOT be used when a product is cancelled, put
        out of print, or otherwise withdrawn from sale: this should be
        handled as a change of Publishing status, leaving the receiver
        to decide whether to retain or delete the record. A Delete
        instruction is used ONLY when there is a particular reason to
        withdraw a record completely, eg because it was issued in error
    :cvar VALUE_08: Notice of sale Notice of sale of a product, from one
        publisher to another: sent by the publisher disposing of the
        product
    :cvar VALUE_09: Notice of acquisition Notice of acquisition of a
        product, by one publisher from another: sent by the acquiring
        publisher
    :cvar VALUE_88: Test update (Partial) Only for use in ONIX 3.0 or
        later. Record may be processed for test purposes, but data
        should be discarded when testing is complete. Sender must ensure
        the &lt;RecordReference&gt; matches a previously-sent Test
        record
    :cvar VALUE_89: Test record Record may be processed for test
        purposes, but data should be discarded when testing is complete.
        Sender must ensure the &lt;RecordReference&gt; does not match
        any previously-sent live product record
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_88 = "88"
    VALUE_89 = "89"


class List100(Enum):
    """
    Discount code type.

    :cvar VALUE_01: BIC discount group code UK publisher’s or
        distributor’s discount group code in a format specified by BIC
        to ensure uniqueness (a five-letter prefix allocated by BIC,
        plus one to three alphanumeric characters – normally digits –
        chosen by the supplier). See
        https://bic.org.uk/resources/discount-group-codes/
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
    :cvar VALUE_07: ISNI-based discount group code ISNI-based discount
        group scheme devised initially by the German IG
        ProduktMetadaten, in a format comprised of the supplier’s
        16-digit ISNI, followed by a hyphen and one to three
        alphanumeric characters – normally digits – chosen by the
        supplier. These characters are the index to a discount
        percentage in a table shared in advance by the supplier with
        individual customers. In this way, a supplier may maintain
        individual product-specific discount arrangements with each
        customer. Only for use in ONIX 3.0 or later
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"


class List102(Enum):
    """
    Sales outlet identifier type.

    :cvar VALUE_01: Proprietary Proprietary list of retail and other
        end-user sales outlet IDs. Note that &lt;IDTypeName&gt; is
        required with proprietary identifiers
    :cvar VALUE_03: ONIX retail sales outlet ID code Use with ONIX
        retail and other end-user sales outlet IDs from List 139
    :cvar VALUE_04: Retail sales outlet GLN 13-digit GS1 global location
        number (formerly EAN location number). Only for use in ONIX 3.0
        or later
    :cvar VALUE_05: Retail sales outlet SAN 7-digit Book trade Standard
        Address Number (US, UK etc). Only for use in ONIX 3.0 or later
    """

    VALUE_01 = "01"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"


class List12(Enum):
    """
    Trade category.

    :cvar VALUE_01: UK open market edition An edition from a UK
        publisher sold only in territories where exclusive rights are
        not held. Rights details should be carried in PR.21 (in ONIX
        2.1) OR P.21 (in ONIX 3.0 or later) as usual
    :cvar VALUE_02: Airport edition In UK, an edition intended primarily
        for airside sales in UK airports, though it may be available for
        sale in other territories where exclusive rights are not held.
        Rights details should be carried in PR.21 (in ONIX 2.1) OR P.21
        (in ONIX 3.0 or later) as usual
    :cvar VALUE_03: Sonderausgabe In Germany, a special printing sold at
        a lower price than the regular hardback
    :cvar VALUE_04: Pocket book In countries where recognised as a
        distinct trade category, eg France « livre de poche », Germany
        ,Taschenbuch‘, Italy «tascabile», Spain «libro de bolsillo»
    :cvar VALUE_05: International edition (US) Edition produced solely
        for sale in designated export markets
    :cvar VALUE_06: Library audio edition Audio product sold in special
        durable packaging and with a replacement guarantee for the
        contained cassettes or CDs for a specified shelf-life
    :cvar VALUE_07: US open market edition An edition from a US
        publisher sold only in territories where exclusive rights are
        not held. Rights details should be carried in PR.21 (in ONIX
        2.1) OR P.21 (in ONIX 3.0 or later) as usual
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
    :cvar VALUE_15: Superpocket book In countries where recognised as a
        distinct trade category, eg Italy «supertascabile». Only for use
        in ONIX 3.0 or later
    :cvar VALUE_16: Beau-livre Category of books, usually hardcover and
        of a large format (A4 or larger) and printed on high-quality
        paper, where the primary features are illustrations, and these
        are more important than text. Sometimes called ‘coffee-table
        books’ or ‘art books’ in English. Only for use in ONIX 3.0 or
        later
    :cvar VALUE_17: Podcast Category of audio products typically
        distinguished by being free of charge (but which may be
        monetised through advertising content) and episodic. Only for
        use in ONIX 3.0 or later
    :cvar VALUE_18: Periodical Category of books or e-books which are
        single issues of a periodical publication, sold as independent
        products. Only for use in ONIX 3.0 or later
    :cvar VALUE_19: Catalog Publisher’s or supplier’s catalog (when
        treated as a product in its own right). Only for use in ONIX 3.0
        or later
    :cvar VALUE_20: Atlas Category of books containing a linked group of
        plates, tables, diagrams, lists, often but not always combined
        with maps or a geographical theme or approach. Only for use in
        ONIX 3.0 or later
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


class List121(Enum):
    """
    Text script – based on ISO 15924.

    :cvar ADLM: Adlam Only for use in ONIX 3.0 or later
    :cvar AFAK: Afaka Script is not supported by Unicode
    :cvar AGHB: Caucasian Albanian Ancient/historic script. Only for use
        in ONIX 3.0 or later
    :cvar AHOM: Ahom, Tai Ahom Ancient/historic script. Only for use in
        ONIX 3.0 or later
    :cvar ARAB: Arabic
    :cvar ARAN: Arabic (Nastaliq variant) Typographic variant of Arabic.
        Only for use in ONIX 3.0 or later
    :cvar ARMI: Imperial Aramaic Ancient/historic script
    :cvar ARMN: Armenian
    :cvar AVST: Avestan Ancient/historic script
    :cvar BALI: Balinese
    :cvar BAMU: Bamun
    :cvar BASS: Bassa Vah Ancient/historic script
    :cvar BATK: Batak
    :cvar BENG: Bengali (Bangla)
    :cvar BHKS: Bhaiksuki Ancient/historic script. Only for use in ONIX
        3.0 or later
    :cvar BLIS: Blissymbols Script is not supported by Unicode
    :cvar BOPO: Bopomofo
    :cvar BRAH: Brahmi Ancient/historic script
    :cvar BRAI: Braille
    :cvar BUGI: Buginese
    :cvar BUHD: Buhid
    :cvar CAKM: Chakma
    :cvar CANS: Unified Canadian Aboriginal Syllabics
    :cvar CARI: Carian Ancient/historic script
    :cvar CHAM: Cham
    :cvar CHER: Cherokee
    :cvar CHRS: Chorasmian Khwārezmian. Ancient/historic script. Only
        for use in ONIX 3.0 or later
    :cvar CIRT: Cirth Script is not supported by Unicode
    :cvar COPT: Coptic Ancient/historic script
    :cvar CPMN: Cypro-Minoan Ancient/historic script. Only for use in
        ONIX 3.0 or later
    :cvar CPRT: Cypriot Ancient/historic script
    :cvar CYRL: Cyrillic
    :cvar CYRS: Cyrillic (Old Church Slavonic variant) Ancient/historic,
        typographic variant of Cyrillic
    :cvar DEVA: Devanagari (Nagari)
    :cvar DIAK: Dives Akuru Ancient/historic script. Only for use in
        ONIX 3.0 or later
    :cvar DOGR: Dogra Only for use in ONIX 3.0 or later
    :cvar DSRT: Deseret (Mormon)
    :cvar DUPL: Duployan shorthand, Duployan stenography
    :cvar EGYD: Egyptian demotic Script is not supported by Unicode
    :cvar EGYH: Egyptian hieratic Script is not supported by Unicode
    :cvar EGYP: Egyptian hieroglyphs Ancient/historic script
    :cvar ELBA: Elbasan Ancient/historic script
    :cvar ELYM: Elymaic Ancient/historic script. Only for use in ONIX
        3.0 or later
    :cvar ETHI: Ethiopic (Ge‘ez)
    :cvar GEOK: Khutsuri (Asomtavruli and Khutsuri) Georgian in Unicode
    :cvar GEOR: Georgian (Mkhedruli and Mtavruli)
    :cvar GLAG: Glagolitic Ancient/historic script
    :cvar GONG: Gunjala Gondi Only for use in ONIX 3.0 or later
    :cvar GONM: Masaram Gondi Only for use in ONIX 3.0 or later
    :cvar GOTH: Gothic Ancient/historic script
    :cvar GRAN: Grantha Ancient/historic script
    :cvar GREK: Greek
    :cvar GUJR: Gujarati
    :cvar GURU: Gurmukhi
    :cvar HANB: Han with Bopomofo See Hani, Bopo. Only for use in ONIX
        3.0 or later
    :cvar HANG: Hangul (Hangŭl, Hangeul)
    :cvar HANI: Han (Hanzi, Kanji, Hanja)
    :cvar HANO: Hanunoo (Hanunóo)
    :cvar HANS: Han (Simplified variant) Subset of Hani
    :cvar HANT: Han (Traditional variant) Subset of Hani
    :cvar HATR: Hatran Ancient/historic script. Only for use in ONIX 3.0
        or later
    :cvar HEBR: Hebrew
    :cvar HIRA: Hiragana
    :cvar HLUW: Anatolian Hieroglyphs (Luwian Hieroglyphs, Hittite
        Hieroglyphs) Ancient/historic script. Only for use in ONIX 3.0
        or later
    :cvar HMNG: Pahawh Hmong
    :cvar HMNP: Nyiakeng Puachue Hmong Only for use in ONIX 3.0 or later
    :cvar HRKT: Japanese syllabaries (alias for Hiragana + Katakana) See
        Hira, Kana
    :cvar HUNG: Old Hungarian (Hungarian Runic) Ancient/historic script
    :cvar INDS: Indus (Harappan) Script is not supported by Unicode
    :cvar ITAL: Old Italic (Etruscan, Oscan, etc.) Ancient/historic
        script
    :cvar JAMO: Jamo (alias for Jamo subset of Hangul) Subset of Hang.
        Only for use in ONIX 3.0 or later
    :cvar JAVA: Javanese
    :cvar JPAN: Japanese (alias for Han + Hiragana + Katakana) See Hani,
        Hira and Kana
    :cvar JURC: Jurchen Script is not supported by Unicode
    :cvar KALI: Kayah Li
    :cvar KANA: Katakana
    :cvar KAWI: Kawi Ancient/historic script. Only for use in ONIX 3.0
        or later
    :cvar KHAR: Kharoshthi Ancient/historic script
    :cvar KHMR: Khmer
    :cvar KHOJ: Khojki Ancient/historic script
    :cvar KITL: Khitan large script Script is not supported by Unicode.
        Only for use in ONIX 3.0 or later
    :cvar KITS: Khitan small script Only for use in ONIX 3.0 or later
    :cvar KNDA: Kannada
    :cvar KORE: Korean (alias for Hangul + Han) See Hani and Hang
    :cvar KPEL: Kpelle Script is not supported by Unicode
    :cvar KTHI: Kaithi Ancient/historic script
    :cvar LANA: Tai Tham (Lanna)
    :cvar LAOO: Lao
    :cvar LATF: Latin (Fraktur variant) Typographic variant of Latin
    :cvar LATG: Latin (Gaelic variant) Typographic variant of Latin
    :cvar LATN: Latin
    :cvar LEKE: Leke Script is not supported by Unicode. Only for use in
        ONIX 3.0 or later
    :cvar LEPC: Lepcha (Róng)
    :cvar LIMB: Limbu
    :cvar LINA: Linear A Ancient/historic script
    :cvar LINB: Linear B Ancient/historic script
    :cvar LISU: Lisu (Fraser)
    :cvar LOMA: Loma Script is not supported by Unicode
    :cvar LYCI: Lycian Ancient/historic script
    :cvar LYDI: Lydian Ancient/historic script
    :cvar MAHJ: Mahajani Ancient/historic script. Only for use in ONIX
        3.0 or later
    :cvar MAKA: Makasar Only for use in ONIX 3.0 or later
    :cvar MAND: Mandaic, Mandaean
    :cvar MANI: Manichaean Ancient/historic script
    :cvar MARC: Marchen Ancient/historic script. Only for use in ONIX
        3.0 or later
    :cvar MAYA: Mayan hieroglyphs Script is not supported by Unicode
    :cvar MEDF: Medefaidrin (Oberi Okaime, Oberi Ɔkaimɛ) Script is not
        supported by Unicode. Only for use in ONIX 3.0 or later
    :cvar MEND: Mende Kikakui
    :cvar MERC: Meroitic Cursive Ancient/historic script
    :cvar MERO: Meroitic Hieroglyphs Ancient/historic script
    :cvar MLYM: Malayalam
    :cvar MODI: Modi, Moḍī Ancient/historic script. Only for use in ONIX
        3.0 or later
    :cvar MONG: Mongolian Includes Clear, Manchu scripts
    :cvar MOON: Moon (Moon code, Moon script, Moon type) Script is not
        supported by Unicode
    :cvar MROO: Mro, Mru
    :cvar MTEI: Meitei Mayek (Meithei, Meetei)
    :cvar MULT: Multani Ancient/historic script. Only for use in ONIX
        3.0 or later
    :cvar MYMR: Myanmar (Burmese)
    :cvar NAGM: Nag Mundari Only for use in ONIX 3.0 or later
    :cvar NAND: Nandinagari Ancient/historic script. Only for use in
        ONIX 3.0 or later
    :cvar NARB: Old North Arabian (Ancient North Arabian)
        Ancient/historic script
    :cvar NBAT: Nabatean Ancient/historic script
    :cvar NEWA: Newa, Newar, Newari, Nepāla lipi Only for use in ONIX
        3.0 or later
    :cvar NKGB: Nakhi Geba (’Na-’Khi ²Ggŏ-¹baw, Naxi Geba) Script is not
        supported by Unicode
    :cvar NKOO: N’Ko
    :cvar NSHU: Nüshu
    :cvar OGAM: Ogham Ancient/historic script
    :cvar OLCK: Ol Chiki (Ol Cemet’, Ol, Santali)
    :cvar ORKH: Old Turkic, Orkhon Runic Ancient/historic script
    :cvar ORYA: Oriya (Odia)
    :cvar OSGE: Osage Only for use in ONIX 3.0 or later
    :cvar OSMA: Osmanya
    :cvar OUGR: Old Uyghur Ancient/historic script. Only for use in ONIX
        3.0 or later
    :cvar PALM: Palmyrene Ancient/historic script
    :cvar PAUC: Pau Cin Hau Only for use in ONIX 3.0 or later
    :cvar PERM: Old Permic Ancient/historic script
    :cvar PHAG: Phags-pa Ancient/historic script
    :cvar PHLI: Inscriptional Pahlavi Ancient/historic script
    :cvar PHLP: Psalter Pahlavi Ancient/historic script
    :cvar PHLV: Book Pahlavi Script is not supported by Unicode
    :cvar PHNX: Phoenician Ancient/historic script
    :cvar PIQD: Klingon (KLI plqaD) Script is not supported by Unicode.
        Only for use in ONIX 3.0 or later
    :cvar PLRD: Miao (Pollard)
    :cvar PRTI: Inscriptional Parthian Ancient/historic script
    :cvar QAAA: Reserved for private use (start)
    :cvar QABP: Picture Communication Symbols (PCS) ONIX local code for
        graphical symbols used in augmentative and alternative
        communication and education, not listed in ISO 15924. Only for
        use in ONIX 3.0 or later
    :cvar QABW: Widgit symbols ONIX local code for graphical symbols
        used in augmentative and alternative communication and
        education, not listed in ISO 15924. Only for use in ONIX 3.0 or
        later
    :cvar QABX: Reserved for private use (end)
    :cvar RJNG: Rejang (Redjang, Kaganga)
    :cvar RORO: Rongorongo Script is not supported by Unicode
    :cvar RUNR: Runic Ancient/historic script
    :cvar SAMR: Samaritan
    :cvar SARA: Sarati Script is not supported by Unicode
    :cvar SARB: Old South Arabian Ancient/historic script
    :cvar SAUR: Saurashtra
    :cvar SGNW: SignWriting
    :cvar SHAW: Shavian (Shaw)
    :cvar SHRD: Sharada, Śāradā
    :cvar SIDD: Siddham, Siddhaṃ, Siddhamātṛkā Ancient/historic script.
        Only for use in ONIX 3.0 or later
    :cvar SIND: Khudawadi, Sindhi
    :cvar SINH: Sinhala
    :cvar SOGD: Sogdian Ancient/historic script. Only for use in ONIX
        3.0 or later
    :cvar SOGO: Old Sogdian Ancient/historic script. Only for use in
        ONIX 3.0 or later
    :cvar SORA: Sora Sompeng
    :cvar SOYO: Soyombo Only for use in ONIX 3.0 or later
    :cvar SUND: Sundanese
    :cvar SYLO: Syloti Nagri
    :cvar SYRC: Syriac
    :cvar SYRE: Syriac (Estrangelo variant) Typographic variant of
        Syriac
    :cvar SYRJ: Syriac (Western variant) Typographic variant of Syriac
    :cvar SYRN: Syriac (Eastern variant) Typographic variant of Syriac
    :cvar TAGB: Tagbanwa
    :cvar TAKR: Takri, Ṭākrī, Ṭāṅkrī
    :cvar TALE: Tai Le
    :cvar TALU: New Tai Lue
    :cvar TAML: Tamil
    :cvar TANG: Tangut Ancient/historic script
    :cvar TAVT: Tai Viet
    :cvar TELU: Telugu
    :cvar TENG: Tengwar Script is not supported by Unicode
    :cvar TFNG: Tifinagh (Berber)
    :cvar TGLG: Tagalog (Baybayin, Alibata)
    :cvar THAA: Thaana
    :cvar THAI: Thai
    :cvar TIBT: Tibetan
    :cvar TIRH: Tirhuta
    :cvar TNSA: Tangsa Only for use in ONIX 3.0 or later
    :cvar TOTO: Toto Only for use in ONIX 3.0 or later
    :cvar UGAR: Ugaritic Ancient/historic script
    :cvar VAII: Vai
    :cvar VISP: Visible Speech Script is not supported by Unicode
    :cvar VITH: Vithkuqi Ancient/historic script. Only for use in ONIX
        3.0 or later
    :cvar WARA: Warang Citi (Varang Kshiti)
    :cvar WCHO: Wancho Only for use in ONIX 3.0 or later
    :cvar WOLE: Woleai Script is not supported by Unicode
    :cvar XPEO: Old Persian Ancient/historic script
    :cvar XSUX: Cuneiform, Sumero-Akkadian Ancient/historic script
    :cvar YEZI: Yezidi Ancient/historic script. Only for use in ONIX 3.0
        or later
    :cvar YIII: Yi
    :cvar ZANB: Zanabazar Square (Zanabazarin Dörböljin Useg, Xewtee
        Dörböljin Bicig, Horizontal Square Script) Only for use in ONIX
        3.0 or later
    :cvar ZMTH: Mathematical notation Not a script in Unicode
    :cvar ZSYE: Symbols (Emoji variant) Not a script in Unicode. Only
        for use in ONIX 3.0 or later
    :cvar ZSYM: Symbols Not a script in Unicode
    :cvar ZXXX: Code for unwritten documents Not a script in Unicode
    :cvar ZINH: Code for inherited script
    :cvar ZYYY: Code for undetermined script
    :cvar ZZZZ: Code for uncoded script
    """

    ADLM = "Adlm"
    AFAK = "Afak"
    AGHB = "Aghb"
    AHOM = "Ahom"
    ARAB = "Arab"
    ARAN = "Aran"
    ARMI = "Armi"
    ARMN = "Armn"
    AVST = "Avst"
    BALI = "Bali"
    BAMU = "Bamu"
    BASS = "Bass"
    BATK = "Batk"
    BENG = "Beng"
    BHKS = "Bhks"
    BLIS = "Blis"
    BOPO = "Bopo"
    BRAH = "Brah"
    BRAI = "Brai"
    BUGI = "Bugi"
    BUHD = "Buhd"
    CAKM = "Cakm"
    CANS = "Cans"
    CARI = "Cari"
    CHAM = "Cham"
    CHER = "Cher"
    CHRS = "Chrs"
    CIRT = "Cirt"
    COPT = "Copt"
    CPMN = "Cpmn"
    CPRT = "Cprt"
    CYRL = "Cyrl"
    CYRS = "Cyrs"
    DEVA = "Deva"
    DIAK = "Diak"
    DOGR = "Dogr"
    DSRT = "Dsrt"
    DUPL = "Dupl"
    EGYD = "Egyd"
    EGYH = "Egyh"
    EGYP = "Egyp"
    ELBA = "Elba"
    ELYM = "Elym"
    ETHI = "Ethi"
    GEOK = "Geok"
    GEOR = "Geor"
    GLAG = "Glag"
    GONG = "Gong"
    GONM = "Gonm"
    GOTH = "Goth"
    GRAN = "Gran"
    GREK = "Grek"
    GUJR = "Gujr"
    GURU = "Guru"
    HANB = "Hanb"
    HANG = "Hang"
    HANI = "Hani"
    HANO = "Hano"
    HANS = "Hans"
    HANT = "Hant"
    HATR = "Hatr"
    HEBR = "Hebr"
    HIRA = "Hira"
    HLUW = "Hluw"
    HMNG = "Hmng"
    HMNP = "Hmnp"
    HRKT = "Hrkt"
    HUNG = "Hung"
    INDS = "Inds"
    ITAL = "Ital"
    JAMO = "Jamo"
    JAVA = "Java"
    JPAN = "Jpan"
    JURC = "Jurc"
    KALI = "Kali"
    KANA = "Kana"
    KAWI = "Kawi"
    KHAR = "Khar"
    KHMR = "Khmr"
    KHOJ = "Khoj"
    KITL = "Kitl"
    KITS = "Kits"
    KNDA = "Knda"
    KORE = "Kore"
    KPEL = "Kpel"
    KTHI = "Kthi"
    LANA = "Lana"
    LAOO = "Laoo"
    LATF = "Latf"
    LATG = "Latg"
    LATN = "Latn"
    LEKE = "Leke"
    LEPC = "Lepc"
    LIMB = "Limb"
    LINA = "Lina"
    LINB = "Linb"
    LISU = "Lisu"
    LOMA = "Loma"
    LYCI = "Lyci"
    LYDI = "Lydi"
    MAHJ = "Mahj"
    MAKA = "Maka"
    MAND = "Mand"
    MANI = "Mani"
    MARC = "Marc"
    MAYA = "Maya"
    MEDF = "Medf"
    MEND = "Mend"
    MERC = "Merc"
    MERO = "Mero"
    MLYM = "Mlym"
    MODI = "Modi"
    MONG = "Mong"
    MOON = "Moon"
    MROO = "Mroo"
    MTEI = "Mtei"
    MULT = "Mult"
    MYMR = "Mymr"
    NAGM = "Nagm"
    NAND = "Nand"
    NARB = "Narb"
    NBAT = "Nbat"
    NEWA = "Newa"
    NKGB = "Nkgb"
    NKOO = "Nkoo"
    NSHU = "Nshu"
    OGAM = "Ogam"
    OLCK = "Olck"
    ORKH = "Orkh"
    ORYA = "Orya"
    OSGE = "Osge"
    OSMA = "Osma"
    OUGR = "Ougr"
    PALM = "Palm"
    PAUC = "Pauc"
    PERM = "Perm"
    PHAG = "Phag"
    PHLI = "Phli"
    PHLP = "Phlp"
    PHLV = "Phlv"
    PHNX = "Phnx"
    PIQD = "Piqd"
    PLRD = "Plrd"
    PRTI = "Prti"
    QAAA = "Qaaa"
    QABP = "Qabp"
    QABW = "Qabw"
    QABX = "Qabx"
    RJNG = "Rjng"
    RORO = "Roro"
    RUNR = "Runr"
    SAMR = "Samr"
    SARA = "Sara"
    SARB = "Sarb"
    SAUR = "Saur"
    SGNW = "Sgnw"
    SHAW = "Shaw"
    SHRD = "Shrd"
    SIDD = "Sidd"
    SIND = "Sind"
    SINH = "Sinh"
    SOGD = "Sogd"
    SOGO = "Sogo"
    SORA = "Sora"
    SOYO = "Soyo"
    SUND = "Sund"
    SYLO = "Sylo"
    SYRC = "Syrc"
    SYRE = "Syre"
    SYRJ = "Syrj"
    SYRN = "Syrn"
    TAGB = "Tagb"
    TAKR = "Takr"
    TALE = "Tale"
    TALU = "Talu"
    TAML = "Taml"
    TANG = "Tang"
    TAVT = "Tavt"
    TELU = "Telu"
    TENG = "Teng"
    TFNG = "Tfng"
    TGLG = "Tglg"
    THAA = "Thaa"
    THAI = "Thai"
    TIBT = "Tibt"
    TIRH = "Tirh"
    TNSA = "Tnsa"
    TOTO = "Toto"
    UGAR = "Ugar"
    VAII = "Vaii"
    VISP = "Visp"
    VITH = "Vith"
    WARA = "Wara"
    WCHO = "Wcho"
    WOLE = "Wole"
    XPEO = "Xpeo"
    XSUX = "Xsux"
    YEZI = "Yezi"
    YIII = "Yiii"
    ZANB = "Zanb"
    ZMTH = "Zmth"
    ZSYE = "Zsye"
    ZSYM = "Zsym"
    ZXXX = "Zxxx"
    ZINH = "Zinh"
    ZYYY = "Zyyy"
    ZZZZ = "Zzzz"


class List13(Enum):
    """
    Collection identifier type.

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
        character set, beginning ‘10.’ and without https://doi.org/ or
        the older http://dx.doi.org/)
    :cvar VALUE_15: ISBN-13 Use only where the collection (series or
        set) is available as a single product
    :cvar VALUE_22: URN Uniform Resource Name using full URN syntax, eg
        urn:issn:1476-4687 – though where a specific code for the
        identifier type is available, use of that code (ie code 02 for
        ISSN) is preferred
    :cvar VALUE_27: JP Magazine ID Japanese magazine identifier, similar
        in scope to ISSN. Five digits to identify the periodical,
        without any hyphen or two digit extension. Only for use in ONIX
        3.0 or later
    :cvar VALUE_29: BNF Control number French National Bibliography
        series ID. Identifiant des publications en série maintenu par la
        Bibliothèque Nationale de France
    :cvar VALUE_35: ARK Archival Resource Key, as a URL (including the
        address of the ARK resolver provided by eg a national library)
    :cvar VALUE_38: ISSN-L International Standard Serial Number ‘linking
        ISSN’, used when distinct from the serial ISSN. Unhyphenated, 8
        digits. Only for use in ONIX 3.0 or later
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_15 = "15"
    VALUE_22 = "22"
    VALUE_27 = "27"
    VALUE_29 = "29"
    VALUE_35 = "35"
    VALUE_38 = "38"


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
    :cvar VALUE_03: All capitals For example, ‘THE CONQUEST OF MEXICO’.
        Use only when Sentence or Title case are not possible (for
        example because of system limitations). Do NOT use simply
        because title is (correctly) in all caps (eg ‘BBQ USA’)
    """

    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"


class List141(Enum):
    """
    Barcode indicator.

    :cvar VALUE_00: Not barcoded
    :cvar VALUE_01: Barcoded, scheme unspecified
    :cvar VALUE_02: GTIN-13 Barcode uses 13-digit EAN symbology (version
        NR without 5-digit extension). See (eg) https://bic.org.uk/wp-
        content/uploads/2022/11/2019.05.31-Bar-Coding-for-Books-
        rev-09.pdf or https://www.bisg.org/barcoding-guidelines-for-the-
        us-book-industry
    :cvar VALUE_03: GTIN-13+5 (US dollar price encoded) EAN symbology
        (version NK, first digit of 5-digit extension is 1–5)
    :cvar VALUE_04: GTIN-13+5 (CAN dollar price encoded) EAN symbology
        (version NK, first digit of 5-digit extension is 6)
    :cvar VALUE_05: GTIN-13+5 (no price encoded) EAN symbology (version
        NF, 5-digit extension is 90000–98999 for proprietary use –
        extension does not indicate a price)
    :cvar VALUE_06: UPC-12 (item-specific) AKA item/price
    :cvar VALUE_07: UPC-12+5 (item-specific) AKA item/price
    :cvar VALUE_08: UPC-12 (price-point) AKA price/item
    :cvar VALUE_09: UPC-12+5 (price-point) AKA price/item
    :cvar VALUE_10: GTIN-13+5 (UK Pound Sterling price encoded) EAN
        symbology (version NK, first digit of 5-digit extension is 0)
    :cvar VALUE_11: GTIN-13+5 (other price encoded) EAN symbology
        (version NK, price currency by local agreement)
    :cvar VALUE_12: GTIN-13+2 EAN symbology (two-digit extension,
        normally indicating periodical issue number)
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


class List142(Enum):
    """
    Position on product.

    :cvar VALUE_00: Unknown / unspecified Position unknown or
        unspecified
    :cvar VALUE_01: Cover 4 The back cover of a book (or book jacket) –
        the recommended position
    :cvar VALUE_02: Cover 3 The inside back cover of a book
    :cvar VALUE_03: Cover 2 The inside front cover of a book
    :cvar VALUE_04: Cover 1 The front cover of a book
    :cvar VALUE_05: On spine The spine of a book
    :cvar VALUE_06: On box Used only for boxed products
    :cvar VALUE_07: On tag Used only for products fitted with hanging
        tags
    :cvar VALUE_08: On bottom Not be used for books unless they are
        contained within outer packaging
    :cvar VALUE_09: On back Not be used for books unless they are
        contained within outer packaging
    :cvar VALUE_10: On outer sleeve / back Used only for products
        packaged in outer sleeves
    :cvar VALUE_11: On removable wrapping Used only for products
        packaged in shrink-wrap or other removable wrapping
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


class List144(Enum):
    """
    E-publication technical protection.

    :cvar VALUE_00: None Has no technical protection
    :cvar VALUE_01: DRM Has DRM protection
    :cvar VALUE_02: Digital watermarking Has digital watermarking
    :cvar VALUE_03: Adobe DRM Has DRM protection applied by the Adobe
        CS4 Content Server Package or by the Adobe ADEPT hosted service
    :cvar VALUE_04: Apple DRM Has FairPlay DRM protection applied via
        Apple proprietary online store
    :cvar VALUE_05: OMA DRM Has OMA v2 DRM protection applied, as used
        to protect some mobile phone content
    :cvar VALUE_06: Readium LCP DRM Has Licensed Content Protection DRM
        applied by a Readium License Server
    :cvar VALUE_07: Sony DRM Has Sony DADC User Rights Management (URMS)
        DRM protection applied
    """

    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"


class List145(Enum):
    """
    Usage type.

    :cvar VALUE_00: No constraints Allows positive indication that there
        are no particular constraints (that can be specifed in
        &lt;EpubUsageConstraint&gt;). By convention, use 01 in
        &lt;EpubUsageStatus&gt;
    :cvar VALUE_01: Preview Preview before purchase. Allows a retail
        customer, account holder or patron to view or listen to a
        proportion of the book before purchase. Also applies to
        borrowers making use of ‘acquisition on demand’ models in
        libraries, and to ‘subscription’ models where the purchase is
        made on behalf of the reader
    :cvar VALUE_02: Print Print paper copy of extract
    :cvar VALUE_03: Copy / paste Make digital copy of extract
    :cvar VALUE_04: Share Share product across multiple concurrent
        devices. Allows a retail customer, account holder or patron to
        read the book across multiple devices linked to the same
        account. Also applies to readers in library borrowing and
        ‘subscription’ models
    :cvar VALUE_05: Text to speech ‘Read aloud’ with text to speech
        functionality
    :cvar VALUE_06: Lend Lendable by the purchaser to other device owner
        or account holder or patron, eg ‘Lend-to-a-friend’, library
        lending (where the library product has a separate
        &lt;ProductIdentifier&gt; from the consumer product). The
        ‘primary’ copy becomes unusable while the secondary copy is ‘on
        loan’ unless a number of concurrent borrowers is also specified
    :cvar VALUE_07: Time-limited license E-publication license is time-
        limited. Use with code 02 from List 146 and either a time period
        in days, weeks or months in &lt;EpubUsageLimit&gt;, or a Valid
        until date in &lt;EpubUsageLimit&gt;. The purchased copy becomes
        unusable when the license expires. For clarity, a perpetual
        license is the default, but may be specified explicitly with
        code 01 from list 146, or with code 02 and a limit
        &lt;Quantity&gt; of 0 days
    :cvar VALUE_08: Loan renewal Maximum number of consecutive loans or
        loan extensions (eg from a library) to a single device owner or
        account holder. Note that a limit of 1 indicates that a loan
        cannot be renewed or extended
    :cvar VALUE_09: Multi-user license E-publication license is multi-
        user. Maximum number of concurrent users licensed to use the
        product should be given in &lt;EpubUsageLimit&gt;. For clarity,
        unlimited concurrencyis the default, but may be specified
        explicitly with code 01 from list 146, or with code 02 and a
        limit &lt;Quantity&gt; of 0 users
    :cvar VALUE_10: Preview on premises Preview locally before purchase.
        Allows a retail customer, account holder or patron to view a
        proportion of the book (or the whole book, if no proportion is
        specified) before purchase, but ONLY while located physically in
        the retailer’s store (eg while logged on to the store or library
        wifi). Also applies to patrons making use of ‘acquisition on
        demand’ models in libraries
    :cvar VALUE_11: Text and data mining Make use of the content of the
        product (text, images, audio etc) for extraction of useful (and
        possibly new) information through automated computer analysis.
        By convention, use 01 or 03 in &lt;EpubUsageStatus&gt;. Note 03
        should be regarded as ‘prohibited to the full extent allowed by
        law’, or otherwise expressly reserved by the rightsholder, as in
        some jurisdictions, TDM may be subject to copyright exception
        (eg for not-for-profit purposes), subject to optional
        reservation, or allowed under ‘fair use’ doctrine
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


class List146(Enum):
    """
    Usage status.

    :cvar VALUE_01: Permitted unlimited
    :cvar VALUE_02: Permitted subject to limit Limit should be specified
        in &lt;EpubUsageLimit&gt; or &lt;PriceConstraintLimit&gt;
    :cvar VALUE_03: Prohibited
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"


class List147(Enum):
    """
    Unit of usage.

    :cvar VALUE_01: Copies Maximum number of copies that may be made of
        a permitted extract
    :cvar VALUE_02: Characters Maximum number of characters in a
        permitted extract for a specified usage
    :cvar VALUE_03: Words Maximum number of words in a permitted extract
        for a specified usage
    :cvar VALUE_04: Pages Maximum number of pages in a permitted extract
        for a specified usage
    :cvar VALUE_05: Percentage Maximum percentage of total content in a
        permitted extract for a specified usage
    :cvar VALUE_06: Devices Maximum number of devices in ‘share group’
    :cvar VALUE_07: Concurrent users Maximum number of concurrent users.
        NB where the number of concurrent users is specifically not
        limited, set the number of concurrent users to zero
    :cvar VALUE_15: Users Maximum number of licensed individual users,
        independent of concurrency of use
    :cvar VALUE_19: Concurrent classes Maximum number of licensed
        concurrent classes of user. A ‘class’ is a group of learners
        attending a specific course or lesson and generally taught as a
        group
    :cvar VALUE_20: Classes Maximum number of licensed classes of
        learners, independent of concurrency of use and the number of
        users per class
    :cvar VALUE_31: Institutions Maximum number of licensed
        institutions, independend of concurrency of use and the number
        of classes or individuals per institution
    :cvar VALUE_08: Percentage per time period Maximum percentage of
        total content which may be used in a specified usage per time
        period; the time period being specified as another
        &lt;EpubUsageLimit&gt; Quantity
    :cvar VALUE_09: Days Maximum time period in days (beginning from
        product purchase or activation)
    :cvar VALUE_13: Weeks Maximum time period in weeks
    :cvar VALUE_14: Months Maximum time period in months
    :cvar VALUE_16: Hours minutes and seconds Maximum amount of time in
        hours, minutes and seconds allowed in a permitted extract for a
        specified usage, in the format HHHMMSS (7 digits, with leading
        zeros if necessary)
    :cvar VALUE_27: Days (fixed start) Maximum time period in days
        (beginning from the product publication date). In effect, this
        defines a fixed end date for the license independent of the
        purchase or activation date
    :cvar VALUE_28: Weeks (fixed start) Maximum time period in weeks
    :cvar VALUE_29: Months (fixed start) Maximum time period in months
    :cvar VALUE_10: Times Maximum number of times a specified usage
        event may occur (in the lifetime of the product)
    :cvar VALUE_22: Times per day Maximum frequency a specified usage
        event may occur (per day)
    :cvar VALUE_23: Times per month Maximum frequency a specified usage
        event may occur (per month)
    :cvar VALUE_24: Times per year Maximum frequency a specified usage
        event may occur (per year)
    :cvar VALUE_21: Dots per inch Maximum resolution of printed or
        copy/pasted extracts
    :cvar VALUE_26: Dots per cm Maximum resolution of printed or
        copy/pasted extracts
    :cvar VALUE_11: Allowed usage start page Page number where allowed
        usage begins. &lt;Quantity&gt; should contain an absolute page
        number, counting the cover as page 1. (This type of page
        numbering should not be used where the e-publication has no
        fixed pagination). Use with (max number of) Pages, Percentage of
        content, or End page to specify pages allowed in Preview
    :cvar VALUE_12: Allowed usage end page Page number at which allowed
        usage ends. &lt;Quantity&gt; should contain an absolute page
        number, counting the cover as page 1. (This type of page
        numbering should not be used where the e-publication has no
        fixed pagination). Use with Start page to specify pages allowed
        in a preview
    :cvar VALUE_17: Allowed usage start time Time at which allowed usage
        begins. &lt;Quantity&gt; should contain an absolute time,
        counting from the beginning of an audio or video product, in the
        format HHHMMSS or HHHMMSScc. Use with Time, Percentage of
        content, or End time to specify time-based extract allowed in
        Preview
    :cvar VALUE_18: Allowed usage end time Time at which allowed usage
        ends. &lt;Quantity&gt; should contain an absolute time, counting
        from the beginning of an audio or video product, in the format
        HHHMMSS or HHHMMSScc. Use with Start time to specify time-based
        extract allowed in Preview
    :cvar VALUE_98: Valid from The date from which the usage constraint
        applies. &lt;Quantity&gt; is in the format YYYYMMDD
    :cvar VALUE_99: Valid to The date until which the usage constraint
        applies. &lt;Quantity&gt; is in the format YYYYMMDD
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_15 = "15"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_31 = "31"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_16 = "16"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_10 = "10"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_21 = "21"
    VALUE_26 = "26"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_98 = "98"
    VALUE_99 = "99"


class List148(Enum):
    """
    Collection type.

    :cvar VALUE_00: Unspecified (default) Collection type is not
        determined
    :cvar VALUE_10: Publisher collection The collection is a
        bibliographic collection (eg a series or set (Fr. série))
        defined and identified by a publisher, either on the product
        itself or in product information supplied by the publisher. The
        books in the collection generally share a subject, narrative,
        design style or authorship. They may may have a specific order,
        or the collection may be unordered
    :cvar VALUE_11: Collection éditoriale The collection is a
        bibliographic collection defined and identified by a publisher,
        either on the product itself or in product information supplied
        by the publisher, where the books in the collection have no
        specific order, shared subject, narrative, style or shared
        authorship, and are grouped by the publisher largely for
        marketing purposes. The collection has many of the
        characteristics of an imprint or marque. Used primarily in
        French book publishing, to distinguish between ‘série’ (using
        the normal code 10) and ‘collection’ (code 11), and where the
        collection éditoriale is not an imprint
    :cvar VALUE_20: Ascribed collection The collection has been defined
        and identified by a party in the metadata supply chain other
        than the publisher, typically an aggregator.
    """

    VALUE_00 = "00"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_20 = "20"


class List149(Enum):
    """
    Title element level.

    :cvar VALUE_01: Product The title element refers to an individual
        product
    :cvar VALUE_02: Collection level The title element refers to the top
        level of a bibliographic collection
    :cvar VALUE_03: Subcollection The title element refers to an
        intermediate level of a bibliographic collection that comprises
        two or more ‘sub-collections’
    :cvar VALUE_04: Content item The title element refers to a content
        item within a product, eg a work included in a combined or
        ‘omnibus’ edition, or a chapter in a book. Generally used only
        for titles within &lt;ContentItem&gt; (Block 3)
    :cvar VALUE_05: Master brand The title element names a multimedia
        franchise, licensed property or master brand where the use of
        the brand spans multiple collections and product forms, and
        possibly multiple imprints and publishers. It need not have a
        hierarchical relationship with title elements at other levels,
        or with other master brands. Used only for branded media
        properties carrying, for example, a children’s character brand
        or film franchise branding
    :cvar VALUE_06: Sub-subcollection The title element refers to an
        intermediate level of a bibliographic collection that is a
        subdivision of a sub-collection (a third level of collective
        identity)
    :cvar VALUE_07: Universe The title element names a ‘universe’, where
        parallel or intersecting narratives spanning multiple works and
        multiple characters occur in the same consistent fictional
        setting. It need not have a hierarchical relationship with title
        elements at other levels, in particular with master brands. Used
        primarily for comic books, but applicable to other fiction where
        appropriate
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"


class List15(Enum):
    """
    Title type.

    :cvar VALUE_00: Undefined
    :cvar VALUE_01: Distinctive title (book); Cover title (serial);
        Title onf item or collection (serial content item or reviewed
        resource) The full text of the distinctive title of the item,
        without abbreviation or abridgement. For books, generally taken
        from the title page (see codes 11–14 where an alternative title
        is provided on cover or spine). Where the item is an omnibus
        edition containing two or more works by the same author, and
        there is no separate combined title, a distinctive title may be
        constructed (by the sender) by concatenating the individual
        titles, with suitable punctuation, as in ‘Pride and prejudice /
        Sense and sensibility / Northanger Abbey’. Where the title alone
        is not distinctive, recipients may add elements may be taken
        from a set or series collection title and part number etc to
        create a distinctive title – but these elements should be
        provided separately by the sender
    :cvar VALUE_02: ISSN key title of serial Serials only
    :cvar VALUE_03: Title in original language Where the subject of the
        ONIX record is a translated item
    :cvar VALUE_04: Title acronym or initialism For serials: an acronym
        or initialism of Title Type 01, eg ‘JAMA’, ‘JACM’
    :cvar VALUE_05: Abbreviated title An abbreviated form of Title Type
        01
    :cvar VALUE_06: Title in other language A translation of Title Type
        01 or 03, or an independent title, used when the work is
        translated into another language, sometimes termed a ‘parallel
        title’
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
        (including a title used in another market – but see code 06 for
        translations)
    :cvar VALUE_15: Alternative title on spine An alternative title that
        appears on the spine of a book. Only for use in ONIX 3.0 or
        later
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
    VALUE_15 = "15"


class List150(Enum):
    """
    Product form.

    :cvar VALUE_00: Undefined
    :cvar AA: Audio Audio recording – detail unspecified. Use only when
        the form is unknown and no further detail can be provided.
        Prefer AZ plus &lt;ProductFormDescription&gt; if detail is
        available but no other A* code applies
    :cvar AB: Audio cassette Audio cassette (analogue)
    :cvar AC: CD-Audio Audio compact disc: use for ‘Red book’ discs
        (conventional audio CD) and SACD, and use coding in
        &lt;ProductFormDetail&gt; to specify the format, if required
    :cvar AD: DAT Digital audio tape cassette
    :cvar AE: Audio disc Audio disc (excluding CD-Audio): use for
        ‘Yellow book’ (CD-Rom-style) discs, including for example mp3
        CDs, and use coding in &lt;ProductFormDetail&gt; to specify the
        format of the data on the disc
    :cvar AF: Audio tape Audio tape (analogue open reel tape)
    :cvar AG: MiniDisc Sony MiniDisc format
    :cvar AH: CD-Extra Audio compact disc with part CD-ROM content, also
        termed CD-Plus or Enhanced-CD: use for ‘Blue book’ and
        ‘Yellow/Red book’ two-session discs
    :cvar AI: DVD Audio
    :cvar AJ: Downloadable audio file Digital audio recording
        downloadable to the purchaser’s own device(s)
    :cvar AK: Pre-recorded digital audio player For example, Playaway
        audiobook and player: use coding in &lt;ProductFormDetail&gt; to
        specify the recording format, if required
    :cvar AL: Pre-recorded SD card For example, Audiofy audiobook chip
    :cvar AM: LP Vinyl disc (analogue).
    :cvar AN: Downloadable and online audio file Digital audio recording
        available both by download to the purchaser’s own device(s) and
        by online (eg streamed) access
    :cvar AO: Online audio file Digital audio recording available online
        (eg streamed), not downloadable to the purchaser’s own device(s)
    :cvar AZ: Other audio format Other audio format not specified by AB
        to AO. Further detail is expected in
        &lt;ProductFormDescription&gt;, as &lt;ProductFormDetail&gt; and
        &lt;ProductFormFeature&gt; are unlikely to be sufficient
    :cvar BA: Book Book – detail unspecified. Use only when the form is
        unknown and no further detail can be provided. Prefer BZ plus
        &lt;ProductFormDescription&gt; if detail is available but no
        other B* code applies
    :cvar BB: Hardback Hardback or cased book
    :cvar BC: Paperback / softback Paperback or other softback book
    :cvar BD: Loose-leaf Loose-leaf book
    :cvar BE: Spiral bound Spiral, comb or coil bound book
    :cvar BF: Pamphlet Pamphlet, stapled (de: ‘geheftet’). Includes low-
        extent wire-stitched books bound without a distinct spine (eg
        many comic book ‘floppies’)
    :cvar BG: Leather / fine binding Use &lt;ProductFormDetail&gt; to
        provide additional description
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
        and intended to be collected and bound into a complete book.
    :cvar BO: Fold-out book or chart Concertina-folded booklet or chart,
        designed to fold to pocket or regular page size, and usually
        bound within distinct board or card covers (de: ‘Leporello’)
    :cvar BP: Foam book A children’s book whose cover and pages are made
        of foam
    :cvar BZ: Other book format Other book format or binding not
        specified by BB to BP. Further detail is expected in
        &lt;ProductFormDescription&gt;, as &lt;ProductFormDetail&gt; and
        &lt;ProductFormFeature&gt; are unlikely to be sufficient
    :cvar CA: Sheet map Sheet map – detail unspecified. Use only when
        the form is unknown and no further detail can be provided.
        Prefer CZ plus &lt;ProductFormDescription&gt; if detail is
        available but no other C* code applies
    :cvar CB: Sheet map, folded
    :cvar CC: Sheet map, flat
    :cvar CD: Sheet map, rolled See &lt;ProductPackaging&gt; and
        Codelist 80 for ‘rolled in tube’
    :cvar CE: Globe Globe or planisphere
    :cvar CZ: Other cartographic Other cartographic format not specified
        by CB to CE. Further detail is expected in
        &lt;ProductFormDescription&gt;, as &lt;ProductFormDetail&gt; and
        &lt;ProductFormFeature&gt; are unlikely to be sufficient
    :cvar DA: Digital (on physical carrier) Digital content delivered on
        a physical carrier (detail unspecified). Use only when the form
        is unknown and no further detail can be provided. Prefer DZ plus
        &lt;ProductFormDescription&gt; if detail is available but no
        other D* code applies
    :cvar DB: CD-ROM
    :cvar DC: CD-I CD interactive: use for ‘Green book’ discs
    :cvar DE: Game cartridge
    :cvar DF: Diskette AKA ‘floppy disc’
    :cvar DI: DVD-ROM
    :cvar DJ: Secure Digital (SD) Memory Card
    :cvar DK: Compact Flash Memory Card
    :cvar DL: Memory Stick Memory Card
    :cvar DM: USB Flash Drive
    :cvar DN: Double-sided CD/DVD Double-sided disc, one side Audio
        CD/CD-ROM, other side DVD
    :cvar DO: BR-ROM (Blu Ray ROM)
    :cvar DZ: Other digital carrier Other carrier of digital content not
        specified by DB to DO. Further detail is expected in
        &lt;ProductFormDescription&gt;, as &lt;ProductFormDetail&gt; and
        &lt;ProductFormFeature&gt; are unlikely to be sufficient
    :cvar EA: Digital (delivered electronically) Digital content
        delivered electronically (delivery method unspecified). Use only
        when the form and delivery method is unknown, or when no other
        E* code applies and the delivery method is described in
        &lt;ProductFormDescription&gt;. Note, use
        &lt;ProductFormDetail&gt; to specify file format
    :cvar EB: Digital download and online Digital content available both
        by download and by online access
    :cvar EC: Digital online Digital content accessed online only
    :cvar ED: Digital download Digital content delivered by download
        only
    :cvar FA: Film or transparency Film or transparency – detail
        unspecified. Use only when the form is unknown and no further
        detail can be provided. Prefer FZ plus
        &lt;ProductFormDescription&gt; if detail is available but no
        other F* code applies
    :cvar FC: Slides Photographic transparencies mounted for projection
    :cvar FD: OHP transparencies Transparencies for overhead projector
    :cvar FE: Filmstrip Photographic transparencies, unmounted but cut
        into short multi-frame strips
    :cvar FF: Film Continuous movie film as opposed to filmstrip
    :cvar FZ: Other film or transparency format Other film or
        transparency format not specified by FB to FF. Further detail is
        expected in &lt;ProductFormDescription&gt;, as
        &lt;ProductFormDetail&gt; and &lt;ProductFormFeature&gt; are
        unlikely to be sufficient
    :cvar LA: Digital product license Digital product license (delivery
        method unspecified). Use only when the form is unknown, or when
        no other L* code applies and the delivery method is described in
        &lt;ProductFormDescription&gt;
    :cvar LB: Digital product license key Digital product license
        delivered through the retail supply chain as a physical ‘key’,
        typically a card or booklet containing a code enabling the
        purchaser to download the associated product
    :cvar LC: Digital product license code Digital product license
        delivered by email or other electronic distribution, typically
        providing a code enabling the purchaser to activate, upgrade or
        extend the license supplied with the associated product
    :cvar MA: Microform Microform – detail unspecified. Use only when
        the form is unknown and no further detail can be provided.
        Prefer MZ plus &lt;ProductFormDescription&gt; if detail is
        available but no other M* code applies
    :cvar MB: Microfiche
    :cvar MC: Microfilm Roll microfilm
    :cvar MZ: Other microform Other microform not specified by MB or MC.
        Further detail is expected in &lt;ProductFormDescription&gt;, as
        &lt;ProductFormDetail&gt; and &lt;ProductFormFeature&gt; are
        unlikely to be sufficient
    :cvar PA: Miscellaneous print Miscellaneous printed material –
        detail unspecified. Use only when the form is unknown and no
        further detail can be provided. Prefer PZ plus
        &lt;ProductFormDescription&gt; if detail is available but no
        other P* code applies
    :cvar PB: Address book May use &lt;ProductFormDetail&gt; codes P201
        to P204 to specify binding
    :cvar PC: Calendar
    :cvar PD: Cards Cards, flash cards (eg for teaching reading),
        revision cards, divination, playing or trading cards
    :cvar PE: Copymasters Copymasters, photocopiable sheets
    :cvar PF: Diary or journal May use &lt;ProductFormDetail&gt; codes
        P201 to P204 to specify binding
    :cvar PG: Frieze Narrow strip-shaped printed sheet used mostly for
        education or children’s products (eg depicting alphabet, number
        line, procession of illustrated characters etc). Usually
        intended for horizontal display
    :cvar PH: Kit Parts for post-purchase assembly, including card, wood
        or plastic parts or model components, interlocking construction
        blocks, beads and other crafting materials etc
    :cvar PI: Sheet music May use &lt;ProductFormDetail&gt; codes P201
        to P204 to specify binding
    :cvar PJ: Postcard book or pack Including greeting cards and packs.
        For bound books (usually with perforated sheets to remove
        cards), may use &lt;ProductFormDetail&gt; codes P201 to P204 to
        specify binding
    :cvar PK: Poster Poster for retail sale – see also XF
    :cvar PL: Record book Record book (eg ‘birthday book’, ‘baby book’):
        binding unspecified; may use &lt;ProductFormDetail&gt; codes
        P201 to P204 to specify binding
    :cvar PM: Wallet or folder Wallet, folder or box (containing loose
        sheets etc, or empty): it is preferable to code the contents and
        treat ‘wallet’ (or folder / box) as packaging in
        &lt;ProductPackaging&gt; with Codelist 80, but if this is not
        possible (eg where the product is empty and intended for storing
        other loose items) the product as a whole may be coded as a
        ‘wallet’. For binders intended for loose leaf or partwork
        publications intended to be updateable, see codes BD, BN
    :cvar PN: Pictures or photographs
    :cvar PO: Wallchart
    :cvar PP: Stickers
    :cvar PQ: Plate (lámina) A book-sized (as opposed to poster-sized)
        sheet, usually in color or high quality print
    :cvar PR: Notebook / blank book A book with all pages blank for the
        buyer’s own use; may use &lt;ProductFormDetail&gt; codes P201 to
        P204 to specify binding
    :cvar PS: Organizer May use &lt;ProductFormDetail&gt; codes P201 to
        P204 to specify binding
    :cvar PT: Bookmark
    :cvar PU: Leaflet Folded but unbound
    :cvar PV: Book plates Ex libris’ book labels and packs
    :cvar PZ: Other printed item Other printed item not specified by PB
        to PQ. Further detail is expected in
        &lt;ProductFormDescription&gt;, as &lt;ProductFormDetail&gt; and
        &lt;ProductFormFeature&gt; are unlikely to be sufficient
    :cvar SA: Multiple-component retail product Presentation
        unspecified: format of product components must be given in
        &lt;ProductPart&gt;. Use only when the packaging of the product
        is unknown, or when no other S* code applies and the
        presentation is described in &lt;ProductFormDescription&gt;
    :cvar SB: Multiple-component retail product, boxed Format of product
        components must be given in &lt;ProductPart&gt;
    :cvar SC: Multiple-component retail product, slip-cased Format of
        product components must be given in &lt;ProductPart&gt;
    :cvar SD: Multiple-component retail product, shrink-wrapped Format
        of product components must be given in &lt;ProductPart&gt;. Use
        code XL for a shrink-wrapped pack for trade supply, where the
        retail items it contains are intended for sale individually
    :cvar SE: Multiple-component retail product, loose Format of product
        components must be given in &lt;ProductPart&gt;
    :cvar SF: Multiple-component retail product, part(s) enclosed
        Multiple component product where subsidiary product part(s)
        is/are supplied as enclosures to the primary part, eg a book
        with a CD packaged in a sleeve glued within the back cover.
        Format of product components must be given in
        &lt;ProductPart&gt;
    :cvar SG: Multiple-component retail product, entirely digital
        Multiple component product where all parts are digital, and
        delivered as separate files, eg a group of individual EPUB
        files, an EPUB with a PDF, an e-book with a license to access a
        range of online resources, etc. Format of product components
        must be given in &lt;ProductPart&gt;
    :cvar VA: Video Video – detail unspecified. Use only when the form
        is unknown and no further detail can be provided. Prefer VZ plus
        &lt;ProductFormDescription&gt; if detail is available but no
        other V* code applies
    :cvar VF: Videodisc eg Laserdisc
    :cvar VI: DVD video DVD video: specify TV standard in
        &lt;ProductFormDetail&gt;
    :cvar VJ: VHS video VHS videotape: specify TV standard in
        &lt;ProductFormDetail&gt;
    :cvar VK: Betamax video Betamax videotape: specify TV standard in
        &lt;ProductFormDetail&gt;
    :cvar VL: VCD VideoCD
    :cvar VM: SVCD Super VideoCD
    :cvar VN: HD DVD High definition DVD disc, Toshiba HD DVD format
    :cvar VO: Blu-ray High definition DVD disc, Sony Blu-ray format
    :cvar VP: UMD Video Sony Universal Media disc
    :cvar VQ: CBHD China Blue High-Definition, derivative of HD-DVD
    :cvar VZ: Other video format Other video format not specified by VB
        to VQ. Further detail is expected in
        &lt;ProductFormDescription&gt;, as &lt;ProductFormDetail&gt; and
        &lt;ProductFormFeature&gt; are unlikely to be sufficient
    :cvar XA: Trade-only material Trade-only material (unspecified). Use
        only when the form is unknown and no further detail can be
        provided. Prefer XZ plus &lt;ProductFormDescription&gt; if
        detail is available but no other X* code applies
    :cvar XB: Dumpbin – empty
    :cvar XC: Dumpbin – filled Dumpbin with contents. ISBN (where
        applicable) and format of contained items must be given in
        &lt;ProductPart&gt;
    :cvar XD: Counterpack – empty
    :cvar XE: Counterpack – filled Counterpack with contents. ISBN
        (where applicable) and format of contained items must be given
        in &lt;ProductPart&gt;
    :cvar XF: Poster, promotional Promotional poster for display, not
        for sale – see also PK
    :cvar XG: Shelf strip
    :cvar XH: Window piece Promotional piece for shop window display
    :cvar XI: Streamer
    :cvar XJ: Spinner – empty
    :cvar XK: Large book display Large scale facsimile of book for
        promotional display
    :cvar XL: Shrink-wrapped pack A quantity pack with its own product
        code, usually for trade supply only: the retail items it
        contains are intended for sale individually. ISBN (where
        applicable) and format of contained items must be given in
        &lt;ProductPart&gt;. For products or product bundles supplied
        individually shrink-wrapped for retail sale, use code SD
    :cvar XM: Boxed pack A quantity pack with its own product code,
        usually for trade supply only: the retail items it contains are
        intended for sale individually. ISBN (where applicable) and
        format of contained items must be given in &lt;ProductPart&gt;.
        For products or product bundles boxed individually for retail
        sale, use code SB
    :cvar XN: Pack (outer packaging unspecified) A quantity pack with
        its own product code, usually for trade supply only: the retail
        items it contains are intended for sale individually. ISBN
        (where applicable) and format of contained items must be given
        in &lt;ProductPart&gt;. Use only when the pack is neither
        shrinp-wrapped nor boxed
    :cvar XO: Spinner – filled Spinner with contents. ISBN(s) (where
        applicable) and detail of contained items must be given in
        &lt;ProductPart&gt;
    :cvar XY: Other point of sale – including retail product Other point
        of sale material not specified by XB to XO, supplied with
        included product(s) for retail sale. The retail product(s) must
        be described in &lt;ProductPart&gt;. Further detail of the POS
        material is expected in &lt;ProductFormDescription&gt;, as
        &lt;ProductFormDetail&gt; and &lt;ProductFormFeature&gt; are
        unlikely to be sufficient
    :cvar XZ: Other point of sale Other point of sale material not
        specified by XB to XY, promotional or decorative. Further detail
        is expected in &lt;ProductFormDescription&gt;, as
        &lt;ProductFormDetail&gt; and &lt;ProductFormFeature&gt; are
        unlikely to be sufficient
    :cvar ZA: General merchandise General merchandise, book accessories
        and non-book products – unspecified. Use only when the form is
        unknown and no further detail can be provided. Prefer ZX, ZY or
        ZZ, plus &lt;ProductFormDescription&gt; if detail is available
        but no other Z* code applies
    :cvar ZB: Doll or figure Including action figures, figurines
    :cvar ZC: Soft toy Soft or plush toy
    :cvar ZD: Toy Including educational toys (where no other code is
        relevant)
    :cvar ZE: Game Board game, or other game (except computer game: see
        DE and other D* codes)
    :cvar ZF: T-shirt
    :cvar ZG: E-book reader Dedicated e-book reading device, typically
        with mono screen
    :cvar ZH: Tablet computer General purpose tablet computer, typically
        with color screen
    :cvar ZI: Audiobook player Dedicated audiobook player device,
        typically including book-related features like bookmarking
    :cvar ZJ: Jigsaw Jigsaw or similar ‘shapes’ puzzle
    :cvar ZK: Mug For example, branded, promotional or tie-in drinking
        mug, cup etc
    :cvar ZL: Tote bag For example, branded, promotional or tie-in bag
    :cvar ZM: Tableware For example, branded, promotional or tie-in
        plates, bowls etc (note for mugs and cups, use code ZK)
    :cvar ZN: Umbrella For example, branded, promotional or tie-in
        umbrella
    :cvar ZO: Paints, crayons, pencils Coloring set, including pens,
        chalks, etc
    :cvar ZP: Handicraft kit Handicraft kit or set, eg sewing, crochet,
        weaving, basketry, beadwork, leather, wood or metalworking,
        pottery and glassworking, candlemaking etc
    :cvar ZX: Other toy/game accessories Other toy, game and puzzle
        items not specified by ZB to ZQ, generally accessories to other
        products etc. Further detail is expected in
        &lt;ProductFormDescription&gt;, as &lt;ProductFormDetail&gt; and
        &lt;ProductFormFeature&gt; are unlikely to be sufficient
    :cvar ZY: Other apparel Other apparel items not specified by ZB to
        ZQ, including branded, promotional or tie-in scarves, caps,
        aprons, dress-up costumes etc. Further detail is expected in
        &lt;ProductFormDescription&gt;, as &lt;ProductFormDetail&gt; and
        &lt;ProductFormFeature&gt; are unlikely to be sufficient
    :cvar ZZ: Other merchandise Other branded, promotional or tie-in
        merchandise not specified by ZB to ZY. Further detail is
        expected in &lt;ProductFormDescription&gt;, as
        &lt;ProductFormDetail&gt; and &lt;ProductFormFeature&gt; are
        unlikely to be sufficient
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
    AM = "AM"
    AN = "AN"
    AO = "AO"
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
    DE = "DE"
    DF = "DF"
    DI = "DI"
    DJ = "DJ"
    DK = "DK"
    DL = "DL"
    DM = "DM"
    DN = "DN"
    DO = "DO"
    DZ = "DZ"
    EA = "EA"
    EB = "EB"
    EC = "EC"
    ED = "ED"
    FA = "FA"
    FC = "FC"
    FD = "FD"
    FE = "FE"
    FF = "FF"
    FZ = "FZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
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
    PU = "PU"
    PV = "PV"
    PZ = "PZ"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SF = "SF"
    SG = "SG"
    VA = "VA"
    VF = "VF"
    VI = "VI"
    VJ = "VJ"
    VK = "VK"
    VL = "VL"
    VM = "VM"
    VN = "VN"
    VO = "VO"
    VP = "VP"
    VQ = "VQ"
    VZ = "VZ"
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
    XN = "XN"
    XO = "XO"
    XY = "XY"
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
    ZK = "ZK"
    ZL = "ZL"
    ZM = "ZM"
    ZN = "ZN"
    ZO = "ZO"
    ZP = "ZP"
    ZX = "ZX"
    ZY = "ZY"
    ZZ = "ZZ"


class List151(Enum):
    """
    Contributor place relator.

    :cvar VALUE_00: Associated with To express unknown relationship
        types (for use when expressing legacy ONIX 2.1 data in ONIX 3.0)
    :cvar VALUE_01: Born in
    :cvar VALUE_02: Died in
    :cvar VALUE_03: Formerly resided in
    :cvar VALUE_04: Currently resides in
    :cvar VALUE_05: Educated in
    :cvar VALUE_06: Worked in
    :cvar VALUE_07: Flourished in (‘Floruit’)
    :cvar VALUE_08: Citizen of Or nationality. For use with country
        codes only
    :cvar VALUE_09: Registered in The place of legal registration of an
        organization
    :cvar VALUE_10: Operating from The place an organization or part of
        an organization is based or operates from
    :cvar VALUE_11: Eligible for geographical marketing programs
        Contributor is eligible for national, regional or local
        marketing support. Use with country code, region code or
        country/region plus location, as appropriate
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


class List152(Enum):
    """
    Illustrated / not illustrated.

    :cvar VALUE_01: No Not illustrated
    :cvar VALUE_02: Yes Illustrated
    """

    VALUE_01 = "01"
    VALUE_02 = "02"


class List153(Enum):
    """
    Text type.

    :cvar VALUE_01: Sender-defined text To be used only in circumstances
        where the parties to an exchange have agreed to include text
        which (a) is not for general distribution, and (b) cannot be
        coded elsewhere. If more than one type of text is sent, it must
        be identified by tagging within the text itself
    :cvar VALUE_02: Short description/annotation Of the product. Limited
        to a maximum of 350 characters
    :cvar VALUE_03: Description Of the product. Length unrestricted
    :cvar VALUE_04: Table of contents Used for a table of contents sent
        as a single text field, which may or may not carry structure
        expressed using XHTML
    :cvar VALUE_05: Primary cover copy Primary descriptive blurb usually
        taken from the back cover or jacket, or occasionally from the
        cover/jacket flaps. See also code 27
    :cvar VALUE_06: Review quote A quote taken from a review of the
        product or of the work in question where there is no need to
        take account of different editions
    :cvar VALUE_07: Review quote: previous edition A quote taken from a
        review of a previous edition of the work
    :cvar VALUE_08: Review quote: previous work A quote taken from a
        review of a previous work by the same author(s) or in the same
        series
    :cvar VALUE_09: Endorsement A quote usually provided by a celebrity
        or another author to promote a new book, not from a review
    :cvar VALUE_10: Promotional headline A promotional phrase which is
        intended to headline a description of the product
    :cvar VALUE_11: Feature Text describing a feature of a product to
        which the publisher wishes to draw attention for promotional
        purposes. Each separate feature should be described by a
        separate repeat, so that formatting can be applied at the
        discretion of the receiver of the ONIX record, or multiple
        features can be described using appropriate XHTML markup
    :cvar VALUE_12: Biographical note A note referring to all
        contributors to a product – NOT linked to a single contributor
    :cvar VALUE_13: Publisher’s notice A statement included by a
        publisher in fulfillment of contractual obligations, such as a
        disclaimer, sponsor statement, or legal notice of any sort. Note
        that the inclusion of such a notice cannot and does not imply
        that a user of the ONIX record is obliged to reproduce it
    :cvar VALUE_14: Excerpt A short excerpt from the main text of the
        work
    :cvar VALUE_15: Index Used for an index sent as a single text field,
        which may be structured using XHTML
    :cvar VALUE_16: Short description/annotation for collection (of
        which the product is a part.) Limited to a maximum of 350
        characters
    :cvar VALUE_17: Description for collection (of which the product is
        a part.) Length unrestricted
    :cvar VALUE_18: New feature As code 11 but used for a new feature of
        this edition or version
    :cvar VALUE_19: Version history
    :cvar VALUE_20: Open access statement Short summary statement of
        open access status and any related conditions (eg ‘Open access –
        no commercial use’), primarily for marketing purposes. Should
        always be accompanied by a link to the complete license (see
        &lt;EpubLicense&gt; or code 99 in List 158)
    :cvar VALUE_21: Digital exclusivity statement Short summary
        statement that the product is available only in digital formats
        (eg ‘Digital exclusive’). If a non-digital version is planned,
        &lt;ContentDate&gt; should be used to specify the date when
        exclusivity will end (use content date role code 15). If a non-
        digital version is available, the statement should not be
        included
    :cvar VALUE_22: Official recommendation For example a recommendation
        or approval provided by a ministry of education or other
        official body. Use &lt;Text&gt; to provide details and ideally
        use &lt;TextSourceCorporate&gt; to name the approver
    :cvar VALUE_23: JBPA description Short description in format
        specified by Japanese Book Publishers Association
    :cvar VALUE_24: schema.org snippet JSON-LD snippet suitable for use
        within an HTML &lt;script type="application/ld+json"&gt; tag,
        containing structured metadata suitable for use with schema.org
    :cvar VALUE_25: Errata
    :cvar VALUE_26: Introduction Introduction, preface or the text of
        other preliminary material, sent as a single text field, which
        may be structured using XHTML
    :cvar VALUE_27: Secondary cover copy Secondary descriptive blurb
        taken from the cover/jacket flaps, or occasionally from the back
        cover or jacket, used only when there are two separate texts and
        the primary text is included using code 05
    :cvar VALUE_28: Full cast and credit list For use with dramatized
        audiobooks, filmed entertainment etc, for a cast list sent as a
        single text field, which may or may not carry structure
        expressed using XHTML
    :cvar VALUE_29: Bibliography Complete list of books by the
        author(s), supplied as a single text field, which may be
        structured using (X)HTML
    :cvar VALUE_30: Abstract Formal summary of content (normally used
        with academic and scholarly content only)
    :cvar VALUE_31: Rules or instructions Eg for a game, kit
    :cvar VALUE_32: List of contents Eg for a game, kit. Note: use code
        04 for a Table of Contents of a book
    :cvar VALUE_33: Short description/annotation for imprint Length
        limited to a maximum of 350 characters
    :cvar VALUE_34: Description for imprint Length unrestricted
    :cvar VALUE_35: Short description/annotation for publisher Length
        limited to a maximum of 350 characters
    :cvar VALUE_36: Description for publisher Length unrestricted
    :cvar VALUE_37: Cover line (US) Reading line – line of usually
        explanatory copy on cover, somewhat like a subtitle but not on
        the title page and added by the publisher, eg ‘with 125
        illustrated recipes’
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


class List154(Enum):
    """
    Content audience.

    :cvar VALUE_00: Unrestricted Any audience
    :cvar VALUE_01: Restricted Distribution by agreement between the
        parties to the ONIX exchange (this value is provided to cover
        applications where ONIX content includes material which is not
        for general distribution)
    :cvar VALUE_02: Booktrade Distributors, bookstores, publisher’s own
        staff etc
    :cvar VALUE_03: End-customers
    :cvar VALUE_04: Librarians
    :cvar VALUE_05: Teachers
    :cvar VALUE_06: Students
    :cvar VALUE_07: Press Press or other media
    :cvar VALUE_08: Shopping comparison service Where a specially
        formatted description is required for this audience
    :cvar VALUE_09: Search engine index Text not intended for display,
        but may be used (in addition to any less restricted text) for
        indexing and search
    :cvar VALUE_10: Bloggers (Including vloggers, influencers etc) Where
        this is distinct from end customers or the Press
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


class List155(Enum):
    """
    Content date role.

    :cvar VALUE_01: Publication date Nominal date of publication (of the
        content item or supporting resource)
    :cvar VALUE_04: Broadcast date Date when a TV or radio program was /
        will be broadcast
    :cvar VALUE_14: From date Date from which a content item or
        supporting resource may be referenced or used. The content is
        embargoed until this date
    :cvar VALUE_15: Until date Date until which a content item or
        supporting resource may be referenced or used
    :cvar VALUE_17: Last updated Date when a resource was last changed
        or updated
    :cvar VALUE_24: From… until date Combines From date and Until date
        to define a period (both dates are inclusive). Use for example
        with dateformat 06
    :cvar VALUE_27: Available from Date from which a supporting resource
        is available for download. Note that this date also implies that
        it can be immediately displayed to the intended audience, unless
        a From date (code 14) is also supplied and is later than the
        Available from date
    :cvar VALUE_28: Available until Date until which a supporting
        resource is available for download. Note that this date does not
        imply it must be removed from display to the intended audience
        on this date – for this, use Until date (code 15)
    :cvar VALUE_31: Associated start date Start date referenced by the
        supporting resource, for example, the ‘earliest exam date’ for
        an official recommendation
    :cvar VALUE_32: Associated end date End date referenced by the
        supporting resource, for example, the ‘latest exam date’ for an
        official recommendation
    """

    VALUE_01 = "01"
    VALUE_04 = "04"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_17 = "17"
    VALUE_24 = "24"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_31 = "31"
    VALUE_32 = "32"


class List156(Enum):
    """
    Cited content type.

    :cvar VALUE_01: Review The full text of a review in a third-party
        publication in any medium
    :cvar VALUE_02: Bestseller list
    :cvar VALUE_03: Media mention Other than a review
    :cvar VALUE_04: ‘One locality, one book’ program Inclusion in a
        program such as ‘Chicago Reads’, ‘Seattle Reads’, ‘Canada
        Reads’, ‘One Dublin, one book’
    :cvar VALUE_05: Curated list For example a ‘best books of the year’
        or ‘25 books you should have read’ list, without regard to their
        bestseller status
    :cvar VALUE_06: Commentary / discussion For example a third party
        podcast episode, social media message, newsletter issue, other
        commentary (see also code 03 for very brief items)
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"


class List157(Enum):
    """
    Content source type.

    :cvar VALUE_01: Printed media
    :cvar VALUE_02: Website
    :cvar VALUE_03: Radio
    :cvar VALUE_04: TV
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"


class List158(Enum):
    """
    Resource content type.

    :cvar VALUE_01: Front cover 2D
    :cvar VALUE_02: Back cover 2D
    :cvar VALUE_03: Cover / pack Not limited to front or back, including
        3D perspective
    :cvar VALUE_04: Contributor picture Photograph or portrait of
        contributor(s)
    :cvar VALUE_05: Series image / artwork
    :cvar VALUE_06: Series logo
    :cvar VALUE_07: Product image / artwork For example, an isolated
        image from the front cover (without text), image of a completed
        jigsaw
    :cvar VALUE_08: Product logo
    :cvar VALUE_09: Publisher logo
    :cvar VALUE_10: Imprint logo
    :cvar VALUE_11: Contributor interview
    :cvar VALUE_12: Contributor presentation Contributor presentation
        and/or commentary
    :cvar VALUE_13: Contributor reading
    :cvar VALUE_14: Contributor event schedule Link to a schedule in
        iCalendar format
    :cvar VALUE_15: Sample content For example: a short excerpt, sample
        text or a complete sample chapter, page images, screenshots etc
    :cvar VALUE_16: Widget A ‘look inside’ feature presented as a small
        embeddable application
    :cvar VALUE_17: Review Review text held in a separate downloadable
        file, not in the ONIX record. Equivalent of code 06 in List 153.
        Use the &lt;TextContent&gt; composite for review quotes carried
        in the ONIX record. Use the &lt;CitedContent&gt; composite for a
        third-party review which is referenced from the ONIX record. Use
        &lt;SupportingResource&gt; for review text offered as a separate
        file resource for reproduction as part of promotional material
        for the product
    :cvar VALUE_18: Commentary / discussion For example a publisher’s
        podcast episode, social media message, newsletter issue, other
        commentary
    :cvar VALUE_19: Reading group guide
    :cvar VALUE_20: Teacher’s guide Incuding associated teacher /
        instructor resources
    :cvar VALUE_21: Feature article Feature article provided by
        publisher
    :cvar VALUE_22: Character ‘interview’ Fictional character
        ‘interview’
    :cvar VALUE_23: Wallpaper / screensaver
    :cvar VALUE_24: Press release
    :cvar VALUE_25: Table of contents A table of contents held in a
        separate downloadable file, not in the ONIX record. Equivalent
        of code 04 in List 153. Use the &lt;TextContent&gt; composite
        for a table of contents carried in the ONIX record. Use
        &lt;Supporting Resource&gt; for text offered as a separate file
        resource
    :cvar VALUE_26: Trailer A promotional video (or audio), similar to a
        movie trailer (sometimes referred to as a ‘book trailer’)
    :cvar VALUE_27: Cover thumbnail Intended ONLY for transitional use,
        where ONIX 2.1 records referencing existing thumbnail assets of
        unknown pixel size are being re-expressed in ONIX 3.0. Use code
        01 for all new cover assets, and where the pixel size of older
        assets is known
    :cvar VALUE_28: Full content The full content of the product (or the
        product itself), supplied for example to support full-text
        search or indexing
    :cvar VALUE_29: Full cover Includes cover, back cover, spine and –
        where appropriate – any flaps
    :cvar VALUE_30: Master brand logo
    :cvar VALUE_31: Description Descriptive text in a separate
        downloadable file, not in the ONIX record. Equivalent of code 03
        in List 153. Use the &lt;TextContent&gt; composite for
        descriptions carried in the ONIX record. Use &lt;Supporting
        Resource&gt; for text offered as a separate file resource for
        reproduction as part of promotional material for the product
    :cvar VALUE_32: Index Index text held in a separate downloadable
        file, not in the ONIX record. Equivalent of code 15 in List 153.
        Use the &lt;TextContent&gt; composite for index text carried in
        the ONIX record. Use &lt;Supporting Resource&gt; for an index
        offered as a separate file resource
    :cvar VALUE_33: Student’s guide Including associated student /
        learner resources
    :cvar VALUE_34: Publisher’s catalogue For example a PDF or other
        digital representation of a publisher’s ‘new titles’ or range
        catalog
    :cvar VALUE_35: Online advertisement panel For example a banner ad
        for the product. Pixel dimensions should typically be included
        in &lt;ResourceVersionFeature&gt;
    :cvar VALUE_36: Online advertisement page (de: ‘Búhnenbild’)
    :cvar VALUE_37: Promotional event material For example, posters,
        logos, banners, advertising templates for use in connection with
        a promotional event
    :cvar VALUE_38: Digital review copy Availability of a digital
        review, evaluation or sample copy, or a digital proof copy,
        which may be limited to authorised users or account holders, but
        should otherwise be fully readable and functional
    :cvar VALUE_39: Instructional material For example, video showing
        how to use the product
    :cvar VALUE_40: Errata
    :cvar VALUE_41: Introduction Introduction, preface or other
        preliminary material in a separate resource file
    :cvar VALUE_42: Collection description Descriptive material in a
        separate resource file, not in the ONIX record. Equivalent of
        code 17 in List 153. Use the &lt;TextContent&gt; composite for
        collection descriptions carried in the ONIX record. Use
        &lt;Supporting Resource&gt; for material (which need not be
        solely only) offered as a separate file resource for
        reproduction as part of promotional material for the product and
        collection
    :cvar VALUE_43: Bibliography Complete list of books by the
        author(s), supplied as a separate resource file
    :cvar VALUE_44: Abstract Formal summary of content (normally used
        with academic and scholarly content only)
    :cvar VALUE_45: Cover holding image Image that may be used for
        promotional purposes in place of a front cover, ONLY where the
        front cover itself cannot be provided or used for any reason.
        Typically, holding images may comprise logos, artwork or an
        unfinished front cover image. Senders should ensure removal of
        the holding image from the record as soon as a cover image is
        available. Recipients must ensure replacement of the holding
        image with the cover image when it is supplied
    :cvar VALUE_46: Rules or instructions Eg for a game, kit
    :cvar VALUE_47: Transcript Full transcript of audio or video content
        of the product
    :cvar VALUE_48: Full cast and credit list For use with dramatised
        audiobooks, filmed entertainment etc, for a cast list sent as a
        separate resource file, not in the ONIX record. Equivalent of
        code 28 in List 153
    :cvar VALUE_49: Image for social media Image – not specifically a
        cover image or artwork, contributor image, or logo – explicitly
        intended for use in social media
    :cvar VALUE_50: Supplementary learning resources Eg downloadable
        worksheets, home learning materials
    :cvar VALUE_51: Cover flap 2D, front or back flap image
    :cvar VALUE_99: License Link to a license covering permitted usage
        of the product content. Deprecated in favor of
        &lt;EpubLicense&gt;. This was a temporary workaround in ONIX
        3.0, and use of &lt;EpubLicense&gt; is strongly preferred
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
    VALUE_99 = "99"


class List159(Enum):
    """
    Resource mode.

    :cvar VALUE_01: Application An executable together with data on
        which it operates
    :cvar VALUE_02: Audio A sound recording
    :cvar VALUE_03: Image A still image
    :cvar VALUE_04: Text Readable text, with or without associated
        images etc
    :cvar VALUE_05: Video Moving images, with or without accompanying
        sound
    :cvar VALUE_06: Multi-mode A website or other supporting resource
        delivering content in a variety of modes
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"


class List16(Enum):
    """
    Work identifier type.

    :cvar VALUE_01: Proprietary Note that &lt;IDTypeName&gt; is required
        with proprietary identifiers
    :cvar VALUE_02: ISBN-10 10-character ISBN of manifestation of work,
        when this is the only work identifier available – now Deprecated
        in ONIX for Books, except where providing historical information
        for compatibility with legacy systems. It should only be used in
        relation to products published before 2007 – when ISBN-13
        superseded it – and should never be used as the ONLY identifier
        (it should always be accompanied by the correct GTIN-13 /
        ISBN-13 of the manifestation of the work)
    :cvar VALUE_06: DOI Digital Object Identifier (variable length and
        character set, beginning ‘10.’ and without https://doi.org/ or
        the older http://dx.doi.org/)
    :cvar VALUE_11: ISTC International Standard Text Code (16
        characters: numerals and letters A-F, unhyphenated)
    :cvar VALUE_15: ISBN-13 13-character ISBN of a manifestation of
        work, when this is the only work identifier available (13
        digits, without spaces or hyphens)
    :cvar VALUE_18: ISRC International Standard Recording Code
    :cvar VALUE_32: GLIMIR Global Library Manifestation Identifier,
        OCLC’s ‘manifestation cluster’ ID
    :cvar VALUE_33: OWI OCLC Work Identifier
    :cvar VALUE_39: ISCC International Standard Content Code, a
        ‘similarity hash’ derived algorithmically from the content
        itself (see https://iscc.codes). &lt;IDValue&gt; is a sequence
        comprising the Meta-Code and Content-Code ISCC-UNITSs generated
        from a digital manifestation of the work, as a variable-length
        case-insensitive alphanumeric string (or 27 characters including
        one hyphen if using ISCC v1.0, but this is deprecated). Note
        alphabetic characters in v1.x ISCCs use Base32 encoding and are
        conventionally upper case. The ‘ISCC:’ prefix is omitted. Only
        for use in ONIX 3.0 or later
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_06 = "06"
    VALUE_11 = "11"
    VALUE_15 = "15"
    VALUE_18 = "18"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_39 = "39"


class List160(Enum):
    """
    Resource feature type.

    :cvar VALUE_01: Required credit Credit that must be displayed when a
        resource is used (eg ‘Photo Jerry Bauer’ or ‘© Magnum Photo’).
        Credit text should be carried in &lt;FeatureNote&gt;
    :cvar VALUE_02: Caption Explanatory caption that may accompany a
        resource (eg use to identify an author in a photograph). Caption
        text should be carried in &lt;FeatureNote&gt;
    :cvar VALUE_03: Copyright holder Copyright holder of resource
        (indicative only, as the resource can be used without
        consultation). Copyright text should be carried in
        &lt;FeatureNote&gt;
    :cvar VALUE_04: Length in minutes Approximate length in minutes of
        an audio or video resource. &lt;FeatureValue&gt; should contain
        the length of time as an integer number of minutes
    :cvar VALUE_05: ISNI of resource contributor Use to link resource to
        a contributor unambiguously, for example with Resource Content
        types 04, 11–14 from List 158, particularly where the product
        has more than a single contributor. &lt;FeatureValue&gt;
        contains the 16-digit ISNI, which must match an ISNI given in an
        instance of &lt;Contributor&gt;
    :cvar VALUE_06: Proprietary ID of resource contributor Use to link
        resource to a contributor unambiguously, for example with
        Resource Content types 04, 11–14 from List 158, particularly
        where the product has more than a single contributor.
        &lt;FeatureValue&gt; contains the proprietary ID, which must
        match a proprietary ID given in an instance of
        &lt;Contributor&gt;
    :cvar VALUE_07: Resource alternative text &lt;FeatureNote&gt; is
        Alternative text for the resource, which might be presented to
        visually-impaired readers
    :cvar VALUE_08: Background color of image resource
        &lt;FeatureValue&gt; is a 24-bit RGB or 32-bit RBGA color in
        hexadecimal, eg fff2de for an opaque warm cream. Used when the
        resource – for example a 3D image of the product – includes a
        background, or if used with an alpha channel, when the image is
        irregularly shaped or contains a semi-transparent shadow thrown
        against a background
    :cvar VALUE_09: Attribute of product image resource
        &lt;FeatureValue&gt; is an ONIX code from List 256 that
        describes an attribute of a product image resource (eg
        perspective, content)
    :cvar VALUE_10: Background color of page &lt;FeatureValue&gt; is a
        24-bit RGB color in hexadecimal, eg ffc300 for a rich yellow-
        orange, used when the resource supplier requests a specific
        background color be displayed behind the resource on a web page
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


class List161(Enum):
    """
    Resource form.

    :cvar VALUE_01: Linkable resource A resource that may be accessed by
        a hyperlink. The current host (eg the ONIX sender, who may be
        the publisher) will provide ongoing hosting services for the
        resource for the active life of the product (or at least until
        the Until Date specified in &lt;ContentDate&gt;). The ONIX
        recipient may embed the URL in a consumer facing-website (eg as
        the src attribute in an &lt;img&gt; link), and need not host an
        independent copy of the resource
    :cvar VALUE_02: Downloadable file A file that may be downloaded on
        demand for third-party use. The ONIX sender will host a copy of
        the resource until the specified Until Date, but only for the
        ONIX recipient’s direct use. The ONIX recipient should download
        a copy of the resource, and must host an independent copy of the
        resource if it is used on a consumer-facing website. Special
        attention should be paid to the ‘Last Updated’
        &lt;ContentDate&gt; to ensure the independent copy of the
        resource is kept up to date
    :cvar VALUE_03: Embeddable application An application which is
        supplied in a form which can be embedded into a third-party
        webpage. As type 02, except the resource contains active content
        such as JavaScript, Flash, etc
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"


class List162(Enum):
    """
    Resource version feature type.

    :cvar VALUE_01: File format Resource Version Feature Value carries a
        code from List 178
    :cvar VALUE_02: Image height in pixels Resource Version Feature
        Value carries an integer
    :cvar VALUE_03: Image width in pixels Resource Version Feature Value
        carries an integer
    :cvar VALUE_04: Filename Resource Version Feature Value carries the
        filename of the supporting resource, necessary only when it is
        different from the last part of the path provided in
        &lt;ResourceLink&gt;
    :cvar VALUE_05: Approximate download file size in megabytes Resource
        Version Feature Value carries a decimal number only, suggested
        no more than 2 or 3 significant digits (eg 1.7, not 1.7462 or
        1.75MB)
    :cvar VALUE_06: MD5 hash value MD5 hash value of the resource file.
        &lt;ResourceVersionFeatureValue&gt; should contain the 128-bit
        digest value (as 32 hexadecimal digits). Can be used as a
        cryptographic check on the integrity of a resource after it has
        been retrieved
    :cvar VALUE_07: Exact download file size in bytes Resource Version
        Feature Value carries a integer number only (eg 1831023)
    :cvar VALUE_08: SHA-256 hash value SHA-256 hash value of the
        resource file. &lt;ResourceVersionFeatureValue&gt; should
        contain the 256-bit digest value (as 64 hexadecimal digits). Can
        be used as a cryptographic check on the integrity of a resource
        after it has been retrieved
    :cvar VALUE_09: ISCC International Standard Content Code, a
        ‘similarity hash’ derived algorithmically from the resource
        content itself (see https://iscc.codes). &lt;IDValue&gt; is the
        ISCC-CODE generated from a digital manifestation of the work, as
        a variable-length case-insensitive alphanumeric string (or 55
        characters including three hyphens if using ISCC v1.0, but this
        is deprecated). Note alphabetic characters in v1.x ISCCs use
        Base32 encoding and are conventionally upper case. The ‘ISCC:’
        prefix is omitted
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


class List163(Enum):
    """
    Publishing date role.

    :cvar VALUE_01: Publication date Nominal date of publication. This
        date is primarily used for planning, promotion and other
        business process purposes, and is not necessarily the first date
        for retail sales or fulfillment of pre-orders. In the absence of
        a sales embargo date, retail sales and pre-order fulfillment may
        begin as soon as stock is available to the retailer
    :cvar VALUE_02: Sales embargo date If there is an embargo on retail
        sales (in the market) before a certain date, the date from which
        the embargo is lifted and retail sales and fulfillment of pre-
        orders are permitted. In the absence of an embargo date, retail
        sales and pre-order fulfillment may begin as soon as stock is
        available to the retailer
    :cvar VALUE_09: Public announcement date Date when a new product may
        be announced to the general public. Prior to the announcement
        date, the product data is intended for internal use by the
        recipient and supply chain partners only. After the announcement
        date, or in the absence of an announcement date, the planned
        product may be announced to the public as soon as metadata is
        available
    :cvar VALUE_10: Trade announcement date Date when a new product may
        be announced to the book trade only. Prior to the announcement
        date, the product information is intended for internal use by
        the recipient only. After the announcement date, or in the
        absence of a trade announcement date, the planned product may be
        announced to supply chain partners (but not necessarily made
        public – see the Public announcement date) as soon as metadata
        is available
    :cvar VALUE_11: Date of first publication Date when the work
        incorporated in a product was first published. For works in
        translation, see also Date of first publication in original
        language (code 20)
    :cvar VALUE_12: Last reprint date Date when a product was last
        reprinted
    :cvar VALUE_13: Out-of-print / permanently withdrawn date Date when
        a product was (or will be) declared out-of-print, permanently
        withdrawn from sale or deleted
    :cvar VALUE_16: Last reissue date Date when a product was last
        reissued
    :cvar VALUE_19: Publication date of print counterpart Date of
        publication of a printed book which is the direct print
        counterpart to a digital product. The counterpart product may be
        included in &lt;RelatedProduct&gt; using code 13
    :cvar VALUE_20: Date of first publication in original language Date
        when the original language version of work incorporated in a
        product was first published (note, use only on works in
        translation – see code 11 for first publication date in the
        translated language)
    :cvar VALUE_21: Forthcoming reissue date Date when a product will be
        reissued
    :cvar VALUE_22: Expected availability date after temporary
        withdrawal Date when a product that has been temporary withdrawn
        from sale or recalled for any reason is expected to become
        available again, eg after correction of quality or technical
        issues
    :cvar VALUE_23: Review embargo date Date from which reviews of a
        product may be published eg in newspapers and magazines or
        online. Provided to the book trade for information only:
        newspapers and magazines are not expected to be recipients of
        ONIX metadata
    :cvar VALUE_25: Publisher’s reservation order deadline Latest date
        on which an order may be placed with the publisher for
        guaranteed delivery prior to the publication date. May or may
        not be linked to a special reservation or pre-publication price
    :cvar VALUE_26: Forthcoming reprint date Date when a product will be
        reprinted
    :cvar VALUE_27: Preorder embargo date Earliest date a retail
        ‘preorder’ can be placed (in the market), where this is distinct
        from the public announcement date. In the absence of a preorder
        embargo, advance orders can be placed as soon as metadata is
        available to the consumer (this would be the public announcement
        date, or in the absence of a public announcement date, the
        earliest date metadata is available to the retailer)
    :cvar VALUE_28: Transfer date Date of acquisition of product by new
        publisher (use with publishing roles 09 and 13)
    :cvar VALUE_29: Date of production For an audiovisual work (eg on
        DVD)
    :cvar VALUE_30: Streaming embargo date For digital products that are
        available to end customers both as a download and streamed, the
        earliest date the product can be made available on a stream,
        where the streamed version becomes available later than the
        download. For the download, see code 02 if it is embargoed or
        code 01 if there is no embargo
    :cvar VALUE_31: Subscription embargo date For digital products that
        are available to end customers both as purchases and as part of
        a subscription package, the earliest date the product can be
        made available by subscription, where the product may not be
        included in a subscription package until shome while after
        publication. For ordinary sales, see code 02 if there is a sales
        embargo or code 01 if there is no embargo
    :cvar VALUE_35: CIP date Date by which CIP copy is required for
        inclusion in the product
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_16 = "16"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_30 = "30"
    VALUE_31 = "31"
    VALUE_35 = "35"


class List164(Enum):
    """
    Work relation.

    :cvar VALUE_01: Manifestation of Product A is or includes a
        manifestation of work X. (There is a direct parent–child
        relation between work X and the product). The instance of
        &lt;RelatedWork&gt; must include an identifier for work X
    :cvar VALUE_02: Derived from Product A is or includes a
        manifestation of a work X which is derived (directly) from
        related work W in one or more of the ways specified in the
        former ISTC rules. (There is a relationship between a
        grandparent work W and a parent work X, and between that parent
        work and the product.) This relation type is intended to enable
        products with a common ‘grandparent’ work to be linked without
        specifying the precise nature of their derivation, and without
        necessarily assigning an identifier to the product’s parent work
        X. The instance of &lt;RelatedWork&gt; must include an
        identifier for work W. Codes 20–30 may be used instead to
        provide details of the derivation of work X from work W
    :cvar VALUE_03: Related work is derived from this Product A is a
        manifestation of a work X from which related work Y is
        (directly) derived in one or more of the ways specified in the
        former ISTC rules. (There is a relationship between a parent
        work X and a child work Y, and between the parent work X and the
        product.) The instance of &lt;RelatedWork&gt; must include an
        identifier for work Y. Codes 40–50 may be used instead to
        provide details of the derivation of work Y from work X
    :cvar VALUE_04: Other work in same (bibliographic) collection
        Product A is a manifestation of a work X in the same
        (bibliographic) collection as related work Z. (There is a
        relationship between the parent work X and a ‘same collection’
        work Z, and between the parent work X and the product.) The
        instance of &lt;RelatedWork&gt; must include an identifier for
        work Z
    :cvar VALUE_05: Other work by same contributor Product A is a
        manifestation of a work X by the same contributor(s) as related
        work Z. (There is a relationship between the parent work X and a
        work Z where X and Z have at least one contributor in common,
        and between the parent work X and the product.) The instance of
        &lt;RelatedWork&gt; must include an identifier for work Z
    :cvar VALUE_06: Manifestation of original work Product A is or
        includes a manifestation of work X. (There is a direct
        parent–child relation between work X and the product, and work X
        is original, ie not a derived work of any kind – there is no
        work W.) The instance of &lt;RelatedWork&gt; must include an
        identifier for work X. See code 01 if the originality of X is
        unspecified or unknown
    :cvar VALUE_21: Derived from by abridgement Product A is or includes
        a manifestation of a work X which is derived directly from
        related work W by abridgement. (There is a relationship between
        the grandparent [unabridged] work W and the parent [abridged]
        work X, and between the parent work X and the product.) The
        instance of &lt;RelatedWork&gt; must include an identifier for
        [unabridged] work W. &lt;EditionType&gt; of product A would
        normally be ABR. See code 02 if the method of derivation of X
        from W is unknown or unstated. The [abridged] parent work X may
        be identified using a separate instance of &lt;RelatedWork&gt;
        with relation code 01
    :cvar VALUE_22: Derived from by annotation Product A is or includes
        a manifestation of a work X which is derived directly from
        related work W by annotation. The instance of
        &lt;RelatedWork&gt; must include an identifier for [unannotated]
        work W. &lt;EditionType&gt; of product X would normally be ANN,
        VAR etc. See code 02 if the method of derivation of X from W is
        unknown or unstated. The [annotated] parent work X may be
        identified using a separate instance of &lt;RelatedWork&gt; with
        relation code 01
    :cvar VALUE_23: Derived from by compilation The content of the work
        X has been formed by compilation of work W and another work Z.
        The instance of &lt;RelatedWork&gt; must include an identifier
        for work W. &lt;EditionType&gt; of product A may be CMB. Work Z
        may be identified using a separate instance of
        &lt;RelatedWork&gt; with code 23. The compiled parent work X may
        be identified using a separate instance of &lt;Related&gt; work
        with relation code 01
    :cvar VALUE_24: Derived from by criticism The content of the work W
        has been augmented by the addition of critical commendary to
        form work X. The instance of &lt;RelatedWork&gt; must include an
        identifier for work W. &lt;EditionType&gt; of Product A would
        normally be CRI
    :cvar VALUE_25: Derived from by excerption The content of the work X
        is an excerpt from work W. The instance of &lt;RelatedWork&gt;
        must include an identifier for [complete] work W
    :cvar VALUE_26: Derived from by expurgation Offensive or unsuitable
        text material has been removed from work W to form work X. The
        instance of &lt;RelatedWork&gt; must include an identifier for
        [unsuitable] work W. &lt;EditionType&gt; of Product A would
        normally be EXP
    :cvar VALUE_27: Derived from by addition (of non-text material) The
        content of work W has been augmented by the addition of
        significant non-textual elements to form work X. The instance of
        &lt;RelatedWork&gt; must include an identifier for [unaugmented]
        work W. &lt;EditionType&gt; of product A may be ILL, ENH etc
    :cvar VALUE_28: Derived from by revision The content of work W has
        been revised and/or expanded or enlarged to form work X
        [including addition, deletion or replacement of text material].
        The instance of &lt;RelatedWork&gt; must include an identifier
        for [unrevised] work W. &lt;EditionType&gt; of product A may be
        REV, NED, etc, or A may be numbered
    :cvar VALUE_29: Derived from via translation The content of work W
        has been translated into another language to form work X. The
        instance of &lt;RelatedWork&gt; must include an identifier for
        [untranslated] work W
    :cvar VALUE_30: Derived from via adaptation The content of work W
        has been adapted [into a different literary form] to form work
        X. The instance of &lt;RelatedWork&gt; must include an
        identifier for [unadapted] work W. &lt;EditionType&gt; of
        product A would normally be ADP, ACT etc
    :cvar VALUE_31: Derived from by subtraction (of non-text material)
        The content of work W has been modified by the removal of
        significant non-textual elements to form work X. The instance of
        &lt;RelatedWork&gt; must include an identifier for work W
    :cvar VALUE_41: Related work is derived from this by abridgement
        Product A is a manifestation of a work X from which the related
        work Y is (directly) derived by abridgement. (There is a
        relationship between the parent [unabridged] work X and the
        child [abridged] work Y, and between parent work X and the
        product.) The instance of &lt;RelatedWork&gt; must include the
        identifier for [abridged] work Y. See code 03 if the method of
        derivation of Y from X is unknown or unstated. The [unabridged]
        parent work X may be identified using a separate instance of
        &lt;RelatedWork&gt; with relation code 01 or 06
    :cvar VALUE_42: Related work is derived from this by annotation
    :cvar VALUE_43: Related work is derived from this by compilation
    :cvar VALUE_44: Related work is derived from this by criticism
    :cvar VALUE_45: Related work is derived from this by excerption
    :cvar VALUE_46: Related work is derived from this by expurgation
    :cvar VALUE_47: Related work is derived from this by addition (of
        non-text material)
    :cvar VALUE_48: Related work is derived from this by revision
    :cvar VALUE_49: Related work is derived from this via translation
    :cvar VALUE_50: Related work is derived from this via adaptation
    :cvar VALUE_51: Derived from this by subtraction (of non-text
        material)
    :cvar VALUE_98: Manifestation of LRM work Product A is or includes a
        manifestation of an expression of LRM work X. Do not use, except
        as a workaround for differences between LRM works and
        expressions, and ONIX works in LRM library practice, and always
        also include a relationship to an ONIX work using code 01
    :cvar VALUE_99: Manifestation of LRM expression Product A is or
        includes a manifestation of an LRM expression with the same
        content, same agents and in the same modality (text, audio,
        video etc) as work X. Do not use, except as a workaround for
        differences between LRM expressions and ONIX works in LRM
        library practice, and always also include a relationship to an
        ONIX work using code 01
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
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
    VALUE_98 = "98"
    VALUE_99 = "99"


class List165(Enum):
    """
    Supplier own code type.

    :cvar VALUE_01: Supplier’s sales classification A rating applied by
        a supplier (typically a wholesaler) to indicate its assessment
        of the expected or actual sales performance of a product
    :cvar VALUE_02: Supplier’s bonus eligibility A supplier’s coding of
        the eligibility of a product for a bonus scheme on overall sales
    :cvar VALUE_03: Publisher’s sales classification A rating applied by
        the publisher to indicate a sales category (eg
        backlist/frontlist, core stock etc). Use only when the publisher
        is not the ‘supplier’
    :cvar VALUE_04: Supplier’s pricing restriction classification A
        classification applied by a supplier to a product sold on Agency
        terms, to indicate that retail price restrictions are applicable
    :cvar VALUE_05: Supplier’s sales expectation Code is the ISBN of
        another book that had sales (both in terms of copy numbers and
        customer profile) comparable to that the distributor or supplier
        estimates for the product. &lt;SupplierCodeValue&gt; must be an
        ISBN-13 or GTIN-13
    :cvar VALUE_06: Publisher’s sales expectation Code is the ISBN of
        another book that had sales (both in terms of copy numbers and
        customer profile) comparable to that the publisher estimates for
        the product. &lt;SupplierCodeValue&gt; must be an ISBN-13 or
        GTIN-13
    :cvar VALUE_07: Supplier’s order routing eligibility Code indicates
        whether an order can be placed with the supplier indirectly via
        an intermediary system. The code name type indicates the
        specific intermediate order aggregation/routing platform and the
        code indicates the eligibility
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"


class List166(Enum):
    """
    Supply date role.

    :cvar VALUE_02: Sales embargo date If there is an embargo on retail
        sales (of copies from the supplier) before a certain date and
        this is later than any general or market-wide embargo date, the
        date from which the embargo is lifted and retail sales and
        fulfillment of pre-orders are permitted. Use code 02 here ONLY
        in the exceptional case when the embargo is supplier-specific.
        More general market-wide or global sales embargos should be
        specified in &lt;MarketDate&gt; or &lt;PublishingDate&gt; codes.
        In the absence of any supplier-specific, market-wide or general
        embargo date, retail sales and pre-order fulfillment may begin
        as soon as stock is available to the retailer
    :cvar VALUE_08: Expected availability date The date on which
        physical stock is expected to be available to be shipped from
        the supplier to retailers, or a digital product is expected to
        be released by the publisher or digital asset distributor to
        retailers or their retail platform providers
    :cvar VALUE_18: Last date for returns Last date when returns will be
        accepted, generally for a product which is being remaindered or
        put out of print
    :cvar VALUE_25: Reservation order deadline Latest date on which an
        order may be placed for guaranteed delivery prior to the
        publication date. May or may not be linked to a special
        reservation or pre-publication price
    :cvar VALUE_29: Last redownload date Latest date on which existing
        owners or licensees may download or re-download a copy of the
        product. Existing users may continue to use their local copy of
        the product
    :cvar VALUE_30: Last TPM date Date on which any required technical
        protection measures (DRM) support will be withdrawn. DRM-
        protected products may not be usable after this date
    :cvar VALUE_34: Expected warehouse date The date on which physical
        stock is expected to be delivered to the supplier from the
        manufacturer or from a primary distributor. For the distributor
        or wholesaler (the supplier) this is the ‘goods in’ date, as
        contrasted with the Expected availability date, code 08, which
        is the ‘goods out’ date
    :cvar VALUE_50: New supplier start date First date on which the
        supplier specified in &lt;NewSupplier&gt; will accept orders.
        Note the first date would typically be the day after the old
        supplier end date, but they may overlap if there is an agreement
        to forward any orders between old and new supplier for
        fulfillment
    :cvar VALUE_51: Supplier end date Last date on which the supplier
        specified in &lt;Supplier&gt; will accept orders. New supplier
        should be specified where available. Note last date would
        typically be the day before the new supplier start date, but
        they may overlap if there is an agreement to forward any orders
        between old and new supplier for fulfillment
    """

    VALUE_02 = "02"
    VALUE_08 = "08"
    VALUE_18 = "18"
    VALUE_25 = "25"
    VALUE_29 = "29"
    VALUE_30 = "30"
    VALUE_34 = "34"
    VALUE_50 = "50"
    VALUE_51 = "51"


class List167(Enum):
    """
    Price condition type.

    :cvar VALUE_00: No conditions Allows positive indication that there
        are no conditions (the default if &lt;PriceCondition&gt; is
        omitted)
    :cvar VALUE_01: Includes updates Purchase at this price includes
        specified updates
    :cvar VALUE_02: Must also purchase updates Purchase at this price
        requires commitment to purchase specified updates, not included
        in price
    :cvar VALUE_03: Updates available Updates may be purchased
        separately, no minimum commitment required
    :cvar VALUE_04: Linked subsequent purchase price Use with
        &lt;PriceConditionQuantity&gt; and &lt;ProductIdentifier&gt;.
        Purchase at this price requires commitment to purchase the
        specified linked product, which is not included in the price
    :cvar VALUE_05: Linked prior purchase price Use with
        &lt;PriceConditionQuantity&gt; and &lt;ProductIdentifier&gt;.
        Purchase at this price requires prior purchase of the specified
        linked product
    :cvar VALUE_06: Linked price Use with &lt;PriceConditionQuantity&gt;
        and &lt;ProductIdentifier&gt;. Purchase at this price requires
        simultaneous purchase of the specified linked product, which is
        not included in the price
    :cvar VALUE_07: Auto-renewing The rental or subscription will
        automatically renew at the end of the period unless actively
        cancelled
    :cvar VALUE_08: Combined price Purchase at this price includes the
        price of the specified other product
    :cvar VALUE_10: Rental duration The duration of the rental to which
        the price applies. Deprecated, use &lt;PriceConstraint&gt;
        instead
    :cvar VALUE_11: Rental to purchase Purchase at this price requires
        prior rental of the product. &lt;PriceConditionQuantity&gt;
        gives minimum prior rental period, and &lt;ProductIdentifier&gt;
        may be used if rental uses a different product identifier
    :cvar VALUE_12: Rental extension Upgrade to longer rental duration.
        &lt;PriceConditionQuantity&gt; gives minimum prior rental
        duration, and &lt;ProductIdentifier&gt; may be used if rental
        uses a different product identifier. Separate price constraint
        with time limited license duration (code 07) specifies the new
        combined rental duration
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


class List168(Enum):
    """
    Price condition quantity type.

    :cvar VALUE_01: Time period The price condition quantity represents
        a time period
    :cvar VALUE_02: Number of updates The price condition quantity is a
        number of updates
    :cvar VALUE_03: Number of linked products Use with Price condition
        type 06 and a Quantity of units. Price is valid when purchased
        with a specific number of products from a list of product
        identifiers provided in the associated &lt;ProductIdentifier&gt;
        composites. Use for example when describing a price for this
        product which is valid if it is purchased along with any two
        from a list of other products
    :cvar VALUE_04: Number of copies of this product Use with Price
        condition type 06 and a Quantity of units. Meeting the Price
        condition qualifies for purchase of a specified number of copies
        of this product at this price. Use for example when describing a
        price that applies to the specified number of units of this
        product which is valid if they are purchased along with a number
        of copies of another product
    :cvar VALUE_05: Minimum number of linked products Use with Price
        condition type 06 and a Quantity of units. Price is valid when
        purchased with at least a specific number of products from a
        list of product identifiers provided in the associated
        &lt;ProductIdentifier&gt; composites. Use for example when
        describing a price for this product which is valid if it is
        purchased along with any two from a list of other products
    :cvar VALUE_06: Maximum number of copies of this product (at this
        price). Use with Price condition type 06 and a Quantity of
        units. Meeting the Price condition qualifies for purchase of up
        to the specified number of copies of this product at this price.
        Use for example when describing a price that applies to the
        specified number of units of this product which is valid if they
        are purchased along with a number of copies of another product
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"


class List169(Enum):
    """
    Quantity unit.

    :cvar VALUE_00: Units The quantity refers to a unit implied by the
        quantity type
    :cvar VALUE_07: Days
    :cvar VALUE_08: Weeks
    :cvar VALUE_09: Months
    :cvar VALUE_10: Years
    :cvar VALUE_20: Classes Multiple copies or units suitable for a
        class. A ‘class’ is a group of learners attending a specific
        course or lesson and generally taught as a group
    """

    VALUE_00 = "00"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_20 = "20"


class List17(Enum):
    """
    Contributor role code.

    :cvar A01: By (author) Author of a textual work
    :cvar A02: With With or as told to: ‘ghost’ or secondary author of a
        literary work (for clarity, should not be used for true ‘ghost’
        authors who are not credited on the book and whose existence is
        secret)
    :cvar A03: Screenplay by Writer of screenplay or script (film or
        video)
    :cvar A04: Libretto by Writer of libretto (opera): see also A31
    :cvar A05: Lyrics by Author of lyrics (song): see also A31
    :cvar A06: By (composer) Composer of music
    :cvar A07: By (artist) Visual artist when named as the primary
        creator of, eg, a book of reproductions of artworks
    :cvar A08: By (photographer) Photographer when named as the primary
        creator of, eg, a book of photographs
    :cvar A09: Created by For example of editorial concept, of board
        game, etc
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
    :cvar A28: Interpreted through Use with narratives drawn from an
        oral tradition, where no ‘ownership’ of the narrative is
        claimed. See also B33. Only for use in ONIX 3.0 or later
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
        book. Use with A12 for ‘drawn by’. Use A40 for ‘finished by’,
        but prefer more specific codes A46 to A48 instead of A40 unless
        the more specific secondary roles are inappropriate, unclear or
        unavailable
    :cvar A41: Paper engineering by Designer or paper engineer of die-
        cuts, press-outs or of pop-ups in a pop-up book, who may be
        different from the illustrator
    :cvar A42: Continued by Use where a standard work is being continued
        by somebody other than the original author
    :cvar A43: Interviewer
    :cvar A44: Interviewee
    :cvar A45: Comic script by Writer of dialogue, captions in a comic
        book (following an outline by the primary writer)
    :cvar A46: Inker Renders final comic book line art based on work of
        the illustrator or penciller (code A12). Preferred to code A40
    :cvar A47: Colorist Provides comic book color art and effects.
        Preferred to code A40
    :cvar A48: Letterer Creates comic book text balloons and other text
        elements (where this is a distinct role from script writer
        and/or illustrator), or creates calligraphy in non-comic
        products
    :cvar A49: Cover inker Renders final comic book cover line art based
        on work of the cover designer (code A36), where different from
        the inker of the interior line art. Only for use in ONIX 3.0 or
        later
    :cvar A50: Cover colorist Provides comic book cover color art and
        effects, where different from the colorist of the interior art
        and effects. Only for use in ONIX 3.0 or later
    :cvar A51: Research by Person or organization responsible for
        performing research on which the work is based. Only for use in
        ONIX 3.0 or later
    :cvar A52: Original character design (for comic books). Only for use
        in ONIX 3.0 or later
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
        publication (de: Begruendet von)
    :cvar B18: Prepared for publication by
    :cvar B19: Associate editor
    :cvar B20: Consultant editor Use also for ‘advisory editor’, ‘series
        advisor’, ‘editorial consultant’ etc
    :cvar B21: General editor
    :cvar B22: Dramatized by
    :cvar B23: General rapporteur In Europe, an expert editor who takes
        responsibility for the legal content of a collaborative law
        volume
    :cvar B24: Literary editor Editor who is responsible for
        establishing the text used in an edition of a literary work,
        where this is recognised as a distinctive role (es: editor
        literario)
    :cvar B25: Arranged by (music)
    :cvar B26: Technical editor Responsible for the technical accuracy
        and language, may also be involved in coordinating and preparing
        technical material for publication
    :cvar B27: Thesis advisor or supervisor
    :cvar B28: Thesis examiner
    :cvar B29: Scientific editor Responsible overall for the scientific
        content of the publication
    :cvar B30: Historical advisor Only for use in ONIX 3.0 or later
    :cvar B31: Original editor Editor of the first edition (usually of a
        standard work) who is not an editor of the current edition. Only
        for use in ONIX 3.0 or later
    :cvar B32: Translation revised by Where possible, use with B06 for
        the original translator. Only for use in ONIX 3.0 or later
    :cvar B33: Transcribed by As told to. Use with narratives drawn from
        an oral tradition, and with B03 (Retold by), B07 (As told by) or
        A28 (Interpreted through). Only for use in ONIX 3.0 or later
    :cvar B99: Other adaptation by Other type of adaptation or editing
        not specified above
    :cvar C01: Compiled by For puzzles, directories, statistics, etc
    :cvar C02: Selected by For textual material (eg for an anthology)
    :cvar C03: Non-text material selected by Eg for a collection of
        photographs etc
    :cvar C04: Curated by Eg for an exhibition
    :cvar C99: Other compilation by Other type of compilation not
        specified above
    :cvar D01: Producer Of a film, of a theatrical or multimedia
        production, of dramatized audio etc
    :cvar D02: Director Of a film, of a theatrical or multimedia
        production, of dramatized audio etc
    :cvar D03: Conductor Conductor of a musical performance
    :cvar D04: Choreographer Of a dance performance. Only for use in
        ONIX 3.0 or later
    :cvar D99: Other direction by Other type of direction not specified
        above
    :cvar E01: Actor Performer in a dramatized production (including a
        voice actor in an audio production)
    :cvar E02: Dancer
    :cvar E03: Narrator Where the narrator is a character in a
        dramatized production (including a voice actor in an audio
        production). For the ‘narrator’ of a non-dramatized audiobook,
        use code E07
    :cvar E04: Commentator
    :cvar E05: Vocal soloist Singer etc
    :cvar E06: Instrumental soloist
    :cvar E07: Read by Reader of recorded text, as in an audiobook
    :cvar E08: Performed by (orchestra, band, ensemble) Name of a
        musical group in a performing role
    :cvar E09: Speaker Of a speech, lecture etc
    :cvar E10: Presenter Introduces and links other contributors and
        material, eg within a documentary
    :cvar E11: Introduction read by Reader of recorded introduction (or
        other ‘front matter’) in an audiobook. Only for use in ONIX 3.0
        or later
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
    :cvar Z03: Enacting jurisdiction For publication of laws,
        regulations, rulings etc. Only for use in ONIX 3.0 or later
    :cvar Z04: Peer reviewed Use with &lt;UnnamedPersons&gt; code 02 as
        a ‘flag’ to indicate the publication is anonymously peer-
        reviewed. Only for use in ONIX 3.0 or later
    :cvar Z05: Posthumously completed by May be associated with any
        contributor role, and placement should therefore be controlled
        by contributor sequence numbering. Only for use in ONIX 3.0 or
        later
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
    A28 = "A28"
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
    A49 = "A49"
    A50 = "A50"
    A51 = "A51"
    A52 = "A52"
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
    B30 = "B30"
    B31 = "B31"
    B32 = "B32"
    B33 = "B33"
    B99 = "B99"
    C01 = "C01"
    C02 = "C02"
    C03 = "C03"
    C04 = "C04"
    C99 = "C99"
    D01 = "D01"
    D02 = "D02"
    D03 = "D03"
    D04 = "D04"
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
    E11 = "E11"
    E99 = "E99"
    F01 = "F01"
    F02 = "F02"
    F99 = "F99"
    Z01 = "Z01"
    Z02 = "Z02"
    Z03 = "Z03"
    Z04 = "Z04"
    Z05 = "Z05"
    Z98 = "Z98"
    Z99 = "Z99"


class List170(Enum):
    """
    Discount type.

    :cvar VALUE_01: Rising discount Discount applied to all units in a
        qualifying order. The default if no &lt;DiscountType&gt; is
        specified
    :cvar VALUE_02: Rising discount (cumulative) Additional discount may
        be applied retrospectively, based on number of units ordered
        over a specific period
    :cvar VALUE_03: Progressive discount Discount applied to marginal
        units in a qualifying order
    :cvar VALUE_04: Progressive discount (cumulative) Previous orders
        within a specific time period are counted when calculating a
        progressive discount
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"


class List171(Enum):
    """
    Tax type.

    :cvar VALUE_01: VAT (Value-added tax) TVA, IVA, MwSt, GST etc,
        levied incrementally at all parts of the supply chain
    :cvar VALUE_02: GST (Sales tax) General sales tax, levied on retail
        sales
    :cvar VALUE_03: ECO ‘Green’ or eco-tax, levied to encourage
        responsible production or disposal, used only where this is
        identified separately from value-added or sales taxes
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"


class List173(Enum):
    """
    Price date role.

    :cvar VALUE_14: From date Date on which a price becomes effective
    :cvar VALUE_15: Until date Date on which a price ceases to be
        effective
    :cvar VALUE_24: From… until date Combines From date and Until date
        to define a period (both dates are inclusive). Use for example
        with dateformat 06
    """

    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_24 = "24"


class List174(Enum):
    """
    Printed on product.

    :cvar VALUE_01: No Price not printed on product
    :cvar VALUE_02: Yes Price printed on product
    """

    VALUE_01 = "01"
    VALUE_02 = "02"


class List175(Enum):
    """
    Product form detail.

    :cvar A101: CD standard audio format CD ‘red book’ format
    :cvar A102: SACD super audio format
    :cvar A103: MP3 format MPEG-1/2 Audio Layer III file
    :cvar A104: WAV format
    :cvar A105: Real Audio format
    :cvar A106: WMA Windows Media Audio format
    :cvar A107: AAC Advanced Audio Coding format
    :cvar A108: Ogg/Vorbis Vorbis audio format in the Ogg container
    :cvar A109: Audible Audio format proprietary to Audible.com
    :cvar A110: FLAC Free lossless audio codec
    :cvar A111: AIFF Audio Interchangeable File Format
    :cvar A112: ALAC Apple Lossless Audio Codec
    :cvar A113: W3C Audiobook format Audiobook package format
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
    :cvar A211: DAISY 3: full text with navigation and partial audio
        Reading systems may provide full audio via text-to-speech
    :cvar A212: DAISY 3: full text with navigation and no audio Reading
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
    :cvar A310: Sound effects Incidental sounds added to the audiobook
        narration (eg background environmental sounds)
    :cvar A311: Background music Incidental music added to the audiobook
        narration (eg to heighten atmosphere). Do not use where the
        music is a primary part of the audio
    :cvar A312: Without background sounds Pre-recorded audiobook
        narration does not contain any background sounds, including
        music, sound effects, etc, though music and effects may be
        present if isolated from the speech (ie the sounds do not
        overlap)
    :cvar A400: 64kbits/s Constant or average bit rate (eg of an mp3 or
        AAC audio file) 64kbits/second or more. Note the bit rate is the
        total across all channels, not a per channel rate
    :cvar A401: 128kbits/s Constant or average bit rate 128bbits/second
        or more
    :cvar A402: 192kbits/s
    :cvar A403: 256kbits/s
    :cvar A404: 320kbits/s
    :cvar A410: Mono Includes ‘stereo’ where channels are identical
    :cvar A420: Stereo Includes ‘joint stereo’
    :cvar A421: Stereo 2.1 Stereo plus low-frequency channel
    :cvar A441: Surround 4.1 Five-channel audio (including low-frequency
        channel)
    :cvar A451: Surround 5.1 Six-channel audio (including low-frequency
        channel)
    :cvar A471: Dolby Atmos Multi-channel ‘spatial’ audio (eg for 7.1.4
        speaker arrangements or processed for headphone delivery)
    :cvar B101: Mass market (rack) paperback In North America, a
        category of paperback characterized partly by page size
        (typically from 6¾ up to 7⅛ x 4¼ inches) and partly by target
        market and terms of trade. Use with Product Form code BC
    :cvar B102: Trade paperback (US) In North America, a category of
        paperback characterized partly by page size (larger than rack-
        sized) and partly by target market and terms of trade. AKA
        ‘quality paperback’, and including textbooks. Most paperback
        books sold in North America except ‘mass-market’ (B101) and
        ‘tall rack’ (B107) are correctly described with this code. Use
        with Product Form code BC
    :cvar B103: Digest format paperback In North America, a category of
        paperback characterized by page size (typically 7 x 5 inches)
        and generally used for children’s books; use with Product Form
        code BC. Note: was wrongly shown as B102 (duplicate entry) in
        Issue 3
    :cvar B104: A-format paperback In UK and IE, a category of paperback
        characterized by page size (normally 178 x 111 mm approx); use
        with Product Form code BC
    :cvar B105: B-format paperback In UK and IE, a category of paperback
        characterized by page size (normally 198 x 129 mm approx); use
        with Product Form code BC
    :cvar B106: Trade paperback (UK) In UK and IE, a category of
        paperback characterized largely by size (usually in traditional
        hardback dimensions), and often used for paperback originals or
        retailer/travel/export-exclusives; use with Product Form code BC
    :cvar B107: Tall rack paperback (US) In North America, a category of
        paperback characterised partly by page size (typically 7½ x 4¼
        inches) and partly by target market and terms of trade; use with
        Product Form code BC
    :cvar B108: A5 size Tankobon Japanese A-series size, 210 x 148mm. A
        tankobon is a complete collected story originally published in
        serialised form (eg in a magazine)
    :cvar B109: JIS B5 size Tankobon Japanese B-series size, 257 x 182mm
    :cvar B110: JIS B6 size Tankobon Japanese B-series size, 182 x 128mm
    :cvar B111: A6 size Bunko Japanese A-series size, 148 x 105mm
    :cvar B112: B40-dori Shinsho Japanese format, 182x103mm or 173x105mm
    :cvar B113: Pocket (Sweden, Norway, France) A Swedish, Norwegian,
        French paperback format, of no particular fixed size. Use with
        Product Form Code BC
    :cvar B114: Storpocket (Sweden) A Swedish paperback format, use with
        Product Form Code BC. In Finnish, Jättipokkari
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
        (ie parallel with the lines of text). Use with Product Form code
        BC – see www.dwarsligger.com
    :cvar B119: 46 size Japanese format, 188 x 127mm
    :cvar B120: 46-Henkei size Japanese format, approximately 188 x
        127mm
    :cvar B121: A4 297 x 210mm
    :cvar B122: A4-Henkei size Japanese format, approximately 297 x
        210mm
    :cvar B123: A5-Henkei size Japanese format, approximately 210 x
        146mm
    :cvar B124: B5-Henkei size Japanese format, approximately 257 x
        182mm
    :cvar B125: B6-Henkei size Japanese format, approximately 182 x
        128mm
    :cvar B126: AB size 257 x 210mm
    :cvar B127: JIS B7 size Japanese B-series size, 128 x 91mm
    :cvar B128: Kiku size Japanese format, 218 x 152mm or 227 x 152mm
    :cvar B129: Kiku-Henkei size Japanese format
    :cvar B130: JIS B4 size Japanese B-series size, 364 x 257 mm
    :cvar B131: Paperback (DE) German large paperback format, greater
        than about 205mm high, with flaps. Use with Product form code BC
    :cvar B132: Libro de bolsillo Spanish pocket paperback. Use with
        Product form code BC
    :cvar B133: Pocket-sized Pocket-sized format, usually less than
        about 205mm high, without necessarily implying a particular
        trade category (de: ,Taschenbuch‘; it: «Tascabile /
        Supertascabile»; es: «libro de bolsillo»; fr: « livre de poche »
        etc). Use with Product form code BB or BC. See also List 12 code
        04
    :cvar B134: A5 210 x 148mm
    :cvar B135: Mass market max paperback In North America, a category
        of paperback characterized partly by page size (typically 7⅛ x
        4¾ inches) and partly by target market and terms of trade. Use
        with Product Form code BC
    :cvar B139: Comic book size (US) Standard 10.25 x 6.625in size
        approx (260 x 170mm)
    :cvar B140: Comic album size (Euro) Standard 240 x 320mm size approx
    :cvar B141: B4-Henkei size Japanese format, approximately 364 x 257
        mm
    :cvar B201: Coloring / join-the-dot book
    :cvar B202: Lift-the-flap book
    :cvar B204: Miniature book
    :cvar B205: Moving picture / flicker book
    :cvar B206: Pop-up book
    :cvar B207: Scented / ‘smelly’ book
    :cvar B208: Sound story / ‘noisy’ book
    :cvar B209: Sticker book
    :cvar B210: Touch-and-feel book A book whose pages have a variety of
        textured inserts designed to stimulate tactile exploration: see
        also B214 and B215
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
    :cvar B216: Press-out puzzle pieces A book containing pages with
        die-cut or press-out pieces that can be used as a jigsaw, puzzle
        pieces, etc
    :cvar B221: Picture book Picture book, generally for children, with
        few words per illustration: use with applicable Product Form
        code
    :cvar B222: ‘Carousel’ book (aka ‘Star’ book). Tax treatment of
        products may differ from that of products with similar codes
        such as Book as toy or Pop-up book)
    :cvar B223: Pull-the-tab book A book with movable card ‘tabs’ within
        the pages. Pull a tab to reveal or animate part of a picture
        (distinct from a ‘lift-the-flap’ book, where flaps simply reveal
        hidden pictures, and not a ‘pop-up’ book with 3D paper
        engineering)
    :cvar B224: ‘Wordless’ book Picture book, generally for children
        though also used in augmentative and alternative education,
        without text in the body of the book. Also ‘silent books’,
        wordless graphic novels and comic books: use with applicable
        Product Form code
    :cvar B301: Loose leaf or partwork – sheets / parts and binder /
        wallet Use with Product Form code BD, BN or PM
    :cvar B302: Loose leaf or partwork – binder / wallet only Use with
        Product Form code BD, BN or PM
    :cvar B303: Loose leaf or partwork – sheets / parts only Use with
        Product Form code BD, BN or PM
    :cvar B304: Sewn AKA stitched; for ‘saddle-sewn’, see code B310
    :cvar B305: Unsewn / adhesive bound Including ‘perfect bound’,
        ‘glued’
    :cvar B306: Library binding Strengthened cloth-over-boards binding
        intended for libraries: use with Product form code BB
    :cvar B307: Reinforced binding Strengthened binding, not
        specifically intended for libraries: use with Product form code
        BB or BC
    :cvar B308: Half bound Highest qualiy material used on spine and
        corners only. Must be accompanied by a code specifiying a
        material, eg ‘half-bound real leather’
    :cvar B309: Quarter bound Highest qualiy material used on spine
        only. Must be accompanied by a code specifiying a material, eg
        ‘quarter bound real leather’
    :cvar B310: Saddle-sewn AKA ‘saddle-stitched’ or ‘wire-stitched’
    :cvar B311: Comb bound Round or oval plastic forms in a clamp-like
        configuration: use with Product Form code BE
    :cvar B312: Wire-O Twin loop metal wire spine: use with Product Form
        code BE
    :cvar B313: Concealed wire Cased over Coiled or Wire-O binding: use
        with Product Form code BE and Product Form Detail code B312 or
        B314
    :cvar B314: Coiled wire bound Spiral wire bound. Use with product
        form code BE. The default if a spiral binding type is not
        stated. Cf. Comb and Wire-O binding
    :cvar B315: Trade binding Hardcover binding intended for general
        consumers rather than libraries, use with Product form code BB.
        The default if a hardcover binding detail is not stated. cf.
        Library binding
    :cvar B316: Swiss binding Cover is attached to the book block along
        only one edge of the spine, allowing the cover to lay flat
    :cvar B317: Notched binding Refinement of perfect binding, with
        notches cut in the spine of the book block prior to glueing, to
        improve adhesion and durability
    :cvar B318: Lay-flat binding Hardcover or softcover where interior
        spreads lay flat across the spine
    :cvar B400: Self-covered Covers do not use a distinctive stock, but
        are the same as the body pages
    :cvar B401: Cloth over boards Cotton, linen or other woven fabric
        over boards. Use with &lt;ProductForm&gt; BB
    :cvar B402: Paper over boards Cellulose-based or similar non-woven
        material, which may be printed and may be embossed with an
        artificial cloth or leather-like texture, over boards. Use with
        &lt;ProductForm&gt; BB
    :cvar B403: Leather, real Covered with leather created by tanning
        animal hide. May be ‘full-grain’ using the entire thickness of
        the hide, ‘top grain’ using the outer layer of the hide, or
        ‘split’ using the inner layers of the hide. Split leather may be
        embossed with an artificial grain or texture. Use with
        &lt;ProductForm&gt; BG, and if appropriate with codes B308 or
        B309 (otherwise ‘full-bound’ is implied)
    :cvar B404: Leather, imitation Covered with synthetic leather-like
        material – polymer or non-animal fibre over a textile backing,
        usually coated and embossed with an artificial grain or texture.
        Leatherette, pleather etc. Use with &lt;ProductForm&gt; BB (or
        BG if particularly high-quality), and if appropriate with codes
        B308 or B309 (otherwise ‘full-bound’ is implied)
    :cvar B405: Leather, bonded Covered with leather reconstituted from
        a pulp made from shredded animal hide, layered on a fibre or
        textile backing, coated and usually embossed with an artificial
        grain or texture. Use with &lt;ProductForm&gt; BG, and if
        appropriate with codes B308 or B309 (otherwise ‘full-bound’ is
        implied)
    :cvar B406: Vellum Pages made with prepared but untanned animal skin
        (usually calf, occasionally goat or sheep). Includes parchment,
        a thicker and less refined form of animal skin, but not ‘paper
        vellum’ or vegetable parchment made from synthetic or plant
        fibres
    :cvar B407: Head and tail bands Decorative or functional
    :cvar B408: Decorated endpapers Illustrated or abstract printed
        endpapers, but not those solely of colored paper
    :cvar B409: Cloth Cloth, not necessarily over boards – cf B401
    :cvar B410: Imitation cloth Spanish ‘simil-tela’
    :cvar B411: Velvet
    :cvar B412: Flexible plastic / vinyl cover AKA ‘flexibound’: use
        with Product Form code BC
    :cvar B413: Plastic-covered Separate outer plastic cover, often
        transparent and allowing the cover to show through. Typically
        has pockets into which the cover tucks. See also B412, where the
        cover itself is plastic or vinyl
    :cvar B414: Vinyl-covered Separate outer vinyl cover. See also B412,
        where the cover itself is plastic or vinyl
    :cvar B415: Laminated cover Book, laminating material unspecified,
        often termed PLC or PPC (printed laminated case, printed paper
        case) when used with Product form BB. Use L101 for ‘whole
        product laminated’, eg a laminated sheet map or wallchart
    :cvar B416: Card cover With card cover (like a typical paperback).
        As distinct from a self-cover or more elaborate binding
    :cvar B417: Duplex-printed cover Printed both inside and outside the
        front and/or back cover
    :cvar B420: Delicate cover / jacket finish Cover or jacket finish
        may merit special handling or packaging during distribution and
        fulfilment, for example because of gloss varnish which may hold
        fingerprints or matt laminate liable to scuffing
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
    :cvar B511: Foldout With one or more gatefold or foldout sections
        bound in
    :cvar B512: Wide margin Pages include extra-wide margin specifically
        intended for hand-written annotations
    :cvar B513: With fastening strap Book with attached loop for fixing
        to baby stroller, cot, chair etc
    :cvar B514: With perforated pages With one or more pages perforated
        and intended to be torn out for use
    :cvar B515: Acid-free paper Printed on acid-free or alkaline
        buffered paper conforming with ISO 9706
    :cvar B516: Archival paper Printed on acid-free or alkaline buffered
        paper with a high cotton content, conforming with ISO 11108
    :cvar B517: With elasticated strap Strap acts as closure or as page
        marker
    :cvar B518: With serialized authenticity token For example,
        holographic sticker such as the banderol used in the Turkish
        book trade
    :cvar B519: With dust jacket poster Jacket in the form of a pamphlet
        or poster, specifically intended to be removed and read or used
        separately from the book
    :cvar B520: Rounded corners Usually die-cut rounding to foredge
        corners of cover (and/or to foredge page corners). See B212 for
        elaborate die-cutting
    :cvar B521: Splashproof Water-resistant or ‘waterproof’ cover and
        pages
    :cvar B522: Mineral paper Pages composed of ‘mineral paper’
        comprised of HDPE plastic and ground calcium carbonate, eg
        Stonepaper
    :cvar B601: Turn-around book A book in which half the content is
        printed upside-down, to be read the other way round. Also known
        as a ‘flip-book’ or ‘tête-bêche’ (Fr) binding, it has two front
        covers and a single spine. Usually an omnibus of two works
    :cvar B602: Unflipped manga format Manga with pages and panels in
        the sequence of (right-to-left flowing) Japanese-style design
    :cvar B603: Back-to-back book A book in which half the content is
        printed so as to be read from the other cover. All content is
        printed the same way up. Also known as ‘dos-à-dos’ (Fr) binding,
        it has two front covers and two spines. Usually an omnibus of
        two works
    :cvar B604: Flipped manga format Manga with pages and panels in the
        sequence mirrored from Japanese-style design (thus flowing left-
        to-right)
    :cvar B605: Variant turn-around book A book in which half the
        content is read the other way round from ‘back’ to ‘front’. A
        variant on ‘flip-book’ or ‘tête-bêche’ (fr) binding where the
        text is in two languages with different page progression (eg
        English and Arabic) and neither needs to be upside down, it has
        two front covers and a single spine. Usually an omnibus of a
        work and a derived translated work
    :cvar B606: Page progression LTR Pages are ordered left to right
        (the left page in a spread is read before the right). Note this
        does not specifically mean text on the page is also read left to
        right
    :cvar B607: Page progression RTL Pages are ordered right to left
    :cvar B608: Page progression TTB Pages are ordered top to bottom,
        with the spine oriented horizontally. See also Dwarsligger (code
        B118), a proprietary variation of this format
    :cvar B609: Page progression other Pages are ordered bottom to top,
        with the spine oriented horizontally, or in a way for which
        there is no other code
    :cvar B610: Syllabification Text shows syllable breaks
    :cvar B611: Upper case only For bicameral scripts, body text is
        upper case only
    :cvar B701: UK Uncontracted Braille Single letters only. Was
        formerly identified as UK Braille Grade 1
    :cvar B702: UK Contracted Braille With some letter combinations. Was
        formerly identified as UK Braille Grade 2
    :cvar B703: US Braille For US Braille, prefer codes B704 and B705 as
        appropriate
    :cvar B704: US Uncontracted Braille
    :cvar B705: US Contracted Braille
    :cvar B706: Unified English Braille For UEB, prefer codes B708 and
        B709 as appropriate
    :cvar B707: Moon Moon embossed alphabet, used by some print-impaired
        readers who have difficulties with Braille
    :cvar B708: Unified English Uncontracted Braille
    :cvar B709: Unified English Contracted Braille
    :cvar B750: Tactile images Eg charts, diagrams, maps, that are
        embossed or textured for accessibility purposes
    :cvar B751: Lenticular images Image-changing effect, ‘3D’ images,
        ‘tilt cards’, printed with tiny lenses
    :cvar B752: Anaglyph images Stereoscopic 3D effect (eg of images) as
        viewed through red/green filters
    :cvar C750: Raised 3D relief Physical 3D relief (eg of a map, globe)
        reflects height of terrain etc
    :cvar D101: Real Video format Proprietary RealNetworks format.
        Includes Real Video packaged within a .rm RealMedia container
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
    :cvar D301: Microsoft XBox Use with Product Form code DB or DI as
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
    :cvar D310: Sony PlayStation 1 Use with Product Form code DB as
        applicable
    :cvar D311: Sony PlayStation 2 Use with Product Form code DB or DI
        as applicable
    :cvar D312: Nintendo Dual Screen Use with Product Form code DE as
        applicable
    :cvar D313: Sony PlayStation 3 Use with Product Form code DB, DI, DO
        or E* as applicable
    :cvar D314: Microsoft Xbox 360 Use with Product Form code DB, DI or
        VN as applicable
    :cvar D315: Nintendo Wii Use with Product Form code DA or E* as
        applicable
    :cvar D316: Sony PlayStation Portable (PSP) Use with Product Form
        code DL or VL as applicable
    :cvar D317: Sony PlayStation 3 Use with Product Form code DB, DI, DO
        or E* as applicable. Deprecated – use D313
    :cvar D318: Sony PlayStation 4 Use with Product Form code DB, DI, DO
        or E* as applicable
    :cvar D319: Sony PlayStation Vita Use with Product Form code DA or
        E* as applicable
    :cvar D320: Microsoft Xbox One Use with Product Form code DB, DI, DO
        or E* as applicable
    :cvar D321: Nintendo Switch Use with Product Form code DE or DB as
        applicable
    :cvar D322: Nintendo Wii U Use with Product Form code DE or DB as
        applicable
    :cvar D323: Sony PlayStation 5 Use with Product Form code DB, DI, DO
        or E* as applicable
    :cvar D324: Microsoft Xbox Series X / S Use with Product Form code
        DB, DI, DO or E* as applicable
    :cvar E100: Other No code allocated for this e-publication format
        yet
    :cvar E101: EPUB The Open Publication Structure / OPS Container
        Format standard of the International Digital Publishing Forum
        (IDPF) [File extension .epub]
    :cvar E102: OEB The Open EBook format of the IDPF, a predecessor of
        the full EPUB format, still (2008) supported as part of the
        latter [File extension .opf]. Includes EPUB format up to and
        including version 2 – but prefer code E101 for EPUB 2, and
        always use code E101 for EPUB 3
    :cvar E103: DOC Microsoft Word binary document format [File
        extension .doc]
    :cvar E104: DOCX Office Open XML / Microsoft Word XML document
        format (ISO/IEC 29500:2008) [File extension .docx]
    :cvar E105: HTML HyperText Mark-up Language [File extension .html,
        .htm]
    :cvar E106: ODF Open Document Format [File extension .odt]
    :cvar E107: PDF Portable Document Format (ISO 32000-1:2008) [File
        extension .pdf]
    :cvar E108: PDF/A PDF archiving format defined by ISO 19005-1:2005
        [File extension .pdf]
    :cvar E109: RTF Rich Text Format [File extension .rtf]
    :cvar E110: SGML Standard Generalized Mark-up Language
    :cvar E111: TCR A compressed text format mainly used on Psion
        handheld devices [File extension .tcr]
    :cvar E112: TXT Text file format [File extension .txt]. Typically
        ASCII or Unicode UTF-8/16
    :cvar E113: XHTML Extensible Hypertext Markup Language [File
        extension .xhtml, .xht, .xml, .html, .htm]
    :cvar E114: zTXT A compressed text format mainly used on Palm
        handheld devices [File extension .pdb – see also E121, E125,
        E130]
    :cvar E115: XPS XML Paper Specification format [File extension .xps]
    :cvar E116: Amazon Kindle A format proprietary to Amazon for use
        with its Kindle reading devices or software readers [File
        extensions .azw, .mobi, .prc etc]. Prefer code E148 for Print
        Replica files
    :cvar E117: BBeB A Sony proprietary format for use with the Sony
        Reader and LIBRIé reading devices [File extension .lrf]
    :cvar E118: DXReader A proprietary format for use with DXReader
        software
    :cvar E119: EBL A format proprietary to the Ebook Library service
    :cvar E120: Ebrary A format proprietary to the Ebrary service
    :cvar E121: eReader A proprietary format for use with eReader (AKA
        ‘Palm Reader’) software on various hardware platforms [File
        extension .pdb – see also E114, E125, E130]
    :cvar E122: Exebook A proprietary format with its own reading system
        for Windows platforms [File extension .exe]
    :cvar E123: Franklin eBookman A proprietary format for use with the
        Franklin eBookman reader
    :cvar E124: Gemstar Rocketbook A proprietary format for use with the
        Gemstar Rocketbook reader [File extension .rb]
    :cvar E125: iSilo A proprietary format for use with iSilo software
        on various hardware platforms [File extension .pdb – see also
        E114, E121, E130]
    :cvar E126: Microsoft Reader A proprietary format for use with
        Microsoft Reader software on Windows and Pocket PC platforms
        [File extension .lit]
    :cvar E127: Mobipocket A proprietary format for use with Mobipocket
        software on various hardware platforms [File extensions .mobi,
        .prc]. Includes Amazon Kindle formats up to and including
        version 7 – but prefer code E116 for version 7, and always use
        E116 for KF8
    :cvar E128: MyiLibrary A format proprietary to the MyiLibrary
        service
    :cvar E129: NetLibrary A format proprietary to the NetLibrary
        service
    :cvar E130: Plucker A proprietary format for use with Plucker reader
        software on Palm and other handheld devices [File extension .pdb
        – see also E114, E121, E125]
    :cvar E131: VitalBook A format proprietary to the VitalSource
        service
    :cvar E132: Vook A proprietary digital product combining text and
        video content and available to be used online or as a
        downloadable application for a mobile device – see www.vook.com
    :cvar E133: Google Edition An epublication made available by Google
        in association with a publisher; readable online on a browser-
        enabled device and offline on designated ebook readers
    :cvar E134: Book ‘app’ for iOS Epublication packaged as application
        for iOS (eg Apple iPhone, iPad etc), containing both executable
        code and content. Use &lt;ProductContentType&gt; to describe
        content, and &lt;ProductFormFeatureType&gt; to list detailed
        technical requirements
    :cvar E135: Book ‘app’ for Android Epublication packaged as
        application for Android (eg Android phone or tablet), containing
        both executable code and content. Use &lt;ProductContentType&gt;
        to describe content, and &lt;ProductFormFeatureType&gt; to list
        detailed technical requirements
    :cvar E136: Book ‘app’ for other operating system Epublication
        packaged as application, containing both executable code and
        content. Use where other ‘app’ codes are not applicable.
        Technical requirements such as target operating system and/or
        device should be provided eg in &lt;ProductFormFeatureType&gt;.
        Content type (text or text plus various ‘enhancements’) may be
        described with &lt;ProductContentType&gt;
    :cvar E139: CEB Founder Apabi’s proprietary basic e-book format
    :cvar E140: CEBX Founder Apabi’s proprietary XML e-book format
    :cvar E141: iBook Apple’s iBook format (a proprietary extension of
        EPUB), can only be read on Apple iOS devices
    :cvar E142: ePIB Proprietary format based on EPUB used by Barnes and
        Noble for fixed-format e-books, readable on NOOK devices and
        Nook reader software
    :cvar E143: SCORM Sharable Content Object Reference Model, standard
        content and packaging format for e-learning objects
    :cvar E144: EBP E-book Plus (proprietary Norwegian e-book format)
    :cvar E145: Page Perfect Proprietary format based on PDF used by
        Barnes and Noble for fixed-format e-books, readable on some NOOK
        devices and Nook reader software
    :cvar E146: BRF (Braille-ready file) Electronic Braille file
    :cvar E147: Erudit Proprietary XML format for articles, see for
        example https://www.cairn.info/services-aux-editeurs.php
    :cvar E148: Amazon Kindle Print Replica A format proprietary to
        Amazon for use with its Kindle reading devices or software
        readers. Essentially a PDF embedded within a KF8 format file
    :cvar E149: Comic Book Archive Format for comic books, consisting
        primarily of sequentially-named PNG or JPEG images in a zip
        container
    :cvar E200: Reflowable Use this and/or code E201 when a particular
        e-publication type (specified using codes E100 and upwards) has
        both fixed format and reflowable variants, to indicate which
        option is included in this product
    :cvar E201: Fixed format Use this and/or code E200 when a particular
        e-publication type (specified using codes E100 and upwards) has
        both fixed format and reflowable variants, to indicate which
        option is included in this product
    :cvar E202: Readable offline All e-publication resources are
        included within the e-publication package
    :cvar E203: Requires network connection E-publication requires a
        network connection to access some resources (eg an enhanced
        e-book where video clips are not stored within the e-publication
        package itself, but are delivered via an internet connection)
    :cvar E204: Content removed Resources (eg images) present in other
        editions have been removed from this product, eg due to rights
        issues
    :cvar E205: Visible page numbering (Mostly fixed-format)
        e-publication contains visible page numbers. Use with List 196
        code 19 if numbering has a print-equivalent
    :cvar E206: No preferred page progression For e-publications only,
        pages may be rendered LTR or RTL (see B606 to B609)
    :cvar E210: Landscape Use for fixed-format e-books optimised for
        landscape display. Also include an indication of the optimal
        screen aspect ratio
    :cvar E211: Portrait Use for fixed-format e-books optimised for
        portrait display. Also include an indication of the optimal
        screen aspect ratio
    :cvar E212: Square Use for fixed-format e-books optimised for a
        square display.
    :cvar E213: Vertical scrolling Use for fixed-format e-publications
        optimised for vertical scrolling display (‘webtoon format’)
    :cvar E221: 5:4 (1.25:1) Use for fixed-format e-books optimised for
        displays with a 5:4 aspect ratio (eg 1280x1024 pixels etc,
        assuming square pixels). Note that aspect ratio codes are NOT
        specific to actual screen dimensions or pixel counts, but to the
        ratios between two dimensions or two pixel counts
    :cvar E222: 4:3 (1.33:1) Use for fixed-format e-books optimised for
        displays with a 4:3 aspect ratio (eg 800x600, 1024x768,
        2048x1536 pixels etc)
    :cvar E223: 3:2 (1.5:1) Use for fixed-format e-books optimised for
        displays with a 3:2 aspect ratio (eg 960x640, 3072x2048 pixels
        etc)
    :cvar E224: 16:10 (1.6:1) Use for fixed-format e-books optimised for
        displays with a 16:10 aspect ratio (eg 1440x900, 2560x1600
        pixels etc)
    :cvar E225: 16:9 (1.77:1) Use for fixed-format e-books optimised for
        displays with a 16:9 aspect ratio (eg 1024x576, 1920x1080,
        2048x1152 pixels etc)
    :cvar E226: 18:9 (2:1) Use for fixed-format e-books optimised for
        displays with an 18:9 aspect ratio (eg 2160x1080, 2880x1440
        pixels etc)
    :cvar E227: 21:9 (2.37:1) Use for fixed-format e-books optimised for
        displays with an 21:9 (or 64:27) aspect ratio (eg 3840x1644
        pixels etc)
    :cvar L101: Laminated Whole product laminated (eg laminated map,
        fold-out chart, wallchart, etc): use B415 for book with
        laminated cover
    :cvar P091: Calendar with write-in space (de: Nutzkalendarium)
        Calendar or diary has spaces intended for entering birthdays,
        appointments, notes etc. Use with other calendar / diary type
        codes
    :cvar P092: Calendar without write-in space (de: Schmuckkalendarium)
        Calendar or diary has no spaces intended for entering birthdays,
        appointments, notes etc. Use with other calendar / diary type
        codes
    :cvar P096: Multiple months per page (de: Mehrmonatskalender)
        Calendar has multiple months (but not whole year) per page or
        view. Use with other calendar / diary type codes when the time
        period per sheet, page or view is not the expected arrangement
    :cvar P097: One month per page (de: Monatskalender) Calendar has one
        month per page or view
    :cvar P098: One week per page (de: Wochenkalender) Calendar has one
        week per page or view
    :cvar P099: One day per page (de: Tageskalender) Calendar has one
        day per page or view
    :cvar P101: Desk calendar or diary Large format, usually one week
        per page or view. Use with Product Form code PC or PF
    :cvar P102: Mini calendar or pocket diary Small format, usually one
        week per page or view. Use with Product Form code PC or PF
    :cvar P103: Engagement calendar or Appointment diary Day planner.
        Usually one day per page or view, with time-of-day subdivisions
        (rather than just days) or adequate space to add them. Use with
        Product Form code PC or PF
    :cvar P104: Day by day calendar Eg tear-off calendars (one day per
        sheet). Use with Product Form code PC
    :cvar P105: Poster calendar Large single-sheet calendar intended for
        hanging. Use with Product Form code PC or PK
    :cvar P106: Wall calendar Large calendar usually intended for
        hanging from the spine, typically one page per view and one
        month per view, with illustrations. See also P134. Use with
        Product Form code PC
    :cvar P107: Perpetual calendar or diary Usually undated. Use with
        Product Form code PC or PF, and can be combined with other
        calendar/diary type codes
    :cvar P108: Advent calendar Use with Product Form code PC, and can
        be combined with other calendar/diary type codes
    :cvar P109: Bookmark calendar Use with Product Form code PC or PT
    :cvar P110: Student or Academic calendar or diary Mid-year diary,
        start and end aligned with the academic year. Use with Product
        Form code PC or PF, and can be combined with other
        calendar/diary type codes
    :cvar P111: Project calendar Use with Product Form code PC
    :cvar P112: Almanac calendar Use with Product Form code PC
    :cvar P113: Other calendar, diary or organiser A calendar, diary or
        organiser that is not one of the types specified elsewhere: use
        with Product Form code PC, PF or PS
    :cvar P114: Other calendar or organiser product A product that is
        associated with or ancillary to a calendar or organiser, eg a
        deskstand for a calendar, or an insert for an organiser: use
        with Product Form code PC or PS
    :cvar P115: Family planner Wall or poster calendar with entries for
        each family member. Use with Product Form code PC or PK
    :cvar P116: Postcard calendar Calendar sheets detachable (usually
        perforated) and intended for mailing as postcards. Use with
        Product Form code PC
    :cvar P131: Blank calendar Wall calendar without illustrations,
        usually one page per month, intended to be used by adding your
        own images (de: Bastelkalender). Use with Product Form code PC
    :cvar P132: Panoramic calendar Very large wall calendar intended for
        hanging, usually one page per month, wide landscape orientation,
        with illustrations. Use with Product Form code PC
    :cvar P133: Columnar calendar Very large wall calendar intended for
        hanging, usually one page per month, narrow portrait
        orientation, with illustrations. Use with Product Form code PC
    :cvar P134: Square calendar (de: Broschurkalender) Wall calendar,
        usually intended for hanging from a page edge, typically two
        pages per view and one month per view, with illustrations. See
        also P106. Use with Product Form code PC
    :cvar P120: Picture story cards Kamishibai / Cantastoria cards
    :cvar P121: Flash cards For use to specify letter, word, image (etc)
        recognition cards for teaching reading or other classroom use.
        Use with Product form code PD
    :cvar P122: Reference cards Quick reference cards, revision cards,
        recipe cards etc. Use with Product form code PD
    :cvar P123: Recreation cards For use to specify cards and card decks
        for gaming, collecting and trading etc. Use also for divination
        cards. Use with Product form codes PD
    :cvar P124: Postcards And postcard packs / books. Use with Product
        form code PJ
    :cvar P125: Greeting cards And greeting card packs. Use with Product
        form code PJ
    :cvar P126: Gift cards Physical cards which carry an intrinsic
        value, or which are intended to have value added to them, that
        may be redeemed later. For example book token cards, gift cards.
        Note value additions and redemption may be in a physical store
        or online
    :cvar P127: Certificate cards Blank certificate, award or achivement
        cards, Use with Product form code PD
    :cvar P201: Hardback (stationery) Stationery item in hardback book
        format
    :cvar P202: Paperback / softback (stationery) Stationery item in
        paperback/softback book format
    :cvar P203: Spiral bound (stationery) Stationery item in spiral-
        bound book format
    :cvar P204: Leather / fine binding (stationery) Stationery item in
        leather-bound book format, or other fine binding
    :cvar P301: With hanging strips For wall map, poster, wallchart etc
    :cvar P305: Single-sided Content is printed single-sided (for
        wallcharts and hanging maps, calendars, etc)
    :cvar P306: Double-sided Content is printed double-sided (for
        wallcharts and hanging maps, calendars, etc, where double-sided
        may not always be expected)
    :cvar V201: PAL SD TV standard for video or DVD
    :cvar V202: NTSC SD TV standard for video or DVD
    :cvar V203: SECAM SD TV standard for video or DVD
    :cvar V205: HD Up to 2K resolution (1920 or 2048 pixels wide) eg for
        Blu-Ray
    :cvar V206: UHD Up to 4K resolution (3840 or 4096 pixels wide) eg
        for Ultra HD Blu-Ray
    :cvar V207: 3D video Eg for Blu-ray 3D
    :cvar V210: Closed captions Or subtitles
    :cvar V211: Open captions ‘Burnt-in’ or hard captions or subtitles
    :cvar V220: Home use Licensed for use in domestic contexts only
    :cvar V221: Classroom use Licensed for use in education
    :cvar Z101: Wooden Primary material composition (eg of kit or puzzle
        pieces, of gameplay tokens or tiles) is wood or has wooden
        pieces/parts
    :cvar Z102: Plastic Plastic or plastic pieces/parts
    :cvar Z103: Board Card or board pieces/parts
    :cvar Z111: 3D puzzle Puzzle assembles into a 3D object
    :cvar Z112: Noisy kit / puzzle / toy Toy makes a noise. See B208 for
        noisy books
    :cvar Z113: Puppet Including finger / hand puppets, marionettes
    :cvar Z121: Extra large pieces Designed and sized for the very
        young, or those with visual impairments, limited motor skills,
        dementia etc
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
    A113 = "A113"
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
    A310 = "A310"
    A311 = "A311"
    A312 = "A312"
    A400 = "A400"
    A401 = "A401"
    A402 = "A402"
    A403 = "A403"
    A404 = "A404"
    A410 = "A410"
    A420 = "A420"
    A421 = "A421"
    A441 = "A441"
    A451 = "A451"
    A471 = "A471"
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
    B132 = "B132"
    B133 = "B133"
    B134 = "B134"
    B135 = "B135"
    B139 = "B139"
    B140 = "B140"
    B141 = "B141"
    B201 = "B201"
    B202 = "B202"
    B204 = "B204"
    B205 = "B205"
    B206 = "B206"
    B207 = "B207"
    B208 = "B208"
    B209 = "B209"
    B210 = "B210"
    B212 = "B212"
    B213 = "B213"
    B214 = "B214"
    B215 = "B215"
    B216 = "B216"
    B221 = "B221"
    B222 = "B222"
    B223 = "B223"
    B224 = "B224"
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
    B316 = "B316"
    B317 = "B317"
    B318 = "B318"
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
    B417 = "B417"
    B420 = "B420"
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
    B515 = "B515"
    B516 = "B516"
    B517 = "B517"
    B518 = "B518"
    B519 = "B519"
    B520 = "B520"
    B521 = "B521"
    B522 = "B522"
    B601 = "B601"
    B602 = "B602"
    B603 = "B603"
    B604 = "B604"
    B605 = "B605"
    B606 = "B606"
    B607 = "B607"
    B608 = "B608"
    B609 = "B609"
    B610 = "B610"
    B611 = "B611"
    B701 = "B701"
    B702 = "B702"
    B703 = "B703"
    B704 = "B704"
    B705 = "B705"
    B706 = "B706"
    B707 = "B707"
    B708 = "B708"
    B709 = "B709"
    B750 = "B750"
    B751 = "B751"
    B752 = "B752"
    C750 = "C750"
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
    D317 = "D317"
    D318 = "D318"
    D319 = "D319"
    D320 = "D320"
    D321 = "D321"
    D322 = "D322"
    D323 = "D323"
    D324 = "D324"
    E100 = "E100"
    E101 = "E101"
    E102 = "E102"
    E103 = "E103"
    E104 = "E104"
    E105 = "E105"
    E106 = "E106"
    E107 = "E107"
    E108 = "E108"
    E109 = "E109"
    E110 = "E110"
    E111 = "E111"
    E112 = "E112"
    E113 = "E113"
    E114 = "E114"
    E115 = "E115"
    E116 = "E116"
    E117 = "E117"
    E118 = "E118"
    E119 = "E119"
    E120 = "E120"
    E121 = "E121"
    E122 = "E122"
    E123 = "E123"
    E124 = "E124"
    E125 = "E125"
    E126 = "E126"
    E127 = "E127"
    E128 = "E128"
    E129 = "E129"
    E130 = "E130"
    E131 = "E131"
    E132 = "E132"
    E133 = "E133"
    E134 = "E134"
    E135 = "E135"
    E136 = "E136"
    E139 = "E139"
    E140 = "E140"
    E141 = "E141"
    E142 = "E142"
    E143 = "E143"
    E144 = "E144"
    E145 = "E145"
    E146 = "E146"
    E147 = "E147"
    E148 = "E148"
    E149 = "E149"
    E200 = "E200"
    E201 = "E201"
    E202 = "E202"
    E203 = "E203"
    E204 = "E204"
    E205 = "E205"
    E206 = "E206"
    E210 = "E210"
    E211 = "E211"
    E212 = "E212"
    E213 = "E213"
    E221 = "E221"
    E222 = "E222"
    E223 = "E223"
    E224 = "E224"
    E225 = "E225"
    E226 = "E226"
    E227 = "E227"
    L101 = "L101"
    P091 = "P091"
    P092 = "P092"
    P096 = "P096"
    P097 = "P097"
    P098 = "P098"
    P099 = "P099"
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
    P115 = "P115"
    P116 = "P116"
    P131 = "P131"
    P132 = "P132"
    P133 = "P133"
    P134 = "P134"
    P120 = "P120"
    P121 = "P121"
    P122 = "P122"
    P123 = "P123"
    P124 = "P124"
    P125 = "P125"
    P126 = "P126"
    P127 = "P127"
    P201 = "P201"
    P202 = "P202"
    P203 = "P203"
    P204 = "P204"
    P301 = "P301"
    P305 = "P305"
    P306 = "P306"
    V201 = "V201"
    V202 = "V202"
    V203 = "V203"
    V205 = "V205"
    V206 = "V206"
    V207 = "V207"
    V210 = "V210"
    V211 = "V211"
    V220 = "V220"
    V221 = "V221"
    Z101 = "Z101"
    Z102 = "Z102"
    Z103 = "Z103"
    Z111 = "Z111"
    Z112 = "Z112"
    Z113 = "Z113"
    Z121 = "Z121"


class List177(Enum):
    """
    Person / organization date role.

    :cvar VALUE_50: Date of birth
    :cvar VALUE_51: Date of death
    :cvar VALUE_56: Flourished around (‘Floruit’). To date the height of
        or most productive period during a career
    """

    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_56 = "56"


class List179(Enum):
    """
    Price code type.

    :cvar VALUE_01: Proprietary A publisher or retailer’s proprietary
        code list as specified in &lt;PriceCodeTypeName&gt; which
        identifies particular codes with particular price points, price
        tiers or bands
    :cvar VALUE_02: Finnish Pocket Book price code Price Code scheme for
        Finnish Pocket Books (Pokkareiden hintaryhmä). Price codes
        expressed as letters A–J in &lt;PriceCode&gt;
    :cvar VALUE_03: Finnish Miki Book price code Price Code scheme for
        Finnish Miki Books (Miki-kirjojen hintaryhmä). Price codes
        expressed as an integer 1–n in &lt;PriceCode&gt;
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"


class List18(Enum):
    """
    Person / organization name type.

    :cvar VALUE_00: Unspecified Usually the name as it is presented on
        the book
    :cvar VALUE_01: Pseudonym May be used to give a well-known
        pseudonym, where the primary name is a ‘real’ name
    :cvar VALUE_02: Authority-controlled name
    :cvar VALUE_03: Earlier name Use only within &lt;AlternativeName&gt;
    :cvar VALUE_04: ‘Real’ name May be used to identify a well-known
        real name, where the primary name is a pseudonym
    :cvar VALUE_05: Transliterated / translated form of primary name Use
        only within &lt;AlternativeName&gt;, when the primary name type
        is unspecified, for names in a different script or language
    :cvar VALUE_06: Later name Use only within &lt;AlternativeName&gt;
    :cvar VALUE_07: Fictional character name Use only within
        &lt;NameAsSubject&gt; to indicate the subject is fictional, or
        in &lt;AlternativeName&gt; alongside &lt;UnnamedPersons&gt; to
        indicate a human-like name for a synthetic voice or AI. Only for
        use in ONIX 3.0 or later
    """

    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"


class List19(Enum):
    """
    Unnamed person(s)

    :cvar VALUE_01: Unknown
    :cvar VALUE_02: Anonymous Note that Anonymous can be interpreted as
        singular or plural. A real name can be provided using
        &lt;AlternativeName&gt; where it is generally known
    :cvar VALUE_03: et al And others. Use when some but not all
        contributors are listed
    :cvar VALUE_04: Various When there are multiple contributors, and
        none are listed individually. Use for example when the product
        is a pack of books by different authors
    :cvar VALUE_05: Synthesised voice – male Use with Contributor role
        code E07 ‘read by’, eg for audio books with digital narration
    :cvar VALUE_06: Synthesised voice – female Use with Contributor role
        code E07 ‘read by’, eg for audio books with digital narration
    :cvar VALUE_07: Synthesised voice – unspecified Use with Contributor
        role code E07 ‘read by’, eg for audio books with digital
        narration
    :cvar VALUE_08: Synthesised voice – based on real voice actor Use
        with Contributor role code E07 ‘read by’, eg for audio books
        with digital narration, and provide name of voice actor in
        &lt;AlternativeName&gt;. Only for use in ONIX 3.0 or later
    :cvar VALUE_09: AI (Artificial intelligence) Use when the creator
        (of text, of images etc) is a generative AI model or technique.
        Note, can also be combined with the role ‘assisted by’. Only for
        use in ONIX 3.0 or later
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


class List197(Enum):
    """
    Collection sequence type.

    :cvar VALUE_01: Proprietary A short explanatory label for the
        sequence should be provided in
        &lt;CollectionSequenceTypeName&gt;
    :cvar VALUE_02: Title order Order as specified by the title, eg by
        volume or part number sequence, provided for confirmation
    :cvar VALUE_03: Publication order Order of publication of products
        within the collection
    :cvar VALUE_04: Temporal/narrative order Order defined by a
        continuing narrative or temporal sequence within products in the
        collection. Applicable to either fiction or to non-fiction (eg
        within a collection of history textbooks)
    :cvar VALUE_05: Original publication order Original publication
        order, for a republished collection or collected works
        originally published outside a collection
    :cvar VALUE_06: Suggested reading order Where it is different from
        the title order, publication order, narrative order etc
    :cvar VALUE_07: Suggested display order Where it is different from
        the title order, publication order, narrative order, reading
        order etc
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"


class List198(Enum):
    """
    Product contact role.

    :cvar VALUE_00: Metadata contact For queries and feedback concerning
        the metadata record itself
    :cvar VALUE_01: Accessibility request contact Eg for requests for
        supply of mutable digital files for conversion to other formats
    :cvar VALUE_02: Promotional contact Eg for requests relating to
        interviews, author events
    :cvar VALUE_03: Advertising contact Eg for co-op advertising
    :cvar VALUE_04: Review copy contact Eg for requests for review
        copies
    :cvar VALUE_05: Evaluation copy contact Eg for requests for approval
        or evaluation copies (particularly within education)
    :cvar VALUE_06: Permissions contact Eg for requests to reproduce or
        repurpose parts of the publication
    :cvar VALUE_07: Return authorisation contact Eg for use where
        authorisation must be gained from the publisher rather than the
        distributor or wholesaler
    :cvar VALUE_08: CIP / Legal deposit contact Eg for legal deposit or
        long-term preservation
    :cvar VALUE_09: Rights and licensing contact Eg for subrights
        licensing, collective licensing
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


class List2(Enum):
    """
    Product composition.

    :cvar VALUE_00: Single-component retail product
    :cvar VALUE_01: Single-component, not available separately Used only
        when an ONIX record is required for a component-as-an-item, even
        though it is not currently available as such
    :cvar VALUE_10: Multiple-component retail product Multiple-component
        product retailed as a whole
    :cvar VALUE_11: Multiple-item collection, retailed as separate parts
        Used only when an ONIX record is required for a collection-as-a-
        whole, even though it is not currently retailed as such
    :cvar VALUE_20: Trade-only product Product available to the book
        trade, but not for retail sale, and not carrying retail items,
        eg empty dumpbin, empty counterpack, promotional material
    :cvar VALUE_30: Multiple-item trade-only pack Product available to
        the book trade, but not for general retail sale as a whole. It
        carries multiple components for retailing as separate items, eg
        shrink-wrapped trade pack, filled dumpbin, filled counterpack
    :cvar VALUE_31: Multiple-item pack Carrying multiple components,
        primarily for retailing as separate items. The pack may be split
        and retailed as separate items OR retailed as a single item. Use
        instead of Multiple-item trade-only pack (code 30) if the data
        provider specifically wishes to make explicit that the pack may
        optionally be retailed as a whole
    """

    VALUE_00 = "00"
    VALUE_01 = "01"
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
    Edition type.

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
    :cvar ALT: Alternate Do not use. Deprecated, but retained in the
        list for reasons of backwards compatibility. Not for use in ONIX
        3.0 or later
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
    :cvar BUD: Budget edition Product sold at lower price than other
        editions, usually with lower quality paper or binding to reduce
        production costs. Only for use in ONIX 3.0 or later
    :cvar CMB: Combined volume An edition in which two or more works
        also published separately are combined in a single volume; AKA
        ‘omnibus edition’, or in comic books a ‘trade paperback’ (fr:
        ‘intégrale’)
    :cvar CRI: Critical edition Content includes critical commentary on
        the text
    :cvar CSP: Coursepack Content was compiled for a specified
        educational course
    :cvar DGO: Digital original A digital product that, at the time of
        publication, has or had no physical counterpart and that is or
        was not expected to have a physical counterpart for a reasonable
        time (recommended at least 30 days following publication)
    :cvar ENH: Enhanced edition Use for e-publications that have been
        enhanced with additional text, speech, other audio, video,
        interactive or other content
    :cvar ENL: Enlarged edition Content has been enlarged or expanded
        from that of a previous edition
    :cvar ETR: Easy-to-read edition Book which uses highly simplified
        wording, clear page layout and typography to ensure the content
        can be understood by those with intellectual disabilities. See
        https://www.inclusion-europe.eu/easy-to-read for guidelines. See
        also SMP for editions with simplified language. Only for use in
        ONIX 3.0 or later
    :cvar EXP: Expurgated edition ‘Offensive’ content has been removed
    :cvar FAC: Facsimile edition Exact reproduction of the content and
        format of a previous edition
    :cvar FST: Festschrift A collection of writings published in honor
        of a person, an institution or a society
    :cvar HRE: High readability edition Edition optimised for high
        readability, typically featuring colored or tinted page
        backgrounds to reduce contrast, extra letter, word and line
        spacing to reduce crowding and isolate individual words,
        simplified page layouts and an open, sans serif font (or
        occasionally, an unusual font design) intended to aid
        readability. Sometimes labelled ‘dyslexia-friendly’. See also
        code SMP if the text itself is simplified, and codes LTE or ULP
        if the type size is significantly larger than normal. Only for
        use in ONIX 3.0 or later
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
        other coded type or edition numbering is applicable
    :cvar NUM: Edition with numbered copies A limited or collectors’
        edition in which each copy is individually numbered, and the
        actual number of copies is strictly limited. Note that the
        supplier may limit the number of orders fulfilled per retail
        outlet. Use &lt;EditionStatement&gt; to give details of the
        number of copies printed
    :cvar PBO: Paperback original A product published in any form of
        soft cover, that at the time of publication, has or had no
        counterpart in any other format, and that is or was not expected
        to have such a counterpart for a reasonable time (recommended at
        least 30 days following publication). Only for use in ONIX 3.0
        or later
    :cvar PRB: Prebound edition In the US, a book that was previously
        bound, normally as a paperback, and has been rebound with a
        library-quality hardcover binding by a supplier other than the
        original publisher. See also the &lt;Publisher&gt; and
        &lt;RelatedProduct&gt; composites for other aspects of the
        treatment of prebound editions in ONIX
    :cvar REV: Revised edition Content has been revised from that of a
        previous edition (often used when there has been no
        corresponding increment in the edition number, or no edition
        numbering is available)
    :cvar SCH: School edition An edition intended specifically for use
        in schools
    :cvar SIG: Signed edition Individually autographed by the author(s)
    :cvar SMP: Simplified language edition An edition that uses
        simplified language, usually for second or additional language
        learners. See ETR for highly simplified editions for readers
        with intellectual disabilities
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
    :cvar UNN: Edition with unnumbered copies A limited or collectors’
        edition in which each copy is not individually numbered – but
        where the actual number of copies is strictly limited. Note that
        the supplier may limit the number of orders fulfilled per retail
        outlet. Use &lt;EditionStatement&gt; to give details of the
        number of copies printed
    :cvar UXP: Unexpurgated edition Content previously considered
        ‘offensive’ has been restored
    :cvar VAR: Variorum edition Content includes notes by various
        commentators, and/or includes and compares several variant texts
        of the same work
    :cvar VOR: Vorlesebücher Readaloud edition – specifially intended
        and designed for reading aloud (to children). Only for use in
        ONIX 3.0 or later
    """

    ABR = "ABR"
    ACT = "ACT"
    ADP = "ADP"
    ALT = "ALT"
    ANN = "ANN"
    BLL = "BLL"
    BLP = "BLP"
    BRL = "BRL"
    BUD = "BUD"
    CMB = "CMB"
    CRI = "CRI"
    CSP = "CSP"
    DGO = "DGO"
    ENH = "ENH"
    ENL = "ENL"
    ETR = "ETR"
    EXP = "EXP"
    FAC = "FAC"
    FST = "FST"
    HRE = "HRE"
    ILL = "ILL"
    INT = "INT"
    LTE = "LTE"
    MCP = "MCP"
    MDT = "MDT"
    MLL = "MLL"
    NED = "NED"
    NUM = "NUM"
    PBO = "PBO"
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
    VOR = "VOR"


class List215(Enum):
    """
    Proximity.

    :cvar VALUE_01: Less than
    :cvar VALUE_02: Not more than
    :cvar VALUE_03: Exactly The supplier’s true figure, or at least a
        best estimate expected to be within 10% of the true figure (ie a
        quoted figure of 100 could in fact be anything between 91 and
        111)
    :cvar VALUE_04: Approximately Generally interpreted as within 25% of
        the true figure (ie a quoted figure of 100 could in fact be
        anything between 80 and 133). The supplier may introduce a
        deliberate approximation to reduce the commercial sensitivity of
        the figure
    :cvar VALUE_05: About Generally interpreted as within a factor of
        two of the true figure (ie a quoted figure of 100 could in fact
        be anything between 50 and 200). The supplier may introduce a
        deliberate approximation to reduce the commercial sensitivity of
        the figure
    :cvar VALUE_06: Not less than
    :cvar VALUE_07: More than
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"


class List216(Enum):
    """
    Velocity metric.

    :cvar VALUE_01: Mean daily sale Typically measured over most recent
        1 month period
    :cvar VALUE_02: Maximum daily sale Typically measured over most
        recent 1 month period
    :cvar VALUE_03: Minimum daily sale Typically measured over most
        recent 1 month period
    :cvar VALUE_04: Mean weekly sale Typically measured over most recent
        rolling 12 week period
    :cvar VALUE_05: Maximum weekly sale Typically measured over most
        recent rolling 12 week period
    :cvar VALUE_06: Minimum weekly sale Typically measured over most
        recent rolling 12 week period
    :cvar VALUE_07: Mean monthly sale Typically measured over most
        recent rolling 6 month period
    :cvar VALUE_08: Maximum monthly sale Typically measured over the
        most recent rolling 6 month period
    :cvar VALUE_09: Minimum monthly sale Typically measured over the
        most recent rolling 6 month period
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


class List217(Enum):
    """
    Price identifier type.

    :cvar VALUE_01: Proprietary Note that &lt;IDTypeName&gt; is required
        for proprietary identifiers
    :cvar VALUE_02: Proprietary price point identifier Proprietary
        identifier uniquely identifies price amount and currency. Two
        unrelated products with the same price amount carry the same
        identifier, though their price types may be different
    :cvar VALUE_03: Proprietary price type identifier Proprietary
        identifier uniquely identifies price type, qualifier and any
        constraints and conditions. Two unrelated products with the same
        price type carry the same identifier, though their price points
        may be different
    :cvar VALUE_04: Proprietary price point and type identifier
        Proprietary identifier identifies a unique combination of price
        point and type, though two unrelated products may carry the same
        identifier if all details of their prices are identical
    :cvar VALUE_05: Proprietary unique price identifier Proprietary
        identifier is unique to a single price point, price type and
        product. No two products can carry the same identifier, even if
        all details of their prices are identical
    :cvar VALUE_06: Proprietary product price point identifier
        Proprietary identifier uniquely identifies a specific
        combination of product, price amount and currency, independent
        of the price type
    :cvar VALUE_07: Proprietary product price type identifier
        Proprietary identifier uniquely identifies a specific
        combination of product, price type, qualifier and any
        constraints and conditions, independent of the price amount and
        currency. A product with the same product price type identififer
        may carry differing price amounts, currencies at different
        points in time
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"


class List218(Enum):
    """
    License expression type.

    :cvar VALUE_01: Human readable Document (eg Word file, PDF or web
        page) Intended for the lay reader
    :cvar VALUE_02: Professional readable Document (eg Word file, PDF or
        web page) Intended for the legal specialist reader
    :cvar VALUE_10: ONIX-PL
    :cvar VALUE_20: ODRL Open Digital Rights Language (ODRL) in JSON-LD
        format. Used for example to express TDM licenses using the W3C
        TDM Reservation Protocol
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_10 = "10"
    VALUE_20 = "20"


class List219(Enum):
    """
    Rights type.

    :cvar C: Copyright Text or image copyright (normally indicated by
        the © symbol). The default if no &lt;CopyrightType&gt; is
        specified
    :cvar P: Phonogram right Phonogram copyright or neighbouring right
        (normally indicated by the ℗ symbol)
    :cvar D: Database right Sui generis database right
    """

    C = "C"
    P = "P"
    D = "D"


class List22(Enum):
    """
    Language role.

    :cvar VALUE_01: Language of text
    :cvar VALUE_02: Original language of a translated text Where the
        text in the original language is NOT part of the current product
    :cvar VALUE_03: Language of abstracts Where different from language
        of text: used mainly for serials
    :cvar VALUE_06: Original language in a multilingual edition Where
        the text in the original language is part of a bilingual or
        multilingual product
    :cvar VALUE_07: Translated language in a multilingual edition Where
        the text in a translated language is part of a bilingual or
        multilingual product
    :cvar VALUE_08: Language of audio track For example, on an audiobook
        or video product. Use for the only available audio track, or
        where there are multiple tracks (eg on a DVD), for an alternate
        language audio track that is NOT the original. (In the latter
        case, use code 11 for the original language audio if it is
        included in the product, or code 10 to identify an original
        language that is not present in the product)
    :cvar VALUE_09: Language of subtitles For example, on a DVD
    :cvar VALUE_10: Language of original audio track Where the audio in
        the original language is NOT part of the current product
    :cvar VALUE_11: Original language audio track in a multilingual
        product Where the audio in the original language is part of a
        multilingual product with multiple audio tracks
    :cvar VALUE_12: Language of notes Use for the language of footnotes,
        endnotes, annotations or commentary, instructions or guidance
        for use etc, where it is different from the language of the main
        text
    :cvar VALUE_13: Language of introduction / end matter Use for the
        language of any introductory text, prologue, etc, or epilogue,
        end matter, etc, where it is different from the language of the
        main text. Only for use in ONIX 3.0 or later
    :cvar VALUE_14: Target language of teaching / learning Eg for the
        book ‘Ingles para latinos’, English. For phrasebooks and
        language teaching, learning or study material. Wherever
        possible, the language should also be listed as the subject of
        the book. Only for use in ONIX 3.0 or later
    :cvar VALUE_15: Additional vocabulary / text in this language Use of
        significant words, phrases, quotations or short passages from a
        language other than the main language of the text, as an
        integral part of the text. This does not include ‘loanwords’,
        academic Latin, etc. Only for use in ONIX 3.0 or later
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
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


class List228(Enum):
    """
    Grant identifier type.

    :cvar VALUE_01: Proprietary Note that &lt;IDTypeName&gt; is required
        with proprietary identifiers
    :cvar VALUE_06: DOI Digital Object Identifier (variable length and
        character set, beginning ‘10.’ and without https://doi.org/ or
        the older http://dx.doi.org/)
    """

    VALUE_01 = "01"
    VALUE_06 = "06"


class List23(Enum):
    """
    Extent type.

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
    :cvar VALUE_02: Total text length Number of words or characters of
        natural language text
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
        number of pages (equivalent to the Content page count, code 11)
        in the print counterpart of a digital product delivered without
        fixed pagination, or of an audio product
    :cvar VALUE_09: Duration Total duration in time, expressed in the
        specified extent unit. This is the ‘running time’ equivalent of
        code 11
    :cvar VALUE_10: Notional number of pages in digital product An
        estimate of the number of ‘pages’ in a digital product delivered
        without fixed pagination, and with no print counterpart, given
        as an indication of the size of the work. Equivalent to code 08,
        but exclusively for digital or audio products
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
        any significant amount of running time represented by a musical
        intro, announcements, titles, introduction or other material
        prefacing the main content
    :cvar VALUE_14: Duration of main content Duration in time, expressed
        in the specified extent units, of the main content. This is the
        ‘running time’ equivalent of code 00, and excludes time
        represented by announcements, titles, introduction or other
        prefatory material or ‘back matter’
    :cvar VALUE_15: Duration of back matter Duration in time, expressed
        in the specified extent units, of any content that follows the
        main content of a book. This may consist of an afterword,
        appendices, endnotes, end music etc. It excludes extracts or
        ‘teaser’ material from other works. This is the ‘running time’
        equivalent of code 04
    :cvar VALUE_16: Production duration Duration in time, expressed in
        the specified extent units, of the complete content of a book.
        This is the ‘running time’ equivalent of code 06, and includes
        time represented by musical themes, announcements, titles,
        introductory and other prefatory material, plus ‘back matter’
        such as any afterword, appendices, plus any extracts or ‘teaser’
        material from other works
    :cvar VALUE_17: Number of cards In a pack of educational flash
        cards, playing cards, postcards, greeting cards etc. Only for
        use in ONIX 3.0 or later
    :cvar VALUE_18: Number of write-in pages Count of the number of
        pages within the main content page count that are blank or
        substantially blank, intended for the reader to fill in (eg in a
        journal). Only for use in ONIX 3.0 or later
    :cvar VALUE_22: Filesize Approximate size of a digital file or
        package (in the form it is downloaded), expressed in the
        specified extent unit
    :cvar VALUE_23: Storage filesize Approximate size of storage space
        required for a digital file or package in the form in which it
        is usually stored for use on a device, where this is different
        from the download filesize (see code 22), and expressed in the
        specified extent unit. Only for use in ONIX 3.0 or later
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
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_22 = "22"
    VALUE_23 = "23"


class List230(Enum):
    """
    Price constraint type.

    :cvar VALUE_00: No price-specific constraints Allows positive
        indication that there are no additional constraints (other than
        those specified in &lt;EpubUsageConstraint&gt;). By convention,
        use 01 in &lt;PriceConstraintStatus&gt;
    :cvar VALUE_01: Preview Preview before purchase. Allows a retail
        customer, account holder or patron to view or listen to a
        proportion of the book before purchase. Also applies to
        borrowers making use of ‘acquisition on demand’ models in
        libraries, and to ‘subscription’ models where the purchase is
        made on behalf of the reader. Generally used to specify
        different preview percentages across different customer types
    :cvar VALUE_06: Lend Lendable by the purchaser to other device
        owner, account holder or patron, eg library lending (use where
        the library product is not identified with a separate
        &lt;ProductIdentifier&gt; from the consumer product). The
        ‘primary’ copy becomes unusable while the secondary copy is on
        loan, unless a number of concurrent borrowers is also specified
    :cvar VALUE_07: Time-limited license E-publication license is time-
        limited. Use with code 02 from List 146 and either a time period
        in days, weeks or months in &lt;PriceConstraintLimit&gt;, or a
        Valid until date in &lt;PriceConstraintLimit&gt;. The purchased
        copy becomes unusable when the license expires. For clarity, a
        perpetual license is the default, but may be specified
        explicitly with code 01 from list 146, or with code 02 and a
        limit &lt;Quantity&gt; of 0 days
    :cvar VALUE_08: Loan renewal Maximum number of consecutive loans or
        loan extensions (eg from a library) to a single device owner,
        account holder or patron. Note that a limit of 1 indicates that
        a loan cannot be renewed or extended
    :cvar VALUE_09: Multi-user license E-publication license is multi-
        user. Maximum number of concurrent users licensed to use the
        product should be given in &lt;PriceConstraintLimit&gt;. For
        clarity, unlimited concurrencyis the default, but may be
        specified explicitly with code 01 from list 146, or with code 02
        and a limit &lt;Quantity&gt; of 0 users
    :cvar VALUE_10: Preview on premises Preview locally before purchase.
        Allows a retail customer, account holder or patron to view a
        proportion of the book (or the whole book, if no proportion is
        specified) before purchase, but ONLY while located physically in
        the retailer’s store (eg while logged on to the store wifi).
        Also applies to borrowers making use of ‘acquisition on demand’
        models in libraries
    """

    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"


class List239(Enum):
    """
    Supply contact role.

    :cvar VALUE_07: Return authorisation contact Eg for use where
        authorisation must be gained from the supplier (distributor or
        wholesaler)
    :cvar VALUE_99: Customer services contact For general enquiries
    """

    VALUE_07 = "07"
    VALUE_99 = "99"


class List24(Enum):
    """
    Extent unit.

    :cvar VALUE_00: Physical pieces Unbound sheets or leaves, where
        ‘pages’ is not appropriate. For example a count of the
        individual number of cards in a pack. Only for use in ONIX 3.0
        or later. For number of pieces in eg a jigsaw, kit, board game,
        see &lt;ProductFormFeature&gt; and code 22 from list 79
    :cvar VALUE_01: Characters Approximate number of characters
        (including spaces) of natural language text. Only for use in
        ONIX 3.0 or later
    :cvar VALUE_02: Words Approximate number of words of natural
        language text
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
    :cvar VALUE_12: Discs Of an audiobook on multiple Red Book audio
        CDs. Conventionally, each disc is 60–70 minutes of running time,
        and disc counts are misleading and inappropriate if the average
        disc duration is significantly more or less than this (for
        example if the discs are Yellow Book CDs containing mp3 files).
        Note that disc breaks are not necessarily aligned with
        structural breaks in the text (eg chapter breaks). Only for use
        in ONIX 3.0 or later
    :cvar VALUE_14: Hours HHH Fill with leading zeroes if any elements
        are missing
    :cvar VALUE_15: Hours and minutes HHHMM Fill with leading zeroes if
        any elements are missing
    :cvar VALUE_16: Hours minutes seconds HHHMMSS Fill with leading
        zeroes if any elements are missing. If centisecond precision is
        required, use HHHMMSScc. Only for use in ONIX 3.0 or later
    :cvar VALUE_17: Bytes
    :cvar VALUE_18: Kbytes
    :cvar VALUE_19: Mbytes
    :cvar VALUE_31: Chapters Number of chapters (or other similar
        subdivisions) of the content. Only for use in ONIX 3.0 or later
    """

    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_31 = "31"


class List240(Enum):
    """
    AV Item type code.

    :cvar VALUE_01: Audiovisual work A complete audiovisual work which
        is published as a content item in a product which carries two or
        more such works, eg when two or three AV works are published in
        a single omnibus package
    :cvar VALUE_02: Front matter Audiovisual components such as a scene
        index or introduction which appear before the main content of
        the product
    :cvar VALUE_03: Body matter Audiovisual components such as scenes or
        ‘chapters’ which appear as part of the main body of the AV
        material in the product
    :cvar VALUE_04: End matter Audiovisual components such as
        advertising which appear after the main content of the product
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"


class List241(Enum):
    """
    AV Item Identifier type.

    :cvar VALUE_01: Proprietary For example, a publisher’s own
        identifier. Note that &lt;IDTypeName&gt; is required with
        proprietary identifiers
    :cvar VALUE_03: GTIN-13 Formerly known as the EAN-13 (unhyphenated)
    :cvar VALUE_06: DOI Digital Object Identifier (variable length and
        character set, beginning ‘10.’ and without https://doi.org/ or
        the older http://dx.doi.org/)
    :cvar VALUE_12: IMDB Motion picture work identifier from the
        International Movie Database
    :cvar VALUE_18: ISRC International Standard Recording Code, 5
        alphanumeric characters plus 7 digits
    :cvar VALUE_19: ISAN International Standard Audiovisual Number (17
        or 26 characters – 16 or 24 hexadecimal digits, plus one or two
        alphanumeric check characters, and without spaces or hyphens)
    :cvar VALUE_31: EIDR DOI Entertainment Identifier Registry DOI
    """

    VALUE_01 = "01"
    VALUE_03 = "03"
    VALUE_06 = "06"
    VALUE_12 = "12"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_31 = "31"


class List244(Enum):
    """
    Event identifier type.

    :cvar VALUE_01: Proprietary
    """

    VALUE_01 = "01"


class List245(Enum):
    """
    Event type.

    :cvar VALUE_00: Unspecified – see description
    :cvar VALUE_01: Book signing
    :cvar VALUE_02: Book reading
    """

    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"


class List246(Enum):
    """
    Event status.

    :cvar A: Announced
    :cvar C: Cancelled Abandoned after having previously been announced
    """

    A = "A"
    C = "C"


class List247(Enum):
    """
    Event occurrence date role.

    :cvar VALUE_01: Date of occurrence Date and (with the default
        dateformat) time the event occurrence begins
    :cvar VALUE_02: Date of occurrence end Date and (with the default
        dateformat) time the event occurrence ends
    """

    VALUE_01 = "01"
    VALUE_02 = "02"


class List248(Enum):
    """
    Specification detail code.

    :cvar A411: 22.05kHz
    :cvar A412: 44.1kHz 44,100 samples per channel per second (CD
        quality)
    :cvar A413: 48kHz
    :cvar A416: 16-bits per sample Bit depth, 16 bits per sample (CD-
        quality)
    :cvar A418: 24-bits per sample
    :cvar A424: ID3v1 Includes v1.1
    :cvar A425: ID3v2
    :cvar B001: Printed long grain Grain of paper parallel to spine
    :cvar B002: Printed short grain Grain of paper perpendicular to
        spine
    :cvar B003: Monochrome Usually B/W
    :cvar B004: Printed CMYK
    :cvar B005: Printed higher-quality CMYK Printed ‘premium’ or high-
        fidelity / high resolution CMYK (where different from ‘Printed
        CMYK’, and the manufacturer offers two quality settings)
    :cvar B006: Printed with bleed At least some content bleeds to or
        beyond trimmed page edge
    """

    A411 = "A411"
    A412 = "A412"
    A413 = "A413"
    A416 = "A416"
    A418 = "A418"
    A424 = "A424"
    A425 = "A425"
    B001 = "B001"
    B002 = "B002"
    B003 = "B003"
    B004 = "B004"
    B005 = "B005"
    B006 = "B006"


class List249(Enum):
    """
    Specification feature type.

    :cvar VALUE_04: Filename Specification Feature Value carries the
        filename of the final product
    :cvar VALUE_21: Audio loudness Specification Feature Value is the
        target loudness in LKFS (LUFS) used for audio normalisation –
        see ITU-R BS.1770
    :cvar VALUE_41: Paper type Specification Feature Description is the
        paper or card type, eg Coated, uncoated
    :cvar VALUE_42: Paper weight Specification Feature Value is the
        paper or card weight in GSM
    :cvar VALUE_43: Paper color Specification Feature Value is the paper
        or card color code selected from List 257
    :cvar VALUE_44: Ink color(s) Specification Feature Description lists
        the ink color(s) required. Do not use if mono or conventional
        CMYK
    :cvar VALUE_45: Special finish Specification Feature Value lists a
        special finish required, from List 258
    """

    VALUE_04 = "04"
    VALUE_21 = "21"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"
    VALUE_45 = "45"


class List25(Enum):
    """
    Illustration and other content type.

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
    :cvar VALUE_30: Table of contents Only for use in ONIX 3.0 or later
    :cvar VALUE_31: Gazetteer Geographical index. Only for use in ONIX
        3.0 or later
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


class List250(Enum):
    """
    Resource identifier type.

    :cvar VALUE_01: Proprietary For example, a publisher’s internal
        digital asset ID. Note that &lt;IDTypeName&gt; is required with
        proprietary identifiers
    :cvar VALUE_09: ISCC International Standard Content Code, a
        ‘similarity hash’ derived algorithmically from the resource
        content itself (see https://iscc.codes). &lt;IDValue&gt; is the
        ISCC-CODE generated from a digital manifestation of the work, as
        a variable-length case-insensitive alphanumeric string (or 55
        characters including three hyphens if using ISCC v1.0, but this
        is deprecated). Note alphabetic characters in v1.x ISCCs use
        Base32 encoding and are conventionally upper case. The ‘ISCC:’
        prefix is omitted
    """

    VALUE_01 = "01"
    VALUE_09 = "09"


class List252(Enum):
    """
    Resource file detail code.

    :cvar A410: Mono Includes ‘stereo’ where channels are identical
    :cvar A411: 22.05kHz
    :cvar A412: 44.1kHz 44,100 samples per channel per second (CD-
        quality)
    :cvar A413: 48kHz
    :cvar A414: 88.2kHz
    :cvar A415: 96kHz
    :cvar A416: 16-bits per sample Bit depth, 16 bits per sample (CD-
        quality)
    :cvar A417: 20-bits per sample
    :cvar A418: 24-bits per sample
    :cvar A419: 32-bits per sample (FP)
    :cvar A420: Stereo Includes ‘joint stereo’
    :cvar A421: Stereo 2.1
    :cvar A422: ID3v1 Includes v1.1
    :cvar A423: ID3v2
    :cvar A441: Surround 4.1 Five-channel audio (including low-frequency
        channel)
    :cvar A451: Surround 5.1 Six-channel audio (including low-frequency
        channel)
    :cvar B001: With crop marks
    :cvar B002: Without crop marks If page size of the resource file is
        not equal to final trimmed page size of the product (in
        &lt;Measure&gt;, then text or image area should be centred on
        final pages. Note that content may not bleed to the trimmed page
        edge
    :cvar B003: Monochrome
    :cvar B004: Preseparated – 2 channels Two pages in the resource file
        represent a single page in the product
    :cvar B005: Preseparated – 3 channels
    :cvar B006: Preseparated – 4 channels For example, preseparated CMYK
    :cvar B010: Composite (CMYK)
    :cvar B011: Composite (RGB)
    """

    A410 = "A410"
    A411 = "A411"
    A412 = "A412"
    A413 = "A413"
    A414 = "A414"
    A415 = "A415"
    A416 = "A416"
    A417 = "A417"
    A418 = "A418"
    A419 = "A419"
    A420 = "A420"
    A421 = "A421"
    A422 = "A422"
    A423 = "A423"
    A441 = "A441"
    A451 = "A451"
    B001 = "B001"
    B002 = "B002"
    B003 = "B003"
    B004 = "B004"
    B005 = "B005"
    B006 = "B006"
    B010 = "B010"
    B011 = "B011"


class List253(Enum):
    """
    Resource file feature type.

    :cvar VALUE_01: File format Resource File Feature Value carries a
        code from List 178
    :cvar VALUE_04: Filename Resource File Feature Value carries the
        filename of the supporting resource, necessary only when it is
        different from the last part of the path provided in
        &lt;ResourceFileLink&gt;
    :cvar VALUE_05: Approximate download file size in megabytes Resource
        File Feature Value carries a decimal number only, suggested no
        more than 2 or 3 significant digits (eg 1.7, not 1.7462 or
        1.75MB)
    :cvar VALUE_06: MD5 hash value MD5 hash value of the resource file.
        &lt;ResourceFileFeatureValue&gt; should contain the 128-bit
        digest value (as 32 hexadecimal digits). Can be used as a
        cryptographic check on the integrity of a resource after it has
        been retrieved
    :cvar VALUE_07: Exact download file size in bytes Resource File
        Feature Value carries a integer number only (eg 1831023)
    :cvar VALUE_08: SHA-256 hash value SHA-256 hash value of the
        resource file. &lt;ResourceFileFeatureValue&gt; should contain
        the 256-bit digest value (as 64 hexadecimal digits). Can be used
        as a cryptographic check on the integrity of a resource after it
        has been retrieved
    :cvar VALUE_31: Audio loudness Resource File Feature Value is the
        loudness in LKFS (LUFS) used for audio normalisation – see ITU-R
        BS.1770
    """

    VALUE_01 = "01"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_31 = "31"


class List254(Enum):
    """
    Resource file date role code.

    :cvar VALUE_17: Last updated Date when a resource was last changed
        or updated
    :cvar VALUE_27: Available from Date from which a resource is
        available for download
    :cvar VALUE_28: Available until Date until which a resource is
        available for download
    """

    VALUE_17 = "17"
    VALUE_27 = "27"
    VALUE_28 = "28"


class List255(Enum):
    """
    Insert point type.

    :cvar ALP: Adjacent to logical page Insert appears after an even
        numbered or before an odd numbered logical page.
        &lt;InsertPointValue&gt; is an integer page number
    :cvar APP: Adjacent to physical page Insert appears after an even
        numbered or before an odd numbered printed page number.
        &lt;InsertPointValue&gt; is an integer page number
    :cvar ATC: At timecode Insert appears in the body at a specific
        timecode (hours, minutes, seconds, counted from the beginning of
        the product before any inserts are added).
        &lt;InsertPointValue&gt; is in the format HHHMMSS. Fill with
        leading zeroes if any elements are missing. If centisecond
        precision is required, use HHHMMSScc
    :cvar AHL: Adjacent to HTML label Insert appears before the block-
        level HTML element – &amp;lt;InsertPointValue&gt; is the value
        of the id or name attribute of the block-level element (which
        must be unique within the body of the product)
    """

    ALP = "ALP"
    APP = "APP"
    ATC = "ATC"
    AHL = "AHL"


class List259(Enum):
    """
    Collection frequency code.

    :cvar U: Unknown
    :cvar I: Irregular No fixed publication schedule
    :cvar E: Biennial Once every two years
    :cvar A: Annual Yearly
    :cvar B: Biannual Twice a year, or once per academic semester
    :cvar T: Triannual Three times a year, or once per academic term
    :cvar Q: Quarterly Four times a year
    :cvar S: Bimonthly Six times per year
    :cvar M: Monthly Once every month, or approximately twelve times per
        year
    :cvar F: Fortnightly Once every two weeks, or approximately twenty
        five times per year
    :cvar W: Weekly Or approximately fifty times per year
    :cvar D: More frequently than weekly
    :cvar X: No future publications Positive indication that the product
        is the last to be published in the collection, or that no
        further publications are planned
    """

    U = "u"
    I = "i"
    E = "e"
    A = "a"
    B = "b"
    T = "t"
    Q = "q"
    S = "s"
    M = "m"
    F = "f"
    W = "w"
    D = "d"
    X = "x"


class List260(Enum):
    """
    Epublication license date role.

    :cvar VALUE_14: Valid from Date on which a license becomes effective
    :cvar VALUE_15: Valid until Date on which a license ceases to be
        effective
    :cvar VALUE_24: From… until date Combines From date and Until date
        to define a period (both dates are inclusive). Use for example
        with dateformat 06
    """

    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_24 = "24"


class List263(Enum):
    """
    Prize identifier type.

    :cvar VALUE_01: Proprietary Note that &lt;IDTypeName&gt; is required
        with proprietary identifiers
    """

    VALUE_01 = "01"


class List27(Enum):
    """
    Subject scheme identifier.

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
        https://www.bisg.org/complete-bisac-subject-headings-list
    :cvar VALUE_11: BISAC Regional theme A geographical qualifier used
        with a BISAC subject category
    :cvar VALUE_12: BIC subject category For all BIC subject codes and
        qualifiers, see https://bic.org.uk/resources/BIC-Standard-
        Subject-Categories/
    :cvar VALUE_13: BIC geographical qualifier
    :cvar VALUE_14: BIC language qualifier (language as subject)
    :cvar VALUE_15: BIC time period qualifier
    :cvar VALUE_16: BIC educational purpose qualifier
    :cvar VALUE_17: BIC reading level and special interest qualifier
    :cvar VALUE_18: DDC-Sachgruppen der Deutschen Nationalbibliografie
        Used for German National Bibliography since 2004 (100 subjects).
        Is different from value 30. See
        http://www.dnb.de/service/pdf/ddc_wv_aktuell.pdf (in German) or
        http://www.dnb.de/eng/service/pdf/ddc_wv_aktuell_eng.pdf
        (English)
    :cvar VALUE_19: LC fiction genre heading
    :cvar VALUE_20: Keywords For indexing and search purposes, not
        normally intended for display. Where multiple keywords or
        keyword phrases are sent, this should be in a single instance of
        the &lt;SubjectHeadingText&gt; element, and it is recommended
        that they should be separated by semi-colons (this is consistent
        with Library of Congress preferred practice)
    :cvar VALUE_21: BIC children’s book marketing category See PA/BIC
        CBMC guidelines at https://bic.org.uk/resources/childrens-books-
        marketing-classifications/
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
        See https://vlb.de/assets/images/wgsneuversion2_0.pdf (in
        German)
    :cvar VALUE_27: SWD Schlagwortnormdatei – Subject Headings Authority
        File in the German-speaking countries. See
        http://www.dnb.de/standardisierung/normdateien/swd.htm (in
        German) and
        http://www.dnb.de/eng/standardisierung/normdateien/swd.htm
        (English). Deprecated in favor of the GND
    :cvar VALUE_28: Thèmes Electre Subject classification used by
        Electre (France)
    :cvar VALUE_29: CLIL Classification thématique France. A four-digit
        number, see https://clil.centprod.com/listeActive.html (in
        French)
    :cvar VALUE_30: DNB-Sachgruppen Deutsche Bibliothek subject groups.
        Used for German National Bibliography until 2003 (65 subjects).
        Is different from value 18. See
        http://www.dnb.de/service/pdf/ddc_wv_alt_neu.pdf (in German)
    :cvar VALUE_31: NUGI Nederlandse Uniforme Genre-Indeling (former
        Dutch book trade classification)
    :cvar VALUE_32: NUR Nederlandstalige Uniforme Rubrieksindeling
        (Dutch book trade classification, from 2002), see
        http://www.boek.nl/nur (in Dutch)
    :cvar VALUE_33: ECPA Christian Book Category Former ECPA Christian
        Product Category Book Codes, consisting of up to three x
        3-letter blocks, for Super Category, Primary Category and Sub-
        Category, previously at
        http://www.ecpa.org/ECPA/cbacategories.xls. No longer maintained
        by the ECPA. Deprecated
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
    :cvar VALUE_39: Læreplaner-KL06 Norwegian school curriculum version.
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
        documentation available at https://www.ie-online.it/CCE2_2.0.pdf
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
        German association of educational media publishers, formerly at
        http://www.bildungsmedien.de/service/onixlisten/unterrichtsfach_onix_codelist27_value59_0408.pdf.
        Deprecated – use Thema subject category (eg YPA – Educational:
        Arts, general) instead, and add a Thema language qualifier (eg
        2ACB – English) for language teaching
    :cvar VALUE_60: Fagkoder Norwegian primary and secondary school
        subject categories (fagkoder), see http://www.udir.no/
    :cvar VALUE_61: JEL classification Journal of Economic Literature
        classification scheme
    :cvar VALUE_62: CSH National Library of Canada subject heading
        (English)
    :cvar VALUE_63: RVM Répertoire de vedettes-matière Bibliothèque de
        l’Université Laval) (French)
    :cvar VALUE_64: YSA Finnish General Thesaurus (Finnish: Yleinen
        suomalainen asiasanasto). See https://finto.fi/ysa/fi/ (in
        Finnish). Deprecated. No longer updated, and replaced by YSO
        (see code 71)
    :cvar VALUE_65: Allärs Swedish translation of the Finnish General
        Thesaurus (Swedish: Allmän tesaurus på svenska). See
        https://finto.fi/allars/sv/ (in Swedish). Deprecated. No longer
        updated, and replaced by YSO (see code 71)
    :cvar VALUE_66: YKL Finnish Public Libraries Classification System
        (Finnish: Yleisten kirjastojen luokitusjärjestelmä). See
        https://finto.fi/ykl/fi/ (in Finnish), https://finto.fi/ykl/sv/
        (in Swedish), https://finto.fi/ykl/en/ (in English)
    :cvar VALUE_67: MUSA Finnish Music Thesaurus (Finnish: Musiikin
        asiasanasto). See https://finto.fi/musa/fi/ (in Finnish).
        Deprecated, and replaced by YSO (see code 71)
    :cvar VALUE_68: CILLA Swedish translation of the Finnish Music
        Thesaurus (Swedish: Specialtesaurus för musik). See
        https://finto.fi/musa/sv/ (in Swedish). Deprecated, and replaced
        by YSO (see code 71)
    :cvar VALUE_69: Kaunokki Finnish thesaurus for fiction (Finnish:
        Fiktiivisen aineiston asiasanasto). See
        https://finto.fi/kaunokki/fi/ (in Finnish). Deprecated. No
        longer updated, and replaced by Kauno and SLM (see codes D0 and
        D1)
    :cvar VALUE_70: Bella Swedish translation of the Finnish thesaurus
        for fiction (Swedish: Specialtesaurus för fiktivt material:).
        See https://finto.fi/kaunokki/sv/ (in Swedish). Deprecated. No
        longer updated, and replaced by Kauno and SLM (see codes D0 and
        D1)
    :cvar VALUE_71: YSO General Finnish Ontology (Finnish: Yleinen
        suomalainen ontologia). See https://finto.fi/yso/fi/ (in
        Finnish), https://finto.fi/yso/sv/ (in Swedish),
        https://finto.fi/yso/en/ (in English)
    :cvar VALUE_72: PTO Finnish Geospatial Domain Ontology (Finnish:
        Paikkatieto ontologia). See https://finto.fi/pto/fi/ (in
        Finnish), https://finto.fi/pto/sv/ (in Swedish),
        https://finto.fi/pto/en/ (in English)
    :cvar VALUE_73: Suomalainen kirja-alan luokitus Finnish book trade
        categorisation
    :cvar VALUE_74: Sears Sears List of Subject Headings
    :cvar VALUE_75: BIC E4L BIC E4Libraries Category Headings, formerly
        at http://www.bic.org.uk/51/E4libraries-Subject-Category-
        Headings/ but replaced by UK Standard Library Categories (code
        92). Deprecated
    :cvar VALUE_76: CSR Code Sujet Rayon: subject categories used by
        bookstores in France
    :cvar VALUE_77: Suomalainen oppiaineluokitus Finnish school subject
        categories. See https://www.onixkeskus.fi/media/f/5722
    :cvar VALUE_78: Japanese book trade C-Code See
        https://isbn.jpo.or.jp/doc/08.pdf#page=44 (in Japanese)
    :cvar VALUE_79: Japanese book trade Genre Code
    :cvar VALUE_80: Fiktiivisen aineiston lisäluokitus Finnish fiction
        genre classification. See
        https://finto.fi/ykl/fi/page/fiktioluokka (in Finnish),
        https://finto.fi/ykl/sv/page/fiktioluokka (in Swedish),
        https://finto.fi/ykl/en/page/fiktioluokka (in English)
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
    :cvar VALUE_91: GND (de: Gemeinsame Normdatei) Integrated Authority
        File used in the German-speaking countries. See
        https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html
        (English). Combines the PND, SWD and GKD into a single authority
        file, and should be used in preference to the older codes
    :cvar VALUE_92: BIC UKSLC UK Standard Library Categories, the
        successor to BIC’s E4L classification scheme. See
        https://bic.org.uk/resources/uk-standard-library-categories/
    :cvar VALUE_93: Thema subject category International multilingual
        subject category scheme – see https://ns.editeur.org/thema
    :cvar VALUE_94: Thema place qualifier
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
        subject classification, URI
        http://data.education.fr/voc/scolomfr/scolomfr-voc-015GTPX
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
        educational objectives. See
        https://www.bisg.org/products/recommendations-for-citing-
        educational-standards-and-objectives-in-metadata
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
        educational subject classification, URI
        http://data.education.fr/voc/scolomfr/scolomfr-voc-029
    :cvar B4: Key character names For fiction and non-fiction, one or
        more key names, provided – like keywords – for indexing and
        search purposes. Where multiple character names are sent, this
        should be in a single instance of &lt;SubjectHeadingText&gt;,
        and multiple names should be separated by semi-colons. Note
        &lt;NameAsSubject&gt; should be used for people who are the
        central subject of the book. Code B4 may be used for names of
        lesser importance
    :cvar B5: Key place names For fiction and non-fiction, one or more
        key names, provded – like keywords – for indexing and search
        purposes. Where multiple place names are sent, this should in a
        single instance of &lt;SubjectHeadingText&gt;, and multiple
        names should be separated by semi-colons. Only for use in ONIX
        3.0 or later
    :cvar B6: FAST Faceted Application of Subject Terminology, OCLC
        subject scheme based on but different from LCSH (see code 04).
        Only for use in ONIX 3.0 or later
    :cvar B7: NGSS Next Generation Science Standards for K-12 education
        in the USA (https://www.nextgenscience.org). &lt;SubjectCode&gt;
        is a code such as 4-PS3-2. Only for use in ONIX 3.0 or later
    :cvar B8: MVB-Lesemotive MVB classification of ‘reading rationales’,
        which classify unconscious motives that lead to a book purchase.
        Categories are assigned and maintained by MVB. Only for use in
        ONIX 3.0 or later. See https://vlb.de/lesemotive
    :cvar B9: LOPS21 Subject module Finnish Suomalainen
        oppiaineluokitus. Only for use in ONIX 3.0 or later
    :cvar C0: Læreplaner-LK20 Codes for Norwegian curriculum for primary
        and secondary education. Only for use in ONIX 3.0 or later. See
        Læreplaner-LK20 at https://www.udir.no/om-udir/data/kl06-grep/
    :cvar C1: Kompetansemål-LK20 Codes for competency aims in the
        Norwegian curriculum for primary and secondary education. Only
        for use in ONIX 3.0 or later. See Kompetansemål-LK20 at
        https://www.udir.no/om-udir/data/kl06-grep/
    :cvar C2: Kompetansemålsett-LK20 Codes for sets of competency aims
        in the Norwegian curriculum for primary and secondary education.
        Only for use in ONIX 3.0 or later. See Kompetansemålsett-LK20 at
        https://www.udir.no/om-udir/data/kl06-grep/
    :cvar C3: Tverrfaglige temaer-LK20 Codes for interdisciplinary
        topics in the Norwegian curriculum for primary and secondary
        education. Only for use in ONIX 3.0 or later. See Tverrfaglige
        temaer-LK20 at https://www.udir.no/om-udir/data/kl06-grep/
    :cvar C4: CLIL – Type d’article scolaire Only for use in ONIX 3.0 or
        later
    :cvar C5: GAR – Type pédagogique Gestionnaire d’Accès aux resources
        – see https://gar.education.fr/ Only for use in ONIX 3.0 or
        later
    :cvar C6: ISCED-F UNESCO ISCED Fields of education and training
        (2013), eg &lt;SubjectCode&gt; 0222 is ‘History and
        archaeology’. Only for use in ONIX 3.0 or later. See
        http://uis.unesco.org/sites/default/files/documents/international-
        standard-classification-of-education-fields-of-education-and-
        training-2013-detailed-field-descriptions-2015-en.pdf
    :cvar C7: Klassifikationen von Spielen, Puzzles und Spielwaren
        German category scheme for games, puzzles and toys. Only for use
        in ONIX 3.0 or later. See
        https://www.ludologie.de/fileadmin/user_upload/PDFs/211126_Kategorisierung_von_Spielen_Puzzles_und_Spielwaren.pdf
    :cvar C8: NBVok NTSF National Library of Norway genre and form
        thesaurus. Only for use in ONIX 3.0 or later. See
        https://www.nb.no/nbvok/ntsf
    :cvar C9: JPRO Genre Subject / genre code used in Japan. Only for
        use in ONIX 3.0 or later
    :cvar D0: KAUNO Finnish Ontology for fiction (Finnish: Fiktiivisen
        aineiston ontologia). See https://finto.fi/kauno/fi/ (in
        Finnish), https://finto.fi/kauno/sv/ (in Swedish),
        https://finto.fi/kauno/en/ (in English). Only for use in ONIX
        3.0 or later
    :cvar D1: SLM Finnish genre and form vocabulary (Finnish:
        Suomalainen lajityyppi ja muotosanasto). See
        https://finto.fi/slm/fi/ (in Finnish), https://finto.fi/slm/sv/
        (in Swedish), https://finto.fi/slm/en/ (in English). Only for
        use in ONIX 3.0 or later
    :cvar D2: YSO-places General Finnish Ontology for Places (Finnish:
        Yleinen suomalainen ontologia – paikat). See
        https://finto.fi/yso-paikat/fi/ (in Finnish),
        https://finto.fi/yso-paikat/sv/ (in Swedish),
        https://finto.fi/yso-paikat/en/ (in English). Only for use in
        ONIX 3.0 or later
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
    B5 = "B5"
    B6 = "B6"
    B7 = "B7"
    B8 = "B8"
    B9 = "B9"
    C0 = "C0"
    C1 = "C1"
    C2 = "C2"
    C3 = "C3"
    C4 = "C4"
    C5 = "C5"
    C6 = "C6"
    C7 = "C7"
    C8 = "C8"
    C9 = "C9"
    D0 = "D0"
    D1 = "D1"
    D2 = "D2"


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
    :cvar VALUE_12: Schulform Type of school: codelist formerly
        maintained by VdS Bildungsmedien eV, the German association of
        educational media publishers at
        http://www.bildungsmedien.de/service/onixlisten/schulform_onix_codelist29_value12_0408.pdf.
        Deprecated – use Thema educational purpose qualifier (eg 4Z-DE-
        BA – for German Elementary School) in &lt;Subject&gt; instead
    :cvar VALUE_13: Bundesland School region: codelist maintained by VdS
        Bildungsmedien eV, the German association of educational media
        publishers, indicating where products are licensed to be used in
        schools. See
        http://www.bildungsmedien.de/service/onixlisten/bundesland_onix_codelist29_value13_0408.pdf.
        Deprecated
    :cvar VALUE_14: Ausbildungsberuf Occupation: codelist for vocational
        training materials formerly maintained by VdS Bildungsmedien eV,
        the German association of educational media publishers at
        http://www.bildungsmedien.de/service/onixlisten/ausbildungsberufe_onix_codelist29_value14_0408.pdf.
        Deprecated – use Thema educational purpose qualifier (eg 4Z-DE-
        UH – for specific German professional/vocational qualifications
        and degrees) in &lt;Subject&gt; instead
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
        indicating suitability for a particular adult audience, using a
        code from List 203. Should only be used when the ONIX Audience
        code indicates a general adult audience (code 01 from List 28)
    :cvar VALUE_23: Common European Framework of Reference for Language
        Learning (CEFR) Codes A1 to C2 indicating standardised level of
        language learning or teaching material, from beginner to
        advanced, defined by the Council of Europe (see
        http://www.coe.int/lang-CEFR)
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
    :cvar VALUE_30: ISCED 2011 International Standard Classification of
        Education levels (2011), eg &lt;AudienceCodeValue&gt; 253 is
        ‘Lower secondary vocational education, level completion without
        direct access to upper secondary education’. Only for use in
        ONIX 3.0 or later. See
        http://uis.unesco.org/en/topic/international-standard-
        classification-education-isced
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


class List3(Enum):
    """
    Record source type.

    :cvar VALUE_00: Unspecified
    :cvar VALUE_01: Publisher
    :cvar VALUE_02: Publisher’s distributor Use to designate a
        distributor providing primary warehousing and fulfillment for a
        publisher or for a publisher’s sales agent, as distinct from a
        wholesaler
    :cvar VALUE_03: Wholesaler
    :cvar VALUE_04: Bibliographic agency Bibliographic data aggregator
    :cvar VALUE_05: Library bookseller Library supplier. Bookseller
        selling to libraries (including academic libraries)
    :cvar VALUE_06: Publisher’s sales agent Use for a publisher’s sales
        agent responsible for marketing the publisher’s products within
        a territory, as opposed to a publisher’s distributor who
        fulfills orders but does not market
    :cvar VALUE_07: Publisher’s conversion service provider Downstream
        provider of e-publication format conversion services (who might
        also be a distributor or retailer of the converted
        e-publication), supplying metadata on behalf of the publisher.
        The assigned ISBN is taken from the publisher’s ISBN prefix
    :cvar VALUE_08: Conversion service provider Downstream provider of
        e-publication format conversion services (who might also be a
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
    :cvar VALUE_12: UK school grade Values are to be defined by BIC for
        England and Wales, Scotland and N Ireland
    :cvar VALUE_15: Reading speed, words per minute Values in
        &lt;AudienceRangeValue&gt; must be integers
    :cvar VALUE_16: Interest age, months For use up to 36 months only,
        or up to 42 months in Audience range value (2) only: values in
        &lt;AudienceRangeValue&gt; must be integers. Should not be used
        when an Audience range with qualifier code 17 is present
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
    :cvar VALUE_23: Schulform Deprecated – assigned in error: see List
        29
    :cvar VALUE_24: Bundesland Deprecated – assigned in error: see List
        29
    :cvar VALUE_25: Ausbildungsberuf Deprecated – assigned in error: see
        List 29
    :cvar VALUE_26: Canadian school grade range Values for
        &lt;AudienceRangeValue&gt; are specified in List 77
    :cvar VALUE_27: Finnish school grade range
    :cvar VALUE_28: Finnish Upper secondary school course Lukion kurssi
    :cvar VALUE_29: Chinese School Grade range Values are P, K, 1–17
        (including college-level audiences), see List 227
    :cvar VALUE_30: French school cycles / classes Detailed French
        educational level classification. Values are defined by
        ScoLOMFR, see http://data.education.fr/voc/scolomfr/scolomfr-
        voc-022 – Cycles de l’enseignement scolaire. See also code 34
    :cvar VALUE_31: Brazil Education level Nível de Educação do Brasil,
        see List 238. Only for use in ONIX 3.0 or later
    :cvar VALUE_32: French educational levels Basic French educational
        level classification. Values are defined by ScoLOMFR. Only for
        use in ONIX 3.0 or later. See
        http://data.education.fr/voc/scolomfr/scolomfr-voc-012
    :cvar VALUE_33: Finnish Upper secondary school course (2021+) Only
        for use in ONIX 3.0 or later
    :cvar VALUE_34: Detailed French educational levels Detailed French
        educational level classification. Values are defined by
        ScoLOMFR. Only for use in ONIX 3.0 or later. See
        http://data.education.fr/voc/scolomfr/scolomfr-voc-022 – Niveau
        éducatif détaillé. See also code 30
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
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_34 = "34"


class List31(Enum):
    """
    Audience range precision.

    :cvar VALUE_01: Exact May only be used in Audience range precision
        (1), and when no Audience range precision (2) is present
    :cvar VALUE_03: From May only be used in Audience range precision
        (1)
    :cvar VALUE_04: To May be used in Audience range precision (1) when
        no Audience range precision (2) is present, or in Audience range
        precision (2) when Audience range precision (1) is code 03
    """

    VALUE_01 = "01"
    VALUE_03 = "03"
    VALUE_04 = "04"


class List32(Enum):
    """
    Complexity scheme identifier.

    :cvar VALUE_01: Lexile code For example AD or HL. Deprecated in ONIX
        3 – use code 06 instead
    :cvar VALUE_02: Lexile number For example 880L. Deprecated in ONIX 3
        – use code 06 instead
    :cvar VALUE_03: Fry Readability score Fry readability metric based
        on number of sentences and syllables per 100 words. Expressed as
        an integer from 1 to 15 in &lt;ComplexityCode&gt;
    :cvar VALUE_04: IoE Book Band UK Institute of Education Book Bands
        for Guided Reading scheme (see https://www.ucl.ac.uk/reading-
        recovery-europe/ilc/publications/which-book-why).
        &lt;ComplexityCode&gt; is a color, eg ‘Pink A’ or ‘Copper’
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
        Learning Accelerated Reader scheme. &lt;ComplexityCode&gt; is
        the ‘Book Level’, a real number between 0 and 17. See
        http://www.renaissance.com/products/accelerated-reader/atos-
        analyzer
    :cvar VALUE_08: Flesch-Kincaid Grade Level Flesch-Kincaid Grade
        Level Formula, a standard readability measure based on the
        weighted number of syllables per word and words per sentence.
        &lt;ComplexityCode&gt; is a real number typically between about
        -1 and 20
    :cvar VALUE_09: Guided Reading Level Use this code for books
        levelled by the publisher or a third party using the Fountas and
        Pinnell Guided Reading methodology
    :cvar VALUE_10: Reading Recovery Level Used for books aimed at K-2
        literacy intervention. &lt;ComplexityCode&gt; is an integer
        between 1 and 20
    :cvar VALUE_11: LIX Swedish ‘läsbarhetsindex’ readability index used
        in Scandinavia. Only for use in ONIX 3.0 or later
    :cvar VALUE_12: Lexile Audio measure Lexile Audio measure from
        MetaMetrics’ Framework for Listening. The code in
        &lt;ComplexityCode&gt; indicates the difficulty of comprehension
        of audio material (for example 600L or 1030L). Only for use in
        ONIX 3.0 or later. See https://lexile.global/the-lexile-
        framework-for-listening/
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


class List34(Enum):
    """
    Text format.

    :cvar VALUE_02: HTML Other than XHTML
    :cvar VALUE_03: XML Other than XHTML
    :cvar VALUE_05: XHTML
    :cvar VALUE_06: Default text format Default: plain text containing
        no markup tags of any kind, except for the character entities
        &amp;amp; and &amp;lt; that XML insists must be used to
        represent ampersand and less-than characters in textual data,
        and in the encoding declared at the head of the message or in
        the XML default (UTF-8 or UTF-16) if there is no explicit
        declaration
    :cvar VALUE_07: Basic ASCII text Plain text containing no markup
        tags of any kind, except for the character entities &amp;amp;
        and &amp;lt; that XML insists must be used to represent
        ampersand and less-than characters in textual data, and with the
        character set limited to the ASCII range, i.e. valid characters
        whose Unicode character numbers lie between 32 (space) and 126
        (tilde)
    """

    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"


class List41(Enum):
    """
    Prize or award achievement.

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
    Text item type.

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
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"


class List43(Enum):
    """
    Text item identifier type.

    :cvar VALUE_01: Proprietary For example, a publisher’s own
        identifier. Note that &lt;IDTypeName&gt; is required with
        proprietary identifiers
    :cvar VALUE_03: GTIN-13 Formerly known as the EAN-13 (unhyphenated)
    :cvar VALUE_06: DOI
    :cvar VALUE_09: PII Publisher item identifier
    :cvar VALUE_10: SICI For serial items only
    :cvar VALUE_11: ISTC
    :cvar VALUE_15: ISBN-13 (Unhyphenated)
    :cvar VALUE_39: ISCC International Standard Content Code, a
        ‘similarity hash’ derived algorithmically from the content
        itself (see https://iscc.codes). &lt;IDValue&gt; is a sequence
        comprising the Meta-Code and Content-Code ISCC-UNITSs generated
        from a digital manifestation of the work, as a variable-length
        case-insensitive alphanumeric string (or 27 characters including
        one hyphen if using ISCC v1.0, but this is deprecated). Note
        alphabetic characters in v1.x ISCCs use Base32 encoding and are
        conventionally upper case. The ‘ISCC:’ prefix is omitted. Only
        for use in ONIX 3.0 or later
    """

    VALUE_01 = "01"
    VALUE_03 = "03"
    VALUE_06 = "06"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_15 = "15"
    VALUE_39 = "39"


class List44(Enum):
    """
    Name identifier type.

    :cvar VALUE_01: Proprietary Note that &lt;IDTypeName&gt; is required
        with proprietary identifiers
    :cvar VALUE_02: Proprietary Deprecated – use code 01
    :cvar VALUE_03: DNB publisher identifier Deutsche Nationalbibliothek
        publisher identifier
    :cvar VALUE_04: Börsenverein Verkehrsnummer (de: Verkehrsnummer ded
        Börsenverein des deutschen Buchhandels)
    :cvar VALUE_05: German ISBN Agency publisher identifier (de: MVB-
        Kennnummer)
    :cvar VALUE_06: GLN GS1 global location number (formerly EAN
        location number)
    :cvar VALUE_07: SAN Book trade Standard Address Number – US, UK etc
    :cvar VALUE_08: MARC organization code MARC code list for
        organizations – see
        http://www.loc.gov/marc/organizations/orgshome.html
    :cvar VALUE_10: Centraal Boekhuis Relatie ID Trading party
        identifier used in the Netherlands
    :cvar VALUE_12: Distributeurscode Boekenbank Flemish supplier code.
        Only for use in ONIX 3.0 or later
    :cvar VALUE_13: Fondscode Boekenbank Flemish publisher code
    :cvar VALUE_15: Y-tunnus Business Identity Code (Finland). See
        http://www.ytj.fi/ (in Finnish)
    :cvar VALUE_16: ISNI International Standard Name Identifier. A
        sixteen digit number. Usually presented with spaces or hyphens
        dividing the number into four groups of four digits, but in ONIX
        the spaces or hyphens should be omitted. See https://isni.org/
    :cvar VALUE_17: PND Personennamendatei – person name authority file
        used by Deutsche Nationalbibliothek and in other German-speaking
        countries. See
        http://www.dnb.de/standardisierung/normdateien/pnd.htm (German)
        or http://www.dnb.de/eng/standardisierung/normdateien/pnd.htm
        (English). Deprecated in favor of the GND
    :cvar VALUE_18: NACO A control number assigned to a Library of
        Congress Control Number (LCCN) Name Authority / NACO record
    :cvar VALUE_19: Japanese Publisher identifier Publisher identifier
        administered by Japanese ISBN Agency
    :cvar VALUE_20: GKD Gemeinsame Körperschaftsdatei – Corporate Body
        Authority File in the German-speaking countries. See
        http://www.dnb.de/standardisierung/normdateien/gkd.htm (German)
        or http://www.dnb.de/eng/standardisierung/normdateien/gkd.htm
        (English). Deprecated in favor of the GND
    :cvar VALUE_21: ORCID Open Researcher and Contributor ID. A sixteen
        digit number. Usually presented with hyphens dividing the number
        into four groups of four digits, but in ONIX the hyphens should
        be omitted. See http://www.orcid.org/
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
        http://www.ringgold.com/identify.html
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
        https://www.crossref.org/services/funder-registry/
    :cvar VALUE_33: BNE CN Control number assigned to a Name Authority
        record by the Biblioteca Nacional de España
    :cvar VALUE_34: BNF Control Number Numéro de la notice de personne
        BNF
    :cvar VALUE_35: ARK Archival Resource Key, as a URL (including the
        address of the ARK resolver provided by eg a national library)
    :cvar VALUE_36: Nasjonalt autoritetsregister Nasjonalt
        autoritetsregister for navn – Norwegian national authority file
        for personal and corporate names. Only for use in ONIX 3.0 or
        later
    :cvar VALUE_37: GRID Global Research Identifier Database ID (see
        https://www.grid.ac). Only for use in ONIX 3.0 or later.
        Deprecated – ROR is now generally preferred
    :cvar VALUE_38: IDRef Party ID from Identifiers and Standards for
        Higher Education and Research (fr: Identifiants et Référentiels
        pour l’enseignement supérieur et la recherche). Only for use in
        ONIX 3.0 or later. See https://www.idref.fr
    :cvar VALUE_39: IPI Party ID from CISAC’s proprietary Interested
        Party Information scheme, used primarily in rights and royalies
        administration. Only for use in ONIX 3.0 or later
    :cvar VALUE_40: ROR Research organization registry identifier (see
        https://ror.org), leading 0 followed by 8 alphanumeric
        characters (including 2-digit checksum). Only for use in ONIX
        3.0 or later
    :cvar VALUE_41: EORI Economic Operators Registration and
        Identification, identifier for businesses that import into or
        export from the EU. Only for use in ONIX 3.0 or later
    :cvar VALUE_42: LEI Legal Entity Identifier, administered by the
        Global LEI Foundation, as 20 alphanumeric characters without
        spaces or hyphens. Only for use in ONIX 3.0 or later
    :cvar VALUE_43: SIREN French business identifier, issued by the
        National Institute of Statistics and Economic Studies (INSEE). 9
        digits, without spaces. Only for use in ONIX 3.0 or later
    :cvar VALUE_44: SIRET French business and location identifier,
        issued by the National Institute of Statistics and Economic
        Studies (INSEE). 14 digits (the SIREN plus a further five
        digits), without spaces, or occasionally an alphanumeric code.
        Only for use in ONIX 3.0 or later
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
    VALUE_12 = "12"
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
    VALUE_36 = "36"
    VALUE_37 = "37"
    VALUE_38 = "38"
    VALUE_39 = "39"
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_44 = "44"


class List45(Enum):
    """
    Publishing role.

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
        different from the body funding the underlying research.
        Intended primarily for use with open access publications
    :cvar VALUE_15: Research funder Body funding the research on which
        publication is based, if different from the body funding the
        publication. Intended primarily for use with open access
        publications
    :cvar VALUE_16: Funding body Body funding research and publication.
        Intended primarily for use with open access publications
    :cvar VALUE_17: Printer Organization responsible for printing a
        printed product. Supplied primarily to meet legal deposit
        requirements, and may apply only to the first impression. The
        organization may also be responsible for binding, when a
        separate binder is not specified
    :cvar VALUE_18: Binder Organization responsible for binding a
        printed product (where distinct from the printer). Supplied
        primarily to meet legal deposit requirements, and may apply only
        to the first impression
    :cvar VALUE_19: Manufacturer Organization primarily responsible for
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
    Sales rights type.

    :cvar VALUE_00: Sales rights unknown or unstated for any reason May
        only be used with the &lt;ROWSalesRightsType&gt; element
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
        use with ONIX 3.0. Deprecated
    :cvar VALUE_08: For sale with non-exclusive rights in the specified
        countries or territories (sales restriction applies) Only for
        use with ONIX 3.0. Deprecated
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


class List48(Enum):
    """
    Measure type.

    :cvar VALUE_01: Height For a book, the overall height when standing
        on a shelf. For a folded map, the height when folded. For
        packaged products, the height of the retail packaging, and for
        trade-only products, the height of the trade packaging. In
        general, the height of a product in the form in which it is
        presented or packaged for retail sale
    :cvar VALUE_02: Width For a book, the overall horizontal dimension
        of the cover when standing upright. For a folded map, the width
        when folded. For packaged products, the width of the retail
        packaging, and for trade-only products, the width of the trade
        packaging. In general, the width of a product in the form in
        which it is presented or packaged for retail sale
    :cvar VALUE_03: Thickness For a book, the overall thickness of the
        spine. For a folded map, the thickness when folded. For packaged
        products, the depth of the retail packaging, and for trade-only
        products, the depth of the trade packaging. In general, the
        thickness or depth of a product in the form in which it is
        presented or packaged for retail sale
    :cvar VALUE_04: Page trim height Overall height (code 01) is
        preferred for general use, as it includes the board overhang for
        hardbacks
    :cvar VALUE_05: Page trim width Overall width (code 02) is preferred
        for general use, as it includes the board overhang and spine
        thickness for hardbacks
    :cvar VALUE_06: Unit volume The volume of the product, including any
        retail packaging. Note the &lt;MeasureUnit&gt; is interpreted as
        a volumetric unit – for example code cm = cubic centimetres (ie
        millilitres), and code oz = (US) fluid ounces. Only for use in
        ONIX 3.0 or later
    :cvar VALUE_07: Unit capacity Volume of the internal (fluid)
        contents of a product (eg of paint in a can). Note the
        &lt;MeasureUnit&gt; is interpreted as a volumetric unit – for
        example code cm = cubic centimetres (ie millilitres), and code
        oz = (US) fluid ounces. Only for use in ONIX 3.0 or later
    :cvar VALUE_08: Unit weight The overall weight of the product,
        including any retail packaging
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
    :cvar VALUE_14: Unpackaged height As height, but of the product
        without packaging (use only for products supplied in retail
        packaging, must also supply overall size when packaged using
        code 01). Only for use in ONIX 3.0 or later
    :cvar VALUE_15: Unpackaged width As width, but of the product
        without packaging (use only for products supplied in retail
        packaging, must also supply overall size when packaged using
        code 02). Only for use in ONIX 3.0 or later
    :cvar VALUE_16: Unpackaged thickness As thickness, but of the
        product without packaging (use only for products supplied in
        retail packaging, must also supply overall size when packaged
        using code 03). Only for use in ONIX 3.0 or later
    :cvar VALUE_17: Total battery weight Weight of batteries built-in,
        pre-installed or supplied with the product. Details of the
        batteries should be provided using &lt;ProductFormFeature&gt;. A
        per-battery unit weight may be calculated from the number of
        batteries if required. Only for use in ONIX 3.0 or later
    :cvar VALUE_18: Total weight of Lithium Mass or equivalent mass of
        elemental Lithium within the batteries built-in, pre-installed
        or supplied with the product (eg a Lithium Iron phosphate
        battery with 160g of cathode material would have a total of
        around 7g of Lithium). Details of the batteries must be provided
        using ProductFormFeature. A per-battery unit mass of Lithium may
        be calculated from the number of batteries if required. Only for
        use in ONIX 3.0 or later
    :cvar VALUE_19: Assembled length For use where product or part of
        product requires assembly, for example the size of a completed
        kit, puzzle or assembled display piece. The assembled dimensions
        may be larger than the product size as supplied. Use only when
        the unassembled dimensions as supplied (including any retail or
        trade packaging) are also provided using codes 01, 02 and 03.
        Only for use in ONIX 3.0 or later
    :cvar VALUE_20: Assembled width
    :cvar VALUE_21: Assembled height
    :cvar VALUE_22: Unpackaged unit weight Overall unit weight (code 08)
        is preferred for general use, as it includes the weight of any
        packaging. Use Unpackaged unit weight only for products supplied
        in retail packaging, and must also supply overall unit weight.
        Only for use in ONIX 3.0 or later
    :cvar VALUE_23: Carton length Includes packaging. See
        &lt;PackQuantity&gt; for number of copies of the product per
        pack, and used only when dimensions of individual copies (codes
        01, 02, 03) AND &lt;PackQuantity&gt; are supplied. Note that
        neither orders nor deliveries have to be aligned with multiples
        of the pack quantity, but such orders and deliveries may be more
        convenient to handle. Only for use in ONIX 3.0 or later
    :cvar VALUE_24: Carton width
    :cvar VALUE_25: Carton height
    :cvar VALUE_26: Carton weight Includes the weight of product(s)
        within the carton. See &lt;PackQuantity&gt; for number of copies
        per pack, and used only when the weight of individual copies
        (code 08) AND &lt;PackQuantity&gt; are supplied. Only for use in
        ONIX 3.0 or later
    :cvar VALUE_27: Pallet length Includes pallet and packaging. See
        &lt;PalletQuantity&gt; for number of copies of the product per
        pallet, and used only when dimensions of individual copies
        (codes 01, 02, 03) AND &lt;PalletQuantity&gt; are supplied. Note
        that neither orders nor deliveries have to be aligned with
        multiples of the pallet quantity, but such orders and deliveries
        may be more convenient to handle. Only for use in ONIX 3.0 or
        later
    :cvar VALUE_28: Pallet width
    :cvar VALUE_29: Pallet height
    :cvar VALUE_30: Pallet weight Includes the weight of product(s) and
        cartons stacked on the pallet. See &lt;PalletQuantity&gt; for
        the number of copies per pallet, and used only when the weight
        of individual copies (code 08) AND &lt;PalletQuantity&gt; are
        supplied.Only for use in ONIX 3.0 or later
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


class List49(Enum):
    """
    Region – based on ISO 3166-2.

    :cvar AU_CT: Australian Capital Territory
    :cvar AU_NS: New South Wales
    :cvar AU_NT: Northern Territory
    :cvar AU_QL: Queensland
    :cvar AU_SA: South Australia
    :cvar AU_TS: Tasmania
    :cvar AU_VI: Victoria
    :cvar AU_WA: Western Australia
    :cvar BE_BRU: Brussels-Capital Region Only for use in ONIX 3.0 or
        later
    :cvar BE_VLG: Flemish Region Only for use in ONIX 3.0 or later
    :cvar BE_WAL: Walloon Region Only for use in ONIX 3.0 or later
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
    :cvar CN_BJ: Beijing Municipality Only for use in ONIX 3.0 or later
    :cvar CN_TJ: Tianjin Municipality Only for use in ONIX 3.0 or later
    :cvar CN_HE: Hebei Province Only for use in ONIX 3.0 or later
    :cvar CN_SX: Shanxi Province Only for use in ONIX 3.0 or later
    :cvar CN_NM: Nei Mongol Autonomous Region Only for use in ONIX 3.0
        or later
    :cvar CN_LN: Liaoning Province Only for use in ONIX 3.0 or later
    :cvar CN_JL: Jilin Province Only for use in ONIX 3.0 or later
    :cvar CN_HL: Heilongjiang Province Only for use in ONIX 3.0 or later
    :cvar CN_SH: Shanghai Municipality Only for use in ONIX 3.0 or later
    :cvar CN_JS: Jiangsu Province Only for use in ONIX 3.0 or later
    :cvar CN_ZJ: Zhejiang Province Only for use in ONIX 3.0 or later
    :cvar CN_AH: Anhui Province Only for use in ONIX 3.0 or later
    :cvar CN_FJ: Fujian Province Only for use in ONIX 3.0 or later
    :cvar CN_JX: Jiangxi Province Only for use in ONIX 3.0 or later
    :cvar CN_SD: Shandong Province Only for use in ONIX 3.0 or later
    :cvar CN_HA: Henan Province Only for use in ONIX 3.0 or later
    :cvar CN_HB: Hubei Province Only for use in ONIX 3.0 or later
    :cvar CN_HN: Hunan Province Only for use in ONIX 3.0 or later
    :cvar CN_GD: Guangdong Province Only for use in ONIX 3.0 or later
    :cvar CN_GX: Guangxi Zhuangzu Autonomous Region Only for use in ONIX
        3.0 or later
    :cvar CN_HI: Hainan Province Only for use in ONIX 3.0 or later
    :cvar CN_CQ: Chongqing Municipality Only for use in ONIX 3.0 or
        later
    :cvar CN_SC: Sichuan Province Only for use in ONIX 3.0 or later
    :cvar CN_GZ: Guizhou Province Only for use in ONIX 3.0 or later
    :cvar CN_YN: Yunnan Province Only for use in ONIX 3.0 or later
    :cvar CN_XZ: Tibet Autonomous Region Only for use in ONIX 3.0 or
        later
    :cvar CN_SN: Shaanxi Province Only for use in ONIX 3.0 or later
    :cvar CN_GS: Gansu Province Only for use in ONIX 3.0 or later
    :cvar CN_QH: Qinghai Province Only for use in ONIX 3.0 or later
    :cvar CN_NX: Ningxia Huizu Autonomous Region Only for use in ONIX
        3.0 or later
    :cvar CN_XJ: Xinjiang Uygur Autonomous Region Only for use in ONIX
        3.0 or later
    :cvar CN_TW: Taiwan Province Prefer code TW (Taiwan, Province of
        China) from List 91. Only for use in ONIX 3.0 or later
    :cvar CN_HK: Hong Kong Special Administrative Region Prefer code HK
        (Hong Kong) from List 91. Only for use in ONIX 3.0 or later
    :cvar CN_MO: Macau Special Administrative Region Prefer code MO
        (Macao) from List 91. Only for use in ONIX 3.0 or later
    :cvar CN_11: Beijing Municipality Deprecated in favor of CN-BJ
    :cvar CN_12: Tianjin Municipality Deprecated in favor of CN-TJ
    :cvar CN_13: Hebei Province Deprecated in favor of CN-HE
    :cvar CN_14: Shanxi Province Deprecated in favor of CN-SX
    :cvar CN_15: Inner Mongolia Autonomous Region Deprecated in favor of
        CN-NM
    :cvar CN_21: Liaoning Province Deprecated in favor of CN-LN
    :cvar CN_22: Jilin Province Deprecated in favor of CN-JL
    :cvar CN_23: Heilongjiang Province Deprecated in favor of CN-HL
    :cvar CN_31: Shanghai Municipality Deprecated in favor of CN-SH
    :cvar CN_32: Jiangsu Province Deprecated in favor of CN-JS
    :cvar CN_33: Zhejiang Province Deprecated in favor of CN-ZJ
    :cvar CN_34: Anhui Province Deprecated in favor of CN-AH
    :cvar CN_35: Fujian Province Deprecated in favor of CN-FJ
    :cvar CN_36: Jiangxi Province Deprecated in favor of CN-JX
    :cvar CN_37: Shandong Province Deprecated in favor of CN-SD
    :cvar CN_41: Henan Province Deprecated in favor of CN-HA
    :cvar CN_42: Hubei Province Deprecated in favor of CN-HB
    :cvar CN_43: Hunan Province Deprecated in favor of CN-HN
    :cvar CN_44: Guangdong Province Deprecated in favor of CN-GD
    :cvar CN_45: Guangxi Zhuang Autonomous Region Deprecated in favor of
        CN-GX
    :cvar CN_46: Hainan Province Deprecated in favor of CN-HI
    :cvar CN_50: Chongqing Municipality Deprecated in favor of CN-CQ
    :cvar CN_51: Sichuan Province Deprecated in favor of CN-SC
    :cvar CN_52: Guizhou Province Deprecated in favor of CN-GZ
    :cvar CN_53: Yunnan Province Deprecated in favor of CN-YN
    :cvar CN_54: Tibet Autonomous Region Deprecated in favor of CN-XZ
    :cvar CN_61: Shaanxi Province Deprecated in favor of CN-SN
    :cvar CN_62: Gansu Province Deprecated in favor of CN-GS
    :cvar CN_63: Qinghai Province Deprecated in favor of CN-QH
    :cvar CN_64: Ningxia Hui Autonomous Region Deprecated in favor of
        CN-NX
    :cvar CN_65: Xinjiang Uyghur Autonomous Region Deprecated in favor
        of CN-XJ
    :cvar CN_71: Taiwan Province Deprecated in favor of CN-TW, but
        prefer code TW (Taiwan, Province of China) from List 91
    :cvar CN_91: Hong Kong Special Administrative Region Deprecated in
        favor of CN-HK, but prefer code HK (Hong Kong) from List 91
    :cvar CN_92: Macau Special Administrative Region Deprecated in favor
        of CN-MO, but prefer code MO (Macao) from List 91
    :cvar ES_CN: Canary Islands
    :cvar FR_H: Corsica
    :cvar GB_AIR: UK airside Airside outlets at UK international
        airports only
    :cvar GB_APS: UK airports All UK airports, including both airside
        and other outlets
    :cvar GB_CHA: Channel Islands Deprecated, replaced by country codes
        GG – Guernsey, and JE – Jersey from List 91
    :cvar GB_ENG: England
    :cvar GB_EWS: England, Wales, Scotland UK excluding Northern
        Ireland. Deprecated – use separate region codes GB-ENG, GB-SCT,
        GB-WLS instead
    :cvar GB_IOM: Isle of Man Deprecated, replaced by country code IM –
        Isle of Man from List 91
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
        writing, this is a synonym for ‘AT BE CY EE FI FR DE ES GR HR IE
        IT LT LU LV MT NL PT SI SK’ (the official Eurozone 20), plus ‘AD
        MC SM VA ME’ and Kosovo (other Euro-using countries in
        continental Europe). Note some other territories using the Euro,
        but outside continental Europe are excluded from this list, and
        may need to be specified separately. ONLY valid in ONIX 3.0, and
        ONLY within P.26 – and this use is itself Deprecated. Use of an
        explicit list of countries instead of ECZ is strongly encouraged
    :cvar WORLD: World In ONIX 3.0 and later, may ONLY be used in
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
    BE_BRU = "BE-BRU"
    BE_VLG = "BE-VLG"
    BE_WAL = "BE-WAL"
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
    CN_BJ = "CN-BJ"
    CN_TJ = "CN-TJ"
    CN_HE = "CN-HE"
    CN_SX = "CN-SX"
    CN_NM = "CN-NM"
    CN_LN = "CN-LN"
    CN_JL = "CN-JL"
    CN_HL = "CN-HL"
    CN_SH = "CN-SH"
    CN_JS = "CN-JS"
    CN_ZJ = "CN-ZJ"
    CN_AH = "CN-AH"
    CN_FJ = "CN-FJ"
    CN_JX = "CN-JX"
    CN_SD = "CN-SD"
    CN_HA = "CN-HA"
    CN_HB = "CN-HB"
    CN_HN = "CN-HN"
    CN_GD = "CN-GD"
    CN_GX = "CN-GX"
    CN_HI = "CN-HI"
    CN_CQ = "CN-CQ"
    CN_SC = "CN-SC"
    CN_GZ = "CN-GZ"
    CN_YN = "CN-YN"
    CN_XZ = "CN-XZ"
    CN_SN = "CN-SN"
    CN_GS = "CN-GS"
    CN_QH = "CN-QH"
    CN_NX = "CN-NX"
    CN_XJ = "CN-XJ"
    CN_TW = "CN-TW"
    CN_HK = "CN-HK"
    CN_MO = "CN-MO"
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
    WORLD = "WORLD"


class List5(Enum):
    """
    Product identifier type.

    :cvar VALUE_01: Proprietary For example, a publisher’s or
        wholesaler’s product number or SKU. Note that &lt;IDTypeName&gt;
        is required with proprietary identifiers
    :cvar VALUE_02: ISBN-10 International Standard Book Number, pre-2007
        (10 digits, or 9 digits plus X, without spaces or hyphens) – now
        Deprecated in ONIX for Books, except where providing historical
        information for compatibility with legacy systems. It should
        only be used in relation to products published before 2007 –
        when ISBN-13 superseded it – and should never be used as the
        ONLY identifier (it should always be accompanied by the correct
        GTIN-13 / ISBN-13)
    :cvar VALUE_03: GTIN-13 GS1 Global Trade Item Number, formerly known
        as EAN article number (13 digits, without spaces or hyphens)
    :cvar VALUE_04: UPC UPC product number (12 digits, without spaces or
        hyphens)
    :cvar VALUE_05: ISMN-10 International Standard Music Number,
        pre-2008 (M plus nine digits, without spaces or hyphens) – now
        Deprecated in ONIX for Books, except where providing historical
        information for compatibility with legacy systems. It should
        only be used in relation to products published before 2008 –
        when ISMN-13 superseded it – and should never be used as the
        ONLY identifier (it should always be accompanied by the correct
        GTIN-12 / ISMN-13)
    :cvar VALUE_06: DOI Digital Object Identifier (variable length and
        character set, beginning ‘10.’ and without https://doi.org/ or
        the older http://dx.doi.org/)
    :cvar VALUE_13: LCCN Library of Congress Control Number in
        normalized form (up to 12 characters, alphanumeric)
    :cvar VALUE_14: GTIN-14 GS1 Global Trade Item Number (14 digits,
        without spaces or hyphens)
    :cvar VALUE_15: ISBN-13 International Standard Book Number, from
        2007 (13 digits starting 978 or 9791–9799, without spaces or
        hyphens)
    :cvar VALUE_17: Legal deposit number The number assigned to a
        publication as part of a national legal deposit process
    :cvar VALUE_22: URN Uniform Resource Name: note that in trade
        applications an ISBN must be sent as a GTIN-13 and, where
        required, as an ISBN-13 – it should not be sent as a URN
    :cvar VALUE_23: OCLC number A unique number assigned to a
        bibliographic item by OCLC
    :cvar VALUE_24: Co-publisher’s ISBN-13 An ISBN-13 assigned by a co-
        publisher. The ‘main’ ISBN sent with &lt;ProductIDType&gt; codes
        03 and/or 15 should always be the ISBN that is used for ordering
        from the supplier identified in &lt;SupplyDetail&gt;. However,
        ISBN rules allow a co-published title to carry more than one
        ISBN. The co-publisher should be identified in an instance of
        the &lt;Publisher&gt; composite, with the applicable
        &lt;PublishingRole&gt; code
    :cvar VALUE_25: ISMN-13 International Standard Music Number, from
        2008 (13-digit number starting 9790, without spaces or hyphens)
    :cvar VALUE_26: ISBN-A Actionable ISBN, in fact a special DOI
        incorporating the ISBN-13 within the DOI syntax. Begins
        ‘10.978.’ or ‘10.979.’ and includes a / character between the
        registrant element (publisher prefix) and publication element of
        the ISBN, eg 10.978.000/1234567. Note the ISBN-A should always
        be accompanied by the ISBN itself, using &lt;ProductIDType&gt;
        codes 03 and/or 15
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
    Measure unit.

    :cvar CM: Centimeters Millimeters are the preferred metric unit of
        length
    :cvar GR: Grams
    :cvar IN: Inches (US)
    :cvar KG: Kilograms Grams are the preferred metric unit of weight
    :cvar LB: Pounds (US) Ounces are the preferred US customary unit of
        weight
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
    Product relation.

    :cvar VALUE_00: Unspecified &lt;Product&gt; is related to
        &lt;RelatedProduct&gt; in a way that cannot be specified by
        another code value
    :cvar VALUE_01: Includes &lt;Product&gt; includes
        &lt;RelatedProduct&gt; (inverse of code 02)
    :cvar VALUE_02: Is part of &lt;Product&gt; is part of
        &lt;RelatedProduct&gt;: use for ‘also available as part of’
        (inverse of code 01)
    :cvar VALUE_03: Replaces &lt;Product&gt; replaces, or is new edition
        of, &lt;RelatedProduct&gt; (inverse of code 05)
    :cvar VALUE_04: Has companion product &lt;Product&gt; and
        &lt;RelatedProduct&gt; are companion products, intended to be
        used, or are usable, together (is own inverse). Only for use in
        ONIX 3.0 or later
    :cvar VALUE_05: Replaced by &lt;Product&gt; is replaced by, or has
        new edition, &lt;RelatedProduct&gt; (inverse of code 03)
    :cvar VALUE_06: Alternative format &lt;Product&gt; is available in
        an alternative format as &lt;RelatedProduct&gt; – indicates an
        alternative format of the same content which is or may be
        available (is own inverse)
    :cvar VALUE_07: Has ancillary product &lt;Product&gt; has an
        ancillary or supplementary product &lt;RelatedProduct&gt;
        (inverse of code 08)
    :cvar VALUE_08: Is ancillary to &lt;Product&gt; is ancillary or
        supplementary to &lt;RelatedProduct&gt; (inverse of code 07)
    :cvar VALUE_09: Is remaindered as &lt;Product&gt; is remaindered as
        &lt;RelatedProduct&gt;, when a remainder merchant assigns its
        own identifier to the product (inverse of code 10)
    :cvar VALUE_10: Is remainder of &lt;Product&gt; was originally sold
        as &lt;RelatedProduct&gt;, indicating the publisher’s original
        identifier for a title which is offered as a remainder under a
        different identifier (inverse of code 09)
    :cvar VALUE_11: Is other-language version of &lt;Product&gt; is an
        other-language version of &lt;RelatedProduct&gt; (is own
        inverse)
    :cvar VALUE_12: Publisher’s suggested alternative &lt;Product&gt;
        has a publisher’s suggested alternative &lt;RelatedProduct&gt;,
        which does not, however, carry the same content (cf 05 and 06)
    :cvar VALUE_13: Epublication based on (print product)
        &lt;Product&gt; is an epublication based on printed product
        &lt;RelatedProduct&gt;. The related product is the source of any
        print-equivalent page numbering present in the epublication
        (inverse of code 27)
    :cvar VALUE_16: POD replacement for &lt;Product&gt; is a POD
        replacement for &lt;RelatedProduct&gt;. &lt;RelatedProduct&gt;
        is an out-of-print product replaced by a print-on-demand version
        under a new ISBN (inverse of code 17)
    :cvar VALUE_17: Replaced by POD &lt;Product&gt; is replaced by POD
        &lt;RelatedProduct&gt;. &lt;RelatedProduct&gt; is a print-on-
        demand replacement, under a new ISBN, for an out-of-print
        &lt;Product&gt; (inverse of code 16)
    :cvar VALUE_18: Is special edition of &lt;Product&gt; is a special
        edition of &lt;RelatedProduct&gt;. Used for a special edition
        (de: ‘Sonderausgabe’) with different cover, binding, premium
        content etc – more than ‘alternative format’ – which may be
        available in limited quantity and for a limited time (inverse of
        code 19)
    :cvar VALUE_19: Has special edition &lt;Product&gt; has a special
        edition &lt;RelatedProduct&gt; (inverse of code 18)
    :cvar VALUE_20: Is prebound edition of &lt;Product&gt; is a prebound
        edition of &lt;RelatedProduct&gt; (In the US, a ‘prebound’
        edition is ‘a book that was previously bound and has been
        rebound with a library quality hardcover binding. In almost all
        commercial cases, the book in question began as a paperback.
        This might also be termed ‘re-bound’) (inverse of code 21)
    :cvar VALUE_21: Is original of prebound edition &lt;Product&gt; is
        the regular edition of which &lt;RelatedProduct&gt; is a
        prebound edition (inverse of code 20)
    :cvar VALUE_22: Product by same author &lt;Product&gt; and
        &lt;RelatedProduct&gt; have a common author
    :cvar VALUE_23: Similar product &lt;RelatedProduct&gt; is another
        product that is suggested as similar to &lt;Product&gt; (‘if you
        liked &lt;Product&gt;, you may also like
        &lt;RelatedProduct&gt;’, or vice versa)
    :cvar VALUE_24: Is facsimile of &lt;Product&gt; is a facsimile
        edition of &lt;RelatedProduct&gt; (inverse of code 25)
    :cvar VALUE_25: Is original of facsimile &lt;Product&gt; is the
        original edition from which a facsimile edition
        &lt;RelatedProduct&gt; is taken (inverse of code 24)
    :cvar VALUE_26: Is license for &lt;Product&gt; is a license for a
        digital &lt;RelatedProduct&gt;, traded or supplied separately
    :cvar VALUE_27: Electronic version available as
        &lt;RelatedProduct&gt; is an electronic version of print
        &lt;Product&gt; (inverse of code 13)
    :cvar VALUE_28: Enhanced version available as &lt;RelatedProduct&gt;
        is an ‘enhanced’ version of &lt;Product&gt;, with additional
        content. Typically used to link an enhanced e-book to its
        original ‘unenhanced’ equivalent, but not specifically limited
        to linking e-books – for example, may be used to link
        illustrated and non-illustrated print books. &lt;Product&gt; and
        &lt;RelatedProduct&gt; should share the same &lt;ProductForm&gt;
        (inverse of code 29)
    :cvar VALUE_29: Basic version available as &lt;RelatedProduct&gt; is
        a basic version of &lt;Product&gt;. &lt;Product&gt; and
        &lt;RelatedProduct&gt; should share the same &lt;ProductForm&gt;
        (inverse of code 28)
    :cvar VALUE_30: Product in same collection &lt;RelatedProduct&gt;
        and &lt;Product&gt; are part of the same collection (eg two
        products in same series or set) (is own inverse)
    :cvar VALUE_31: Has alternative in a different market sector
        &lt;RelatedProduct&gt; is an alternative product in another
        sector (of the same geographical market). Indicates an
        alternative that carries the same content, but available to a
        different set of customers, as one or both products are
        retailer-, channel- or market sector-specific (is own inverse)
    :cvar VALUE_32: Has equivalent intended for a different market
        &lt;RelatedProduct&gt; is an equivalent product, often intended
        for another (geographical) market. Indicates an alternative that
        carries essentially the same content, though slightly adapted
        for local circumstances (as opposed to a translation – use code
        11) (is own inverse)
    :cvar VALUE_33: Has alternative intended for different market
        &lt;RelatedProduct&gt; is an alternative product, often intended
        for another (geographical) market. Indicates the content of the
        alternative is identical in all respects (is own inverse)
    :cvar VALUE_34: Cites &lt;Product&gt; cites &lt;RelatedProduct&gt;
        (inverse of code 35)
    :cvar VALUE_35: Is cited by &lt;Product&gt; is the object of a
        citation in &lt;RelatedProduct&gt; (inverse of code 34)
    :cvar VALUE_37: Is signed version of &lt;Product&gt; is a signed
        copy of &lt;RelatedProduct&gt;. Use where signed copies are
        given a distinct product identifier and can be ordered
        separately, but are otherwise identical (inverse of code 38)
    :cvar VALUE_38: Has signed version &lt;Product&gt; is an unsigned
        copy of &lt;RelatedProduct&gt;. Use where signed copies are
        given a distinct product identifier and can be ordered
        separately, but are otherwise identical (inverse of code 37)
    :cvar VALUE_39: Has related student material &lt;Product&gt; is
        intended for teacher use, and the related product is for student
        use
    :cvar VALUE_40: Has related teacher material &lt;Product&gt; is
        intended for student use, and the related product is for teacher
        use
    :cvar VALUE_41: Some content shared with &lt;Product&gt; includes
        some content shared with &lt;RelatedProduct&gt;. Note the shared
        content does not form the whole of either product. Compare with
        the ‘includes’ / ‘is part of’ relationship pair (codes 01 and
        02), where the shared content forms the whole of one of the
        products, and with the ‘alternative format’ relationship (code
        06), where the shared content forms the whole of both products
        (code 41 is own inverse)
    :cvar VALUE_42: Is later edition of first edition &lt;Product&gt; is
        a later edition of &lt;RelatedProduct&gt;, where the related
        product is the first edition
    :cvar VALUE_43: Adapted from &lt;Product&gt; is an adapted
        (dramatized, abridged, novelized etc) version of
        &lt;RelatedProduct&gt; (inverse of code 44). Only for use in
        ONIX 3.0 or later
    :cvar VALUE_44: Adapted as &lt;Product&gt; is the original from
        which &lt;RelatedProduct&gt; is adapted (dramatized etc)
        (inverse of code 43). Only for use in ONIX 3.0 or later
    :cvar VALUE_45: Has linked product offer Purchases of
        &lt;Product&gt; may qualify for one or more copies of
        &lt;RelatedProduct&gt; either free of charge or at a reduced
        price (inverse of code 48). This may be dependent on retailer
        participation, upon price and upon the quantity of the
        &lt;Product&gt; purchased. Only for use in ONIX 3.0 or later
    :cvar VALUE_46: May be substituted by If ordered, &lt;Product&gt;
        may (at the supplier’s discretion) be substituted and the
        &lt;RelatedProduct&gt; supplied instead (inverse of code 47).
        Only for use in ONIX 3.0 or later
    :cvar VALUE_47: May be substituted for If ordered,
        &lt;RelatedProduct&gt; may (at the supplier’s discretion) be
        substituted and the &lt;Product&gt; supplied instead (inverse of
        code 46). Only for use in ONIX 3.0 or later
    :cvar VALUE_48: Is linked product offer Purchases of
        &lt;RelatedProduct&gt; may qualify for one or more copies of
        &lt;Product&gt; either free of charge or at a reduced price
        (inverse of code 45). This may be dependent on retailer
        participation, upon price and upon the quantity of the
        &lt;RelatedProduct&gt; purchased. Only for use in ONIX 3.0 or
        later
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


class List53(Enum):
    """
    Returns conditions code type.

    :cvar VALUE_00: Proprietary As specified in
        &lt;ReturnsCodeTypeName&gt;. Only for use in ONIX 3.0 or later
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


class List55(Enum):
    """
    Date format.

    :cvar VALUE_00: YYYYMMDD Common Era year, month and day (default for
        most dates)
    :cvar VALUE_01: YYYYMM Year and month
    :cvar VALUE_02: YYYYWW Year and week number
    :cvar VALUE_03: YYYYQ Year and quarter (Q = 1, 2, 3, 4, with 1 = Jan
        to Mar)
    :cvar VALUE_04: YYYYS Year and season (S = 1, 2, 3, 4, with 1 =
        ‘Spring’)
    :cvar VALUE_05: YYYY Year (default for some dates)
    :cvar VALUE_06: YYYYMMDDYYYYMMDD Spread of exact dates
    :cvar VALUE_07: YYYYMMYYYYMM Spread of months
    :cvar VALUE_08: YYYYWWYYYYWW Spread of week numbers
    :cvar VALUE_09: YYYYQYYYYQ Spread of quarters
    :cvar VALUE_10: YYYYSYYYYS Spread of seasons
    :cvar VALUE_11: YYYYYYYY Spread of years
    :cvar VALUE_12: Text string For complex, approximate or uncertain
        dates, or dates BCE. Suggested maximum length 100 characters
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
        Arabic script. Suggested maximum length 100 characters
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


class List57(Enum):
    """
    Unpriced item type.

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
    :cvar VALUE_07: Calculated from contents Price calculated as sum of
        individual prices of components listed as Product parts. Only
        for use in ONIX 3.0 or later
    :cvar VALUE_08: Supplier does not supply The supplier does not
        operate, or does not offer this product, in this part of the
        market as indicated by &lt;territory&gt;. Use when other prices
        apply in different parts of the market (eg when the market is
        global, but the particular supplier does not operate outside its
        domestic territory). Use code 04 when the supplier does supply
        but has not set a price for part of the market. Only for use in
        ONIX 3.0 or later
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"


class List58(Enum):
    """
    Price type.

    :cvar VALUE_01: RRP excluding tax Recommended Retail Price,
        excluding any sales tax or value-added tax. Price recommended by
        the publisher or supplier for retail sales to the consumer. Also
        termed the Suggested Retail Price (SRP) or Maximum Suggested
        Retail Price (MSRP) in some countries. The retailer may choose
        to use this recommended price, or may choose to sell to the
        consumer at a lower (or occasionally, a higher) price which is
        termed the Actual Selling Price (ASP) in sales reports. The net
        price charged to the retailer depends on the RRP minus a trade
        discount (which may be customer-specific). Relevant tax detail
        must be calculated by the data recipient
    :cvar VALUE_02: RRP including tax Recommended Retail Price,
        including sales or value-added tax where applicable. The net
        price charged to the retailer depends on the trade discount.
        Sales or value-added tax detail is usually supplied in the
        &lt;Tax&gt; composite
    :cvar VALUE_03: FRP excluding tax Fixed Retail Price, excluding any
        sales or value-added tax, used in countries where retail price
        maintenance applies (by law or via trade agreement) to certain
        products. Price fixed by the publisher or supplier for retail
        sales to the consumer. The retailer must use this price, or may
        vary the price only within certain legally-prescribed limits.
        The net price charged to the retailer depends on the FRP minus a
        customer-specific trade discount. Relevant tax detail must be
        calculated by the data recipient
    :cvar VALUE_04: FRP including tax Fixed Retail Price, including any
        sales or value-added tax where applicable, used in countries
        where retail price maintenance applies (by law or via trade
        agreement) to certain products. The net price charged to the
        retailer depends on the trade discount. Sales or value-added tax
        detail is usually supplied in the &lt;Tax&gt; composite
    :cvar VALUE_05: Supplier’s Net price excluding tax Net or wholesale
        price, excluding any sales or value-added tax. Unit price
        charged by supplier for business-to-business transactions,
        without any direct relationship to the price for retail sales to
        the consumer, but sometimes subject to a further customer-
        specific trade discount based on volume. Relevant tax detail
        must be calculated by the data recipient
    :cvar VALUE_06: Supplier’s Net price excluding tax: rental goods
        Unit price charged by supplier to reseller / rental outlet,
        excluding any sales tax or value-added tax: goods for rental
        (used for video and DVD)
    :cvar VALUE_07: Supplier’s Net price including tax Net or wholesale
        price, including any sales or value-added tax where applicable.
        Unit price charged by supplier for business-to-business
        transactions, without any direct relationship to the price for
        retail sales to the consumer, but sometimes subject to a further
        customer-specific trade discount based on volume. Sales or
        value-added tax detail is usually supplied in the &lt;Tax&gt;
        composite
    :cvar VALUE_08: Supplier’s alternative Net price excluding tax Net
        or wholesale price charged by supplier to a specified class of
        reseller, excluding any sales tax or value-added tax. Relevant
        tax detail must be calculated by the data recipient. (This value
        is for use only in countries, eg Finland, where trade practice
        requires two different Net prices to be listed for different
        classes of resellers, and where national guidelines specify how
        the code should be used)
    :cvar VALUE_09: Supplier’s alternative net price including tax Net
        or wholesale price charged by supplier to a specified class of
        reseller, including any sales tax or value-added tax. Sales or
        value-added tax detail is usually supplied in the &lt;Tax&gt;
        composite. (This value is for use only in countries, eg Finland,
        where trade practice requires two different Net prices to be
        listed for different classes of resellers, and where national
        guidelines specify how the code should be used)
    :cvar VALUE_11: Special sale RRP excluding tax Special sale RRP
        excluding any sales tax or value-added tax. Note ‘special sales’
        are sales where terms and conditions are different from normal
        trade sales, when for example products that are normally sold on
        a sale-or-return basis are sold on firm-sale terms, where a
        particular product is tailored for a specific retail outlet
        (often termed a ‘premium’ product), or where other specific
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
    :cvar VALUE_35: Nominal gratis copy value for customs purposes,
        excluding tax Nominal value of gratis copies (eg review, sample
        or evaluation copies) for international customs declarations
        only, when a ‘free of charge’ price cannot be used. Only for use
        in ONIX 3.0 or later
    :cvar VALUE_36: Nominal value for claims purposes, excluding tax
        Nominal value of copies for claims purposes only (eg to account
        for copies lost during distribution). Only for use in ONIX 3.0
        or later
    :cvar VALUE_37: Nominal value for customs purposes, excluding tax
        Nominal value of copies (Declared Unit Value) for international
        customs declarations only. Only for use in ONIX 3.0 or later
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
    VALUE_35 = "35"
    VALUE_36 = "36"
    VALUE_37 = "37"
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
        2.1) or in the &lt;PriceDate&gt; composite (ONIX 3.0 or later)
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
        &lt;PriceDate&gt; composite in ONIX 3.0 or later), and should
        also be accompanied by a ‘normal’ price
    :cvar VALUE_08: Promotional offer price Temporary ‘Special offer’
        price. Must be accompanied by &lt;PriceEffectiveFrom&gt; and
        &lt;PriceEffectiveUntil&gt; dates (or equivalent
        &lt;PriceDate&gt; composites in ONIX 3.0 or later), and may also
        be accompanied by a ‘normal’ price
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
        organizations or services offering consumers subscription access
        to a library of books
    :cvar VALUE_14: School library price Price for primary and secondary
        education
    :cvar VALUE_15: Academic library price Price for higher education
        and scholarly institutions
    :cvar VALUE_16: Public library price
    :cvar VALUE_17: Introductory price Initial ‘Introductory offer’
        price. Must be accompanied by an Effective until date in a
        &lt;PriceDate&gt; composite in ONIX 3, and may also be
        accompanied by a ‘normal’ price valid after the introductory
        offer expires (Fr. Prix de lancement). Only for use in ONIX 3.0
        or later
    :cvar VALUE_18: Consortial price Price for library consortia. Only
        for use in ONIX 3.0 or later
    :cvar VALUE_19: Education price for alternative provision (fr:
        « prix pour l’education specialisée ») Only for use in ONIX 3.0
        or later
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


class List60(Enum):
    """
    Unit of pricing.

    :cvar VALUE_00: Per copy of whole product Default. Note where the
        product is a pack of multiple copies, the price is per multi-
        item product, not per individual copy within the pack
    :cvar VALUE_01: Per page for printed loose-leaf content only
    """

    VALUE_00 = "00"
    VALUE_01 = "01"


class List61(Enum):
    """
    Price status.

    :cvar VALUE_00: Unspecified Default
    :cvar VALUE_01: Provisional
    :cvar VALUE_02: Confirmed
    """

    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"


class List62(Enum):
    """
    Tax rate type.

    :cvar H: Higher rate Specifies that tax is applied at a higher rate
        than standard
    :cvar P: Tax paid at source (Italy) Under Italian tax rules, VAT on
        books may be paid at source by the publisher, and subsequent
        transactions through the supply chain are tax-exempt
    :cvar R: Lower rate Specifies that tax is applied at a lower rate
        than standard. In the EU, use code R for ‘Reduced rates’, and
        for rates lower than 5%, use code T (‘Super-reduced’) or Z
        (Zero-rated)
    :cvar S: Standard rate
    :cvar T: Super-low rate Specifies that tax is applied at a rate
        lower than the Lower rate(s). In the EU, use code T for ‘Super-
        reduced rates’, and for Reduced rates (5% or above) use code R
        (Lower rate). Only for use in ONIX 3.0 or later
    :cvar Z: Zero-rated
    """

    H = "H"
    P = "P"
    R = "R"
    S = "S"
    T = "T"
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
        or later must not be sent
    :cvar VALUE_02: Forthcoming Not yet published; must be accompanied
        by the expected date in &lt;PublicationDate&gt; in ONIX 2.1, or
        its equivalent in the &lt;PublishingDate&gt; composite in ONIX
        3.0 or later
    :cvar VALUE_03: Postponed indefinitely The product was announced,
        and subsequently postponed with no expected publication date;
        the &lt;PublicationDate&gt; element in ONIX 2.1, or its
        equivalent as a &lt;PublishingDate&gt; composite in ONIX 3.0 or
        later, must not be sent
    :cvar VALUE_04: Active The product was published, and is still
        active in the sense that the publisher will accept orders for
        it, though it may or may not be immediately available, for which
        see &lt;SupplyDetail&gt;
    :cvar VALUE_05: No longer our product Ownership of the product has
        been transferred to another publisher (with details of acquiring
        publisher if possible in PR.19 (ONIX 2.1) OR P.19 (ONIX 3.0 or
        later))
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
        published and active but, as a publishing decision, its
        constituent parts are not sold separately – only in an assembly
        or as part of a pack, eg with Product composition code 01. Also
        use with Product composition codes 30, 31 where depending on
        product composition and pricing, items in the pack may or may
        not be saleable separately at retail
    :cvar VALUE_15: Recalled Recalled for reasons of consumer safety
    :cvar VALUE_16: Temporarily withdrawn from sale Withdrawn
        temporarily, typically for quality or technical reasons. In ONIX
        3.0 or later, must be accompanied by expected availability date
        coded ‘22’ within the &lt;PublishingDate&gt; composite, except
        in exceptional circumstances where no date is known
    :cvar VALUE_17: Permanently withdrawn from sale Withdrawn
        permanently from sale in all markets. Effectively synonymous
        with ‘Out of print’ (code 07), but specific to downloadable and
        online digital products (where no ‘stock’ would remain in the
        supply chain)
    :cvar VALUE_18: Active, but not sold as set The various constituent
        parts of a product are published and active but, as a publishing
        decision, they are not sold together as a single product – eg
        with Product composition code 11 – and are only available as a
        number of individual items. Only for use in ONIX 3.0 or later
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
    VALUE_18 = "18"


class List65(Enum):
    """
    Product availability.

    :cvar VALUE_01: Cancelled Product was announced, and subsequently
        abandoned by the publisher. No expected availability date should
        be included in &lt;SupplyDate&gt;
    :cvar VALUE_09: Not yet available, postponed indefinitely Not yet
        available from the supplier, and the publisher indicates that it
        has been postponed indefinitely. Should be used in preference to
        code 10 where the publisher has indicated that a previously-
        announced publication date is no longer correct, and no new date
        has yet been announced. No expected avalabilty date should be
        included in &lt;SupplyDate&gt;. Only for use in ONIX 3.0 or
        later
    :cvar VALUE_10: Not yet available Not yet available (requires
        expected date, either as &lt;ExpectedShipDate&gt; (ONIX 2.1) or
        as &lt;SupplyDate&gt; with &lt;SupplyDateRole&gt; coded ‘08’
        (ONIX 3.0 or later), except in exceptional circumstances where
        no date is known)
    :cvar VALUE_11: Awaiting stock Not yet available, but will be a
        stock item when available (requires expected date, either as
        &lt;ExpectedShipDate&gt; (ONIX 2.1) or as &lt;SupplyDate&gt;
        with &lt;SupplyDateRole&gt; coded ‘08’ (ONIX 3.0 or later),
        except in exceptional circumstances where no date is known).
        Used particularly for imports which have been published in the
        country of origin but have not yet arrived in the importing
        country
    :cvar VALUE_12: Not yet available, will be POD Not yet available, to
        be published as print-on-demand only (requires expected date,
        either as &lt;ExpectedShipDate&gt; (ONIX 2.1) or as
        &lt;SupplyDate&gt; with &lt;SupplyDateRole&gt; coded ‘08’ (ONIX
        3.0 or later), except in exceptional circumstances where no date
        is known). May apply either to a POD successor to an existing
        conventional edition, when the successor will be published under
        a different ISBN (normally because different trade terms apply);
        or to a title that is being published as a POD original
    :cvar VALUE_20: Available Available from us (form of availability
        unspecified)
    :cvar VALUE_21: In stock Available from us as a stock item
    :cvar VALUE_22: To order Available from the supplier as a non-stock
        item, by special order. Where possible, an &lt;OrderTime&gt;
        should be included
    :cvar VALUE_23: POD Available from the supplier by print-on-demand.
        If the fulfillment delay is likely to be more than 24 hours, an
        &lt;OrderTime&gt; should be included
    :cvar VALUE_30: Temporarily unavailable Temporarily unavailable:
        temporarily unavailable from us (reason unspecified) (requires
        expected date, either as &lt;ExpectedShipDate&gt; (ONIX 2.1) or
        as &lt;SupplyDate&gt; with &lt;SupplyDateRole&gt; coded ‘08’
        (ONIX 3.0 or later), except in exceptional circumstances where
        no date is known)
    :cvar VALUE_31: Out of stock Stock item, temporarily out of stock
        (requires expected date, either as &lt;ExpectedShipDate&gt;
        (ONIX 2.1) or as &lt;SupplyDate&gt; with &lt;SupplyDateRole&gt;
        coded ‘08’ (ONIX 3.0 or later), except in exceptional
        circumstances where no date is known)
    :cvar VALUE_32: Reprinting Temporarily unavailable, reprinting
        (requires expected date, either as &lt;ExpectedShipDate&gt;
        (ONIX 2.1) or as &lt;SupplyDate&gt; with &lt;SupplyDateRole&gt;
        coded ‘08’ (ONIX 3.0 or later), except in exceptional
        circumstances where no date is known)
    :cvar VALUE_33: Awaiting reissue Temporarily unavailable, awaiting
        reissue (requires expected date, either as
        &lt;ExpectedShipDate&gt; (ONIX 2.1) or as &lt;SupplyDate&gt;
        with &lt;SupplyDateRole&gt; coded ‘08’ (ONIX 3.0 or later),
        except in exceptional circumstances where no date is known)
    :cvar VALUE_34: Temporarily withdrawn from sale May be for quality
        or technical reasons. Requires expected availability date,
        either as &lt;ExpectedShipDate&gt; (ONIX 2.1) or as
        &lt;SupplyDate&gt; with &lt;SupplyDateRole&gt; coded ‘08’ (ONIX
        3.0 or later), except in exceptional circumstances where no date
        is known
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
        or trade pack (identify set or pack in &lt;RelatedProduct&gt;
        using code 02). Individual copies of the product are not
        available from the supplier, but packs of copies are available,
        or individual copies of the product may typically be sold at
        retail
    :cvar VALUE_46: Withdrawn from sale May be for legal reasons or to
        avoid giving offence
    :cvar VALUE_47: Remaindered Remaindered
    :cvar VALUE_48: Not available, replaced by POD Out of print, but a
        print-on-demand edition is or will be available under a
        different ISBN. Use only when the POD successor has a different
        ISBN, normally because different trade terms apply
    :cvar VALUE_49: Recalled Recalled for reasons of consumer safety
    :cvar VALUE_50: Not sold as set Must be bought as individual items
        (identify contents of set or oack in &lt;RelatedProduct&lt;
        using code 01. Used when a collection that is not sold as a set
        nevertheless has its own ONIX record
    :cvar VALUE_51: Not available, publisher indicates OP This product
        is unavailable from the supplier, no successor product or
        alternative format is available or planned. Use this code only
        when the publisher has indicated the product is out of print
    :cvar VALUE_52: Not available, publisher no longer sells product in
        this market This product is unavailable from the supplier in
        this market, no successor product or alternative format is
        available or planned. Use this code when a publisher has
        indicated the product is permanently unavailable (in this
        market) while remaining available elsewhere
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
    VALUE_09 = "09"
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


class List68(Enum):
    """
    Market publishing status.

    :cvar VALUE_00: Unspecified Status is not specified (as distinct
        from unknown): the default if the &lt;MarketPublishingStatus&gt;
        element is not sent
    :cvar VALUE_01: Cancelled The product was announced for publication
        in this market, and subsequently abandoned. A market publication
        date must not be sent
    :cvar VALUE_02: Forthcoming Not yet published in this market, should
        be accompanied by expected local publication date
    :cvar VALUE_03: Postponed indefinitely The product was announced for
        publication in this market, and subsequently postponed with no
        expected local publication date. A market publication date must
        not be sent
    :cvar VALUE_04: Active The product was published in this market, and
        is still active in the sense that the publisher will accept
        orders for it, though it may or may not be immediately
        available, for which see &lt;SupplyDetail&gt;
    :cvar VALUE_05: No longer our product Responsibility for the product
        in this market has been transferred elsewhere (with details of
        acquiring publisher representative in this market if possible in
        PR.25 (in ONIX 2.1) OR P.25 (in ONIX 3.0 or later))
    :cvar VALUE_06: Out of stock indefinitely The product was active in
        this market, but is now inactive in the sense that (a) the
        publisher representative (local publisher or sales agent) cannot
        fulfill orders for it, though stock may still be available
        elsewhere in the supply chain, and (b) there are no current
        plans to bring it back into stock in this market. Code 06 does
        not specifically imply that returns are or are not still
        accepted
    :cvar VALUE_07: Out of print The product was active in this market,
        but is now permanently inactive in this market in the sense that
        (a) the publisher representative (local publisher or sales
        agent) will not accept orders for it, though stock may still be
        available elsewhere in the supply chain, and (b) the product
        will not be made available again in this market under the same
        ISBN. Code 07 normally implies that the publisher will not
        accept returns beyond a specified date
    :cvar VALUE_08: Inactive The product was active in this market, but
        is now permanently or indefinitely inactive in the sense that
        the publisher representative (local publisher or sales agent)
        will not accept orders for it, though stock may still be
        available elsewhere in the supply chain. Code 08 covers both of
        codes 06 and 07, and may be used where the distinction between
        those values is either unnecessary or meaningless
    :cvar VALUE_09: Unknown The sender of the ONIX record does not know
        the current publishing status in this market
    :cvar VALUE_10: Remaindered The product is no longer available in
        this market from the publisher representative (local publisher
        or sales agent), under the current ISBN, at the current price.
        It may be available to be traded through another channel,
        usually at a reduced price
    :cvar VALUE_11: Withdrawn from sale Withdrawn from sale in this
        market, typically for legal reasons or to avoid giving offence
    :cvar VALUE_12: Not available in this market Either no rights are
        held for the product in this market, or for other reasons the
        publisher has decided not to make it available in this market
    :cvar VALUE_13: Active, but not sold separately The product is
        published and active in this market but, as a publishing
        decision, its constituent parts are not sold separately – only
        in an assembly or as part of a pack, eg with Product composition
        code 01. Also use with Product composition codes 30, 31 where
        depending on product composition and pricing, items in the pack
        may be saleable separately at retail
    :cvar VALUE_14: Active, with market restrictions The product is
        published in this market and active, but is not available to all
        customer types, typically because the market is split between
        exclusive sales agents for different market segments. In ONIX
        2.1, should be accompanied by a free-text statement in
        &lt;MarketRestrictionDetail&gt; describing the nature of the
        restriction. In ONIX 3.0 or later, the &lt;SalesRestriction&gt;
        composite in Group P.24 should be used
    :cvar VALUE_15: Recalled Recalled in this market for reasons of
        consumer safety
    :cvar VALUE_16: Temporarily withdrawn from sale Temporarily
        withdrawn from sale in this market, typically for quality or
        technical reasons. In ONIX 3.0 or later, must be accompanied by
        expected availability date coded ‘22’ within the
        &lt;MarketDate&gt; composite, except in exceptional
        circumstances where no date is known
    :cvar VALUE_17: Permanently withdrawn from sale Withdrawn
        permanently from sale in this market. Effectively synonymous
        with ‘Out of print’ (code 07), but specific to downloadable and
        online digital products (where no ‘stock’ would remain in the
        supply chain). Only for use in ONIX 3.0 or later
    :cvar VALUE_18: Active, but not sold as set The various constituent
        parts of a product are published and active in this market but,
        as a publishing decision, they are not sold together as a single
        product – eg with Product composition code 11 – and are only
        available as a number of individual items. Only for use in ONIX
        3.0 or later
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


class List69(Enum):
    """
    Agent role.

    :cvar VALUE_05: Exclusive sales agent Publisher’s exclusive sales
        agent in a specified territory
    :cvar VALUE_06: Non-exclusive sales agent Publisher’s non-exclusive
        sales agent in a specified territory
    :cvar VALUE_07: Local publisher Publisher for a specified territory
    :cvar VALUE_08: Sales agent Publisher’s sales agent in a specific
        territory. Use only where exclusive / non-exclusive status is
        not known. Prefer 05 or 06 as appropriate, where possible
    """

    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"


class List70(Enum):
    """
    Stock quantity code type.

    :cvar VALUE_01: Proprietary As specified in
        &lt;StockQuantityCodeTypeName&gt;
    :cvar VALUE_02: APA stock quantity code Code scheme defined by the
        Australian Publishers Association. Deprecated
    """

    VALUE_01 = "01"
    VALUE_02 = "02"


class List71(Enum):
    """
    Sales restriction type.

    :cvar VALUE_00: Unspecified – see text Restriction must be described
        in &lt;SalesRestrictionDetail&gt; (ONIX 2.1) or
        &lt;SalesRestrictionNote&gt; (ONIX 3.0 or later)
    :cvar VALUE_01: Retailer exclusive / own brand Sales rights (or
        market distribution rights) apply to sales through designated
        retailer(s), which must be identified or named in an instance of
        the &lt;SalesOutlet&gt; composite. Use only when it is not
        possible to assign the more explicit codes 04 or 05
    :cvar VALUE_02: Through office supplies outlets only Sales rights
        (or market distribution rights) apply to sales though office
        supplies channels. Specific outlet(s) may be identified or named
        in an instance of the &lt;SalesOutlet&gt; composite
    :cvar VALUE_03: Internal publisher use only: do not list For an ISBN
        that is assigned for a publisher’s internal purposes
    :cvar VALUE_04: Retailer exclusive Sales rights (or market
        distribution rights) apply to sales (under the publisher’s brand
        / imprint) through the designated retailer(s), which must be
        identified or named in an instance of the &lt;SalesOutlet&gt;
        composite
    :cvar VALUE_05: Retailer own brand Sales rights (or market
        distribution rights) apply to sales (under the retailer’s own
        brand / imprint) through the designated retailer(s), which must
        be identified or named in an instance of the &lt;SalesOutlet&gt;
        composite
    :cvar VALUE_06: To libraries only Sales rights (or market
        distribution rights) apply to supplies to libraries
    :cvar VALUE_07: To schools only Sales rights (or market distribution
        rights) apply to supplies to schools
    :cvar VALUE_08: Indiziert Indexed for the German market – in
        Deutschland indiziert
    :cvar VALUE_09: Except to libraries Sales rights (or market
        distribution rights) apply to supplies other than to libraries
    :cvar VALUE_10: Through news outlets only Sales rights (or market
        distribution rights) apply to sales though news outlet channels
        (newsstands / newsagents)
    :cvar VALUE_11: Retailer exception Sales rights (or market
        distribution rights) apply to sales other than through
        designated retailer(s), which must be identified or named in the
        &lt;SalesOutlet&gt; composite
    :cvar VALUE_12: Except to subscription services Sales rights (or
        market distribution rights) apply to supplies other than to
        organizations or services offering consumers subscription access
        to a catalog of books
    :cvar VALUE_13: To subscription services only Sales rights (or
        market distribution rights) apply to supplies to organizations
        or services offering consumers subscription access to a catalog
        of books
    :cvar VALUE_14: Except through online retail Sales rights (or market
        distribution rights) apply to sales other than through online
        retail channels
    :cvar VALUE_15: Through online retail only Sales rights (or market
        distribution rights) apply to sales through online retail
        channels
    :cvar VALUE_16: Except to schools Sales rights (or market
        distribution rights) apply to supplies other than to schools.
        Only for use in ONIX 3.0 or later
    :cvar VALUE_17: Through Inventoryless POD POD copies may be
        manufactured at any time, either to fulfill a customer order
        immediately or to replace a minimal stockholding (ie near-
        inventoryless). Only for use in ONIX 3.0 or later
    :cvar VALUE_18: Through Stock Protection POD POD copies may be
        manfactured only to fulfill a customer order immediately while
        out of stock and awaiting delivery of further stock from the
        supplier. Only for use in ONIX 3.0 or later
    :cvar VALUE_19: Except through POD Not eligible for POD. Only for
        use in ONIX 3.0 or later
    :cvar VALUE_20: Except to some subscription services Sales rights
        (or market distribution rights) apply to all supplies through
        retailers, and to the designated subscription services, which
        must be identified or named in an instance of the
        &lt;SalesOutlet&gt; composite. Only for use in ONIX 3.0 or later
    :cvar VALUE_21: Subscription service exclusive Sales rights (or
        market distribution rights) apply to supplies to the designated
        subscription service(s), which must be identified or named in an
        instance of the &lt;SalesOutlet&gt; composite. Only for use in
        ONIX 3.0 or later
    :cvar VALUE_99: No restrictions on sales Positive indication that no
        sales restrictions apply, for example to indicate the product
        may be sold both online and in bricks-and mortar retail, or to
        subscription services and non-subscription customers. Only for
        use in ONIX 3.0 or later
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
    VALUE_99 = "99"


class List72(Enum):
    """
    Thesis type.

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
        &lt;Website&gt; composite (typically within &lt;Publisher&gt; or
        &lt;SupplyDetail&gt;) when sending a link to a webpage at which
        a digital product is available for download and/or online access
    :cvar VALUE_30: Web page for other commentary / discussion For
        example a subscribable podcast hosting site, social media
        message, newsletter issue, other commentary
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
        For example, a Facebook, Instagram, Youtube, Pinterest, Tiktok
        (including Booktok), Twitter (latterly, X) or similar URL for
        the product or work
    :cvar VALUE_42: Author’s social networking URL For example, a
        Facebook, Instagram, Youtube, Pinterest, Tiktok (including
        Booktok), Twitter (latterly, X) or similar page
    :cvar VALUE_43: Publisher’s social networking URL For example, a
        Facebook, Instagram, Youtube, Pinterest, Tiktok (including
        Booktok), Twitter (latterly, X) or similar page
    :cvar VALUE_44: Social networking URL for specific article, chapter
        or content item For example, a Facebook, Instagram, Youtube,
        Pinterest, Tiktok (including Booktok), Twitter (latterly, X) or
        similar page. Use only in the context of a specific content item
        (eg within &lt;ContentItem&gt;)
    :cvar VALUE_45: Publisher’s or third party website for permissions
        requests For example, a service offering click-through licensing
        of extracts
    :cvar VALUE_46: Publisher’s or third party website for privacy
        statement For example, a page providing details related to GDPR.
        Only for use in ONIX 3.0 or later
    :cvar VALUE_47: Publisher’s website for digital preservation The URL
        of the publisher’s preservation service, or a more specific URL
        for access to its preservation metadata, to provide confirmation
        of the preservation status of the product.
        &lt;WebsiteDescription&gt; may contain the name of the service.
        Only for use in ONIX 3.0 or later
    :cvar VALUE_48: Third-party website for digital preservation The URL
        of the preservation service (eg https://clockss.org), or a more
        specific URL for access to its preservation metadata, to provide
        confirmation of the preservation status of the product.
        &lt;WebsiteDescription&gt; may contain the name of the service.
        Only for use in ONIX 3.0 or later
    :cvar VALUE_49: Product website for environmental responsibility
        statement The URL of a web page describing the environmental and
        sustainability policy, or carbon neutrality status, that applies
        to the specific product. Only for use in ONIX 3.0 or later
    :cvar VALUE_50: Organization’s website for environmental
        responsibility statement The URL of a web page describing the
        environmental and sustainability policies, carbon neutrality
        status, etc of the organization (publisher, supplier etc). For
        environmental sustainability of the product itself, see List 79.
        Only for use in ONIX 3.0 or later
    :cvar VALUE_51: Legal deposit website for digital preservation The
        URL of a digital legal deposit service (eg
        https://www.legaldeposit.org.uk), or a more specific URL for
        access to its preservation metadata, to provide confirmation of
        the digital legal deposit status of the product.
        &lt;WebsiteDescription&gt; may contain the name of the service.
        Only for use in ONIX 3.0 or later
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
    VALUE_46 = "46"
    VALUE_47 = "47"
    VALUE_48 = "48"
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_51 = "51"


class List74(Enum):
    """
    Language – based on ISO 639-2/B.

    :cvar ABK: Abkhazian
    :cvar ACE: Achinese
    :cvar ACH: Acoli
    :cvar ADA: Adangme
    :cvar ADY: Adygei; Adyghe (West Circassian)
    :cvar AAR: Afar
    :cvar AFH: Afrihili Artificial language
    :cvar AFR: Afrikaans
    :cvar AFA: Afro-Asiatic languages Collective name
    :cvar AIN: Ainu
    :cvar AKA: Akan Macrolanguage. See also fat (Fanti), twi (Twi)
    :cvar AKK: Akkadian
    :cvar ALB: Albanian Macrolanguage
    :cvar ALE: Aleut
    :cvar ALG: Algonquian languages Collective name
    :cvar ALQ: Algonquin Alginkin. ONIX local code, equivalent to alq in
        ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar TUT: Altaic languages Collective name
    :cvar AMH: Amharic
    :cvar ANP: Angika
    :cvar APA: Apache languages Collective name
    :cvar ARA: Arabic Macrolanguage
    :cvar ARG: Aragonese
    :cvar QAR: Aranés ONIX local code, distinct dialect of Occitan (not
        distinguished from oci by ISO 639-3)
    :cvar ARP: Arapaho
    :cvar ARW: Arawak
    :cvar ARM: Armenian
    :cvar RUP: Aromanian; Arumanian; Macedo-Romanian
    :cvar ART: Artificial languages Collective name
    :cvar ASM: Assamese
    :cvar AST: Asturian; Bable; Leonese; Asturleonese
    :cvar ATH: Athapascan languages Collective name
    :cvar ATJ: Atikamekw ONIX local code, equivalent to atj in ISO
        639-3. Only for use in ONIX 3.0 or later
    :cvar AUS: Australian languages Collective name
    :cvar AAV: Austro-Asiatic languages Collective name. ONIX local
        code, equivalent of aav in ISO 639-5. Only for use in ONIX 3.0
        or later
    :cvar MAP: Austronesian languages Collective name
    :cvar AVA: Avaric
    :cvar AVE: Avestan
    :cvar AWA: Awadhi
    :cvar AYM: Aymara Macrolanguage
    :cvar AZE: Azerbaijani Macrolanguage
    :cvar BAN: Balinese
    :cvar BAT: Baltic languages Collective name
    :cvar BAL: Baluchi Macrolanguage
    :cvar BAM: Bambara
    :cvar BAI: Bamileke languages Collective name
    :cvar BAD: Banda languages Collective name
    :cvar BNT: Bantu languages Collective name
    :cvar BAS: Basa
    :cvar BAK: Bashkir
    :cvar BAQ: Basque
    :cvar BTK: Batak languages Collective name
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
    :cvar BYN: Blin; Bilin
    :cvar ZBL: Blissymbols; Blissymbolics; Bliss Artificial language
    :cvar BRX: Bodo (India) Boro. ONIX local code, equivalent to brx in
        ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar BOS: Bosnian
    :cvar BRA: Braj
    :cvar BRE: Breton
    :cvar BUG: Buginese
    :cvar BUL: Bulgarian
    :cvar BUM: Bulu (Cameroon) ONIX local code, equivalent to bum in ISO
        639-3. Only for use in ONIX 3.0 or later
    :cvar BUA: Buriat Macrolanguage
    :cvar BUR: Burmese
    :cvar CAD: Caddo
    :cvar SRO: Campidanese ONIX local code for Sardinian dialect,
        equivalent to sro in ISO 639-3. Only for use in ONIX 3.0 or
        later
    :cvar YUE: Cantonese ONIX local code, equivalent to yue in ISO 639-3
    :cvar CAT: Catalan See also qav (Valencian)
    :cvar CAU: Caucasian languages Collective name
    :cvar CAY: Cayuga ONIX local code, equivalent to cay in ISO 639-3.
        Only for use in ONIX 3.0 or later
    :cvar CEB: Cebuano
    :cvar CEL: Celtic languages Collective name
    :cvar CAI: Central American Indian languages Collective name
    :cvar TZM: Central Atlas Tamazight ONIX local code, equivalent to
        tzm in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar KHM: Central Khmer
    :cvar CKB: Central Kurdish (Sorani) ONIX local code, equivalent to
        ckb in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar CHG: Chagatai
    :cvar CMC: Chamic languages Collective name
    :cvar CHA: Chamorro
    :cvar CHE: Chechen
    :cvar CHR: Cherokee
    :cvar CHY: Cheyenne
    :cvar CHB: Chibcha
    :cvar NYA: Chichewa; Chewa; Nyanja
    :cvar CIC: Chickasaw ONIX local code, equivalent to cic in ISO
        639-3. Only for use in ONIX 3.0 or later
    :cvar CHI: Chinese Macrolanguage. See also cmn (Mandarin), yue
        (Cantonese)
    :cvar CHN: Chinook jargon
    :cvar CHP: Chipewyan; Dene Suline
    :cvar CHO: Choctaw
    :cvar CHU: Church Slavic; Old Slavonic; Church Slavonic; Old
        Bulgarian; Old Church Slavonic
    :cvar CHK: Chuukese (Truk)
    :cvar CHV: Chuvash
    :cvar NWC: Classical Newari; Old Newari; Classical Nepal Bhasa
    :cvar SYC: Classical Syriac
    :cvar COP: Coptic
    :cvar COR: Cornish
    :cvar COS: Corsican
    :cvar CRE: Cree Macrolanguage. See also crj (Southern East Cree),
        crk (plains Cree), crl (Northern East Cree), crm (Moose Cree),
        csw (Swampy Cree), cwd (Woods Cree)
    :cvar MUS: Creek Seminole
    :cvar CRP: Creoles and pidgins Collective name
    :cvar CPE: Creoles and pidgins, English-based Collective name
    :cvar CPF: Creoles and pidgins, French-based Collective name
    :cvar CPP: Creoles and pidgins, Portuguese-based Collective name
    :cvar CRH: Crimean Turkish; Crimean Tatar
    :cvar HRV: Croatian
    :cvar SCR: Croatian Deprecated – use hrv
    :cvar CUS: Cushitic languages Collective name
    :cvar CZE: Czech
    :cvar DAK: Dakota
    :cvar DAN: Danish
    :cvar DAR: Dargwa
    :cvar PRS: Dari; Afghan Persian ONIX local code, equivalent to prs
        in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar DEL: Delaware Macrolanguage
    :cvar DIN: Dinka Macrolanguage
    :cvar DIV: Divehi; Dhivehi; Maldivian
    :cvar DOI: Dogri Macrolanguage
    :cvar DGR: Dogrib
    :cvar DRA: Dravidian languages Collective name
    :cvar DUA: Duala
    :cvar DUM: Dutch, Middle (ca. 1050-1350)
    :cvar DUT: Dutch; Flemish
    :cvar DYU: Dyula
    :cvar DZO: Dzongkha
    :cvar IKE: Eastern Canadian Inuktitut ONIX local code, equivalent to
        ike in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar FRS: Eastern Frisian
    :cvar EFI: Efik
    :cvar EGY: Egyptian (Ancient)
    :cvar EKA: Ekajuk
    :cvar ELX: Elamite
    :cvar EGL: Emilian ONIX local code for Italian dialect, equivalent
        to egl in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar ENG: English
    :cvar ENM: English, Middle (1100-1500)
    :cvar ANG: English, Old (ca. 450-1100)
    :cvar MYV: Erzya
    :cvar ESX: Eskaleut languages Inuit-Yupik-Unangan languages.
        Collective name. ONIX local code, equivalent of esx in ISO
        639-5. Only for use in ONIX 3.0 or later
    :cvar EPO: Esperanto Artificial language
    :cvar EST: Estonian Macrolanguage
    :cvar GEZ: Ethiopic (Ge’ez)
    :cvar EWE: Ewe
    :cvar EWO: Ewondo
    :cvar FAN: Fang
    :cvar FAT: Fanti
    :cvar FAO: Faroese
    :cvar FIJ: Fijian
    :cvar FIL: Filipino; Pilipino
    :cvar FIN: Finnish
    :cvar FIU: Finno-Ugrian languages Collective name
    :cvar FON: Fon
    :cvar FRE: French
    :cvar FRM: French, Middle (ca. 1400-1600)
    :cvar FRO: French, Old (ca. 842-1400) See also qgl (Gallo)
    :cvar FUR: Friulian
    :cvar FUL: Fulah Macrolanguage
    :cvar GAA: Gã
    :cvar CAR: Galibi Carib
    :cvar GLG: Galician
    :cvar QGL: Gallo ONIX local code, distinct variant of langue d’oïl
        (old northern French), not distinguished from fro, or from frm,
        fre, nrf by ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar SDN: Gallurese ONIX local code for Sardinian dialect,
        equivalent to sdn in ISO 639-3. Only for use in ONIX 3.0 or
        later
    :cvar LUG: Ganda
    :cvar GRT: Garo ONIX local code, equivalent to grt in ISO 639-3.
        Only for use in ONIX 3.0 or later
    :cvar GAY: Gayo
    :cvar GBA: Gbaya Macrolanguage
    :cvar GEO: Georgian
    :cvar GER: German
    :cvar GMH: German, Middle High (ca. 1050-1500)
    :cvar GOH: German, Old High (ca. 750-1050)
    :cvar GEM: Germanic languages Collective name
    :cvar GIL: Gilbertese
    :cvar GIT: Gitxsan ONIX local code, equivalent to git in ISO 639-3.
        Only for use in ONIX 3.0 or later
    :cvar GON: Gondi Macrolanguage
    :cvar GOR: Gorontalo
    :cvar GOT: Gothic
    :cvar GRB: Grebo Macrolanguage
    :cvar GRC: Greek, Ancient (to 1453)
    :cvar GRE: Greek, Modern (1453-)
    :cvar GRN: Guarani Macrolanguage
    :cvar NRF: Guernésiais, Jèrriais ONIX local code, equivalent to nrf
        in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar GUJ: Gujarati
    :cvar GWI: Gwich’in
    :cvar HAI: Haida Macrolanguage
    :cvar HAT: Haitian; Haitian Creole
    :cvar HAU: Hausa
    :cvar HAW: Hawaiian
    :cvar HEB: Hebrew
    :cvar HER: Herero
    :cvar HIL: Hiligaynon
    :cvar HIM: Himachali languages; Western Pahari languages Collective
        name
    :cvar HIN: Hindi
    :cvar HMO: Hiri Motu
    :cvar HIT: Hittite
    :cvar HMX: Hmong-Mien languages Collective name. ONIX local code,
        equivalent of hmx in ISO 639-5. Only for use in ONIX 3.0 or
        later
    :cvar HMN: Hmong; Mong Macrolanguage
    :cvar HOP: Hopi ONIX local code, equivalent to hop in ISO 639-3.
        Only for use in ONIX 3.0 or later
    :cvar HUN: Hungarian
    :cvar HUP: Hupa
    :cvar IBA: Iban
    :cvar ICE: Icelandic
    :cvar IDO: Ido Artificial language
    :cvar IBO: Igbo
    :cvar IJO: Ijo languages Collective name
    :cvar ILO: Iloko
    :cvar SMN: Inari Sami
    :cvar INC: Indic languages Collective name
    :cvar INE: Indo-European languages Collective name
    :cvar IND: Indonesian
    :cvar INH: Ingush
    :cvar MOE: Innu, Montagnais ONIX local code, equivalent to moe in
        ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar INA: Interlingua (International Auxiliary Language
        Association) Artificial language
    :cvar ILE: Interlingue; Occidental Artificial language
    :cvar IKT: Inuinnaqtun Western Canadian Inuktitut. ONIX local code,
        equivalent to ikt in ISO 639-3. Only for use in ONIX 3.0 or
        later
    :cvar IKU: Inuktitut Macrolanguage. See also ike (Eastern Canadian
        Inuktitut), ikt (Inuinnaqtun)
    :cvar IPK: Inupiaq Macrolanguage
    :cvar QIV: Inuvialuktun ONIX local code, distinct dialect of
        Inuktitut (not distinguished from iku, ike, ikt by ISO 639-3).
        Only for use in ONIX 3.0 or later
    :cvar IRA: Iranian languages Collective name
    :cvar PES: Iranian Persian; Parsi ONIX local code, equivalent to pes
        in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar GLE: Irish
    :cvar MGA: Irish, Middle (ca. 1100-1550)
    :cvar SGA: Irish, Old (to 1100)
    :cvar IRO: Iroquoian languages Collective name
    :cvar ITA: Italian
    :cvar JPN: Japanese
    :cvar JPX: Japanese languages Japonic. Collective name. ONIX local
        code, equivalent of jpx in ISO 639-5. Only for use in ONIX 3.0
        or later
    :cvar JAV: Javanese
    :cvar JOW: Jowulu ONIX local code, equivalent to jow in ISO 639-3.
        Only for use in ONIX 3.0 or later
    :cvar JRB: Judeo-Arabic Macrolanguage
    :cvar JPR: Judeo-Persian
    :cvar KBD: Kabardian (East Circassian)
    :cvar KBP: Kabiyè ONIX local code, equivalent to kbp in ISO 639-3.
        Only for use in ONIX 3.0 or later
    :cvar KAB: Kabyle
    :cvar KAC: Kachin; Jingpho
    :cvar KAL: Kalâtdlisut; Greenlandic
    :cvar XAL: Kalmyk; Oirat
    :cvar KAM: Kamba
    :cvar KAN: Kannada
    :cvar KAU: Kanuri Macrolanguage
    :cvar KAA: Kara-Kalpak
    :cvar KRC: Karachay-Balkar
    :cvar KDR: Karaim ONIX local code, equivalent to kdr in ISO 639-3
    :cvar KRL: Karelian
    :cvar KAR: Karen languages Collective name
    :cvar KAS: Kashmiri
    :cvar CSB: Kashubian
    :cvar KAW: Kawi
    :cvar KAZ: Kazakh
    :cvar KHA: Khasi
    :cvar KHI: Khoisan languages Collective name
    :cvar KHO: Khotanese; Sakan
    :cvar XUU: Khwedam, Kxoe ONIX local code, equivalent to xuu in ISO
        639-3. Only for use in ONIX 3.0 or later
    :cvar KIK: Kikuyu; Gikuyu
    :cvar KMB: Kimbundu
    :cvar KIN: Kinyarwanda
    :cvar KIR: Kirghiz; Kyrgyz
    :cvar KQS: Kissi, Northern Kisi (Guinean language). ONIX local code,
        equivalent to kqs in ISO 639-3. Only for use in ONIX 3.0 or
        later. Do not confuse with Kisi (Tanzanian language)
    :cvar KSS: Kissi, Southern Kisi (Liberian language). ONIX local
        code, equivalent to kss in ISO 639-3. Only for use in ONIX 3.0
        or later. Do not confuse with Kisi (Tanzanian language)
    :cvar TLH: Klingon; tlhIngan-Hol Artificial language
    :cvar KOM: Komi Macrolanguage
    :cvar KON: Kongo Macrolanguage
    :cvar KOK: Konkani Macrolanguage
    :cvar KOR: Korean
    :cvar KPE: Kpelle Macrolanguage
    :cvar KRO: Kru languages Collective name
    :cvar KUA: Kuanyama; Kwanyama
    :cvar KUM: Kumyk
    :cvar KUR: Kurdish Macrolanguage. See also ckb (Central Kurdish)
    :cvar KRU: Kurukh
    :cvar KOS: Kusaiean (Caroline Islands)
    :cvar KUT: Kutenai
    :cvar FKV: Kvensk ONIX local code, equivalent to fkv in ISO 639-3
    :cvar KWK: Kwakiutl ONIX local code, equivalent to kwk in ISO 639-3.
        Only for use in ONIX 3.0 or later
    :cvar LAD: Ladino
    :cvar LAH: Lahnda Macrolanguage
    :cvar LKT: Lakota Teton, Teton Sioux. ONIX local code, equivalent to
        lkt in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar LAM: Lamba
    :cvar DAY: Land Dayak languages Collective name
    :cvar LAO: Lao
    :cvar LAT: Latin
    :cvar LAV: Latvian Macrolanguage
    :cvar QLK: Lemko ONIX local code, distinct dialect of of Rusyn (not
        distinguished from rue by ISO 639-3). Only for use in ONIX 3.0
        or later
    :cvar LEZ: Lezgian
    :cvar LIJ: Ligurian ONIX local code for Italian dialect, equivalent
        to lij in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar LIM: Limbergan; Limburger; Limburgish
    :cvar LIN: Lingala
    :cvar LIT: Lithuanian
    :cvar JBO: Lojban
    :cvar LMO: Lombard ONIX local code for Italian dialect, equivalent
        to lmo in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar NDS: Low German; Low Saxon
    :cvar DSB: Lower Sorbian
    :cvar LOZ: Lozi
    :cvar LUB: Luba-Katanga
    :cvar LUA: Luba-Lulua
    :cvar LUI: Luiseño
    :cvar SMJ: Lule Sami
    :cvar LUN: Lunda
    :cvar LUO: Luo (Kenya and Tanzania)
    :cvar LUS: Lushai
    :cvar LTZ: Luxembourgish; Letzeburgesch
    :cvar MAC: Macedonian
    :cvar MAD: Madurese
    :cvar MAG: Magahi
    :cvar MAI: Maithili
    :cvar MAK: Makasar
    :cvar MLG: Malagasy Macrolanguage
    :cvar MAY: Malay Macrolanguage
    :cvar MAL: Malayalam
    :cvar POZ: Malayo-Polynesian languages Collective name. ONIX local
        code, equivalent of poz in ISO 639-5. Only for use in ONIX 3.0
        or later
    :cvar MLT: Maltese
    :cvar MNC: Manchu
    :cvar MDR: Mandar
    :cvar CMN: Mandarin ONIX local code, equivalent to cmn in ISO 639-3
    :cvar MAN: Mandingo Macrolanguage
    :cvar MNI: Manipuri
    :cvar MNO: Manobo languages Collective name
    :cvar GLV: Manx
    :cvar MAO: Maori
    :cvar ARN: Mapudungun; Mapuche
    :cvar MAR: Marathi
    :cvar CHM: Mari Macrolanguage
    :cvar MAH: Marshallese
    :cvar MWR: Marwari Macrolanguage
    :cvar MAS: Masai
    :cvar MYN: Mayan languages Collective name
    :cvar FIT: Meänkieli / Tornedalen Finnish ONIX local code,
        equivalent to fit in ISO 639-3
    :cvar MEN: Mende
    :cvar MIC: Mi’kmaq; Micmac
    :cvar CRG: Michif ONIX local code, equivalent to crg in ISO 639-3.
        Only for use in ONIX 3.0 or later
    :cvar GML: Middle Low German ONIX local code, equivalent to gml in
        ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar MIN: Minangkabau
    :cvar MWL: Mirandese
    :cvar MOH: Mohawk
    :cvar MDF: Moksha
    :cvar MOL: Moldavian; Moldovan Deprecated – use rum
    :cvar MKH: Mon-Khmer languages Collective name
    :cvar LOL: Mongo-Nkundu
    :cvar MON: Mongolian Macrolanguage
    :cvar CNR: Montenegrin Only for use in ONIX 3.0 or later
    :cvar MOS: Mooré; Mossi
    :cvar CRM: Moose Cree ONIX local code, equivalent to crm in ISO
        639-3. Only for use in ONIX 3.0 or later
    :cvar MUN: Munda languages Collective name
    :cvar MWF: Murrinh-Patha ONIX local code, equivalent to mwf in ISO
        639-3. Only for use in ONIX 3.0 or later
    :cvar NQO: N’Ko
    :cvar NAH: Nahuatl languages Collective name
    :cvar NSK: Naskapi ONIX local code, equivalent to nsk in ISO 639-3.
        Only for use in ONIX 3.0 or later
    :cvar NAU: Nauruan
    :cvar NAV: Navajo; Navaho
    :cvar NDE: Ndebele, North
    :cvar NBL: Ndebele, South
    :cvar NDO: Ndonga
    :cvar NAP: Neapolitan
    :cvar NEP: Nepali Macrolanguage
    :cvar QLS: Neutral Latin American Spanish ONIX local code, distinct
        and exclusively spoken variation of Spanish, not distinguished
        from spa (Spanish, Castilian) by ISO 639-3. Neutral Latin
        American Spanish should be considered a ‘shorthand’ for spa plus
        a ‘country code’ for Latin America – but prefer spa plus the
        relevant country code for specifically Mexican Spanish,
        Argentine (Rioplatense) Spanish, Puerto Rican Spanish etc.
        Neutral Latin American Spanish must only be used with audio
        material (including the audio tracks of TV, video and film) to
        indicate use of accent, vocabulary and construction suitable for
        broad use across Latin America. Only for use in ONIX 3.0 or
        later
    :cvar NEW: Newari; Nepal Bhasa
    :cvar NIA: Nias
    :cvar NIC: Niger-Kordofanian languages Collective name
    :cvar SSA: Nilo-Saharan languages Collective name
    :cvar NIU: Niuean
    :cvar NOG: Nogai
    :cvar QNF: Norman French Normand, of which Guernésiais, Jèrriais are
        distinct dialects. ONIX local code (not distinguished from nrf
        in ISO 639-3). Only for use in ONIX 3.0 or later
    :cvar NAI: North American Indian languages Collective name
    :cvar CRL: Northern East Cree ONIX local code, equivalent to crl in
        ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar FRR: Northern Frisian
    :cvar SME: Northern Sami
    :cvar NOR: Norwegian Macrolanguage. See also nob (Bokmål), nno
        (Nynorsk)
    :cvar NOB: Norwegian Bokmål
    :cvar NNO: Norwegian Nynorsk
    :cvar NUB: Nubian languages Collective name
    :cvar NYM: Nyamwezi
    :cvar NYN: Nyankole
    :cvar NYO: Nyoro
    :cvar NZI: Nzima
    :cvar OCI: Occitan (post-1500) See also qar (Aranés)
    :cvar ARC: Official Aramaic; Imperial Aramaic (700-300 BCE)
    :cvar OJI: Ojibwa Macrolanguage. See also ojs (Severn Ojibwa)
    :cvar ODT: Old Dutch / Old Low Franconian (ca. 400–1050) ONIX local
        code, equivalent to odt in ISO 639-3
    :cvar NON: Old Norse
    :cvar PEO: Old Persian (ca. 600-400 B.C.)
    :cvar ORI: Oriya Macrolanguage
    :cvar ORM: Oromo Macrolanguage
    :cvar OSA: Osage
    :cvar OSS: Ossetian; Ossetic
    :cvar OMQ: Oto-Manguean languages ONIX local code, equivalent to omq
        in ISO 639-5. Collective name
    :cvar OTO: Otomian languages Collective name
    :cvar PAL: Pahlavi
    :cvar PAU: Palauan
    :cvar PLI: Pali
    :cvar PAM: Pampanga; Kapampangan
    :cvar PAG: Pangasinan
    :cvar PAN: Panjabi
    :cvar PAP: Papiamento
    :cvar PAA: Papuan languages Collective name
    :cvar NSO: Pedi; Sepedi; Northern Sotho
    :cvar PER: Persian Macrolanguage. See also pes (Iranian Persian,
        Farsi), prs (Dari)
    :cvar PHI: Philippine languages Collective name
    :cvar PHN: Phoenician
    :cvar PCD: Picard ONIX local code, distinct variant of langue d’oïl
        (old northern French), equivalent to pcd in ISO 639-3. Only for
        use in ONIX 3.0 or later
    :cvar QSP: Picture Communication Symbols (PCS) ONIX local code for
        graphical symbols used in augmentative and alternative
        communication and education, not listed in ISO 639-3. Only for
        use in ONIX 3.0 or later
    :cvar PMS: Piedmontese ONIX local code for Italian dialect,
        equivalent to pms in ISO 639-3. Only for use in ONIX 3.0 or
        later
    :cvar CRK: Plains Cree ONIX local code, equivalent to crk in ISO
        639-3. Only for use in ONIX 3.0 or later
    :cvar POL: Polish
    :cvar PON: Ponapeian
    :cvar POR: Portuguese
    :cvar PRA: Prakrit languages Collective name
    :cvar PRO: Provençal, Old (to 1500); Occitan, Old (to 1500)
    :cvar PUS: Pushto; Pashto Macrolanguage
    :cvar QUE: Quechua Macrolanguage
    :cvar RAJ: Rajasthani Macrolanguage
    :cvar RAP: Rapanui
    :cvar RAR: Rarotongan; Cook Islands Maori
    :cvar RCF: Réunion Creole French ONIX local code, equivalent to rcf
        in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar RGN: Romagnol ONIX local code for Italian dialect, equivalent
        to rgl in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar ROA: Romance languages Collective name
    :cvar RUM: Romanian
    :cvar ROH: Romansh
    :cvar ROM: Romany Romani. Macrolanguage
    :cvar RUN: Rundi
    :cvar RUS: Russian
    :cvar SAL: Salishan languages Collective name
    :cvar SAM: Samaritan Aramaic
    :cvar SMI: Sami languages Collective name
    :cvar SMO: Samoan
    :cvar SAD: Sandawe
    :cvar SAG: Sango
    :cvar SAN: Sanskrit
    :cvar SAT: Santali
    :cvar SRM: Saramaccan ONIX local code for Saramaccan language,
        equivalent to srm in ISO 639-3. Only for use in ONIX 3.0 or
        later
    :cvar SRD: Sardinian Macrolanguage. See also sdc (Sassarese), sdn
        (Gallurese), sro (Campidanese)
    :cvar SAS: Sasak
    :cvar SDC: Sassarese ONIX local code for Sardinian dialect,
        equivalent to sdc in ISO 639-3. Only for use in ONIX 3.0 or
        later
    :cvar SCO: Scots
    :cvar GLA: Scottish Gaelic
    :cvar SEL: Selkup
    :cvar SEM: Semitic languages Collective name
    :cvar SCC: Serbian Deprecated – use srp
    :cvar SRP: Serbian
    :cvar SRR: Serer
    :cvar OJS: Severn Ojibwa ONIX local code, equivalent to ojs in ISO
        639-3. Only for use in ONIX 3.0 or later
    :cvar SHN: Shan
    :cvar SNA: Shona
    :cvar SHS: Shuswap ONIX local code, equivalent to shs in ISO 639-3.
        Only for use in ONIX 3.0 or later
    :cvar III: Sichuan Yi; Nuosu
    :cvar SCN: Sicilian
    :cvar SID: Sidamo
    :cvar SGN: Sign languages Collective name
    :cvar BLA: Siksika
    :cvar SZL: Silesian ONIX local code, equivalent to szl in ISO 639-3.
        Only for use in ONIX 3.0 or later
    :cvar SND: Sindhi
    :cvar SIN: Sinhala; Sinhalese
    :cvar ZHX: Sinitic languages Chinese (family) languages. Collective
        name. ONIX local code, equivalent of zhx in ISO 639-5. Only for
        use in ONIX 3.0 or later
    :cvar SIT: Sino-Tibetan languages Collective name
    :cvar SIO: Siouan languages Collective name
    :cvar SMS: Skolt Sami
    :cvar DEN: Slave (Athapascan) Macrolanguage
    :cvar SLA: Slavic languages Collective name
    :cvar SLO: Slovak
    :cvar SLV: Slovenian
    :cvar SOG: Sogdian
    :cvar SOM: Somali
    :cvar SON: Songhai languages Collective name
    :cvar SNK: Soninke
    :cvar WEN: Sorbian languages Collective name
    :cvar SOT: Sotho; Sesotho
    :cvar SAI: South American Indian languages Collective name
    :cvar ALT: Southern Altai
    :cvar CRJ: Southern East Cree ONIX local code, equivalent to crj in
        ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar SMA: Southern Sami
    :cvar SPA: Spanish
    :cvar SRN: Sranan Tongo
    :cvar ZGH: Standard Moroccan Tamazight
    :cvar STO: Stoney ONIX local code, equivalent to sto in ISO 639-3.
        Only for use in ONIX 3.0 or later
    :cvar SUK: Sukuma
    :cvar SUX: Sumerian
    :cvar SUN: Sundanese
    :cvar SUS: Susu
    :cvar SWA: Swahili Macrolanguage
    :cvar CSW: Swampy Cree ONIX local code, equivalent to csw in ISO
        639-3. Only for use in ONIX 3.0 or later
    :cvar SSW: Swazi; Swati
    :cvar SWE: Swedish
    :cvar GSW: Swiss German; Alemannic; Alsatian
    :cvar SYR: Syriac Macrolanguage
    :cvar TGL: Tagalog
    :cvar TAH: Tahitian
    :cvar TAI: Tai languages Collective name
    :cvar TGK: Tajik; Tajiki Persian
    :cvar TMH: Tamashek Macrolanguage
    :cvar TAM: Tamil
    :cvar SHI: Tashelhit; Shilha ONIX local code, equivalent to shi in
        ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar TAT: Tatar
    :cvar TEL: Telugu
    :cvar TEM: Temne; Time
    :cvar TER: Terena
    :cvar TET: Tetum
    :cvar THA: Thai
    :cvar THP: Thompson Nla’kapamux. ONIX local code, equivalent to thp
        in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar TIB: Tibetan
    :cvar TIG: Tigré
    :cvar TIR: Tigrinya
    :cvar TIV: Tiv
    :cvar TLI: Tlingit
    :cvar TPI: Tok Pisin
    :cvar TKL: Tokelauan
    :cvar TOG: Tonga (Nyasa)
    :cvar TON: Tongan
    :cvar RMG: Traveler Norwegian ONIX local code for Norwegian
        Scandoromani variant, equivalent to rmg in ISO 639-3. Only for
        use in ONIX 3.0 or later
    :cvar TSD: Tsakonian ONIX local code, equivalent to tsd in ISO
        639-3. Only for use in ONIX 3.0 or later
    :cvar TSI: Tsimshian
    :cvar TSO: Tsonga
    :cvar TSN: Tswana AKA Setswana
    :cvar TUM: Tumbuka
    :cvar TUP: Tupi languages Collective name
    :cvar TUR: Turkish
    :cvar OTA: Turkish, Ottoman
    :cvar TUK: Turkmen
    :cvar TVL: Tuvaluan
    :cvar TYV: Tuvinian
    :cvar TWI: Twi
    :cvar TZO: Tzotzil ONIX local code, equivalent to tzo in ISO 639-3
    :cvar UDM: Udmurt
    :cvar UGA: Ugaritic
    :cvar UIG: Uighur; Uyghur
    :cvar UKR: Ukrainian
    :cvar UMB: Umbundu
    :cvar HSB: Upper Sorbian
    :cvar URJ: Uralic languages Collective name. ONIX local code,
        equivalent of urj in ISO 639-5. Only for use in ONIX 3.0 or
        later
    :cvar URD: Urdu
    :cvar UZB: Uzbek Macrolanguage
    :cvar VAI: Vai
    :cvar QAV: Valencian ONIX local code, distinct dialect of Catalan
        (not distinguished from cat by ISO 639-3)
    :cvar VEN: Venda
    :cvar VEC: Venetian/Venetan ONIX local code for Italian dialect,
        equivalent to vec in ISO 639-3. Only for use in ONIX 3.0 or
        later
    :cvar VIE: Vietnamese
    :cvar VOL: Volapük Artificial language
    :cvar VOT: Votic
    :cvar WAK: Wakashan languages Collective name
    :cvar WLS: Wallisian East Uvean. ONIX local code, equivalent to wls
        in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar WLN: Walloon
    :cvar WAR: Waray
    :cvar WAS: Washo
    :cvar GUC: Wayuu Guajiro. ONIX local code, equivalent of guc in ISO
        639-3. Only for use in ONIX 3.0 or later
    :cvar WEL: Welsh
    :cvar FRY: Western Frisian
    :cvar QSW: Widgit symbols ONIX local code for graphical symbols used
        in augmentative and alternative communication and education, not
        listed in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar WAL: Wolaitta; Wolaytta
    :cvar WOL: Wolof
    :cvar CWD: Woods Cree ONIX local code, equivalent to cwd in ISO
        639-3. Only for use in ONIX 3.0 or later
    :cvar WYM: Wymysorys Vilamovian. ONIX local code, equivalent to wym
        in ISO 639-3. Only for use in ONIX 3.0 or later
    :cvar XHO: Xhosa
    :cvar SAH: Yakut
    :cvar YAO: Yao
    :cvar YAP: Yapese
    :cvar YID: Yiddish Macrolanguage
    :cvar YOR: Yoruba
    :cvar YPK: Yupik languages Collective name
    :cvar ZND: Zande languages Collective name
    :cvar ZAP: Zapotec Macrolanguage
    :cvar ZZA: Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki
        Macrolanguage
    :cvar ZEN: Zenaga
    :cvar ZHA: Zhuang; Chuang Macrolanguage
    :cvar ZUL: Zulu
    :cvar ZUN: Zuni
    :cvar MIS: Uncoded language Use where no suitable code is available
    :cvar UND: Undetermined language
    :cvar MUL: Multiple languages
    :cvar ZXX: No linguistic content
    """

    ABK = "abk"
    ACE = "ace"
    ACH = "ach"
    ADA = "ada"
    ADY = "ady"
    AAR = "aar"
    AFH = "afh"
    AFR = "afr"
    AFA = "afa"
    AIN = "ain"
    AKA = "aka"
    AKK = "akk"
    ALB = "alb"
    ALE = "ale"
    ALG = "alg"
    ALQ = "alq"
    TUT = "tut"
    AMH = "amh"
    ANP = "anp"
    APA = "apa"
    ARA = "ara"
    ARG = "arg"
    QAR = "qar"
    ARP = "arp"
    ARW = "arw"
    ARM = "arm"
    RUP = "rup"
    ART = "art"
    ASM = "asm"
    AST = "ast"
    ATH = "ath"
    ATJ = "atj"
    AUS = "aus"
    AAV = "aav"
    MAP = "map"
    AVA = "ava"
    AVE = "ave"
    AWA = "awa"
    AYM = "aym"
    AZE = "aze"
    BAN = "ban"
    BAT = "bat"
    BAL = "bal"
    BAM = "bam"
    BAI = "bai"
    BAD = "bad"
    BNT = "bnt"
    BAS = "bas"
    BAK = "bak"
    BAQ = "baq"
    BTK = "btk"
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
    BYN = "byn"
    ZBL = "zbl"
    BRX = "brx"
    BOS = "bos"
    BRA = "bra"
    BRE = "bre"
    BUG = "bug"
    BUL = "bul"
    BUM = "bum"
    BUA = "bua"
    BUR = "bur"
    CAD = "cad"
    SRO = "sro"
    YUE = "yue"
    CAT = "cat"
    CAU = "cau"
    CAY = "cay"
    CEB = "ceb"
    CEL = "cel"
    CAI = "cai"
    TZM = "tzm"
    KHM = "khm"
    CKB = "ckb"
    CHG = "chg"
    CMC = "cmc"
    CHA = "cha"
    CHE = "che"
    CHR = "chr"
    CHY = "chy"
    CHB = "chb"
    NYA = "nya"
    CIC = "cic"
    CHI = "chi"
    CHN = "chn"
    CHP = "chp"
    CHO = "cho"
    CHU = "chu"
    CHK = "chk"
    CHV = "chv"
    NWC = "nwc"
    SYC = "syc"
    COP = "cop"
    COR = "cor"
    COS = "cos"
    CRE = "cre"
    MUS = "mus"
    CRP = "crp"
    CPE = "cpe"
    CPF = "cpf"
    CPP = "cpp"
    CRH = "crh"
    HRV = "hrv"
    SCR = "scr"
    CUS = "cus"
    CZE = "cze"
    DAK = "dak"
    DAN = "dan"
    DAR = "dar"
    PRS = "prs"
    DEL = "del"
    DIN = "din"
    DIV = "div"
    DOI = "doi"
    DGR = "dgr"
    DRA = "dra"
    DUA = "dua"
    DUM = "dum"
    DUT = "dut"
    DYU = "dyu"
    DZO = "dzo"
    IKE = "ike"
    FRS = "frs"
    EFI = "efi"
    EGY = "egy"
    EKA = "eka"
    ELX = "elx"
    EGL = "egl"
    ENG = "eng"
    ENM = "enm"
    ANG = "ang"
    MYV = "myv"
    ESX = "esx"
    EPO = "epo"
    EST = "est"
    GEZ = "gez"
    EWE = "ewe"
    EWO = "ewo"
    FAN = "fan"
    FAT = "fat"
    FAO = "fao"
    FIJ = "fij"
    FIL = "fil"
    FIN = "fin"
    FIU = "fiu"
    FON = "fon"
    FRE = "fre"
    FRM = "frm"
    FRO = "fro"
    FUR = "fur"
    FUL = "ful"
    GAA = "gaa"
    CAR = "car"
    GLG = "glg"
    QGL = "qgl"
    SDN = "sdn"
    LUG = "lug"
    GRT = "grt"
    GAY = "gay"
    GBA = "gba"
    GEO = "geo"
    GER = "ger"
    GMH = "gmh"
    GOH = "goh"
    GEM = "gem"
    GIL = "gil"
    GIT = "git"
    GON = "gon"
    GOR = "gor"
    GOT = "got"
    GRB = "grb"
    GRC = "grc"
    GRE = "gre"
    GRN = "grn"
    NRF = "nrf"
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
    HMO = "hmo"
    HIT = "hit"
    HMX = "hmx"
    HMN = "hmn"
    HOP = "hop"
    HUN = "hun"
    HUP = "hup"
    IBA = "iba"
    ICE = "ice"
    IDO = "ido"
    IBO = "ibo"
    IJO = "ijo"
    ILO = "ilo"
    SMN = "smn"
    INC = "inc"
    INE = "ine"
    IND = "ind"
    INH = "inh"
    MOE = "moe"
    INA = "ina"
    ILE = "ile"
    IKT = "ikt"
    IKU = "iku"
    IPK = "ipk"
    QIV = "qiv"
    IRA = "ira"
    PES = "pes"
    GLE = "gle"
    MGA = "mga"
    SGA = "sga"
    IRO = "iro"
    ITA = "ita"
    JPN = "jpn"
    JPX = "jpx"
    JAV = "jav"
    JOW = "jow"
    JRB = "jrb"
    JPR = "jpr"
    KBD = "kbd"
    KBP = "kbp"
    KAB = "kab"
    KAC = "kac"
    KAL = "kal"
    XAL = "xal"
    KAM = "kam"
    KAN = "kan"
    KAU = "kau"
    KAA = "kaa"
    KRC = "krc"
    KDR = "kdr"
    KRL = "krl"
    KAR = "kar"
    KAS = "kas"
    CSB = "csb"
    KAW = "kaw"
    KAZ = "kaz"
    KHA = "kha"
    KHI = "khi"
    KHO = "kho"
    XUU = "xuu"
    KIK = "kik"
    KMB = "kmb"
    KIN = "kin"
    KIR = "kir"
    KQS = "kqs"
    KSS = "kss"
    TLH = "tlh"
    KOM = "kom"
    KON = "kon"
    KOK = "kok"
    KOR = "kor"
    KPE = "kpe"
    KRO = "kro"
    KUA = "kua"
    KUM = "kum"
    KUR = "kur"
    KRU = "kru"
    KOS = "kos"
    KUT = "kut"
    FKV = "fkv"
    KWK = "kwk"
    LAD = "lad"
    LAH = "lah"
    LKT = "lkt"
    LAM = "lam"
    DAY = "day"
    LAO = "lao"
    LAT = "lat"
    LAV = "lav"
    QLK = "qlk"
    LEZ = "lez"
    LIJ = "lij"
    LIM = "lim"
    LIN = "lin"
    LIT = "lit"
    JBO = "jbo"
    LMO = "lmo"
    NDS = "nds"
    DSB = "dsb"
    LOZ = "loz"
    LUB = "lub"
    LUA = "lua"
    LUI = "lui"
    SMJ = "smj"
    LUN = "lun"
    LUO = "luo"
    LUS = "lus"
    LTZ = "ltz"
    MAC = "mac"
    MAD = "mad"
    MAG = "mag"
    MAI = "mai"
    MAK = "mak"
    MLG = "mlg"
    MAY = "may"
    MAL = "mal"
    POZ = "poz"
    MLT = "mlt"
    MNC = "mnc"
    MDR = "mdr"
    CMN = "cmn"
    MAN = "man"
    MNI = "mni"
    MNO = "mno"
    GLV = "glv"
    MAO = "mao"
    ARN = "arn"
    MAR = "mar"
    CHM = "chm"
    MAH = "mah"
    MWR = "mwr"
    MAS = "mas"
    MYN = "myn"
    FIT = "fit"
    MEN = "men"
    MIC = "mic"
    CRG = "crg"
    GML = "gml"
    MIN = "min"
    MWL = "mwl"
    MOH = "moh"
    MDF = "mdf"
    MOL = "mol"
    MKH = "mkh"
    LOL = "lol"
    MON = "mon"
    CNR = "cnr"
    MOS = "mos"
    CRM = "crm"
    MUN = "mun"
    MWF = "mwf"
    NQO = "nqo"
    NAH = "nah"
    NSK = "nsk"
    NAU = "nau"
    NAV = "nav"
    NDE = "nde"
    NBL = "nbl"
    NDO = "ndo"
    NAP = "nap"
    NEP = "nep"
    QLS = "qls"
    NEW = "new"
    NIA = "nia"
    NIC = "nic"
    SSA = "ssa"
    NIU = "niu"
    NOG = "nog"
    QNF = "qnf"
    NAI = "nai"
    CRL = "crl"
    FRR = "frr"
    SME = "sme"
    NOR = "nor"
    NOB = "nob"
    NNO = "nno"
    NUB = "nub"
    NYM = "nym"
    NYN = "nyn"
    NYO = "nyo"
    NZI = "nzi"
    OCI = "oci"
    ARC = "arc"
    OJI = "oji"
    ODT = "odt"
    NON = "non"
    PEO = "peo"
    ORI = "ori"
    ORM = "orm"
    OSA = "osa"
    OSS = "oss"
    OMQ = "omq"
    OTO = "oto"
    PAL = "pal"
    PAU = "pau"
    PLI = "pli"
    PAM = "pam"
    PAG = "pag"
    PAN = "pan"
    PAP = "pap"
    PAA = "paa"
    NSO = "nso"
    PER = "per"
    PHI = "phi"
    PHN = "phn"
    PCD = "pcd"
    QSP = "qsp"
    PMS = "pms"
    CRK = "crk"
    POL = "pol"
    PON = "pon"
    POR = "por"
    PRA = "pra"
    PRO = "pro"
    PUS = "pus"
    QUE = "que"
    RAJ = "raj"
    RAP = "rap"
    RAR = "rar"
    RCF = "rcf"
    RGN = "rgn"
    ROA = "roa"
    RUM = "rum"
    ROH = "roh"
    ROM = "rom"
    RUN = "run"
    RUS = "rus"
    SAL = "sal"
    SAM = "sam"
    SMI = "smi"
    SMO = "smo"
    SAD = "sad"
    SAG = "sag"
    SAN = "san"
    SAT = "sat"
    SRM = "srm"
    SRD = "srd"
    SAS = "sas"
    SDC = "sdc"
    SCO = "sco"
    GLA = "gla"
    SEL = "sel"
    SEM = "sem"
    SCC = "scc"
    SRP = "srp"
    SRR = "srr"
    OJS = "ojs"
    SHN = "shn"
    SNA = "sna"
    SHS = "shs"
    III = "iii"
    SCN = "scn"
    SID = "sid"
    SGN = "sgn"
    BLA = "bla"
    SZL = "szl"
    SND = "snd"
    SIN = "sin"
    ZHX = "zhx"
    SIT = "sit"
    SIO = "sio"
    SMS = "sms"
    DEN = "den"
    SLA = "sla"
    SLO = "slo"
    SLV = "slv"
    SOG = "sog"
    SOM = "som"
    SON = "son"
    SNK = "snk"
    WEN = "wen"
    SOT = "sot"
    SAI = "sai"
    ALT = "alt"
    CRJ = "crj"
    SMA = "sma"
    SPA = "spa"
    SRN = "srn"
    ZGH = "zgh"
    STO = "sto"
    SUK = "suk"
    SUX = "sux"
    SUN = "sun"
    SUS = "sus"
    SWA = "swa"
    CSW = "csw"
    SSW = "ssw"
    SWE = "swe"
    GSW = "gsw"
    SYR = "syr"
    TGL = "tgl"
    TAH = "tah"
    TAI = "tai"
    TGK = "tgk"
    TMH = "tmh"
    TAM = "tam"
    SHI = "shi"
    TAT = "tat"
    TEL = "tel"
    TEM = "tem"
    TER = "ter"
    TET = "tet"
    THA = "tha"
    THP = "thp"
    TIB = "tib"
    TIG = "tig"
    TIR = "tir"
    TIV = "tiv"
    TLI = "tli"
    TPI = "tpi"
    TKL = "tkl"
    TOG = "tog"
    TON = "ton"
    RMG = "rmg"
    TSD = "tsd"
    TSI = "tsi"
    TSO = "tso"
    TSN = "tsn"
    TUM = "tum"
    TUP = "tup"
    TUR = "tur"
    OTA = "ota"
    TUK = "tuk"
    TVL = "tvl"
    TYV = "tyv"
    TWI = "twi"
    TZO = "tzo"
    UDM = "udm"
    UGA = "uga"
    UIG = "uig"
    UKR = "ukr"
    UMB = "umb"
    HSB = "hsb"
    URJ = "urj"
    URD = "urd"
    UZB = "uzb"
    VAI = "vai"
    QAV = "qav"
    VEN = "ven"
    VEC = "vec"
    VIE = "vie"
    VOL = "vol"
    VOT = "vot"
    WAK = "wak"
    WLS = "wls"
    WLN = "wln"
    WAR = "war"
    WAS = "was"
    GUC = "guc"
    WEL = "wel"
    FRY = "fry"
    QSW = "qsw"
    WAL = "wal"
    WOL = "wol"
    CWD = "cwd"
    WYM = "wym"
    XHO = "xho"
    SAH = "sah"
    YAO = "yao"
    YAP = "yap"
    YID = "yid"
    YOR = "yor"
    YPK = "ypk"
    ZND = "znd"
    ZAP = "zap"
    ZZA = "zza"
    ZEN = "zen"
    ZHA = "zha"
    ZUL = "zul"
    ZUN = "zun"
    MIS = "mis"
    UND = "und"
    MUL = "mul"
    ZXX = "zxx"


class List79(Enum):
    """
    Product form feature type.

    :cvar VALUE_01: Color of cover For Product Form Feature values see
        code list 98
    :cvar VALUE_26: Color of spine Where it is different from the
        overall color of the cover (see code 01). For Product Form
        Feature values see code list 98. Only for use in ONIX 3.0 or
        later
    :cvar VALUE_27: Color of foil On cover or spine. For Product Form
        Feature values see metallic colors from code list 98. Only for
        use in ONIX 3.0 or later
    :cvar VALUE_02: Color of page edge Sprayed / gilded edges. For
        Product Form Feature values see code list 98
    :cvar VALUE_03: Text font The principal font used for body text,
        when this is a significant aspect of product description, eg for
        some Bibles, and for large print product. The accompanying
        &lt;ProductFormFeatureDescription&gt; is text specifying the
        typeface name. The font size may be specified with the font
        name, but is preferred separately (in points) in
        &lt;ProductFormFeatureValue&gt;
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
        as Ting Pen (http://www.ting.eu), the iSmart Touch and Read Pen.
        These devices scan invisible codes specially printed on the page
        to identify the book and position of the word, and the word is
        then read aloud by the device. The name of the compatible device
        (or range of devices) should be given in
        &lt;ProductFormFeatureDescription&gt;
    :cvar VALUE_09: E-publication accessibility detail For
        &lt;ProductFormFeatureValue&gt; codes, see Codelist 196
    :cvar VALUE_10: E-publication format version For versioned e-book
        file formats (or in some cases, devices).
        &lt;ProductFormFeatureValue&gt; should contain the version
        number as a period-separated list of numbers (eg ‘7’, ‘1.5’ or
        ‘3.10.7’). Only for use in ONIX 3.0 or later – in ONIX 2.1, use
        &lt;EpubTypeVersion&gt; instead. For the most common file
        formats, code 15 and List 220 is strongly preferred
    :cvar VALUE_12: US CPSIA or other international hazard warning
        Hazard warning required by US Consumer Product Safety
        Improvement Act (CPSIA) of 2008 or other US or international
        legislation. Required, when applicable, for products sold in the
        US. The Product Form Feature Value is a code from List 143.
        Further explanation may be given in Product Form Feature
        Description
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
        is a code from list 220. Only for use in ONIX 3.0 or later
    :cvar VALUE_16: E-publication format validator version For common
        versioned e-book formats, the name and version of the validator
        used to check conformance. &lt;ProductFormFeatureDescription&gt;
        is the common name of the validator used (eg EpubCheck,
        Flightdeck), and &lt;ProductFormFeatureValue&gt; is the version
        number of the validator (eg 4.0.0a). Use with code 15 (or
        possibly code 10), or with &lt;EpubTypeVersion&gt;, to specify
        the version the e-publication conforms with
    :cvar VALUE_17: ‘Point and watch’ device/app compatibility Indicates
        compatibility with proprietary ‘point and watch‘ devices or
        apps. These scan invisible codes specially printed on the page,
        or the whole page image, to identify the book and page position.
        Scanning can trigger display of (for example) an augmented
        reality view of the page. The name of the compatible app or
        device (or range of apps/devices) should be given in
        &lt;ProductFormFeatureDescription&gt;. Only for use in ONIX 3.0
        or later
    :cvar VALUE_18: E-publication authentication and access control
        Requirement for user authentication prior to use, with detail of
        authentication method (user enrolment, and login passwords,
        location- or device-based recognition, authentication via third-
        party identity service etc) given in
        &lt;ProductFormFeatureDescription&gt;. Only for use in ONIX 3.0
        or later
    :cvar VALUE_19: Battery type and safety Use to describe battery
        requirements, types, hazards and battery safety warnings.
        &lt;ProductFormFeatureValue&gt; is a code from List 242. Only
        for use in ONIX 3.0 or later
    :cvar VALUE_20: Battery capacity Total capacity (of batteries in the
        product) in Watt hours. &lt;ProductFormFeatureValue&gt; is an
        integer or decimal number (eg ‘45’, not ‘45Wh’). Only for use in
        ONIX 3.0 or later
    :cvar VALUE_21: Dangerous goods Use to describe regulation of the
        product for various purposes. &lt;ProductFormFeatureValue&gt; is
        a code from List 243. Only for use in ONIX 3.0 or later
    :cvar VALUE_22: Game pieces Number of pieces, eg for jigsaws,
        puzzles, kits, board games. &lt;ProductFormFeatureValue&gt; is
        an integer. Only for use in ONIX 3.0 or later. For pieces like
        cards in a pack, see &lt;Extent&gt; and code 00 from List 24
    :cvar VALUE_23: Game players Number of players, for board games,
        card games, videogames etc. &lt;ProductFormFeatureValue&gt; must
        be a required (exact) number as an integer OR a range (eg
        ‘2–6’), optionally accompanied by the number of players as text
        (eg ‘suitable for 2–6 players’) in
        &lt;ProductFormFeatureDescription&gt;. Only for use in ONIX 3.0
        or later
    :cvar VALUE_24: Game play time Typical time to complete a game, for
        board games, card games, videogames etc, stated as an integer
        (in minutes) OR range (eg ‘60–90’) in
        &lt;ProductFormFeatureValue&gt;, optionally accompanied by the
        playing time as text (eg ‘typically 60–90 minutes’) in
        &lt;ProductFormFeatureDescription&gt;. Only for use in ONIX 3.0
        or later
    :cvar VALUE_25: Personal data requirements Personal data required
        for registration or use of the product. This can be coded in
        &lt;ProductFormFeatureValue&gt; (for example using a URI from
        SCOLOM list 044 – see
        http://data.education.fr/voc/scolomfr/scolomfr-voc-044) – and/or
        described in &lt;ProductFormFeatureDescription&gt;. Only for use
        in ONIX 3.0 or later
    :cvar VALUE_30: Not FSC or PEFC certified Product does not carry FSC
        or PEFC logo. The Product Form Feature Value element is not
        used. The Product Form Feature Description element may carry
        free text indicating the grade or type of paper. The product
        record may also still carry a claimed Pre- and Post-Consumer
        Waste (PCW) percentage value (type code 37) in a separate repeat
        of the Product Form Feature composite
    :cvar VALUE_31: FSC certified – pure Product carries FSC logo (Pure,
        100%). &lt;ProductFormFeatureValue&gt; is the Certification
        number (ie either a Chain Of Custody (COC) number or a Trademark
        License number) printed on the book. Format: Chain of Custody
        number is two to five letters-COC-six digits (the digits should
        include leading zeros if necessary), eg ‘AB-COC-001234’ or
        ‘ABCDE-COC-123456’; Trademark License number is C followed by
        six digits, eg ‘C005678’ (this would normally be prefixed by
        ‘FSC®’ when displayed). The Product Form Feature Description
        element may carry free text indicating the grade or type of
        paper. By definition, a product certified Pure does not contain
        Pre- or Post-Consumer-Waste (PCW), so type code 31 can only
        occur on its own. Certification numbers may be checked at
        https://info.fsc.org/
    :cvar VALUE_32: FSC certified – mixed sources Product carries FSC
        logo (Mixed sources, Mix). &lt;ProductFormFeatureValue&gt; is
        the Certification number (ie either a Chain Of Custody (COC)
        number or a Trademark License number) printed on the book.
        Format: Chain of Custody number is two to five letters-COC-six
        digits (the digits should include leading zeros if necessary),
        eg ‘AB-COC-001234’ or ‘ABCDE-COC-123456’; Trademark License
        number is C followed by six digits, eg ‘C005678’ (this would
        normally be prefixed by ‘FSC®’ when displayed). The Product Form
        Feature Description element may carry free text indicating the
        grade or type of paper. May be accompanied by a Pre- and Post-
        Consumer-Waste (PCW) percentage value, to be reported in another
        instance of &lt;ProductFormFeature&gt; with type code 36.
        Certification numbers may be checked at https://info.fsc.org/
    :cvar VALUE_33: FSC certified – recycled Product carries FSC logo
        (Recycled). &lt;ProductFormFeatureValue&gt; is the Certification
        number (ie either a Chain Of Custody (COC) number or a Trademark
        License number) printed on the book. Format: Chain of Custody
        number is two to five letters-COC-six digits (the digits should
        include leading zeroes if necessary), eg ‘AB-COC-001234’ or
        ‘ABCDE-COC-123456’; Trademark License number is C followed by
        six digits, eg ‘C005678’ (this would normally be prefixed by
        ‘FSC®’ when displayed). The Product Form Feature Description
        element may carry free text indicating the grade or type of
        paper. Should be accompanied by a Pre- and Post-Consumer-Waste
        (PCW) percentage value, to be reported in another instance of
        &lt;ProductFormFeature&gt; with type code 36. Certification
        numbers may be checked at https://info.fsc.org/
    :cvar VALUE_34: PEFC certified Product carries PEFC logo (certified)
        or equivalent from PEFC-endorsed national scheme.
        &lt;ProductFormFeatureValue&gt; is the Chain Of Custody (COC)
        number printed on the book. The Product Form Feature Description
        element may carry free text indicating the grade or type of
        paper. May be accompanied by a Post-Consumer Waste (PCW)
        percentage value, to be reported in another instance of
        &lt;ProductFormFeature&gt; with type code 36
    :cvar VALUE_35: PEFC recycled Product carries PEFC logo (recycled)
        or equivalent from PEFC-endorsed national scheme.
        &lt;ProductFormFeatureValue&gt; is the Chain Of Custody (COC)
        number printed on the book. The Product Form Feature Description
        element may carry free text indicating the grade or type of
        paper. Should be accompanied by a Post-Consumer-Waste (PCW)
        percentage value, to be reported in another instance of
        &lt;ProductFormFeature&gt; with type code 36
    :cvar VALUE_36: FSC or PEFC certified Pre- and Post-Consumer Waste
        (PCW) percentage The percentage of recycled Pre- and Post-
        Consumer-Waste (PCW) used in a product where the composition is
        certified by FSC, PEFC or PEFC-endorsed scheme.
        &lt;ProductFormFeatureValue&gt; is an integer. May occur
        together with type code 32, 33, 34 or 35
    :cvar VALUE_37: Claimed Pre- and Post-Consumer Waste (PCW)
        percentage The percentage of recycled Pre- and Post-Consumer
        Waste (PCW) claimed to be used in a product where the
        composition is not certified by FSC or PEFC. &lt;Product
        FormFeatureValue&gt; is an integer.
        &lt;ProductFormFeatureDescription&gt; may carry free text
        supporting the claim. Must be accompanied by type code 30
    :cvar VALUE_38: ‘Green’ inks Vegetable-based or other
        environmentally-conscious inks and varnishes.
        &lt;ProductFormFeatureDescription&gt; may carry free text with a
        more detailed statement. Only for use in ONIX 3.0 or later
    :cvar VALUE_39: ‘Green’ adhesives Product binding uses
        environmentally-concious adhesives and other binding materials.
        &lt;ProductFormFeatureDescription&gt; may carry free text with a
        more detailed statement. Only for use in ONIX 3.0 or later
    :cvar VALUE_40: Paper produced by ‘green’ technology Product made
        from paper produced using environmentally-conscious technology.
        &lt;ProductFormFeatureDescription&gt; may carry free text with a
        more detailed statement
    :cvar VALUE_41: Carbon/GHG emission certification scheme
        &lt;ProductFormFeatureValue&gt; is a code from List 262
        identifying the particular certification scheme.
        &lt;ProductFormFeatureDescription&gt; may be a descriptor for
        some part, schedule or annex of the certification scheme, where
        necessary. Only for use in ONIX 3.0 or later
    :cvar VALUE_42: Carbon/GHG emission certification / license number
        &lt;ProductFormFeatureValue&gt; is a code from List 262
        identifying a particular certification scheme.
        &lt;ProductFormFeatureDescription&gt; is a certificate or
        license number used to certify compliance with the scheme. Only
        for use in ONIX 3.0 or later
    :cvar VALUE_43: Carbon/GHG emission certification URL
        &lt;ProductFormFeatureValue&gt; is a code from List 262
        identifying a particular certification scheme.
        &lt;ProductFormFeatureDescription&gt; is a URL linking to a web
        page certifying compliance with the scheme. Only for use in ONIX
        3.0 or later
    :cvar VALUE_44: Carbon/GHG Scope 3 certified Carbon dioxide
        equivalent emission &lt;ProductFormFeatureValue&gt; is a code
        from List 262 identifying a particular certification scheme.
        &lt;ProductFormFeatureDescription&gt; is a number specifying
        certified GHG emissions per copy of the product, measured in
        kilograms of Carbon dioxide equivalent (CO₂e) using the Scope 3
        methodology of the scheme. Only for use in ONIX 3.0 or later
    :cvar VALUE_45: Carbon/GHG Scope 2 certified Carbon dioxide
        equivalent emission Only for use in ONIX 3.0 or later
    :cvar VALUE_46: Carbon/GHG Scope 1 certified Carbon dioxide
        equivalent emission Scope 1 emission certifications are not
        recommended for use. Only for use in ONIX 3.0 or later
    """

    VALUE_01 = "01"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
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
    :cvar VALUE_08: Shrink-wrapped (biodegradable) Use for products or
        product bundles supplied for retail sale in shrink-wrapped
        packaging, where the shrink-wrap film is biodegradable. For non-
        degradable film, see code 21. Only for use in ONIX 3.0 or later
    :cvar VALUE_09: In box (with lid) Individual item, items or set in
        card box with separate or hinged lid: not to be confused with
        the commonly-used ‘boxed set’ which is more likely to be
        packaged in a slip case
    :cvar VALUE_10: Slip-cased Slip-case for single item only (de:
        ‘Schuber’)
    :cvar VALUE_11: Slip-cased set Slip-case for multi-volume set, also
        commonly referred to as ‘boxed set’ (de: ‘Kassette’)
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
        biodegradable shrink-wrap film, prefer code 08. For shrink-
        wrapped packs of multiple products for trade supply only, see
        code XL in List 7
    :cvar VALUE_22: Blister pack A pack comprising a pre-formed plastic
        blister and a printed card with a heat-seal coating
    :cvar VALUE_23: Carry case A case with carrying handle, typically
        for a set of educational books and/or learning materials
    :cvar VALUE_24: In tin Individual item, items or set in metal box or
        can with separate or hinged lid
    :cvar VALUE_25: With browse-prevention tape (ja: koguchi tome)
        Peelable sticker or tape sealing the foredge of a book to
        prevent pre-purchase reading of the content. Only for use in
        ONIX 3.0 or later
    """

    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_05 = "05"
    VALUE_06 = "06"
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


class List81(Enum):
    """
    Product content type.

    :cvar VALUE_10: Text Readable text of the main content: this value
        is required, together with applicable &lt;ProductForm&gt; and
        &lt;ProductFormDetail&gt; values, to designate an e-book or
        other digital or physical product whose primary content is text.
        Note ‘text’ is ‘text-as-text’, not ‘text as an image’ or images
        of text
    :cvar VALUE_15: Extensive links between internal content
        E-publication contains a significant number of actionable
        (clickable) cross-references, hyperlinked notes and annotations,
        or with other actionable links between largely textual elements
        (eg quiz/test questions, ‘choose your own ending’ etc)
    :cvar VALUE_14: Extensive links to external content E-publication
        contains a significant number of actionable (clickable) web
        links to external content, downloadable resources, supplementary
        material, etc
    :cvar VALUE_51: Links to external interactive content Publication
        contains actionable (clickable) links to external interactive
        content. Only for use in ONIX 3.0 or later
    :cvar VALUE_16: Additional text not part of main content Publication
        contains additional textual content such as an interview,
        feature article, essay, bibliography, quiz/test, other
        background material, or text that is not included in a primary
        or ‘unenhanced’ version. Note ‘text’ is ‘text-as-text’, not
        ‘text as an image’ or images of text
    :cvar VALUE_45: Text within images Including text-as-text embedded
        in diagrams, charts, or within images containing speech
        balloons, thought bubbles, captions etc. Note this does not
        include ‘text as an image’ or images of text (for which see code
        49). Only for use in ONIX 3.0 or later
    :cvar VALUE_41: Additional eye-readable links to external content
        Publication contains a significant number of web links (printed
        URLs, QR codes etc). Only for use in ONIX 3.0 or later
    :cvar VALUE_17: Promotional text for other book product Publication
        contains supplementary text as promotional content such as, for
        example, a teaser chapter
    :cvar VALUE_11: Musical notation
    :cvar VALUE_07: Still images / graphics Includes any type of
        illustrations. Use only when no more detailed specification is
        provided
    :cvar VALUE_18: Photographs Whether in a plate section / insert, or
        not
    :cvar VALUE_19: Figures, diagrams, charts, graphs Including other
        ‘mechanical’ (ie non-photographic) illustrations
    :cvar VALUE_20: Additional images / graphics not part of main work
        Publication is enhanced with additional images or graphical
        content such as supplementary photographs that are not included
        in a primary or ‘unenhanced’ version
    :cvar VALUE_12: Maps and/or other cartographic content
    :cvar VALUE_47: Chemical content Indicates that the publication
        contains chemical notations, formulae. Only for use in ONIX 3.0
        or later
    :cvar VALUE_48: Mathematical content Indicates that the publication
        contains mathematical notation, equations, formulae. Only for
        use in ONIX 3.0 or later
    :cvar VALUE_46: Decorative images or graphics Publication contains
        visual content that is purely decorative and are not necessary
        to understanding of the content. Only for use in ONIX 3.0 or
        later
    :cvar VALUE_42: Assessment material eg Questions or student
        exercises, problems, quizzes or tests (as an integral part of
        the work). Only for use in ONIX 3.0 or later
    :cvar VALUE_01: Audiobook Audio recording of a reading of a book or
        other text
    :cvar VALUE_02: Performance – spoken word Audio recording of a drama
        or other spoken word performance
    :cvar VALUE_13: Other speech content eg an interview, speech,
        lecture or commentary / discussion, not a ‘reading’ or
        ‘performance’)
    :cvar VALUE_03: Music recording Audio recording of a music
        performance, including musical drama and opera
    :cvar VALUE_04: Other audio Audio recording of other sound, eg
        birdsong, sound effects, ASMR material
    :cvar VALUE_49: Images of text At least some text – including text
        within other images – is ‘text as an image’ (ie a picture of
        text). Only for use in ONIX 3.0 or later
    :cvar VALUE_21: Partial performance – spoken word Audio recording of
        a reading, performance or dramatization of part of the work
    :cvar VALUE_22: Additional audio content not part of main content
        Product includes additional pre-recorded audio of any
        supplementary material such as full or partial reading, lecture,
        performance, dramatization, interview, background documentary or
        other audio content not included in the primary or ‘unenhanced’
        version
    :cvar VALUE_23: Promotional audio for other book product eg Reading
        of teaser chapter
    :cvar VALUE_06: Video Includes Film, video, animation etc. Use only
        when no more detailed specification is provided. Formerly
        ‘Moving images’
    :cvar VALUE_26: Video recording of a reading
    :cvar VALUE_50: Video content without audio Publication contains
        video material with no audio recording or narration (but may
        have music or textual subtitles) . Only for use in ONIX 3.0 or
        later
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
    :cvar VALUE_34: Blank pages or spaces Entire pages or blank spaces,
        forms, boxes, write-in pages etc, intended to be filled in by
        the reader
    :cvar VALUE_35: Advertising content Use only where type of
        advertising content is not stated
    :cvar VALUE_37: Advertising – first party ‘Back ads’ – promotional
        content for other books (that does not include sample content of
        those books, cf codes 17, 23)
    :cvar VALUE_36: Advertising – coupons Eg to obtain discounts on
        other products
    :cvar VALUE_38: Advertising – third party display
    :cvar VALUE_39: Advertising – third party textual
    :cvar VALUE_40: Scripting E-publication contains microprograms
        written (eg) in Javascript and executed within the reading
        system. Only for use in ONIX 3.0 or later
    :cvar VALUE_43: Scripted pop-ups E-publication contains pop-ups or
        other functionality offering (eg) term definitions, cross-links
        or glossary entries [Note this should not include (eg)
        dictionary functionality that is part of the reading system.]
        Only for use in ONIX 3.0 or later
    :cvar VALUE_44: Sequential art Or pictorial narrative, usually
        panel-based. Images displayed in a specific order for the
        purpose of graphic storytelling or giving information (eg
        graphic novels, comics and manga). May include text integrated
        into the image (as speech and thought bubbles, textual ‘sound’
        effects, captions etc). Only for use in ONIX 3.0 or later
    """

    VALUE_10 = "10"
    VALUE_15 = "15"
    VALUE_14 = "14"
    VALUE_51 = "51"
    VALUE_16 = "16"
    VALUE_45 = "45"
    VALUE_41 = "41"
    VALUE_17 = "17"
    VALUE_11 = "11"
    VALUE_07 = "07"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_12 = "12"
    VALUE_47 = "47"
    VALUE_48 = "48"
    VALUE_46 = "46"
    VALUE_42 = "42"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_13 = "13"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_49 = "49"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_06 = "06"
    VALUE_26 = "26"
    VALUE_50 = "50"
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
    VALUE_40 = "40"
    VALUE_43 = "43"
    VALUE_44 = "44"


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
    :cvar BLA: Biblia de las Americas (LBLA) Spanish translation by the
        Lockman Foundation, first published in 1986 and updated in 1995,
        1997. Only for use in ONIX 3.0 or later
    :cvar BLB: Nueva Biblia de las Americas (NBLA) Updated Spanish
        translation by the Lockman Foundation, first published in 2005.
        Also known as Nueva Biblia Latinoamericana de Hoy (NBLH), Nueva
        Biblia de los Hispanos (NBH), and Nueva Biblia Latinoamericana
        (NBL). Only for use in ONIX 3.0 or later
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
    :cvar NBG: Norsk Bibel 88 Norwegian Bible translation
    :cvar NBH: Bibelen 1978-85/rev. 2005 Norwegian Bible translation
    :cvar NBI: Bibelen 2011 Norwegian Bible translation
    :cvar NBJ: Norsk Bibel 88/rev. 2007 Norwegian Bible translation.
        Only for use in ONIX 3.0 or later
    :cvar NBK: Fauskanger 2015 Norwegian Bible translation with
        commentary. Only for use in ONIX 3.0 or later
    :cvar NBL: Bibelen 2011/rev. 2024 Norwegian Bible translation, 2024
        update of Bibelen 2011. Only for use in ONIX 3.0 or later
    :cvar NBP: Pollestad 2023 Norwegian Bible translation. Only for use
        in ONIX 3.0 or later
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
    :cvar NTV: Nueva Traducción Viviente A Spanish translation from the
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
    BLA = "BLA"
    BLB = "BLB"
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
    NBJ = "NBJ"
    NBK = "NBK"
    NBL = "NBL"
    NBP = "NBP"
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
    Product classification type.

    :cvar VALUE_01: WCO Harmonized System World Customs Organization
        Harmonized Commodity Coding and Description System, the basis of
        most other commodity code schemes. Use 6 digits, without
        punctuation. See
        https://www.wcoomd.org/en/topics/nomenclature/instrument-and-
        tools/hs-nomenclature-2022-edition.aspx and
        https://www.wcotradetools.org/en/harmonized-system
    :cvar VALUE_02: UNSPSC UN Standard Product and Service
        Classification, including national versions adopted without any
        additions or changes to the codes or their meaning. Use 8 (or
        occasionally 10) digits, without punctuation
    :cvar VALUE_03: HMRC UK Revenue and Customs classifications, based
        on the Harmonized System (8 or 10 digits, without punctuation,
        for exports from and imports into the UK respectively). See
        https://www.gov.uk/trade-tariff
    :cvar VALUE_04: Warenverzeichnis für die Außenhandelsstatistik
        German export trade classification, based on the Harmonised
        System
    :cvar VALUE_05: TARIC EU TARIC codes, an extended version of the
        Harmonized System primarily for imports into the EU. Use 10
        digits, without punctuation. See https://taxation-
        customs.ec.europa.eu/customs-4/calculation-customs-
        duties/customs-tariff/eu-customs-tariff-taric_en
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
        Use 6 digits, without punctuation. For example, printed
        children’s books are ‘58.11.13’, but the periods are normally
        ommited in ONIX
    :cvar VALUE_10: NCM Mercosur/Mercosul Common Nomenclature, based on
        the Harmonised System. Use 8 digits, without punctuation
    :cvar VALUE_11: CPV Common Procurement Vocabulary (2008), used to
        describe products and services for public tendering and
        procurement within the EU. Code is a nine digit number
        (including the check digit), and may also include a space plus
        an alphanumeric code of two letters and three digits (including
        the supplementary check digit) from the Supplementary
        Vocabulary. See https://simap.ted.europa.eu/web/simap/cpv
    :cvar VALUE_12: PKWiU Polish Classification of Products and Services
        (2015). Use a single letter followed by 2 to 7 digits, without
        punctuation. Only for use in ONIX 3.0 or later
    :cvar VALUE_13: HTSUS US HTS (or HTSA) commodity codes for import of
        goods into USA (10 digits, without punctuation). Only for use in
        ONIX 3.0 or later. See https://hts.usitc.gov/current
    :cvar VALUE_14: US Schedule B US Schedule B commodity codes for
        export from USA (10 digits, without punctuation). Only for use
        in ONIX 3.0 or later. See http://uscensus.prod.3ceonline.com
    :cvar VALUE_15: Clave SAT Mexican SAT classification, based on UN
        SPSC with later modifications (8 digits, without punctuation).
        Only for use in ONIX 3.0 or later. See
        https://www.sat.gob.mx/consultas/53693/catalogo-de-productos-y-
        servicios
    :cvar VALUE_16: CN EU Combined Nomenclature commodity codes, an
        extended version of the Harmonized System primarily for exports
        from the EU. Use 8 digits, without punctuation. Only for use in
        ONIX 3.0 or later. See https://trade.ec.europa.eu/access-to-
        markets/en/content/combined-nomenclature-0
    :cvar VALUE_17: CCT Canadian Customs Tariff scheme, 8 or 10 digits
        for imports into and exports from Canada. Only for use in ONIX
        3.0 or later. See https://www.cbsa-asfc.gc.ca/trade-
        commerce/tariff-tarif/menu-eng.html
    :cvar VALUE_18: CACT Australian ‘Working tariff’. Combined
        Australian Customs Tariff Nomenclature and Statistical
        Classification. Only for use in ONIX 3.0 or later. See
        https://www.abf.gov.au/importing-exporting-and-
        manufacturing/tariff-classification
    :cvar VALUE_19: NICO Mexican Número de Identificación Comercial, 10
        digits for imports into and exports from Mexico. Only for use in
        ONIX 3.0 or later. See
        https://www.snice.gob.mx/cs/avi/snice/nico.ligie.html
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
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_50 = "50"


class List90(Enum):
    """
    Religious text feature.

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
    Country – based on ISO 3166-1.

    :cvar AD: Andorra
    :cvar AE: United Arab Emirates
    :cvar AF: Afghanistan
    :cvar AG: Antigua and Barbuda
    :cvar AI: Anguilla
    :cvar AL: Albania
    :cvar AM: Armenia
    :cvar AN: Netherlands Antilles Deprecated – use BQ, CW and SX as
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
    :cvar CS: Serbia and Montenegro Deprecated, replaced by ME –
        Montenegro and RS – Serbia
    :cvar CU: Cuba
    :cvar CV: Cabo Verde
    :cvar CW: Curaçao
    :cvar CX: Christmas Island
    :cvar CY: Cyprus
    :cvar CZ: Czechia Formerly Czech Republic
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
    :cvar MD: Moldova, Republic of
    :cvar ME: Montenegro
    :cvar MF: Saint Martin (French part)
    :cvar MG: Madagascar
    :cvar MH: Marshall Islands
    :cvar MK: North Macedonia Formerly FYR Macedonia
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
    :cvar SZ: Eswatini Formerly known as Swaziland
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
    :cvar TR: Türkiye Formerly known as Turkey
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
    :cvar YU: Yugoslavia Deprecated, replaced by ME – Montenegro and RS
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
    :cvar VALUE_02: Proprietary Deprecated – use code 01
    :cvar VALUE_04: Börsenverein Verkehrsnummer
    :cvar VALUE_05: German ISBN Agency publisher identifier
    :cvar VALUE_06: GLN GS1 global location number (formerly EAN
        location number)
    :cvar VALUE_07: SAN Book trade Standard Address Number – US, UK etc
    :cvar VALUE_12: Distributeurscode Boekenbank Flemish supplier code
    :cvar VALUE_13: Fondscode Boekenbank Flemish publisher code
    :cvar VALUE_16: ISNI International Standard Name Identifier (used
        here to identify an organization). Only for use in ONIX 3.0 or
        later. See https://isni.org/
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
    VALUE_16 = "16"
    VALUE_23 = "23"


class List93(Enum):
    """
    Supplier role.

    :cvar VALUE_00: Unspecified Default
    :cvar VALUE_01: Publisher to resellers Publisher as supplier to
        retail trade outlets
    :cvar VALUE_02: Publisher’s exclusive distributor to resellers
    :cvar VALUE_03: Publisher’s non-exclusive distributor to resellers
    :cvar VALUE_04: Wholesaler to retailers Wholesaler supplying retail
        trade outlets
    :cvar VALUE_05: Sales agent Deprecated – use
        &lt;MarketRepresentation&gt; (ONIX 2.1) or
        &lt;MarketPublishingDetail&gt; (ONIX 3.0 or later) to specify a
        sales agent
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
    :cvar VALUE_13: Exclusive distributor to resellers and end-customers
        Intermediary as exclusive distributor to retailers and direct to
        consumers and/or institutional customers. Only for use in ONIX
        3.0 or later
    :cvar VALUE_14: Non-exclusive distributor to resellers and end-
        customers Intermediary as non-exclusive distributor to retailers
        and direct to consumers and/or institutional customers. Only for
        use in ONIX 3.0 or later
    :cvar VALUE_15: Distributor to resellers and end-customers Use only
        where exclusive/non-exclusive status is not known. Prefer codes
        13 or 14 as appropriate whenever possible. Only for use in ONIX
        3.0 or later
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


class List96(Enum):
    """
    Currency code – based on ISO 4217.

    :cvar AED: UAE Dirham United Arab Emirates
    :cvar AFA: Afghani Afghanistan. Deprecated, replaced by AFN
    :cvar AFN: Afghani Afghanistan (prices normally quoted as integers)
    :cvar ALL: Lek Albania (prices normally quoted as integers)
    :cvar AMD: Armenian Dram Armenia (prices normally quoted as
        integers)
    :cvar ANG: Netherlands Antillian Guilder Curaçao, Sint Maarten
    :cvar AOA: Kwanza Angola
    :cvar ARS: Argentine Peso Argentina
    :cvar ATS: Schilling Austria. Now replaced by the Euro (EUR).
        Deprecated – use only for historical prices that pre-date the
        introduction of the Euro
    :cvar AUD: Australian Dollar Australia, Christmas Island, Cocos
        (Keeling) Islands, Heard Island and McDonald Islands, Kiribati,
        Nauru, Norfolk Island, Tuvalu
    :cvar AWG: Aruban Florin Aruba
    :cvar AZN: Azerbaijan Manat Azerbaijan
    :cvar BAM: Convertible Marks Bosnia and Herzegovina
    :cvar BBD: Barbados Dollar Barbados
    :cvar BDT: Taka Bangladesh
    :cvar BEF: Belgian Franc Belgium. Now replaced by the Euro (EUR).
        Deprecated – use only for historical prices that pre-date the
        introduction of the Euro
    :cvar BGL: Bulgarian Lev Deprecated, replaced by BGN
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
    :cvar BYR: (Old) Belarussian Ruble Belarus (prices normally quoted
        as integers). Deprecated – now replaced by new Belarussian Ruble
        (BYN): use only for historical prices that pre-date the
        introduction of the new Belarussian Ruble
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
    :cvar CYP: Cyprus Pound Cyprus. Now replaced by the Euro (EUR).
        Deprecated – use only for historical prices that pre-date the
        introduction of the Euro
    :cvar CZK: Czech Koruna Czechia
    :cvar DEM: Mark Germany. Now replaced by the Euro (EUR). Deprecated
        – use only for historical prices that pre-date the introduction
        of the Euro
    :cvar DJF: Djibouti Franc Djibouti (prices normally quoted as
        integers)
    :cvar DKK: Danish Krone Denmark, Faroe Islands, Greenland
    :cvar DOP: Dominican Peso Dominican Republic
    :cvar DZD: Algerian Dinar Algeria
    :cvar EEK: Kroon Estonia.Now replaced by the Euro (EUR). Deprecated
        – use only for historical prices that pre-date the introduction
        of the Euro
    :cvar EGP: Egyptian Pound Egypt
    :cvar ERN: Nakfa Eritrea
    :cvar ESP: Peseta Spain. Now replaced by the Euro (EUR). Deprecated
        – use only for historical prices that pre-date the introduction
        of the Euro (prices normally quoted as integers)
    :cvar ETB: Ethiopian Birr Ethiopia
    :cvar EUR: Euro Eurozone: Andorra, Austria, Belgium, Croatia,
        Cyprus, Estonia, Finland, France, Fr Guiana, Fr S Territories,
        Germany, Greece, Guadeloupe, Holy See (Vatican City), Ireland,
        Italy, Latvia, Lithuania, Luxembourg, Martinique, Malta,
        Mayotte, Monaco, Montenegro, Netherlands, Portugal, Réunion, St
        Barthelemy, St Martin, St Pierre and Miquelon, San Marino,
        Slovakia, Slovenia, Spain
    :cvar FIM: Markka Finland. Now replaced by the Euro (EUR).
        Deprecated – use only for historical prices that pre-date the
        introduction of the Euro
    :cvar FJD: Fiji Dollar Fiji
    :cvar FKP: Falkland Islands Pound Falkland Islands (Malvinas)
    :cvar FRF: Franc France. Now replaced by the Euro (EUR). Deprecated
        – use only for historical prices that pre-date the introduction
        of the Euro
    :cvar GBP: Pound Sterling United Kingdom, Isle of Man, Channel
        Islands, South Georgia, South Sandwich Islands, British Indian
        Ocean Territory (de jure)
    :cvar GEL: Lari Georgia
    :cvar GHC: Ghana Cedi Deprecated, replaced by GHS
    :cvar GHS: Ghana Cedi Ghana
    :cvar GIP: Gibraltar Pound Gibraltar
    :cvar GMD: Dalasi Gambia
    :cvar GNF: Guinean Franc Guinea (prices normally quoted as integers)
    :cvar GRD: Drachma Greece. Now replaced by the Euro (EUR).
        Deprecated – use only for historical prices that pre-date the
        introduction of the Euro
    :cvar GTQ: Quetzal Guatemala
    :cvar GWP: Guinea-Bissau Peso Now replaced by the CFA Franc BCEAO
        XOF use only for historical prices that pre-date use of the CFA
        Franc
    :cvar GYD: Guyana Dollar Guyana (prices normally quoted as integers)
    :cvar HKD: Hong Kong Dollar Hong Kong
    :cvar HNL: Lempira Honduras
    :cvar HRK: Kuna Croatia. Now replaced by the Euro (EUR). Deprecated
        – use only for historical prices that pre-date the introduction
        of the Euro
    :cvar HTG: Gourde Haiti
    :cvar HUF: Forint Hungary (prices normally quoted as integers)
    :cvar IDR: Rupiah Indonesia (prices normally quoted as integers)
    :cvar IEP: Punt Ireland. Now replaced by the Euro (EUR). Deprecated
        – use only for historical prices that pre-date the introduction
        of the Euro
    :cvar ILS: New Israeli Sheqel Israel
    :cvar INR: Indian Rupee India, Bhutan (prices normally quoted as
        integers)
    :cvar IQD: Iraqi Dinar Iraq (prices normally quoted as integers)
    :cvar IRR: Iranian Rial Iran (Islamic Republic of) (prices normally
        quoted as integers)
    :cvar ISK: Iceland Krona Iceland (prices normally quoted as
        integers)
    :cvar ITL: Lira Italy. Now replaced by the Euro (EUR). Deprecated –
        use only for historical prices that pre-date the introduction of
        the Euro (prices normally quoted as integers)
    :cvar JMD: Jamaican Dollar Jamaica
    :cvar JOD: Jordanian Dinar Jordan (prices normally quoted with 3
        decimal places)
    :cvar JPY: Yen Japan (prices normally quoted as integers)
    :cvar KES: Kenyan Shilling Kenya
    :cvar KGS: Som Kyrgyzstan
    :cvar KHR: Riel Cambodia
    :cvar KMF: Comorian Franc Comoros (prices normally quoted as
        integers)
    :cvar KPW: North Korean Won Korea (Democratic People’s Republic of)
        (prices normally quoted as integers)
    :cvar KRW: Won Korea (Republic of) (prices normally quoted as
        integers)
    :cvar KWD: Kuwaiti Dinar Kuwait (prices normally quoted with 3
        decimal places)
    :cvar KYD: Cayman Islands Dollar Cayman Islands
    :cvar KZT: Tenge Kazakstan
    :cvar LAK: Lao Kip Lao People’s Democratic Republic (prices normally
        quoted as integers)
    :cvar LBP: Lebanese Pound Lebanon (prices normally quoted as
        integers)
    :cvar LKR: Sri Lanka Rupee Sri Lanka
    :cvar LRD: Liberian Dollar Liberia
    :cvar LSL: Loti Lesotho
    :cvar LTL: Litus Lithuania. Now replaced by the Euro (EUR).
        Deprecated – use only for historical prices that pre-date the
        introduction of the Euro
    :cvar LUF: Luxembourg Franc Luxembourg. Now replaced by the Euro
        (EUR). Deprecated – use only for historical prices that pre-date
        the introduction of the Euro (prices normally quoted as
        integers)
    :cvar LVL: Latvian Lats Latvia. Now replaced by the Euro (EUR).
        Deprecated – use only for historical prices that pre-date the
        introduction of the Euro
    :cvar LYD: Libyan Dinar Libyan Arab Jamahiriya (prices normally
        quoted with 3 decimal places)
    :cvar MAD: Moroccan Dirham Morocco, Western Sahara
    :cvar MDL: Moldovan Leu Moldova, Republic of
    :cvar MGA: Malagasy Ariary Madagascar (prices normally quoted with 0
        or 1 decimal place – 1 iraimbilanja = Ar0.2)
    :cvar MGF: Malagasy Franc Now replaced by the Ariary (MGA) (prices
        normally quoted as integers)
    :cvar MKD: Denar North Macedonia (formerly FYR Macedonia)
    :cvar MMK: Kyat Myanmar (prices normally quoted as integers)
    :cvar MNT: Tugrik Mongolia (prices normally quoted as integers)
    :cvar MOP: Pataca Macau
    :cvar MRO: (Old) Ouguiya Mauritania (prices normally quoted with 0
        or 1 decimal place – 1 khoums = UM0.2). Was interchangeable with
        MRU (New) Ouguiya at rate of 10:1 until June 2018. Deprecated,
        use MRU instead
    :cvar MRU: Ouguiya Mauritania (prices normally quoted with 0 or 1
        decimal place – 1 khoums = UM0.2). Replaced MRO (old) Ouguiya at
        rate of 10:1 in June 2018. Only for use in ONIX 3.0 or later
    :cvar MTL: Maltese Lira Malta. Now replaced by the Euro (EUR).
        Deprecated – use only for historical prices that pre-date the
        introduction of the Euro
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
    :cvar NLG: Guilder Netherlands. Now replaced by the Euro (EUR).
        Deprecated – use only for historical prices that pre-date the
        introduction of the Euro
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
    :cvar PLN: Złoty Poland
    :cvar PTE: Escudo Portugal. Now replaced by the Euro (EUR).
        Deprecated – use only for historical prices that pre-date the
        introduction of the Euro
    :cvar PYG: Guarani Paraguay (prices normally quoted as integers)
    :cvar QAR: Qatari Rial Qatar
    :cvar ROL: Romanian Old Leu Deprecated, replaced by RON
    :cvar RON: Romanian Leu Romania
    :cvar RSD: Serbian Dinar Serbia (prices normally quoted as integers)
    :cvar RUB: Russian Ruble Russian Federation
    :cvar RUR: Russian Ruble Deprecated, replaced by RUB
    :cvar RWF: Rwanda Franc Rwanda (prices normally quoted as integers)
    :cvar SAR: Saudi Riyal Saudi Arabia
    :cvar SBD: Solomon Islands Dollar Solomon Islands
    :cvar SCR: Seychelles Rupee Seychelles
    :cvar SDD: Sudanese Dinar Now replaced by the Sudanese Pound (SDG)
    :cvar SDG: Sudanese Pound Sudan
    :cvar SEK: Swedish Krona Sweden
    :cvar SGD: Singapore Dollar Singapore
    :cvar SHP: Saint Helena Pound Saint Helena
    :cvar SIT: Tolar Slovenia. Now replaced by the Euro (EUR).
        Deprecated – use only for historical prices that pre-date the
        introduction of the Euro
    :cvar SKK: Slovak Koruna Slovakia. Now replaced by the Euro (EUR).
        Deprecated – use only for historical prices that pre-date the
        introduction of the Euro
    :cvar SLE: Leone Sierra Leone (from April 2022). Only for use in
        ONIX 3.0 or later
    :cvar SLL: Leone Sierra Leone (prices normally quoted as integers).
        Deprecated – gradually replaced by SLE from April 2022, but SLL
        Leone still usable until December 2023 (SLE is a redenomination
        of the Leone by a factor of 1,000)
    :cvar SOS: Somali Shilling Somalia (prices normally quoted as
        integers)
    :cvar SRD: Surinam Dollar Suriname
    :cvar SRG: Suriname Guilder DEPRECATED, replaced by SRD
    :cvar STD: (Old) Dobra São Tome and Principe (prices normally quoted
        as integers). Was interchangeable with STN (New) Dobra at rate
        of 1000:1 until June 2018. Deprecated, use STN instead
    :cvar STN: Dobra São Tome and Principe. Replaced STD (old) Dobra at
        rate of 1000:1 in June 2018. Only for use in ONIX 3.0 or later
    :cvar SVC: El Salvador Colon El Salvador
    :cvar SYP: Syrian Pound Syrian Arab Republic (prices normally quoted
        as integers)
    :cvar SZL: Lilangeni Eswatini (formerly known as Swaziland)
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
    :cvar TRY: Turkish Lira Türkiye, from 1 January 2005
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
    :cvar VEB: Bolívar Deprecated, replaced by VEF
    :cvar VEF: Bolívar Venezuela (formerly Bolívar fuerte). Deprecated,
        replaced by VES
    :cvar VES: Bolívar Soberano Venezuela (replaced VEF from August 2018
        at rate of 100,000:1, and was redenominated by a further factor
        of 1,000,000:1 in late 2021). Only for use in ONIX 3.0 or later
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
    :cvar YUM: Yugoslavian Dinar Deprecated, replaced by CSD
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
    MRU = "MRU"
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
    SLE = "SLE"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    SRG = "SRG"
    STD = "STD"
    STN = "STN"
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
    VES = "VES"
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
