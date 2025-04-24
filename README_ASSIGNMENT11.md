# Assignment 11 – Persistence Layer for Shuttle Tracking System

This assignment extends the domain model by implementing a Repository layer to handle data storage and retrieval for domain entities such as `Trip`.

---

## Repository Structure

```
repositories/
├── repository.py                  # Generic Repository interface
├── trip_repository.py             # TripRepository interface extending the generic repository
├── repository_factory.py          # Factory for selecting storage type
├── inmemory/
│   └── inmemory_trip_repository.py  # Working in-memory TripRepository implementation
└── future/
    └── file_trip_repository.py      # Stub for future file-based repository
```

---

## Key Concepts

### Generic Repository Interface
Defined in `repository.py`, includes methods:
- `save()`
- `find_by_id()`
- `find_all()`
- `delete()`

### TripRepository
A specific interface for `Trip` persistence.

### In-Memory Implementation
The `InMemoryTripRepository` stores Trip objects in a dictionary for testing/demo purposes.

### File-Based Stub
The `FileSystemTripRepository` is a placeholder for future file-based storage.  
All methods currently raise `NotImplementedError`.

### Repository Factory
`repository_factory.py` selects the repository based on the chosen storage type:
```python
repo = get_trip_repository("memory")  # or "file"
```

---

## Test Coverage

Unit test file:
- `tests/test_inmemory_trip_repository.py`

Covers:
- Saving a Trip
- Finding by ID
- Listing all Trips
- Deleting a Trip

---

