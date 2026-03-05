# Coordination

## Mutex (Lock)
- Only one thread can hold it at a time
- Use for critical sections

## Synchronized (Java)
- synchronized method or block
- One thread at a time enters

## ReentrantLock
- More flexible than synchronized
- tryLock(), lockInterruptibly()

## Semaphore
- Controls how many threads can access a resource
- Semaphore(3) = max 3 threads at once

## CountDownLatch
- Wait for N threads to finish before proceeding