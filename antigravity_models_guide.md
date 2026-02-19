# Antigravity Models Guide

Antigravity leverages a curated suite of advanced AI models to provide a powerful and autonomous development experience.

## Model Comparison

| Model | Provider | Primary Strength | Best For... | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Gemini 3 Pro (High)** | Google | **High Reasoning** | Complex refactoring, difficult logic, deep analysis. | Higher compute variant for when accuracy is paramount. |
| **Gemini 3 Pro (Low)** | Google | **Standard Reasoning** | Everyday coding, features, standard refactoring. | Balanced performance for standard tasks. |
| **Gemini 3 Flash** | Google | **Maximum Speed** | Quick fixes, unit tests, docs, repetitive tasks. | Lowest latency and cost. Best for "easy" volume work. |
| **Claude Sonnet 4.6 (Thinking)** | Anthropic | **Balanced Thinking** | Explanations, creative coding, moderate reasoning. | Uses explicit "thinking" process to plan before acting. |
| **Claude Opus 4.6 (Thinking)** | Anthropic | **Deepest Thinking** | System architecture, massive context, hard bugs. | The most powerful reasoning model available. |

---

## ⚡ Quick Cheat Sheet: Which Model Should I Use?

| I need to... | Use this Model: |
| :--- | :--- |
| **Write standard features** (React, Python, etc.) | `Gemini 3 Pro (Low)` |
| **Debug a race condition** or complex crash | `Gemini 3 Pro (High)` or `Claude Opus 4.6 (Thinking)` |
| **Plan a new system architecture** | `Claude Opus 4.6 (Thinking)` |
| **Write unit tests** or boilerplate | `Gemini 3 Flash` |
| **Get a detailed explanation** of a concept | `Claude Sonnet 4.6 (Thinking)` |
| **Refactor a large, messy file** | `Gemini 3 Pro (High)` |
| **Get a quick answer** | `Gemini 3 Flash` |

> [!TIP]
> **Default Strategy:** Start with **Gemini 3 Pro (Low)**. If the task requires more brainpower, upgrade to **Gemini 3 Pro (High)**. For the hardest problems, use **Claude Opus 4.6 (Thinking)**.
