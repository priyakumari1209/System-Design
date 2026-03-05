# Scarcity

## What is Scarcity?
- Limited resources (CPU, memory, DB connections)
- Need to manage fairly and efficiently

## Thread Pool
- Fixed number of threads reused for tasks
- Avoids cost of creating/destroying threads repeatedly
- ExecutorService in Java

## Bounded Queue
- Limits how many tasks wait in the queue
- Prevents memory overflow under high load

## Rate Limiting
- Max N requests per second
- Token bucket / leaky bucket algorithms

## Backpressure
- Tell the producer to slow down when consumer is overwhelmed