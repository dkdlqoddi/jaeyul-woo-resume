#!/usr/bin/env python3
"""
Aggregate cumulative token usage across Claude Code, OpenAI Codex CLI, and Google Antigravity.
Uses only Python standard library (no external dependencies).
"""

import os
import glob
import json
import sqlite3
import sys

def parse_claude_code():
    stats_path = os.path.expanduser("~/.claude/stats-cache.json")
    if not os.path.exists(stats_path):
        return None

    try:
        with open(stats_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        total_input = 0
        total_output = 0
        total_cache_create = 0
        total_cache_read = 0

        for model, usage in data.get("modelUsage", {}).items():
            total_input += usage.get("inputTokens", 0)
            total_output += usage.get("outputTokens", 0)
            total_cache_create += usage.get("cacheCreationInputTokens", 0)
            total_cache_read += usage.get("cacheReadInputTokens", 0)

        total_all = total_input + total_output + total_cache_create + total_cache_read
        return {
            "name": "Claude Code",
            "input_tokens": total_input,
            "output_tokens": total_output,
            "cached_tokens": total_cache_create + total_cache_read,
            "cache_read": total_cache_read,
            "cache_create": total_cache_create,
            "total_tokens": total_all,
            "pure_tokens": total_input + total_output,
        }
    except Exception as e:
        return {"name": "Claude Code", "error": str(e)}

def parse_codex_cli():
    sessions_dir = os.path.expanduser("~/.codex/sessions")
    if not os.path.exists(sessions_dir):
        return None

    rollout_files = glob.glob(os.path.join(sessions_dir, "**/*.jsonl"), recursive=True)
    seen_responses = set()
    total_input = 0
    total_cached = 0
    total_output = 0
    total_reasoning = 0
    total_all = 0

    for rf in rollout_files:
        try:
            with open(rf, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if "token_usage_record" in line:
                        try:
                            d = json.loads(line)
                            if d.get("type") == "token_usage_record":
                                p = d.get("payload", {})
                                resp_id = p.get("response_id")
                                if resp_id and resp_id in seen_responses:
                                    continue
                                if resp_id:
                                    seen_responses.add(resp_id)
                                u = p.get("usage", {})
                                inp = u.get("input_tokens", 0)
                                cached = u.get("cached_input_tokens", 0)
                                out = u.get("output_tokens", 0)
                                rz = u.get("reasoning_output_tokens", 0)
                                tot = u.get("total_tokens", 0)
                                total_input += inp
                                total_cached += cached
                                total_output += out
                                total_reasoning += rz
                                total_all += tot
                        except:
                            pass
        except:
            pass

    return {
        "name": "Codex CLI",
        "input_tokens": total_input,
        "output_tokens": total_output,
        "cached_tokens": total_cached,
        "reasoning_tokens": total_reasoning,
        "total_tokens": total_all,
        "pure_tokens": total_input - total_cached + total_output,
    }

def decode_varint(data, i):
    val = 0
    shift = 0
    while True:
        b = data[i]
        i += 1
        val |= (b & 0x7F) << shift
        shift += 7
        if not (b & 0x80):
            break
    return val, i

def decode_proto(data):
    fields = []
    i = 0
    n = len(data)
    while i < n:
        key, i = decode_varint(data, i)
        field_num = key >> 3
        wire_type = key & 0x7
        if wire_type == 0:  # varint
            val, i = decode_varint(data, i)
            fields.append((field_num, 'varint', val))
        elif wire_type == 2:  # length-delimited
            length, i = decode_varint(data, i)
            val = data[i:i + length]
            i += length
            fields.append((field_num, 'bytes', val))
        elif wire_type == 1:  # 64-bit
            val = data[i:i + 8]
            i += 8
            fields.append((field_num, '64bit', val))
        elif wire_type == 5:  # 32-bit
            val = data[i:i + 4]
            i += 4
            fields.append((field_num, '32bit', val))
        else:
            break
    return fields

def parse_antigravity():
    conv_dir = os.path.expanduser("~/.gemini/antigravity-cli/conversations")
    if not os.path.exists(conv_dir):
        return None

    db_files = glob.glob(os.path.join(conv_dir, "*.db"))
    total_input = 0
    total_cached = 0
    total_output = 0
    total_thinking = 0
    total_response = 0

    for db in db_files:
        try:
            con = sqlite3.connect(db)
            cur = con.cursor()
            rows = cur.execute("SELECT metadata FROM steps WHERE step_type=15;").fetchall()
            for (meta,) in rows:
                if not meta:
                    continue
                try:
                    fields = decode_proto(meta)
                    f9 = [v for k, t, v in fields if k == 9]
                    if f9:
                        sub = decode_proto(f9[0])
                        vdict = {k: v for k, t, v in sub if t == "varint"}
                        total_input += vdict.get(2, 0)
                        total_output += vdict.get(3, 0)
                        total_cached += vdict.get(5, 0)
                        total_thinking += vdict.get(9, 0)
                        total_response += vdict.get(10, 0)
                except:
                    pass
            con.close()
        except:
            pass

    total_all = total_input + total_cached + total_output
    return {
        "name": "Antigravity",
        "input_tokens": total_input,
        "output_tokens": total_output,
        "cached_tokens": total_cached,
        "thinking_tokens": total_thinking,
        "total_tokens": total_all,
        "pure_tokens": total_input + total_output,
    }

def main():
    print("=" * 72)
    print("  AI Coding Agents Cumulative Token Usage Aggregator")
    print("=" * 72)

    claude = parse_claude_code()
    codex = parse_codex_cli()
    antigravity = parse_antigravity()

    tools = [t for t in [claude, codex, antigravity] if t and "error" not in t]

    grand_total_tokens = sum(t["total_tokens"] for t in tools)
    grand_output_tokens = sum(t["output_tokens"] for t in tools)
    grand_pure_tokens = sum(t["pure_tokens"] for t in tools)

    print(f"\n{'Tool':<18} | {'Total Tokens (inc. cache)':<25} | {'Pure Output Tokens':<18}")
    print("-" * 72)
    for t in tools:
        print(f"{t['name']:<18} | {t['total_tokens']:>22,} | {t['output_tokens']:>18,}")
    print("-" * 72)
    print(f"{'Grand Total':<18} | {grand_total_tokens:>22,} | {grand_output_tokens:>18,}")
    print("-" * 72)

    print(f"\n[Summary for Resume]")
    print(f"- Total Context & Prompt Tokens Processed : {grand_total_tokens:,} (~{grand_total_tokens / 1e9:.2f}B+ tokens)")
    print(f"- Pure Generative Output & Reasoning     : {grand_output_tokens:,} (~{grand_output_tokens / 1e6:.1f}M+ tokens)")
    print(f"- Net Input + Output (excl. cache read)   : {grand_pure_tokens:,} (~{grand_pure_tokens / 1e6:.1f}M+ tokens)")
    print("=" * 72)

if __name__ == "__main__":
    main()
