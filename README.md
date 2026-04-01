# Psyware: Intelligent Assistant for Stress Identification and Guidance

Psyware is an AI-based digital well-being assistant designed to analyze
user-provided text and identify stress-related psychosocial experiences.
The system provides supportive, non-clinical guidance using large
language models and a lightweight orchestration workflow.

This project focuses on helping users express their feelings in natural
language and receive meaningful feedback about potential stress patterns
along with practical coping suggestions.

## Project Overview

Increasing academic pressure, workplace demands, and excessive digital
usage contribute to rising stress levels. Psyware aims to provide a
simple, accessible assistant that interprets user input and generates
supportive responses.

The system uses a conversational interface and AI-powered reasoning
to: - Identify possible stress patterns - Provide supportive
suggestions - Encourage self-awareness - Offer non-clinical guidance

## Key Features

-   Natural language stress analysis
-   AI-powered response generation
-   Real-time conversational interface
-   Session-based conversation memory
-   Streamlit user interface
-   n8n workflow orchestration
-   Groq-hosted LLM integration
-   Lightweight and modular architecture

## System Architecture

User → Streamlit UI → Webhook → n8n Workflow → AI Model → Response →
Streamlit UI

### Components

Frontend: - Streamlit chat interface - User input handling - Response
visualization

Backend: - n8n workflow orchestration - Webhook-based communication - AI
model integration - Response formatting

AI Engine: - Groq hosted LLM - Prompt-based stress interpretation -
Supportive guidance generation

Memory: - Session-based context tracking - Short conversational memory

## How It Works

1.  User enters message in Streamlit interface
2.  Message sent to webhook
3.  n8n workflow receives request
4.  AI model analyzes user input
5.  Stress-related patterns identified
6.  Supportive suggestions generated
7.  Response returned to user interface

## Example

User Input: "I feel stressed after using my phone for long hours"

System Output: - Identifies digital fatigue - Suggests screen breaks -
Recommends relaxation techniques - Provides supportive guidance

## Technology Stack

-   Python
-   Streamlit
-   n8n
-   Groq API
-   Large Language Model
-   Webhooks
-   JSON API

## Experimental Work

The project is currently being extended with: - Multi-agent architecture
experimentation - Improved context handling - Enhanced response
generation - Advanced stress classification

These enhancements are under active development.

## Future Scope

-   Multi-agent orchestration
-   Voice-based interaction
-   Mobile application
-   Multilingual support
-   Persistent database
-   Analytics dashboard
-   Mental health resources integration

## Author

Akash Gowri\
B.Tech Computer Science and Engineering\
Jawaharlal Nehru Technological University Hyderabad -- MRCE

## Disclaimer

Psyware is designed for stress awareness and supportive guidance.\
It does not provide medical or clinical diagnosis.
