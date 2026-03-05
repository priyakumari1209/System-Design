# Correctness

## What is correctness?
- Program produces right result regardless of thread timing

## Race Condition
- Two threads read/write shared variable without coordination
- Fix: use locks / synchronized blocks

## Atomic Operations
- Operation that completes fully or not at all
- Use AtomicInteger, AtomicBoolean in Java

## Visibility Problem
- Thread A writes value, Thread B can't see it
- Fix: use volatile keyword (Java) or memory barriers