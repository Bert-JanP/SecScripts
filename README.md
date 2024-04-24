# Security Scripts & Sources

Welcome to the SecScripts repository! This collection of **security scripts and sources** is designed to assist you in automating various security-related tasks and to list sources that are relavant to security related topics. Whether you're a security professional, a system administrator, or an enthusiast, these scripts aim to simplify your workflow and enhance your efficiency. 

#### Scripts
This repository contains a list with scripts that I use to automate security related tasks. The reason I store them in this repository is organize them in a convienient manner. The advantage of this is that the scripts can be shared with others, so they do not need to reinvent the wheel.

#### Sources
The sources section (below) lists relavant sources which I use for a variety of tasks. Feel free to check them out!

## Contributing

We welcome contributions from the security community. If you have a script or sources that you believe would be beneficial to others, feel free to submit a pull request. 

# Cyber Sources

# Documentation
## General
- https://attack.mitre.org/ - MITRE ATT&CK® is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations.
- https://threats.wiz.io/ - Cloud Threat Landscape
- https://www.threat-intel.xyz/ - Free and Open Source Threat Intelligence Feeds
- https://www.microsoft.com/en-us/security/blog/2023/12/05/microsoft-incident-response-lessons-on-preventing-cloud-identity-compromise/ - Microsoft Incident Response lessons on preventing cloud identity compromise

## Security Architecture
- https://learn.microsoft.com/en-us/azure/security/fundamentals/best-practices-and-patterns - Azure security best practices and patterns
- https://learn.microsoft.com/en-us/azure/active-directory/architecture/security-operations-user-accounts - Security Operations Guide Azure Active Directory

## Tools

- https://github.com/rabobank-cdc/DeTTECT - Detect Tactics, Techniques & Combat Threats

## Information Repositories

## Security Tooling

### Microsoft Incident lookup
- https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-risks - What are risk detections?

### MDE
- https://securityoccupied.com/2023/06/15/taking-actions-on-mde-devices-via-powershell-and-mde-api/ - In an attempt to learn more about the Microsoft Defender for Endpoint (MDE) API available for investigative actions on machines, I have created a PowerShell script that can perform several machine actions for single devices and also in bulk.

#### MDE Blogs
- https://medium.com/@DFIRanjith/remote-collection-of-windows-forensic-artifacts-using-kape-and-microsoft-defender-for-endpoint-f7d3a857e2e0 - Remote collection of Windows Forensic Artifacts using KAPE and Microsoft Defender for Endpoint.

### Sentinel
- https://github.com/Azure/Azure-Sentinel-Notebooks - Interactive Azure Sentinel Notebooks provides security insights and actions to investigate anomalies and hunt for malicious behaviors. 

#### Sentinel Blogs
- https://medium.com/@truvis.thornton/microsoft-azure-sentinel-adding-tlps-traffic-light-patterns-to-incidents-alerts-and-analytics-f05e0b2f171e - Microsoft Azure Sentinel: Adding TLPs (Traffic Light Protocol) to Incidents, Alerts and Analytics Rules.

### Microsoft Graph Security

- https://learn.microsoft.com/en-us/connectors/microsoftgraphsecurity/ - The Microsoft Graph Security connector helps to connect different Microsoft and partner security products and services, using a unified schema, to streamline security operations, and improve threat protection, detection, and response capabilities.

### Other
- https://www.echotrail.io/insights - Look up description, commonality, behavior, and more by searching through our extensive insights database.
- https://github.com/indetectables-net/toolkit - The essential toolkit for reversing, malware analysis, and cracking

---
## Red Teaming
- https://github.com/ihebski/DefaultCreds-cheat-sheet/blob/main/DefaultCreds-Cheat-Sheet.csv - One place for all the default credentials to assist the Blue/Red teamers activities on finding devices with default password

