# Design Principles

## SOLID
- S — Single Responsibility: one class, one job
- O — Open/Closed: open for extension, closed for modification
- L — Liskov Substitution: subclasses must work in place of parent
- I — Interface Segregation: don't force unused methods
- D — Dependency Inversion: depend on abstractions, not concretions

## DRY — Don't Repeat Yourself
- Extract repeated logic into a method or class

## KISS — Keep It Simple, Stupid
- Simplest solution that works wins

## YAGNI — You Aren't Gonna Need It
- Don't build features you don't need yet

## Tell, Don't Ask
- Objects should manage their own state
- Don't get data out and make decisions outside — ask the object to do it