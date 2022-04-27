# python-onix

A very simple module to provide dataclasses for EDItEUR's ONIX standards. Mostly generated using [xsdata](https://github.com/tefra/xsdata).

This module isn't even in the Alpha stage yet, and there may be breaking changes.

Currently, only ONIX for Books is covered; but I may add ONIX for Subscription Products in the near future.

## Installation
Install using pip:
~~~bash
pip install python-onix
~~~

## Getting Started
#### Parse an ONIX file
~~~python
from onix.book.v3_0.short.strict import Onixmessage
from xsdata.formats.dataclass.parsers import XmlParser

parser = XmlParser()
message = parser.parse("/some/path/file.onx", Onixmessage)
~~~