### Attack Simulation
- https://github.com/redcanaryco/atomic-red-team/tree/master - Small and highly portable detection tests based on MITRE's ATT&CK.
- https://github.com/redcanaryco/invoke-atomicredteam - Invoke-AtomicRedTeam is a PowerShell module to execute tests as defined in the [atomics folder](https://github.com/redcanaryco/atomic-red-team/tree/master/atomics) of Red Canary's Atomic Red Team project.
- https://github.com/tsale/EDR-Telemetry - This project aims to compare and evaluate the telemetry of various EDR products.
- https://github.com/Orange-Cyberdefense/GOAD - game of active directory
- https://github.com/RedSiege/GraphStrike - Cobalt Strike HTTPS beaconing over Microsoft Graph API
- https://github.com/RedByte1337/GraphSpy - Initial Access and Post-Exploitation Tool for AAD and O365 with a browser-based GUI

### Tools
- https://stratus-red-team.cloud/ - ☁️ ⚡ Granular, Actionable Adversary Emulation for the Cloud

---
## Ransomware
- https://github.com/fastfire/deepdarkCTI/blob/main/ransomware_gang.md - Collection of Cyber Threat Intelligence sources from the deep and dark web
- https://ransomwhe.re/#browse - Ransomwhere is the open, crowdsourced ransomware payment tracker. Browse and download ransomware payment data or help build our dataset by reporting ransomware demands you have received.
---
## Threat Hunting
- https://www.giac.org/paper/gsec/23549/hunting-gathering-powershell/121279
- https://www.betaalvereniging.nl/en/safety/tahiti/ - TaHiTI Threat Hunting Methodology
- https://www.betaalvereniging.nl/wp-content/uploads/DEF-TaHiTI-Threat-Hunting-Methodology.pdf - A joint threat hunting methodology from the Dutch financial sector

---
## Threat Intelligence 
- https://github.com/fastfire/deepdarkCTI - Collection of Cyber Threat Intelligence sources from the deep and dark web
---
## Detection Engineering
- https://github.com/infosecB/awesome-detection-engineering - A list of useful Detection Engineering-related resources.

### Standardized Detection Formats
- https://github.com/SigmaHQ/sigma - Main Sigma Rule Repository
- https://github.com/Yara-Rules/rules - Repository of yara rules
- https://github.com/InQuest/awesome-yara#rules - A curated list of awesome YARA rules, tools, and people.
- https://www.snort.org/downloads/#rule-downloads - Snort community ruleset


### KQL
- https://kqlquery.com/ - Stay informed, stay secure, and stay one step ahead of adversaries with KQL
- https://www.kqlsearch.com/ - This is an aggregator for KQL queries that are shared on GitHub.
- https://github.com/Bert-JanP/Hunting-Queries-Detection-Rules - KQL Queries. Defender For Endpoint and Azure Sentinel Hunting and Detection Queries in KQL. Out of the box KQL queries for: Advanced Hunting, Custom Detection, Analytics Rules & Hunting Rules.
- https://github.com/Cyb3r-Monk/Threat-Hunting-and-Detection - Repository for threat hunting and detection queries, etc. for Defender for Endpoint and Microsoft Sentinel in KQL(Kusto Query Language).
- https://github.com/reprise99/Sentinel-Queries - Collection of KQL queries
- https://github.com/FalconForceTeam/FalconFriday - Hunting queries and detections
- https://github.com/Azure/Azure-Sentinel - About Cloud-native SIEM for intelligent security analytics for your entire enterprise.
- https://github.com/Cloud-Architekt/AzureSentinel - Sharing my KQL queries for Azure Sentinel
- https://github.com/alexverboon/Hunting-Queries-Detection-Rules - KQL Queries. Microsoft 365 Defender, Microsoft Sentinel
- https://github.com/f-bader/AzSentinelQueries - Microsoft Sentinel hunting queries and Analytics rules
- https://github.com/wortell/KQL - KQL queries for Advanced Hunting
- https://gist.github.com/Shivammalaviya - KQL Security Queries
- https://github.com/rod-trent/SentinelKQL - Azure Sentinel KQL
- https://github.com/invictus-ir/Invictus-training/tree/main/KQL-QueryPack - Invictus: Cloud Incident Response Query Pack
- https://github.com/JesseEsquivel/MDATP/tree/master/AdvancedHunting - Microsoft Defender Advanced Threat Protection
- https://kustoinsights.substack.com/ - Kusto Insights newletter
- https://github.com/0xAnalyst/DefenderATPQueries - Hunting Queries for Defender ATP
- https://github.com/LearningKijo/KQL - Threat Hunting query in Microsoft 365 Defender, XDR. Provide out-of-the-box KQL hunting queries - App, Email, Identity and Endpoint.
- https://github.com/KostasKoutrou/KQL/tree/main - KQL Queries for Advanced Hunting / Log Analytics
- https://identityandsecuritydotcom.files.wordpress.com/2020/05/kql_internals_sentinel.pdf - Kusto Query Internals: Hunting TTPs with Azure Sentinel
---
## Incident Response

