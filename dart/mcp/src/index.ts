#!/usr/bin/env node

import { config } from 'dotenv';
import { resolve } from 'path';

// Load environment variables from /Users/speed/dart-tools/.env
config({ path: '/Users/speed/dart-tools/.env' });

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { CallToolRequestSchema, ErrorCode, ListToolsRequestSchema, McpError } from '@modelcontextprotocol/sdk/types.js';
import { spawn } from 'child_process';

class DartServer {
    constructor() {
        this.server = new Server({
            name: 'dart-server',
            version: '0.1.0',
        }, {
            capabilities: {
                tools: {},
            },
            timeout: 120000, // Increase timeout to 2 minutes
        });

        this.setupToolHandlers();
        
        // Error handling
        this.server.onerror = (error) => console.error('[MCP Error]', error);
        process.on('SIGINT', async () => {
            await this.server.close();
            process.exit(0);
        });

        // Check Python environment on startup
        this.checkPythonEnvironment().catch(console.error);
    }

    async checkPythonEnvironment() {
        const command = `import sys
import os
import traceback

try:
    print("[Debug] Python version:", sys.version, file=sys.stderr)
    print("[Debug] Python executable:", sys.executable, file=sys.stderr)
    print("[Debug] PYTHONPATH:", os.environ.get('PYTHONPATH'), file=sys.stderr)
    print("[Debug] Current directory:", os.getcwd(), file=sys.stderr)
    print("[Debug] DART_TOKEN:", os.environ.get('DART_TOKEN'), file=sys.stderr)

    import dart
    print("[Debug] dart package version:", getattr(dart, '__version__', 'unknown'), file=sys.stderr)

    from dart import Dart
    client = Dart()
    print("[Debug] Successfully created Dart client", file=sys.stderr)
except Exception as e:
    print(f"[Debug] Environment check failed: {str(e)}", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)`;

        try {
            // Use pyenv Python
            const pythonPath = '/Users/speed/.pyenv/shims/python';
            console.error('[Debug] Running environment check with:', pythonPath);
            console.error('[Debug] Environment check command:', command);

            // Create a clean environment without virtual env variables
            const env = { ...process.env };
            delete env.VIRTUAL_ENV;
            delete env.CONDA_PREFIX;
            delete env.CONDA_DEFAULT_ENV;
            delete env.CONDA_PYTHON_EXE;

            const childProcess = spawn(pythonPath, ['-c', command], {
                env: {
                    ...env,
                    PYTHONUNBUFFERED: '1',
                    PYTHONPATH: process.env.PYTHONPATH || process.cwd(),
                    DART_TOKEN: process.env.DART_TOKEN,
                },
                stdio: ['pipe', 'pipe', 'pipe'],
            });

            let output = '';
            let errorOutput = '';

            childProcess.stdout?.on('data', (data) => {
                const str = data.toString();
                console.error('[Debug] Environment check stdout:', str);
                output += str;
            });

            childProcess.stderr?.on('data', (data) => {
                const str = data.toString();
                console.error('[Debug] Environment check stderr:', str);
                errorOutput += str;
            });

            await new Promise((resolve, reject) => {
                childProcess.on('error', (error) => {
                    console.error('[Debug] Environment check error:', error);
                    reject(new Error(`Failed to start Python process: ${error.message}`));
                });

                childProcess.on('close', (code) => {
                    console.error(`[Debug] Environment check exited with code ${code}`);
                    if (code === 0) {
                        resolve(output.trim());
                    } else {
                        reject(new Error(errorOutput || `Environment check failed with exit code ${code}`));
                    }
                });
            });

            console.error('[Debug] Python environment check passed');
        } catch (error) {
            console.error('[Debug] Python environment check failed:', error);
            throw error;
        }
    }

