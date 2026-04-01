# Psyaware: Multi-Agent Intelligent Assistant for Stress Identification and Guidance

Psyaware is an AI-powered digital well-being assistant designed to
analyze user-provided text, identify stress-related psychosocial
patterns, and generate supportive guidance using a multi-agent
architecture. The system leverages large language models, conversational
memory, and workflow orchestration to provide real-time stress awareness
and personalized suggestions.

## Overview

Modern users often experience stress due to academic pressure, work
overload, and continuous exposure to digital environments. Psyaware
allows users to describe their feelings in natural language and receive
AI-generated insights about potential stress conditions along with
practical coping suggestions.

Unlike traditional ML models trained on structured datasets, Psyaware
performs on-the-fly interpretation using LLM-based reasoning and
multi-agent coordination.

## Key Features

-   Multi-agent AI architecture for stress analysis
-   Natural language understanding of user emotions
-   Real-time stress identification and guidance
-   Conversational memory for contextual responses
-   Streamlit-based interactive chat interface
-   n8n workflow orchestration backend
-   Groq-hosted LLM integration
-   Modular and scalable architecture

## System Architecture

User → Streamlit UI → Webhook → n8n Workflow → Multi-Agent AI → Memory →
LLM → Response → UI

### Components

-   Frontend: Streamlit Chat Interface
-   Orchestration: n8n Workflow Engine
-   AI Engine: Groq LLM (openai-120b)
-   Memory: Session-based conversational context
-   Communication: Webhook-based API pipeline

## Multi-Agent Design

Psyaware uses multiple logical agents:

-   Input Understanding Agent\
-   Stress Detection Agent\
-   Context Memory Agent\
-   Guidance Generation Agent\
-   Response Formatter Agent

These agents collaborate to analyze user input and produce structured,
empathetic responses.

## Technology Stack

-   Python
-   Streamlit
-   n8n
-   Groq API
-   LLM (openai-120b)
-   Webhooks
-   JSON API
-   Session Memory

## How It Works

1.  User enters message in Streamlit interface
2.  Message sent to webhook
3.  n8n workflow triggers AI agents
4.  Memory agent retrieves conversation context
5.  Stress detection agent analyzes message
6.  Guidance agent generates suggestions
7.  Response returned to Streamlit UI

## Example Use Case

User Input: "I feel stressed after using my phone for 6 hours"

Psyaware Response: - Identifies digital overload stress - Suggests
screen breaks - Recommends relaxation techniques - Provides structured
coping advice

## Future Improvements

-   Voice-based interaction
-   Emotion detection
-   Mobile application
-   Multilingual support
-   Mental health dashboard
-   Persistent database
-   Multi-user analytics

## Author

Akash Gowri\
B.Tech Computer Science and Engineering\
Jawaharlal Nehru Technological University Hyderabad -- MRCE

## Note

Psyaware is designed for stress awareness and supportive guidance.\
It is not a medical diagnosis tool.
