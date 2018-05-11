# ValidateQuote File

## Usage

Validating file `C:\data\quotefile.txt` on the command-line with maven:

To run only `rawquotefile` validation tests (do not `processedquotefile`):

```
mvn clean test -Drawquotefile=C:\data\rawquotefile.txt
```

Tests are skipped if properties are not defined.


To run both:

```
mvn clean test -Drawquotefile=C:\data\rawquotefile.txt -Drawquotefile=C:\data\rawquotefile.txt
```

To specify path/spaces:

```
mvn clean test -Drawquotefile=C:\data\rawquotefile.txt -Dprocessedquotefile="C:\data\processed quotefile.txt"
```

----

```
C:\Workspace\ValidateQuoteFile>mvn clean test -Drawquotefile="transfertest77 (1).txt" -Dprocessedquotefile=quote-20180504.txt
```
