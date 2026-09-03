# -*- coding: utf-8 -*-
import json, os

data_path = r"C:\Users\vansh\.gemini\antigravity\scratch\omnicampus-ai\static\data\sample_syllabus.json"

with open(data_path, "r", encoding="utf-8") as f:
    syllabus = json.load(f)

# Add rich structured roadmap tree
syllabus["roadmap"] = {
    "courseTitle": "CS 8803: Distributed Cloud Architectures & Resiliency",
    "totalEstimatedHours": 85,
    "currentMasteryPercent": 25,
    "phases": [
        {
            "id": "phase-1",
            "phaseNumber": 1,
            "title": "Phase 1: Foundations & RPC Primitives",
            "weeks": "Weeks 1-3",
            "color": "indigo",
            "nodes": [
                {
                    "id": "node-101",
                    "title": "Network Models & Socket I/O",
                    "type": "Concept",
                    "status": "Mastered",
                    "hours": 6,
                    "difficulty": "Foundational",
                    "description": "Understanding asynchronous event loops (epoll/kqueue), non-blocking socket I/O, and TCP flow control under latency variance.",
                    "learningObjectives": [
                        "Master TCP socket buffers, head-of-line blocking, and connection pooling",
                        "Implement non-blocking event-driven servers in Python/Node.js"
                    ],
                    "resources": [
                        {"title": "Unix Network Programming (Stevens)", "type": "Book", "url": "https://en.wikipedia.org/wiki/W._Richard_Stevens"},
                        {"title": "Asynchronous I/O Deep Dive", "type": "Video", "url": "https://www.youtube.com/watch?v=aircAruvnKk"}
                    ],
                    "practiceTask": "Build a custom non-blocking HTTP/1.1 server from raw TCP sockets without high-level frameworks."
                },
                {
                    "id": "node-102",
                    "title": "RPC Protocols & Protocol Buffers",
                    "type": "Lab",
                    "status": "Mastered",
                    "hours": 8,
                    "difficulty": "Intermediate",
                    "description": "Binary serialization efficiency (Protobuf vs JSON), gRPC streaming architectures, and dead-letter queue error handling.",
                    "learningObjectives": [
                        "Design robust .proto schema contracts with backward compatibility",
                        "Implement bidirectional streaming gRPC microservices with client-side load balancing"
                    ],
                    "resources": [
                        {"title": "gRPC Core Architecture Docs", "type": "Doc", "url": "https://grpc.io/docs/"},
                        {"title": "Protocol Buffers Spec Guide", "type": "Doc", "url": "https://protobuf.dev/"}
                    ],
                    "practiceTask": "Implement a gRPC key-value service with streaming telemetry and retry backoff."
                }
            ]
        },
        {
            "id": "phase-2",
            "phaseNumber": 2,
            "title": "Phase 2: Consensus & State Machine Replication",
            "weeks": "Weeks 4-7",
            "color": "purple",
            "nodes": [
                {
                    "id": "node-201",
                    "title": "FLP Impossibility & Failure Models",
                    "type": "Theory",
                    "status": "In Progress",
                    "hours": 7,
                    "difficulty": "Advanced",
                    "description": "Formal proof of Fischer-Lynch-Paterson impossibility theorem in asynchronous crash-stop networks and quorum math.",
                    "learningObjectives": [
                        "Understand why synchronous physical clocks cannot guarantee deterministic consensus",
                        "Calculate quorum intersection properties: floor(N/2) + 1"
                    ],
                    "resources": [
                        {"title": "Original FLP Impossibility Paper (1985)", "type": "Paper", "url": "https://dl.acm.org/doi/10.1145/3149.214121"}
                    ],
                    "practiceTask": "Write mathematical proof demonstrating that two majorities in an N-node cluster must intersect by at least 1 node."
                },
                {
                    "id": "node-202",
                    "title": "Raft Consensus Protocol & Election",
                    "type": "Core Milestone",
                    "status": "In Progress",
                    "hours": 14,
                    "difficulty": "Advanced",
                    "description": "Leader election with randomized heartbeats, log entry commit invariants, and cluster membership reconfiguration.",
                    "learningObjectives": [
                        "Implement Follower -> Candidate -> Leader state transition state machine",
                        "Guarantee Raft Log Matching Property and Joint Consensus configuration"
                    ],
                    "resources": [
                        {"title": "In Search of an Understandable Consensus Algorithm (Ongaro & Ousterhout)", "type": "Paper", "url": "https://raft.github.io/raft.pdf"},
                        {"title": "The Secret Lives of Data: Raft Animation", "type": "Interactive", "url": "https://thesecretlivesofdata.com/raft/"}
                    ],
                    "practiceTask": "Implement 3-node Raft election cluster with randomized timeouts in Python or Go."
                }
            ]
        },
        {
            "id": "phase-3",
            "phaseNumber": 3,
            "title": "Phase 3: Midterm Mastery & Distributed Storage",
            "weeks": "Week 8",
            "color": "pink",
            "nodes": [
                {
                    "id": "node-301",
                    "title": "Midterm Exam Comprehensive Synthesis",
                    "type": "Exam Checkpoint",
                    "status": "Not Started",
                    "hours": 10,
                    "difficulty": "Critical",
                    "description": "Comprehensive review of consensus proofs, vector clocks, consistent hashing ring, and quorum read/write thresholds (R + W > N).",
                    "learningObjectives": [
                        "Solve past 3 years midterm exam problems under timed 90-minute conditions",
                        "Derive Amazon Dynamo consistent hashing virtual node partition formulas"
                    ],
                    "resources": [
                        {"title": "Amazon Dynamo Paper (DeCandia et al.)", "type": "Paper", "url": "https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf"}
                    ],
                    "practiceTask": "Simulate consistent hashing ring with 256 virtual nodes per physical worker."
                }
            ]
        },
        {
            "id": "phase-4",
            "phaseNumber": 4,
            "title": "Phase 4: Transactions & High Scalability",
            "weeks": "Weeks 9-13",
            "color": "cyan",
            "nodes": [
                {
                    "id": "node-401",
                    "title": "Two-Phase Commit (2PC) & Saga Pattern",
                    "type": "Architecture",
                    "status": "Not Started",
                    "hours": 10,
                    "difficulty": "Advanced",
                    "description": "Atomic cross-shard transaction coordination, coordinator crash recovery, and asynchronous event-driven Sagas with compensating actions.",
                    "learningObjectives": [
                        "Identify blocking vulnerabilities in 2PC coordinator crashes",
                        "Design orchestrator-based Saga workflows with idempotent rollback APIs"
                    ],
                    "resources": [
                        {"title": "Designing Data-Intensive Applications (Kleppmann)", "type": "Book", "url": "https://dataintensive.net/"}
                    ],
                    "practiceTask": "Build a distributed banking transfer simulation using the Saga compensation pattern."
                },
                {
                    "id": "node-402",
                    "title": "Distributed Caching & Vector Clocks",
                    "type": "Optimization",
                    "status": "Not Started",
                    "hours": 8,
                    "difficulty": "Intermediate",
                    "description": "Cache-aside vs Write-through caching patterns, stampede mitigation with mutexes, and conflict resolution via Vector Clocks.",
                    "learningObjectives": [
                        "Construct causality matrices with vector clock timestamps",
                        "Implement Redis probabilistic early expiration caching"
                    ],
                    "resources": [
                        {"title": "Why Vector Clocks are Easy", "type": "Article", "url": "https://riak.com/posts/technical/vector-clocks-made-easy/"}
                    ],
                    "practiceTask": "Implement a Vector Clock concurrency resolver that detects concurrent writes."
                }
            ]
        },
        {
            "id": "phase-5",
            "phaseNumber": 5,
            "title": "Phase 5: Capstone Chaos Testing & Final Mastery",
            "weeks": "Weeks 14-15",
            "color": "emerald",
            "nodes": [
                {
                    "id": "node-501",
                    "title": "Jepsen Chaos Testing & Fault Injection",
                    "type": "Capstone Lab",
                    "status": "Not Started",
                    "hours": 14,
                    "difficulty": "Mastery",
                    "description": "Network partition injection (split-brain), process kills, clock skews, and linearizability checking against the Raft cluster.",
                    "learningObjectives": [
                        "Detect stale read anomalies and split-brain leadership transitions",
                        "Generate automated Grafana metrics for p99 consensus latency"
                    ],
                    "resources": [
                        {"title": "Jepsen Testing Framework", "type": "Tool", "url": "https://jepsen.io/"}
                    ],
                    "practiceTask": "Execute automated network partition chaos script and verify zero data loss."
                },
                {
                    "id": "node-502",
                    "title": "Final Capstone Project Defense & Exam",
                    "type": "Final Milestone",
                    "status": "Not Started",
                    "hours": 8,
                    "difficulty": "Mastery",
                    "description": "Final codebase presentation, performance benchmark metrics submission, and comprehensive course retrospective.",
                    "learningObjectives": [
                        "Deliver production-ready distributed consensus storage engine",
                        "Achieve 100% curriculum mastery scorecard"
                    ],
                    "resources": [
                        {"title": "OmniCampus Final Retrospective Checklist", "type": "Doc", "url": "#"}
                    ],
                    "practiceTask": "Prepare final system architecture blueprint and 5-minute project demo recording."
                }
            ]
        }
    ]
}

with open(data_path, "w", encoding="utf-8") as f:
    json.dump(syllabus, f, indent=2)

print("Updated sample_syllabus.json with rich Roadmap graph.")