- https://www.microsoft.com/content/dam/microsoft/final/en-us/microsoft-brand/documents/MS-IR-Playbook-Final.pdf%20 - Navigating the Maze of Incident Response

### Google Workspace
- https://github.com/invictus-ir/ALFA - ALFA stands for Automated Audit Log Forensic Analysis for Google Workspace. You can use this tool to acquire all Google Workspace audit logs and to perform automated forensic analysis on the audit logs using statistics and the MITRE ATT&CK Cloud Framework

### UNIX
- https://github.com/tclahr/uac - UAC is a Live Response collection script for Incident Response that makes use of native binaries and tools to automate the collection of AIX, Android, ESXi, FreeBSD, Linux, macOS, NetBSD, NetScaler, OpenBSD and Solaris systems artifacts.

### Windows
- https://www.kroll.com/en/services/cyber-risk/incident-response-litigation-support/kroll-artifact-parser-extractor-kape - Kroll's Artifact Parser and Extractor (KAPE) – created by Kroll senior director and three-time Forensic 4:cast DFIR Investigator of the Year Eric Zimmerman – lets forensic teams collect and process forensically useful artifacts within minutes.

## Microsoft Azure & Office 365
- https://github.com/invictus-ir/Microsoft-Extractor-Suite - A PowerShell module for acquisition of data from Microsoft 365 and Azure for Incident Response and Cyber Security purposes.
- https://github.com/PwC-IR/Business-Email-Compromise-Guide - The Business Email Compromise Guide sets out to describe 10 steps for performing a Business Email Compromise (BEC) investigation in an Office 365 environment. Each step is intended to guide the process of identifying, collecting and analysing activity associated with BEC intrusions.

## Other
- https://github.com/DebugPrivilege/InsightEngineering/ - This GitHub repository dives into fundamental concepts I believe are important for understanding debugging and troubleshooting complex issues on Windows.
- https://github.com/FriedrichWeinmann/PkiExtension - Welcome to the PKI Extension PowerShell module project.
- https://digger.tools/
- https://www.microsoft.com/en-us/security/blog/2024/01/17/new-microsoft-incident-response-guides-help-security-teams-analyze-suspicious-activity/ - New Microsoft Incident Response guides help security teams analyze suspicious activity
- https://privacy.sexy/ - Enforce privacy & security best-practices on Windows, macOS and Linux.
- https://br0k3nlab.com/resources/zen-of-security-rules/ - The Zen of python does a perfect job succinctly capturing guiding principles for developing via 19 aphorisms. This is the zen of writing security rules, for fostering high-quality, high-efficacy rules as simply as possible.
- https://github.com/WithSecureLabs/lolcerts - A repository of code signing certificates known to have been leaked or stolen, then abused by threat actors
- https://learn.microsoft.com/en-us/purview/audit-log-activities - Audit log activities
- https://techcommunity.microsoft.com/t5/microsoft-security-experts-blog/strategies-to-monitor-and-prevent-vulnerable-driver-attacks/ba-p/4103985 - Strategies to monitor and prevent vulnerable driver attacks
- https://www.xintra.org/labs - XINTRA Labs

## Reports
- https://www.microsoft.com/en-us/security/security-insider/microsoft-digital-defense-report-2023 - Microsoft Digital Defense Report 2023
- https://services.google.com/fh/files/misc/m-trends-2024.pdf - M-Trends 2024 Special Report
- https://www.sans.edu/cyber-research/active-directory-tactical-containment-to-curb-domain-dominance/ - Active Directory: Tactical Containment to Curb Domain Dominance
- https://www.microsoft.com/en-us/security/blog/2024/04/23/new-microsoft-incident-response-guide-helps-simplify-cyberthreat-investigations/ - New Microsoft Incident Response guide helps simplify cyberthreat investigations
