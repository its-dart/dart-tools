# Dart MCP Server

A Model Context Protocol (MCP) server implementation for Dart, providing task management, document handling, and workspace organization capabilities through MCP tools.

## Prerequisites

- Node.js 16.x or higher
- Python 3.8 or higher
- Dart Python SDK installed (`pip install dart-sdk`)
- A valid Dart API token

## Features

- Task Management
  - Create and update tasks
  - Set task priorities and status
  - Assign tasks to team members
- Document Management
  - Create and organize documents
  - Support for markdown content
  - Report generation
- Space Management
  - Create and manage workspaces
  - Organize content with folders
  - Control access permissions
- Dartboard Integration
  - Default status management
  - Task organization
  - Team collaboration

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jmanhype/dart-mcp-server.git
cd dart-mcp-server
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Set up Python environment and install Dart SDK:
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install Dart SDK
pip install dart-sdk
```

4. Set up environment variables:
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your configuration
# Required: DART_TOKEN
# Optional: PYTHONPATH (path to dart sdk)
```

## Usage

1. Build the TypeScript code:
```bash
npm run build
```

2. Start the MCP server:
```bash
npm start
```

## Development

```bash
# Watch for TypeScript changes
npm run dev

# Run tests
npm test
```

## Environment Variables

Create a `.env` file with the following variables:

```env
# Required: Your Dart API token
DART_TOKEN=your_dart_token_here

# Optional: Path to your Dart SDK installation
PYTHONPATH=/path/to/dart/sdk

# Optional: Python executable path (defaults to system Python)
PYTHON_PATH=/path/to/python
```

## Available MCP Tools

- `create_task`: Create new tasks with title, description, priority, etc.
- `update_task`: Update existing tasks' status, title, description
- `get_default_status`: Get default status DUIDs
- `get_default_space`: Get default space DUID
- `get_dartboards`: List available dartboards
- `get_folders`: List folders in a space
- `create_folder`: Create new folders
- `create_doc`: Create new documents or reports
- `create_space`: Create new workspaces
- `delete_space`: Delete existing workspaces

## Troubleshooting

If you encounter issues:

1. Verify Python environment:
   ```bash
   python --version
   pip list | grep dart
   ```

2. Check Dart SDK installation:
   ```python
   python -c "import dart; print(dart.__version__)"
   ```

3. Verify environment variables:
   ```bash
   echo $DART_TOKEN
   echo $PYTHONPATH
   ```

## License

MIT License 