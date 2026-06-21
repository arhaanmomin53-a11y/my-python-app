# My D-Drive Python Agents Project

\# Multi-Agent Dispute System (ADK Architecture)



This project implements an automated multi-agent framework designed to parse records, flag system inconsistencies, and systematically build formal dispute documentation.



\## System Architecture Diagram



```mermaid

graph TD

&#x20;   %% Styling Configuration

&#x20;   classDef intake fill:#cfe2ff,stroke:#0d6efd,stroke-width:2px,color:#000;

&#x20;   classDef auditor fill:#fff3cd,stroke:#ffc107,stroke-width:2px,color:#000;

&#x20;   classDef action fill:#d1e7dd,stroke:#198754,stroke-width:2px,color:#000;

&#x20;   classDef data fill:#e2e3e5,stroke:#6c757d,stroke-width:1px,color:#000,stroke-dasharray: 5 5;



&#x20;   %% Data Inputs

&#x20;   A\[Raw Input Documents] -->|Reads Files| B(1. Intake Agent)

&#x20;   

&#x20;   %% Multi-Agent Chain

&#x20;   B -->|Extracts Clean Data| C(2. Auditor Agent)

&#x20;   D\[Reference Databases/Rules] -->|Cross-References| C

&#x20;   C -->|Flags Discrepancies| E(3. Action Agent)

&#x20;   

&#x20;   %% System Output

&#x20;   E -->|Generates Output| F\[Final Drafted Dispute Document]



&#x20;   %% Class Assignments

&#x20;   class B intake;

&#x20;   class C auditor;

&#x20;   class E action;

&#x20;   class A,D,F data;