    async runDartCommand(args) {
        return new Promise((resolve, reject) => {
            // Use pyenv Python
            const pythonPath = '/Users/speed/.pyenv/shims/python';
            console.error('[Debug] Running Python command with:', pythonPath);
            
            const command = `import sys
import os
import traceback
import json
from dart import Dart, Operation, OperationKind, OperationModelKind, TaskCreate, TaskUpdate, TransactionKind, TaskSourceType, SpaceCreate
from dart.generated.types import UNSET
from dart.dart import _Session, UserBundle, _make_duid
from dart.generated.models.icon_kind import IconKind
from dart.generated.models.sprint_mode import SprintMode
from dart.generated.models.validation_error_response import ValidationErrorResponse

def initialize():
    print("[Debug] Starting Python execution", file=sys.stderr)
    print("[Debug] Current directory:", os.getcwd(), file=sys.stderr)
    print("[Debug] PYTHONPATH:", os.environ.get('PYTHONPATH'), file=sys.stderr)
    print("[Debug] DART_TOKEN:", os.environ.get('DART_TOKEN'), file=sys.stderr)
    
    session = _Session()
    print("[Debug] Session created", file=sys.stderr)
    bundle = UserBundle(session)
    print("[Debug] UserBundle created", file=sys.stderr)
    dartboard_duid = bundle.default_dartboard["duid"]
    print(f"[Debug] Got dartboard DUID: {dartboard_duid}", file=sys.stderr)
    client = Dart()
    print("[Debug] Dart client created", file=sys.stderr)
    
    return client, bundle, dartboard_duid

def run_command(client, bundle, dartboard_duid):
    ${args}

def main():
    client, bundle, dartboard_duid = initialize()
    run_command(client, bundle, dartboard_duid)

try:
    main()
except Exception as e:
    print(f"Error: {str(e)}", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)`;
            
            console.error('[Debug] Python command:', command);

            // Create a clean environment without virtual env variables
            const env = { ...process.env };
            delete env.VIRTUAL_ENV;
            delete env.CONDA_PREFIX;
            delete env.CONDA_DEFAULT_ENV;
            delete env.CONDA_PYTHON_EXE;

            const childProcess = spawn(pythonPath, ['-c', command], {
                env: {
                    ...env,
                    PYTHONUNBUFFERED: '1',
                    PYTHONPATH: process.env.PYTHONPATH || process.cwd(),
                    DART_TOKEN: process.env.DART_TOKEN,
                },
                stdio: ['pipe', 'pipe', 'pipe'],
            });

            let output = '';
            let errorOutput = '';

            childProcess.stdout?.on('data', (data) => {
                const str = data.toString();
                console.error('[Debug] Python stdout:', str);
                output += str;
            });

            childProcess.stderr?.on('data', (data) => {
                const str = data.toString();
                console.error('[Debug] Python stderr:', str);
                errorOutput += str;
            });

            childProcess.on('error', (error) => {
                console.error('[Debug] Python process error:', error);
                reject(new Error(`Failed to start Python process: ${error.message}`));
            });

            // Add timeout
            const timeout = setTimeout(() => {
                console.error('[Debug] Python command timed out');
                childProcess.kill();
                reject(new Error('Command timed out'));
            }, 30000); // 30 second timeout

            childProcess.on('close', (code) => {
                clearTimeout(timeout);
                console.error(`[Debug] Python process exited with code ${code}`);
                if (code === 0) {
                    resolve(output.trim());
                } else {
                    reject(new Error(errorOutput || `Command failed with exit code ${code}`));
                }
            });
        });
    }

