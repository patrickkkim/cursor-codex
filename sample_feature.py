#!/usr/bin/env python3
"""
Sample feature module demonstrating MCP GitHub integration.

This module showcases how MCP GitHub tools can be used to:
- Create and manage files in GitHub repositories
- Create branches and pull requests
- Demonstrate automated GitHub workflows
"""

def hello_world():
    """Return a simple greeting message."""
    return "Hello, World! This is a sample feature created via MCP GitHub tools."

def demonstrate_mcp_capabilities():
    """Demonstrate the capabilities of MCP GitHub integration."""
    capabilities = [
        "Create and update files",
        "Create branches",
        "Create pull requests",
        "Manage repository contents",
        "Automate GitHub workflows"
    ]
    
    print("MCP GitHub Integration Capabilities:")
    for i, capability in enumerate(capabilities, 1):
        print(f"{i}. {capability}")
    
    return capabilities

if __name__ == "__main__":
    print(hello_world())
    demonstrate_mcp_capabilities()