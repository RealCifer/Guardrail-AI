# Guardrail AI
## AI-Driven Investment Communication Workflow with Compliance Guardrail

Guardrail AI is an automated compliance-aware messaging workflow designed for financial communication systems.  
The platform reads scheduled investor messages from a Google Sheet, validates the inputs, applies a compliance guardrail layer to detect risky or misleading financial claims, and dispatches approved messages at scheduled times.

This project demonstrates **AI workflow orchestration, compliance safety design, automated scheduling, and backend system architecture**.

---

# Project Objective

Financial institutions must ensure that investor communication follows regulatory guidelines and avoids misleading claims.

Guardrail AI provides a workflow that:

• Reads investor communication data from Google Sheets  
• Validates message inputs  
• Applies compliance guardrails before sending  
• Blocks misleading financial communication  
• Schedules approved messages  
• Sends messages automatically at scheduled times  
• Updates delivery status back to the sheet  

---

# System Architecture

```
                          ┌───────────────────────────┐
                          │       Google Sheet        │
                          │  (Investor Message Data)  │
                          └─────────────┬─────────────┘
                                        │
                                        ▼
                          ┌───────────────────────────┐
                          │     Data Reading Layer     │
                          │  - Fetch rows from sheet   │
                          │  - Filter Pending rows     │
                          └─────────────┬─────────────┘
                                        │
                                        ▼
                          ┌───────────────────────────┐
                          │      Validation Layer      │
                          │  - Mobile number format    │
                          │  - Message not empty       │
                          │  - Valid datetime format   │
                          │  - Schedule not in past    │
                          │  - Category validation     │
                          └─────────────┬─────────────┘
                                        │
                                        ▼
                          ┌───────────────────────────┐
                          │   Compliance Guardrail     │
                          │      Classification        │
                          │                           │
                          │   Approved                │
                          │   Requires Review         │
                          │   Rejected                │
                          └───────┬─────────┬─────────┘
                                  │         │
                     ┌────────────┘         └────────────┐
                     ▼                                   ▼
         ┌───────────────────────┐          ┌───────────────────────┐
         │    Blocked Messages    │          │    Approved Messages   │
         │  Status → Blocked      │          │  Continue Workflow     │
         └─────────────┬─────────┘          └─────────────┬─────────┘
                       │                                  │
                       ▼                                  ▼
               ┌─────────────────────────────────────────────┐
               │             Scheduling Layer                 │
               │       APScheduler Job Scheduler              │
               │  - Schedule message dispatch time            │
               │  - Prevent duplicate sending                 │
               └─────────────┬───────────────────────────────┘
                             │
                             ▼
               ┌─────────────────────────────────────────────┐
               │             Sending Layer                    │
               │        SMS / WhatsApp / Email API            │
               │       (Simulated in this project)            │
               └─────────────┬───────────────────────────────┘
                             │
                             ▼
               ┌─────────────────────────────────────────────┐
               │            Status Update Layer               │
               │        Update Google Sheet Status            │
               │                                             │
               │  Scheduled → Sent / Failed / Blocked        │
               └─────────────────────────────────────────────┘
```

---

# Workflow Overview

1. Investor messages are stored in a Google Sheet.
2. The system reads rows where **Status = Pending**.
3. Inputs are validated for correctness.
4. Messages pass through the **Compliance Guardrail Layer**.
5. Unsafe messages are blocked.
6. Approved messages are scheduled.
7. The scheduler sends messages at the scheduled time.
8. Message delivery status is updated back to the Google Sheet.

---

# Input Data Structure

The system reads the following columns from Google Sheets.

| Column | Description |
|------|-------------|
| Name | Recipient name |
| Mobile | Recipient phone number |
| Message | Investor communication message |
| Schedule | Datetime when message should be sent |
| Category | Message category |
| Status | Workflow status |
| Compliance_flag | Compliance classification |

---

# Validation Rules

Before processing messages, the system validates:

• Mobile number format  
• Message content is not empty  
• Schedule datetime format is valid  
• Scheduled time is not in the past  
• Category belongs to allowed values  

Allowed Categories:

```
Performance Update
Research Insight
Product Communication
Marketing
```

If validation fails:

```
Status = Invalid
```

---

# Compliance Guardrail Logic

The compliance layer detects risky financial claims and classifies messages into:

```
Approved
Requires Review
Rejected
```

### Rejected Messages

Messages containing prohibited phrases such as:

```
Guaranteed returns
Assured returns
Risk-free investment
Double your money
```

These are blocked.

```
Status = Blocked
```

---

### Requires Review

Messages containing direct investment advice:

```
Strong buy
Invest now
High return investment
```

These require manual compliance review.

---

### Approved

Neutral investor communication such as:

```
Performance updates
Research insights
Market commentary
Product announcements
```

These messages proceed to scheduling.

---

# Scheduling Layer

The system uses **APScheduler** to schedule message delivery.

Features:

• Dispatch messages at scheduled time  
• Prevent duplicate message sending  
• Maintain execution queue  
• Ensure reliable workflow execution  

---

# Sending Layer

For demonstration purposes, message sending is simulated.

The system logs:

```
Sending message to <mobile>
Message Sent Successfully
```

In production, this layer can integrate:

• Twilio SMS API  
• WhatsApp Business API  
• Email services  

---

# Status Management

The system updates the Google Sheet automatically.

Possible status values:

```
Pending
Scheduled
Sent
Failed
Invalid
Blocked
```

This ensures full workflow traceability.

---

# Technologies Used

Python  
Google Sheets API  
gspread  
OAuth2 Service Accounts  
APScheduler  
dotenv  
Rule-based Compliance Guardrail Engine  

---

# Project Structure

```
Guardrail-AI
│
├── src
│   ├── sheets_reader.py
│   ├── validator.py
│   ├── compliance.py
│   ├── scheduler_engine.py
│   └── sender.py
│
├── output.py
├── requirements.txt
├── .env
├── credentials.json
└── README.md
```

---

# Installation

Clone the repository.

```
git clone https://github.com/RealCifer/Guardrail-AI.git
cd Guardrail-AI
```

Create virtual environment.

```
python -m venv venv
```

Activate environment.

```
venv\Scripts\activate
```

Install dependencies.

```
pip install -r requirements.txt
```

---

# Configuration

Create `.env` file.

```
GOOGLE_SHEET_NAME=Guardrail_Test_Data
```

Place the Google Cloud service account file in project root.

```
credentials.json
```

Share the Google Sheet with the service account email.

---

# Running the Application

Run the workflow engine:

```
python output.py
```

The system will:

1. Read pending rows  
2. Validate data  
3. Apply compliance guardrails  
4. Schedule approved messages  
5. Send messages at scheduled time  

---

# Example Execution Output

```
Rows found for processing: 2

Processing row: 2
Validation Passed
Compliance Classification: Rejected
Message Blocked

Processing row: 3
Validation Passed
Compliance Classification: Approved
Message Approved
Message scheduled for 2026-03-05 16:00
```

---

# Future Improvements

Potential extensions for production systems:

• Real SMS/WhatsApp API integration  
• ML-based compliance classifier  
• Compliance audit logs  
• Dashboard for message monitoring  
• Alert system for blocked communications  

---

# Author

Aditya Khamait  
Software Developer | AI Systems | Backend Engineering