    setupToolHandlers() {
        this.server.setRequestHandler(ListToolsRequestSchema, async () => {
            console.error('[Debug] Handling listTools request');
            const tools = [
                {
                    name: 'get_default_status',
                    description: 'Get the default status DUIDs',
                    inputSchema: {
                        type: 'object',
                        properties: {},
                        required: [],
                    },
                },
                {
                    name: 'get_default_space',
                    description: 'Get the default space DUID',
                    inputSchema: {
                        type: 'object',
                        properties: {},
                        required: [],
                    },
                },
                {
                    name: 'create_task',
                    description: 'Create a new Dart task',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            title: {
                                type: 'string',
                                description: 'Title of the task',
                            },
                            description: {
                                type: 'string',
                                description: 'Description of the task',
                            },
                            priority: {
                                type: 'string',
                                description: 'Priority of the task',
                                enum: ['Low', 'Medium', 'High', 'Critical'],
                            },
                            tags: {
                                type: 'array',
                                items: {
                                    type: 'string',
                                },
                                description: 'Tags for the task',
                            },
                            size: {
                                type: 'number',
                                description: 'Size/complexity of the task (1-5)',
                                minimum: 1,
                                maximum: 5,
                            },
                            assignee_duids: {
                                type: 'array',
                                items: {
                                    type: 'string',
                                },
                                description: 'List of assignee DUIDs',
                            },
                            subscriber_duids: {
                                type: 'array',
                                items: {
                                    type: 'string',
                                },
                                description: 'List of subscriber DUIDs',
                            }
                        },
                        required: ['title', 'description'],
                    },
                },
                {
                    name: 'update_task',
                    description: 'Update an existing task',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            duid: {
                                type: 'string',
                                description: 'DUID of the task to update',
                            },
                            status_duid: {
                                type: 'string',
                                description: 'New status DUID',
                            },
                            title: {
                                type: 'string',
                                description: 'New title for the task',
                            },
                            description: {
                                type: 'string',
                                description: 'New description for the task',
                            },
                            priority: {
                                type: 'string',
                                description: 'New priority for the task',
                                enum: ['Low', 'Medium', 'High', 'Critical'],
                            }
                        },
                        required: ['duid'],
                    },
                },
                {
                    name: 'get_dartboards',
                    description: 'Get available dartboards',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            space_duid: {
                                type: 'string',
                                description: 'Space DUID to get dartboards from',
                            }
                        },
                        required: ['space_duid'],
                    },
                },
                {
                    name: 'get_folders',
                    description: 'Get available folders',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            space_duid: {
                                type: 'string',
                                description: 'Space DUID to get folders from',
                            }
                        },
                        required: ['space_duid'],
                    },
                },
                {
                    name: 'create_folder',
                    description: 'Create a new folder in a space',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            space_duid: {
                                type: 'string',
                                description: 'Space DUID to create the folder in',
                            },
                            title: {
                                type: 'string',
                                description: 'Title of the folder',
                            },
                            description: {
                                type: 'string',
                                description: 'Description of the folder',
                            },
                            kind: {
                                type: 'string',
                                description: 'Kind of folder',
                                enum: ['Default', 'Reports', 'Other'],
                                default: 'Default'
                            }
                        },
                        required: ['space_duid', 'title'],
                    },
                },
                {
                    name: 'create_doc',
                    description: 'Create a new document or report',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            folder_duid: {
                                type: 'string',
                                description: 'Folder DUID to create the document in',
                            },
                            title: {
                                type: 'string',
                                description: 'Title of the document',
                            },
                            text: {
                                type: 'string',
                                description: 'Content of the document',
                            },
                            text_markdown: {
                                type: 'string',
                                description: 'Markdown content of the document',
                            },
                            report_kind: {
                                type: 'string',
                                description: 'Kind of report (if creating a report)',
                                enum: ['Changelog', 'Standup'],
                            },
                            editor_duids: {
                                type: 'array',
                                items: {
                                    type: 'string',
                                },
                                description: 'List of editor DUIDs',
                            },
                            subscriber_duids: {
                                type: 'array',
                                items: {
                                    type: 'string',
                                },
                                description: 'List of subscriber DUIDs',
                            }
                        },
                        required: ['folder_duid', 'title'],
                    },
                },
                {
                    name: 'create_space',
                    description: 'Create a new space',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            title: {
                                type: 'string',
                                description: 'Title of the space'
                            },
                            description: {
                                type: 'string',
                                description: 'Description of the space'
                            },
                            abrev: {
                                type: 'string',
                                description: 'Short abbreviation for the space'
                            },
                            accessible_by_team: {
                                type: 'boolean',
                                description: 'Whether the space is accessible by the whole team',
                                default: true
                            },
                            accessible_by_user_duids: {
                                type: 'array',
                                items: {
                                    type: 'string'
                                },
                                description: 'List of user DUIDs who can access the space'
                            },
                            icon_kind: {
                                type: 'string',
                                enum: ['None', 'Icon', 'Emoji'],
                                description: 'Kind of icon to use',
                                default: 'None'
                            },
                            icon_name_or_emoji: {
                                type: 'string',
                                description: 'Icon name or emoji character'
                            },
                            color_hex: {
                                type: 'string',
                                description: 'Color in hex format (e.g. #FF0000)'
                            },
                            sprint_mode: {
                                type: 'string',
                                enum: ['None', 'ANBA'],
                                description: 'Sprint mode for the space',
                                default: 'None'
                            },
                            sprint_replicate_on_rollover: {
                                type: 'boolean',
                                description: 'Whether to replicate sprints on rollover',
                                default: false
                            },
                            sprint_name_fmt: {
                                type: 'string',
                                description: 'Sprint name format'
                            }
                        },
                        required: ['title']
                    }
                },
                {
                    name: 'delete_space',
                    description: 'Delete a space and all its contents',
                    inputSchema: {
                        type: 'object',
                        properties: {
                            space_duid: {
                                type: 'string',
                                description: 'DUID of the space to delete'
                            }
                        },
                        required: ['space_duid']
                    }
                }
            ];
            console.error('[Debug] Sending tools response:', JSON.stringify(tools, null, 2));
            return { tools };
        });

        this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
            try {
                const { name, arguments: args } = request.params;
                console.error('[Debug] Tool request:', name, JSON.stringify(args, null, 2));
                
                switch (name) {
                    case 'create_task': {
                        console.error('[Debug] Handling create_task request');
                        const pythonCode = `    # Parse optional parameters from JSON
    tags_json = '''${JSON.stringify(args.tags || [])}'''
    assignee_duids_json = '''${JSON.stringify(args.assignee_duids || [])}'''
    subscriber_duids_json = '''${JSON.stringify(args.subscriber_duids || [])}'''

    # Convert JSON strings to Python objects
    tags = json.loads(tags_json) if tags_json.strip() != '[]' else []
    assignee_duids = json.loads(assignee_duids_json) if assignee_duids_json.strip() != '[]' else []
    subscriber_duids = json.loads(subscriber_duids_json) if subscriber_duids_json.strip() != '[]' else []

    print("[Debug] Creating task object", file=sys.stderr)

    # Create the task
    task = TaskCreate(
        source_type=TaskSourceType.CLI,
        duid=_make_duid(),  # Generate a new DUID for the task
        dartboard_duid=dartboard_duid,  # Set the dartboard DUID separately
        title='''${args.title.replace(/'/g, "\\'")}''',
        description='''${args.description.replace(/'/g, "\\'")}''',
        priority="${args.priority || 'Medium'}",
        size=${args.size || 1}
    )

    # Add optional parameters if they exist
    if tags:
        print("[Debug] Adding tags:", tags, file=sys.stderr)
        task.tag_duids = tags
    if assignee_duids:
        print("[Debug] Adding assignees:", assignee_duids, file=sys.stderr)
        task.assignee_duids = assignee_duids
    if subscriber_duids:
        print("[Debug] Adding subscribers:", subscriber_duids, file=sys.stderr)
        task.subscriber_duids = subscriber_duids

    print("[Debug] Task object created:", task, file=sys.stderr)

    print("[Debug] Creating operation", file=sys.stderr)
    task_op = Operation(
        model=OperationModelKind.TASK,
        kind=OperationKind.CREATE,
        data=task
    )
    print("[Debug] Operation created:", task_op, file=sys.stderr)

    print("[Debug] Executing transaction", file=sys.stderr)
    response = client.transact([task_op], TransactionKind.TASK_CREATE)
    print("[Debug] Transaction completed", file=sys.stderr)

    if response.results and response.results[0].success:
        task = response.results[0].models.tasks[0]
        print(f"Task created successfully with DUID: {task.duid}")
        print(f"[Debug] Task DUID: {task.duid}", file=sys.stderr)
    else:
        print("[Debug] Task creation failed", file=sys.stderr)
        if response.results:
            print(f"[Debug] Result: {response.results[0]}", file=sys.stderr)
        sys.exit(1)`;
                        
                        // Add proper indentation to the Python code
                        const command = pythonCode.split('\n').map(line => line.length > 0 ? '    ' + line : line).join('\n');

                        console.error('[Debug] Running Python command for task creation');
                        const output = await this.runDartCommand(command);
                        console.error('[Debug] Task creation output:', output);
                        const response = {
                            content: [{
                                type: 'text',
                                text: output,
                            }],
                        };
                        console.error('[Debug] Sending task creation response:', JSON.stringify(response, null, 2));
                        return response;
                    }

                    case 'update_task': {
                        console.error('[Debug] Handling update_task request');
                        const command = `print("[Debug] Starting task update", file=sys.stderr)

try:
    # Get initialized client and bundle
    client, bundle, dartboard_duid = initialize()
    print("[Debug] Got client and bundle", file=sys.stderr)

    print("[Debug] Creating task update object", file=sys.stderr)
    task_update = TaskUpdate(
        duid="${args.duid}",
        source_type=UNSET
    )
    
    if ${args.status_duid !== undefined ? 'True' : 'False'}:
        task_update.status_duid = "${args.status_duid}"
    if ${args.title !== undefined ? 'True' : 'False'}:
        task_update.title = "${args.title}"
    if ${args.description !== undefined ? 'True' : 'False'}:
        task_update.description = "${args.description}"
    if ${args.priority !== undefined ? 'True' : 'False'}:
        task_update.priority = "${args.priority}"
    
    print("[Debug] Task update object created:", task_update, file=sys.stderr)

    print("[Debug] Creating operation", file=sys.stderr)
    task_update_op = Operation(
        model=OperationModelKind.TASK,
        kind=OperationKind.UPDATE,
        data=task_update
    )
    print("[Debug] Operation created:", task_update_op, file=sys.stderr)

    print("[Debug] Executing transaction", file=sys.stderr)
    response = client.transact([task_update_op], TransactionKind.TASK_UPDATE)
    print("[Debug] Transaction completed", file=sys.stderr)
    
    if response.results and response.results[0].success:
        print(f"Task updated successfully")
        print(f"[Debug] Task update successful", file=sys.stderr)
    else:
        print("[Debug] Task update failed", file=sys.stderr)
        if response.results:
            print(f"[Debug] Result: {response.results[0]}", file=sys.stderr)
        print("Failed to update task", file=sys.stderr)
        sys.exit(1)
except Exception as e:
    print(f"[Debug] Task update error: {str(e)}", file=sys.stderr)
    print("[Debug] Error type:", type(e), file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)`;

                        console.error('[Debug] Running Python command for task update');
                        const output = await this.runDartCommand(command);
                        console.error('[Debug] Task update output:', output);
                        const response = {
                            content: [{
                                type: 'text',
                                text: output,
                            }],
                        };
                        console.error('[Debug] Sending task update response:', JSON.stringify(response, null, 2));
                        return response;
                    }

                    case 'get_default_status': {
                        console.error('[Debug] Handling get_default_status request');
                        const command = `print("[Debug] Getting default statuses", file=sys.stderr)

try:
    # Get initialized client and bundle
    client, bundle, dartboard_duid = initialize()
    print("[Debug] Got bundle", file=sys.stderr)
    
    statuses = bundle.default_statuses
    print("[Debug] Got statuses:", statuses, file=sys.stderr)
    if not statuses:
        print("No statuses found")
        sys.exit(1)
    
    # Map status kinds to their DUIDs
    status_map = {}
    for status in statuses:
        if status["kind"] == "Unstarted":
            status_map["todo"] = status["duid"]
        elif status["kind"] == "Started":
            status_map["doing"] = status["duid"]
        elif status["kind"] == "Finished":
            status_map["done"] = status["duid"]
    
    print(f"Status DUIDs:")
    print(f"Todo: {status_map.get('todo', 'N/A')}")
    print(f"Doing: {status_map.get('doing', 'N/A')}")
    print(f"Done: {status_map.get('done', 'N/A')}")
except Exception as e:
    print(f"[Debug] Error getting default statuses: {str(e)}", file=sys.stderr)
    print("[Debug] Error type:", type(e), file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)`;

                        console.error('[Debug] Running Python command for getting default statuses');
                        const output = await this.runDartCommand(command);
                        console.error('[Debug] Get default statuses output:', output);
                        const response = {
                            content: [{
                                type: 'text',
                                text: output,
                            }],
                        };
                        return response;
                    }

                    case 'get_default_space': {
                        console.error('[Debug] Handling get_default_space request');
                        // Note: Using raw string with proper indentation for the run_command function
                        const pythonCode = `    # Get default space
    print("[Debug] Getting default space", file=sys.stderr)
    try:
        spaces = bundle.spaces
        print("[Debug] Got spaces:", spaces, file=sys.stderr)
        if not spaces:
            print("No spaces found")
            sys.exit(1)
        default_space = spaces[0]
        print(f"Default space DUID: {default_space['duid']}")
    except Exception as e:
        print(f"[Debug] Error getting space: {str(e)}", file=sys.stderr)
        sys.exit(1)`;

                        // Add proper indentation to the Python code
                        const command = pythonCode.split('\n').map(line => line.length > 0 ? '    ' + line : line).join('\n');

                        console.error('[Debug] Running Python command for getting default space');
                        const output = await this.runDartCommand(command);
                        console.error('[Debug] Get default space output:', output);
                        const response = {
                            content: [{
                                type: 'text',
                                text: output,
                            }],
                        };
                        return response;
                    }

                    case 'get_dartboards': {
                        console.error('[Debug] Handling get_dartboards request');
                        const pythonCode = `    # Get dartboards for the space
    print("[Debug] Getting dartboards", file=sys.stderr)
    try:
        # Get dartboards from the bundle
        dartboards = bundle.dartboards
        print("[Debug] Got dartboards:", dartboards, file=sys.stderr)
        if not dartboards:
            print("No dartboards found")
            sys.exit(1)
        # Print dartboard titles
        print("Available dartboards:")
        for d in dartboards:
            print(f"- {d['title']} (DUID: {d['duid']})")
    except Exception as e:
        print(f"[Debug] Error getting dartboards: {str(e)}", file=sys.stderr)
        sys.exit(1)`;

                        // Add proper indentation to the Python code
                        const command = pythonCode.split('\n').map(line => line.length > 0 ? '    ' + line : line).join('\n');

                        console.error('[Debug] Running Python command for getting dartboards');
                        const output = await this.runDartCommand(command);
                        console.error('[Debug] Get dartboards output:', output);
                        const response = {
                            content: [{
                                type: 'text',
                                text: output,
                            }],
                        };
                        return response;
                    }

                    case 'get_folders': {
                        console.error('[Debug] Handling get_folders request');
                        const pythonCode = `    # Get folders for the space
    print("[Debug] Getting folders", file=sys.stderr)
    try:
        # Get folders using the get_folders function from dart module
        space_duid = "${args.space_duid}"
        print(f"[Debug] Getting folders for space: {space_duid}", file=sys.stderr)
        from dart import get_folders
        folders = get_folders(space_duid, include_special=True)  # Include all folders
        print("[Debug] Got folders:", folders, file=sys.stderr)
        
        # Print folder titles or indicate no folders found
        if not folders:
            print("No folders found in this space")
        else:
            print("Available folders:")
            for folder in folders:
                print(f"- {folder.title} (DUID: {folder.duid}, Kind: {folder.kind})")
    except Exception as e:
        print(f"[Debug] Error getting folders: {str(e)}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)`;

                        // Add proper indentation to the Python code
                        const command = pythonCode.split('\n').map(line => line.length > 0 ? '    ' + line : line).join('\n');

                        console.error('[Debug] Running Python command for getting folders');
                        const output = await this.runDartCommand(command);
                        console.error('[Debug] Get folders output:', output);
                        const response = {
                            content: [{
                                type: 'text',
                                text: output,
                            }],
                        };
                        return response;
                    }

                    case 'create_folder': {
                        console.error('[Debug] Handling create_folder request');
                        const pythonCode = `    # Create a new folder
    print("[Debug] Creating folder", file=sys.stderr)
    try:
        from dart import Operation, OperationKind, OperationModelKind, FolderCreate, TransactionKind
        from dart.generated.models.folder_kind import FolderKind
        from dart.generated.models.validation_error_response import ValidationErrorResponse
        from dart.dart import _make_duid
        
        space_duid = "${args.space_duid}"
        title = '''${args.title.replace(/'/g, "\\'")}'''
        description = '''${args.description ? args.description.replace(/'/g, "\\'") : ''}'''
        kind_str = "${args.kind || 'Default'}"
        
        print(f"[Debug] Creating folder in space: {space_duid}", file=sys.stderr)
        print(f"[Debug] Folder title: {title}", file=sys.stderr)
        print(f"[Debug] Folder kind: {kind_str}", file=sys.stderr)
        
        # Create the folder object with required fields
        folder = FolderCreate(
            duid=_make_duid(),
            space_duid=space_duid,
            order="0",  # Default order at the top
            title=title,
            description=description if description else "",  # Use empty string instead of None
            kind=FolderKind(kind_str)  # Convert string to enum
        )
        print("[Debug] Folder object created:", folder, file=sys.stderr)
        
        # Create the operation
        folder_op = Operation(
            model=OperationModelKind.FOLDER,
            kind=OperationKind.CREATE,
            data=folder
        )
        print("[Debug] Operation created:", folder_op, file=sys.stderr)
        
        # Execute the transaction
        print("[Debug] Executing transaction", file=sys.stderr)
        try:
            response = client.transact([folder_op], TransactionKind.FOLDER_CREATE)
            print("[Debug] Transaction completed", file=sys.stderr)
            print("[Debug] Response type:", type(response), file=sys.stderr)
            print("[Debug] Response:", response, file=sys.stderr)
            
            if isinstance(response, ValidationErrorResponse):
                print("[Debug] Validation error:", response.items.additional_properties, file=sys.stderr)
                print(f"Validation error: {response.items.additional_properties}")
                sys.exit(1)
            
            if response.results and response.results[0].success:
                folder = response.results[0].models.folders[0]
                print(f"Folder created successfully")
                print(f"Title: {folder.title}")
                print(f"DUID: {folder.duid}")
                print(f"[Debug] Folder DUID: {folder.duid}", file=sys.stderr)
            else:
                print("[Debug] Folder creation failed", file=sys.stderr)
                if response.results:
                    print(f"[Debug] Result: {response.results[0]}", file=sys.stderr)
                sys.exit(1)
        except Exception as e:
            print(f"[Debug] Transaction error: {str(e)}", file=sys.stderr)
            print("[Debug] Error type:", type(e), file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"[Debug] Error creating folder: {str(e)}", file=sys.stderr)
        print("[Debug] Error type:", type(e), file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)`;

                        // Add proper indentation to the Python code
                        const command = pythonCode.split('\n').map(line => line.length > 0 ? '    ' + line : line).join('\n');

                        console.error('[Debug] Running Python command for folder creation');
                        const output = await this.runDartCommand(command);
                        console.error('[Debug] Folder creation output:', output);
                        const response = {
                            content: [{
                                type: 'text',
                                text: output,
                            }],
                        };
                        return response;
                    }

                    case 'create_doc': {
                        console.error('[Debug] Handling create_doc request');
                        
                        // Validate required fields
                        if (!args.folder_duid) {
                            throw new McpError(ErrorCode.INVALID_PARAMS, "folder_duid is required");
                        }
                        if (!args.title) {
                            throw new McpError(ErrorCode.INVALID_PARAMS, "title is required");
                        }
                        
                        const pythonCode = `    # Create a new document
    print("[Debug] Creating document", file=sys.stderr)
    try:
        from dart import Operation, OperationKind, OperationModelKind, DocCreate, TransactionKind, DocSourceType
        from dart.generated.models.report_kind import ReportKind
        from dart.generated.models.validation_error_response import ValidationErrorResponse
        from dart.dart import _make_duid
        
        folder_duid = "${args.folder_duid}"
        title = '''${args.title.replace(/'/g, "\\'")}'''  # title is validated above
        text = '''${args.text ? args.text.replace(/'/g, "\\'") : ''}'''
        text_markdown = '''${args.text_markdown ? args.text_markdown.replace(/'/g, "\\'") : ''}'''
        report_kind_str = "${args.report_kind || ''}"
        
        print(f"[Debug] Creating document in folder: {folder_duid}", file=sys.stderr)
        print(f"[Debug] Document title: {title}", file=sys.stderr)
        if report_kind_str:
            print(f"[Debug] Report kind: {report_kind_str}", file=sys.stderr)
        
        # Create the document object
        doc = DocCreate(
            duid=_make_duid(),
            folder_duid=folder_duid,
            title=title,
            source_type=DocSourceType.APPLICATION,
            order="0"  # Add order field like in create_folder
        )
        
        # Add optional fields
        if text:
            doc.text = text
        if text_markdown:
            doc.text_markdown = text_markdown
        if report_kind_str:
            doc.report_kind = ReportKind(report_kind_str)
            
        # Add editor and subscriber DUIDs if provided
        editor_duids_json = '''${JSON.stringify(args.editor_duids || [])}'''
        subscriber_duids_json = '''${JSON.stringify(args.subscriber_duids || [])}'''
        editor_duids = json.loads(editor_duids_json)
        subscriber_duids = json.loads(subscriber_duids_json)
        
        if editor_duids:
            doc.editor_duids = editor_duids
        if subscriber_duids:
            doc.subscriber_duids = subscriber_duids
            
        print("[Debug] Document object created:", doc, file=sys.stderr)
        
        # Create the operation
        doc_op = Operation(
            model=OperationModelKind.DOC,
            kind=OperationKind.CREATE,
            data=doc
        )
        print("[Debug] Operation created:", doc_op, file=sys.stderr)
        
        # Execute the transaction
        print("[Debug] Executing transaction", file=sys.stderr)
        response = client.transact([doc_op], TransactionKind.DOC_CREATE)
        print("[Debug] Transaction completed", file=sys.stderr)
        print("[Debug] Response type:", type(response), file=sys.stderr)
        print("[Debug] Response:", response, file=sys.stderr)
        
        if isinstance(response, ValidationErrorResponse):
            print("[Debug] Validation error:", response.items.additional_properties, file=sys.stderr)
            print(f"Validation error: {response.items.additional_properties}")
            sys.exit(1)
        
        if response.results and response.results[0].success:
            doc = response.results[0].models.docs[0]
            print(f"Document created successfully")
            print(f"Title: {doc.title}")
            print(f"DUID: {doc.duid}")
            if hasattr(doc, 'report_kind') and doc.report_kind:
                print(f"Report Kind: {doc.report_kind}")
            print(f"[Debug] Document DUID: {doc.duid}", file=sys.stderr)
        else:
            print("[Debug] Document creation failed", file=sys.stderr)
            if response.results:
                print(f"[Debug] Result: {response.results[0]}", file=sys.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"[Debug] Error creating document: {str(e)}", file=sys.stderr)
        print("[Debug] Error type:", type(e), file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)`;

                        // Add proper indentation to the Python code
                        const command = pythonCode.split('\n').map(line => line.length > 0 ? '    ' + line : line).join('\n');

                        console.error('[Debug] Running Python command for document creation');
                        const output = await this.runDartCommand(command);
                        console.error('[Debug] Document creation output:', output);
                        const response = {
                            content: [{
                                type: 'text',
                                text: output,
                            }],
                        };
                        return response;
                    }

                    case 'create_space': {
                        console.error('[Debug] Handling create_space request');
                        const pythonCode = `
import sys
import json
from dart import Dart, Operation, OperationKind, OperationModelKind, SpaceCreate, TransactionKind
from dart.dart import _Session, UserBundle, _make_duid
from dart.generated.models.icon_kind import IconKind

print("[Debug] Starting Python execution", file=sys.stderr)

# Parse arguments from JSON
args_json = '''${JSON.stringify(args)}'''
args = json.loads(args_json)
print(f"[Debug] Parsed args: {args}", file=sys.stderr)

# Initialize session and client
session = _Session()
print("[Debug] Session created", file=sys.stderr)
bundle = UserBundle(session)
print("[Debug] UserBundle created", file=sys.stderr)
client = Dart()
print("[Debug] Dart client created", file=sys.stderr)

# Get the user's DUID
user_duid = bundle.user["duid"]
print(f"[Debug] User DUID: {user_duid}", file=sys.stderr)

# Generate a unique DUID for the space
space_duid = _make_duid()
print(f"[Debug] Generated space DUID: {space_duid}", file=sys.stderr)

# Create the space object with required fields
space = SpaceCreate(
    duid=space_duid,
    order="0",
    title=args.get("title"),
    description=args.get("description", ""),
    drafter_duid=user_duid,  # Set drafter_duid explicitly
    accessible_by_team=args.get("accessible_by_team", True),
    accessible_by_user_duids=args.get("accessible_by_user_duids", []),
    icon_kind=IconKind(args.get("icon_kind", "None")),
    icon_name_or_emoji=args.get("icon_name_or_emoji", "")
)
print(f"[Debug] Created space object: {space}", file=sys.stderr)

# Create the operation
space_op = Operation(
    model=OperationModelKind.SPACE,
    kind=OperationKind.CREATE,
    data=space  # Pass the SpaceCreate object
)

print(f"[Debug] Created operation: {space_op}", file=sys.stderr)

# Execute the transaction
result = client.transact([space_op], TransactionKind.SPACE_CREATE)
print(f"[Debug] Transaction completed", file=sys.stderr)

if result.results and result.results[0].success:
    space = result.results[0].models.spaces[0]
    print(f"Space created successfully")
    print(f"Title: {space.title}")
    print(f"DUID: {space.duid}")
    print(f"[Debug] Space DUID: {space.duid}", file=sys.stderr)
else:
    print("[Debug] Space creation failed", file=sys.stderr)
    if result.results:
        print(f"[Debug] Result: {result.results[0]}", file=sys.stderr)
    sys.exit(1)`;

                        // Add proper indentation to the Python code
                        const command = pythonCode.split('\n').map(line => {
                            if (line.trim().length === 0) return line;
                            return '    ' + line;
                        }).join('\n');

                        console.error('[Debug] Running Python command for space creation');
                        const output = await this.runDartCommand(command);
                        console.error('[Debug] Space creation output:', output);
                        const response = {
                            content: [{
                                type: 'text',
                                text: output,
                            }],
                        };
                        return response;
                    }

                    case 'delete_space': {
                        console.error('[Debug] Handling delete_space request');
                        const pythonCode = `    # Delete space
    print("[Debug] Starting space deletion", file=sys.stderr)
    try:
        # Parse space_duid from args
        space_duid = "${args.space_duid}"
        print(f"[Debug] Deleting space with DUID: {space_duid}", file=sys.stderr)

        # Create the delete operation
        delete_op = Operation(
            model=OperationModelKind.SPACE,
            kind=OperationKind.DELETE,
            data={"duid": space_duid}  # For delete operations, we just need the DUID
        )
        print("[Debug] Created delete operation", file=sys.stderr)
        
        # Execute the transaction
        print("[Debug] Executing transaction", file=sys.stderr)
        response = client.transact([delete_op], TransactionKind.SPACE_DELETE)
        print("[Debug] Transaction completed", file=sys.stderr)
        
        if response.results and response.results[0].success:
            print(f"Space {space_duid} deleted successfully")
            print(f"[Debug] Space deletion successful", file=sys.stderr)
        else:
            print("[Debug] Space deletion failed", file=sys.stderr)
            if response.results:
                print(f"[Debug] Result: {response.results[0]}", file=sys.stderr)
            sys.exit(1)
            
    except Exception as e:
        print(f"[Debug] Error deleting space: {str(e)}", file=sys.stderr)
        print("[Debug] Error type:", type(e), file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)`;

                        // Add proper indentation to the Python code
                        const command = pythonCode.split('\n').map(line => {
                            if (line.trim().length === 0) return line;
                            return '    ' + line;
                        }).join('\n');

                        console.error('[Debug] Running Python command for space deletion');
                        const output = await this.runDartCommand(command);
                        console.error('[Debug] Space deletion output:', output);
                        const response = {
                            content: [{
                                type: 'text',
                                text: output,
                            }],
                        };
                        return response;
                    }

                    default:
                        throw new McpError(ErrorCode.UNKNOWN_TOOL, `Unknown tool: ${name}`);
                }
            } catch (error) {
                console.error('[Debug] Tool error:', error);
                throw new McpError(
                    error.code ?? ErrorCode.INTERNAL_ERROR,
                    error.message || 'Internal server error',
                    error.data
                );
            }
        });
    }

    async start() {
        const transport = new StdioServerTransport();
        await this.server.connect(transport);
        console.error('Dart MCP server running on stdio');
    }
}

const server = new DartServer();
server.start().catch(console.error); 