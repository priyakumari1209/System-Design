# Concurrency Introduction

## What is Concurrency?
- Multiple tasks running at the same time (or appearing to)

## Thread vs Process
- Process: independent program with its own memory
- Thread: lightweight unit inside a process, shares memory

## Why it's hard
- Shared state + multiple threads = unpredictable results

## Key Terms
- Race condition: outcome depends on thread timing
- Deadlock: two threads waiting on each other forever
- Starvation: a thread never gets CPU time