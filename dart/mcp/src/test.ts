#!/usr/bin/env node

import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StdioClientTransport } from '@modelcontextprotocol/sdk/client/stdio.js';
import { join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = fileURLToPath(new URL('.', import.meta.url));

async function main() {
    // Create transport for stdio communication
    const transport = new StdioClientTransport({
        command: 'node',
        args: [join(__dirname, 'index.js')],
        stderr: process.stderr,
    });

    // Initialize client with capabilities
    const client = new Client({
        name: 'dart-test-client',
        version: '0.1.0',
    }, {
        capabilities: {
            tools: {}, // Empty object to enable tools capability
        },
    });

    try {
        // Connect to server
        await client.connect(transport);
        console.log('Connected to server');

        // List available tools
        console.log('Listing available tools...');
        const tools = await client.listTools();
        console.log('Available tools:', JSON.stringify(tools, null, 2));

        // Get default space DUID
        console.log('\nGetting default space DUID...');
        const spaceResponse = await client.callTool('get_default_space', {});
        console.log('Space response:', spaceResponse.content[0].text);

        // Extract space DUID from response
        const spaceMatch = spaceResponse.content[0].text.match(/DUID: ([a-zA-Z0-9-]+)/);
        if (!spaceMatch) {
            throw new Error('Failed to extract space DUID from response');
        }
        const spaceDuid = spaceMatch[1];
        console.log('Default space DUID:', spaceDuid);

        // Get default status DUIDs
        console.log('\nGetting default status DUIDs...');
        const statusResponse = await client.callTool('get_default_status', {});
        console.log('Status response:', statusResponse.content[0].text);

        // Extract status DUIDs
        const todoMatch = statusResponse.content[0].text.match(/Todo: ([a-zA-Z0-9-]+)/);
        const doingMatch = statusResponse.content[0].text.match(/Doing: ([a-zA-Z0-9-]+)/);
        const doneMatch = statusResponse.content[0].text.match(/Done: ([a-zA-Z0-9-]+)/);

        if (!todoMatch || !doingMatch || !doneMatch) {
            throw new Error('Failed to extract status DUIDs from response');
        }

        const statusDuids = {
            todo: todoMatch[1],
            doing: doingMatch[1],
            done: doneMatch[1]
        };
        console.log('Status DUIDs:', statusDuids);

        // Get dartboards
        console.log('\nGetting dartboards...');
        const dartboardsResponse = await client.callTool('get_dartboards', {
            space_duid: spaceDuid
        });
        console.log('Dartboards response:', dartboardsResponse.content[0].text);

        // Create a test task
        console.log('\nCreating test task...');
        const createResponse = await client.callTool('create_task', {
            title: 'Test MCP Task',
            description: 'Testing the MCP server integration',
            priority: 'High',
            tags: ['test', 'mcp'],
            size: 3,
        });
        console.log('Create task response:', createResponse.content[0].text);

        // Extract DUID from response
        const match = createResponse.content[0].text.match(/DUID: ([a-zA-Z0-9-]+)/);
        if (!match) {
            throw new Error('Failed to extract task DUID from response');
        }
        const taskDuid = match[1];
        console.log('Created task DUID:', taskDuid);

        // Update the task to "doing" status
        console.log('\nUpdating task to "doing" status...');
        const doingResponse = await client.callTool('update_task', {
            duid: taskDuid,
            status_duid: statusDuids.doing,
            description: 'Updated description via MCP',
            priority: 'Critical'
        });
        console.log('Update to doing response:', doingResponse.content[0].text);

        // Get folders
        console.log('\nGetting folders...');
        const foldersResponse = await client.callTool('get_folders', {
            space_duid: spaceDuid
        });
        console.log('Folders response:', foldersResponse.content[0].text);

        // Mark task as done
        console.log('\nMarking task as done...');
        const doneResponse = await client.callTool('update_task', {
            duid: taskDuid,
            status_duid: statusDuids.done
        });
        console.log('Mark as done response:', doneResponse.content[0].text);

    } catch (error) {
        console.error('Test failed:', error);
        if (error.response) {
            console.error('Response:', error.response);
        }
        if (error.stack) {
            console.error('Stack:', error.stack);
        }
        process.exit(1);
    } finally {
        // Cleanup
        await client.close();
    }
}

main().catch(error => {
    console.error('Unhandled error:', error);
    process.exit(1);
}); 