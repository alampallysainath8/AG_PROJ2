# Swarm Flight Refund Assistant

## Overview

This project implements a multi-agent conversational system for handling flight refund requests using the [autogen-agentchat](https://github.com/microsoft/autogen) framework. The system features two main agents:

- **Travel Agent:** Interacts with the user, gathers necessary information, and coordinates the refund process.
- **Flight Refunder:** Specializes in processing flight refunds using a provided tool.

Agents communicate and hand off tasks to each other and the user, ensuring a smooth and interactive experience.

---

## Features

- Multi-agent orchestration with clear role separation.
- Tool integration for flight refund processing.
- Interactive handoff between agents and user.
- Termination conditions for controlled conversation flow.
- Console-based user interface.

---

## Project Structure
Swarm/ ├── .env ├── .gitignore ├── README.md └── swarmapp.py

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [autogen-agentchat](https://github.com/microsoft/autogen) and dependencies
- OpenAI API key

### Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/swarm-flight-refund.git
   cd swarm-flight-refund/Swarm