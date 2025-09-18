# Candidate Search MCP Server

A Model Context Protocol (MCP) server built with [FastMCP](https://gofastmcp.com/) that provides tools for searching and filtering a database of developer candidates.

## Overview

This MCP server exposes tools to search through a database of 20 sample developers with various skills, experience levels, and specializations. It's designed to demonstrate how to build an MCP server that provides data search and filtering capabilities.

## Features

The server provides three main tools:

### 1. `search_candidates`
Search for candidates based on multiple criteria:
- **skill**: Search for specific technical skills (e.g., "Python", "React")
- **min_experience**: Filter by minimum years of experience
- **max_rate**: Filter by maximum hourly rate (USD)
- **location**: Filter by location (partial match)
- **availability**: Filter by availability (e.g., "Immediate", "2 weeks")
- **specialization**: Search for specific areas of expertise

### 2. `get_candidate_details`
Get detailed information about a specific candidate by their ID.

### 3. `list_all_skills`
Get a comprehensive list of all unique skills in the candidate database along with their frequency.

## Sample Data

The server includes 20 diverse developer profiles including:
- Full Stack Developers
- DevOps Engineers
- Machine Learning Engineers
- Mobile Developers
- Security Engineers
- Cloud Architects
- And more...

Each candidate profile contains:
- Name and title
- Technical skills
- Years of experience
- Location
- Hourly rate
- Availability
- Areas of specialization

## Installation

### Prerequisites

- Python 3.13 or higher
- `uv` package manager

### Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd mcp-server
```

2. Install dependencies using uv:
```bash
uv pip install -e .
```

## How to Use

### Adding to Claude Desktop

To use this MCP server with Claude Desktop or other tools. Follow the instructions at [FastMCP Claude Desktop Integration](https://gofastmcp.com/integrations/claude-desktop#fastmcp-cli) to add this server.

### Running Locally

For development and testing, you can run the server directly:

Or using uv:
```bash
uv run main.py
```

## Example Usage

Once connected to Claude Desktop, you can use natural language to interact with the tools:

- "Search for Python developers with at least 5 years of experience"
- "Find developers available immediately with a rate under $150/hour"
- "Show me all developers with machine learning skills"
- "Get details for candidate ID 4"
- "List all available skills in the database"

## Development

The project structure:
- `main.py` - Main server file with tool definitions
- `candidates.py` - Sample candidate database
- `pyproject.toml` - Project configuration and dependencies

## Built With

- [FastMCP](https://gofastmcp.com/) - A framework for building MCP servers quickly and easily
- Python 3.13+

## Created by

Elva - https://www.elva-group.com
