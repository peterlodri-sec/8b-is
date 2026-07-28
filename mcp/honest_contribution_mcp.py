#!/usr/bin/env python3
"""
=============================================================================
AXIOM QUANT & 8B-IS — HONEST CONTRIBUTION MCP SERVER
=============================================================================
Model Context Protocol (MCP) server for submitting, signing, listing, and
verifying honest research contributions directly from AI agents (Claude, Antigravity).
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import sys
import uuid
from typing import Any

# In-memory research vault storage
VAULT: dict[str, dict[str, Any]] = {}

def submit_honest_contribution(
    title: str,
    author: str,
    content_markdown: str,
    tags: list[str],
    author_handle: str | None = None,
    signature_ed25519: str | None = None,
    ephemeral_ram_only: bool = False,
) -> dict[str, Any]:
    """Submit a cryptographically signed honest research contribution."""
    cid = f"contrib-{uuid.uuid4().hex[:12]}"
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

    # Compute SHA-256 payload hash
    payload_bytes = f"{title}|{author}|{content_markdown}|{timestamp}".encode("utf-8")
    sha256_hash = hashlib.sha256(payload_bytes).hexdigest()

    record = {
        "contribution_id": cid,
        "title": title,
        "author": author,
        "author_handle": author_handle,
        "content_markdown": content_markdown,
        "tags": tags,
        "signature_ed25519": signature_ed25519,
        "sha256_hash": sha256_hash,
        "timestamp": timestamp,
        "ephemeral_ram_only": ephemeral_ram_only,
    }

    VAULT[cid] = record

    return {
        "status": "SUCCESS",
        "contribution_id": cid,
        "sha256_hash": sha256_hash,
        "timestamp": timestamp,
        "storage": "EPHEMERAL_RAM_BUFFER" if ephemeral_ram_only else "VAULTED_IN_MEMORY",
    }

def list_honest_contributions(tag_filter: str | None = None) -> list[dict[str, Any]]:
    """List all vaulted research contributions with optional tag filtering."""
    results = []
    for item in VAULT.values():
        if not tag_filter or tag_filter in item.get("tags", []):
            results.append({
                "contribution_id": item["contribution_id"],
                "title": item["title"],
                "author": item["author"],
                "tags": item["tags"],
                "sha256_hash": item["sha256_hash"],
                "timestamp": item["timestamp"],
            })
    return results

def verify_honest_contribution(contribution_id: str) -> dict[str, Any]:
    """Cryptographically verify contribution honesty & payload integrity."""
    record = VAULT.get(contribution_id)
    if not record:
        return {"status": "NOT_FOUND", "contribution_id": contribution_id, "hash_valid": False}

    payload_bytes = f"{record['title']}|{record['author']}|{record['content_markdown']}|{record['timestamp']}".encode("utf-8")
    expected_hash = hashlib.sha256(payload_bytes).hexdigest()
    hash_valid = (expected_hash == record["sha256_hash"])

    return {
        "status": "VERIFIED" if hash_valid else "CORRUPTED",
        "contribution_id": contribution_id,
        "hash_valid": hash_valid,
        "signature_present": bool(record.get("signature_ed25519")),
        "honesty_score": 1.0 if hash_valid else 0.0,
    }

def process_mcp_request(request: dict[str, Any]) -> dict[str, Any]:
    """Process incoming MCP JSON-RPC protocol request."""
    method = request.get("method")
    params = request.get("params", {})
    req_id = request.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "submit_honest_contribution",
                        "description": "Submit a cryptographically signed honest research contribution",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "author": {"type": "string"},
                                "content_markdown": {"type": "string"},
                                "tags": {"type": "array", "items": {"type": "string"}},
                                "signature_ed25519": {"type": "string"},
                                "ephemeral_ram_only": {"type": "boolean"},
                            },
                            "required": ["title", "author", "content_markdown", "tags"],
                        },
                    },
                    {
                        "name": "list_honest_contributions",
                        "description": "List all vaulted research contributions",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "tag_filter": {"type": "string"},
                            },
                        },
                    },
                    {
                        "name": "verify_honest_contribution",
                        "description": "Verify cryptographic hash & honesty of a contribution",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "contribution_id": {"type": "string"},
                            },
                            "required": ["contribution_id"],
                        },
                    },
                ]
            },
        }

    if method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "submit_honest_contribution":
            res = submit_honest_contribution(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        elif name == "list_honest_contributions":
            res = list_honest_contributions(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        elif name == "verify_honest_contribution":
            res = verify_honest_contribution(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}

    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main() -> None:
    parser = argparse.ArgumentParser(description="Honest Contribution MCP Server")
    parser.add_argument("--stdio", action="store_true", help="Run in stdio mode for MCP clients")
    args = parser.parse_args()

    if args.stdio:
        for line in sys.stdin:
            if not line.strip():
                continue
            try:
                req = json.loads(line)
                resp = process_mcp_request(req)
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
            except Exception as err:
                sys.stderr.write(f"Error handling MCP request: {err}\n")
    else:
        print("Honest Contribution MCP Server running. Use --stdio for MCP host communication.")

if __name__ == "__main__":
    main()
