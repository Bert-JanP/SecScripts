# CISAPy
CISAPy is a small command line tool that lets you interact with the [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog). 
It offers the following functionalities:
1. Listing (filtered) vulnerabilities
2. Exporting (filtered) vulnerabilities
3. Provide statistics on when the vulnerabilities have been added to the list.

Example of one of the Vulnerabilities in the catalog:
```JSON
  {
    "cveID": "CVE-2023-6448",
    "vendorProject": "Unitronics",
    "product": "Vision PLC and HMI",
    "vulnerabilityName": "Unitronics Vision PLC and HMI Insecure Default Password Vulnerability",
    "dateAdded": "2023-12-11",
    "shortDescription": "Unitronics Vision Series PLCs and HMIs ship with an insecure default password, which if left unchanged, can allow attackers to execute remote commands.",
    "requiredAction": "Apply mitigations per vendor instructions or discontinue use of the product if mitigations are unavailable.",
    "dueDate": "2023-12-18",
    "knownRansomwareCampaignUse": "Unknown",
    "notes": "Note that while it is possible to change the default password, implementors are encouraged to remove affected controllers from public networks per vendor advice: https://www.unitronicsplc.com/cyber_security_vision-samba/"
  }
```

## Requirements
To run this tool python3 must be installed.

# Usage

## Windows

### Help
```PowerShell
PS C:\scripts>  python.exe .\cisapy.py -h
usage: cisapy.py [-h] [-s] [-e] [-y YEAR]

CISAPy by By twitter: @BertJanCyber, Github: Bert-JanP. CISAPy is a commandline tool that lets you interact with the CISA Known Exploited Vulnerabilities Catalog. It lets you fetch the vulnerabilities catalog to dynamic JSON and perform statistics analysis.

optional arguments:
  -h, --help            show this help message and exit
  -s, --stats           Show statistics of vulnerabilities added for each year
  -e, --export          Export vulnerabilities to a JSON file
  -y YEAR, --year YEAR  Filter entries equal to or newer than the specified YEAR (format: YYYY)
```

### List all vulnerabilities
```PowerShell
PS C:\scripts> python.exe .\cisapy.py
```

### List vulnerabilities that have been added in 2022 or newer
```PowerShell
PS C:\scripts> python.exe .\cisapy.py -y 2022
```

### List export results to JSON file
```PowerShell
PS C:\scripts> python.exe .\cisapy.py -y 2022 -e
Exported vulnerabilities to 'exported_cisa_vulnerabilities.json'
```

### List statistics

```Bash
PS C:\scripts> python.exe .\cisapy.py -s
Vulnerabilities added in
{
  "2021": 311,
  "2022": 555,
  "2023": 185
}
```

## Linux

### Help
```Bash
bert-jan@ubuntu:~/scripts$ python3 cisapy.py -h
usage: cisapy.py [-h] [-s] [-e] [-y YEAR]

CISAPy by By twitter: @BertJanCyber, Github: Bert-JanP. CISAPy is a commandline tool that lets you interact with the CISA Known Exploited Vulnerabilities Catalog. It lets you fetch the vulnerabilities catalog to dynamic JSON and perform statistics analysis.

options:
  -h, --help            show this help message and exit
  -s, --stats           Show statistics of vulnerabilities added for each year
  -e, --export          Export vulnerabilities to a JSON file
  -y YEAR, --year YEAR  Filter entries equal to or newer than the specified
                        YEAR (format: YYYY)
```

### List all vulnerabilities
```Bash
bert-jan@ubuntu:~/scripts$ python3 cisapy.py
```

### List vulnerabilities that have been added in 2022 or newer
```Bash
bert-jan@ubuntu:~/scripts$ python3 cisapy.py -y 2022
```

### List export results to JSON file
```Bash
bert-jan@ubuntu:~/scripts$ python3 cisapy.py -y 2022 -e
Exported vulnerabilities to 'exported_cisa_vulnerabilities.json'
```

### List statistics

```Bash
bert-jan@ubuntu:~/scripts$ python3 cisapy.py -s
Vulnerabilities added in
{
  "2021": 311,
  "2022": 555,
  "2023": 185
}
```